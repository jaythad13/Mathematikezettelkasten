---
tags:
- math-142
- diff-geo
lecture:
- math-142-29
- math-142-30
- math-142-31
- math-142-32
---

Given a surface $M$, we want to define a tangent space $\mathrm{T}_{p}M$ at each point $p \in M$. Hopefully this will also allow us to define directional derivatives, and vector fields on a surface!

### Lines on surfaces

If $D \subset \mathbb{R}^2$ is open with a mapping $x : D \to \mathbb{R}^3$, we can draw a line around each point $(u_{0}, v_{0})$ and then push it through to the image $x^\text{img}(D)$. That is, we have the curve $\alpha : I \to D \subset \mathbb{R}^2$ by $\alpha(t) = (u_{0} + a_{1}t, v_{0} + a_{2}t)$ contained in $D$. Thus, $x \circ \alpha$ is a map $I \to \mathbb{R}^3$.

It turns out that due to regularity, if $(a_{1}, a_{2})$ and $(b_{1}, b_{2})$ are linearly independent, then the derivatives of $\alpha$ and $\beta$ (defined by $\beta(t) = (u_{0} + ct, v_{0} + dt)$) are linearly independent due to the full rank of $x$. 

Specifically,
$$
\alpha'(t_{0}) = Dx \Big |_{(u_{0}, v_{0})} (a_{1}, a_{2})
$$
and
$$
\beta'(t_{0}) = Dx \Big |_{u_{0}, v_{0}} (b_{1}, b_{2}).
$$

Thus, by mapping lines through a point onto the surface through its coordinates in $\mathbb{R}^2$, we can get a two-dimensional vector space at each point. This will become the basic idea with which we define the tangent space at each point.

In particular, it can be useful to consider the derivative of the lines that define the axes in $\mathbb{R}^2$. That is, we define the parameter curves

##### _definition:_ $u$-parameter curve, $v$-parameter curve

For a surface $M$ and a patch $x : D \to M$
1) The $u$-parameter curve, at $(u_{0}, v_{0})$ is $x_{u}(u_{0}, v_{0}) = (x \circ \alpha)'(0)$ where $\alpha : I \to D$ is defined by $\alpha(t) = (u_{0}, v_{0}) + (1, 0)t$.
2) The $v$-parameter curve, at $(u_{0}, v_{0})$ is $x_{v}(u_{0}, v_{0}) = (x \circ \beta)'(0)$ where $\beta : I \to D$ is defined by $\beta(t) = (u_{0}, v_{0}) + (0, 1)t$.

### Tangent vectors

Since we're embedded in $\mathbb{R}^3$, we can just choose the tangent vectors from $\mathrm{T}\mathbb{R}^3$ that are "tangent" to the surface. To do so, we will first show some equivalent definitions of what it means to be tangent to a surface $M$.

First, we'll just do some bookkeeping so we don't have to keep stating hypotheses

##### _notation:_ $M$

For this section $M$ is a surface covered by at least two families family of proper patches $x_{k} : D_{k} \to M$, $y_{l} : E_{l} \to M$ indexed by $k \in A$ and $l \in B$ respectively.

##### _proposition:_ tangent vectors are derivatives of curves

Let $p$ be a point on $M$. Then the following are equivalent for any $[\mathbf{v}, p] \in \mathrm{T}_{p}\mathbb{R}^3$:

1) There exists a smooth curve $\alpha : I \to M$ such that $\alpha'(t_{0}) = [\mathbf{v}, p]$ for some $t_{0} \in I$.
2) There exists $k \in A$ such that for $x = x_{k}$ we have $p = x(u_{0}, v_{0})$ for some point $(u_{0}, v_{0}) \in D = D_{k}$ and $[\mathbf{v}, p]$ lies in the span of $x_{u}(u_{0}, v_{0}), x_{v}(u_{0}, v_{0})$.
3) There exists $k \in I$ such that for $x = x_{k}$ we have $[\mathbf{v}, p] = x_{*}([\mathbf{c}, (u_{0}, v_{0})])$ for some $(u_{0}, v_{0}) \in D_{k}$.

###### _proof:_

First we will show that 1) and 2) are equivalent.

Suppose we have $\alpha : I \to M$ satisfying $\alpha'(t_{0}) = [\mathbf{v}, p]$. We know that we can write $p = x (u_{0}, v_{0})$ for some patch $x = x_{k} : D = D_{k} \to M$. Notice that we can also write 
$$
\begin{split}
a(t) & = (x ^{-1} \circ \alpha)(t) \\
 & = (a_{1}(t), a_{2}(t))
\end{split}
$$

Note that, [[Calculus on surfaces#_definition _ smooth functions into a surface|by definition]] for $\alpha$ to be smooth, we have that $a = x^{-1} \circ \alpha$ is smooth. Thus, we can think of $\alpha = x \circ a$, and then by the chain rule, we have that
$$
\alpha'(t_{0}) = x_{u}(u_{0}, v_{0}) \, \frac{da_{1}}{dt} \Big |_{t_{0}} + x_{v}(u_{0}, v_{0}) \, \frac{da_{2}}{dt} \Big |_{t_{0}}.
$$
This gives us $[\mathbf{v}, p] = \alpha'(t_{0})$ as the desired linear combination.

Now suppose we have $[\mathbf{v}, p] = c_{1} x_{u}(u_{0}, v_{0}) + c_{2} (u_{0}, v_{0})$ for some constants, $c_{1}, c_2 \in \mathbb{R}$. Then consider the curve $a : I \to D$ by $a(t) = (u_{0}, v_{0}) + (c_{1}, c_{2})t$. By the openness of $D$, there is a non-empty interval $I \subset \mathbb{R}$ where this curve is actually defined (namely $I = \{ t \in \mathbb{R} \mid \lvert t \rvert < r/\sqrt{ 1 + c_{1}^2 + c_{2}^2} \}$ where $r$ is the radius of a neighbourhood of $(u_{0}, v_{0})$ contained in $D$).

Then if we define $\alpha = x \circ a$, we get
$$
\begin{split}
\alpha'(t_{0}) & = x_{u}(u_{0}, v_{0}) \, \frac{da_{1}}{dt} \Big |_{t_{0}} + x_{v}(u_{0}, v_{0}) \, \frac{da_{2}}{dt} \Big |_{t_{0}} \\
 & = c_1 x_{u}(u_{0}, v_{0}) + c_{2} x_{v}(u_{0}, v_{0}).
\end{split}
$$

Now we will show that 2) and 3) are equivalent. This just amounts to noticing that
$$
x_{*}([\mathbf{c}, (u_{0}, v_{0})]) = c_1 x_{u}(u_{0}, v_{0}) + c_2 x_{v}(u_{0}, v_0)
$$
since the parameter curves are just the columns of the Jacobian. Then both directions are obvious.

It turns out that this equivalence is invariant under different patches!

##### _proposition:_ tangent vectors are invariant under different patches

For any $p \in M$
1) There exist patches $x = x_{k}, y = y_{l}$ such that $p = x(u_{0}, v_{0}) = y(z_{0}, w_{0})$ for some $(u_{0}, v_{0}) \in D = D_{k}$ and $(z_{0}, w_{0}) \in E = E_{l}$ for some $k \in A, l \in B$.
2) As subspaces of $\mathrm{T}_{p}\mathbb{R}^3$, $\operatorname{span}(x_{u}(u_{0}, v_{0}), x_{v}(u_{0}, v_{0})) = \operatorname{span}(y_{z}(z_{0}, w_{0}), y_{w}(z_{0}, w_{0}))$.

###### _proof sketch:_

Note that the first part just follows from the definition of a surface — the families of patches must cover $M$.

The second part follows from the fact that first span is exactly the derivatives of smooth curves (or alternatively, exactly the image of the tangent vectors at $(u_{0}, v_{0})$ under the tangent map $x_{*}$), is exactly the second span.


Since these are all equivalent, now we can define the tangent space and the tangent bundle of a surface independently of the patches!

##### _definition:_ tangent vectors to a surface, tangent space, tangent bundle

A tangent vector $[\mathbf{v}, p] \in \mathrm{T}_{p}\mathbb{R}^3$ is a tangent vector to $M$ at $p$ if $[\mathbf{v}, p] = \alpha'(t_{0})$ for a smooth curve $\alpha : I \to M$ (and some $t_{0} \in I$).

The collection of all tangent vectors to $M$ at $p$ is $\mathrm{T}_{p}M$.

The disjoint union of all $\mathrm{T}_{p}M$ (for all points $p \in M$) is $\mathrm{T}M$.

##### _example:_ the tangent space of a plane

For any plane $M$, then, for any $p \in M$, $\mathrm{T}_{p}M$ is isomorphic to the subspace of $\mathbb{R}^3$ that is parallel to $M$ — it's all of the vectors "in the plane".

### Vector fields and the geometry of the tangent plane

All of these definitions for tangent spaces allow us to define vector fields in the obvious way.

##### _definition:_ tangent vector field (on a surface)

For a surface $M$, a tangent vector field on $M$ is a function $\mathbf{V} : M \to \mathrm{T}M$ such that $p \mapsto [\mathbf{v}, p] \in \mathrm{T}_{p}M$.

Note that we have $\mathrm{T}_{p}\mathbb{R}^3 \cong \mathbb{R}^3$ by $[\mathbf{v}, p] \mapsto \mathbf{v}$ and $\mathrm{T}_{p}M \cong \mathbb{R}^2$ by $c_{1} x_{u}  + c_{2} x_{v} \mapsto (c_{1}, c_{2})$. Thus, we should be able to embed $\mathrm{T}_{p}M$ as a subspace of $\mathrm{T}_p \mathbb{R}^3$, and then in $\mathbb{R}^3$ as well.

To do this we need to talk about normal vectors

##### _proposition, definition:_ normal vectors are the cross product of parameter curves, normal vectors, normal space, normal bundle

The following are equivalent for all $[\mathbf{n}, p] \in \mathrm{T}_{p}\mathbb{R}^3$:
1) $[\mathbf{n}, p] \cdot [\mathbf{v}, p] = 0$ for all $[\mathbf{v}, p] \in \mathrm{T}_{p}M$.
2) $[\mathbf{n}, p] = \lambda (x_{u}(u_{0}, v_{0}) \times x_{v}(u_{0}, v_{0}))$ where $x$ is a patch such that $x(u_{0}, v_{0}) = p$.

###### _proof:_

Note that $x_{u}(u_{0}, v_{0}), x_{v}(u_{0}, v_{0}), x_{u}(u_{0}, v_{0}) \times x_{v}(u_{0}, v_{0})$ form a basis for $\mathrm{T}_{p}\mathbb{R}^3$. Note  that $x_{u}(u_{0}, v_{0}), x_{v}(u_{0}, v_{0})$ is a basis of $\mathrm{T}M$. Since $x_{u}(u_{0}, v_{0}) \times x_{v}(u_{0}, v_{0})$ is orthogonal to both $x_{u}(u_{0}, v_{0})$ and $x_{v}(u_{0}, v_{0})$, it is orthogonal to $\mathrm{T}M$ as a whole. Since $\mathrm{T}_{p}\mathbb{R}^3$ is only three dimensional $\mathrm{T}M^\perp = \operatorname{span} (x_{u}(u_{0}, v_{0}) \times x_{v}(u_{0}, v_{0}))$.

Then the equivalence follows.

Thus we can define, a normal vector to $M$ at $p$ is some $[\mathbf{n}, p] \in \mathrm{T}_{p}\mathbb{R}^3$ such that $[\mathbf{n}, p] \cdot [\mathbf{v}, p] = 0$ for all $[\mathbf{v}, p] \in \mathrm{T}_{p}M$.

The collection of all normal vectors to $M$ at $p$ is called the normal space at $p$, denoted $\mathrm{T}_{p}M^\perp$.

The disjoint union of all $\mathrm{T}_{p}M^\perp$ for all $p \in M$ is the normal bundle $\mathrm{T}M^\perp$.

Note that this gives proof gives us the short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathrm T_p M^\perp \ar[r, hook] & \mathrm T_p \mathbb R^3 \ar[r] & \mathrm T_p M \ar[r] & 0
	\end{tikzcd}
\end{document}
```
and thus the fact that $\mathrm{T}_{p}\mathbb{R}^3 / \mathrm{T}_{p}M^\perp \cong \mathrm{T}_{p} M$.

This also motivates the definition of a normal vector field.

##### _definition:_ normal vector field

For a surface $M$ a normal vector field on $M$ is a function $\mathbf{V} : M \to \mathrm{T}M^\perp$ such that $p \mapsto [\mathbf{n}, p] \in \mathrm{T}_{p}M^\perp$.

##### _example:_ a general, non-trivial example of a vector field

Suppose we have a [[Surfaces#_corollary _ level sets are surfaces|level set that is a surface]]:
$$
M = \{ p \in \mathbb{R}^3 \mid g(p) = 0 \}.
$$
We know that this is only a surface if $Dg \Big |_{q} \neq 0$ for all $q \in \mathbb{R}^3$. Then the function
$$
\begin{split}
\nabla g &:  M \to \mathrm{T}M^\perp \\
 &:p \mapsto \left[ \left( \frac{ \partial g }{ \partial x } \Big |_{p}, \frac{ \partial g }{ \partial y } \Big |_{p}, \frac{ \partial g }{ \partial z } \Big |_{p}  \right), p \right]
\end{split}
$$
is a normal vector field.





