---
tags:
- alg-nt
- metric
- top
- napkin
- rtg-2025
- math-177/8
- math-177/20
---

The topology that the $p$-[[p-adic numbers --- math-177/notes/The p-adic numbers#_definition _ $p$-adic valuation, absolute value|adic absolute value]] induces on $\mathbb{Q}_{p}$ and $\mathbb{Z}_{p}$ is terrifying. In particular, $\mathbb{Z}_{p}$ is an open, compact subset of the non-compact set $\mathbb{Q}_{p}$, and both of them are totally disconnected. In fact, all open balls are actually clopen! This is nothing like $\mathbb{Z} \subseteq \mathbb{R}$ where $\mathbb{Z}$ is non-compact and closed and $\mathbb{R}$ has lots of connected sets.

This has to do with the fact that the norm [[p-adic numbers --- math-177/notes/The p-adic numbers#_corollary _ $ mathbb{Q}_{p}$ is non-archimedean|is non-archimedean]]. 

##### _proposition:_ every element of a $p$-adic closed ball is a centre of the ball

For any $y \in \overline{B}(x, r) = \{ y \in \mathbb{Q}_{p} \mid \lvert y - x \rvert_{p} \leq r \}$, we have $\overline{B}(y, r) = \overline{B}(x, r)$.

###### _proof sketch:_

Suppose $z \in \overline{B}(y, r)$. Notice that $\lvert z - x \rvert_{p} \leq \max \{ \lvert z - y \rvert_{p}, \lvert y - x \rvert_{p} \} \leq r$. Thus, $\overline{B}(y, r) \subseteq \overline{B}(x, r)$ Since $x \in \overline{B}(y, r)$ we can use the same argument to show $\overline{B}(x, r) \subseteq \overline{B}(y, r)$.

---

A similar trick shows that any triangle is isosceles. This works in any non-archimedean field. That is,

##### _proposition:_ every triangle is isosceles

For any $x, y \in \mathbb{K}$ with $\lVert x \rVert > \lVert y \rVert$ where $\mathbb{K}$ is a non-archimedean field, $\lVert x + y \rVert = \lVert x \rVert$.

---

##### _lemma:_ open balls are clopen

For any $x \in \mathbb{Q}_{p}$, the open ball of radius $r$, centred at $x$
$$
B(x, r) = \{ y \in \mathbb{Q}_{p} \mid \lvert y - x \rvert _{p} < r \}
$$
is also closed.

###### _proof:_

Note of course that by the definition of a metric topology, this ball is open. We just need to show it is closed. We will show (equivalently) that [[Topology --- math-147/notes/Limit points and closed sets#_theorem _ closed sets are complements of open sets|its complement is open]]. 

[[Topology --- math-147/notes/Topologies#_proposition, definition _ checking openness by neighbourhood, neighbourhood|It suffices]] to give a disjoint ball $B(y, \rho) \subseteq \mathbb{Q}_{p} \setminus B(x, r)$ for each point $y$ in the complement of $B(x, r)$. Consider for each $y \in \mathbb{Q}_{p} \setminus B(x,r )$ the points $z \in \mathbb{Q}_{p}$ with $\lvert z - y \rvert_{p} < \lvert x - y \rvert_{p}$. Since $\lvert z - x \rvert_{p} = \lvert (z - y) - (y - x) \rvert_{p} > \lvert x - y \rvert_{p}$, we have $\lvert z - x \rvert_{p} > \lvert x - y \rvert_{p} \geq r$. Thus, choosing any $\rho < \lvert x - y \rvert_{p}$ gives $B(y, \rho) \subseteq \mathbb{Q}_{p} \setminus B(x, r)$.

---

##### _proposition:_ the $p$-adics are totally disconnected

$\mathbb{Z}_{p}$ and $\mathbb{Q}_{p}$ are totally disconnected — there are no connected subsets of either that are not singletons or the empty set.

###### _proof:_

Suppose $A \subseteq \mathbb{Q}_{p}$ has cardinality $\# A \geq 2$. Let $x, y \in A$ be distinct points. [[Topology --- math-147/notes/Connectedness and path-connectedness#_proposition _ conditions equivalent to connectedness|It suffices]] to show that $A$ has a non-trivial ([[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|relatively]]) clopen subset. For any $r < \lvert x - y \rvert_{p}$, the set $A \cap B(x, r)$ is an example.

---

##### _proposition:_ topological properties of $\mathbb{Z}_{p}$ in $\mathbb{Q}_{p}$

$\mathbb{Z}_{p} \subseteq \mathbb{Q}_{p}$ is an open compact subset.

###### _proof:_

First we show $\mathbb{Z}_{p}$ is open. Again, it suffices to show each integer is the centre of a metric ball contained in $\mathbb{Z}_{p}$. We claim this is the metric ball of radius $1$.

Recall the characterisation of $x \in \mathbb{Z}_{p}$ as exactly those $x \in \mathbb{Q}_{p}$ with $\lvert x \rvert_{p} \leq 1$. For each $x \in \mathbb{Z}_{p}$ consider the metric ball $B(x, 1)$. If $y \in B(x, 1)$, then $\lvert y - x \rvert_{p} < 1$. Thus,
$$
\lvert y \rvert _p = \lvert (y - x) + x \rvert_{p} \leq \max \{ \lvert y - x \rvert_{p}, \lvert x \rvert_{p}  \} \leq 1
$$
and $y \in \mathbb{Z}_{p}$.

We show compactness as sequential compactness — that every infinite subset has a limit point (or every sequence has a [[Analysis --- math-131/notes/Sequences and convergence#_theorem, definition _ subsequential limits|subsequential limit]]), [[Analysis --- math-131/attachments/homework/hw 5/hw 5.pdf|implying compactness]]. 

Write $\{ x_{n} \}_{n \in \mathbb{N}}$ for some arbitrary sequence of $x_{n} \in \mathbb{Z}_{p}$. Note that for each exponent $e$, the set of possible residue classes modulo each $p^i$ for $i$ at most $e$ is finite. As a result, there is a $p$-adic integer $u$, given by residue sequence $(u_{i})_{i \in \mathbb{N}}$, with infinitely many $x_{n}$ agreeing under each $\mathbb{Z}_{p} \twoheadrightarrow{} \mathbb{Z} / p^e / \mathbb{Z}$. Choose a subsequence $\{ x_{n_{k}} \}_{k \in \mathbb{N}}$ with $x_{n_{k}}$ agreeing with $u$ under $\mathbb{Z}_{p} \twoheadrightarrow{} \mathbb{Z} / p^k \mathbb{Z}$. Thus, $\lvert x_{n_{k}} - u \rvert_{p} \leq p^{-k} \to 0$ as $k \to \infty$. That is, $x_{n_{k}} \to u$.

---