# DECISIONS

This document outlines the key trade-offs and reasoning behind my implementation.

---

## Heuristic and ranking

I used a simple, explainable scoring model:

- `goal` and `penalty goal` → **5 points**
- `penalty won`, `post`, `attempt saved`, `attempt blocked` → **4 points**
- `yellow card`, `corner`, `free kick won` → **2 points**

This allowed me to group events into tiers without over fitting to any particular match.

Sorting is done by:

1. score descending  
2. minute ascending  

This produces “most important first, then earlier first” ordering, similar to highlight packages in sports apps.

---

## Data handling (duplicates, missing fields, out-of-order minutes)

Real-world match feeds are inconsistent, so I added the following protections:

- **Minute parsing** supports formats like `"90'+3'"`, `"45'+2'"`, and plain `"26"`.  
- **End events** (`"end 2"`, `"end 14"`) are skipped entirely.  
- **Non-dict entries** are ignored defensively.  
- All minutes are stored as **integers** to guarantee correct sorting.
- Events without players or comments still produce valid highlight pages.

---

## Pack structure and invariants

I followed the story schema requirements:

- Always include a **cover** page.  
- Always include at least one additional page (either highlight or fallback info page).  
- Always append a simple **full-time summary** page.  
- Ensure required top-level fields:  
  `story_id`, `title`, `pages`, `source`, `created_at`.

Pages never violate schema fields (`type`, `headline`, etc.).

---

## Image handling

The assets folder included multiple images and a description file.  
I implemented lightweight heuristics that map event types to images based on keywords (e.g., “goal”, “saved”, “blocked”, “penalty”).  
If no match is found, I use the first asset as a fallback.

This is intentionally simple but adds value to the story visually.

---

## What I would do with 2 more hours

- Improve image selection using fuzzy matching or player-specific lookups.
- I would make the website more responsive and on mobile phones when I inspected it on the web broswer, I saw it is not responsive on phones.
- I would also make it more visually pleasing because due to time, I couldn't fix the images not showing in the preview.
- Add tests for minute parsing and scoring.  
- Use the squad files to replace `playerRef1` with actual player names.  
- Add stronger error messages for unexpected JSON structures.

