---
tags:
- math-135/1
- math-135/2
- anal
---

### $\mathbb{C}$ as a metric space

Since the norm $\lvert z \rvert$ of a complex number $z$ is positive definite and satisfies the triangle inequality, $\mathbb{C}$ is a [[Analysis --- rudin/notes/Metric spaces#_definition_ metric space, metric|metric space]] with the metric $d(z, w) = \lvert z - w \rvert$. In a very obvious way $\mathbb{C} \cong \mathbb{R}^2$ (as topological spaces)

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

### Regions

Most of the theorems in this course are about regions.

##### _definition:_ region

$\Omega \subset \mathbb{C}$ is a region if it is open and connected.

##### _definition:_ path-connected

$\Omega \subset \mathbb{C}$ is path-connected if for all $a, b \in \Omega$, there exists a continuous path $\gamma : [0, 1] \to \Omega$ with $\gamma(0) = a$ and $\gamma(1) = b$.

An exercise in [[Complex Analysis --- math-135/attachments/homework/hw 1/hw 1.pdf|the homework]] is

##### _proposition:_ path-connectedness and connectedness are equivalent on open sets

If $\Omega \subset \mathbb{C}$ is open, $\Omega$ is connected if and only if $\Omega$ is path-connected.

### Convergence

Things you should know are
- What a convergent sequence is
- That convergence happens component-wise — convergence is equivalent to convergence of real and imaginary parts
- What Cauchy sequences are
- What completeness is.

### Continuity

Things you should know are
- What continuity means on $\mathbb{C}$ (the same as on $\mathbb{R}^2$ — epsilon-delta/pre-image of open sets)
- That topological continuity is equivalent to epsilon-delta continuity is equivalent to sequential continuity (continuous functions preserve convergent sequences)

### Compactness

##### _definition:_ compactness

A subset $K \subset \mathbb{C}$ is compact if one of the following equivalent conditions is satisfied
1) Every open cover of $K$ admits a finite sub-cover.
2) Every sequence in $K$ has a convergent subsequence.
3) $K$ is closed and bounded.

Things you should know are
- the extreme value theorem — functions from a compact metric space to the reals attain a maximum (and also a minimum) (apply this to $\lvert f \rvert$ for complex valued functions)
- continuity on a compact set is equivalent to uniform continuity (see below)

##### _definition:_ uniform continuity

$f: A \to B$ is uniformly continuous on $A$ if for every $\varepsilon > 0$ there is a single $\delta > 0$ that gives $\lvert z - a \rvert < \delta \implies \lvert f(z) - f(a) \rvert < \varepsilon$ for all points $a \in A$.

It's also important that we know the distance lemma — that there is a positive distance between disjoint closed and compact sets
##### _proposition:_ distance lemma

There is some minimum distance $\rho$ such that $\lvert z_{K} - z_{F} \rvert > \rho$ for any $z_{K} \in K$ and $z_{F} \in F$ where $K$ is compact and $F$ is closed.

###### _proof sketch:_

Note that every point in the compact set is inside the open complement of the closed set. This means you can draw neighbourhoods around each of its points that don't intersect with the closed set. Then do the standard compactness trick.
