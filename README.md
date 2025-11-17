# Highlights → Stories Mini‑Builder (Tech‑agnostic Scaffold)

This project loads real football match event data, extracts highlight-worthy moments using simple heuristics, and generates a Storyteller-compatible story.json that can be viewed using the provided preview tool.

**Goal**
Take `data/match_events.json` and convert it into a complete Story Pack that includes:
- A cover page
- Several highlight pages (ranked by heuristics)
- A closing info page
- Valid structure following Storyteller’s JSON format

## Features Implemented

Python CLI **(src/cli.py)** that builds a full story pack
Highlight scoring:
- Goals & penalty goals = 5
- Attempt saved / blocked / post = 4
Highlights sorted by:
- score (desc)
- minute (asc)
Minute parsing supports:
- 9
- 90'+3'
Fallbacks for missing fields and defensive parsing
Optional image selection using asset_descriptions.json
Schema-compatible story: cover → highlights → info summary

## How to Run
From the project root: run python `src/cli.py` in the terminal
This generates the output here: `out/story.json`

## How to run the preview (no server needed)
1) Open `preview/index.html` in your browser.
2) Click "Load pack.json" and select the file from `out/`.

## Repository layout
assets/                   # images used for optional highlights
data/match_events.json    # input match feed
out/story.json            # generated story pack
src/builder.py            # story-building logic
src/cli.py                # CLI entry point
preview/index.html        # story viewer

AI_USAGE.md               # how AI was used
DECISIONS.md              # design choices & reasoning
EVALS.md                  # optional evaluations

## Key Features

- Parses real match feed (nested JSON structure)
- Generates highlight slides with ranking heuristics
- Supports added time (`90'+3'`)
- Image selection heuristics using asset metadata
- Schema-valid story structure
- Clear reasoning and documented decisions

## Extending

With more time, I would extend:

- Player name resolution using squad files  
- Stronger matching between events and images  
- Optional captions generated using AI  
- Unit tests for parsing & scoring 

# Status

The solution fully meets the task requirements and is ready for review.







