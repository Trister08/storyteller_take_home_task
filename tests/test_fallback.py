from src.builder import build_story_pack

def test_fallback_added_when_no_highlights():
    events = [
        {"type": "foul", "minute": 10, "playerRef1": "X", "comment": ""}
    ]

    story = build_story_pack(events)

    fallback_page = story["pages"][1]
    assert fallback_page["type"] == "info"
    assert "No Highlights" in fallback_page["headline"]
