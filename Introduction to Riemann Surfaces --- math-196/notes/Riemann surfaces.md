---
tags:
- diff-geo
- math-196/1
---

##### _definition:_ (compact, connected) Riemann surface, (holomorphic) atlas

A (compact, connected) Riemann surface is a pair of a [[Mathematical Analysis I --- math-131/notes/Compactness#_definition _ compact|compact]], [[Mathematical Analysis I --- math-131/notes/Connectedness#_definition _ connectedness|connected]], Hausdorff topological space $S$ and a holomorphic atlas $\mathcal{A}$. 

That is, $\mathcal{A}$ is an open cover $\{ U_{\alpha} \}$ such that each $U_{\alpha}$ is homeomorphic (with the homeomorphism being $\phi_{\alpha}$) to an open, connected subset of $\mathbb{C}$. Further, each "transition map" $\phi_{\beta} \circ \phi_{\alpha} ^{-1}$ is a [[Complex Analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$|holomorphic]] function $\phi_{\alpha}(U_{\alpha} \cap U_{\beta}) \to \phi_{\beta}(U_{\alpha} \cap U_{\beta})$.

The Hausdorff condition is a reasonability condition on topological spaces — for any two distinct points in the topological space, we can separate them in $\mathbb{C}$.

Usually we topologise $S$ so that the open cover is open.

The main theorem that we want to learn is that compact connected Riemann surfaces are completely classified —

##### _theorem:_ the uniformisation theorem

A compact connected Riemann surface $S$ is one of three things
1) the Riemann sphere $\mathbb{P}^1(\mathbb{C})$ (the one-point compactification of $\mathbb{C}$) with genus $0$
2) Euclidean — a torus $\mathbb{C} / \Lambda$ for some lattice $\Lambda$ with genus $1$
3) hyperbolic — $S$ is the right cosets of the upper half plane $\mathbb{H}$ modulo some group $\Gamma$ with genus $g \ge 2$.

When we say "is", we mean something specific.

##### _example:_ the Riemann sphere

The (topological space of the) sphere is exactly the sphere $S^2$ sitting in $\mathbb{R}^3$. We can cover this with one open set $U_{1}$ staying away from the south pole, and another $U_{2}$ staying away from the north pole. Both of these have an obvious homeomorphism to $\mathbb{C}$ itself by stereographic projection. The transition map is $z \mapsto -1/z$ which is indeed holomorphic on $\mathbb{C}$. 

Applying this to the sphere is essentially flipping the sphere.