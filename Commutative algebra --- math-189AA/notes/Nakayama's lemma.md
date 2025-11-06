---
tags:
- comm-alg
- math-189AA/21
---

Let $A$ be a ring.

Nakayama's lemma tells us how scaling by certain elements behaves on 

##### _lemma:_ Nakayama's lemma (version 1)

Suppose $M$ is a [[Commutative algebra --- math-189AA/notes/Finite generation and finite presentation#_definition _ finitely generated|finitely generated]] $A$-module and $\mathfrak{i} \subseteq A$ is contained in the [[Commutative algebra --- math-189AA/notes/Jacobson radical#_definition _ Jacobson radical|Jacobson radical]] of $A$. Then if $\mathfrak{i} M = M$, $M = 0$.

---

##### _lemma_

### Consequences...

Nakayama's lemma is very useful!

For one, it tells us that tensor products behave relatively nicely over local rings.

##### _proposition:_ tensoring over local rings doesn't kill non-zero modules

Let $A, \mathfrak{m}, k$ be a [[Commutative algebra --- math-189AA/notes/Local rings#_definition _ local rings|local ring]]. Let $M, N$ be finitely generated $A$-modules. Then if $M \otimes_{A} N = 0$, either $M = 0$ or $N = 0$.

###### _proof:_

Note that $k$ is an $A$-algebra. Then, using [[Algebraic geometry --- rising-sea/notes/Tensor products, categorically#_proposition _ some nice isomorphisms of tensor products|tensor product identities]] we have
$$
\begin{align}
M \otimes_{A} N \otimes_{k} k & \cong (M \otimes_{A} k) \otimes_{k} (N \otimes_{A} k) \\
 & \cong (M \otimes_{A} A / \mathfrak{m}) \otimes_{k} (N \otimes_{A} / A \mathfrak{m}) \\
 & \cong M / \mathfrak{m} M \otimes_{k} N / \mathfrak{m} N \\
 & \cong k^{\oplus m} \otimes_{k} k^{\oplus n} \\
 & \cong k^{\oplus mn}
\end{align}
$$
where we pick $m$ and $n$ happen to be the minimum number of generators for $M$ and $N$ respectively (over local rings, the minimum number of generators of $M / \mathfrak{m} M$ and $M$ are the same). $k^{\oplus mn}$ is zero if and only if one of $m$ or $n$ is $0$. Then $\mathfrak{m} M = M$ or $\mathfrak{m} N = N$. But then, by Nakayama's lemma $M$ or $N$ is zero.

---