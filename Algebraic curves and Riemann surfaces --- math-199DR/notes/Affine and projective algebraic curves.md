---
tags:
- math-199DR
- alg-geo
- cx-geo
---

For us, the most important examples of algebraic curves will be those coming from algebraic geometry — those (locally) cut out by polynomials in affine space $\mathbb{C}^n$ or projective space $\mathbb{C} \mathbb{P}^n$.

### Affine plane curves

We first look at the simplest case — curves embedded in the affine plane.

Affine plane curves are the zero loci in $\mathbb{C}^{2}$ of polynomials in $\mathbb{C}[x, y]$. Certainly when these take the forms of a graph (when the polynomial is given by $y - g(x)$) it's clear how to give them the structure of a Riemann surface.

##### _proposition:_ graphs of holomorphic functions give Riemann surfaces

For $U \subseteq \mathbb{C}$ connected, the graph of any [[Complex analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$|holomorphic]] $g : U \to \mathbb{C}$ defines a Riemann surface as a [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subspace]] $X = \{ (x, g(x)) \mid x \in U \} \subseteq \mathbb{C}^{2}$.

###### _proof sketch:_

There is a single chart $X \to U$ by projection in the first coordinate. This is clearly continuous and bijective. It is also open since it is the restriction of the open map $\mathbb{C}^{2} \to \mathbb{C}$ (which is open because you can check openness of projection maps from the product space by using the basis of products of open sets).

---

Using the [[Calculus --- spivak/notes/Inverse and implicit functions#_theorem _ the implicit function theorem|implicit function theorem]], affine plane curves are locally graphs (for non-singular polynomials). Thus, they are topologically Riemann surfaces, and it only remains to show that the charts this local expression defines are compatible.

##### _definition:_ non-singular polynomials

A polynomial $f \in \mathbb{C}[x_{1}, \dots, x_{n}]$ is **non-singular at a point** $p$ with $f(p) = 0$ if the total derivative $Df = \left( \frac{ \partial f }{ \partial x_{1} }, \dots, \frac{ \partial f }{ \partial x_{n} } \right)$ is non-zero at $p$.

$f$ is **non-singular** if it is non-singular at each $p \in \mathbb{C}^{2}$ that has $f(p) = 0$.

---

##### _definition, proposition:_ affine plane curves

The **affine plane curve** defined by a polynomial $f \in \mathbb{C}[x, y]$ is the zero locus of $f$, a subspace $X = \{ (x, y) \mid f(x, y) = 0 \} \subseteq \mathbb{C}^{2}$.

If $f$ is non-singular it has a natural Riemann surface structure.

###### _proof:_

By the implicit function theorem and the non-singularity of $f$, in a small neighbourhood of each point $p \in X$, we can write $x = g(y)$ or $y = g(x)$. Thus, $X$ is locally a Riemann surface and then locally $\mathbb{C}$. It only remains to show that these charts are compatible.

Suppose $\varphi : U \to \mathbb{C}$ and $\psi : V \to \mathbb{C}$ are two charts. If both are given by restrictions of $pr_{x} : \mathbb{C}^{2} \to \mathbb{C}$, then $\varphi \circ \psi ^{-1}$ is the identity on $\varphi^\text{img}(U \cap V)$ and thus, clearly holomorphic. Else, one is a restriction of $pr_{x}$ and the other of $pr_{y}$. On an open neighbourhood $W$ of $p$, suppose $X$ looks like $\{ (x, g(x)) \mid x \in W \}$. Then $pr_{x \mid X}^{-1} \circ pr_{y \mid X} : \mathbb{C} \to \mathbb{C}$ is given by $x \mapsto (x, g(x)) \mapsto g(x)$ which is holomorphic since polynomials are holomorphic. 

---

It is a difficult result that if $f$ is irreducible, then the affine plane curve defined by it is connected. 

##### _example:_ a connected Riemann surface

Let $h \in \mathbb{C}[x]$ be non-square polynomial. Then $f(x, y) = y^{2} - h(x)$ is an irreducible polynomial. Let $X$ be its zero locus.

Note that $\partial f / \partial y = 2y$ and so is only $0$ when $y$ is. If $h$ has distinct roots, then there are no points on $X$ where $h(x) = 0$ and $h'(x) = 0$. Thus, there are no points on $X$ where $\partial f / \partial y = \partial f / \partial x = 0$. That is, if $h$ has distinct roots, $f$ defines a (connected) Riemann surface.

---

However, affine plane curves $X$ are always non-compact — for each $x_{0} \in \mathbb{C}$ there are roots of the polynomial $f(x_{0}, y)$, giving points on $X$ at any distance from the origin in $\mathbb{C}^{2}$.

### Projective plane curves

If $f \in \mathbb{C}[x, y, z]$ is homogeneous, then the question of whether it vanishes at points in [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Complex projective space#_definition _ complex projective $n$-space|the complex projective plane]] $\mathbb{C} \mathbb{P}^2$ is well-defined. Intersecting the zero locus with the standard charts on $\mathbb{C} \mathbb{P}^{2}$, we get zero loci on copies of $\mathbb{C}^{2}$. If $f$ is non-singular on the projective plane, these affine zero loci are non-singular, and thus, Riemann surfaces. We can glue these Riemann surfaces together to get a compact Riemann surface.

For this we need a useful result of Euler.

##### _lemma:_ Euler's formula for homogeneous polynomials

If $f \in \mathbb{C}[x_{0}, \dots, x_{n}]$ is homogeneous of degree $d$, then
$$
f = \frac{1}{d} \sum_{i = 1}^n x_{i} \frac{ \partial f }{ \partial x_{i} }.
$$

###### _proof sketch:_

By linearity of the operator applied to $f$ on the right hand side, it suffices to show this for monomials. For monomials (even mixed), this is just the power rule.

---

##### _proposition:_ non-singular projective curves have non-singular charts

If $f \in \mathbb{C}[x, y, z]$ is a homogeneous polynomial defining a projective plane curve $X \subseteq \mathbb{C} \mathbb{P}^{2}$, then $f$ is non-singular at all points in $\mathbb{C} \mathbb{P}^{2}$ if and only if each $X_{i} = X \cap U_{i}$ is a smooth affine plane curve.

###### _proof:_

Suppose $f$ is singular at $(x_{0} : y_{0} : z_{0}) \in \mathbb{C} \mathbb{P}^{2}$ and (without loss of generality) that $x_{0} \neq 0$. Consider $U_{x} \cap X = \{ (y, z) \mid g(y, z) = 0 \} \subseteq \mathbb{C}^{2}$ for $g(y, z) = f(1, y, z)$. Note that $\frac{ \partial f }{ \partial x }$ is homogeneous (taking partials drops the degree of all terms containing $x$ by $1$ and kills all terms that don't contain $x$). Thus, $f$ is also singular at the equivalent point $(1 : y_{0} / x_{0} : z_{0} / x_{0})$. Then since $\frac{ \partial f }{ \partial y } (1, y_{0}, z_{0}) = \frac{ \partial g }{ \partial y }(y_{0}, z_{0})$ and similarly for the $\partial z$, $g$ is singular at $(y_{0}, z_{0})$.

Suppose $f$ is non-singular. Consider $(y_{0}, z_{0}) \in U_{x} \cap X$. Note that then $f(1 : y_{0} : z_{0}) = 0$. Since $f(1 : y_{0} : z_{0}) = 0$, and by Euler's formula, we have
$$
0 =  \frac{ \partial f }{ \partial x }(1 : y_{0} : z_{0}) + \frac{y_{0}}{x_{0}} \frac{ \partial f }{ \partial y } (1 : y_{0} : z_{0}) + \frac{z_{0}}{x_{0}} \frac{ \partial f }{ \partial z } (1 : y_{0} : z_{0}).
$$
Since $f$ is non-singular, not all three partials are zero. Then, for the equation to be satisfied, at least two must be non-zero. Thus, at least one of the partials of $g(y, z) = f(1 : y : z)$ is non-zero.

---

These non-singular charts do in fact glue. We demonstrate this in one case. Suppose $p \in X_{0} \cap X_{1}$, say and note that the charts $\varphi_{0} : X_{0} \to \mathbb{C}^{2} \to \mathbb{C}$ are given by $(x : y : z) \mapsto (y / x, z / x) \mapsto y / x$ or $z / x$. Suppose $\varphi_{0} : (x : y : z) \mapsto y / x$ and $\varphi_{1} : (x : y : z) \mapsto z / y$. Then $\varphi_{0}^{-1}(w) = (1 : w : h(w))$ for some polynomial $h$, and $\varphi_{1} \circ \varphi_{0}^{-1}(w) = h(w) / w$. This is holomorphic on $X_{0} \cap X_{1}$ where $w \neq 0$. Similar considerations show compatibility for all pairs of charts.

##### _definition:_ projective plane curve

Let $f \in \mathbb{C}[x, y, z]$ be a non-singular homogeneous polynomial. Then the **smooth projective plane curve** $X$ defined by it is the zero locus in $\mathbb{C} \mathbb{P}^{2}$ with the Riemann surface structure above.

If $f$ has degree $d$, $X$ is said to be a curve of degree $d$.

---

Note that projective plane curves are compact — they are closed subsets (since zero loci are closed) of the compact manifold $\mathbb{C} \mathbb{P}^{2}$, and [[Topology --- math-147/notes/Compactness#_proposition _ closed subspaces of compact spaces are compact|thus]], compact

### Projective curves and complete intersections

Since $\mathbb{C} \mathbb{P}^n$ is an $n$-dimensional complex manifold, we should expect that imposing $n - 1$ equations would cut down to a $1$-dimensional complex manifold — a Riemann surface. This gives the notion of a complete intersection.

##### _definition:_ complete intersection curve

A **(smooth) complete intersection curve** $X$ in $\mathbb{C} \mathbb{P}^n$ is the zero locus of $n - 1$ homogeneous polynomials $f_{1}, \dots, f_{n - 1}$ such that the derivative of $f = (f_{1}, \dots, f_{n})$ has maximal rank $n - 1$ at every point of $X$.

It has the structure of a compact Riemann surface, with local coordinates $x_{i} / x_{j}$ at every point where $x_{j} \neq 0$.

---

However, complete intersections are not the only 

##### _example:_ the twisted cubic

The twisted cubic is the image of $H : \mathbb{C} \mathbb{P}^1 \to \mathbb{C} \mathbb{P}^3$ by $(x : y) \mapsto (x^{3} : x^{2} y : xy^{2} : y^{3})$. This curve is the zero locus of three polynomials (and cannot be written as the zero locus of two) — $f_{1}(x_{0} : x_{1} : x_{2} : x_{3}) = x_{0} x_{3} - x_{1} x_{2}$, $f_{2}(x_{0} : x_{1} : x_{2} : x_{3}) = x_{0} x_{2} - x_{1}^{2}$ and $f(x_{0} : x_{1} : x_{2} : x_{3}) = x_{1} x_{3} - x^{2}$.

However, near any point on the curve, only two of the three equations are necessary, so it really is a Riemann surface in $\mathbb{C} \mathbb{P}^3$.

---

This motivates the definition of a local complete intersection.

##### _definition:_ local complete intersection curve

A **(smooth) local complete intersection curve** $X$ in $\mathbb{C} \mathbb{P}^n$ is the zero locus of a set of homogeneous polynomials, such that near each point $p \in X$, the curve is described by $n - 1$ of the polynomials, and the derivative of the $n - 1$ polynomials has maximal rank $n - 1$ at $p$.

Again, it has the structure of a compact Riemann surface with local coordinates $x_{i} / x_{j}$ near every point.

---

Every Riemann surface (holomorphically) embedded in projective space is in fact a local complete intersection.