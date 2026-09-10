# Arena

Spine: [`qga`](https://github.com/kinaar8340/qga) — manuscript + pedagogical Python  
Shared math: [`flux_hopf_lib`](https://github.com/kinaar8340/flux_hopf_lib)  
Engine: [`qga_engine`](https://github.com/kinaar8340/qga_engine) · [`qga_gpu`](https://github.com/kinaar8340/qga_gpu)  
This repo: labeled dynamics Model + HUD. Not theorems. Do not grow a second book.

Companion note to QGA, plus a playable HUD demo.

Catalog needs the life. The life is not the catalog.

The book's spine is quaternion orders, Hopf, topographs:
https://github.com/kinaar8340/qga

The mix `Q = Q_O + σ(Z) Q_C` is a labeled **Model**. It is not a theorem
about number theory, and it is not part of the Hatcher lift.

v0 also ships a HUD. It is not a complete framework.
Do not import the TOE manuscript. Do not claim completeness.

## Companion note (LaTeX)

```
cd tex && latexmk -pdf -interaction=nonstopmode main.tex
```

Output: `tex/main.pdf`.

The note:

1. Defines life, catalog, correction, alignment operationally.
2. Proves the cheap lemmas (mass, Markov). Hopf remainder is a spine fact, not a lemma about `Q`.
3. Uses the Hopf fiber as a diagram (base `S^2` catalog-visible, fiber `S^1` remainder).
4. States Protocol S1 (open-loop): fix a density, freeze `Z`, sweep `σ`, report when the jump term dominates. Closed loop is S2, not written.
5. Drops ranked roles (not operational in the generator).
6. Keeps `350/π`, Magic Islands, and pulsar coincidences out.

| File | Role |
| --- | --- |
| `tex/main.tex` | Companion note |
| `tex/scope.tex` | Not a QGA theorem |
| `tex/words.tex` | Four words, operationally |
| `tex/notation.tex` | One notation sheet |
| `tex/formal_full_object.tex` | Helicoid–catenoid Model |
| `tex/lemmas.tex` | Mass, Markov, Hopf remainder |
| `tex/qga_full_object.tex` | Same Model, Hopf stage |
| `tex/protocol.tex` | Protocol S1 (`σ`-sweep), open-loop |
| `fig/formal-full-object.png` | Formal plate |
| `fig/qga-full-object.png` | QGA plate |
| `fig/fiber-diagram.png` | Hopf fiber (post frame) |
| `fig/s1-sweep.png` | S1 plot: `r(σ,T)`, `A[p]`, mark `σ_*` |

Generator is always `Q = Q_O + σ(Z) Q_C` (plus, not minus).
`Q_C` already contains gain−loss. Lens is `∂p/∂t`.

Claim labels follow https://github.com/kinaar8340/qga :

- **Theorem** = arithmetic/geometry already in the QGA spine
- **Model** = this dynamics (not a theorem)
- **Hypothesis** = observational (do not mix into the generator)

See `notes/README.md`.

## HUD

Gold on black instrument. Inject four faults (clock drift, denied leak, frozen pointer, R4 split). CORRECT until residual dies. Or HOLD eight times and watch adaptation take a rank.

Never a sealed happy state: leak = 0 is rejected; pointer ≡ life is rejected.

The HUD still uses ranked roles. The companion note does not.

Python ≥ 3.12. From this directory:

```
python3 -m pytest tests/test_correct.py
python3 -m arena.server
```

Open http://127.0.0.1:8765

`pytest` is the only extra: `pip install pytest` or `pip install -e ".[dev]"`.

The HUD prints claim labels. The mix is **Model**. Runtime import of `toe` / `hfb` / `mystery` is refused.

Geometry libraries are MIT. Several VQC repos are PolyForm Noncommercial plus patent notice US 63/913,110. This repo is MIT.
