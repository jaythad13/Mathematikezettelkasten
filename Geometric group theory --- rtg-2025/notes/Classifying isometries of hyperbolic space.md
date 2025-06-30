---
tags:
- ggt
- cx-geo
- rtg-2025/3
---

Recall that the [[Geometric group theory --- rtg-2025/notes/The hyperbolic plane#_definition _ Möbius transformation|Möbius transformations]] on $\mathbb{H}^{2}$ come exactly from $\mathrm{GL}_{2}(\mathbb{C})$ — $\mathrm{PSL}_{2}(\mathbb{R})$ [[Geometric group theory --- rtg-2025/notes/The hyperbolic plane#_theorem _ Möbius transformations acting on hyperbolic plane are $ mathrm{PSL}_{2}( mathbb{R})$|in particular]]. In fact these are all the automorphisms of $\mathbb{H}^{2}$, but we won't prove this. Recall also that for $A \in \mathrm{PSL}_{2}(\mathbb{R})$, we have $A(z : w) = (z : w)$ exactly when $(z, w)$ is an [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_definition _ eigenvalue, eigenvector|eigenvector]] of $A$. By analysing its characteristic polynomial, we see that $A$ has $2$ (distinct) real eigenvalues, $1$ real eigenvalue, or $2$ (conjugate) complex eigenvalues when $\lvert \operatorname{tr} A \rvert > 2$, $\lvert \operatorname{tr} A \rvert = 2$, and $\lvert \operatorname{tr} A \rvert < 2$ respectively. Thus, by analysing the obvious action of $\mathrm{PSL}_{2}(\mathbb{R})$ on $\mathbb{R}^{2}$, we can understand fixed points of its action on the topological [[Topology --- math-147/notes/Limit points and closed sets#_definition _ closure, closed|closure]] $\overline{\mathbb{H}^{2}} = \mathbb{H}^{2} \cup \mathbb{R} \mathbb{P}^1$. This gives a classification of isometries of $\mathbb{H}^{2}$.

This classification also happens to characterise another (conjugation-invariant) property of Möbius transformations — how far they map points from where they came from.

##### _definition:_ translation length

The translation length of a Möbius transformation $f$ on $\mathbb{H}^{2}$ is the infimum of distances between $z$ and $f(z)$ —
$$
\operatorname{length} f = \inf_{z \in \mathbb{H}^{2}} d_{\mathbb{H}^{2}}(z, f(z)).
$$

##### _proposition:_ translation length is conjugation-invariant

If $f, g \in \operatorname{Möb} \mathbb{H}^{2}$, then
$$
\operatorname{length} f = \operatorname{length} g \circ f \circ g^{-1}.
$$

###### _proof sketch:_

Recall that $g$ [[Geometric group theory --- rtg-2025/notes/The hyperbolic plane#_corollary _ Möbius transformations Geometric group theory --- rtg-2025/notes/Isometric actions _definition _ isometric action act isometrically on the hyperbolic plane|is an isometry]]. That is,
$$
d_{\mathbb{H}^{2}}(g \circ f \circ g^{-1}(z), z) = d_{\mathbb{H}^{2}}(f(z), z)
$$
for all $z \in \mathbb{H}^{2}$.

##### _theorem:_ classification of isometries of the hyperbolic plane

A Möbius transformation of the hyperbolic plane is one of the following —
1) hyperbolic, with two (distinct) fixed points on $\partial \mathbb{H}^{2}$ and positive translation length $\ell \in \mathbb{R}^+$ (actually attained)
2) parabolic, with one fixed point on $\partial \mathbb{H}^{2}$ and translation length $0$ (not actually attained)
3) elliptic, with one fixed point in $\mathbb{H}^{2}$ and translation length $0$ (actually attained).

###### _proof:_

Let $A \in \mathrm{PSL}_{2}(\mathbb{R})$ and let $f$ be the corresponding Möbius transformation.

Suppose $A$ has $2$ real eigenvalues. It then has [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_proposition _ eigenvectors from distinct eigenvalues are linearly independent|linearly independent eigenvectors]] $v_{1}, v_{2} \in \mathbb{R}^{2}$. These give distinct points $z_{1}, z_{2} \in \mathbb{R} \mathbb{P}^1 = \partial \mathbb{H}^{2}$ that are fixed points of $f$. Further, we can conjugate by another matrix (say $B$ corresponding to Möbius transformation $g$) to get a diagonal matrix $C$ corresponding to Möbius transformation $h$. (The fact that the conjugating matrix does correspond to a Möbius transformation comes from [[Geometric group theory --- rtg-2025/notes/The hyperbolic plane#_lemma _ Möbius transformations on $ mathbb{H} {2}$ are three-transitive on $ mathbb{R} mathbb{P} 2$|three transitivity]] on $\mathbb{R} \mathbb{P}^1$). Since $C$ still has determinant $1$, we must have
$$
C = \begin{pmatrix}
e^{\ell / 2} & 0 \\
0 & e^{-\ell / 2}
\end{pmatrix}
$$
and thus, $h(z) = e^{\ell} z$ (that is, $h(z : w) = (e^\ell z : w)$) for some $\ell \in \mathbb{R}^+$. Note that we can choose the matrix positive since we're in $\mathrm{PSL}_{2}(\mathbb{R})$ and $\ell$ positive by swapping bases. Thus it has two fixed points on $\mathbb{R} \mathbb{P}^1$, in particular, $0$ and $\infty$.

It follows from the definition of the [[Geometric group theory --- rtg-2025/notes/The hyperbolic plane#_definition _ hyperbolic length, hyperbolic metric|hyperbolic metric]] that $d_{\mathbb{H}^{2}}(i, h(i)) = \ln(e^\ell) = \ell$. Further, one can find a Möbius transformation that takes any $r e^{i \theta} \mapsto i$ and $h(r e^{i \theta}) = r e^{\ell + i \theta} \mapsto \lambda i$ with $\lambda > e^{\ell}$. Thus, $h$ has length $\ell$. $f$ has the same length.

Suppose $A$ has just $1$ real eigenvalue $\lambda$. Since $\prod \lambda = \det A = 1$, we have $\lambda = 1$. If $A$ is diagonalisable, it is just the identity. Else, $A$ has a unique (up to scalars) eigenvector $v \in \mathbb{R}^{2}$, and thus, a unique fixed point $z \in \mathbb{R} \mathbb{P}^{1}$. By conjugating with a Möbius transformation $g$ with $g(z) = \infty$, we get $h = g \circ f \circ g^{-1}$ with its only fixed point $\infty$. Since the coefficient of $z$ in the denominator must be $0$, we get that the corresponding matrix is upper-triangular, and since it must have the same eigenvalues, it has $1$s on the diagonal. That is,
$$
C = \begin{pmatrix}
1 & t \\
0 & 1
\end{pmatrix}
$$
and $h(z) = z + t$ for some $t \in \mathbb{R}$.

One can find a Möbius transformation $w$ such that $w(y i)$ and $w(yi + t) \in i \mathbb{R}$. In particular, by [[Geometric group theory --- rtg-2025/notes/The hyperbolic plane#_proposition _ the action of Möbius transformations is transitive on geodesic circles|transitivity]], of Möbius transformations on geodesics, choose the Möbius transformation that sends the circle between them to the imaginary line. From the form of this $w$ it follows that as $y \to \infty$,
$$
d_{\mathbb{H}^{2}}(yi, h(yi)) = d_{\mathbb{H}^{2}}(w(yi), w(yi + t)) \to 0.
$$
Thus, $\operatorname{length} f = \operatorname{length} h = 0$.

If $A$ has two conjugate eigenvalues, then (as a map on $\mathbb{C}^{2}$) it has two conjugate eigenvectors $v, \overline{v}$ (where if $v = (z, w)$, then $\overline{v} = (\overline{z}, \overline{w}))$ ). Specifically, if $v$ has eigenvalue $\lambda$, then
$$
A \overline{v} = \overline{A} \overline{v} = \overline{A v} = \overline{\lambda v} = \bar{\lambda} \overline{v}.
$$
For $(z, w) \in \mathbb{C}^{2}$, only one of $(z : w)$ and $(\overline{z} : \overline{w})$ is in the upper half plane, and thus, $\mathbb{H}^{2}$. Assume without loss of generality that $(z : w) \in \mathbb{H}^{2}$. Conjugating by a Möbius transformation such that $g : (z : w) \mapsto i$ gives a Möbius transformation $h$ with unique fixed point $i$ in $\mathbb{H}^{2}$. $h$ still fixes $-i$ in the lower half plane since conjugation is preserved by real Möbius transformations. The matrix $C$ corresponding to $h$ still has determinant $1$, so $\lvert \lambda \rvert^{2} = \lambda \bar{\lambda}  = 1$. Thus, $\lambda = \cos \theta + i \sin \theta$. The matrix $C$ such that $C(i, 1) = e^{i \theta} (i, 1)$ and $C(-i, 1) = e^{-i \theta}(-i, 1)$. This forces
$$
C = \begin{pmatrix}
\cos \theta & - \sin \theta \\
\sin \theta & \cos \theta
\end{pmatrix}.
$$

Since $h(i) = i$, $h$ clearly has length $0$. $f$ also has a fixed point, and thus, length $0$.