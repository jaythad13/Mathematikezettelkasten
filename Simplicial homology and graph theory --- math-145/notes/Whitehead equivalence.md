---
tags:
- math-145/11
- math-145/13
- alg-top
---

We want a notion of isomorphism for [[Simplicial homology and graph theory --- math-145/notes/Simplicial complexes#_definition _ simplicial complex|simplicial complexes]] that identifies two complexes that are obviously the same — with vertices just relabelled, but also identifies other things that are not so obviously the same. Roughly, we want something that is a homotopy invariant and not much weaker.

This is given by elementary modifications and the equivalence relation they generate.

### Elementary modifications and Whitehead equivalence

##### _definition:_ elementary collapse, elementary expansion

Let $X$ be a simplicial complex, and $\sigma \in X$ a simplex. If $\sigma$ has exactly one [[Simplicial homology and graph theory --- math-145/notes/Simplicial complexes#_definition _ face, coface|coface]] $\tau$, then $Y = X \setminus \{ \sigma, \tau \}$ is a simplicial complex.

$Y$ is an elementary collapse of $X$, denoted $X \searrow Y$.

Also, $X$ is an elementary expansion of $Y$ denoted $Y \nearrow X$.

This notion of equivalence essentially allows you to collapse any homotopically trivial simplices into the non-trivial parts of $X$.

##### _definition:_ Whitehead equivalence

Whitehead equivalence is the smallest equivalence relation that considers any $X, Y$ with $X \searrow Y$ to be equivalent.

That is, $X, Y$ are Whitehead equivalent, denoted $X \simeq Y$ if there is a sequence of simplicial complexes, $X_{0}, \dots, X_{n}$ such that $X_{0} = X$, $X_{n} = Y$ and, for each $i$, we have either $X_{i} \searrow X_{i + 1}$ or $X_{i} \nearrow X_{i + 1}$.

### Simple equivalences

There are some useful equivalences to have at hand that we list as lemmas with sketches of a proof.

##### _lemma:_ the edge splitting lemma

Let $X$ be a simplicial complex with an edge $ab$ that has no proper cofaces. Let $Y = {X \cup \{ am, mb \} \setminus \{ ab \}}$. Then $X \simeq Y$.

###### _proof sketch:_

$$
X \nearrow X \cup \{ m, am \} \nearrow X \cup \{ m, am, bm, abm \} \searrow X \cup \{ am, bm \} \setminus \{ ab \}.
$$

Often it's of interest that we can get rid of a space.

##### _definition:_ collapsible

A simplicial complex $X$ is collapsible if it is Whitehead equivalent to the one point space $\{ * \}$.

##### _proposition:_ every cone is collapsible

If $X$ is a finite simplicial complex, and $CX$ is [[Simplicial homology and graph theory --- math-145/notes/Simplicial complexes#_example _ cones|its cone]], then $CX$ is collapsible.

###### _proof:_

Let $\sigma$ be a maximal simplex of $X$. Then $\sigma$ has exactly one coface in $CX$ — $\sigma \cup \{ * \}$. Removing this leaves us with a cone $CX \setminus \{ \sigma, \sigma \cup \{ * \} \}$. By induction, every simplex in $X$ is eventually removed, leaving just the point $\{ * \}$.

### Whitehead invariants

To tell that two simplicial complexes are equivalent, we construct an equivalence. However to tell them apart, we must use invariants. These are functions on simplicial complexes such that if $X \simeq Y$, the functions are the same on $X$ and $Y$.

##### _definition:_ Betti zero of a simplicial complex

The zeroth Betti number of a simplicial complex is $\mathrm{b}_{0}(X)$, the number of connected components of the graph given by its $1$-[[Simplicial homology and graph theory --- math-145/notes/Simplicial complexes#_definition _ $k$-skeleton|skeleton]].

##### _proposition:_ number of connected components is Whitehead invariant

For simplicial complexes $X \searrow Y$, 

##### _definition:_ unsigned Euler characteristic

The unsigned Euler characteristic of a simplicial complex $X$ is the parity of the number of simplices —
$$
\sum_{k = 0}^{\dim X} \dim \mathrm{C}_{k}(X, \mathbb{F}) \pmod 2
$$

###### _proof sketch:_

For $X \searrow Y$ we remove two faces.

##### _definition:_ the Euler characteristic

The Euler characteristic of a simplicial complex $X$ is the alternating sum of the size of the $k$-[[Simplicial homology and graph theory --- math-145/notes/Simplicial complexes#_definition _ $k$-skeleton|skeletons]].
$$
\chi(X) = \sum_{k = 0}^{\dim X} (-1)^k \dim C_{k}(X, \mathbb{F}).
$$

###### _proof sketch:_

For $X \searrow Y$, we remove faces of adjacent dimension, and thus, opposite sign.

### Whitehead invariance of homology

The most significant Whitehead invariant is that of homology since it gives us invariance of $0$th Betti number [[Simplicial homology and graph theory --- math-145/notes/Euler's formula#_theorem _ Euler's formula for simplicial complexes|and Euler characteristic]] all in one,

##### _theorem:_ simplicial homology is Whitehead invariant

Suppose $X, Y$ are Whitehead equivalent simplicial complexes. Then there is an isomorphism of homology groups $\mathrm{H}_{k}(X, \mathbb{F}) \cong \mathrm{H}_{k}(Y, \mathbb{F})$ for each $k$.

###### _proof:_

It suffices to show the theorem in the case that $X \searrow Y$. Specifically, suppose $Y = X - \{ \sigma, \tau \}$ where $\sigma = \{ a_{0}, a_{1}, \dots, a_{n} \}$ and $\tau = \{ a_{1}, \dots, a_{n} \}$. Let $\overline{\sigma} = [a_{0}, a_{1}, \dots, a_{n}]$ and $\overline{\tau} = [a_{1}, \dots, a_{n}]$ are the corresponding [[Simplicial homology and graph theory --- math-145/notes/Simplicial homology#_definition _ chains|chains]].

We claim that inclusion $I : \mathrm{C}_{*}(Y) \to \mathrm{C}_{*}(X)$ is a [[Simplicial homology and graph theory --- math-145/notes/A little homological algebra#_definition _ chain map|chain map]] since the boundary of a $k$-simplex is the same in $X$ and $Y$. To define a chain map in the opposite direction, there is exactly one sensible choice —
$$
P(\alpha) = \begin{cases}
\alpha & \alpha \in \mathrm{C}_{*}(Y) \\
0 & \alpha = \overline{\sigma} \\
\overline{\tau} - \partial \bar{\sigma} & \alpha = \overline{\tau}.
\end{cases}
$$
By dividing into the same cases as above, it's clear that $P$ does commute with the [[Simplicial homology and graph theory --- math-145/notes/Simplicial homology#_definition _ boundary map|boundary map]].

$PI$ is the identity itself since $P$ sends any $\alpha \in \operatorname{img} I$ to itself. We want to define a [[Simplicial homology and graph theory --- math-145/notes/A little homological algebra#_definition _ chain homotopy|chain homotopy]] $K : $
