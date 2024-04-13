---
tags:
- math-142
- diff-geo
lecture:
- math-142-29
- math-142-30
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

### Tangent vectors

Since we're embedded in $\mathbb{R}^3$, we can just choose the tangent vectors from $\mathrm{T}\mathbb{R}^3$ that are "tangent" to the surface. To do so, we will first show some equivalent definitions of what it means to be tangent to a surface $M$.

##### _proposition:_ tangent vectors are derivatives of curves

Let $p$ be a point on a surface $M$. Then the following are equivalent.


%% see the lecture notes for the exact details, I got lost %%