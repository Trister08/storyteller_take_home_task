import json
from builder import build_story_pack

def main():
    # Load raw JSON
    with open("data/match_events.json", "r") as f:
        raw = json.load(f)

    # Extract events from nested structure
    events = raw["messages"][0]["message"]

    # Build final story
    story = build_story_pack(events)

    # Output
    with open("out/story.json", "w") as f:
        json.dump(story, f, indent=2)

    print("✔ Story Pack created at out/story.json")

if __name__ == "__main__":
    main()
