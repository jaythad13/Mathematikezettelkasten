---
tags:
- math-145/13
- alg-top
---

Relative homology gives a way to quotient a geometric object without the quotient having to be geometric — an algebraic version of the quotient. Given [[Topics in Geometry and Topology --- math-145/notes/Simplicial complexes#_definition _ simplicial complex|simplicial complexes]] $X, Y$ with $Y \subseteq X$, we want to define the relative homology $\mathrm{H}_{*}(X, Y)$. Essentially, we're skipping the step of defining $X / Y$, and just defining the homology of it to be $\mathrm{H}_{*}(X, Y)$.

### Relative chains, boundaries, and cycles

##### _definition:_ relative chains

The relative chain complex $\mathrm{C}_{*}(X, Y)$ is given by $\mathrm{C}_{k}(X, Y) = \mathrm{C}_{k}(X) / \mathrm{C}_{k}(Y)$.

##### _definition:_ relative boundary

The regular boundary maps $\partial_{X, k} : \mathrm{C}_{k + 1}(X) \to \mathrm{C}_{k}(X)$ descend to boundary maps $\partial_{X / Y, k} : \mathrm{C}_{k + 1}(X, Y) \to \mathrm{C}_{k}(X, Y)$ called the relative boundary maps.