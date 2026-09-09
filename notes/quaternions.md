# Quaternion algebra (stage, not the generator)

Hamilton’s quaternions are the unique 4-dimensional real division algebra (up to isomorphism). They are the stage QGA uses. They are not yet the generator \(Q\).

This note lays out the algebra first — product, conjugate, norm, units — then the identifications QGA actually uses. Orders and the helicoid–catenoid generator are not mixed in.

QGA sources: `~/Projects/qga/book/01_quaternions.md`, `02_hopf.md`. Fiber field lock: `notes/hopf.md`. Rotation conjugation (a different map): `notes/rotations.md`.

Claim labels: algebra and \(S^{3}\to\mathrm{SO}(3)\) are **Theorem** (classical). \(\mathrm{X}_{\mathrm{O}}(q)=iq\) is **Model**. Lipschitz / Hurwitz orders are QGA spine, not this file.

## The algebra \(\mathbb{H}\)

A quaternion is

\[
q = w + xi + yj + zk,\qquad w,x,y,z\in\mathbb{R},
\]

with Hamilton’s rules

\[
i^{2}=j^{2}=k^{2}=ijk=-1.
\]

Those force the cyclic products and the sign flips:

\[
ij=k,\; jk=i,\; ki=j,
\qquad
ji=-k,\; kj=-i,\; ik=-j.
\]

Addition is componentwise. Multiplication is associative and distributive, **not commutative**. As a real vector space, \(\mathbb{H}\cong\mathbb{R}^{4}\) with basis \(\{1,i,j,k\}\).

Explicit product: if \(q_{1}=w_{1}+x_{1}i+y_{1}j+z_{1}k\) and \(q_{2}=w_{2}+x_{2}i+y_{2}j+z_{2}k\),

\[
\begin{aligned}
q_{1} q_{2}
&=
(w_{1} w_{2} - x_{1} x_{2} - y_{1} y_{2} - z_{1} z_{2})\\
&\quad+(w_{1} x_{2} + x_{1} w_{2} + y_{1} z_{2} - z_{1} y_{2})\,i\\
&\quad+(w_{1} y_{2} - x_{1} z_{2} + y_{1} w_{2} + z_{1} x_{2})\,j\\
&\quad+(w_{1} z_{2} + x_{1} y_{2} - y_{1} x_{2} + z_{1} w_{2})\,k.
\end{aligned}
\]

Scalar–vector form is often cleaner. Write \(q=w+\mathbf{v}\) with \(\mathbf{v}=(x,y,z)\). Then

\[
q_{1} q_{2}
=
(w_{1} w_{2} - \mathbf{v}_{1}\cdot\mathbf{v}_{2})
+
w_{1}\mathbf{v}_{2} + w_{2}\mathbf{v}_{1} + \mathbf{v}_{1}\times\mathbf{v}_{2}.
\]

Two quaternions commute if and only if their vector parts are parallel.

## Conjugate, norm, inverse

The conjugate is

\[
\overline{q}=w-xi-yj-zk.
\]

It is an anti-automorphism: \(\overline{q_{1} q_{2}}=\overline{q_{2}}\,\overline{q_{1}}\) and \(\overline{\overline{q}}=q\). Real and vector parts recover as

\[
\operatorname{Re}(q)=\frac{q+\overline{q}}{2},\qquad
\operatorname{Vec}(q)=\frac{q-\overline{q}}{2}.
\]

The (squared) norm is the Euclidean norm on \(\mathbb{R}^{4}\):

\[
N(q)=q\overline{q}=\overline{q}q=w^{2}+x^{2}+y^{2}+z^{2}.
\]

It is multiplicative,

\[
N(q_{1} q_{2})=N(q_{1})N(q_{2}),
\]

which is the algebraic source of Lagrange’s four-square theorem. That identity is **spine arithmetic**, not a term in \(\partial p/\partial t\). Mass of \(p\) is a different lemma: \(\int Qp=0\). Do not fuse them.

Every nonzero \(q\) has a two-sided inverse

\[
q^{-1}=\frac{\overline{q}}{N(q)}.
\]

So \(\mathbb{H}\) is a division algebra: no zero divisors.

## Units: \(S^{3}\) as a Lie group

The unit quaternions are

\[
S^{3}=\{q\in\mathbb{H}:N(q)=1\}.
\]

Multiplicativity of \(N\) makes \(S^{3}\) a group. The identity is \(1\). The inverse of a unit is its conjugate. This is the compact Lie group \(\operatorname{Sp}(1)\cong\operatorname{SU}(2)\cong\operatorname{Spin}(3)\).

Polar form: if \(q\neq 0\), write

\[
q=\sqrt{N(q)}\,(\cos\theta + u\sin\theta),
\]

where \(u\) is a pure unit quaternion (\(u^{2}=-1\), so \(u\in S^{2}\subset\operatorname{Im}\mathbb{H}\)) and \(\theta\in\mathbb{R}\). This is the exact analogue of \(z=r(\cos\theta+i\sin\theta)\), except the “imaginary unit” now ranges over a whole 2-sphere of square roots of \(-1\).

## Identification with \(\mathbb{C}^{2}\)

The bridge to QGA’s Hopf map is

\[
q=z_{1}+z_{2} j,\qquad z_{1},z_{2}\in\mathbb{C}.
\]

If \(z_{1}=x_{1}+ix_{2}\) and \(z_{2}=x_{3}+ix_{4}\), this is the standard coordinates on \(\mathbb{R}^{4}\). The rule \(ji=-ij\) is what makes the second complex slot work: \(j z = \overline{z}\,j\) for \(z\in\mathbb{C}=\operatorname{span}\{1,i\}\).

On this splitting, left common-phase is

\[
e^{i\phi}q = e^{i\phi}z_{1} + e^{i\phi}z_{2} j,
\]

which is QGA’s fiber. That is why the locked generator is \(\mathrm{X}_{\mathrm{O}}(q)=iq\), not \(qi\).

## Left and right multiplication

For a fixed unit \(u\in S^{3}\):

- \(q\mapsto uq\) is left multiplication: an isometry of \(S^{3}\). It sends fibers of QGA’s \(h\) to fibers and rotates the base.
- \(q\mapsto qu\) is right multiplication: also an isometry. In general it **moves** QGA fibers. It is fiberwise \(U(1)\) only for \(u\) in the structure-group circle \(\operatorname{span}\{1,i\}\).

The infinitesimal facts already locked (`notes/hopf.md`):

- \(X(q)=iq\) generates \(q\mapsto e^{it}q\) and is **right-invariant**,
- \(Y(q)=qi\) generates \(q\mapsto q e^{it}\) and is **left-invariant**.

Do not swap them.

QGA Chapter 4 treats both multiplications as gauge candidates for the lattice. Protocol S1 does not import that gauge story: it freezes \(\mathrm{X}_{\mathrm{O}}\) and \(w\) and sweeps \(\sigma\).

## Pure quaternions and rotations

Identify \(\mathbb{R}^{3}\) with the pure imaginaries \(\operatorname{Im}\mathbb{H}=\operatorname{span}\{i,j,k\}\). For a unit \(q\),

\[
v\longmapsto q v\overline{q}
\]

is a rotation of \(\mathbb{R}^{3}\). This is a surjective group homomorphism

\[
S^{3}\to\operatorname{SO}(3),\qquad \ker=\{ \pm 1\},
\]

the spin double cover. That hides only \(\{q,-q\}\). QGA’s \(h\) hides the whole left common-phase circle \(e^{i\phi}q\). Those are two invisibilities, not one slogan. The third is the right circle of \(qi\overline{q}\). Table: `notes/rotations.md`.

Protocol S1 does not need the rotation homomorphism. Conjugation uses **both** left and right multiplication. It is not QGA’s \(h\). Attitude kinematics uses the same side-of-product bookkeeping as the fiber field, not the same field: \(\mathrm{X}_{\mathrm{O}}(q)=iq\) is not \(\dot q=\tfrac12 q\omega\).

## What this algebra is *not*, in the companion note

Two jobs share the word “quaternion.” Keep them split.

| Object | Role | Label |
| --- | --- | --- |
| \(\mathbb{H}\) as \(\mathbb{R}^{4}\) with associative product | so \(S^{3}\) is a group and left/right multiplications exist | stage |
| \(N(q)=1\) | standing constraint on the Hopf stage | spine |
| \(\mathrm{X}_{\mathrm{O}}(q)=iq\) | life field of QGA’s \(h\) | Model |
| Lipschitz / Hurwitz orders, class groups | integer arithmetic | QGA spine; not in \(Q\) |
| \(\{1,i,j,k\}\) as four elements | drawing dictionary | not an operator |

The generator remains two lobes plus a gate. Quaternion multiplication supplies the manifold and the fiber field. It does not add a third operator.

**Integer orders** (not this file). Lipschitz \(L=\mathbb{Z}[i,j,k]\). Hurwitz \(\mathcal{H}=L+\mathbb{Z}\frac{1+i+j+k}{2}\). The 24 Hurwitz units \(\Lambda_{0}=\mathcal{H}\cap S^{3}\) are the discrete skeleton QGA gauges. Preferring Hurwitz is a QGA **Model** choice (Ch. 1), not a fact about \(Q\).

**Quaternion algebras** \(\bigl(\frac{a,b}{\mathbb{Q}}\bigr)\), reduced norms, left ideals, two-sided class group: QGA Chapter 9. Do not write them into \(\mathrm{Q}_{\mathrm{C}}\).

**Topographs / Magic Islands / \(Z\mapsto\) flywheel.** QGA Parts III–IV and Hypothesis layer. The companion note’s \(Z\) is a coarse parameter of \(\sigma(Z)\). No equation for \(Z\).

If a drawing wants an element diamond, keep it in `notes/construct.md`. Do not add four extra fields to \(Q\).

## What the Model may take

| Application | Touches \(p\)? | Label |
| --- | --- | --- |
| \(S^{3}\) as configuration manifold of the Hopf-stage Model | yes | Model (stage) |
| \(\mathrm{X}_{\mathrm{O}}=iq\) along the fiber | yes | Model |
| Lattice / adjacency kernel for \(\mathrm{Q}_{\mathrm{C}}\) | yes | Model (jumps); adjacency rule is QGA OP1 |
| \(h\) as catalog projection | constraint on what \(\mathrm{Q}_{\mathrm{C}}\) can see | Spine fact |
| \(N(q)=1\) | constraint, not a term in \(Q\) | Spine |
| \(v\mapsto qv\overline{q}\) | no | Theorem; unused by S1 |
| Hurwitz units as discrete gauge group | only if you discretize \(\Lambda\) | QGA Model, unused by S1 |
| Class group / composition of flywheels | no | QGA; out of this note |
| \(\{1,i,j,k\}\) = four elements | no | dictionary |

The difference between a loading construct and a static flux lattice is still \(\sigma\): the lattice is what you get after the catalog gate has already won; the construct is the space in which \(\sigma\) can still be swept.
