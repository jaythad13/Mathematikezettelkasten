---
tags:
- math-199DR/7
- math-199DR/8
- cx-geo
- diff-geo
---

Let $X, Y$ be [[Analysis --- math-131/notes/Compactness#_definition _ compact|compact]], [[Analysis --- math-131/notes/Connectedness#_definition _ connectedness|connected]] Riemann surfaces with (maximal) holomorphic atlases $(\varphi_{\alpha}, U_{\alpha})$ and $(\psi_{\beta}, V_{\beta})$ indexed by $\alpha \in \mathscr{I}$ and $\beta \in \mathscr{ J}$ respectively. Some of the set up doesn't require the compactness hypothesis but all of the serious results do.

Holomorphisms have very nice behaviour locally. Just as the nice behaviour of holomorphic functions on the plane translates to nice topological properties like [[Complex analysis --- math-135/notes/The argument principle and winding number#_theorem _ open mapping theorem|open mapping]], [[Complex analysis --- math-135/notes/The argument principle and winding number#_definition _ winding number|winding number]], and [[Complex analysis --- math-135/notes/The argument principle and winding number#_lemma _ the "$n$-to-one" lemma|pre-image counts]], so does the behaviour of holomorphisms (we've seen some of this nice behaviour [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#Theorems from complex analysis|already]]). Here, we will see that holomorphisms preserve [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological invariants of a surface|topological invariants of a surface]]. We often call this kind of behaviour "global".

### Multiplicity

The idea of a global property is usually to show that a local property is constant everywhere. This local property will be closely related to the multiplicity of a holomorphism — at a point $p$, the $m$ such that it is $m$-to-one near $p$.

The local normal form allows us to write every holomorphism as locally a power map.

##### _proposition:_ local normal form

Let $\pi : X \to Y$ be a non-constant function [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphic]] near $p \in X$. Then there exists a unique positive integer $m$ such that for each chart on $Y$, $\psi : V \to \mathbb{C}$ centred at $\pi(p)$, there exists a chart on $X$, $\varphi : U \to \mathbb{C}$ centred at $p$ such that $\psi \circ \pi \circ \varphi ^{-1}(z) = z^m$.

###### _proof:_

After fixing the chart $(\psi, V)$ choose some chart $\varphi_{0} : U_{0} \to \mathbb{C}$ centred at $p$. By definition, $\psi \circ \pi \circ \varphi ^{-1}_{0} = f$ is [[Complex analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$|holomorphic]], and thus, [[Complex analysis --- math-135/notes/Cauchy integral formula#_corollary _ the derivative form (holomorphic functions are smooth and analytic)|is a Taylor series]] — 
$$
f(w) = \sum_{n = m}^\infty a_{n} w^n
$$
where $m > 0$ since $f(0) = \psi(\pi(p)) = 0$. Notice that $f \neq 0$ since that would give us $\pi$ constant.

Write $f(w) = w^m g(w)$ where $g$ is holomorphic and $g(0) \neq 0$. Since $g$ doesn't vanish at the origin, [[Complex analysis --- math-135/notes/The complex logarithm#_definition _ logarithm, the logarithm|it has]] an $m$th root — we can write $g = h^m$ for some holomorphic function $h$. Thus, $f(w) = (w h(w))^m$ — $f$ has a holomorphic $m$th root. Write $\eta(w)$ for this $m$th root.

Since $\eta'(0) = h(0) \neq 0$, $\eta$ is invertible, and in fact, a homeomorphism near $0$. Then $\varphi = \eta \circ \varphi_{0}$ is a chart centred at $p$. Given $q$ in a vicinity of $p$ and $\varphi_{0}(q) = w$, we get $\varphi(q) = \eta(w)$. For each $z$ in the image of the chart, there is a unique choice of $w$ such that $z = \eta(w)$. Then
$$
\begin{align}
\psi \circ \pi \circ \varphi^{-1}(z) & = (\psi \circ \pi \circ \varphi_{0}^{-1}) \circ \eta^{-1}(z) \\
 & = f(w) \\
 & = \eta(w)^m \\
 & = z^m.
\end{align}
$$

$m$ is unique since it forces $\psi \circ \pi \circ \varphi ^{-1}$ to be $m$-[[Complex analysis --- math-135/notes/The argument principle and winding number#_lemma _ the "$n$-to-one" lemma|to-one]] in a region near $p$, forcing $\pi$ to also be $m$-to-one, regardless of the choice of $\psi$.

---

##### _definition:_ multiplicity

Given $\pi : X \to Y$ (non-constant, holomorphic near $p \in X$) the **multiplicity of $\pi$ at $p$** is the unique $m$ of the local normal form, denoted $\operatorname{mult}_{p} \pi$.

---

Multiplicity has an interpretation in terms of sheaves. [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#The sheaf-theoretic view|Recall]] that a holomorphism $\pi$ induces a map on stalks $\pi^\sharp_{p} : \mathscr{O}_{Y, \pi(p)} \to \mathscr{O}_{X, p}$ by $f \mapsto f \circ \pi$. It is a $\mathbb{C}$-algebra homorphism and a local ring homomorphism sending the unique maximal ideal of [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ holomorphic functions|holomorphic functions]] vanishing at $\pi(p)$, $\mathfrak{m}_{Y, \pi(p)}$ into $\mathfrak{m}_{X, p}$. In fact, the image of $\mathfrak m_{Y, \pi(p)}$ is exactly $\mathfrak m_{X, p}^m$.

##### _example:_ charts have multiplicity $1$

Since [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_examples _ dumb examples of holomorphisms|they are holomorphisms]] to $\mathbb{C}$ and are injective, charts have multiplicity $1$ at each point. Otherwise the $n$-to-one lemma [[Complex analysis --- math-135/notes/The argument principle and winding number#_lemma _ the "$n$-to-one" lemma|from complex analysis]] would force them to be non-injective.

---

While all of this theory is a nice way to define multiplicity and make sure it is chart invariant, there is a much cruder but useful way to calculate multiplicity — it doesn't even require charts to be centred at the requisite points! It follows from the observation that $\operatorname{mult}_{p} \pi$ is always at least $1$, and the remaining behaviour is determined by the derivative of the local normal form ($m z^{m - 1}$).

##### _proposition:_ calculating multiplicities

Consider $\pi : X \to Y$ is holomorphic near $p$ and a pair of charts $\varphi, \psi$ containing $p \in X$ and $\pi(p) \in Y$. Write $f = \psi \circ \pi \circ \varphi ^{-1}$. Then
$$
\operatorname{mult}_{p} \pi = 1 + \operatorname{ord}_{z_{0}} f'.
$$

###### _proof sketch:_

Let $\varphi(p) = z_{0}$ and $\psi(\pi(p)) = w_{0}$. Notice that $f(z) - f(z_{0})$ is "centred at $0$". Thus, its power series expansion about $z_{0}$ is $f(z) - f(z_{0}) = \sum_{n = \operatorname{mult}_{p}\pi}^\infty a_{n} z^n = w - w_{0}$ (even for arbitrary charts, the lowest degree term in the power series expansion is $\operatorname{mult}_{p} \pi$).

But then, differentiating on both sides, we get the desired result.

---

The upshot of this theorem is that the points where multiplicity is greater than $0$ are discrete.

##### _corollary:_ ramification points are discrete

For any holomorphism $\pi : X \to Y$, the set of points with multiplicity greater than $1$ is discrete.

###### _proof sketch:_

Since $\pi$ is non-constant, the corresponding map $\mathbb{C} \to \mathbb{C}$ is also non-constant, and thus, cannot have a non-discrete set of points where its derivative vanishes.

---

### Ramification

Points of high multiplicity are special enough to deserve a name, and so are their images. "Ramification" comes from the Latin word for branching. 

##### _example:_ ramifying and branching

By looking at the function $z^{2}$ from $\mathbb{C}$ to the two sheeted "square root" Riemann surface $X$, we can see that $\mathbb{C}$ covers $X$ twice at every point except $0$. It's also from "$0$" on $X$ that the two covers by $\mathbb{C}$ branch out.

---

##### _definition:_ ramification point, branch point

A point $p$ in $X$ where $\pi : X \to Y$ has multiplicity greater than $1$ are **ramification points** of $f$.

Their images of ramification points under $\pi$ are **branch points** of $\pi$.

---

##### _example:_ ramification points of an affine plane curve under projection

If a [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Affine and projective algebraic curves#_definition, proposition _ affine plane curves|smooth affine plane curve]] is given by the points $f(x, y) = 0$ and $\pi : (x, y) \mapsto x$, the ramification points are where ${ \partial f } / { \partial y } = 0$.

---

For a circle floating somewhere in space, the two antipodal points that intersect a line parallel to the $x$-axis have many points attracted to the same image as them.

### Degree

The degree of a holomorphic map counts the number of pre-images plus "tangency" information.

##### _definition:_ degree at a point

Suppose $\pi : X \to Y$ is a (non-constant) holomorphism. For each $q \in Y$, the **degree of $\pi$ at $q$** is 
$$
\deg_{q} \pi = \sum_{p \in \pi^\text{pre}(\{ q \})} \operatorname{mult}_{p} \pi.
$$

---

##### _theorem:_ degree is constant

Given $\pi : X \to Y$, the function $q \mapsto \deg_{q} \pi$ is constant.

###### _proof:_

We will show $y \mapsto \deg_{q} \pi$ is a locally constant function $Y \to \mathbb{Z}$. Since $Y$ is connected, it will follow that $\deg_{q} \pi$ is actually constant.

First, notice that $z \mapsto z^m$ on the open unit disc satisfies constancy of degree — every non-zero $z$ in $\mathbb{D}$ has $m$-many $m$th roots that map to it. $0$ is the only ramification point, and it has pre-image $0$ with multiplicity $m$. We will  show $\pi$ is the disjoint union of such maps on the pre-image of each point $q \in Y$.

Choose $q \in Y$. Let $\{ p_{1}, \dots, p_{n} \}$ be the pre-image of $q$. With a choice of chart centred at $q$, for each $p_{i}$ we have local normal forms with multiplicities $m_{i}$. By picking disjoint neighbourhoods of each $p_{i}$, we get $\deg_{q} \pi = \sum_{i} m_{i}$. We have a disjoint union of power maps on discs. We will show that these same $m_{i}$ on the same discs give the degree at every point near $q$. 

That is, there is an open neighbourhood $V \ni q$ for which all pre-images of points $q' \in V$ come from the discs around the $p_{i}$. We show this by contradiction. If there weren't such a neighbourhood, then there would be a sequence $q_{n}' \to q$ in $Y$ where all the points have some pre-image not in a disc around some $p_{i}$. Consider the set of all pre-images $p_{n}'$ not in a neighbourhood of some $p_{i}$. Since $X$ is compact [[Analysis --- math-131/notes/Compactness#_theorem _ Bolzano-Weierstrass theorem|we get a convergent subsequence]] $p_{n_{k}}' \to p'$ for some $p' \in X$. Since $\pi$ is continuous, $\pi(p') = q$, and thus $p'$ is one of the $p_{i}$. This contradicts our assumption that the $p'_{n}$ were not in some neighbourhood 

---

##### _definition:_ degree of a map

The degree of a (non-constant) holomorphism $\pi : X \to Y$ is $\deg \pi = \deg_{q} \pi$ at any $q \in Y$.

---

##### _corollary:_ isomorphism is determined by degree

If (non-constant) $\pi  : X \to Y$ has $\operatorname{deg} \pi = 1$, then $\pi$ is an [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ biholomorphism/isomorphism, automorphism|isomorphism]].

###### _proof:_

If $\pi$ has degree $1$ there can't be any branch points, so it is injective. [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ maps from compact Riemann surfaces are surjective|We've shown]] that it is surjective (since $X, Y$ are compact). [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_theorem _ inverse holomorphism theorem|Injective holomorphisms]] are isomorphisms onto their image. We're done!

---

### Ramifications for meromorphic functions

All of this theory has huge *ramifications* for [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ meromorphic|meromorphic functions]] $f : X \to \mathbb{C}$ since [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ meromorphic functions are maps to the Riemann sphere|they correspond to holomorphisms to the Riemann sphere]] $\pi_{f} : X \to \mathbb{C}_{\infty}$.

##### _example:_ surfaces with single simple poles are the Riemann sphere

If $X$ has a meromorphic function with exactly one simple pole, $X \cong \mathbb{C}_{\infty}$ — since it has a degree $1$ map to $\mathbb{C}_{\infty}$, it is isomorphic to it.

##### _lemma:_ multiplicities of meromorphic functions

Given $f : X \to \mathbb{C}$ meromorphic and $\pi_{f} : X \to \mathbb{C}_{\infty}$ the corresponding holomorphism,
1) at poles, $\operatorname{mult}_{p} \pi_{f} = - \operatorname{ord}_{p} f$
2) at zeroes, $\operatorname{mult}_{p} \pi_{f} = \operatorname{ord}_{p} f$
3) everywhere else $\operatorname{mult}_{p} \pi_{f} = \operatorname{ord}_{p}(f - f(p))$

---

This allows us to prove what we already know to be true in the special cases of [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_example _ meromorphic functions on the Riemann sphere and projective line|the Riemann sphere]] and [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ meromorphic functions on a torus $ mathbb{C} / Lambda$ have zero total order|complex tori]].

##### _theorem:_ the sum of orders of a meromorphic function

If $f$ is a non-constant meromorphic function on $X$, then
$$
\sum_{p \in X} \operatorname{ord}_{p} f = 0.
$$

###### _proof:_

Consider the corresponding map $\pi_{f} : X \to \mathbb{C}_{\infty}$. Since degree is constant it is equal at $0$ and at $\infty$. That is, the sum of multiplicities of zeroes is equal to the sum of multiplicities of poles. By the previous result,
$$
\sum_{p \text{ pole}} - \operatorname{ord}_{p} f = \sum_{p \text{ zero}} \operatorname{ord}_{p} f.
$$
That is,
$$
\sum_{p \in X} \operatorname{ord}_{p} f = \sum_{p \text{ pole or zero}} \operatorname{ord}_{p} f = 0
$$
(since the only points with non-zero order are poles and zeroes).

---

### Hurwitz' formula

Hurwitz' formula allows us to relate the topology of two Riemann surfaces given the topological data of a map between them.

##### _theorem:_ Hurwitz' formula

Given (a non-constant holomorphism of compact Riemann surfaces) $\pi : X \to Y$
$$
2g_{X} - 2 = \operatorname{deg} \pi (2g_{Y} - 2) + \sum_{p \in X} (\operatorname{mult}_{p} \pi - 1).
$$

###### _proof sketch:_

Triangulate $Y$ with vertices at branch points. Pull the triangulation back under $\pi$. Since there are no branch points on edges or faces, these get pulled back to $\deg \pi$ times the number of edges and faces.

Almost every vertex has $\operatorname{deg} \pi$ pre-images. Only at the branch points we have to correct. From the degree, we subtract the multiplicity and add $1$ for each point in the pre-image of the vertex — the number of vertices on $X$ is
$$
\#V_{X} = \sum_{p, \pi(p) \in V_{Y}} 1 = (\deg \pi) \# V_{Y} + \sum_{p \text{ ramified}} (1 - \operatorname{mult}_{p} \pi).
$$

Since $2g - 2$ [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological invariants of a surface#_theorem _ Euler characteristic and genus|is the negation of the Euler characteristic]], we get the Hurwitz formula —
$$
\begin{align}
2g_{X} - 2 & = - \chi_{X} \\
 & = - \# V_{X} + \# E_{X} - \# F_{X} \\
 & = (\deg \pi) (-\#V_{Y} + \#E_{Y} - \# F_{Y}) - \sum_{p \text{ ramified}} (1 - \operatorname{mult}_{p} \pi ) \\
 & = (\deg \pi) (2 g_{Y} - 2) + \sum_{p \text{ ramified}} (\operatorname{mult}_{p} \pi - 1).
\end{align}
$$

---

##### _example:_ meromorphic functions on the Riemann sphere

Meromorphic functions on the [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Riemann surfaces#_example _ the Riemann sphere and the complex projective line|Riemann sphere/complex projective plane]] have really nice behaviour. We've seen earlier that [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_example _ meromorphic functions on the Riemann sphere and projective line|they are just rational functions]]. For a rational function that looks like
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

---

##### _example:_ meromorphic functions on non-isomorphic elliptic curves

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

Similarly on the elliptic curve $Y = \{ (x, y) \in \mathbb{C}^{2} \mid y^{2} = x^{3} + x \} \cup \{ \infty \}$, there is an automorphism $\rho_{Y} : Y \to Y$ by $(x, y) \mapsto (\xi_{4}^{2} x, \xi_{4}^3 y) = (-x, -iy)$ (where $\xi_{4}$ is a fourth root of unity).

Since these Riemann surfaces have different automorphism groups, they are not isomorphic!

---