# Gaussian Farey (the \(i\)-plane slice of OP1)

Gaussian Farey is the theorem you get if you stay in one unital plane \(\mathrm{span}\{1,i\}\cong\mathbb{C}\). It is the right specialisation for Exercise 3.H. It is **not** a quaternionic Farey diagram.

Six planes and \(\Lambda_{0}\): `notes/hurwitz.md`. Incidence still open: `notes/op1.md`. Bundle: `notes/hopf.md`.

Claim label: **Theorem** for \(\mathbb{Z}[i]\), \(\mathrm{PSL}(2,\mathbb{Z}[i])\), and unit-determinant adjacency. Glueing that graph to the 24-cell or to \(E_{\parallel}\) is **OP1**.

## Classical reminder

Farey sequence of order \(N\):

\[
\mathcal{F}_{N}
=\Bigl\{\tfrac{a}{b}\in\mathbb{Q}\cup\{\infty\}:
\gcd(a,b)=1,\ 0\le b\le N\Bigr\}
\]

ordered on \(\mathbb{R}\cup\{\infty\}\). Adjacent fractions \(a/b,\,c/d\) satisfy

\[
ad-bc=\pm 1,
\]

and the mediant \((a+c)/(b+d)\) is the first new point that appears between them. Group: \(\mathrm{PSL}(2,\mathbb{Z})\). Picture: ideal triangulation of \(\mathbb{H}^{2}\), Ford circles.

Everything that follows is the same list with \(\mathbb{Z}\) replaced by \(\mathbb{Z}[i]\). The object is no longer an ordered sequence on a line.

## Gaussian integers and Gaussian rationals

\[
\mathbb{Z}[i]=\{m+ni:m,n\in\mathbb{Z}\},\qquad
\mathbb{Q}(i)=\Bigl\{\tfrac{\alpha}{\gamma}:\alpha,\gamma\in\mathbb{Z}[i],\ \gamma\neq 0\Bigr\}.
\]

Norm \(N(\alpha)=\alpha\bar\alpha=m^{2}+n^{2}\). Units

\[
\mathbb{Z}[i]^{\times}=\{1,-1,i,-i\}=C_{4},
\]

exactly the Hopf \(C_{4}\) through \(1\) in the \(i\)-plane. Euclidean algorithm holds (covering radius \(\sqrt{2}/2\)). Unique factorization up to units. That is why a determinant condition can replace \(\gcd=1\).

A fraction \(\alpha/\gamma\) is **reduced** if \(\gcd(\alpha,\gamma)\) is a unit (equivalently, \(\alpha,\gamma\) generate \(\mathbb{Z}[i]\) as an ideal). Write \(\infty=1/0\).

## The Gaussian Farey graph

Height is the **modulus of the denominator**, not the squared norm. That is the convention of Sayous (and the complex Farey literature): \(0<|\gamma|\le T\). Bounding \(N(\gamma)\le T\) is a different filtration; do not use it for \(\mathcal{G}_{T}\).

Height-\(T\) set, living in \(\widehat{\mathbb{C}}=\mathbb{P}^{1}(\mathbb{C})\) (or, for gap statistics, projected to the torus \(\mathbb{C}/\mathbb{Z}[i]\)):

\[
\mathcal{G}_{T}
=\Bigl\{\tfrac{\alpha}{\gamma}\in\mathbb{P}^{1}(\mathbb{Q}(i)):
\alpha,\gamma\in\mathbb{Z}[i],\
\gcd(\alpha,\gamma)\in\mathbb{Z}[i]^{\times},\
0<|\gamma|\le T\Bigr\}.
\]

Source: R. Sayous, *Gaps in the complex Farey sequence of an imaginary quadratic number field*, arXiv:2407.04380. There \(\mathcal{G}_{T}=\{\mathrm{pr}(p/q):0<|q|\le T\}\subset\mathbb{C}/\mathbb{Z}[i]\). For the graph we keep reduced fractions in \(\mathbb{P}^{1}\).

Two reduced fractions \(\alpha/\gamma\) and \(\beta/\delta\) are **adjacent** iff

\[
\alpha\delta-\gamma\beta\in\mathbb{Z}[i]^{\times}=\{1,-1,i,-i\}.
\]

There is no total order. The object is a graph (the 1-skeleton of an octahedral complex), not a sequence \(\mathcal{F}_{N}\).

Group: the Picard group \(\mathrm{PSL}(2,\mathbb{Z}[i])\) (Bianchi group \(\mathrm{Bi}(1)\)). It acts on hyperbolic 3-space \(\mathbb{H}^{3}\). The Farey geodesics are the \(\mathrm{SL}(2,\mathbb{Z}[i])\)-orbit of the edge \(\infty\)–\(0\). They are the 1-skeleton of the tessellation of \(\mathbb{H}^{3}\) by **ideal octahedra**. Ford spheres replace Ford circles.

A mediant is not unique: already in \(\mathbb{C}\) several interpolants of the same height can sit between a pair. The “first new point” slogan does not survive.

## The lock for Exercise 3.H

Restrict a candidate \((\Lambda,E)\) to \(\mathrm{span}\{1,i\}\). After projectivizing, the finite-height part should reproduce \(\mathcal{G}_{T}\) adjacency (determinant a unit), or fail in a named way.

The \(C_{4}\) of units alone is **not** \(\mathcal{G}_{T}\): it is only the four points with \(|\gamma|=1\) (Farey neighbors of \(\infty\)). To see Farey you must include denominators of modulus \(>1\) (\(1+i\) has \(|\gamma|=\sqrt{2}\); then \(2\), \(2+i\), …), i.e. points of quaternion norm \(>1\). Those points are in \(\mathcal{H}\cap\mathrm{span}\{1,i\}=\mathbb{Z}[i]\), so you have already left \(\Lambda_{0}\subset S^{3}\).

That last sentence is the lock. Gaussian Farey is a lattice-in-the-plane fact. The 24-cell is a sphere fact. Glueing them is OP1.

Same construction in the \(j\)-plane and the \(k\)-plane: three scores, do not average (`notes/hurwitz.md`, Reading A). Starred planes are not unital copies of \(\mathbb{C}\) through \(1\).

## What does not lift

**Determinant.** \(\alpha\delta-\gamma\beta\in\mathbb{Z}[i]^{\times}\) uses commutativity of \(\mathbb{C}\). In \(\mathbb{H}\) the same expression is a Dieudonné minor; no adopted convention. That obstruction is independent of this slice.

**One mediant.** Already false in \(\mathbb{C}\). Worse in \(\mathbb{H}\).

**Order / sequence.** False in \(\mathbb{C}\). The object is a graph (or an octahedral complex), not \(\mathcal{F}_{N}\).

**Modular group = unit multiplications.** \(\mathrm{PSL}(2,\mathbb{Z}[i])\) is \(2\times 2\) matrices. Left multiplication by \(j\) sends the \(i\)-plane to the \(k\)-plane and is **not** an element of that Picard group. Gauge equivariance and Farey-in-the-plane are different actions.

**Fiber.** Gaussian Farey has no leftover \(S^{1}\). QGA does. \(E_{\parallel}\) is invisible in \(\mathcal{G}_{T}\).

Same construction exists for Eisenstein integers \(\mathbb{Z}[\omega]\) (Bianchi group \(\mathrm{Bi}(3)\), tetrahedral tessellation of \(\mathbb{H}^{3}\)). That is the other imaginary quadratic Euclidean ring. It is the \(2I\)/icosahedral temptation again, not Hurwitz.

## Practical dictionary for the discrete cut

On \(\mathbb{Z}[i]\subset\mathrm{span}\{1,i\}\), three radii:

| Radius | Points | What you see |
| --- | --- | --- |
| \(\lvert\gamma\rvert=1\) | the \(i\)-square | Farey neighbors of \(\infty\). No mediants yet. |
| \(\lvert\gamma\rvert\le\sqrt{2}\) | add \(1+i,1-i,-1+i,-1-i\) and cousins | first octahedron vertices. Determinant \(\pm 1,\pm i\) vs extra edges can be listed by hand. |
| Height \(T\): \(\lvert\gamma\rvert\le T\) | full \(\mathcal{G}_{T}\) | compare any candidate adjacency, restricted to this plane, against the unit-determinant graph. |

Score: number of unit-det pairs that the candidate misses, and number of extra edges whose det has norm \(>1\). A failed Farey reduction is a pair of those counts, not a picture that “looks like Chapter 2.”

Allowed: Gaussian Farey as the theorem on the \(i\)-plane, including points off \(S^{3}\). Forbidden: “\(\Lambda_{0}\) carries Gaussian Farey” and “Picard octahedra are the 24-cell.”
