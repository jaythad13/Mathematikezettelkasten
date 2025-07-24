---
tags:
- alg
- math-171/18
---

### Maximal ideals

A natural thing to think about is whether an ideal is the largest proper ideal in a ring — does it include as many things as it can without just being the ring?

##### _example:_ maximal ideal of a field

Since any field $R$ has only $0$ and $R$ as ideals, $0$ is the maximal ideal of any field.

Obviously this might be more complicated for less easy rings.

##### _definition:_ maximal ideal

An ideal $I \subset R$ is a maximal ideal if $I \neq R$ and $I$ is maximal with respect to inclusion ($J \subset I$ for any ideal $J \neq R$, or equivalently, the only ideals that contain $I$ are $I$ and $R$)

##### _proposition:_ maximal ideals have fields as quotients

If $R$ is commutative and $I \subset R$ is an ideal, $I$ is maximal if and only if $R/I$ is a field.

###### _proof:_

$I$ is maximal if and only if the only ideals containing $I$ are $I$ and $R$. The [[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the fourth isomorphism theorem|fourth isomorphism theorem]] for rings tells us that this is equivalent to there being exactly two ideals in $R / I$. These ideals must be $0$ and $R / I$ since those are ideals in any ring. [[Abstract algebra --- math-171/notes/Ideals and quotients#_proposition _ when rings are fields|This is equivalent to the ring being a field]].

##### _example:_ maximal ideals with fields as quotients

1) $n\mathbb{Z}$ is maximal in $\mathbb{Z}$ if and only if $n$ is prime, since $\mathbb{Z} / n\mathbb{Z}$ is a field if and only if $n$ is prime. We could see this [[Abstract algebra --- math-171/notes/Cyclic groups and subgroups#_example _ what's the subgroup lattice of $ mathbb{Z} / 24 mathbb{Z}$?|when we drew the lattice of subgroups of cyclic groups]] and the "maximal subgroups" were the primes.

A much less easy example is the following:

2) Let $R$ be the ring of functions $f : [0, 1] \to \mathbb{R}$. Note that the homomorphism $\operatorname{ev}_{a} : f \mapsto f(a)$. We claim that $\ker \operatorname{ev}_{a}$ is a maximal ideal. We can see this by [[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the first isomorphism theorem|the first isomorphism theorem]] — since $\operatorname{ev}_{a}$ is surjective, $R/\ker \operatorname{ev}_{a}$ is a field and thus, $\ker \operatorname{ev}_{a}$ is maximal.

### Prime ideals and [[Abstract algebra --- math-171/notes/Integral domains|integral domains]]

It turns out that ideals have a lot to do with factorisation, as we will see, and thus, we want an analog of primeness. We know that if $p \mid ab$ for some prime $p$, then we must have $p \mid ab$, and similarly, we have prime ideals.

##### _definition:_ prime ideals

Let $R$ be a commutative ring. An ideal $P \subset R$ is a prime ideal if $P \neq R$ and for $a, b \in R$ with $ab \in P$, $a \in P$ or $b \in P$.

These are sort of a weaker version of maximal ideals — replace their relation to fields with integral domains. Specifically,

##### _proposition:_ prime ideals have integral domains as quotients

Let $R$ be a commutative ring with nontrivial identity. The ideal $P \subset R$ is prime if and only if $R/P$ is an integral domain.

###### _proof:_

Suppose $a, b \in R$ with $ab \in P$, or equivalently, $\overline{a}\overline{b} = \overline{ab} = \overline{0}$. Then note that $P$ being prime is equivalent to $a \in P$ or $b \in P$ which is equivalent to $\overline{a} = \overline{0}$ or $\overline{b} = \overline{0}$. Thus $R/P$ is an integral domain.

##### _corollary:_ every maximal ideal is prime

###### _proof:_

Suppose $I \subset R$ is a maximal ideal. Then $R/I$ is a field. Then $R / I$ is an integral domain (note this follows since [[Abstract algebra --- math-171/notes/Rings#_proposition _ every unit is not a zero divisor|units can't be zero divisors]]). Then $I$ is prime.

The converse isn't true.

##### _example:_ not every prime ideal is maximal

1) $(0)$ is prime since $ab \in (0)$ only if $a = 0$ or $b = 0$. However it's trivially non-maximal since $(0) \subset (2) \subsetneq \mathbb{Z}$, or for a sillier proof, because $\mathbb{Z} / (0) \cong \mathbb{Z}$ is obviously not a field.
2) In $\mathbb{Z}[x]$, the ideal $(x)$ is prime since $pq$ only has no constant terms if one of $p$ or $q$ has zero constant terms, or because $\mathbb{Z}[x] / (x) \cong \mathbb{Z}$ is an integral domain by the first isomorphism theorem. However, by the same isomorphism, $\mathbb{Z}[x]/(x)$ is not a field, and thus, $(x)$ is not maximal.