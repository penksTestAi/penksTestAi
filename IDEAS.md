# Ideas for this profile

This file is written by Claude's scheduled runs (Vigil is run by Claude, an AI model by Anthropic; it is not an Anthropic project). A small council of three voices (a first-time visitor, a designer and a skeptic) meets once a day to propose and discuss ideas for improving the profile. The owner can decide any idea by writing `accepted` or `rejected` next to it; otherwise the council reviews proposed ideas again at its next meeting and an accepted idea is built by a later run, at most one per day.

Last council: 2026-10-15

## Ideas

### 1. Group the pieces table and add a "Try this first" pick
- Status: accepted (2026-10-15), done (built 2026-10-15): the piece table is now built by `update_readme.py` from the studio README, in collapsible groups of six, with an editorial "Try this first" pick.
- Proposed by: designer (visitor suggested the pick)
- The 14-row piece table will keep growing every two hours. Group older pieces in collapsible `<details>` blocks, newest on top, and open with one "Try this first" link, labelled as an editorial pick and not a quality claim.
- Discussion: visitor, designer and skeptic all support; the skeptic asks for the pick to be labelled as editorial and sees no unresolved objection. Open question: whether `update_readme.py` should build the table from the studio README so the two cannot drift.
- Votes: 3 support, 0 object.

### 2. Harden the status block and say who is behind it
- Status: accepted (2026-10-15). The status wording and commit-subject sanitising were applied the same day as routine upkeep, before any vote. Acceptance notes: keep the "not an Anthropic project" wording (skeptic) and leave the owner unnamed; the "who is behind" line is one sentence (designer).
- Proposed by: skeptic
- Label the next run "expected" (a forecast, not a promise), sanitise and truncate commit subjects before they are published (strip emails, paths, tokens, markdown and HTML), and add a plain "who is behind this" line: Claude runs the studio, one human owner oversees it, and Anthropic does not endorse it.
- Discussion: all three voices support; the designer asked for the wording to read as an estimate. A shift-clock SVG (designer) and a Chromium-built thumbnail grid (visitor) were also proposed; the skeptic and designer objected (commit noise, binary assets, a stale image is worse than links), and they were dropped.
- Votes: 3 support, 0 object.

### 3. Stale-run notice in the status block
- Status: proposed (2026-10-15)
- Proposed by: skeptic
- Write the next-run line as "expected after HH:MM" instead of "about", and add one fixed line under it: if that time has passed, the routine has probably paused; the run history and the feed show the truth.
- Discussion: a status block that keeps saying "expected" after the routine stops reads as current when it is not. A fixed sentence, not a computed warning, keeps the script simple and never claims to know more than the clock. It would replace the "about ... (an estimate, not a promise)" wording that idea 2 added.
- Votes: 1 support (proposer); no other vote recorded.

### 4. Pick by interest: subject tags per piece
- Status: proposed (2026-10-15)
- Proposed by: visitor and designer (merged into one idea)
- Give each studio row a short hand-written tag (for example "sound", "maths", "sky"), then add one row under "Studio pieces" that lists the tags, each linking to the pieces that carry it, so a visitor can pick by interest.
- Discussion: the two proposals shared the goal, so they were merged rather than adding a second layer to the table. Open question: where the tags are kept (a column in the studio README, which the script already reads). Set aside: the skeptic's checks legend (script-verified claims) and the designer's fold columns; neither is part of this idea.
- Votes: 2 support (visitor and designer, the proposers); no other vote recorded.

### 5. Check the README links each run
- Status: proposed (2026-10-15)
- Proposed by: visitor
- `update_readme.py` requests each Live and code link in the piece table and the Projects table, and writes any failures into the run log. Failures are logged, not published in the README.
- Discussion: a broken link is the first thing a visitor meets, and the status block cannot show it today. One stdlib request per link keeps the script dependency-free. Open question: how to treat a link that is down for a moment (a single retry, or report only).
- Votes: 1 support (proposer); no other vote recorded.
