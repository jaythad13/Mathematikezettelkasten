---
tags:
- math-199DR/26
- cx-geo
---

Let $X$ be a compact, connected Riemann surface.

It's a fact of topology that [[Topology --- math-147/notes/Classification of surfaces#_theorem _ triangulation of low-dimensional manifolds (Moise–Bing)|every surface is triangulable]] — that is, $X$ is homeomorphic to a [[Simplicial homology and graph theory --- math-145/notes/Simplicial complexes#_definition _ simplicial complex|simplicial complex]] $X$ with all maximal [[Simplicial homology and graph theory --- math-145/notes/Simplicial complexes#_definition _ face, coface|faces]] of dimension $2$. This, allows us to use all of the theory of [[Simplicial homology and graph theory --- math-145/notes/Simplicial homology|simplicial homology]] on $X$. Since $X$ is $2$-dimensional, compact, and connected, we don't really care about anything except for the first homology which captures $1$-holes. Note that $\mathrm{H}_{1}(X)$ is the abelianisation of the fundamental group $\pi_{1}(X)$.

Typically, for a genus $g$ curve — a $g$-holed torus, the homology looks like $\mathbb{Z}^{2g}$ (recall that the torus $S^1 \times S^1$ has abelian fundamental group $\mathbb{Z} \times \mathbb{Z}$).

The primary thing we do with homology is de Rham cohomology by [[Riemann surfaces and algebraic curves --- math-199DR/notes/Integrating forms|integrating over it]]. That is, since, by Stokes' theorem we don't have to care about integrating over anything that is a boundary, we have a homomorphism $\mathrm{H}_{1}(X) \to \Omega^1(X)^\vee$ by "integrating over".

##### _definition:_ periods

Given $\gamma \in \mathrm{H}^1(X)$, a period is a functional on holomorphic $1$-forms, in the image of $I : \mathrm{H}^1(X) \to \Omega^1(X)^\vee$ by
$$
I \gamma : \omega \mapsto \int_{\gamma} \omega.
$$

The set of all periods in $\Omega^1(X)^\vee$ is denoted $\Lambda$.

##### _definition:_ the Jacobian

The Jacobian of $X$ is the complex manifold $\operatorname{Jac} X = \Omega^1(X)^\vee / \Lambda$.

##### _example:_ the Jacobian of the torus

We've seen that a torus $\mathbb{C} / \Lambda$ [[Riemann surfaces and algebraic curves --- math-199DR/notes/Linear equivalence of divisors#_theorem _ Abel's theorem for elliptic curves|is isomorphic to its Jacobian]]. (This is confusing notation but we mean a torus defined by a lattice $\Lambda$).

Unfortunately, we don't in general have that Riemann surfaces are isomorphic to their Jacobians — for one, the Jacobian tends to look like a dimension $g$ complex manifold $(\mathbb{C} / \mathbb{Z}^{2})^g$ while Riemann surfaces are of course (complex) dimension $1$.

##### _definition:_ general Abel-Jacobi map

Given a choice of base point $p_{0} \in X$, the general Abel-Jacobi map is $A : \operatorname{Div} X \to \operatorname{Jac} X$ extended linearly from
$$
A(p) : \omega \mapsto \int_{p_{0}}^p \omega \pmod \Lambda.
$$

Of course, we should verify that this is well defined even modulo $\Lambda$. This follows because any two paths from $p_{0}$ to $p$ differ by a cycle $\gamma$ (though not necessarily a boundary). Thus, the two definitions of $A(p)$ differ only by some period $I \gamma \in \Lambda$.

Note that the restriction to degree zero divisors is particularly nice. Since we can pair positive and negative points up, we don't have to care about the base point — 

##### _definition:_ Abel-Jacobi map

The Abel-Jacobi map is $A_{0} : \operatorname{Div}_{0} X \to \operatorname{Jac} X$ given by
$$
A_{0}(D) : \omega \mapsto \sum_{j = 1}^n \int_{q_{j}}^{p_{j}} \omega
$$
where $D(p_{j}) = 1$ and $D(q_{j}) = -1$ for all $j$ (and $D$ is supported nowhere else on $X$).

Abel's theorem will be to investigate the kernel of $A_{0}$. We want to show that it is just the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Divisors#_definition _ principal divisor|principle divisors]] $\operatorname{PDiv} X$.