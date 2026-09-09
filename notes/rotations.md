# Rotation conjugation (not Hopf)

Three invisibilities, not one slogan reused three times:

| Map | Formula | Hidden coordinate |
| --- | --- | --- |
| Rotation (this note) | \(v\mapsto q v\overline{q}\) | only \(\{q,-q\}\) |
| QGA’s \(h\) | left common-phase \(S^{3}\to S^{2}\) | the whole circle \(e^{i\phi}q\) |
| Other Hopf map | \(q i\overline{q}\) | the other circle |

The rotation application is conjugation, not the Hopf projection. A unit quaternion \(q\in S^{3}\) turns a pure vector \(v\in\operatorname{Im}\mathbb{H}\cong\mathbb{R}^{3}\) by \(v\mapsto q\,v\,\overline{q}\). That uses **both** left and right multiplication. It is a different map from QGA’s locked \(h\).

Algebra used here: `notes/quaternions.md`. Fiber of \(h\): `notes/hopf.md`. Protocol S1 does not need this homomorphism.

Claim label: **Theorem** (classical). Not a lemma about \(Q\). Not a third operator.

## The operator

Write a unit quaternion in axis–angle form. If \(u\) is a pure unit quaternion (so \(u^{2}=-1\)) and \(\theta\) is the rotation angle,

\[
q=\cos\frac{\theta}{2}+u\sin\frac{\theta}{2}=e^{u\theta/2}.
\]

Then \(q\,v\,\overline{q}\) is rotation of \(v\) by angle \(\theta\) about axis \(u\). Expanding the product recovers Rodrigues’ formula:

\[
q v \overline{q}
=
v\cos\theta
+(u\times v)\sin\theta
+u(u\cdot v)(1-\cos\theta).
\]

Composition is multiplication: conjugating by \(pq\) is “rotate by \(q\), then by \(p\)”:

\[
(pq)\,v\,\overline{pq}
=
p\bigl(q v \overline{q}\bigr)\overline{p}.
\]

The inverse rotation is the conjugate: \(\overline{q}\,v\,q\). On units, \(\overline{q}=q^{-1}\).

The same \(q\) and \(-q\) give the same rotation, because

\[
(-q)\,v\,\overline{(-q)}=q v \overline{q}.
\]

That is the double cover

\[
S^{3}\to\operatorname{SO}(3),\qquad \ker=\{\pm 1\}.
\]

A full turn of the 3D object is only a half-turn on \(S^{3}\). The extra \(\pi\) of phase is invisible to any function of the rotated vector. That hidden coordinate is \(\{q,-q\}\), not the whole left common-phase circle of QGA’s \(h\), and not the right circle of \(qi\overline{q}\). Three invisibilities.

## Why this is used instead of Euler angles

Euler angles parametrize \(\operatorname{SO}(3)\) by three sequential axis rotations. That chart has singularities: when the middle angle is \(\pm\pi/2\), two gimbals align and one degree of freedom is lost. That is gimbal lock.

Unit quaternions live on \(S^{3}\), which has no coordinate singularity. You never lose a degree of freedom by pointing “straight up.” You do have to remember \(q\sim -q\), and you renormalize after numerical integration so \(N(q)\) stays 1.

Storage and composition are cheap: 4 numbers instead of 9, one multiply instead of two \(3\times 3\) matrix products. Engines, robot stacks, and spacecraft ADCS keep orientation as a unit quaternion internally and convert to matrices only at the render or actuator boundary.

## Interpolation: SLERP

Linearly blending Euler angles does not produce a rotation geodesic and explodes near gimbal lock. On \(S^{3}\) the geodesic is a great circle. Shoemake’s SLERP (1985) is

\[
\operatorname{slerp}(q_{1},q_{2};t)
=
\frac{\sin((1-t)\Omega)}{\sin\Omega}\,q_{1}
+
\frac{\sin(t\Omega)}{\sin\Omega}\,q_{2},
\]

where \(\Omega=\arccos(q_{1}\cdot q_{2})\) after choosing the short branch (\(q_{1}\leftarrow -q_{1}\) if the dot product is negative). The path has constant angular velocity about a fixed axis.

A cheaper relative is NLERP: ordinary linear blend followed by renormalization. It is not constant-speed, but it is good enough for many games.

Neither interpolant is a term in \(Q\).

## Where it actually runs

**Computer graphics and games.** Object and camera orientation, skeletal animation, look-at constraints. Keyframes are quaternions; in-betweens are SLERP. Hierarchical models compose by multiplying parent and child quaternions.

**Robotics.** Arm pose, end-effector orientation, drone and gimbal stabilization. Inverse kinematics that stay in quaternion space do not invent a fake extra twist when the wrist passes vertical. Error-state Kalman filters on IMUs represent the small attitude error as a 3-vector tangent to \(S^{3}\) and carry the global pose as a quaternion.

**Aerospace.** Strapdown inertial navigation and large-angle spacecraft slews. Attitude kinematics are

\[
\dot q=\tfrac12 q\,\omega_{\mathrm{body}}
\qquad\text{versus}\qquad
\dot q=\tfrac12\omega_{\mathrm{inertial}}\,q.
\]

That is the same **side-of-product** bookkeeping as the fiber field, not the same field. \(\mathrm{X}_{\mathrm{O}}(q)=iq\) is the generator of left common-phase on this \(h\). Body-rate \(\omega\) on the right is a general element of \(\operatorname{Im}\mathbb{H}\), not \(i\). Do not write \(\mathrm{X}_{\mathrm{O}}\) as “the attitude kinematic field.” Numerical integration of that ODE plus renormalization is the standard attitude propagator. Neither ODE is a term in \(Q\).

**Computer vision.** Pose estimation, camera registration, and 3D reconstruction often solve for an unknown unit quaternion rather than a rotation matrix, because the unit-norm constraint is one quadratic equation instead of six orthonormality constraints.

**Molecular and rigid-body simulation.** Protein orientations, rigid-body integrators, and ragdoll physics use the same conjugation so constraints stay on \(\operatorname{SO}(3)\) without chart switches.

**Quantum mechanics.** The same double cover is \(\operatorname{SU}(2)\to\operatorname{SO}(3)\). A spin-\(\tfrac12\) state that goes around a loop of rotations in physical space picks up a minus sign — the quaternion has traveled a full turn on \(S^{3}\) while the 3D rotation has only gone once. That is an application of the cover, not of QGA’s Hopf map.

## 4D rotations, briefly

A general rotation of \(\mathbb{R}^{4}\cong\mathbb{H}\) is

\[
x\longmapsto q_{L}\,x\,q_{R}
\]

with two independent units \(q_{L},q_{R}\). That is \(\operatorname{SO}(4)\)’s double cover \(S^{3}\times S^{3}\). Restricting to \(q_{R}=\overline{q_{L}}\) recovers 3D rotation of the pure imaginaries and leaves the real axis fixed. Left-only or right-only multiplication gives isoclinic 4D rotations (Hopf fibers move as rigid circles). That is geometry of the stage, not a third operator in \(Q\).

## Relation to the locked maps

The opening table is the lock. Rotation conjugation is how a catalog-visible 3-vector is moved. QGA’s \(h\) is how a catalog-visible 2-sphere point is read off a unit quaternion. Protocol S1 does not need the rotation homomorphism.

The engineering rule that follows from the algebra, and does not depend on the Model: store orientation as a unit quaternion, compose by multiplication, interpolate by SLERP, integrate \(\dot q=\tfrac12 q\,\omega_{\mathrm{body}}\) (or the left-handed twin), and renormalize. Convert to Euler angles only at the human interface.

Do not put SLERP, gimbal lock, MEKF, or attitude kinematics into the companion note or into \(Q\). Do not identify \(\mathrm{X}_{\mathrm{O}}\) with \(\dot q=\tfrac12 q\omega\).

The generator is still only

\[
\frac{\partial p}{\partial t}=\mathrm{Q}_{\mathrm{O}}p+\sigma(Z)\,\mathrm{Q}_{\mathrm{C}}p.
\]
