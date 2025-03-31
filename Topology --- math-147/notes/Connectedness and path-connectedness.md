---
tags:
- math-147/16
- math-147/17
- math-147/18
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
with the flea at the point $(0, 1)$ — again, you can't split into two nice parts, but you can't walk to the flea either.

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
5) The only subsets of $X$ that are both closed and open in $X$ are $\text{Ø}$ and $X$. We say such sets are clopen.
6) For every pair of points $p, q \in X$ and open cover $\{ U_{\alpha} \}_{\alpha \in \mathcal{I}}$ of $X$ there exists a finite chain of open sets $U_{\alpha_{1}}, \dots, U_{\alpha_{n}}$ with $p \in U_{\alpha_{1}}$, $q \in U_{\alpha_{n}}$ and non-empty intersections $U_{\alpha_{i}} \cap U_{\alpha_{i + 1}}$.

###### _proof:_

We prove the equivalence cyclically with the exception of (1) $\iff$ (2).

If there were a continuous surjection $f : X \to \{ 0, 1 \}$, we would have $X$ as the union of two disjoint open sets $f^\text{pre}(0)$ and $f^\text{pre}(1)$. Thus, if $X$ is connected, there is no such surjection. If $X$ is disconnected with $A, B$ disjoint open sets that have union $X$, then clearly $f : X \to \{ 0, 1 \}$ with $f(a) = 0$ for all $a \in A$ and $f(b) = 1$ for all $b \in B$ is continuous. This is (1) $\iff$ (2).

If $X$ were the union of two non-empty separated sets $A, B$, then since $A \cap \overline{B} = \text{Ø}$, $A = {X \setminus \overline{B}}$ is open, and similarly, so is $B$. Then $X$ would be disconnected. That is, if $X$ is connected, it cannot be the union of two non-empty separated sets. This is (the contrapositive of) (2) $\iff$ (1) $\implies$ (3).

If $X$ were the union of two disjoint non-empty closed sets $A$ and $B$, then since the sets are their closure, they are also separated. Thus, if $X$ is not the union of non-empty separated sets, it is not the union of any pair of non-empty disjoint closed sets. This is (the contrapositive of) (3) $\implies$ (4).

If $A \subseteq X$ is closed and open, then ${B = X \setminus A}$ is also both closed and open. If $X$ is not the union of two disjoint non-empty closed sets, then one of $A$ and $B$ must be empty and the other, the whole space.  This is (4) $\implies$ (5).

Consider an open cover $\{ U_{\alpha} \}_{\alpha \in \mathcal{I}}$ of $X$. Let $\Omega_{p}$ be the set of all points $p' \in X$ such that, for every open cover of $X$, there is a finite chain of open sets between them. $\Omega_{p}$ is clearly open since each point has an open neighbourhood. $\Omega_{p}$ is also closed. Every neighbourhood of any limit point $q$ of $\Omega_{p}$ intersects $\Omega_{p}$, and so the $U_{\beta}$ containing $q$ intersects $\Omega_{p}$ at some point $p' \in \Omega_{p}$. Then if $U_{\alpha_{1}}, \dots, U_{\alpha_{n}}$ is the finite chain of open sets from $p$ to $p'$, the chain $U_{\alpha_{1}}, \dots, U_{\alpha_{n}}, U_{\beta}$ connects $p$ and $q$. Thus, any limit point $q \in \Omega_{p}$. Then $\Omega_{p}$ is clopen and non-empty, and thus, all of $X$. This is (5) $\implies$ (6).

If (6) holds, then any open cover $X = A \cup B$ with $A$ and $B$ non-empty must have $A \cap B$ non-empty. Thus, $X$ is connected. That is, (6) $\implies$ (1).

##### _proposition:_ continuous functions preserve connectedness

Suppose $f : X \to Y$ is a continuous surjection. If $X$ is connected, then $Y$ is connected.

###### _proof:_

If $Y$ is disconnected into disjoint open sets $V_{1} \cup V_{2}$, then their pre-images are disjoint and open too since $f$ is continuous. They also cover $X$ (since every point in $x$ is the pre-image of some point in $Y$). Thus, if $Y$ is not connected, $X$ is not connected — the contrapositive of the result.

Since subsets of $\mathbb{R}$ are only connected if they contain every $z$ between each pair $x, y$ in the set, we get the intermediate value theorem —
![[Mathematical Analysis I --- math-131/notes/Continuity#_corollary _ intermediate value theorem|Connectedness]]

### Path-connectedness

Path-connectedness is a stronger notion that requires you to be able to walk between any two points on the space.

##### _definition:_ path

A path from $p$ to $q$ in $X$ is a [[Topology --- math-147/notes/Continuous functions#_definition _ continuity|continuous function]] $f : [0, 1] \to X$ with $f(0) = p$ and $f(1) = q$.

##### _definition:_ path-connected

$X$ is a path-connected if every pair of points $p, q \in X$ has a path between them.

##### _proposition:_ path-connectedness is stronger

If $X$ is path-connected, $X$ is connected.

###### _proof:_

Suppose $X$ is path-connected. Consider $p, q \in X$ and an open cover $\{ U_{\alpha} \}_{\alpha \in \mathcal{I}}$ of $X$. Since $[0, 1]$ is compact, its image under $f$ is [[Topology --- math-147/notes/Compactness|compact]] and connected. Thus, we have a finite cover $U_{\alpha_{1}}, \dots, U_{\alpha_{n}}$ of $f^\text{img}([0, 1])$, which we choose to order by "left ends" of their pre-images under $f$. Each pair $U_{\alpha_{i}}, U_{\alpha_{i + 1}}$ must have non-empty empty intersection, since the pre-images of $\{ U_{\alpha_{i}} \}$ is an open cover of $[0, 1]$ which must admit a finite sub-chain with the desired property.

##### _example:_ the flea and comb space is connected but not path-connected

Note that the comb itself is path-connected. It follows that the comb is connected, and thus, that is closure is connected.

However, the closure of the comb is not path-connected. Consider a path from the flea $p$ to any other point $q$. Since $p$ is in the upper half plane, there is some neighbourhood around