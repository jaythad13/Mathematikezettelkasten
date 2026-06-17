---
tags:
- uc-2026/morse-theory/1
- carmen-rovi
- diff-geo
- alg-top
---

We should probably know what objects we are computing invariants of.

##### _definition:_ manifold

An **$n$-dimensional manifold $X$**, is a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]] which is locally (every point has a neighbourhood that is) [[Topology --- math-147/notes/Homeomorphisms#_definition _ homeomorphism|homeomorphic]] to $\mathbb{R}^n$.

---

##### _example:_ manifolds in small dimensions

All the $0$-dimensional manifolds are [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete]] sets of points.

The $1$-dimensional manifolds (curves) are all either homeomorphic to $\mathbb{R}$ or the circle $S^1$.

The $2$-dimensional manifolds (surfaces) are more varied, but some are the sphere $S^1$ and the torus $\mathbb{T}^2 = S^1 \times S^1$.

---

In topology, we only want to understand manifolds up to continuous deformation (up to homeomorphism). One helpful way to do this is to create a polyhedral model of our manifold, and then calculate the Euler characteristic of it using the $v - e + f$ formula.

##### _example:_ the Euler characteristic of the sphere

The sphere is homeomorphic to the tetrahedron. The tetrahedron has Euler characteristic $4 - 6 + 4 = 2$. Thus, $\chi(S^2) = 2$. It doesn't just depend on choosing the tetrahedron — a square pyramid also has Euler characteristic $2$. That is, this really is a homeomorphism invariant.

---