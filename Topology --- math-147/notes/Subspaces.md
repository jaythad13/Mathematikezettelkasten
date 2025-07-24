---
tags:
- math-147/9
- top
---

Let $(X, \mathcal{T})$ be a topological space.

If we have a topological space $X$, what's the natural way to make $Y \subseteq X$ a topological space? [[Analysis --- math-131/notes/Metric subspaces#_theorem _ the subspace topology|In analysis]], we saw that the natural idea is to consider intersections of open sets in $X$ with $Y$. Our idea for topological spaces should generalise this, and in fact, are just this idea.

##### _definition:_ subspace topology

For $Y \subseteq X$, the collection of subsets of $Y$,
$$
\mathcal{T}_{Y} = \{ U \mid U = V \cap Y \text{ for some } V \in \mathcal{T} \}
$$
is a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topology]] on $Y$ called the subspace topology.

The topological space $(Y, \mathcal{T}_{Y})$ is called a subspace of $X$.

We should verify that this really is a topology.

##### _proposition:_ the subspace topology is a topology

For $Y \subseteq X$, the subspace topology on $Y$ is a topology on $Y$.

##### _example:_ subspaces of the real line

Consider $Y = [0, 1)$ as a subspace of $\mathbb{R}$ with the Euclidean topology. In $Y$ the set $[1/2, 1)$ is closed since its complement in $Y$ is $[0, 1 / 2)$ is open (as the intersection of, say, $(-1 / 2, 1 / 2) \cap Y$). 

Notice that from this example, being open or closed in $Y$ doesn't necessarily imply the same in $X$.

##### _proposition:_ closed sets in a subspace

$A \subseteq Y \subseteq X$ is closed in $Y$ if and only if $A = B \cap Y$ for some closed set $B \subseteq X$.

###### _proof:_

$A$ closed in $Y$ [[Topology --- math-147/notes/Limit points and closed sets#_theorem _ closed sets are complements of open sets|is equivalent to]] $(Y \setminus A)$ open in $Y$ is equivalent to $(Y \setminus A) = Y \cap U$ for $U$ open in $X$. Equivalently, $X \setminus U$ contains exactly those points of $Y$ that are not in $Y \setminus A$. Equivalently, $A = Y \cap (X \setminus U)$. Notice $X \setminus U$ is closed and choose $B = X \setminus U$.

##### _corollary:_ [[Topology --- math-147/notes/Limit points and closed sets#_definition _ closure, closed|closures]] in a subspace

$A \subseteq Y \subseteq X$ is closed in $Y$ if and only if $A = \operatorname{Cl}_{X}(A) \cap Y$.

###### _proof:_

If $A = \operatorname{Cl}_{X}(A) \cap Y$ then it is the intersection of $Y$ with a larger closed set and is thus closed.

If $A$ is closed, then there is some closed $B \subseteq X$ such that $B \cap Y = A$. Since the closure, is the [[Topology --- math-147/notes/Limit points and closed sets#_proposition _ the closure is the smallest closed set|smallest closed set]] containing $A$, $\operatorname{Cl}_{X}(A) \cap Y \subseteq A$, but since both the closure and $Y$ contain $A$, the inclusion is reversed too — $A = \operatorname{Cl}_{X}(A) \cap Y$.

##### _proposition:_ [[Topology --- math-147/notes/Bases|bases]] for a subspace

If $Y \subseteq X$ is a subspace, and $\mathcal{B}$ is a basis for the topology $\mathcal{T}$ on $X$, then $\mathcal{B}_{Y} = \{ B \cap Y \mid B \in  \mathcal{B} \}$ is a basis for the subspace topology $\mathcal{T}_{Y}$ on $Y$.

###### _proof:_

Clearly, $\mathcal{B}_{Y} \subseteq \mathcal{T}_{Y}$ since $\mathcal{B} \subseteq \mathcal{T}$ and $\mathcal{B}_{Y}$ consists of intersections with $Y$.

Each open $U$ in $\mathcal{T}_{Y}$ is $V \cap Y$ for some open set $V$ in $\mathcal{T}$. Thus, for each point $p \in U \subseteq V$, there is a basic open set $B \in \mathcal{B}$ with $p \in B \subseteq V$. Thus, $p \in B \cap Y \subseteq U$. That is, each open set in $\mathcal{T}_{Y}$ is covered by basic open sets which is [[Topology --- math-147/notes/Bases#_proposition _ equivalent conditions to be a basis of a specific topology|sufficient to show]] $\mathcal{B}_{Y}$ is a basis of $\mathcal{T}_{Y}$.

##### _example:_ a subspace of the lexicographically ordered square

The [[Topology --- math-147/notes/Subbases#_example _ the lexicographical order on the square|lexicographically ordered square]] $[0, 1] \times [0, 1]$ has interesting subspaces.

$D = \{ (x, 1 / 2) \mid 0 < x < 1 \}$ has the discrete (subspace) topology (as does any generic open horizontal line segment). In fact, this is the "same" topological space as $(0, 1)$ with the discrete topology if we forget about the $1 / 2$ in the second component of its points.

We can see that $D$ is discrete by showing that every point is open. Notice that for any $(x, 1 / 2) \in D$, there is a basic open set $\{ (x, y) \mid 0 < y < 1 \}$ in the lexicographically ordered square. It intersects $D$ at exactly one point — $(x, 1 / 2)$. Thus, each point is open and $D$ is discrete.

 $E = \{ (1 / 2, y) \mid 0 < y < 1 \}$ has the usual Euclidean topology of $(0, 1)$ (as does any generic open vertical line segment). It is the "same" topological space as $(0, 1)$ with the subspace topology inherited from $\mathbb{R}$ if we forget about the $1 / 2$ in the first component of its points.

Any [[Topology --- math-147/notes/Subbases#_definition _ subbasis|subbasic open set]] has intersection $\{ 1 /2 \} \times (0, b)$ or $\{ 1 / 2 \} \times (a, 1)$ with $E$. Thus, taking finite intersections of these yields the familiar intervals $(a, b) \subseteq \mathbb{R}$ rotated onto the square as $\{ 1 / 2 \} \times (a, b)$.

$F = \{ (x, 1) \mid 0 < x < 1 \}$ has the [[Topology --- math-147/notes/Bases#_example _ lower limit topology|lower limit topology]] of $(0, 1)$ (it is a special, non-generic horizontal line segment). Consider the intersection of any basic open set $U = \{ (x, y) \mid (x_{1}, y_{1}) < (x, y) < (x_{2}, y_{2}) \}$ in the lexicographical square with $F$. If  $y_{1} < 1$, then $(x_{1}, y_{1}) < (x_{1}, 1)$ and $U \cap F$ must contain $(x_{1}, 1)$. Further, all $x_{1} < x < x_{2}$ have $(x, 1) < (x_{2}, y_{2})$ so $U \cap F$ is all of the half open interval $[x_{1}, x_{2})$. This generates the lower limit topology on $F$.
