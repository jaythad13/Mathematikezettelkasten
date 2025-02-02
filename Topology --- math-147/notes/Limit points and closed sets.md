---
tags:
- math-147/2
- math-147/3
- top
---

For this note, let $X$ be a topological space with topology $\mathcal{T}$.

### Limit points

Limit points of are points very close to it. With metric spaces, we could [[Mathematical Analysis I --- math-131/notes/Metric spaces#_definition _ limit point|define them]] as having no finite distance from the set. Without the metric, our notion of nearness, is instead "contained in the same small open set".

##### _definition:_ limit point

A subset $A \subseteq X$ has limit point $p$ if every [[Topology --- math-147/notes/Topologies#_proposition, definition _ checking openness by neighbourhood, neighbourhood|open neighbourhood]] $U$ of $p$ has $(U \setminus \{ p \}) \cap A$ non-empty.

That is, $p$ is a limit point of $A$ if every neighbourhood of $p$ intersects $A$ at a point other than $p$. Of course, whether this is true depends on the topology on $X$.

##### _example:_ there are more limit points in coarser topologies

$0$ is a limit point of $(1, 2)$ in the indiscrete topology on $\mathbb{R}$ because the only open set containing $0$ is all of $\mathbb{R}$. 

Similarly, any open set of $0$ in the cofinite topology can only exclude finitely many points of $(1, 2)$, and so must have non-trivial intersection with $(1, 2)$. That is, $0$ is a limit point of $(1, 2)$ in the cofinite topology. In both of the previous examples, $0$ is not special — any point is a limit point of $(1, 2)$ or any infinite set.

$0$ is not a limit point of $(1, 2)$ in the Euclidean topology or the discrete topology — $0 \in (-1, 1)$ which has empty intersection with $(1, 2)$.

We should probably justify the removal of $p$ from neighbourhoods that we care about. Essentially this only a condition to stop something like $0$ being a limit point of the set $(1, 2) \cup \{ 0 \}$ (in the Euclidean topology).

##### _proposition:_ limit points not in the set

If $p \not\in A \subseteq X$, $p$ is not a limit point of $A$ if and only if there exists a neighbourhood $U$ of $p$ such that $U \cap A$ is empty.

###### _proof:_

If $p \not\in A$, then $(U \setminus \{ p \}) \cap A$ is just the same as $U \cap A$ since the intersection with $A$ removes $p$ anyway. But then it just follows from the negation of the definition of a limit point that $p$ is not a limit point of $A$ if and only if $U \cap A$ is empty for some neighbourhood of $p$.

##### _definition:_ isolated point

If $p \in A \subseteq X$, but $p$ is not a limit point of $A$, $p$ is an isolated point of $A$.

##### _proposition:_ isolated points have neighbourhoods with singleton intersection

If $p$ is an isolated point of $A \subseteq X$, there is an open neighbourhood $U$ of $p$ with $U \cap A = \{ p \}$.

###### _proof:_

Since $p$ is not a limit point of $A$, then there is an open neighbourhood $U$ with $(U \setminus \{ p \}) \cap A$ empty. Since $U$ contains $p$ and so does $A$, we have
$$
U \cap A = ((U \setminus \{ p \}) \cap A) \cup \{ p \} = \{ p \}.
$$

##### _example:_ limit points of a half-open interval

The set $[0, 1) \cup \{ 2 \}$ (in $\mathbb{R}$ with the standard topology) has
- limit point $0$ that is in the set
- limit point $1$ that is not in the interval
- $2$ is an isolated point
- $3$ is not in the set or a limit point of it

### Closure

Since, in some sense, the closed points "have no distance from the set", we want to think about the sets where all of these infinitely close points are in the set.

##### _definition:_ closure, closed

The closure $\overline{A}$ of $A \subseteq X$ is the set containing $A$ and all of its limit points.

A subset $A \subseteq X$ is closed if it is its own closure.

We might want to verify that closure is indeed closed.

##### _proposition:_ the closure is closed

For any $A \subseteq X$, the closure of $A$ is closed. That is, $\overline{\overline{A}} = \overline{A}$.

###### _proof:_

We want to show that any limit point of $\overline{A}$ is a limit point of $A$ or in $A$. Suppose $p$ is a limit point of $\overline{A}$. Then every open neighbourhood $U$ of $p$ has a non-trivial intersection with $\overline{A}$, say containing $q \in \overline{A}$. If $q \in A$, we are done. If not, $q$ is a limit point of $A$, and every open neighbourhood $V$ of $q$ has a non-trivial intersection with $A$. Since $U$ is open, [[Topology --- math-147/notes/Topologies#_proposition, definition _ checking openness by neighbourhood, neighbourhood|pick the neighbourhood]] $V \subseteq U$ which gives us that $U$ also has non-trivial intersection with $A$.

##### _example:_ closed sets in different topologies

In the discrete topology, every set is closed because there are no limit points — every point $p$ has open neighbourhood $\{ p \}$.

In the indiscrete topology, $X$ and $\emptyset$ are closed.

In the finite complement topology, the finite sets are exactly the closed sets — given any infinite set, every point is a limit point of it, and given a finite set, any point is contained in an open set with all of the other points of the finite set poked out. In the countable complement topology, the countable sets are exactly the closed sets for essentially the same reason.

This seems to hint that the closed sets are just the complement of open sets. [[Mathematical Analysis I --- math-131/notes/Open and closed sets#_theorem _ closed sets are complements of open sets|Just as for metric spaces]] this is true.

##### _proposition:_ closed sets are complements of open sets

Any $A \subseteq X$ is closed if and only if $X \setminus A$ is open.

###### _proof:_

First suppose $A$ is closed. Since $A$ contains all its limit points, every point $x \in X \setminus A$ is not a limit point of $A$, and thus has an open neighbourhood $U_{x} \subseteq X \setminus A$ (a neighbourhood with no intersection with $A$). [[Topology --- math-147/notes/Topologies#_proposition, definition _ checking openness by neighbourhood, neighbourhood|Thus,]] $X \setminus A$ is open.

Suppose $X \setminus A$ is open. Then every point $x \in X \setminus A$ has an open neighbourhood $U_{x} \subseteq X \setminus A$, and thus, has no intersection with $A$. That is, $x$ is not a limit point of $A$. Thus, $A$ contains all its limit points.