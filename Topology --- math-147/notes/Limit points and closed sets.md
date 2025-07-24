---
tags:
- math-147/2
- math-147/3
- math-147/4
- top
---

For this note, let $X$ be a topological space with topology $\mathcal{T}$.

### Limit points

Limit points of are points very close to it. With metric spaces, we could [[Analysis --- math-131/notes/Metric spaces#_definition _ limit point|define them]] as having no finite distance from the set. Without the metric, our notion of nearness, is instead "contained in the same small open set".

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

This seems to hint that the closed sets are just the complement of open sets. [[Analysis --- math-131/notes/Open and closed sets#_theorem _ closed sets are complements of open sets|Just as for metric spaces]] this is true.

##### _theorem:_ closed sets are complements of open sets

Any $A \subseteq X$ is closed if and only if $X \setminus A$ is open.

###### _proof:_

First suppose $A$ is closed. Since $A$ contains all its limit points, every point $x \in X \setminus A$ is not a limit point of $A$, and thus has an open neighbourhood $U_{x} \subseteq X \setminus A$ (a neighbourhood with no intersection with $A$). [[Topology --- math-147/notes/Topologies#_proposition, definition _ checking openness by neighbourhood, neighbourhood|Thus,]] $X \setminus A$ is open.

Suppose $X \setminus A$ is open. Then every point $x \in X \setminus A$ has an open neighbourhood $U_{x} \subseteq X \setminus A$, and thus, has no intersection with $A$. That is, $x$ is not a limit point of $A$. Thus, $A$ contains all its limit points.

Closed and open sets preserve our intuition from [[Analysis --- math-131/notes/Open and closed sets|metric spaces]]. For one, we can remove an open set from a closed set to get a closed set, and vice versa.

##### _proposition:_ open set minus closed set and closed set minus open set

If $A \subseteq X$ is closed and $U \subseteq X$ is open, then $U \setminus A$ is open and $A \setminus U$ is open.

###### _proof:_

$U \setminus A = U \cap (X \setminus A)$ is the intersection of two open sets, and thus, is open by definition.

Similarly, $X \setminus (A \setminus U) = U \cup (X \setminus A)$ is the union of two open sets and thus, is open. Now, by our previous propositions, $A \setminus U$ must be closed.

By using [[Analysis --- math-131/notes/Open and closed sets#_theorem _ De Morgan's law|De Morgan's law]], we can also get the [[Analysis --- math-131/notes/Open and closed sets#_corollary _ finite unions and (potentially infinite) intersections of closed sets are closed|same result about unions and intersections of closed sets]] as in metric spaces. In fact, this is an alternate definition of a topological space.

##### _theorem:_ finite unions and arbitrary intersections of closed sets are closed

Suppose $(X, \mathcal{T})$ is a topological space. Then
1) $\emptyset$ is closed
2) $X$ is closed
3) unions of finitely many closed sets are closed
4) arbitrary intersections of closed sets $A_{\alpha}$, $\bigcap_{\alpha} A_{\alpha}$ are also closed.

###### _proof:_

Since $\emptyset, X$ are open, their complements $X, \emptyset$ respectively are closed.

Recall De Morgan's law —
![[Analysis --- math-131/notes/Open and closed sets#_theorem _ De Morgan's law|Open and closed sets]]

Since finite unions of closed sets $A_{i}$ are just finite unions of complements of open sets $U_{i} = X \setminus A_{i}$, their complement is just the finite intersection of open sets $X \setminus \bigcup_{i = 1}^n A_{i} = \bigcap_{i = 1}^n U_{i}$, and is open. Thus, the finite union is closed

Similarly, since intersections of closed sets $A_{\alpha}$ are just intersections of complements $U_{\alpha} = X \setminus A_{\alpha}$, their complement is just the union of open sets $X \setminus \bigcap A_{\alpha} = \bigcup_{\alpha} U_{\alpha}$, and is open. Thus, the intersection is closed.

##### _example:_ a non-closed (countably) infinite union of closed sets

We can use the "dual" example to the following.
![[Analysis --- math-131/notes/Open and closed sets#_example _ a non-open (countably) infinite intersection of open sets|Open and closed sets]]

That is, the union of all closed sets $A_{n} = (-\infty, -1 / n] \cup [1 / n, \infty)$ is $\mathbb{R} \setminus \{ 0 \}$ (since every real number other than $0$ has magnitude greater than sum $1 / n$). However, this set is not closed since $0$ is a limit point and not contained in it.

##### _example:_ closed and open sets

Consider the topological space $\mathbb{R} \sqcup \mathbb{R}$ — the disjoint union of two copies of the real line (with the Euclidean topology). The open sets here are precisely the disjoint unions of open sets in each copy of $\mathbb{R}$. We will call the two copies $\mathbb{R}_{1}$ and $\mathbb{R}_{2}$.

Each normal open set on $\mathbb{R}$ (on either copy of the line) is an open set and similarly for closed sets. For example $(0, 1) \subseteq \mathbb{R}_{1}$ is open, but not closed, and $[0, 1] \subseteq \mathbb{R}_{2}$ is closed, but not open.

However, in addition to the empty set and the whole space, we have two new sets that are both closed and open —$\mathbb{R}_{1}$ and $\mathbb{R}_{2}$ both.

Finally, $(0, 1) \sqcup [0, 1]$ is neither open nor closed — no open neighbourhood of $1 \in \mathbb{R}_{2}$ is contained in the set, and $0 \in \mathbb{R}_{1}$ is a limit point of the set, but not contained in it.

##### _example:_ closedness versus openness in different topological spaces

In $\mathbb{Z}$ with the [[Topology --- math-147/notes/Topologies#_example _ the finite and countable complement topologies|finite complement topology]], $\{ 0, 1, 2 \}$ is closed, the prime numbers are neither closed nor open, and $\{ n \mid \lvert n \rvert \ge 10 \}$ is open.

In $\mathbb{R}$ with the Euclidean topology, $(0, 1)$ is open, $(0, 1]$ is neither open nor closed, $[0, 1]$ is closed, $\{ 0, 1 \}$ is closed, $\{ 1 /n \mid n \in \mathbb{N} \}$ is neith er open nor closed.

In $\mathbb{R}^{2}$ with the Euclidean topology, the circle $S^1$ is closed, the complement of the closed disc $\mathbb{R}^{2} \setminus  \overline{\mathbb{D}}$ is open, and the complement of the open disc $\mathbb{R}^{2} \setminus \mathbb{D}$ is closed. (Here $\mathbb{D} = \{ (x, y) \mid \lVert (x, y) \rVert < 1 \}$ and $\overline{\mathbb{D}} = \{ (x, y) \mid \lVert (x, y) \rVert \le 1 \}$).

##### _proposition:_ the closure is the smallest closed set

For any $A \subseteq X$, the closure of $A$ is the intersection of all closed sets containing $A$ —
$$
\overline{A} = \bigcap_{A \subseteq B, B \text{ closed}} B.
$$

###### _proof:_

We will show double inclusion. If $x \in \overline{A}$, then $x$ is in $A$ or a limit point of $A$. Thus, $x$ is either contained in each $B \supseteq A$ or is a limit point of it (respectively). Thus, $x$ is contained in any such closed $B$. That is, $\overline{A}$ is a subset of the intersection of all closed sets containing $A$.

If $a \in \bigcap_{A \subseteq B, B \text{ closed}} B$, then since $\overline{A}$ is closed and contains $A$, $x \in \overline{A}$. That is, the intersection of all closed sets containing $A$ is a subset of $\overline{A}$. 

By double inclusion, we have the desired equality.

Using this result, we can show that closure plays nicely with unions and subsets.

##### _proposition:_ set-theoretic properties of closure

For any $A, B \subseteq X$, $A \subseteq B$ implies $\overline{A} \subseteq \overline{B}$ and $\overline{A \cup B} = \overline{A} \cup \overline{B}$.

###### _proof:_

Every closed set containing $B$ must contain $A$. By the previous result the closure of $A$ must be contained in every closed set containing $A$, and thus, in every closed set containing $B$. Since $\overline{B}$ is a closed set containing $B$, we have $\overline{A} \subseteq \overline{B}$.

Every closed set containing both $A$ and $B$, contains all the limit points of $A$ and $B$, and thus, contains $\overline{A}$ and $\overline{B}$. That is, $A \subseteq A \cup B$ and $B \subseteq A \cup B$ gives us $\overline{A} \subseteq  \overline{A \cup B}$ and $\overline{B} \subseteq \overline{A \cup B}$. Thus, $\overline{A} \cup \overline{B} \subseteq \overline{A \cup B}$. Since $\overline{A} \cup \overline{B}$ is closed (as the finite union of closed sets) and contains $A$ and $B$, by the previous result, $\overline{A \cup B} \subseteq \overline{A} \cup \overline{B}$. By double inclusion, we have the desired equality.

Obviously the theorem about pairwise unions can be extended by induction to finite unions. However, it does not extend to arbitrary unions.

##### _example:_ closure of an infinite union of sets

Recall our example of infinite unions of closed sets not being open. ![[#_example _ a non-closed (countably) infinite union of closed sets|Open and closed sets]]
The union of the open sets $U_{n} = (-\infty, -1 / n) \cup (1/n, \infty)$ is just $\mathbb{R} \setminus \{ 0 \}$ which has closure $\mathbb{R}$. However, each of these open sets has closure $\overline{U_{n}} = A_{n}$ which have union $\mathbb{R} \setminus \{ 0 \}$.

##### _example:_ two non-obvious closures

The closure of the topologist's sine curve 
$$
S = \{ (x, \sin(1 / x)) \mid x \in (0, 1) \}
$$
involves adding all the points $(0, y)$ for $y \in [-1, 1]$ as well as $\sin(1 / 1)$. That is,
$$
\overline{S} = S \cup \{ (1, \sin(1)) \} \cup \{ (0, y) \mid y \in [-1, 1] \}
$$

The closure of the topologist's comb 
$$
C = \{ (x, 0) \mid x \in [0, 1] \} \cup \bigcup_{n = 1}^\infty \{ (1 / n, y) \mid y \in [0, 1] \}
$$
is similar. It involves adding the line segment from $0$ to $1$ on the $y$-axis —
$$
\overline{C} = C \cup \{ (0, y) \in \mathbb{R}^{2} \mid y \in [0, 1] \}.
$$
the comb and flea space is $C$ with a flea at the point $(0, 1)$.