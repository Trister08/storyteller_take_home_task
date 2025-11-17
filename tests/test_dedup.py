from src.builder import build_story_pack

def test_no_duplicate_highlights():
    events = [
        {"type": "goal", "minute": 10, "player": "A"},
        {"type": "goal", "minute": 10, "player": "A"},
    ]

    pack = build_story_pack(events)
    highlights = [s for s in pack["slides"] if s["type"] == "highlight"]

    assert len(highlights) == 1
