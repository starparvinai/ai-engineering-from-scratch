# Supplements — Linear Algebra Intuition

Personalized extra explanations captured during tutoring, beyond `en.md`. These are the
parts that needed a second, slower pass.

---

## `angle_between` (code) — 2026-07-05

```python
def angle_between(self, other):
    import math
    cos_theta = self.cosine_similarity(other)   # dot / (|a|*|b|)
    cos_theta = max(-1.0, min(1.0, cos_theta))  # clamp to [-1, 1]
    return math.degrees(math.acos(cos_theta))
```

It's just the **dot product turned into an actual angle**. Cosine similarity returns a
number in `[-1, 1]`; `acos` inverts it into the angle; `degrees` converts radians → degrees.

- The `max(-1, min(1, ...))` **clamp** is defensive: floating-point rounding can produce
  `1.0000000002`, and `math.acos` **crashes** on inputs outside `[-1, 1]`.
- Sanity check: `[1,0]` vs `[0,1]` → 90° (perpendicular, dot=0), vs `[1,1]` → 45°, vs
  itself → 0°. Same "alignment" idea as the dot product, expressed in degrees.

---

## `is_independent` & `rank` — the shared row-reduction engine — 2026-07-05

**Both functions run the same algorithm: Gaussian elimination that counts pivots.** The
pivot count *is* the rank. `is_independent` just returns `rank == n`.

### What rank means
Rank = **how many rows are genuinely new** vs. secretly combinations of the others. The
algorithm hunts down redundant rows and watches them **collapse to all-zeros**. Survivors
= independent directions = rank. The core move is the school-math operation "subtract a
multiple of one row from another" — it never changes the rank but exposes redundancy.

### The recipe (plain English)
Sweep **columns left → right**. In each column:
1. **Find a pivot** — a not-yet-used row with a nonzero entry in this column.
2. No pivot? This column adds nothing new → **skip**.
3. Pivot found? **Use it to zero out this column in every other row.**
4. **Count it** (`r += 1`).

At the end, `r` = number of pivots = **rank**.

### Annotated code
```python
def rank(self):
    rows = [row[:] for row in self.rows]  # working copy
    m, n = self.shape                     # m rows, n cols
    r = 0                                 # pivots found so far (= the answer)
    for col in range(n):                  # sweep columns L→R
        pivot = None                      # step 1: find a pivot in rows r..m-1
        for row in range(r, m):
            if abs(rows[row][col]) > 1e-10:   # "nonzero" within float tolerance
                pivot = row
                break
        if pivot is None:                 # step 2: no pivot → skip column
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]     # bring pivot up to row r
        scale = rows[r][col]
        rows[r] = [x / scale for x in rows[r]]          # make pivot entry = 1
        for row in range(m):                            # step 3: clean col elsewhere
            if row != r and abs(rows[row][col]) > 1e-10:
                factor = rows[row][col]
                rows[row] = [rows[row][j] - factor*rows[r][j] for j in range(n)]
        r += 1                            # step 4: count it
    return r
```

### Trace 1 — `[[1, 2], [2, 4]]` → rank 1
Start `r=0`:
```
row0:  1  2
row1:  2  4
```
**col 0:** pivot = row0 (`1`). scale=1 (row0 unchanged). Clean row1: factor=2 →
`[2−2·1, 4−2·2] = [0, 0]` (collapsed). `r→1`:
```
row0:  1  2
row1:  0  0     ← row1 was 2×row0, so it vanished
```
**col 1:** search rows 1..1 → row1 is `[0,0]`, no nonzero → skip.
Result: **rank 1**.

### Trace 2 — `{e1, e2, 2·e1+e2}` → rank 2 (this is the `is_independent(...) = False` demo)
Start `r=0`:
```
row0:  1  0  0
row1:  0  1  0
row2:  2  1  0     ← = 2·row0 + row1
```
**col 0:** pivot = row0. Clean: row1 has 0 (skip); row2 factor=2 →
`[2−2, 1−0, 0−0] = [0,1,0]`. `r→1`:
```
row0:  1  0  0
row1:  0  1  0
row2:  0  1  0
```
**col 1:** search rows 1..2 → pivot = row1 (`1`). Clean: row0 has 0 (skip); row2 factor=1 →
`[0, 1−1, 0] = [0,0,0]` (collapsed). `r→2`:
```
row0:  1  0  0
row1:  0  1  0
row2:  0  0  0     ← dependent row gone
```
**col 2:** search rows 2..2 → row2 is `[0,0,0]`, no nonzero → skip.
Result: **rank 2**. Then `is_independent` checks `rank == n` → `2 == 3` → **False**.

### Why counting pivots works
A pivot row introduces a direction **no earlier row could reach**. A row that's a
combination of earlier rows gets fully cancelled by the subtractions the earlier pivots
trigger, so it ends as **all zeros and never becomes a pivot**. Pivots = independent rows.

---

## `gram_schmidt` — 2026-07-05

```python
def gram_schmidt(vectors):
    orthonormal = []
    for v in vectors:
        w = v
        for u in orthonormal:            # for each basis vector already built...
            proj = w.project_onto(u)     # ...find w's shadow along u
            w = w - proj                 # ...and subtract it off
        if w.magnitude() < 1e-10:        # nothing left → v was dependent, skip
            continue
        orthonormal.append(w.normalize())  # scale to length 1, keep it
    return orthonormal
```

It's the **projection idea applied repeatedly to manufacture perpendicularity**. For each
new vector `v`: subtract off everything pointing along the vectors you already have
(`w - w.project_onto(u)`), which leaves a `w` perpendicular to all of them; if `w` shrank
to ~0 then `v` was dependent (skip it); otherwise normalize to length 1 and keep it.

That's why the output has every pair `uᵢ·uⱼ ≈ 0` (mutually perpendicular) and every
`|uᵢ| ≈ 1` (unit length) — the definition of an **orthonormal basis**. Since each stored
`u` is already unit-length, `project_onto`'s `(w·u / u·u)·u` has `u·u = 1`.
