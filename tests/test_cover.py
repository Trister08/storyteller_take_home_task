from src.builder import build_story_pack

def test_cover_exists():
    story = build_story_pack([])
    assert story["pages"][0]["type"] == "cover"