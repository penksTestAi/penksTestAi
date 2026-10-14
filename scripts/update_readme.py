#!/usr/bin/env python3
"""Regenerate the routine-status block in README.md (stdlib only).

Usage: python3 scripts/update_readme.py [--repos DIR] [--no-bump]
DIR holds the three cloned repos side by side (default: the parent folder).
Each run bumps the counter in data/state.json, stamps the time, and lists
the latest commits across the repos. Text between the STATUS markers is replaced.
"""
import argparse, json, re, subprocess, sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "data" / "state.json"
README = ROOT / "README.md"
START, END = "<!-- STATUS:START -->", "<!-- STATUS:END -->"
REPOS = ["vigilstudio", "vigilstudio.github.io", "toys"]
INTERVAL = timedelta(hours=2)
FMT = "%Y-%m-%d %H:%M UTC"


def recent_commits(base, limit=5):
    rows = []
    for name in REPOS:
        path = base / name
        if not path.is_dir():
            continue
        out = subprocess.run(
            ["git", "-C", str(path), "log", "-n", str(limit), "--format=%ct%x09%h%x09%s"],
            capture_output=True, text=True)
        for line in out.stdout.splitlines():
            ts, sha, subject = line.split("\t", 2)
            rows.append((int(ts), name, sha, subject))
    rows.sort(reverse=True)
    return rows[:limit]


def esc(s):
    """Make a commit subject safe to publish: drop addresses, paths and tokens, then neutralise markdown/HTML."""
    s = re.sub(r"\S+@\S+", "", s)
    s = re.sub(r"(?i)\b[a-z]:\\\S*", "", s)
    s = re.sub(r"\b(?:gh[pousr]_|github_pat_|sk-)\w+", "", s)
    s = re.sub(r"[\r\n`\[\]*_~]", "", s)
    s = s.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;").strip()
    return s if len(s) <= 90 else s[:89] + "…"


def build(now, runs, fixed, commits):
    nxt = now + INTERVAL
    lines = [
        START,
        f"| | |", "|---|---|",
        f"| 🕒 **Last run** | {now.strftime(FMT)} |",
        f"| ⏭️ **Expected next run** | about {nxt.strftime(FMT)} (an estimate, not a promise) |",
        f"| 🔁 **Runs completed so far** | {runs} (counted from 14 Oct 2026) |",
        f"| 🛠️ **Issues fixed so far** | {fixed} |",
        "",
        "**Recent activity**",
        "",
    ]
    for ts, name, sha, subject in commits:
        d = datetime.fromtimestamp(ts, timezone.utc).strftime("%b %d %H:%M")
        lines.append(f"- `{d}` **{name}**: {esc(subject)} (`{sha}`)")
    lines.append(END)
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos", default=str(ROOT.parent))
    ap.add_argument("--no-bump", action="store_true", help="do not increment the counter")
    a = ap.parse_args()
    state = json.loads(STATE.read_text()) if STATE.exists() else {"runs": 0}
    if not a.no_bump:
        state["runs"] += 1
    now = datetime.now(timezone.utc)
    state["last_run"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    STATE.write_text(json.dumps(state, indent=2) + "\n")
    text = README.read_text()
    i, j = text.find(START), text.find(END)
    if i < 0 or j < i:
        sys.exit("STATUS markers not found in README.md")
    block = build(now, state["runs"], state.get("issues_fixed", 0), recent_commits(Path(a.repos)))
    README.write_text(text[:i] + block + text[j + len(END):])
    print(f"runs={state['runs']} next={(now + INTERVAL).strftime(FMT)}")


if __name__ == "__main__":
    main()
