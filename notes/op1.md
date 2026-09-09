# OP1 — Canonical quaternionic Farey structure

Home: QGA Chapter 3. Status: **open**.

Until OP1 is settled, “quaternionic Farey” is a family of Models. OP2–OP4 inherit that ambiguity. The companion generator may use \(w(q\mid q')\) as an exogenous catalog kernel. It cannot claim that kernel is Hatcher’s Farey lift.

Sources: `~/Projects/qga/book/03_gauged_hopf_lattice.md` §3.2, §3.5; `notes/open_problems.md`; `lib/hopf_lattice.py`. Equivariance diagnostic: Chapter 4, Exercise 4.H.

Claim labels: bundle, linking, and the 24 Hurwitz units are **Theorem**. Every adjacency / mediant helper in the book library is a **Model candidate**.

## Statement

Prove uniqueness, or classify the reasonable choices, of discrete adjacency / mediant rules on a gauged Hopf lattice
\[
(\Lambda,\;h(\Lambda),\;E_{\parallel},\;E_{\perp},\;\mathcal{G})
\]
such that all four hold (Ch. 3 §3.5):

1. **Farey reduction.** Under a fixed embedding \(\mathbb{Q}\cup\{\infty\}\hookrightarrow\) lattice or base, the graph specialises to the classical Farey diagram: \(a/c\sim b/d\) iff \(|ad-bc|=1\).
2. **Gauge equivariance.** Left and right unit multiplications send edges to edges (or a classified failure mode is written down).
3. **Continued-fraction paths.** Discrete walks refine approximants, including walks that advance along fibers.
4. **Optional Euclidean property.** A greedy / shortest-path rule recovers mediants the way Farey neighbors do.

Appendix success criteria: an equivariant rule, a documented Farey reduction, and a comparable mediant algorithm.

The book’s own warning: without a primary rule, the phrase is a metaphor.

## What is already theorem (not OP1)

Do not “solve” these again:

- Hurwitz units \(\Lambda_{0}=\mathcal{H}\cap S^{3}\) (24 points); 24-cell / \(D_{4}\) geometry (`notes/hurwitz.md`).
- 24-cell 1-skeleton \(\neq\) Hopf \(C_{4}\) graph on those vertices.
- Hopf map used in the repo,
  \[
  h(z_{1},z_{2})=\bigl(2\mathrm{Re}(\overline{z_{1}}z_{2}),\;2\mathrm{Im}(\overline{z_{1}}z_{2}),\;|z_{1}|^{2}-|z_{2}|^{2}\bigr),
  \]
  constant on the structure-group action \((z_{1},z_{2})\mapsto(e^{i\phi}z_{1},e^{i\phi}z_{2})\).
- Linking of distinct fibers (Hopf invariant 1).

OP1 is only the discrete incidence structure sitting on that bundle.

Representation theory of \(2T=\mathcal{H}^{\times}\) (`notes/2T.md`) is classical input: left action permutes \(\Lambda_{0}\), along-fiber \(C_{4}\)-cycles are \(\{q,iq,-q,-iq\}\), and \(2T\)-invariant graphs exist. Invariance is the cheap half of criterion 2. It does not pick \(\lvert ad-bc\rvert=1\), a mediant, or an embedding of \(\mathbb{Q}\).

## Classical target

Hatcher / Farey:

- Vertices: \(\mathbb{P}^{1}(\mathbb{Q})=\mathbb{Q}\cup\{\infty\}\).
- Edge: \(a/c\sim b/d\) iff \(|ad-bc|=1\).
- Mediant: \(\frac{a}{c}\oplus\frac{b}{d}=\frac{a+b}{c+d}\), the unique simplest interpolant.
- \(SL(2,\mathbb{Z})\) acts, preserves adjacency, and the diagram is the 1-skeleton of the modular triangulation of the hyperbolic plane.

A quaternionic rule has to say what plays the role of each of those four lines. That is the content of OP1.

## Why it is not automatic

Three independent obstructions.

**Noncommutativity.** The naive lift \(|ad-bc|=1\) needs a \(2\times 2\) determinant. Over \(\mathbb{H}\) that is a Dieudonné determinant (or a complex-pair minor). Exercise 3.F offers two probes, neither adopted:

\[
\bigl|N(q_{1}\overline{q_{2}}-q_{2}\overline{q_{1}})\bigr|
\qquad\text{or a }2\times 2\text{ minor from }(z_{1},z_{2}).
\]

**The extra circle.** Classical Farey lives in a 2-real-dimensional base. The Hopf total space has an \(S^{1}\) fiber with no Farey analogue. Any complete rule must decide \(E_{\parallel}\) (phase neighbors on a fiber) separately from \(E_{\perp}\) (lifts of base neighbors). Criterion 3 insists that continued-fraction walks be allowed to run along fibers; a base-only Delaunay graph on \(S^{2}\) fails that on purpose.

**Which embedding of \(\mathbb{Q}\)?** “Reduce to Farey under a fixed embedding \(\mathbb{Q}\cup\{\infty\}\hookrightarrow\) lattice/base” is part of the problem, not an input. On \(\Lambda_{0}\) the three unital planes \(i,j,k\) (`notes/hurwitz.md`, Reading A) are the first list: report three Farey scores, do not average them. Starred planes \(i^{\ast},j^{\ast},k^{\ast}\) are orthogonal complements, not copies of \(\mathbb{C}\) through \(1\). \(\Lambda_{0}\cap\mathrm{span}\{1,i\}\) is four roots of unity, not \(\mathbb{Q}\); Gaussian Farey (`notes/gaussian_farey.md`) lives on \(\mathbb{Z}[i]\), off the unit sphere, with adjacency \(\alpha\delta-\gamma\beta\in\{1,-1,i,-i\}\). That is a lattice-in-the-plane theorem. The 24-cell is a sphere fact. Glueing them is OP1. Different embeddings give different “the” reductions. Classification, not uniqueness, may be the honest theorem.

A fiber-aware candidate may take \(E_{\parallel}\) as a union of some of the six coordinate \(C_{4}\)s (QGA’s \(h\) uses the \(i\)-square only) and \(E_{\perp}\) from half-integer / 24-cell edges that leave those planes. That labeling is not a Farey theorem. Extra rays that make \(2O\) or \(F_{4}\) are Reading B: a new Model, not an upgrade of \(\Lambda_{0}\).

Left vs right makes this sharper. Left multiplication by a Hurwitz unit permutes \(\Lambda_{0}\) exactly and preserves the multiset \(h(\Lambda_{0})\). Right multiplication by a general unit moves fibers. A rule that is left-equivariant need not be right-equivariant. Exercise 4.H treats recorded failures as constraints on admissible rules, not as bugs to hide.

## The current candidate (sandbox, not the answer)

`lib.hopf_lattice.candidate_adjacency` is labeled **Model candidate only**. Module docstring: every adjacency / mediant helper is an OP1 candidate. There is no implemented mediant.

It returns two edge lists, using Hopf angle charts \((\eta,\xi_{1},\xi_{2})\),

\[
q=(\cos\eta\cos\xi_{1},\;\cos\eta\sin\xi_{1},\;\sin\eta\cos\xi_{2},\;\sin\eta\sin\xi_{2}).
\]

| Piece | Rule | Defaults |
| --- | --- | --- |
| \(E_{\parallel}\) | nearly equal \((\eta,\xi_{1})\), neighboring binned \(\xi_{2}\) | \(\eta\)-tol \(0.08\), \(\xi_{1}\)-tol \(0.08\), \(8\) phase bins |
| \(E_{\perp}\) | angular distance of Hopf images on \(S^{2}\) below a cutoff, excluding \(\xi_{2}\)-circle pairs | \(0.45\) rad |

The function’s own warning: the \(\xi_{2}\)-circle is **not** the structure-group fiber \((z_{1},z_{2})\mapsto(e^{i\phi}z_{1},e^{i\phi}z_{2})\). For a true fiber, call `sample_structure_group_fiber` / `common_phase`. Mixing those two circles is how a figure can look like Chapter 2 while implementing a different \(S^{1}\).

Flux helpers (`discrete_flux_cycle`, `transform_flux`) assume some edge set already exists; they do not choose it.

Diagnostic: `adjacency_equivariance_score(points, unit, side="L"|"R")` reports the fraction of along-fiber and inter-fiber edges whose images remain edges of the same type after left or right multiplication. That is the Exercise 4.H meter. It is not a theorem that the score is \(1\).

Two lattices must not be conflated:

- \(\Lambda_{0}\): 24 Hurwitz units — arithmetic object.
- \(\Lambda_{\mathrm{ang}}=\)`sample_angle_lattice` — a software grid in angle space, explicitly not an order.

A rule that looks clean on \(\Lambda_{\mathrm{ang}}\) can fail to be an automorphism of \(\Lambda_{0}\), and conversely.

## What a solution has to produce

Four objects, not a plot.

1. **Vertex set.** A precise discrete set: all of \(\Lambda_{0}\), a tower \(\Lambda_{n}\) of Hurwitz (or Lipschitz) points of bounded denominator, or a defined rational subset of the base with chosen lifts.
2. **Adjacency predicate.** A yes/no rule, preferably algebraic (norm / Dieudonné det / matrix minor), not a floating threshold. Threshold graphs on \(S^{2}\) will not specialise to \(|ad-bc|=1\).
3. **Mediant.** An operation \(\oplus\) on adjacent vertices whose restriction to the embedded Farey diagram is \((a/c)\oplus(b/d)=(a+b)/(c+d)\), or a proof that no such \(\oplus\) exists and a classified replacement.
4. **Equivariance statement.** For which \(u\in S^{3}\) (left, right, or only \(\Lambda_{0}\)) the predicate is preserved; if only a subgroup, name the subgroup.

Optional but in the problem list: a greedy algorithm on the graph that recovers the mediant path.

Exercise 3.H is the first experimental cut: take `candidate_adjacency`, pick one 2D slice, and write down one failed Farey reduction. The book expects negative reports.

## Design space the book already names

Other candidates, against the same four criteria:

- spherical Delaunay / geodesic neighbors on \(h(\Lambda)\subset S^{2}\), then a gauge choice of lift;
- Hurwitz-norm determinants / Exercise 3.F minors;
- geodesic mediants in \(S^{3}\);
- structure-group sampling for \(E_{\parallel}\) instead of the \(\xi_{2}\)-chart.

Each will fail at least one of: exact Farey specialisation, left-right equivariance, along-fiber continued fractions. The classification theorem is “these families, with these failure modes,” even if no unique winner exists.

## Downstream lock

| Later object | Why it waits on OP1 |
| --- | --- |
| OP2 flux-topograph axioms | Separators live on edges. No canonical \(E\), no canonical river. |
| OP3 Magic Island \(\leftrightarrow\) class number | Needs a reduced-form / class theory on that graph. |
| OP4 \(Z\mapsto\) uniqueness | “The” flywheel is a cycle on \(E\). |
| OP6 flywheel composition | Composition is an operation on classes of cycles. |
| Helicoid–catenoid \(\mathrm{Q}_{\mathrm{C}}\) | Jump kernel is a sum over \(q'\sim q\). That \(\sim\) is OP1. |

## Present state

| Layer | Status |
| --- | --- |
| Bundle, linking, 24 units, left action permutes \(\Lambda_{0}\) | known (Theorem) |
| One chart-based threshold graph plus an equivariance score | implemented (Model candidate) |
| Predicate that reduces to \(\lvert ad-bc\rvert=1\) | not known |
| Mediant | not known |
| Which gauge subgroup must preserve edges | not known |

Allowed conclusion today: several Models exist.

Forbidden conclusion: “the” quaternionic Farey diagram.

The central combinatorial object of the book is still a candidate.
