---
tags:
- math-199DR/7
- math-199DR/8
- cx-geo
- diff-geo
---

Let $X, Y$ be [[Mathematical Analysis I --- math-131/notes/Compactness#_definition _ compact|compact]], [[Mathematical Analysis I --- math-131/notes/Connectedness#_definition _ connectedness|connected]] Riemann surfaces with (maximal) holomorphic atlases $(\phi_{\alpha}, U_{\alpha})$ and $(\psi_{\beta}, V_{\beta})$ indexed by $\alpha \in \mathcal{I}$ and $\beta \in \mathcal{ J}$ respectively.

Holomorphisms have very nice behaviour locally. Just as the nice behaviour of holomorphic functions on the plane translates to nice topological properties like [[Complex Analysis --- math-135/notes/The argument principle and winding number#_theorem _ open mapping theorem|open mapping]], [[Complex Analysis --- math-135/notes/The argument principle and winding number#_definition _ winding number|winding number]], and [[Complex Analysis --- math-135/notes/The argument principle and winding number#_lemma _ the "$n$-to-one" lemma|non-injectivity theorems]] like the $n$-to-one lemma, so does the behaviour of holomorphisms (we've seen some of this nice behaviour [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#Theorems from complex analysis|already]]). Here, we will see that holomorphisms preserve [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological invariants of a surface|topological invariants of a surface]].

### Multiplicity

The local normal form allows us to write every holomorphic map as locally a power map. Eventually we will turn this into a global property.

##### _theorem:_ local normal form

Let $\pi : X \to Y$ be a non-constant function [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphic]] near $p \in X$. Then there exists a unique positive integer $m$ such that for all charts $\psi : V \to \mathbb{C}$ centred at $\pi(p)$ (sending $\pi(p)$ to $0$) there exists a chart $\phi : U \to \mathbb{C}$ centred at $p$ such that $\psi \circ \pi \circ \phi ^{-1}(z) = z^m$.

###### _proof sketch:_

##### _definition:_ multiplicity

Given $\pi : X \to Y$ (non-constant, holomorphic near $p \in X$) the unique $m$ of the local normal form, is called the multiplicty of $\pi$ at $p$, denoted $\operatorname{mult}_{p}\pi$.

Multiplicity has an interpretation in terms of stalks. [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#The sheaf-theoretic view|Recall]] that a holomorphism $\pi$ induces a map on stalks
$$
\pi^* : \mathcal{O}_{Y, \pi(p)} \to \mathcal{O}_{X, p}
$$
by
$$
\pi^* : f \mapsto \pi^*f = f \circ \pi
$$
that is a $\mathbb{C}$-algebra homorphism and a local ring homomorphism sending the unique maximal ideal of [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ holomorphic functions|holomorphic functions]] vanishing at $\pi(p)$, $\mathfrak{m}_{Y, \pi(p)}$ into $\mathfrak{m}_{X, p}$. In fact, we can say exactly what it is. 

##### _proposition:_ the map on stalks has image $\mathfrak{m}_{X, p}^m$

For $\pi : X \to Y$ having multiplicity $m$ at $p$, the induced map on stalks $\pi^* : \mathcal{O}_{Y, \pi(p)} \to \mathcal{O}_{X, p}$ has ${\pi^*}^\text{img}(\mathfrak{m}_{Y, \pi(p)}) = \mathfrak m_{X, p}^m$.

##### _example:_ charts have multiplicity $1$

Since [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_examples _ dumb examples of holomorphisms|they are holomorphisms]] to $\mathbb{C}$ and are injective, charts have multiplicity $1$ at each point. Otherwise the $n$-to-one lemma [[Complex Analysis --- math-135/notes/The argument principle and winding number#_lemma _ the "$n$-to-one" lemma|from complex analysis]] would force them 

Using local coordinates and differentiation we can we can get the 

##### _proposition:_ calculating multiplicities



The upshot of this theorem is that the points where multiplicity is greater than $0$ are discrete.

##### _definition:_ ramification point, branch point

A point $p$ in $X$ where $\pi : X \to Y$ has multiplicity greater than $1$ are ramification points of $f$.

Their images of ramification points under $\pi$ are branch points of $\pi$.

##### _example:_ ramification points of an affine plane curve

If a smooth affine plane curve is given by the points $f(x, y) = 0$ and $\pi : (x, y) \mapsto x$, the ramificiation points are where ${ \partial f } / { \partial y } = 0$.

For a circle floating somewhere in space, the two antipodal points that intersect a line parallel to the $x$-axis have many points attracted to the same image as them.

### Degree

Now we can define and prove the constancy of the degree of a map.

##### _definition:_ degree at a point

Suppose $\pi : X \to Y$ is a (non-constant) holomorphism. For each $y \in Y$, the degree of $\pi$ at $y$ is 
$$
d_{y} \pi = \sum_{p \in \pi^\text{pre}(\{ y \})} \operatorname{mult}_{p} \pi.
$$

##### _theorem:_ degree is constant

Given $\pi : X \to Y$, the function $y \mapsto d_{y} \pi$ is constant.

##### _definition:_ degree of a map

The degree of a (non-constant) holomorphism is constant.

##### _corollary:_ isomorphism is determined by degree

If (non-constant) $\pi  : X \to Y$ has $\operatorname{deg} \pi = 1$, then $\pi$ is an [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ biholomorphism/isomorphism, automorphism|isomorphism]].

###### _proof:_

If $\pi$ has degree $1$ there can't be any branch points, so it is injective. [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ maps from compact Riemann surfaces are surjective|We've shown]] that it is surjective (since $X, Y$ are compact). [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_theorem _ inverse holomorphism theorem|Injective holomorphisms]] are isomorphisms onto their image. So we're done.

### Ramifications for meromorphic functions

All of this theory has huge *ramifications* for [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ meromorphic|meromorphic functions]] $f : X \to \mathbb{C}$ since [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ meromorphic functions are maps to the Riemann sphere|they correspond to holomorphisms to the Riemann sphere]] $\pi_{f} : X \to \mathbb{C}_{\infty}$.

##### _lemma:_ multiplicities of meromorphic functions

Given $f : X \to \mathbb{C}$ meromorphic and $\pi_{f} : X \to \mathbb{C}_{\infty}$ the corresponding holomorphism,
1) at poles, $\operatorname{mult}_{p} \pi_{f} = - \operatorname{ord}_{p} f$
2) at zeroes, $\operatorname{mult}_{p} \pi_{f} = \operatorname{ord}_{p} f$
3) everywhere else $\operatorname{mult}_{p} \pi_{f} = \operatorname{ord}_{p}(f - f(p))$

###### _proof sketch:_

I trust Noah.

### Hurwitz' formula

Hurwitz' formula allows us to relate the topology of two Riemann surfaces given the topological data of a map between them.

##### _theorem:_ Hurwitz' formula

Given (a non-constant holomorphism of compact Riemann surfaces) $\pi : X \to Y$
$$
2g_{X} - 2 = \operatorname{deg} \pi (2g_{Y} - 2) + \sum_{p \text{ ramified}} (\operatorname{mult}_{p} \pi - 1).
$$

###### _proof:_

Triangulate $Y$ with vertices at branch points. Pull the triangulation back under $\pi$. Everything gets multiplied by $\operatorname{deg} \pi$ except the number of vertices which we have to correct for by adding the multiplicity term.

### Example

There are lots of good examples of the kinds of behaviour we're talking about.

##### _example:_ meromorphic functions on the Riemann sphere

Meromorphic functions on the [[Introduction to Riemann Surfaces --- math-199DR/notes/Riemann surfaces#_example _ the Riemann sphere and the complex projective line|Riemann sphere/complex projective plane]] have really nice behaviour. We've seen earlier that [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_example _ meromorphic functions on the Riemann sphere and projective line|they are just rational functions]]. For a rational function that looks like
$$
\pi(z) = \frac{\prod_{i = 1}^n(z - z_{i})^{\alpha_{i}}}{\prod_{j = 1}^m (z - p_{j})^{\beta_{j}}}.
$$

Clearly, at $z_{i}$, $\pi$ has multiplicity $\alpha_{i}$ and at $p_{j}$ it has multiplicity $\beta_{j}$. At $\infty$, to find the multiplicity, we essentially want the absolute value of the order of $\pi(1 / z)$ at $0$. But this is just $\left\lvert  \sum_{i} \alpha_{i} - \sum_{j} \beta_{i}  \right\rvert$ (as long as the difference isn't $0$ in which case things get annoying, but we will ignore that).

We're going to (very weakly) check that degree is constant by calculating it at $\infty$ and $0$. The preimages of infinity are just the poles $p_{j}$ which each have multiplicity $\beta_{j}$, so the degree is $\sum_{j} \beta_{j} - \max \{ 0, \sum_{j} \beta_{j} - \sum_{i} \alpha_{j} \}$ the last term adds the order of a possible pole at infinity. By thinking we can see that this is just saying the degree is $\max \left\{  \sum_{i} \alpha_{i}, \sum_{j} \beta_{j}  \right\}$. By similar analysis at $0$ we again see $\deg \pi = \max \left\{ \sum_{i} \alpha_{i}, \sum_{j} \beta_{j} \right\}$.

This essentially because we're solving for
$$
\prod_{i} (z - z_{i})^{\alpha_{i}} = y \prod_{j} (z - p_{j})^{\beta_{j}}
$$
to get the degree of $\pi$ at $y$. By setting each side to zero this can be solved the desired number of times.

##### _example:_ meromorphic functions and automorphisms of elliptic curves

Consider the elliptic curve $X$ consisting of the one point compactification of its complex points — $\{ (x, y) \in \mathbb{C}^2 \mid y^{2} = x^3 + 13 \} \cup \{ \infty \}$. Consider the meromorphic function $\pi : X \to \mathbb{C}_{\infty}$ by $\pi : (x, y) \mapsto \frac{1 + y}{2}$.

Since $X$ is "cubic", most points have $3$ pre-images. Since the ramification points are discrete, the degree must be $3$.

$\pi$ is ramified at $(0, \pm 1)$ which have corresponding branch points $1$ and $0$ and is also ramified at $\infty$. Note that the non-$\infty$ points are those where the partial with respect to $x$ of the function defining $X$ is zero which is because $\pi$ looks like projection onto the $y$ axis (but isn't quite). Another way to see this is that at the (non-$\infty$, $\pi$ looks like
$$
\pi(x, y) = \frac{1 \pm \sqrt{ x^3 + 1 }}{2} = \frac{1 \pm (1 + x^3 / 2 + O(x^6))}{2}
$$
so should locally look like a cubic.

By Hurwitz formula, since the multiplicity at each ramification point is $3$, we get
$$
2 g_{X} - 2 = \deg \pi (2 g_{\mathbb{C}_{\infty}} - 2) + \sum_{p \in \{ (0, \pm {1}), \infty \}} \operatorname{mult}_{p} \pi  - 1.
$$

If $\xi_{6}$ is a sixth root of unity, then $\rho_{X} : X \to X$ by $\rho(x, y) = (\xi_{6}^2, \xi_{6}^3)$ is an automorphism (notice that $\rho_{X}^6$ is the identity).

Similarly on the elliptic curve $Y = \{ (x, y) \in \mathbb{C}^{2} \mid y^{2} = x^{3} + x \} \cup \{ \infty \}$, there is an automorphism $\rho_{Y} : Y \to Y$ by $(x, y) \mapsto (\xi_{4}^{2} x, \xi_{4}^3 y) = (-x, -iy)$.
