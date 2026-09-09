# Hopf remainder (spine, not a lemma about \(Q\))

The companion note imports one fact from QGA Chapter 2 and does not prove it:

\[
S^{1}\hookrightarrow S^{3}\xrightarrow{h}S^{2}
\]

is a locally trivial principal \(U(1)\)-bundle that is not globally trivial. Catalog observables that factor through \(h\) cannot invert the fiber coordinate.

Claim label: **Spine fact**. Not a lemma about the helicoid–catenoid generator. Not a theorem that reality is a Hopf bundle.

QGA source: `~/Projects/qga/book/02_hopf.md`. One map: `lib.hopf_lattice.hopf_map`.

## The map (lock this one)

Identify \(q=z_{1}+z_{2}j\) with \((z_{1},z_{2})\in\mathbb{C}^{2}\), \(|z_{1}|^{2}+|z_{2}|^{2}=1\), and \(z_{1}=x_{1}+ix_{2}\), \(z_{2}=x_{3}+ix_{4}\). QGA’s Hopf map is

\[
h(z_{1},z_{2})
=
\bigl(
  2\,\mathrm{Re}(\overline{z_{1}}z_{2}),\;
  2\,\mathrm{Im}(\overline{z_{1}}z_{2}),\;
  |z_{1}|^{2}-|z_{2}|^{2}
\bigr)
\in S^{2}\subset\mathbb{R}^{3},
\]

same as the real form

\[
\begin{aligned}
y_{1}&=2(x_{1}x_{3}+x_{2}x_{4}),\\
y_{2}&=2(x_{1}x_{4}-x_{2}x_{3}),\\
y_{3}&=x_{1}^{2}+x_{2}^{2}-x_{3}^{2}-x_{4}^{2}.
\end{aligned}
\]

On unit 4-vectors this already lands on \(S^{2}\). Do not re-normalize the output by \(\|y\|\). Equivalently, \(h(z_{1},z_{2})=[z_{1}:z_{2}]\in\mathbb{CP}^{1}\cong S^{2}\).

The fiber is **left common-phase**:

\[
(z_{1},z_{2})\;\longmapsto\;(e^{i\phi}z_{1},\,e^{i\phi}z_{2}),
\]

i.e. left multiplication \(q\mapsto e^{i\phi}q\) with \(e^{i\phi}\in\mathrm{span}\{1,i\}\). That circle is the remainder. The angle-chart \(\xi_{2}\)-circle at fixed \((\eta,\xi_{1})\) is a different loop; do not call it the Hopf fiber (QGA §2.1–2.2).

## Left vs right on the group \(S^{3}\)

The locked field is not left-invariant. Earlier wording mixed two different circles on \(S^{3}\).

\(S^{3}=\{q\in\mathbb{H}:N(q)=1\}\) is a Lie group under quaternion multiplication. For a fixed unit \(u\),

\[
L_{u}(q)=uq,\qquad R_{u}(q)=qu.
\]

A vector field \(X\) is left-invariant if \((L_{u})_{*}X_{q}=X_{uq}\), and right-invariant if \((R_{u})_{*}X_{q}=X_{qu}\).

One-parameter subgroups give the two families. Let \(\xi\) be a pure unit imaginary (\(\xi^{2}=-1\)). Then

\[
\frac{d}{dt}\Big|_{0}e^{t\xi}\,q=\xi q,
\qquad
\frac{d}{dt}\Big|_{0}q\,e^{t\xi}=q\xi.
\]

| Field | Flow | Invariance | Circle |
| --- | --- | --- | --- |
| \(X(q)=\xi q\) | left multiplication \(q\mapsto e^{t\xi}q\) | **right-invariant** | left cosets of \(\mathrm{span}\{1,\xi\}\) |
| \(Y(q)=q\xi\) | right multiplication \(q\mapsto q e^{t\xi}\) | **left-invariant** | right cosets of \(\mathrm{span}\{1,\xi\}\) |

Check right-invariance of \(X(q)=\xi q\):

\[
X(qu)=\xi(qu)=(\xi q)u=(R_{u})_{*}X(q).
\]

Check left-invariance of \(Y(q)=q\xi\):

\[
Y(uq)=(uq)\xi=u(q\xi)=(L_{u})_{*}Y(q).
\]

Those are different fields unless \(\xi\) is central, which it is not in \(\mathbb{H}\).

## Which one is the fiber of QGA’s \(h\)

QGA’s map is constant on **left common-phase** \(q\mapsto e^{i\phi}q\), i.e. left multiplication by the circle \(\mathrm{span}\{1,i\}\). The infinitesimal generator is therefore

\[
\mathrm{X}_{\mathrm{O}}(q)=iq.
\]

That is the **right-invariant** field of the table, with \(\xi=i\). It is not left-invariant.

Under \(q=z_{1}+z_{2}j\),

\[
iq=i(z_{1}+z_{2}j)=(iz_{1})+(iz_{2})j,
\]

which is exactly \((z_{1},z_{2})\mapsto(e^{i\phi}z_{1},e^{i\phi}z_{2})\) at \(\phi=\pi/2\). That is why \(\mathrm{X}_{\mathrm{O}}=iq\) is the structure-group field of *this* \(h\).

The **left-invariant** field \(q\mapsto qi\) generates the other circle \(q\mapsto q e^{it}\), which is the fiber of the other Hopf map \(q\,i\,\overline{q}\). Same bundle up to isometry of the base; not the book’s coordinates, not the book’s generator.

On the generator that is only

\[
\mathrm{Q}_{\mathrm{O}}p=-\operatorname{div}_{S^{3}}(\mathrm{X}_{\mathrm{O}}\,p),\qquad \mathrm{X}_{\mathrm{O}}(q)=iq.
\]

No extra invariance claim is required inside \(Q\). The invariance type is recorded so the field is not swapped for the other circle.

## Convention trap

These are Hopf maps, up to isometry of the base. They are **not** the same coordinate formula.

| Formula | Structure-group action | Use |
| --- | --- | --- |
| QGA \(h\) above | left common-phase \(e^{i\phi}q\) | lock |
| \(q\,i\,\overline{q}\) | right circle \(q\mapsto q e^{i\phi}\) | valid Hopf map, **not** the book’s \(h\) |
| \(2z_{0}\overline{z_{1}}\) in \(\mathbb{C}\times\mathbb{R}\) | left common-phase, opposite orientation on the \(\mathbb{C}\) slot | same bundle, different chart |

Three invisibilities, not one slogan reused three times (`notes/rotations.md`):

| Map | Hidden coordinate |
| --- | --- |
| \(v\mapsto q v\overline{q}\) | only \(\{q,-q\}\) |
| QGA’s \(h\) | the whole left common-phase circle \(e^{i\phi}q\) |
| \(q i\overline{q}\) | the other circle |

Attitude kinematics \(\dot q=\tfrac12 q\,\omega_{\mathrm{body}}\) versus \(\dot q=\tfrac12\omega_{\mathrm{inertial}}\,q\) is the same **side-of-product** bookkeeping, not the same field. \(\mathrm{X}_{\mathrm{O}}(q)=iq\) generates left common-phase on this \(h\). Body-rate \(\omega\) is a general element of \(\operatorname{Im}\mathbb{H}\), not \(i\). Do not write \(\mathrm{X}_{\mathrm{O}}\) as the attitude kinematic field.

`legacy_portal_map` in QGA is **not** a Hopf map: it ignores \((x_{3},x_{4})\) in \(y_{1},y_{2}\), vanishes at \((0,0,1,0)\), and is not constant on structure-group fibers.

The companion note uses \(\mathrm{X}_{\mathrm{O}}(q)=iq\), the right-invariant generator of left common-phase. It does not use the left-invariant field of \(q\,i\,\overline{q}\).

## Locally a product

A map \(E\to B\) with fiber \(F\) is a fiber bundle if every point of \(B\) has a neighborhood \(U\) and a homeomorphism \(\varphi:U\times F\xrightarrow{\cong}h^{-1}(U)\) commuting with projection.

Two charts suffice: delete the north pole or the south pole of \(S^{2}\). Each complement is diffeomorphic to \(\mathbb{R}^{2}\), and

\[
h^{-1}(S^{2}\setminus\{N\})\;\cong\;(S^{2}\setminus\{N\})\times S^{1}.
\]

Locally one may choose a continuous fiber coordinate. That is the note’s local metric agreement: on a trivialization the two lobes of the Model may share the bundle metric.

## Globally not a product

\(S^{3}\not\cong S^{2}\times S^{1}\). Cheap proofs, in increasing strength:

1. \(\pi_{1}(S^{3})=0\) while \(\pi_{1}(S^{2}\times S^{1})\cong\mathbb{Z}\).
2. \(\pi_{2}(S^{3})=0\) while \(\pi_{2}(S^{2}\times S^{1})\cong\mathbb{Z}\).
3. There is no continuous global section \(s:S^{2}\to S^{3}\) with \(h\circ s=\mathrm{id}_{S^{2}}\). A section would split the bundle and force it to be trivial.

“The base cannot invert the fiber” is (3): there is no continuous rule that, for every catalog-visible point of \(S^{2}\), picks one point on its circle in \(S^{3}\).

What does exist: local sections over any proper open of \(S^{2}\); discontinuous sections (choose a point in each circle by brute force); sections after deleting a point from the base.

The remainder is a global topological obstruction, not hidden data a better catalog could recover.

## Clutching and \(c_{1}\) (spine, not in the note)

Cover \(S^{2}\) by contractible hemispheres \(U_{N},U_{S}\). On the equator \(U_{N}\cap U_{S}\simeq S^{1}\) the two trivializations differ by a clutching map \(\tau:S^{1}\to U(1)\cong S^{1}\) of degree \(\pm 1\). Principal \(U(1)\)-bundles over \(S^{2}\) are classified by \(\pi_{1}(S^{1})\cong\mathbb{Z}\), and that integer is \(c_{1}\). Hopf is the generator \(c_{1}=\pm 1\). The product bundle has \(c_{1}=0\).

Chern–Weil: \(c_{1}\neq 0\) forbids a flat connection. Curvature is forced. The companion note does not need this sentence; it is why no global section exists.

## Linking

Any two distinct fibers are linked once. After stereographic projection \(S^{3}\setminus\{\mathrm{pt}\}\to\mathbb{R}^{3}\), fibers fill \(\mathbb{R}^{3}\) by circles (plus one line, the fiber through the pole). Every pair is a Hopf link, linking number \(\pm 1\). That is the Hopf invariant of the generator of \(\pi_{3}(S^{2})\cong\mathbb{Z}\).

Linking is why the bundle cannot be untwisted. If the fibers were unlinked, a continuous section would exist. Flywheel Hopf linking in QGA lives on this fact. The Model uses it as input; it does not prove it.

## Homotopy (pointer)

The long exact sequence of the fibration gives \(\pi_{2}(S^{2})\cong\mathbb{Z}\), \(\pi_{3}(S^{2})\cong\mathbb{Z}\), and \(\pi_{k}(S^{3})\cong\pi_{k}(S^{2})\) for \(k\ge 3\). The Hopf map represents a generator of \(\pi_{3}(S^{2})\). Do not put this sequence in the companion note.

## Four sphere fibrations (do not confuse)

Normed division algebras give four sphere fibrations. QGA and this note use the **complex** one, even though the total space is unit quaternions:

| Algebra | Bundle | Fiber | Base |
| --- | --- | --- | --- |
| \(\mathbb{R}\) | \(S^{0}\hookrightarrow S^{1}\to S^{1}\) | \(\{\pm 1\}\) | \(\mathbb{RP}^{1}\cong S^{1}\) |
| \(\mathbb{C}\) | \(S^{1}\hookrightarrow S^{3}\to S^{2}\) | \(S^{1}\) | \(\mathbb{CP}^{1}\cong S^{2}\) |
| \(\mathbb{H}\) | \(S^{3}\hookrightarrow S^{7}\to S^{4}\) | \(S^{3}\) | \(\mathbb{HP}^{1}\cong S^{4}\) |
| \(\mathbb{O}\) | \(S^{7}\hookrightarrow S^{15}\to S^{8}\) | \(S^{7}\) | \(\mathbb{OP}^{1}\cong S^{8}\) |

The quaternionic Hopf fibration \(S^{7}\to S^{4}\) is a different object. Do not move the stage there by renaming \(\mathbb{H}\).

## What the Model is allowed to take

- Local triviality of \(h\).
- No global section.
- Catalog functions are constant on fibers (pullbacks from the base).
- \(\mathrm{X}_{\mathrm{O}}\) along the structure-group fiber; \(\mathrm{Q}_{\mathrm{C}}\) on jumps that may factor through \(h\).
- Linking as imported protection language for flywheels.

Not allowed: proving any of the above as a lemma about \(Q\); writing \(c_{1}\), clutching, or \(\pi_{3}(S^{2})\) into the generator; treating helicoid/catenoid as the configuration manifold; substituting \(q\,i\,\overline{q}\) silently for QGA’s \(h\).
