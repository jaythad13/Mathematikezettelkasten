---
tags:
- top
- math-147/5
---

Let $(X, \mathcal{T})$ be a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]].

Just as with closedness and limit points, we can extend our metric space notions of [[Analysis --- math-131/notes/Metric spaces#_definition _ interior point|interior]] and boundary to arbitrary topological spaces.

### Interior

The interior of a set is the set of points where you could wiggle and stay in the set.

##### _definition:_ interior, interior point

The interior of a subset $A \subseteq X$ is $A^\circ$, the union of all open subsets of $A$.

Points of $A^\circ$ are called interior points of $A$.

Notice that being an interior point of $A$ is equivalent to having an open neighbourhood $U$ contained in $A$. Thus, every point of $A$ being interior is equivalent to every point having an open neighbourhood [[Topology --- math-147/notes/Topologies#_proposition, definition _ checking openness by neighbourhood, neighbourhood|is equivalent to]] $A$ being open.

### Boundary

Boundary points are close to or contained in both, a set and its complement.

##### _definition:_ boundary

The boundary of a subset $A \subseteq X$ is $\partial A = \overline{A} \cap \overline{X \setminus A}$.

Note that an [[Topology --- math-147/notes/Limit points and closed sets#_definition _ isolated point|isolated point]] of a set is a boundary point. This is what makes it tricky to prove our next result —

##### _proposition:_ interior, exterior, and the boundary are the whole space

For each subset $A \subseteq X$ the interior $A^\circ$, the exterior $(X \setminus A)^\circ$, and the boundary $\partial A$ are disjoint and union to the entire space $X$.

###### _proof:_

Notice that the interior and exterior of a set are disjoint since they are subsets of the disjoint sets $A$ and $X \setminus A$ respectively. If $x \in \partial A$ and is contained in either $A$ or $X \setminus A$ then $x$ isn't contained in the interior of the other. If $x$ is in neither $A$ nor $X \setminus A$, then it is a limit point of both. That is, each neighbourhood $U$ of $x$ contains points of both, $A$ and $X \setminus A$. That is, no neighbourhood of $x$ is completely contained in $A$ or $X \setminus A$ and thus, $x$ is not an interior point of $A$ nor $X \setminus A$. Thus, $\partial A$ is disjoint from both $A^\circ$ and $(X \setminus A)^\circ$.

If $x$ is not in the interior of $A$ not in the interior of $X \setminus A$, then there cannot be a neighbourhood $U$ of $x$ contained completely in $A$ or in $X \setminus A$. Thus, each neighbourhood $U$ of $x$ contains points of both $A$ and $X \setminus A$. $x$ is contained in exactly one of $A$ and $X \setminus A$ by definition, and as a result, is a limit point of the other. That is, $x \in \partial A = \overline{A} \cap \overline{X \setminus A}$.

##### _examples:_ interior points and boundaries in different topologies on $\mathbb{R}$

1) In the discrete topology (on any set), every subset is it's own interior and has no boundary (since [[Topology --- math-147/notes/Limit points and closed sets#_example _ closed sets in different topologies|every set is its own closure]] giving $\overline{A} \cap  \overline{X \setminus A} = A \cap (X \setminus A)$ empty)
2) In the indiscrete topology (on any set), every subset has no interior and consists entirely of its boundary.
3) In the cofinite topology on $\mathbb{R}$ $[0, 1] \cup \{ 2 \}$ has no interior and consists entirely of its boundary.
4) In the Euclidean topology on $\mathbb{R}$, $[0, 1] \cup \{ 2 \}$ has interior $(0, 1)$ and boundary $\{ 0, 1, 2 \}$.