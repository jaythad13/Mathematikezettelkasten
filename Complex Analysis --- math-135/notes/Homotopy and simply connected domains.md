---
tags:
- math-135/9
- math-135/12
- anal
- complex
- alg-top
---

Homotopy allows us to talk about when two curves are the basically the same in all the ways that we care about.

##### _definition:_ homotopy

If there exists a family of curves
$$
\{ \gamma_{s} : [a, b] \to \Omega \mid s \in [0, 1] \}
$$
such that they all have common endpoints $\alpha, \beta$, and $\gamma : [0, 1] \times [a, b] \to \mathbb{C}$ by $(s, t) \to \gamma_{s}(t)$ is continuous, then we say $\gamma_{0}$ and $\gamma_{1}$ are homotopic.

##### _theorem:_ deformation theorem

If $\gamma_{0}$ and $\gamma_{1}$ are homotopic curves in $\Omega$, and $f : \Omega \to \mathbb{C}$ is holomorphic, then they have the same integral —
$$
\int_{\gamma_{1}} f = \int_{\gamma_{2}} f.
$$

###### _proof sketch:_

Show that for $s_{1}$ close to $s_{2}$, the integrals over $\gamma_{s_{1}}$ and $\gamma_{s_{2}}$ are the same. With enough clever $\varepsilon$-$\delta$ arguments, the difference of the integrals reduces to a telescoping sum with the end terms being the difference of $f$ evaluated on the end points of each curve. This is just zero, since the curves have the same endpoints.

### Simple connectedness

Simply connected regions are ones where there is essentially only one path between two points — all curves with the same endpoints are homotopic.

##### _definition:_ simply connected

If $\Omega$ is a region in $\mathbb{C}$ where all curves with the same endpoints are homotopic, then $\Omega$ is simply connected.

##### _example:_ simply connected and non-simply connected regions

Think $\mathbb{C}$ and $\mathbb{C} \setminus \{ 0 \}$.

##### _lemma:_ existence of primitives

Say $f$ is continuous on some region $\Omega$, then the following are equivalent
1) $f$ has a primitive in $\Omega$
2) Any contour integral of $f$ in $\Omega$ is path independent (dependent only on the endpoints of the curve)
3) Any contour integral of $f$ over a closed curve in $\Omega$ is $0$.

###### _proof:_

 That (1) implies (2) is just the fundamental theorem of calculus. (2) and (3) are clearly equivalent.

(2) implies (1) is just [[Complex analysis --- math-135/notes/Cauchy-Goursat theorem#_corollary _ Cauchy's theorem|the existence of primitives]].

Now, we have as a corollary — 

##### _corollary:_ generalised Cauchy's theorem

If $f$ is holomorphic on a simply connected region $\Omega$, then
$$
\int_{\gamma} f(z) \, dz = 0
$$
for any closed curve in $\gamma$ in $\Omega$.