---
tags:
- alg-geo
- rising-sea/4
---

### Motivation from smooth geometry

Shemes comprise a set of points, a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topology]] on them, and a structure [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf, separated presheaf|sheaf]] (of rings) defining the algebraic functions, and thus, the geometric structure of the scheme. In short, they are [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, functions, global functions|ringed spaces]] (with some additional properties). This idea generalises from smooth manifolds in the following sense.

![[Algebraic geometry --- rising-sea/notes/Ringed spaces#_example _ smooth manifolds as (locally) ringed spaces|Ringed spaces]]

A scheme is similarly defined to be a topological space with a structure sheaf. Here, instead of a local "isomorphism of ringed spaces" to $\mathbb{R}^n$, we have a local isomorphism to an [[Algebraic geometry --- rising-sea/notes/Affine schemes|affine scheme]] (possibly different affines near different points). Finally, separatedness will be the analogue of "reasonable" topology, though we won't require it for a scheme to be a scheme. (Previously a non-separated scheme might be called a prescheme, like a non-Hausdorff manifold is called a premanifold) 

Sheaf morphisms will be similarly defined as a pair of $\pi : X \to Y$ and $\mathscr{O}_{Y} \to \pi_{*} \mathscr{O}_{X}$ so that the stalk map preserves the maximal ideal. Also, the cotangent space is *defined* as $\mathfrak{m}_{X, p} / \mathfrak{m}_{X, p}^{2}$ as the tangent space is *defined* as its dual.

### Schemes

A curious fact about more complicated definitions is that we will be able to (and will need to) define isomorphisms in our category of schemes before we can define morphisms.

##### _definition:_ scheme, isomorphism of schemes

A **scheme** is a [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, functions, global functions|ringed space]] $X, \mathscr{O}_{X}$ such that each point $p \in X$ has an open neighbourhood $U$ such that $U, \mathscr{O}_{X \mid U}$ is (isomorphic to, as a ringed spaces) an [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition _ affine scheme|affine scheme]].

An **isomorphism of schemes** is an isomorphism of ringed spaces.

---

Just as with ringed spaces in general, we refer to sections $f \in \mathscr{O}_{X}(U)$ as **functions** on $U$, and **global functions** when $U = X$.

### Examples of (non-affine) schemes