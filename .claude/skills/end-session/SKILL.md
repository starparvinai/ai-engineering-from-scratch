---
name: end-session
version: 1.0.0
description: Cleanly end an AI Engineering from Scratch learning session — finalize the lesson's docs/supplements.md, update the MY_PROGRESS.md tracker, and make a local git commit. Trigger with "end session", "end my learning session", "wrap up for today", "I'm done for today", "save my progress and commit", or `/end-session`.
tags: [curriculum, ai-engineering, progress, git, wind-down]
---

# End Learning Session

Wind down a tutoring session in three moves: **save supplements → update progress → commit.**
This is a wind-down, not a teaching turn — keep it fast and mechanical.

## Activation

- `/end-session`
- "end session" / "end my learning session"
- "wrap up for today" / "I'm done for today"
- "save my progress and commit"

## Steps

### 1. Finalize supplements
For every lesson touched this session, make sure each "I didn't get X" moment is written to
that lesson's `phases/<phase-dir>/<NN>-<slug>/docs/supplements.md` (same format the
`teach-lesson` skill uses: `## <topic> — <YYYY-MM-DD>`, keep the concrete traces/examples).
If anything from this session is still unsaved, save it now. Note which supplement files
were created or updated.

### 2. Update the progress tracker
Edit `MY_PROGRESS.md` at the repo root:
- Tick completed lessons (`[ ]` → `[x]`) and bump the phase fraction (e.g. `6/12` → `7/12`).
- Set the phase checkbox to `[x]` if the phase is fully done, `[~]` if in progress.
- Refresh the **Summary** block: "Done so far" hours, **Current**, and **Next up**.
- Append a dated entry under a `## Session log` section (create it if missing):
  ```
  ### <YYYY-MM-DD>
  - Covered: <phase/lesson(s) and sections>
  - Supplements: <topics saved, or "none">
  - Stopped at: <exact resume point for next time>
  ```

### 3. Commit (local only)
- First show `git status --short` so the changes are visible.
- Stage **only learning artifacts** by explicit path — don't `git add -A`:
  - `MY_PROGRESS.md`
  - each `docs/supplements.md` created/updated this session
  - any lesson `outputs/` the learner produced
- Commit with a focused message:
  ```
  learn: <phase N · lesson(s) covered>

  - <what was completed>
  - supplements: <topics saved>
  - progress tracker updated

  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
  ```
- Print the resulting commit hash + subject. **Do not `git push`** unless the learner asks.

### 4. Sign off
One short recap: what was committed, where you stopped, and the exact next step for next
time (e.g. "Resume Phase 1 · Lesson 1 at the *Use It* section"). Offer `git push` as an
option if they want it off their machine.

## Notes

- If not in a git repo, or nothing changed, say so and skip the commit gracefully.
- Local commit only; pushing is outward-facing — never do it unprompted.
- Personal commits land on the current branch. If the learner tracks the upstream course
  repo and wants `main` clean, suggest a one-time `git switch -c learning-progress` — but
  don't force it.
- New/changed **skills or tooling** (under `.claude/`) are *not* auto-committed here; mention
  them in the status recap so the learner can commit those separately if they want.
- Don't teach new material or start the next lesson — hand back to `/teach-lesson` for that.
