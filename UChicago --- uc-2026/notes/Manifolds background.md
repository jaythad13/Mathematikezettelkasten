---
tags:
- uc-2026/morse-theory/1
- uc-2026/morse-theory/2
- carmen-rovi
- diff-geo
- alg-top
---

We should probably understand the objects we are computing invariants of.

##### _definition:_ manifold

An **$n$-manifold $X$**, is a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]] which is locally (every point has a neighbourhood that is) [[Topology --- math-147/notes/Homeomorphisms#_definition _ homeomorphism|homeomorphic]] to $\mathbb{R}^n$.

---

##### _example:_ manifolds in small dimensions

All the $0$-dimensional manifolds are [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete]] sets of points.

The $1$-dimensional manifolds (curves) are all either homeomorphic to $\mathbb{R}$ or the circle $S^1$.

The $2$-dimensional manifolds (surfaces) are more varied, but some are the sphere $S^1$ and the torus $\mathbb{T}^2 = S^1 \times S^1$.

---

In topology, we only want to classify manifolds up to continuous deformation (up to homeomorphism). One helpful way to do this is to create a polyhedral model of our manifold, and then calculate the Euler characteristic of it using the $v - e + f$ formula.

##### _example:_ the Euler characteristic of the sphere

The sphere is homeomorphic to the tetrahedron. The tetrahedron has Euler characteristic $4 - 6 + 4 = 2$. Thus, $\chi(S^2) = 2$. It doesn't just depend on choosing the tetrahedron — a square pyramid also has Euler characteristic $2$. That is, this really is a homeomorphism invariant.

---

### Critical points

Though we are topologists, to understand critical points of height functions on the manifold, we need to understand the smooth structure on the manifold.

##### _definition:_ smooth manifold, chart, atlas, transition function

A **smooth $n$-manifold** is an $n$-manifold and a distinguished **atlas** of homeomorphisms  $\varphi : U \to \mathbb{R}^n$ called **charts** such that, for any chart $\psi : V \to \mathbb{R}^n$, the **transition function** $\varphi \circ \psi ^{-1} : \mathbb{R}^n \to \mathbb{R}^n$ is a smooth function (with appropriate restrictions to open subsets of $\mathbb{R}^n$ where $\varphi \circ \psi ^{-1}$ is actually defined)

---

##### _definition:_ smooth map

A **smooth map** or function $f : X \to Y$ is a [[Topology --- math-147/notes/Continuous functions#_definition _ continuity|continuous]] function such that, for each pair of charts $U, \varphi$ on $X$ and $V, \psi$ on $Y$, the function $\psi \circ f \circ \varphi ^{-1} : \mathbb{R}^n \to \mathbb{R}^m$ is differentiable.  

---

Since transition functions are all smooth, it suffices to just check this on any cover of charts. Also, since transition functions are all invertible, they have invertible derivative everywhere. Thus, though we can't give an invariant definition of the gradient of the function yet, we can know that the rank of the derivative is invariant under choice of chart. Specifically,

##### _proposition:_ rank of the derivative is chart invariant

Suppose $f : X \to Y$ is a function. Then $\operatorname{rank} D(\psi_{1} \circ f \circ \varphi_{1} ^{-1}) = \operatorname{rank} D(\psi_{2} \circ f \circ \varphi_{2} ^{-1})$ for any choice of charts (containing $p$) on $X$ and $Y$.

---

If $Y = \mathbb{R}$, the same applies for the rank of the Hessian.

##### _definition:_ critical point

A **critical point** of a smooth function $f : X \to Y$ is a point $p \in X$ at which the rank of $Df_{\mid p}$ is less than full rank. 

---

In fact, all of these details don't really matter, because we can and will assume all our manifolds are embedded in some large $\mathbb{R}^N$ which will give us an obvious definition of the tangent bundle on $X$, a Riemannian metric on $X$, et c. Thus, not only can we compute $Df$ as we would for any the function, but also we have a way to take the value of $Df_{\mid p}$ on a tangent vector $v \in \mathscr{T}_{X, p}$.