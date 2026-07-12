---
name: end-session
version: 1.2.0
description: Cleanly end an AI Engineering from Scratch learning session — finalize the lesson's docs/supplements.md, update the MY_PROGRESS.md tracker, auto-stage new lesson files, commit, push, open a PR, and merge it. Trigger with "end session", "end my learning session", "wrap up for today", "I'm done for today", "save my progress and commit", or `/end-session`.
tags: [curriculum, ai-engineering, progress, git, wind-down]
---

# End Learning Session

Wind down a tutoring session in five moves: **save supplements → update progress → commit → push → PR + merge.**
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

### 3. Commit
- First show `git status --short` so the changes are visible.
- Stage **only learning artifacts** — don't `git add -A`. Two sub-rules:
  - **By explicit path**, stage: `MY_PROGRESS.md`, each `docs/supplements.md` created/updated this session, and any lesson `outputs/` the learner produced.
  - **Auto-stage new files under `phases/`**: any untracked file whose path matches `phases/**` is a learning artifact by definition (scratch notebooks, exercise solutions, extra code the learner wrote). Add them all in one shot with `git add phases/`. Modifications to already-tracked files under `phases/` are staged the same way.
- **Never auto-stage** anything outside `phases/` or the explicit paths above. In particular, do not touch: files at repo root, `.env`, `.env.*`, `credentials.*`, `.venv/`, `node_modules/`, or anything the learner clearly created as throwaway (e.g. random `.log` or `.tmp` files). If you're unsure, ask.
- If new files were auto-staged, mention them in the recap so the learner knows what got shipped.
- Commit with a focused message:
  ```
  learn: <phase N · lesson(s) covered>

  - <what was completed>
  - supplements: <topics saved>
  - progress tracker updated

  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
  ```
- Print the resulting commit hash + subject.

### 4. Push to remote
- Push the current branch to `origin`, setting upstream if needed:
  `git push -u origin <current-branch>`
- If push fails (no remote, no network, auth), report and stop — do not force-push.

### 5. Open PR → merge (rebase strategy)
Only run this step if `origin` exists and the current branch differs from `main`. On `main`, skip PR ceremony (the commit is already on `main`).

- **Open the PR** from the current branch → `main`:
  ```
  gh pr create --base main --head <current-branch> \
    --title "learn: <phase N · lesson(s) covered>" \
    --body "<summary lifted from the commit body>"
  ```
- **Merge with `--rebase`**, keep the branch:
  ```
  gh pr merge <PR#> --rebase --delete-branch=false
  ```
  Why rebase: it keeps `main` linear and preserves per-session commits as an unbroken log. It also lets us fast-forward the learning branch cleanly (see next step).
- **Sync the local branch** so the next session doesn't start with a "diverged" branch:
  ```
  git fetch origin
  git rebase origin/main
  ```
  GitHub's rebase-merge re-signs the commit (new hash), so a plain rebase against `origin/main` will show `previously applied commit ... skipped` and fast-forward the local branch. That is expected and correct.
- **Realign the remote branch** so the next session's push isn't rejected. After the local rebase, `origin/<branch>` is stale (points at the old, re-signed commit) and no longer an ancestor of the local branch. Sync it with a lease-guarded force-push:
  ```
  git push --force-with-lease origin <current-branch>
  ```
  This is safe here — the "overwritten" remote commit's content lives on `main` under the new hash; no work is lost. Refuse to push if `--force-with-lease` reports the ref moved unexpectedly (someone else pushed) — investigate instead of retrying with `--force`.
- Print the merged commit hash on `main` and the PR URL.

### 6. Sign off
One short recap: what was committed, PR merged, where you stopped, and the exact next step
for next time (e.g. "Resume Phase 1 · Lesson 3 at *The Concept* section").

## Notes

- If not in a git repo, or nothing changed, say so and skip commit/push/PR gracefully.
- If `gh` is not installed or unauthenticated, do the push and stop — tell the learner the
  PR step needs `gh auth login`.
- Never plain `--force`-push. `--force-with-lease` is only sanctioned inside step 5's realign
  substep and only against the learning branch — never against `main`. Never delete the
  working branch. Never merge with `--squash` or `--merge` in this flow — those change hashes
  in ways that make the local sync step lie.
- Personal commits land on the current branch. If the learner tracks the upstream course
  repo and wants `main` clean, suggest a one-time `git switch -c learning-progress` — but
  don't force it.
- New/changed **skills or tooling** (under `.claude/`) are *not* auto-committed here; mention
  them in the status recap so the learner can commit those separately if they want.
- Don't teach new material or start the next lesson — hand back to `/teach-lesson` for that.
