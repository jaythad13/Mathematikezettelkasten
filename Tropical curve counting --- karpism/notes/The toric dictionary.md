---
tags:
- alg-geo
- cx-geo
- trop-geo
- karpism
---

The correspondence between [[Tropical curve counting --- karpism/notes/Toric varieties and fans#_definition _ toric varieties, algebraic torus|toric varieties]] $X$ and their fans $\Sigma_{X}$ is very nice. Not only can we read off many nice torus-invariant properties of $X$ from its fan, but also, the correspondence is functorial and cohomological.

In particular, let $X, Y$ be a (normal) toric varieties with dense open torus $\mathbb{T}$. Let $\Sigma_{X}, \Sigma_{Y}$ be their corresponding fans.

### Torus-invariant loci and scheme-theoretic properties

##### _proposition:_ cones covariantly correspond to torus-invariant affine opens

##### _proposition:_ cones contravariantly correspond to torus orbits

##### _proposition:_ $\mathbb{Z}$-basis cones correspond to smooth varieties

##### _proposition:_ complete fans correspond to proper varieties


### Functoriality

##### _proposition:_ the toric variety–fan correspondence is functorial

##### _proposition:_ proper morphisms come from fan maps surjective on support


### Cohomology and divisors

We can read off the cohomology of a toric variety just from its fan.

##### _theorem:_ reading cohomology from a fan

Let $X$ be a smooth projective [[Tropical curve counting --- karpism/notes/Toric varieties and fans#_definition _ toric varieties, algebraic torus|toric variety]] with [[Tropical curve counting --- karpism/notes/Toric varieties and fans#_definition _ cones, (strongly convex, rational, polyhedral) fans|fan]] $\Sigma \subseteq M$ with $\Sigma^1 = \{ \left< v_{1} \right>, \dots, \left< v_{n} \right> \}$. Then, the cohomology ring of $X$ (is isomorphic to the Chow ring) is isomorphic as a graded ring to
$$
H^\bullet(X, \mathbb{Z}) \cong A^\bullet(X) \cong \mathbb{Z}[d_{1}, \dots, d_{n}] / \mathfrak{i}
$$
where $\mathfrak{i}$ gives the following relations.

- The product $d_{i_{1}} \cdots d_{i_{k}} = 0$ exactly when $\left< v_{i_{1}}, \dots, v_{i_{k}} \right> \not\in \Sigma$ — when the corresponding vectors do not span a cone.
- For each $\varphi \in M^\vee$, the relation $\sum_{i = 1}^n \varphi(v_{i}) d_{i} = 0$.

---

Note here that multiplication in the cohomology ring correspond to intersection 

##### _example:_ the cohomology of $\mathbb{P}^2$

We have $H^\bullet(\mathbb{P}^{2}) = \mathbb{Z}[d_{1}, d_{2}, d_{3}] / \mathfrak{i}$ with $\mathfrak{i}$ giving relations
1) $d_{1} d_{2} d_{3} = 0$
2) $d_{1} - d_{3} = 0$ and $d_{2} - d_{3} = 0$.
Thus, $H^\bullet(\mathbb{P}^{2}) = \mathbb{Z}[h] / h^{3}$. We write this as $\mathbb{Z}[h]$ to indicate that $h$ stands for hyperplane.

---

##### _example:_ compute the cohomology of $\operatorname{Bl}_{p} \mathbb{P}^{2}$ 

Let $\operatorname{Bl}_{p} \mathbb{P}^{2}$ be the blowup of $\mathbb{P}^{2}$ at a torus-invariant point $p$. Then $H^\bullet(\operatorname{Bl}_{p} \mathbb{P}^{2}, \mathbb{Z}) =  \mathbb{Z}[h, e] / \mathfrak{i}$ where $\mathfrak{i}$ gives relations $e^{2} = -h^{2}$, $h e = 0$ (which together, imply $h^{3} = 0$)

Geometrically, $h$ is a generic line, which typically doesn't intersect the exceptional divisor $e$. Thus, $he = 0$. However, when $h$ corresponds to line in $\mathbb{P}^{2}$ that contained $p$, $h$ intersects $e$. This gives $(e - h) e = (e - h) h = 0$, and thus, $e^{2} - h^{2} = 0$.

---

##### _example:_ the cohomology of $\operatorname{Bl}_{p_{1}, p_{2}, p_{3}} \mathbb{P}^{2}$

---