# Arena

Demo HUD for a research skeleton:
ranked roles + incompleteness dynamics + Alignment that must be corrected.

## Mission

Typeset a short companion note to QGA, not a chapter of it.

The book's spine is quaternion orders, Hopf, topographs:
https://github.com/kinaar8340/qga

The helicoid–catenoid mix
`Q = Q_O + σ(Z) Q_C`
is a labeled **Model**. It is not a theorem about number theory, and it is
not part of the Hatcher lift. Put it in `tex/` as a companion note
(Part V appendix tone) so it cannot be read as a QGA theorem.

Claim labels follow https://github.com/kinaar8340/qga :
- Theorem = arithmetic/geometry already in the QGA spine
- Model = this dynamics (not a theorem)
- Hypothesis = observational (do not mix into the generator)

The note must:
1. Define four words operationally, one page: life, catalog, correction, alignment.
2. Drop ranked roles from the note (not operational in the generator).
3. Prove the cheap lemmas internal to the Model:
   ∫ Qp = 0; Q*1=0 and the jump piece is Kolmogorov forward.
   Hopf remainder is a Spine fact (input), not a lemma about Q.
   Those sentences are the content of
   “the catalog cannot prove it captured the life.”
4. Use the Hopf fiber as a diagram, not extra symbols:
   base S^2 catalog-visible, fiber S^1 the remainder.
5. State Protocol S1 as open-loop: fix a density, freeze Z (no equation for Z),
   sweep σ, report r(σ,T) and a named A[p]. C is unused; closed loop is S2.
   Life-drift D=KL(p^σ||p^0) is not alignment.
6. Keep 350/π, Magic Islands, pulsar coincidences out.

## Do

- Write files under `tex/` and `notes/` only unless asked.
- Keep one notation sheet. Do not revive Φ once Ψ or q is chosen.
- Q_O is life/helicoid (or X_O on S^3). Q_C is catalog/catenoid (or lattice jumps).
- Generator is ALWAYS Q = Q_O + σ(Z) Q_C (plus, not minus).
- Q_C already contains gain−loss. Never put an extra minus on the catalog lobe.
- Intersection / lens is ∂p/∂t (or ∂p(q,t)/∂t), never a third operator.
- Preserve: ∫ Qp = 0, and in QGA also N(q)=1 and flywheel Hopf linking.
- Z is coarse: σ(Z) is a parameter of the fast generator.

## Do not

- Do not call the dynamics a Theorem.
- Do not invent 350/π or Magic Island numerics into the generator.
- Do not change symbol meaning across the two objects.
- Do not import ranked roles into the companion note unless they are
  defined operationally as maps of p.
- Do not let the Model be read as a theorem about quaternion orders.

## Build

Work only in `~/Projects/arena`.

```
cd tex && latexmk -pdf -interaction=nonstopmode main.tex
```

Keep:

```
tex/main.tex
tex/preamble.tex
tex/scope.tex
tex/words.tex
tex/notation.tex
tex/formal_full_object.tex
tex/lemmas.tex
tex/qga_full_object.tex
tex/protocol.tex
fig/.gitkeep
```

If `fig/qga-full-object.png` or `fig/formal-full-object.png` exist, `\includegraphics` them; otherwise use a tikz placeholder caption "place exported slide here".

## Origin

- Visual theme from Aaron's shadow-as-theory Venn (gold on black).
- Structure from Cankay cavity roles, promoted to ranked roles (HUD only).
- Law: catalog needs the life; the life is not the catalog.
- Motto: Without correction, adaptation takes control.
  The companion note treats this as Protocol S1, not as a slogan.
- Related work: https://github.com/kinaar8340 (kingdom_come, qga, flux_hopf_lib)
- This repo is a NEW project. Do not import the TOE manuscript. Do not claim completeness.

## Stack for v0

- Python 3.12 engine (sim only).
- Static HUD: one HTML page, vanilla JS, no React unless the plan justifies it.
- Tiny local server (stdlib or FastAPI) so the HUD can POST inject/correct.
- No Hugging Face, no GPU, no Gradio for v0 (Gradio fights a HUD look).
- CPU only. Runs with `python -m arena.server` from repo root.

## Theme (non-negotiable)

- Background #0b0b0b. Ink #e8d5a3 / #c4a35a. Muted #8a7a55. Danger #c45c4a. Ok #7a9a6a.
- Typography: old-style serif titles + monospace readouts.
- Copy voice: short, exact, no marketing. Use the words catalog, life, shadow, leak, pointer, correction, adaptation.
- Banner: WARNING COGNITIVE DISSONANCE AHEAD
- Never draw a closed, sealed system as the happy state.

## Domain model (HUD only; do not rename)

Alignment A = [time, coupling, leak, global_pointer]
Ranks R1 ≺ R2 ≺ R3 ≺ R4 ≺ R5
  R1 lattice-waveguide
  R2 energy surfaces
  R3 near-field network
  R4 identity shell
  R5 boundary-scaffold
Admissible set A-star:
  |t-t*| <= eps_t
  |c-c*| <= eps_c
  ell_min <= leak <= ell_max
  pointer is a proper subset of life (never identical)

The companion note does not use this rank list.
Its alignment is a named functional A[p] of the density.

## Correction

HUD:
- Measure residuals dt, dc, dℓ, dp from rank observations.
- Classify first match: frozen pointer | denied leak | runaway leak | unlock | clock drift | admissible.
- Act at the lowest competent rank.
- Reject writes that set leak == 0 or pointer ≡ life.
- If the same fault persists N=8 steps, raise ADAPTATION_RISK, then lock-in or terminal.

Companion note:
- Correction is a map C: (p, e) → (σ', w') with e = A[p] − A*.
- Adaptation is not a success state. Protocol S1 reports when the jump term dominates.

Plan first, build second. No extra features in v0.
