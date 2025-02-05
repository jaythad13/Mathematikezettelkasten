---
tags:
- diff-geo
- cx-geo
- math-196/1
- math-196/2
- math-196/3
---

##### _definition:_ (compact, connected) Riemann surface, (holomorphic) atlas

A (compact, connected) Riemann surface is a pair of a ([[Mathematical Analysis I --- math-131/notes/Compactness#_definition _ compact|compact]], [[Mathematical Analysis I --- math-131/notes/Connectedness#_definition _ connectedness|connected]]) second  countable, Hausdorff topological space $X$ and a holomorphic atlas $\mathcal{A}$. 

That is, $\mathcal{A}$ is an open cover $\{ U_{\alpha} \}$ such that each $U_{\alpha}$ is homeomorphic (with the homeomorphism being $\phi_{\alpha}$) to an open, connected subset of $\mathbb{C}$. Further, each "transition map" $\phi_{\beta} \circ \phi_{\alpha} ^{-1}$ is a [[Complex Analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$|holomorphic]] function $\phi_{\alpha}(U_{\alpha} \cap U_{\beta}) \to \phi_{\beta}(U_{\alpha} \cap U_{\beta})$.

The Hausdorff condition is a reasonability condition on topological spaces — for any two distinct points in the topological space, we can separate them in $\mathbb{C}$.

Usually given reasonable sets $X$, we can topologise $X$ so that the ope n cover is open.

The main theorem that we want to learn is that compact connected Riemann surfaces are completely classified —

##### _theorem:_ the uniformisation theorem

A compact connected Riemann surface $X$ is one of three things
1) the Riemann sphere $\mathbb{P}^1(\mathbb{C})$ (the one-point compactification of $\mathbb{C}$) with genus $0$
2) Euclidean — a torus $\mathbb{C} / \Lambda$ for some lattice $\Lambda$ with genus $1$
3) hyperbolic — $X$ is the right cosets of the (compactified) upper half plane $\mathbb{H}^*$ modulo some group $\Gamma$ with genus $g \ge 2$.

When we say "is", we mean something specific, but we will not specify what that is that we mean.

##### _example:_ the Riemann sphere

The (topological space of the) sphere is exactly the sphere $S^2$ sitting in $\mathbb{R}^3$. We can cover this with one open set $U_{1}$ staying away from the south pole, and another $U_{2}$ staying away from the north pole. Both of these have an obvious homeomorphism to $\mathbb{C}$ itself by stereographic projection. We often call this projective $1$-space and write that as $\mathbb{P}^1(\mathbb{C})$.

The transition map is $z \mapsto 1/z$ which is indeed holomorphic on $\mathbb{C}$. Applying this to the sphere is essentially flipping the sphere.

This means that we actually have a natural metric on $\mathbb{P}^1(\mathbb{C})$ — it's just the metric inherited by the $2$-sphere $S^2$ sitting in $\mathbb{R}^3$.

##### _example:_ [[Algebraic Geometry --- math-176/notes/Elliptic curves#_proposition, definition _ reducing cubics, elliptic curves|elliptic curves]]

An elliptic curve $E(\mathbb{C})$ is the set of complex points, $(x, y) \in \mathbb{C}^2$ such that $y^{2} = x^3 + A x + B$ for coefficients $A, B \in \mathbb{C}$ with non-zero discriminant $4A^3 + 27 B^{2} = 0$, with an additional "point at infinity" — the one point compactification of the original set. It's really the quotient of the complex plane by some lattice, and thus, is a torus.

In particular, for the three distinct points $(e_{1}, 0), (e_{2}, 0), (e_{3}, 0)$ on the elliptic curve, we can consider two integrals of stuff to get a lattice spanned by $\omega_{1}, \omega_{2}$.

Now we define the Weierstrass $\wp$-function for this lattice by
$$
\wp_{\Lambda}(z) = 4 \left( \frac{1}{z^{2}} + \sum_{\omega \in \Lambda \setminus \{ 0 \}} \left( \frac{1}{(z - \omega)^{2}} - \frac{1}{\omega^{2}} \right) \right).
$$
Since it is doubly periodic with periods given by $\Lambda$, and its derivative satisfies
$$
\wp'_{\Lambda}(z)^{2} = \wp_{\Lambda}(z)^{3} + A \wp_{\Lambda}(z) + B,
$$
we have a bijection $\mathbb{C} / \Lambda \to E(\mathbb{C})$ by $z \mapsto (\wp_{\Lambda}(z), \wp_{\Lambda}'(z))$. If we're willing to believe this is actually a homeomorphism (it's actually an analytic group isomorphism with the [[Algebraic Geometry --- math-176/notes/Elliptic curves#The elliptic curve group|elliptic curve group]]) where $E(\mathbb{C})$ is thought of as a [[Mathematical Analysis I --- math-131/notes/Subspaces|subspace]], then $E(\mathbb{C})$ must just be the torus.

All elliptic curves are the same as Riemann surfaces, but if you have a finer notion of maps, then you can tell them apart.

##### _example:_ the non-compact Poincaré models

As open subsets of $\mathbb{C}$, the upper half plane $\mathbb{H}$ and the open disc $\mathbb{D}$ are both Riemann (sub)surfaces of $\mathbb{C}$. In fact, there's a bijection $\mathbb{H} \to \mathbb{D}$ called the Cayley transform —
$$
\tau \mapsto \frac{\tau - i}{\tau + i}
$$
In fact, if we think of the real projective line $\mathbb{R} \mathbb{P}$ as the boundary of the upper-half plane, the Cayley transform extends to send this to the circle $S^1$ with the point at infinity sent to $1$.

The disc $\mathbb{D}$ has a bijection to the hyperboloid $S^+ = \{ (x, y, z) \mid x^{2} + y^{2} - z^{2} = - 1 \}$  that looks like stereographic projection. (This is called the Minkowski model and parametrise points in $2 + 1$ relativistic physics).

##### _exercise:_ the left action that induces higher genus Riemann surfaces

Choose a subgroup $\Gamma \le \operatorname{PSL}_{2}(\mathbb{R}) = \operatorname{SL}_{2}(\mathbb{R}) / \{ \pm I \}$. Show that $\Gamma$ [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ (left) group action|acts]] on the (compactified) upper half plane $\mathbb{H}^* = \mathbb{H} \cup \{ i \infty \}$ on the left by
$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix} \cdot \tau = \frac{a \tau + b}{c \tau + d}.
$$

Note that $\operatorname{PSL}_{2}(\mathbb{R})$ isn't just a group, but also a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]]. One can see this by noticing that the adjoint representation of $\operatorname{PSL}_{2}(\mathbb{R})$ is an irreducible $3$-dimensional representation that has an injective [[Abstract Algebra I --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|homomorphism]] into in $\operatorname{SL}_{3}(\mathbb{R})$. Of course, $\operatorname{SL}_{3}(\mathbb{R})$ is a submanifold of $\mathbb{R}^9$. Pulling back topologies (or [[Mathematical Analysis I --- math-131/notes/Metric spaces#_definition_ metric space, metric|metrics]]) we get the topology on $\operatorname{PSL}_{2}(\mathbb{R})$.

If we consider $X = \Gamma \setminus \mathbb{H}$ to be the set of all [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ orbit|orbits]] $[\tau]$ of $\tau \in \mathbb{H}$, we can make it a topological space with the quotient topology ($U \subseteq X$ is open if and only if $\pi ^{\text{pre}}(U)$ is open, for the projection $\pi : \tau \mapsto [\tau]$). 

$X$ is connected because $\pi$ it is the image of a continuous map from the connected space $\mathbb{H}$. It's second countable, again because $\mathbb{H}$ is. We compactify it later. It only remains to show $X$ is Hausdorff.

For $X$ to be Hausdorff, we need each of the orbits to be closed in $\mathbb{H}$. This happens exactly when $\Gamma$ acts properly dicontinuously — points in different orbits have open neighbourhoods that never intersect, even after action by $\Gamma$. Equivalently, $\Gamma$ is discrete — it has the [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete topology]] as a [[Mathematical Analysis I --- math-131/notes/Subspaces#_theorem _ the subspace topology|subspace]]. We call such subgroups of $\operatorname{PSL}_{2}(\mathbb{R})$ Fuchsian. For example $\operatorname{PSL}_{2}(\mathbb{Z})$ is Fuchsian.

The atlas is the one inherited from $\mathbb{H}$ (pushforward sheaf?).