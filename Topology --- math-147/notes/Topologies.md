---
tags:
 - top
 - math-147/1
 - math-147/2
---

> Topology is analysis without the [[Analysis --- math-131/notes/Metric spaces|metric]].

\- Francis Su

Topology is about those properties that are preserved by [[Analysis --- math-131/notes/Continuity|continuous maps]] of metric spaces, but metric spaces themselves contain additional information. 

##### _example:_ continuous maps don't preserve metric properties

With the Euclidean metric on $\mathbb{R}$ we can tell that $(0, 1)$ is bounded and $\mathbb{R}$ is not. However, continuous maps don't care about this information — in the (hypothetical) [[Basic category theory --- basic-cat/notes/Categories#_definition _ category|category]] where continuous maps are the morphisms, $(0, 1)$ and $\mathbb{R}$ are isomorphic. 

The one thing we do know that uniquely characterises continuous maps of metric spaces is that [[Analysis --- math-131/notes/Continuity#_proposition _ $ varepsilon$-$ delta$ continuity is equivalent to topological continuity|open sets pull back to open sets]]. Therefore a topology should contain exactly that information — just the open sets. In fact, we can abstract away the metric, and just deal with open sets that satisfy the [[Analysis --- math-131/notes/Open and closed sets|properties]] of open subsets of metric spaces.

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

Proceed by induction — the base case $n = 1$ is true since $U_{1}$ is open (alternately, $n = 0$ is the whole set $X$), $n = 2$ is true by the definition of a topological space, and we can use $n = 2$ and the case of $n$ to show that $(U_{1} \cap \dots \cap  U_{n}) \cap U_{n + 1}$ is the open intersection of two open sets.

Note that this doesn't prove that the infinite intersection of open sets is open (that would require transfinite induction, which requires more things to be true). In fact, there is an example of the opposite —

![[Analysis --- math-131/notes/Open and closed sets#_example _ a non-open (countably) infinite intersection of open sets|Open and closed sets]]

For metric spaces, open sets are defined as those sets which contain an open ball around each of their points, often called a neighbourhood. There is an analogue for topological spaces too.

##### _proposition, definition:_ checking openness by neighbourhood, neighbourhood

A set $U$ is open in a topological space $(X, \mathcal{T})$ if and only if, for every point $x \in U$, there exists an open set $U_{x}$ such that $U_{x} \subseteq U$.

An open set containing $x$ is called a neighbourhood of $x$.

###### _proof:_

If $U$ is open, then one can choose $U_{x} = U$ for each $x$.

If for each $x \in U$, there is a neighbourhood $U_{x} \subseteq U$, then the union of all these neighbourhoods contains all $x \in U$ and thus, $U$. Conversely, since each neighbourhood is contained in $U$, so is their union. Thus,
$$
U = \bigcup_{x \in U} U_{x}
$$
is open.

This is the fact that proves that the Euclidean topology on $\mathbb{R}^n$ (and in fact, the topology induced by any metric space) [[Analysis --- math-131/notes/Open and closed sets#_proposition _ (potentially infinite) unions and finite intersections of open sets are open|really is a topology]].

##### _example:_ the Euclidean topology on $\mathbb{R}^n$ is a topology

The Euclidean topology on $\mathbb{R}^n$ is the one where a set is open if it contains an open ball around every point in it. The empty set is vacuously open, and to show $\mathbb{R}^n$ is open, we can pick any ball around each point. 

To show that the intersection of two open sets is open, choose the ball with the minimum radius. Since it is contained in the ball with the larger radius, it is contained in both sets. Since subsets are preserved by unions, the union contains the same balls around points as the sets that contain those points.

### Some interesting topologies

There are other topologies one can put on a set. We call topologies finer if they contain more and smaller open sets, and coarser if they contain fewer and larger open sets. The finest and coarsest possible topologies on any set are the discrete and indiscrete topologies.

##### _example:_ the discrete and indiscrete topologies

The discrete topology on a set $X$ has every subset an open set. Thus, this topology is closed under arbitrary unions and finite intersections.

The indiscrete topology on $X$ has (at most) two open sets — $\emptyset$ and $X$. Since the only possible unions and intersections of these subsets are $\emptyset$ and $X$, this too is really a topology.

##### _example:_ the finite and countable complement topologies

Another pair of important topologies is the finite and countable complement topologies. These are exactly what they say — topologies where open sets are the complements of finite or countable sets respectively. Instead of proving that the arbitrary unions of the complements of finite/countable sets are complements ... and so on, it's easier to prove that these are topologies by using [[Analysis --- math-131/notes/Open and closed sets#_theorem _ De Morgan's law|De Morgan's law]] and proving the complementary facts about finite and countable sets instead.

In the case where $X = \mathbb{C}$ or $\mathbb{R}$, the finite complement topology is the [[Algebraic Geometry --- math-176/notes/The Zariski topology|Zariski topology]], which is coarser than the Euclidean topology. However, this is not true of the countable complement topology since points can accumulate. For example, the complement of the countable set $\{ 1 / n \mid n \in \mathbb{N}\}$ is not open in the Euclidean topology.

Note that these different topologies have very different open sets that don't coincide with our normal idea of nearness! For example, the "open" interval $(0, 1)$ is open in the discrete topology, but not open in the indiscrete, finite complement, or countable complement topologies.