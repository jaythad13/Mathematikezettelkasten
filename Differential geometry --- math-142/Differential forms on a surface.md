---
tags:
- math-142
- diff-geo
lecture:
- math-142-33
---

We've seen how to deal with [[Differential forms|differential forms]] on $\mathbb{R}^3$. If you replace all of the domains $\mathbb{R}^3$ with a surface $M$, we get differential forms on a surface.

### $0$-forms and $1$-forms on a surface

To avoid repeating hypotheses all the time
##### _notation:_ $M$

For this section, let $M$ be a surface in $\mathbb{R}^3$ with a family of patches $x_{k} : D_{k} \to I$ for $k \in I$.

We already have a notion of [[Calculus on surfaces#_definition _ smooth functions on a surface|smooth functions]] on a surface. Thus, we have $0$-forms on a surface already.

##### _definition:_ $0$-forms on a surface

A $0$-form on $M$ is a smooth function $f : M \to \mathbb{R}$.

$1$-forms allow us to take tangent vectors to the reals smoothly — we can define them in the most obvious way.

##### _definition:_ $1$-forms on a surface

A $1$-form on $M$ is a function $\phi : \mathrm{T}M \to \mathbb{R}$ that is $\mathbb{R}$-linear on each tangent space $\mathrm{T}_{p}M$ (for all $p \in M$).

We denote the collection of all $1$-forms on $M$ by $\Omega^1(M)$.

Note that most $1$-forms on $M$ can be thought of as $1$-forms on $\mathbb{R}^3$ as well.

There should then be an obvious way to go from $0$-forms to $1$-forms like the [[The exterior derivative|exterior derivative]] was on $\mathbb{R}^3$.

##### _proposition:_ the exterior derivative on $0$-forms

Say $f : M \to \mathbb{R}$ is a $0$-form and $[\mathbf{v}, p] \in \mathrm{T}_{p}M$ is given by $[\mathbf{v}, p] = \alpha'(t_{0})$. Let $p = x_{k}(u_{0}, v_{0})$ and let $a = x^{-1} \circ \alpha: \mathbb{R} \to \mathbb{R}^2$. Then the map $df : \mathrm{T}M \to \mathbb{R}$ given by
$$
df([\mathbf{v}, p]) = Df_{k} \Big |_{p} (a'(t_{0}))
$$
is a $1$-form.

##### _proposition:_ the coordinate expression for $1$-forms on a surface

Fix some $p \in M$

1) For any $\phi \in \Omega^1(M)$. Then, restricted to $\mathrm{T}_{p}M$
$$
\phi : g_{1} \, du + g_{2} \, dv
$$
	for some $g_{1}, g_{2} : D_{k} \to \mathbb{R}$.
2) Say $f : M \to \mathbb{R}$ is a $0$-form. Then, restricted to $\mathrm{T}_{p}M$,
$$
df = \frac{ \partial (f \circ x_{k}) }{ \partial u } \Big |_{(u_{0}, v_{0})} \, du + \frac{ \partial (f \circ x_{k}) }{ \partial v } \Big |_{(u_{0}, v_{0})} \, dv
$$