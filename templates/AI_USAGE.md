# AI USAGE

This take-home task allowed the use of AI assistants. I used AI in a targeted and transparent way to speed up parts of the workflow while keeping final reasoning and verification entirely manual.

---

## Where AI helped

- **Understanding the task structure and constraints**  
  I used AI to summarise the problem and clarify expected outputs such as story structure, page requirements, and invariants.

- **Brainstorming heuristics for ranking events**  
  I generated initial ideas for scoring goals, penalty events, and attacking highlights.  
  I refined these heuristics myself to keep them simple and explainable.

- **Drafting helper functions**  
  AI assisted with early versions of utility functions like minute parsing and simple text matching for choosing images.

- **JSON schema alignment checks**  
  AI helped me confirm that my generated `story.json` followed the required shape (`story_id`, `pages`, `created_at`, etc.).

---

## Prompts or strategies that worked

- Asking for **“simple, explainable heuristics suitable for a junior solution”** helped avoid overly complex logic.
- Requesting **“edge cases I should test manually”** helped me catch issues such as:
  - added-time formats (`90'+2'`)
  - end-period events
  - non-highlight event types
- Using AI to **review partial code**, not generate full modules, helped keep my implementation clean and readable.

---

## Verification steps (tests, assertions, manual checks)

I verified the output in 3 ways:

1. **Manual inspection of `story.json`**  
   - minutes stored as integers  
   - valid page types (`cover`, `highlight`, `info`)  
   - explanations included for ranked highlights  
   - correct source and timestamps  

2. **Preview via `preview/index.html`**  
   - checked that the story rendered  
   - ensured cover page appeared  
   - validated ordering of highlights and correct captions  

3. **Ad-hoc assertions during development**  
   - printed intermediate parsed minutes  
   - counted number of goals & highlight-worthy events  
   - validated image filename selection

These checks ensured correctness beyond AI-generated suggestions.

---

## Cases where I chose **not** to use AI and why

- **Final ranking logic**  
  I designed and implemented the actual sorting myself so I could explain it clearly during review.

- **Minute parsing**  
  AI provided starting points, but I finished the logic manually because real data included edge formats that required careful reasoning.

- **Image selection heuristics**  
  I intentionally kept these simple and personally authored the rules so they reflected my own understanding.

Overall, AI accelerated my steps, but the core reasoning, decisions, and verification were my own.

-
