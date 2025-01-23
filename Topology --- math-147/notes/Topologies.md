---
tags:
 - top
 - math-147/1
---

> Topology is analysis without the [[Mathematical Analysis I --- math-131/notes/Metric spaces|metric]].

\- Francis Su

Topology is about those properties that are preserved by [[Mathematical Analysis I --- math-131/notes/Continuity|continuous maps]] of metric spaces, but metric spaces themselves contain additional information. 

##### _example:_ continuous maps don't preserve metric properties

With the Euclidean metric on $\mathbb{R}$ we can tell that $(0, 1)$ is bounded and $\mathbb{R}$ is not. However, continuous maps don't care about this information — in the (hypothetical) [[Basic category theory --- basic-cat/notes/Categories#_definition _ category|category]] where continuous maps are the morphisms, $(0, 1)$ and $\mathbb{R}$ are isomorphic. 

The one thing we do know that uniquely characterises continuous maps of metric spaces is that [[Mathematical Analysis I --- math-131/notes/Continuity#_proposition _ $ varepsilon$-$ delta$ continuity is equivalent to topological continuity|open sets pull back to open sets]]. Therefore a topology should contain exactly that information — just the open sets. In fact, we can abstract away the metric, and just deal with open sets that satisfy the [[Mathematical Analysis I --- math-131/notes/Open and closed sets|properties]] of open subsets of metric spaces.

##### _definition:_ topology, open sets, topological space

A topology $\mathcal{T}$ on a set $X$ is a collection of subsets (called open sets) of $X$ such that
1) $\emptyset \in \mathcal{T}$
2) $X \in \mathcal{T}$
3) for any two open sets $U, V \in \mathcal{T}$ their intersection $U \cap V \in \mathcal{T}$.
4) arbitrary unions of open sets $U_{\alpha} \in \mathcal{T}$, $\bigcup_{\alpha} U_{\alpha}$ are also in $\mathcal{T}$.

A topological space is the data of a set $X$ and a topology $\mathcal{T}$ on it. We usually just write $X$ to represent the space (when it's clear which topology it has).

### Properties of topological spaces

For the rest of this note, let $X$ be an arbitrary topological space with topology $\mathcal{T}$.

##### _proposition:_ finite intersections of open sets are open

If $U_{1}, \dots, U_{n} \subset X$ are finitely many open sets, then their intersection is open.

###### _proof sketch:_

Proceed by induction — the base case $n = 1$ is true since $U_{1}$ is open, $n = 2$ is true by the definition of a topological space, and we can use $n = 2$ and the case of $n$ to show that $(U_{1} \cap \dots \cap  U_{n}) \cap U_{n + 1}$ is the open intersection of two open sets.

Note that this doesn't prove that the infinite intersection of open sets is open (that would require transfinite induction, which requires more things to be true). In fact, there is an example of the opposite —

![[Mathematical Analysis I --- math-131/notes/Open and closed sets#_example _ a non-open (countably) infinite intersection of open sets|Open and closed sets]]