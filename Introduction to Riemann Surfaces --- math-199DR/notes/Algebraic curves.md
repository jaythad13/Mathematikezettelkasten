---
tags:
- math-199DR/20
- cx-geo
- alg-geo
---

Let $X$ be a compact Riemann surface.

Algebraic curves have the nicest properties of any Riemann surface — they are the compactifications of zero sets of polynomials. 

Typically, we would define algebraic curves to be these compactifications of zero sets, but here we will just define them as having the property we want — enough meromorphic functions.

##### _definition:_ separating points, separating tangents

A subset of $\mathcal{M}_{X}(X)$ is said to separate points if for every pair of points $p, q$ it contains a meromorphic function $f$ with $f(p) \neq f(q)$.

It is said to separate tangents if for each point $p \in X$ there is a meromorphic function with ([[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ meromorphic functions are maps to the Riemann sphere|associated map to the Riemann sphere having]]) [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ multiplicity|multiplicity]] $1$ at $p$.

It's obvious what separating points means, but separating tangents is more subtle. Separating tangents can be thought of as either having a map to the Riemann sphere that induces an isomorphism of tangent/cotangent spaces, or (when $f$ isn't a pole) having a [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_example _ charts have multiplicity $1$|chart]] at $p$ that extends to a meromorphic function on all of $X$.

It's easy to see that an "algebraically defined curve" $X$ has $\mathcal{M}_{X}(X)$ separating points and tangents — for any pair of points $p, q \in X$ there is an open neighbourhood containing both of them where $X$ looks like the zero set of some $r \in \mathbb{C}[x_{1}, \dots, x_{n}]$ (to be exact, this is true for quasi-projective schemes of finite type over some field). If $p = (p_{1}, \dots, p_{n})$ and $q = (q_{1}, \dots, q_{n})$ differ in the first coordinate choose $f(x_{1}, \dots, x_{n}) = x_{1} - p_{1}$. This separates $p$ and $q$ and has multiplicity $1$ at $p$.

It's harder to show that if a Riemann surface has $\mathcal{M}_{X}(X)$ separating points and tangents that it is then defined by a polynomial, but it can be done. From $z$, a meromorphic function of [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ degree of a map|degree]] $n$, and another meromorphic function $f$ on $X$ we can create functions in $z$ that look like symmetric functions of $f$ applied to the $n$ pre-images of each (non-[[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ ramification point, branch point|branched]] points) of $\mathbb{C}_{\infty}$. That is,
$$
\begin{align}
r_{k}(z) = (-1)^n \sum_{n_{1} < \dots < n_{k}}^n f(p_{n_{1}}) \cdots f(p_{n_{k}})
\end{align}
$$
Then it turns out that
$$
f^n + r_{1}(z) f^{n - 1} + \dots + r_{n - 1}(z) f + r_{n}(z) = 0
$$
so mapping $p \mapsto (z, f)$ gives $X$ as an algebraic curve.

Thus, we define an algebraic curve by this "having enough meromorphic functions" property.

##### _definition:_ algebraic curve

A compact Riemann surface $X$ is an algebraic curve if $\mathcal{M}_{X}(X)$ separates points and tangents of $X$.

It turns out that all compact Riemann surfaces separate points and tangents, and are thus algebraic curves. One can either show this generally for compact complex manifolds using cohomology theory from complex analytic geometry or just for Riemann surfaces by showing that there exists a non-constant meromorphic function on every compact Riemann surface and then using the Narasimhan proof to get algebraicity.

### Laurent series approximation

### Function fields as field extensions