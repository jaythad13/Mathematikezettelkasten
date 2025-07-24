---
tags:
- math-131/4
- anal
---

Central to analysis is the notion of the size of a set. In order to compare sets, we try to put them in bijection with sets whose size is obvious. 

##### _definition:_ cardinality

We say that two sets $A$ and $B$ have the same cardinality $\lvert A \rvert = \lvert B \rvert$ if there exists a bijection $f$ between them.

In order to get an even more specific handle on the size of sets, we can compare them to sets whose size is obvious — the natural numbers $\mathbb{N} = \{ 1, 2, 3, \dots \}$, and $\mathbb{N}_{n} = \{ 1, \dots, n \}$.

##### _definition:_ countability, finiteness

We say a set $A$ is countable if it is in bijection with $\mathbb{N}$.

We say $A$ is finite, with cardinality $n$ if it is in bijection with $\mathbb{N}_{n}$.

##### _theorem:_ a variant of Cantor-Schröder-Bernstein?

If $f : A \to \mathbb{N}$ is injective, and $A$ is not finite, then there exists a bijection $g : A \to \mathbb{N}$.

###### _proof sketch:_

Use [[Analysis --- math-131/notes/Before the real numbers#_definition _ the Peano axioms|the well ordering principle]] to keep picking the $n$th smallest value of $f$, $f(a_{n})$. Then set $f(a_{n}) = n$. By the pigeonhole principle, you never stop.

This theorem allows us to prove that a lot of sets are countable without all the work of creating a bijection — we just need to create an injection.

##### _lemma:_ finite products of countable sets are countable

If $A_{1}, \dots, A_{n}$ are countable, then
$$
A_{1} \times \dots \times A_{n} = \{ (x_{1}, \dots, x_{n}) \mid x_{i} \in A_{i} \}
$$
is countable.

###### _proof sketch:_

We can use the [[Superdiscrete --- math-55A/notes/Euclid's algorithm and primes|primes and unique factorisation]] as an indicator. Let $p_{1}, \dots, p_{n}$ be distinct primes. Since each $A_{i}$ is countable, we have bijections $f_{i} : A_{i} \to \mathbb{N}$. Then consider 
$$
f : (x_{1}, \dots, x_{n}) \mapsto p_{1}^{f_{1}(x_{1})} \cdots p_{n}^{f_{n}(x_{n})}. 
$$
$f$ is clearly injective, and thus, $A_{1} \times \dots \times A_{n}$ is countable.

##### _lemma:_ countable unions of countable sets are countable

Let $A_{1}, A_{2}, \dots$ be countably many countable sets. Then $\bigcup_{i = 0}^\infty A_{i}$ is countable.

###### _proof:_

We will first show this for the disjoint union of $A_{1}, A_{2}, \dots,$. Note that it suffices to show it in this case. If we have an injection $f : \bigsqcup_{i = 0}^\infty A_{i} \cdots \to \mathbb{N}$, the (injective) inclusion $i : \bigcup_{i = 0}^\infty A_{i} \to \bigsqcup_{i = 0}^\infty A_{i}$ gives us an injection $f \circ i : \bigcup_{i = 0}^\infty A_{i} \to \mathbb{N}$.

Since each $A_{i}$ is countable, we have bijections $f_{i} : A_{i} \to \mathbb{N}$. Let $p_{1}, p_{2}, \dots$ be distinct primes. Then consider
$$
f : x \mapsto p_{i}^{f_{i}(x)}
$$
for $x \in A_{i}$. By unique factorisation (and the injectivity of $f_{i}$ and the disjointedness of the $A_{i}$) this is injective.

##### _corollary:_ $\mathbb{Z}$ is countable

###### _proof sketch:_

$\mathbb{Z}$ can be put in bijection with $\mathbb{N} \sqcup \mathbb{N} \sqcup \{ 0 \}$.

##### _corollary:_ $\mathbb{Q}$ is countable

###### _proof sketch:_

$\mathbb{Q}$ can be put in bijection with a subset of $\mathbb{Z} \times \mathbb{N}$. Thus, precomposing the inclusion with any bijection $\mathbb{Z} \times \mathbb{N} \to \mathbb{N}$ gives us an injection $\mathbb{Q} \to \mathbb{N}$. Choose your favourite proof that the rationals are infinite.

So are all sets countable?

### Uncountable sets

Gloriously, [[Analysis --- math-131/notes/The reals|the reals]] are the first example of an uncountable set.

##### _theorem:_ Cantor's diagonalisation theorem

The interval $I = \{ x \mid 0 < x < 1 \}$ is uncountable.

###### _proof:_

Suppose by way of contradiction that $I$ is countable. Then we could write the reals as a sequence $x_{n} = 0.a_{1, i} a_{2, i} \cdots$. Then consider $x = 0.a_{1} a_{2} \cdots$ where
$$
a_{i} = \begin{cases}
1 & a_{i, i} \neq 1 \\
0 & a_{ii} = 1.
\end{cases}
$$
$x \neq x_{i}$ for any $i \in \mathbb{N}$. Thus, we have a contradiction.

Note as a corollary that $\mathbb{R}$ is uncountable since any bijection to $\mathbb{N}$ would involve an injection $[0, 1] \to \mathbb{N}$.

##### _corollary:_ irrationals are uncountable

###### _proof sketch:_

Else the rationals union the irrationals would be countable.