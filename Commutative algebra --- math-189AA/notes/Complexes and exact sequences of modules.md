---
tags:
- math-189AA/9
- comm-alg
---

Complexes and exact sequences of $A$-modules are exactly complexes and exact sequences in the category of $A$-modules.

![[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ complexes, exactness, short exact sequence|Complexes and exactness]]

So is homology!

![[Algebraic geometry --- rising-sea/notes/Homology of complexes#_definition _ homology, boundaries, cycles, cohomology|Homology of complexes]]

##### _example:_ the cell complex of a torus

We can draw a torus $X$ as a the [[Topology --- math-147/notes/Quotient and identification spaces#_definition _ identification space|identification space]] $\mathbb{C} / \Lambda$ for some lattice $\Lambda$. We can write this identification space as a cell complex — a disjoint union of points, lines, discs et c., modulo some attaching equivalence relations. We have one $0$-cell, two $1$-cells, and one $2$-cell.

Write the module of $0$-cells as $\mathbb{Z}$, $1$-cells as $\mathbb{Z}^{\oplus 2}$, and $2$-cells as $\mathbb{Z}$ again. Then, we have a map from $k$-cells to $(k - 1)$-cells by mapping a cell to its boundary. That is, send the $1$-cell between $0$-cells $v_{1}, v_{2}$ to the $0$-cell $v_{2} - v_{1}$. In this case, all $0$-cells on the torus have no boundary. Note that if we did this over $\mathbb{Z} / (2)$, then we wouldn't need to care about signs at all.

Taking homology gives $H_0(X) = \mathbb{Z} = H_{2}(X)$ and $H_{1}(X) = \mathbb{Z}^{\oplus 2}$ which tells us that the space has one connected component, two one-dimensional holes, and is a closed surface with one two-dimensional hole.
