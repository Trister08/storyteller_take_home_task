from datetime import datetime
import json
import os

# ================================================================
# Load asset metadata (image descriptions)
# ================================================================
ASSET_FILE = "asset_descriptions.json"
ASSET_DIR = "assets"

if os.path.exists(ASSET_FILE):
    with open(ASSET_FILE, "r") as f:
        ASSET_DATA = json.load(f).get("assets", [])
else:
    ASSET_DATA = []


# ================================================================
# Event scoring
# ================================================================
def score_event(event):
    etype = event.get("type", "").lower()
    comment = event.get("comment", "").lower()

    # High-value events
    if etype == "goal":
        return 5
    if etype == "penalty goal":
        return 5
    if "goal!" in comment:
        return 5

    # Strong attacking highlights
    if etype in ["penalty won", "post", "attempt saved", "attempt blocked"]:
        return 4

    # Medium importance
    if etype in ["yellow card", "corner", "free kick won"]:
        return 2

    return 0


# ================================================================
# Parse minute (supports 90'+3', 45'+2', etc.)
# ================================================================
def parse_minute(raw_minute, period=None):
    if raw_minute is None:
        return 0

    # Try direct integer
    try:
        return int(raw_minute)
    except:
        pass

    s = str(raw_minute)

    # Base minute until first non-digit
    base_digits = ""
    for c in s:
        if c.isdigit():
            base_digits += c
        else:
            break

    if base_digits == "":
        return 0

    base = int(base_digits)

    # Added time e.g. 90'+3'
    if "+" in s:
        extra_part = s.split("+")[1]
        extra_digits = "".join(c for c in extra_part if c.isdigit())
        if extra_digits:
            return base + int(extra_digits)

    return base


# ================================================================
# Pick an image for a given event type (simple heuristics)
# ================================================================
def pick_image_for_event(event_type):
    et = event_type.lower()

    # Heuristic matching based on description keywords
    for asset in ASSET_DATA:
        desc = asset.get("description", "").lower()

        if "goal" in et and ("goal" in desc or "celebrates" in desc or "scores" in desc):
            return f"../assets/{asset['filename']}"

        if "penalty" in et and "penalty" in desc:
            return f"../assets/{asset['filename']}"

        if "blocked" in et and "blocked" in desc:
            return f"../assets/{asset['filename']}"

        if "saved" in et and "saved" in desc:
            return f"../assets/{asset['filename']}"

        if "post" in et and "post" in desc:
            return f"../assets/{asset['filename']}"

    # fallback: first available image
    if ASSET_DATA:
        return f"../assets/{ASSET_DATA[0]['filename']}"

    return "../assets/placeholder.png"


# ================================================================
# Build highlight slides
# ================================================================
def build_highlight_slides(events):
    highlights = []

    for event in events:
        if not isinstance(event, dict):
            continue

        etype = event.get("type", "").lower()

        # Ignore end events
        if etype.startswith("end "):
            continue

        score = score_event(event)
        if score == 0:
            continue

        minute = parse_minute(event.get("minute"), event.get("period"))
        player = event.get("playerRef1", "")
        comment = event.get("comment", "")

        highlights.append({
            "type": "highlight",
            "minute": int(minute),
            "headline": f"{etype.upper()} — {player}",
            "caption": comment,
            "image": pick_image_for_event(etype),
            "explanation": f"{etype}={score}"
        })

    # Sort:
    # 1) score DESC
    # 2) minute ASC
    highlights.sort(
        key=lambda x: (
            -int(x["explanation"].split("=")[1]),
            int(x["minute"])
        )
    )

    return highlights


# ================================================================
# Build final story pack
# ================================================================
def build_story_pack(events):
    highlights = build_highlight_slides(events)

    pages = []

    # ------------------------------------------------------------
    # Cover page
    # ------------------------------------------------------------
    cover_image = "../assets/placeholder.png"
    if ASSET_DATA:
        cover_image = f"../assets/{ASSET_DATA[0]['filename']}"

    pages.append({
        "type": "cover",
        "headline": "Celtic vs Kilmarnock — Highlights",
        "image": cover_image
    })

    # ------------------------------------------------------------
    # Highlight pages
    # ------------------------------------------------------------
    if len(highlights) == 0:
        pages.append({
            "type": "info",
            "headline": "No Highlights",
            "body": "There were no major highlight-worthy events."
        })
    else:
        pages.extend(highlights)

    # ------------------------------------------------------------
    # End-of-match info page
    # ------------------------------------------------------------
    pages.append({
        "type": "info",
        "headline": "Full-time",
        "body": "End of match summary."
    })

    # ------------------------------------------------------------
    # Construct final story JSON
    # ------------------------------------------------------------
    story = {
        "story_id": "celtic_kilmarnock_" + datetime.now().strftime("%Y%m%d_%H%M%S"),
        "title": "Top Moments — Celtic vs Kilmarnock",
        "pages": pages,
        "metrics": {
            "goals": sum(
                1 for e in events
                if isinstance(e, dict)
                and e.get("type") in ["goal", "penalty goal"]
            ),
            "highlights": len(highlights)
        },
        "source": "../data/match_events.json",
        "created_at": datetime.utcnow().isoformat() + "Z"
    }

    return story
