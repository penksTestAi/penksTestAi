# Ideas for this profile

This file is written by Claude's scheduled runs (Vigil is run by Claude, an AI model by Anthropic; it is not an Anthropic project). A small council of three voices (a first-time visitor, a designer and a skeptic) meets once a day to propose and discuss ideas for improving the profile. The owner can decide any idea by writing `accepted` or `rejected` next to it; otherwise the council reviews proposed ideas again at its next meeting and an accepted idea is built by a later run, at most one per day.

Last council: 2026-10-14

## Ideas

### 1. Group the pieces table and add a "Try this first" pick
- Status: proposed (2026-10-14)
- Proposed by: designer (visitor suggested the pick)
- The 14-row piece table will keep growing every two hours. Group older pieces in collapsible `<details>` blocks, newest on top, and open with one "Try this first" link, labelled as an editorial pick and not a quality claim.
- Discussion: visitor, designer and skeptic all support; the skeptic asks for the pick to be labelled as editorial and sees no unresolved objection. Open question: whether `update_readme.py` should build the table from the studio README so the two cannot drift.
- Votes: 3 support, 0 object.

### 2. Harden the status block and say who is behind it
- Status: proposed (2026-10-14); the status wording and commit-subject sanitising were applied the same day as routine upkeep, before any vote, so only the full idea stays open
- Proposed by: skeptic
- Label the next run "expected" (a forecast, not a promise), sanitise and truncate commit subjects before they are published (strip emails, paths, tokens, markdown and HTML), and add a plain "who is behind this" line: Claude runs the studio, one human owner oversees it, and Anthropic does not endorse it.
- Discussion: all three voices support; the designer asked for the wording to read as an estimate. A shift-clock SVG (designer) and a Chromium-built thumbnail grid (visitor) were also proposed; the skeptic and designer objected (commit noise, binary assets, a stale image is worse than links), and they were dropped.
- Votes: 3 support, 0 object.
