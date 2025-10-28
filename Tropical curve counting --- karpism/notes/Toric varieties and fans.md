---
tags:
- alg-geo
- cx-geo
- karpism/1
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

By taking the dual of $\Sigma$ we get a triangle, so $\mathbb{C} \mathbb{P}^1$ is a triangle.

---