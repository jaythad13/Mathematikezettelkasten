---
tags:
- math-147
- top
- alg-top
- diff-geo
---

With our tools, we can now characterise all curves and surfaces topologically. We should however, first explain what we mean by curves and surfaces.

##### _definition:_ manifold

An $n$-manifold is a [[Topology --- math-147/notes/Separation properties#_definition _ Hausdorff spaces, $T_{2}$ spaces|Hausdorff]], [[Topology --- math-147/notes/Size restrictions#_definition _ second countable|second countable]] space $X$ that is locally homeomorphic to $\mathbb{R}^n$, or equivalently, an open $n$-ball, or equivalently, an open subset of $\mathbb{R}^n$. That is, every point $p \in X$ has an [[Topology --- math-147/notes/Topologies#_proposition, definition _ checking openness by neighbourhood, neighbourhood|open neighbourhood]] homeomorphic to.

It is equivalent to assume $X$ is [[Topology --- math-147/notes/Size restrictions#_definition _ separable|separable]] and [[Analysis --- math-131/notes/Metric spaces#_definition_ metric space, metric|a metric space]].

##### _example:_ non-manifolds

We assume that a manifold is Hausdorff and second countable for a reason — we want to avoid the pathological behaviour of spaces like [[Topology --- math-147/notes/Bases#_example _ the double-headed snake|two double headed snakes]] wedged together at their heads ($\mathbb{R} \sqcup \mathbb{R} / \{ x_{1}, x_{2} \mid x_{1} \equiv x_{2}, x_{1} \neq 0_{1}, x_{2} \neq 0_{2} \}$)

We assume that it is separable to avoid the pathology of the long line which is $\omega_{1} \times [0, 1)$ where $\omega_{1}$ is the first uncountable ordinal. This is kind of horrible because every increasing sequence converges and, it is [[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ connectedness|connected]] but not [[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ path-connected|path-connected]].

Now we can define curves and surfaces as manifolds of the right dimensions.

##### _definition:_ curve

A curve is a $1$-manifold.

##### _definition:_ surface

A surface is a $2$-manifold.

### Facts about triangulation

To classify these we need to make them simpler by discretising them. We do this by way of [[Simplicial homology and graph theory --- math-145/notes/Simplicial complexes#_definition _ simplicial complex|simplicial complexes]]. 

##### _definition:_ triangulation

A triangulation of an $n$-manifold $X$ is a simplicial complex $T$ (with all maximal [[Simplicial homology and graph theory --- math-145/notes/Simplicial complexes#_definition _ face, coface|faces]] have dimension $n$) so that $X$ is [[Topology --- math-147/notes/Homeomorphisms#_definition _ homeomorphism|homeomorphic]] to $T$.

Something that's neat about these triangles is that there is a way to make them smaller.

##### _definition:_ barycentric division

The barycentric division of a triangulation $T$ is its [[Simplicial homology and graph theory --- math-145/attachments/homework/hw 10/hw 10.pdf#page=12|derived complex]] with the original vertices identified with the corresponding vertices in the derived complex.

##### _theorem:_ triangulation of low-dimensional manifolds (Moise–Bing)

Every [[Topology --- math-147/notes/Compactness#_definition _ compact|compact]], [[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ connectedness|connected]] manifold of dimension at most $3$ is triangulable.

This is a hard theorem (especially in dimension $3$), but we can reasonably assume it by observation in dimension $1$.