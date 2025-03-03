---
tags:
- math-147/11
- top
---

Let $(X, \mathcal{T})$ be a topological space.

Separation properties are really interesting definitions with terrible names. They allow us to get an idea of how strong topologies are and whether there exist degeneracies in the topology that don't allow it to see differences that we might want it to.

##### _definition:_ $T_{1}$ space

$X$ is $T_{1}$ if every pair of distinct points $x, y \in X$ have open neighbourhoods $U_{x}, U_{y}$ respectively such that $y \not\in U_{x}$ and $x \not\in U_{y}$.

This condition is equivalent to points being closed.

##### _proposition:_ $T_{1}$ spaces are spaces with all closed points 

$X$ is $T_{1}$ if and only if each $x \in X$ forms a closed set $\{ x \}$.

###### _proof sketch:_

$x \in X$ being closed is equivalent to every $y \in X$ not being a limit point of $x$, is equivalent to $y$ having an open neighbourhood that doesn't touch $X$. This is symmetric in $x$ and $y$.

##### _example:_ the [[Topology --- math-147/notes/Topologies#_example _ the finite and countable complement topologies|cofinite topology]] is $T_{1}$

The cofinite topology is $T_{1}$ since [[Topology --- math-147/notes/Limit points and closed sets#_theorem _ closed sets are complements of open sets|all finite sets are closed]].

##### _definition:_ Hausdorff spaces, $T_{2}$ spaces

$X$ is Hausdorff (or $T_{2}$) if every pair of distinct points $x, y \in X$ has a pair of disjoint open neighbourhoods $U_{x}, U_{y}$.

##### _example:_ $\mathbb{R}$ is clearly Hausdorff

##### _definition:_ regular spaces, $T_{3}$ spaces

$X$ is regular if for every point $x \in X$, and closed set $A \subseteq X$ not with $x \not\in A$, there are disjoint open sets $U$ and $V$ containing $x$ and $A$ respectively.

$X$ is $T_{3}$ if it is regular and $T_{1}$.

##### _example:_ [[Topology --- math-147/notes/Bases#_example _ the sticky bubble topology|the sticky bubble topology is regular]]

##### _definition:_ normal spaces, $T_{4}$ spaces

$X$ is normal if every pair of disjoint closed sets $A, B \subseteq X$ has a pair of disjoint open sets containing the respective closed set.

##### _example:_ the [[Topology --- math-147/notes/Bases#_example _ lower limit topology|lower limit topology]] on $\mathbb{R}$ is normal

##### _example:_ the plane is regular and normal

##### _proposition:_ hierarchy of separation properties

For all $i < j$, a $T_{j}$ space is $T_{i}$.