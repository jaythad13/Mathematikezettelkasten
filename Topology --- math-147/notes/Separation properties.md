---
tags:
- math-147/11
- math-147/12
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

##### _example:_ any metric space is regular and normal

Consider any closed sets $A, B$ in a metric space $X$, and a point $p \in X$ not in $A$. For concreteness we could work in $\mathbb{R}^{2}$, but the proof works the same in any metric.

It's not hard to show that a metric space is regular — if $A$ is closed and $p \not\in A$, then $p \in X \setminus A$ which is open. Thus, there is an open ball of some radius $r$ centred at $p$ such that $B_{r}(p) \subseteq {X \setminus A}$. Then $r / 2$ is a positive lower bound on $\{ d(p, a) \mid a \in A \}$. Thus, the set has positive infimum.

Thus, taking the union of all balls of radius $r / 2$ (centred at points in $a$) and the ball of radius $r / 2$ at $p$, we have separated $A$ and $p$.

However, we cannot just take the the infimum of distances between two closed sets to separate them — in $\mathbb{R}^{2}$, the curves $\{ (x, 1 / x) \mid x \ge 1 \}$ and $\{ (x, -1 / x) \mid x \ge 1 \}$ get infinitely close despite each of their points being separated from all of the other set.

However, by taking small enough balls around each point, we can separate points. Specifically, for $a \in A$, choose the ball $B_{r_{a} / 2}(a)$ where $r_{a} = \inf \{ d(a, b) \mid b \in B \}$ and similarly for $b \in B$. No two balls $B_{r_{a} / 2}(a)$ and $B_{r_{b} / 2}(b)$ intersect — if they did, by the triangle inequality, the distance between $a$ and $b$ would be less than $r_{a} / 2 + r_{b} / 2 \leq r_{a}$ (assuming without loss of generality that $r_{a} > r_{b}$). Since we chose $r_{a}$ to be a lower bound on the distances between $a$ and points in $B$, this is impossible.

##### _proposition:_ hierarchy of separation properties

For all $i < j$, a $T_{j}$ space is $T_{i}$.

###### _proof sketch:_

It's easy to see that $T_{2} \implies T_{1}$ — if $x$ and $y$ can be separated with disjoint open neighbourhoods, then the neighbourhood of $x$ doesn't include $y$ and vice versa.

Now we use the fact that $T_{1}$ is equivalent to all points in the space being closed. $T_{3}$ and $T_{4}$ spaces are $T_{1}$ by definition. 

The condition to be $T_{3}$ is the same as the condition to be $T_{2}$ with one of the points replaced by a closed set. Since all points are closed sets in $T_{1}$ spaces, the $T_{3}$ implies $T_{2}$. Similarly, $T_{4}$ implies $T_{3}$ since the requirement to be $T_{4}$ replaces the point in the requirement to be $T_{3}$ with a closed set.

##### _proposition:_ points in regular spaces are super contained in neighbourhoods

$X$ is regular if and only if, for each point $p \in X$ and open neighbourhood $U$ of $p$, there is an open set $V$ such that $p \in V$ and $\overline{V} \subseteq U$.

###### _proof:_

Suppose $X$ is regular. If $p \in U$ with $U$ open, we must be able to separate $p$ from the closed set ${A = X \setminus U}$ which it is not contained in. That is, there is an open neighbourhood $V$ of $p$ and an open set $W$ containing $A$ with $V \cap W = \text{Ø}$. Notice then that ${X \setminus W}$ is closed, contains $V$, and is contained in $U = {X \setminus A}$. Since $\overline{V}$ is [[Topology --- math-147/notes/Limit points and closed sets#_proposition _ the closure is the smallest closed set|the smallest closed set]] containing $V$, we must have $\overline{V} \subseteq {X \setminus W} \subseteq U$. That is, $X$ has the desired "super containment" property.

Suppose $X$ has the "super containment" property. Consider a closed set $A$ and a point $p$ not in it. Since $U = X \setminus A$ is open, and $p \in U$, there is some open $V$ with $p \in V \subseteq \overline{V} \subseteq U$. Then $V$ and $W = {X \setminus \overline{V}} \supseteq {X \setminus U}$ are disjoint open sets with $p \in V$ and $A \subseteq W$. Since we can separate an arbitrary closed set and point not in it, $X$ must be regular.

Clearly separating sets with open sets is pretty hard. However, with some reasonable conditions on open covers of the sets, we can separate them. Typically this is used to prove normality of a space.

##### _lemma:_ the normality lemma

### Separating products

Do separation properties lift to products of sets with those properties? Sometimes!

##### _proposition:_ product of Hausdorff spaces

If $X$ and $Y$ are Hausdorff, then $X \times Y$ is Hausdorff.

###### _proof sketch:_

Take products of the separating sets in each Hausdorff factor.

##### _proposition:_ product of regular spaces

If $X$ and $Y$ are regular, then $X \times Y$ is regular.

###### _proof sketch:_

We use the equivalent "super containment" condition for regularity. Note that $\overline{U} \times \overline{V}$ is closed and contains $U \times V$ so $\overline{U \times V} \subseteq \overline{U} \times \overline{V}$.

Given some open $W$ and a point $p \in W$,

### Inheriting separation properties

Separation properties don't always descend to [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subspaces]] either. However, in nice cases they do.

##### _example:_ normality doesn't always descend to subspaces

##### _proposition:_ normality descends to closed subspaces

If $Y \subseteq X$ is closed, then the subspace topology on $Y$ is normal.