---
tags:
- alg-geo
- cx-geo
- karpism/1
- karpism/2
---

 Here, we identify $\mathbb{A}^n_{\mathbb{C}}$ with $\mathbb{C}^n$ and $\operatorname{Spec} \mathbb{C}[x, x ^{-1}]$ with $\mathbb{C}^\times$.

Toric varieties are a special class of varieties that admit a very combinatorial description.

##### _definition:_ toric varieties, algebraic torus

A **toric variety** $X$ is a variety $X$ over $\mathbb{C}$ with an dense open embedding of the **algebraic torus** $\mathbb{T}^n = (\mathbb{C}^\times)^n \subseteq X$ and an action $\mathbb{T} = \mathbb{C}^\times \circlearrowright X$ that restricts to the normal torus action on the embedding of $\mathbb{T}^n$.

---

##### _definition:_ cones, (strongly convex, rational, polyhedral) fans

A **cone** $\left< v_{i} \right>_{i = 1}^n$ of vectors $v_{i} \in \mathbb{R}^d$ is the span of all $a_{1} v_{1} + \dots + a_{n} v_{n} \subseteq \mathbb{R}^d$ with

A **strongly convex, rational, polyhedral fan** is a set of cones in $\mathbb{R}^d$, so that there is no cone crossing the origin (**strongly convex**) each vector of which has **rational** slope, and so that the intersection of any two cones is a cone (**polyhedral**).

---

Given a fan $\Sigma$, we can always get back a toric variety $X$. In fact, we can get one that preserves certain information — there is an inclusion-reversing bijection between cones and $\mathbb{T}$-invariant subvarieties of $X$.

##### _definition:_ the toric variety of a fan

Given a fan $\Sigma$, the corresponding **toric variety of the fan** is the quotient variety
$$
X_{\Sigma} = (\mathbb{C}^n \setminus Z(\Sigma)) / G.
$$

Here $n$ is the size of the $1$-skeleton of $\Sigma$ — $n = \# \Sigma(1)$. Thus to each copy of $\mathbb{C}$ we associate some $\rho \in \Sigma(1)$.

$Z(\Sigma)$ is the union of all $V(S)$ as $S \subseteq \Sigma(1)$. $V(S)$ is the linear subspace where all $x_{\rho} = 0$ for $\rho \in S$.

Let $M$ is the lattice $\mathbb{Z}^d \subseteq \mathbb{R}^d$ for $\Sigma \subseteq \mathbb{R}^d$. Consider $\varphi : \operatorname{Mor}_{\mathsf{Set}}(\Sigma(1), \mathbb{C}^\times) \to \operatorname{Hom}_{\mathsf{Ab}}(M, \mathbb{C}^\times)$ given as follows. Send a map $f : \Sigma(1) \to \mathbb{C}^\times$ to a map $M \to \mathbb{C}^\times$ by $m \mapsto \prod_{v \in \Sigma(1)} f(v)^{\left< m, v \right>}$. In particular, we can think of $\varphi$ as $(\mathbb{C}^\times)^n \to (\mathbb{C}^\times)^r$ by $(t_{1}, \dots, t_{n}) \mapsto \left( \prod_{j = 1}^n t_{j}^{v_{j}^1}, \dots, \prod_{j = 1}^n t_{j}^{v_{j}^n} \right)$ (here write $v_{j}^i$ for the $i$th component of $v_{j}$). 

Notice that we can think of $\operatorname{Mor}_{\mathsf{Set}}(\Sigma(1), \mathbb{C}^\times)$ as a group. Thus, we can define $G = \ker \varphi$.

---

##### _example:_ the complex projective plane is a triangle

Consider $\Sigma \subseteq \mathbb{R}^2$ with $v_{0} = (-1, -1)$, $v_{1} = (1, 0)$, and $v_{2} = (0, 1)$ and consider the cones $\Sigma = \{ 0, \left< v_{0} \right>, \left< v_{1} \right>, \left< v_{2} \right>, \left< v_{1}, v_{2} \right>, \left< v_{0}, v_{1} \right>, \left< v_{0}, v_{2} \right > \}$. This gives the map $\varphi$ with $(t_{0}, t_{1}, t_{2}) \mapsto (t_{0}^{-1} t_{1} t_{2}^0, t_{0}^{-1}, t_{1}^0 t_{2}) = (t_{0}^{-1} t_{1}, t_{0}^{-1} t_{2})$. This has kernel the subgroup $G = \{ (t, t, t) \} \subseteq (\mathbb{C}^\times)^3$. Then $(\mathbb{C}^\times)^3 / G \cong \mathbb{C} \mathbb{P}^2$.

By taking the dual of $\Sigma$ we get a triangle, so $\mathbb{C} \mathbb{P}^2$ is a triangle.

---

How do we go the other way? What's the fan of a toric variety? We show how it's done for $\mathbb{C} \mathbb{P}^{2}$. Most else works the same way.

##### _example:_ the fan of the complex projective plane

Consider the action $\mathbb{T}^{2} \circlearrowright \mathbb{C} \mathbb{P}^2$ by $(s, t) \circlearrowright (x : y : z) = (x : sy : tz)$. Consider also the one-parameter subgroup $\mathbb{T}^1 \circlearrowright \{ (t, t) \}$ by $(t, t) \circlearrowright (x : y : z) = (x : t^a y : t^b z)$  for $a, b \in \mathbb{Z}$. We look at the orbit closure of limit points as $t \mapsto 0$.

| $a, b$      | $\lim_{ t \to 0 } (x : t^a y : t^b z)$ |
| ----------- | -------------------------------------- |
| $a, b > 0$  | $(1 : 0 : 0)$                          |
| $a = b < 0$ | $(0 : y  : z)$                         |
| $a = b = 0$ | $(x : y : z)$                          |

Similarly, we have $(0 : 1 : 0)$ for $a < 0, b$ and $(x : y : 0)$ for $a = 0 < b$ et c. Thus, we can think of the point $(0 , 0)$ as corresponding to all of $\mathbb{P}^{2}$, the rays like $\{ (a, b) \mid a = b <  0 \}$ corresponding to $\mathbb{P}^1$s that complements of the natural affine opens, and finally, the cones spanned by pairs of those rays as torus fixed points like $(0 : 1 : 0)$. Moreover, these preserve the intersection data of these objects.

---

This allows us to do neat things in enumerative geometry like blowups.

##### _example:_ the blowup of $\mathbb{C}^{2}$ and the blowup of $\mathbb{C} \mathbb{P}^2$.

The blowup of $\mathbb{C}^{2}$ at the origin is
$$
\operatorname{Bl}_{(0, 0)} \mathbb{C}^{2} = \{ (z, u) = ((z_{1}, z_{2}), (u_{1} : u_{2})) \in \mathbb{C}^{2} \times \mathbb{C} \mathbb{P}^1 \mid z_{1} u_{2} = z_{2} u_{1} \}
$$
with the map to $\mathbb{C}^{2}$ by $(z, u) \mapsto z$. The fibre above every non-zero point $(z_{1}, z_{2})$ is just $((z_{1}, z_{2}), (z_{1} : z_{2}))$. However, at $(0 : 0)$ the fibre is all of $\mathbb{C} \mathbb{P}^1$! We can think of this as sending each point to a line through the origin that carries the data of which point it comes from. Each non-zero point corresponds to a unique slope, but $(0 : 0)$ has a whole $\mathbb{P}^1$ worth of lines through it and the origin (which is itself).

This can be thought of as the distinguished affine cover of the point $(1 : 0 : 0)$ in the blowup of $\mathbb{C} \mathbb{P}^2$ —
$$
\operatorname{Bl}_{(1 : 0 : 0)} \mathbb{C} \mathbb{P}^{2} = \{ (z, u) = ((z_{0} : z_{1} : z_{2}), (u_{1} : u_{2})) \in \mathbb{C} \mathbb{P}^{2} \times \mathbb{C} \mathbb{P}^1 \mid z_{1} u_{2} = z_{2} u_{1} \}.
$$
Then adding $\left< v_{1} + v_{2} \right>$ to subdivide the maximal cone corresponding to $(1 : 0 : 0)$ in the cone of $\mathbb{C} \mathbb{P}^2$. That is, we've replaced the point with a line.

---

##### _homework:_ the toric variety of the fan of the blowup of $\mathbb{C}\mathbb{P}^2$ is just the blowup of $\mathbb{C} \mathbb{P}^2$