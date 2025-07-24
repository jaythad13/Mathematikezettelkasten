---
tags:
- math-199DR/7
- math-199DR/10
- alg-top
---

There are two fundamental topological invariants of a surface — the Euler characteristic and the genus. The genus is explicitly the number of holes in the surface, but the Euler characteristic is easier to compute, and carries the same information. We will define both and prove this relationship.

We will also some machinery from algebraic topology.

### Genus

The genus of a surface counts the number of holes in it cutting out curves.

##### _definition:_ genus 

The genus of a (connected) surface $X$ is $g_{X}$, the maximum number of disjoint simple closed curves that can be removed from the surface while leaving it connected.

##### _example:_ the genus of some surfaces

The genus of
1) the sphere $S^1$ is $0$
2) the torus $S^1 \times S^1$ is $1$ (cut it into a cylinder or in the opposite direction into a rectangle)
3) the Möbius strip is $1$ (cut along the centre)


### Euler characteristic

The Euler number is a fundamental topological invariant. Here we will define for Riemann surfaces (and in the process, define it for $2$-manifolds in general).

##### _definition:_ triangulation

A triangulation $X_{T}$ of a surface $X$ is a collection of closed subsets $\{ \Delta \}$ of $X$, each homeomorphic to a triangle such that any two triangles are disjoint, intersect only at a single vertex, or intersect at a single edge.

##### _definition:_ Euler characteristic of a triangulation

The characteristic of a triangulation $X_{T}$ is $\chi(X_{T}) = V - E + F$, where $V$ is the number of vertices, $E$ is the number of edges, and $F$ is the number of faces in the triangulation.

##### _definition:_ Euler characteristic

The Euler characteristic of a surface $X$ is $\chi(X) = \chi(X_{T})$ for a triangulation $X_{T}$.

##### _example:_ Euler characteristics of some surfaces

The Euler characteristic of
1) the sphere is $\chi(S^2) = 2$ (build an octahedron out of eight triangles)
2) the cylinder is $\chi(S_{1} \times [0, 1]) = 0$ (build four squares out of two triangles each, and make them into a square cylinder)
3) the disc is $\chi(\mathbb{D}) = 1$ since $\mathbb{D} \cong \Delta$ and the triangle has Euler characteristic $1$.
4) the torus is $\chi(S^1 \times S^1) = 1$ (identify the ends of the cylinder losing $4$ edges)

We should probably explain why this is well-defined.

##### _proposition:_ the Euler characteristic doesn't depend on the triangulation

For any surface $X$, any two triangulations $X_{T_{1}}$ and $X_{T_{2}}$ have $\chi(X_{T_{1}}) = \chi(X_{T_{2}})$.

###### _proof sketch:_

Essentially, we use the [[Calculus --- spivak/notes/Integration over closed rectangles#_corollary _ any upper sum is greater than any lower sum|common refinement trick]] just as we did to prove [[Simplicial homology and graph theory --- math-145/notes/Continuous and differentiable winding number#_theorem _ the continuous winding number theorem|the continuous winding number theorem]].

A refinement of a triangulation involves a triangulation of each triangle. By checking manually, one can see that any triangulation of a triangle still has the same Euler characteristic. Thus, the refinement of any triangulation of a surface still has the same Euler characteristic.

By overlaying two triangulations one can see that any two triangulations have a common refinement — take the union of their vertices and edges and add vertices where edges cross edges. Since $X_{T_{1}}$ and $X_{T_{2}}$ have the same Euler characteristic as their common refinement $X_{T}$, they have the same Euler characteristic as each other.

##### _theorem:_ Euler characteristic and genus

For $X$ a compact orientable $2$-manifold without boundary (for our purposes, [[Riemann surfaces and algebraic curves --- math-199DR/notes/Riemann surfaces|a Riemann surface]]), of genus $g$,
$$
\chi(X) = 2 - 2 g.
$$

###### _proof sketch:_

Notice that the sphere $S^2$ satisfies $\chi(S^1) = 2 - 2 g_{S^1}$ with $g_{S^1} = 0$.

It is a theorem that all surfaces come from adding handles to a sphere — removing two discs and adding a cylinder in its place. Adding a handle, almost by definition adds $1$ to the genus. However, removing the two discs drops the Euler characteristic by $1$ for each, and adding the cylinder doesn't change the Euler characteristic. That is, adding $1$ to the genus, drops the Euler characteristic by $2$.

By induction from our base case $g = 0$, $\chi(X) = 2$, we get that in general
$$
\chi(X) = 2 - 2 g.
$$