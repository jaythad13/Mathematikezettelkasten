---
tags:
- a-lie/5
- lie
- alg
- diff-geo
---

Let $L$ be a Lie algebra

### The lower derived series

While the upper derived subalgebras and series
![[Lie algebras --- a-lie/notes/Solubility#_definition _ upper derived subalgebra, upper derived series|Solubility]]
give one way to get a chain of ideals smaller than $L'$. We can also get a different chain with the lower derived series

##### _definition:_ lower derived subalgebra, lower derived series

The $n$th lower derived subalgebra is $L^1 = L'$ for $n = 1$ and
$$
L^n = [L, L^n]
$$
otherwise.

The lower derived series of $L$ is the chain
$$
\dots \subset L^{n + 1} \subset L^n \subset \dots \subset L^1 \subset L.
$$

##### _lemma:_ lower derived subalgebras and quotients

For any ideal $I \subset L$, $(L / I)^{n} \cong (L^{n} + I)/I$

###### _proof sketch:_

Since $L^1 = L^{(1)}$ we have [[Lie algebras --- a-lie/notes/Solubility#_lemma _ upper derived subalgebras and quotients|already shown]] the case $n = 1$. Proceed by induction, using the case $n = 1$ to go from $n$ to $n + 1$.

### Nilpotency

Again, we say a Lie algebra is nilpotent if the lower derived series terminates

##### _definition:_ nilpotent

$L$ is nilpotent if $L^N = 0$ for some $N \in \mathbb{N}$.

An interesting result is that you don't really need to think about the centre of a Lie algebra to determine its nilpotency.

##### _proposition:_  $L / Z(L)$'s nilpotency determines $L$'s nilpotency

If $L / Z(L)$ is nilpotent, $L$ is nilpotent.

###### _proof:_

Suppose $L / Z(L)$ is nilpotent with $(L / Z(L))^N = 0$. By a lemma above, we can write $(L^N + Z(L)) / Z(L) = 0$. Thus, $L^N \subset Z(L)$. But $Z(L)' = 0$ so $L^{N + 1} \subset Z(L)' = 0$.