---
tags:
- uc-2026/ggt/1
- uc-2026/ggt/2
- ben-lowe
- ggt
- diff-geo
---

##### _definition:_ hyperbolic $3$-space

**Hyperbolic $3$-space** is the Riemannian $3$-fold $\mathbb{R}^{2} \times \mathbb{R}_{> 0}$ with the metric 
$$
ds = \frac{dx^{2}  +dy^{2} + dz^{2}}{z^{2}}.
$$
We think of the first factor as $\mathbb{C}$.

---

##### _definition:_ complete hyperbolic $3$-fold

A **complete hyperbolic $3$-fold** is a quotient Riemannian manifold $X = \Gamma \setminus \mathbb{H}^{3}$ for a discrete subgroup $\Gamma \leq \mathrm{PSL}_{2}(\mathbb{C})$ acting [[Abstract algebra --- math-171/notes/Group actions#_definition _ stabiliser, free|freely]].

---

Note $\mathrm{PSL}_{2}(\mathbb{C})$ is just the group of isometries of $\mathbb{H}^{3}$, so we're just asking for any discrete action $\Gamma \circlearrowright \mathbb{H}^{3}$. Also note, by covering space theory, we have $\pi_{1}(\Gamma \setminus \mathbb{H}^{3}) \cong \Gamma$. In fact, they are Eilenberg–MacLane spaces $K(\Gamma, 1)$s.

An important fact is that this group $\Gamma$ is essentially the data of the whole manifold.

##### _theorem:_ Mostow rigidity

Let $n \geq 3$. A complete finite volume hyperbolic $n$-fold is determined up to isometry by its fundamental group.

---

Thus, all geometric invariants of finite volume hyperbolic $3$-folds are homotopy invariant. In particular, this means that each hyperbolic manifold has a *unique* hyperbolic metric.

##### _example:_ a simple hyperbolic $3$-fold

Consider
$$
\Gamma = \left \{ \begin{pmatrix}
1 & a + bi \\
0 & 1
\end{pmatrix} \mid a, b \in \mathbb{Z} \right \} \cong \mathbb{Z}[i] \cong \mathbb{Z}^{\oplus 2}. 
$$
Since we're quotienting $X = \Gamma \setminus \mathbb{C} \times \mathbb{R}_{\geq 0}$, topologically $X$ is a product of tori $\mathbb{T}^{2} \times \mathbb{R}_{\geq 0}$. However, because of the metric we have, these tori should get smaller as we go up (as $z \in \mathbb{R}_{\geq 0}$ gets bigger).

---

##### _example:_ hyperbolic $3$-folds coming from knots

A **knot** is an embedding $S^1 \to S^{3}$ up to **isotopy** ([[Algebraic topology --- concise/notes/Homotopy#_definition _ homotopic, homotopy, homotopic relative to|homotopy]] where each $s \mapsto H(t, s)$ is an embedding).

Consider $Y = S^3 \setminus K$ where $K$ is the image of the figure-eight knot. It turns out that this is $\mathrm{PSL}_{2}(\mathbb{Z} [\omega]) \setminus \mathbb{H}^{3}$ where $\omega = e^{2 \pi i / 3}$ is a cube root of unity. $\mathrm{PSL}_{2}(\mathbb{Z}[\omega])$ is actually really large (even $\mathrm{PSL}_{2}(\mathbb{Z})$ [[Geometric group theory --- rtg-2025/notes/The special linear group over the integers#_theorem _ $ mathrm{PSL}_{2}( mathbb{Z})$ is a free product of cyclic groups|is complicated]]).

$Y$ can be given a hyperbolic metric so that it is a complete, finite-volume, hyperbolic $3$-manifold. The idea is to push the knot to $\infty$.

With this metric, our previous example $X$ covers $Y$! If we thicken the image of $K$, we get a solid torus, and the boundary is just a torus. As we look at all of these getting closer to the knot, we see $X$.

We can see this more abstractly by noting that $\mathrm{PSL}_{2}(\mathbb{Z}[\omega])$ contains the fundamental group $\Gamma$ from our previous example. Then it follows from covering space theory.

---

A theorem of Thurston helps us understand all the ways we can get a manifold from a knot.

##### _theorem:_ almost all knots are hyperbolic or satellites (Thurston)

A knot $K$ is either
- the unknot
- a satellite
- or $S^3 \setminus K$ has a complete finite volume hyperbolic metric.

---

If the last is true, we say $K$ is a **hyperbolic knot**.

In general, for a not $K$ in $S^{3}$ we can make a closed $3$-manifold by gluing a solid torus to $S^{3} \setminus K_{\varepsilon}$ where $K_{\varepsilon}$ is a sufficiently small tubular neighbourhood of the knot and the gluing identifies the tori $\partial H$ and $\partial K_{\varepsilon}$. The different ways we can do this is given by the **mapping class group** of the torus $\operatorname{Aut}_{\mathsf{Diff}} \mathbb{T}^{2} / \sim$ where $\sim$ identifies isotopic diffeomorphisms. We call this process **Dehn filling**.

##### _theorem:_ Thurston's second hyperbolisation theorem

All but finitely many Dehn fillings of a hyperbolic knot $K$ have complete hyperbolic metrics.

---

If we want to classify hyperbolic $3$-folds, we need to understand the surfaces they contain. We can have lots of surfaces inside a hyperbolic $3$-manifold and we want to be able to ignore the ones that are cheap to get.

##### _definition:_ incompressible surface

Let $Y \subseteq X$ be an embedded surface in a $3$-manifold. $Y$ is an **incompressible surface** if every injective continuous curve $\gamma : S^1 \to Y$ that is not null-homotopic in $Y$ is also not null-homotopic in $X$.

---

Note, it suffices for $\pi_{1}(Y) \to \pi_{1}(X)$ to be injective, but not all incompressible surfaces satisfy this.

##### _theorem:_ classification of complete finite volume hyperbolic $3$-folds (Bass)

Suppose $X$ is a complete, finite volume, hyperbolic $3$-fold. Then either $X$ contains an incompressible surface or $\pi_{1}(X) \cong \Gamma \leq \mathrm{PSL}_{2}(\mathscr{O}_{\mathbb{K}})$ for some [[Transcendental number theory --- math-195/notes/Number fields#_definition _ number field|number field]] $\mathbb{K}$.

###### _proof sketch:_

Consider $\chi(X, \mathrm{PSL}_{2}(\mathbb{C}))$, the **$\mathrm{PSL}_{2}(\mathbb{C})$ character variety of $X$**. The set of points of $\chi(X, \mathrm{PSL}_{2}(\mathbb{C}))$ is the set of all homomorphisms $\pi_{1}(X) \to \mathrm{PSL}_{2}(\mathbb{C})$ upto conjugation. These have the structure of a variety since they are given by the choice of images of the $k$ generators of $\pi_{1}(X)$ satisfying corresponding relations. But then the entries of these matrices in $\mathrm{PSL}_{2}(\mathbb{C})^k \subseteq \mathbb{C}^{4k}$ are exactly the points of $\mathbb{C}^{4k}$ satisfying some polynomial equations. Then we quotient by the action of $\mathrm{PSL}_{2}(\mathbb{C})$ by conjugation.

It turns out that by geometric invariant theory, $\chi(X, \mathrm{PSL}_{2}(\mathbb{C}))$ is 

Each hyperbolic structure on $X$ gives a point in $\chi(X, \mathrm{PSL}_{2}(\mathbb{C}))$ — a hyperbolic structure gives an action $\pi_{1}(X) \circlearrowright \mathbb{H}^{3}$ or equivalently, $\pi_{1}(X) \to \mathrm{PSL}_{2}(\mathbb{C}) = \operatorname{Aut}_{\mathsf{Metric}} \mathbb{H}^{3}$. There is a component of $\chi(X, \mathrm{PSL}_{2}(\mathbb{C}))$ corresponding to nice (discrete) subgroups. Mostow rigidity tells us that this is an isolated point in $\chi(X, \mathrm{PSL}_{2}(\mathbb{C}))$. Its coefficients determine $\Gamma$. We claim this forces $\Gamma$ to be defined over $\overline{\mathbb{Q}}$.

What we're saying affine-locally is that if $p_{1}, \dots, p_{k} \in \mathbb{Q}[x_{1}, \dots, x_{n}]$ have just a single root over $\mathbb{C}$, then that root must be algebraic. The idea is that if they had a transcendental root $\pi$, then $p_{1}, \dots, p_{k} \in \mathbb{Q}(y)[x_{1}, \dots, x_{n}]$ have a common root. But then $p_{1}, \dots, p_{k}$ have a root for [[Transcendental number theory --- math-195/notes/Transcendental and algebraic numbers#_proposition _ algebraic independence and maps from function fields|any transcendental number]]. There's more than just one transcendental number. This isn't a formal proof because we could have $y_{1}, \dots, y_{m}$ different. The idea is to use dimension theory — we claim that if $\mathbb{Q} [x_{1}, \dots, x_{n}] / (p_{1}, \dots, p_{k})$ has one $\mathbb{C}$-point, it is a finite-dimensional $\mathbb{Q}$-module.

Computing concretely, we can use the lack of compressible surfaces to see that in fact these polynomials must be monic.

---

Note, this gives a complete classification. We understand hyperbolic $3$-folds containing incompressible surfaces already. They are called **Haken manifolds** and they can be repeatedly cut along their incompressible surfaces to obtain a bunch of $3$-balls. Knot complements are always Haken, but some Dehn fillings of knot complements are non-Haken.