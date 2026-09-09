# Notes

Companion note to QGA, typeset in `tex/`. Figures in `fig/`.

Write under `tex/` and `notes/` only unless asked.

The mix `Q = Q_O + σ(Z) Q_C` is a **Model**.
It is not a theorem of quaternion orders, Hopf, or topographs.
Those remain the QGA spine: https://github.com/kinaar8340/qga

Use upright \(\mathrm{O}\) and \(\mathrm{C}\) in macros (`\QO`, `\QC`)
so \(Q_O p\) cannot be read as \(Q\circ p\).
The vector field is always \(O[\Psi]\), never a bare \(Op\) that can be
misread as \(Qp\).

## Claim labels

| Label | Meaning |
| --- | --- |
| Theorem | arithmetic/geometry already in the QGA spine |
| Model | this dynamics (not a theorem) |
| Hypothesis | observational — do not mix into the generator |
| Spine fact | input from QGA/Hatcher, not a lemma about \(Q\) |

## Four words (operational)

| Word | Object |
| --- | --- |
| life | continuous transport `Q_O` |
| catalog | jump kernel `Q_C` (gain−loss already inside) |
| correction | map `C: (p, e) → (σ', w')` from error `e = A[p] − A*` |
| alignment | a named functional `A[p]` that correction is supposed to restore |

Life-drift \(D(\sigma,t)=\mathrm{KL}(p_t^\sigma\|p_t^0)\) is not alignment.

Ranked roles are dropped from the note. They are not maps of `p`.
No equation for \(Z\) in this note.

## Cheap lemmas (internal to the Model)

1. Mass: `∫ Qp = 0`
2. Markov: `Q*1 = 0`; jump piece is Kolmogorov forward under `w≥0`, `σ≥0`.
   Semigroup existence is not claimed.

Hopf remainder is a **Spine fact**, not a lemma about \(Q\).

## Protocol S1

Open-loop. `C` is defined in §1 and unused. Closed loop is S2, not written.

Fix a density, freeze `O` and `w`, freeze `Z`, sweep `σ`.
Report dominance `r`, life-drift `D`, named alignment `A`.
`σ_*` is the gate at which the jump term dominates.

The S1 plot in `fig/s1-sweep.png` is a circle (generic Ψ-space).
Helicoid/catenoid are pictures of the split, not the configuration manifold.

Script: `notes/s1_sweep.py`.

## Spine and dictionary (not extra sections of the PDF)

| File | Role |
| --- | --- |
| `notes/op1.md` | Canonical quaternionic Farey: open; `candidate_adjacency` is a Model candidate, not the answer |
| `notes/2T.md` | Binary tetrahedral group: irreps, McKay \(\widetilde{E}_6\); does not solve OP1 |
| `notes/hurwitz.md` | 24-cell / \(D_4\); six planes on the same 24 vertices; \(F_4\)-rays are a different Model |
| `notes/gaussian_farey.md` | Theorem on \(\mathbb{Z}[i]\): unit-det graph, Picard octahedra; not \(\Lambda_0\), not quaternionic Farey |
| `notes/hopf.md` | Hopf remainder as spine: QGA's one map, local triviality, no global section, left vs right circles |
| `notes/quaternions.md` | Algebra first: product, conjugate, norm, units, \(\mathbb{C}^2\); not orders, not \(Q\) |
| `notes/rotations.md` | Conjugation \(v\mapsto q v\bar q\), not Hopf; SLERP and attitude stay out of the PDF |
| `notes/construct.md` | Arena / loader / scene / gate / lens as a reading of the four operational words |
| `notes/post.md` | Three frames, not the PDF |

The companion note still uses the Hopf fiber as a diagram, not extra symbols.
`X_O(q)=iq` is the **right-invariant** generator of left common-phase on QGA's `h`.
The left-invariant field `q ↦ qi` is the other circle (`q i q̄`) and is not used.
Attitude kinematics is the same side-of-product bookkeeping, not the same field:
body-rate `ω` is a general element of `Im H`, not `i`. Do not write `X_O` as
the attitude kinematic field.

Three invisibilities: `{q,-q}` (conjugation); the left common-phase circle (`h`);
the right circle (`q i q̄`).

## Do not put in the generator or this note

- 350/π
- Magic Island numerics
- pulsar coincidences
- ranked roles
- a unique \(A\)
- a diffusion term
- an equation for \(Z\)
- Protocol S2
- SLERP, MEKF, attitude kinematics as a name for `X_O`
- a Farey theorem for \(q'\sim q\) (that is QGA OP1; the kernel is exogenous)
- the 24-cell as Hatcher's modular diagram
- a 5120-face geodesic icosahedron as a stand-in for \(\Lambda_0\)
- six fiber fields \(i,i^*,j,j^*,k,k^*\) in \(Q\)
- \(F_4\)-rays / \(2O\) as a silent upgrade of \(\Lambda_0\)
- the six-plane coloring as a quaternionic Farey diagram
- “\(\Lambda_0\) carries Gaussian Farey” or “Picard octahedra are the 24-cell”
