---
tags:
- math-135/1
- anal
---

### $\mathbb{C}$ as a metric space

Since the norm $\lvert z \rvert$ of a complex number $z$ is positive definite and satisfies the triangle inequality, $\mathbb{C}$ is a [[Analysis --- rudin/notes/Metric spaces#_definition_ metric space, metric|metric space]] with the metric $d(z, w) = \lvert z - w \rvert$.

### Open and closed sets

Central to the topology of $\mathbb{C}$ is the notion of an $r$-neighbourhood of a point $z \in \mathbb{C}$. We use several different types of neighbourhoods

##### _definition:_ neighbourhoods

1) The $r$-neighbourhood of $z$, $N_{r}(z)$ is the set of all $w \in \mathbb{C}$ with $d(z, w) < r$.
2) $\overline{N_{r}(z)}$ is the closure of $N_{r}(z)$ which is just the set of all $w \in \mathbb{C}$ with $d(z, w) \le r$.
3) The punctured $r$-neighbourhood of $z$, $N^*_{r}(z)$, is $N_{r}(z) \setminus \{ z \}$. 

We can now define open and closed sets and all related notions.

##### _definition:_ open set

$U \subset \mathbb{C}$ is open in $\mathbb{C}$ if every $z \in U$ is an interior point of $U$. That is, for every $z \in U$, there is some $r > 0$ such that $N_{r}(z) \subset \mathbb{C}$.

##### _definition:_ closed set

$V \subset \mathbb{C}$ is closed if its complement is open, or equivalently, if $V$ contains all its limit points. That is, if every $N^*_{r}(z) \cap V$ is always non-empty, then $z$ is in $V$.

##### _definition:_ interior

The interior of $U \subset \mathbb{C}$ is $U^\circ$, the set of all interior points of $U$.

##### _definition:_ closure

The interior of $V \subset C$ is $\overline{V}$, the union of $V$ and the set of all limit points of $V$.

##### _definition:_ bounded, diameter

$U \subset \mathbb{C}$ is bounded if there is some $M$ such that $\lvert z \rvert < M$ for all $z \in U$.

If $U$ is bounded, we say $\sup \{ \lvert z - w \rvert : z, w \in \mathbb{C} \}$ is its diameter.

### Compactness

##### _definition:_ compactness

A subset $K \subset \mathbb{C}$ is compact if one of the following equivalent conditions is satisfied
1) Every open cover of $K$ admits a finite sub-cover.
2) Every sequence in $K$ has a convergent subsequence.
3) $K$ is closed and bounded.