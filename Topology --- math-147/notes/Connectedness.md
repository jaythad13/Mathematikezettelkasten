---
tags:
- math-147/16
- top
---

Let $(X, \mathcal{T})$ be a topological space.

Connectedness seems to be obvious — if a topological space can't be split up into two distinct pieces or you can walk from any point to another, it's connected. How to define what distinct means, and the consequences for whether more pathological spaces are connected are more subtle.

##### _examples:_ things that are obviously not connected

- The disjoint union of any two topological spaces should not be connected.
- $(0, 1) \cup (1, 2)$, since you can draw a line between the two intervals at $1$.
- Any [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete space]].

##### _examples:_ things that are obviously connected

- $(0, 1)$ and $[0, 1]$ since any way to split them must assign the boundary to one and the rest to the other.

##### _examples:_ where it's less clear

- The closure of the topologist's sine curve $S = \{ (x, \sin(1 / x)) \mid x \in (0, 1) \}$ in $\mathbb{R}^{2}$ — you can't split into two nice parts, but you can't walk from the squiggly bits to the limiting vertical line on the $y$ axis.
- The union of the topologist's comb 
$$
C = \{ (x, 0) \mid x \in [0, 1] \} \cup \bigcup_{n = 1}^\infty \{ (1/n, y) \mid y \in [0, 1] \}
$$
with the fly at the point $(0, 1)$ — again, you can't split into two nice parts, but you can't walk to the fly either.

### Connectedness

It turns out that the notion of walking is strictly stronger than the regular notion of connectedness, and we will call it path-connectedness. For now, just regular connectedness.

##### _definition:_ connectedness

$X$ is connected if $X$ is not the union of two disjoint, non-empty, open sets.

This has many equivalent definitions, including one in terms of separated sets.

##### _definition:_ separated

$A, B \subseteq X$ are separated if neither of them intersects with the other's [[Topology --- math-147/notes/Limit points and closed sets#_definition _ closure, closed|closure]] — $\overline{A} \cap B = \text{Ø}$ and $A \cap \overline{B} = \text{Ø}$.

We write $X = A \mid B$ to indicate that $X$ is the union of separated sets $A$ and $B$.

##### _proposition:_ conditions equivalent to connectedness

The following are equivalent
1) $X$ is connected.
2) There is no continuous surjective function $f : X \to \{ 0, 1 \}$ (where $\{ 0, 1 \}$ is given the discrete topology).
3) $X$ is not the union of two non-empty separated sets.
4) $X$ is not the union of two disjoint non-empty closed sets.
5) The only subsets of $X$ that are both closed and open in $X$ are $\text{Ø}$ and $X$.
6) For every pair of points $p, q \in X$ and open cover $\{ U_{\alpha} \}_{\alpha \in \mathcal{I}}$ of $X$ there exists a finite chain of open sets $U_{\alpha_{1}}, \dots, U_{\alpha_{n}}$ with $p \in U_{\alpha_{1}}$, $q \in U_{\alpha_{n}}$ and non-empty intersections $U_{\alpha_{i}} \cap U_{\alpha_{i + 1}}$.

###### _proof:_

We prove the equivalence cyclically with the exception of (1) $\iff$ (2) and (1) $\iff$ (5)

If there were a continuous surjection $f : X \to \{ 0, 1 \}$, we would have $X$ as the union of two disjoint open sets $f^\text{pre}(0)$ and $f^\text{pre}(1)$. Thus, if $X$ is connected, there is no such surjection. If $X$ is disconnected with $A, B$ disjoint open sets that have union $X$, then clearly $f : X \to \{ 0, 1 \}$ with $f(a) = 0$ for all $a \in A$ and $f(b) = 1$ for all $b \in B$ is continuous.

If $X$ were the union of two non-empty separated sets $A, B$, then since $A \cap \overline{B} = \text{Ø}$, $A = {X \setminus \overline{B}}$ is open, and similarly, so is $B$. Then $X$ would be disconnected. That is, if $X$ is connected, it cannot be the union of two non-empty separated sets.

If $X$ were the union of two disjoint non-empty closed sets $A$ and $B$, then since the sets are their closure, they are also separated. Thus, if $X$ is not the union of non-empty separated sets, it is not the union of any pair of non-empty disjoint closed sets.

If $A \subseteq X$ is closed and open, then ${B = X \setminus A}$ is also both closed and open. If $X$ is not the union of two disjoint non-empty closed sets, then one of $A$ and $B$ must be empty and the other, the whole space. 

If $X$ is disconnected as the disjoint union of non-empty open sets $A$ and $B$, then $A$ and $B$ are clearly also both closed.

Suppose $X$ is connected. 