# My Progress — AI Engineering from Scratch

> Personal learning tracker. Flip `[ ]` → `[x]` as you finish each lesson.
> Full lesson lists per phase live in [ROADMAP.md](ROADMAP.md).

**Started:** 2026-07-03
**Path:** Full curriculum, Phase 0 → 19 (ground-up build)
**Placement:** 9/10 — skip-eligible from Phase 11, but choosing the complete foundation.

---

## Summary

| Metric | Value |
|---|---|
| Total scope | ~1,094.5 hrs · 20 phases · 503 lessons |
| Done so far | ~6.75 hrs (Phase 0 setup + Phase 1 · L1) |
| Current | Phase 1 · Math Foundations — Lesson 1 done |
| Next up | Phase 1 · Lesson 2 — Vectors, Matrices & Operations |

**Pace reference** — learning (Phases 0–18, ~475h) / everything (incl. capstones, ~1,095h):
- 10 hrs/wk → ~11 months / ~2.1 years
- 20 hrs/wk → ~5.5 months / ~1 year

---

## Phases

Legend: `[x]` done · `[~]` in progress · `[ ]` not started · 🎯 placement: skip-eligible · ⚠️ placement: review

- [~] **Phase 0 — Setup & Tooling** · 6/12 · ~14h · *cum 14h* — 🚧 see lesson detail below
- [~] **Phase 1 — Math Foundations** · 1/22 · ~23h · *cum 37h* · 🎯 ← **in progress**
- [ ] **Phase 2 — ML Fundamentals** · 0/18 · ~21h · *cum 58h* · ⚠️ review (Random Forest / hyperparameters)
- [ ] **Phase 3 — Deep Learning Core** · 0/13 · ~15h · *cum 73h* · 🎯
- [ ] **Phase 4 — Computer Vision** · 0/28 · ~27h · *cum 100h* · 🎯
- [ ] **Phase 5 — NLP: Foundations to Advanced** · 0/29 · ~30h · *cum 130h* · 🎯
- [ ] **Phase 6 — Speech & Audio** · 0/17 · ~18h · *cum 148h* · 🎯
- [ ] **Phase 7 — Transformers Deep Dive** · 0/16 · ~14h · *cum 162h* · 🎯
- [ ] **Phase 8 — Generative AI** · 0/15 · ~14h · *cum 176h* · 🎯
- [ ] **Phase 9 — Reinforcement Learning** · 0/12 · ~13h · *cum 189h* · 🎯
- [ ] **Phase 10 — LLMs from Scratch** · 0/24 · ~26h · *cum 215h* · 🎯
- [ ] **Phase 11 — LLM Engineering** · 0/17 · ~17h · *cum 232h* ← placement entry point
- [ ] **Phase 12 — Multimodal AI** · 0/25 · ~65h · *cum 297h*
- [ ] **Phase 13 — Tools & Protocols** · 0/23 · ~24.5h · *cum 321.5h*
- [ ] **Phase 14 — Agent Engineering** · 0/42 · ~42h · *cum 363.5h*
- [ ] **Phase 15 — Autonomous Systems** · 0/22 · ~20h · *cum 383.5h*
- [ ] **Phase 16 — Multi-Agent & Swarms** · 0/25 · ~28h · *cum 411.5h*
- [ ] **Phase 17 — Infrastructure & Production** · 0/28 · ~32h · *cum 443.5h*
- [ ] **Phase 18 — Ethics, Safety & Alignment** · 0/30 · ~31h · *cum 474.5h*
- [ ] **Phase 19 — Capstone Projects** · 0/85 · ~620h · *cum 1094.5h* — portfolio track, pull from over time

---

## Phase 0 — lesson detail

- [x] 01 · Dev Environment — Python 3.12.13, Node 26, git ✓ *(Rust not installed — optional)*
- [ ] 02 · Git & Collaboration — ~45 min ← **do next** (tool ready; learn the branch/commit/PR workflow)
- [ ] 03 · GPU Setup & Cloud — ~75 min *(defer — API-based path, no local GPU yet)*
- [x] 04 · APIs & Keys — Anthropic key + `.env` wired in ✓
- [x] 05 · Jupyter Notebooks — installed in venv ✓ *(run `jupyter lab` to use)*
- [x] 06 · Python Environments — `.venv` via uv ✓
- [ ] 07 · Docker for AI — ~75 min *(defer — not installed; first needed at Phase 11·L13)*
- [x] 08 · Editor Setup — Claude Code ✓
- [ ] 09 · Data Management — ~75 min
- [x] 10 · Terminal & Shell — ✓
- [ ] 11 · Linux for AI — ~45 min *(defer — you're on macOS)*
- [ ] 12 · Debugging & Profiling — ~75 min

**Left before Phase 1:** lessons 02, 09, 12 (~3.25h). Lessons 03, 07, 11 are deferrable (~3.25h).

---

## How to use

1. Each work session: `cd` into the repo, then `source .venv/bin/activate` and `set -a; source .env; set +a`.
2. Finish a lesson → change its `[ ]` to `[x]` and bump the phase fraction (e.g. `6/12` → `7/12`).
3. End of a phase → run `/check-understanding <phase>` to self-test before advancing.
4. Starting a new phase → ask me (or copy from [ROADMAP.md](ROADMAP.md)) to expand its lessons into checkboxes here.
5. Keep this file out of git if you want: `echo 'MY_PROGRESS.md' >> .gitignore`.

---

## Session log

### 2026-07-05
- Covered: Phase 1 · Lesson 1 — Linear Algebra Intuition (all concept segments; ran `vectors.py`; NumPy one-liners; PyTorch autodiff)
- Supplements: angle_between, is_independent/rank (row-reduction traces), gram_schmidt
- Stopped at: **lesson complete** — resume at Phase 1 · Lesson 2 (Vectors, Matrices & Operations)
