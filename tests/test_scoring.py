from src.builder import build_story_pack

def test_goal_scored_creates_highlight():
    events = [
        {"type": "goal", "minute": 50, "playerRef1": "Player A", "comment": "Nice goal!"}
    ]

    story = build_story_pack(events)
    highlight = story["pages"][1]

    assert highlight["type"] == "highlight"
    assert "GOAL" in highlight["headline"]
