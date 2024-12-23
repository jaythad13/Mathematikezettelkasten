---
tags:
- a-lie/5
- alg
- diff-geo
- lie
---

For this note, $L$ is a Lie algebra.

### The upper derived series

Recall the derived subalgebra
![[Lie algebras --- a-lie/notes/Subalgebras, ideals, and quotients#_definition _ commutator, derived subalgebra|Subalgebras, ideals, and quotients]]

One simple example of this is the following.

##### _lemma:_ abelian quotients

If $L$ ha an ideal $I \subset L$, then $L / I$ is [[Lie algebras --- a-lie/notes/Lie algebras#_definition _ abelian Lie algebra|abelian]] if and only if $L' \subset I$.

###### _proof:_

Suppose $L' \subset I$. Then any $[x, y] \in I$ and thus, $[x + I ,y + I] = [x, y] + I$ is zero. That is, $L / I$ is abelian.

Suppose $L / I$ is abelian. Then any $[x, y] + I = [x + I, y + I] = 0$, so $[x, y] \in I$. Since $I$ is closed under taking the span of all $[x, y]$, we have $L' \subset I$.

A natural extension of the derived subalgebra is to just keep taking brackets. We define the $n$th upper derived subalgebra inductively —

##### _definition:_ upper derived subalgebra, upper derived series

The $n$th upper derived subalgebra is $L^{(1)} = L'$ for $n = 1$ and
$$
L^{(n)} = [L^{(n - 1)}, L^{(n - 1)}]
$$
otherwise.

The upper derived series of $L$ is the chain
$$
\dots \subset L^{(n + 1)} \subset L^{(n)} \subset \dots \subset L^{(1)} \subset L
$$

##### _lemma:_ upper derived subalgebras and quotients

For any ideal $I \subset L$, $(L / I)^{(n)} \cong (L^{(n)} + I)/I$.

###### _proof sketch:_

For $n = 1$ we want to show $(L / I)' \cong (L' + I) / I$. By [[Lie algebras --- a-lie/notes/Lie algebra isomorphisms#_theorem _ the second Lie algebra isomorphism theorem|the second isomorphism theorem]], the right hand side is $L' / L' \cap I$.

Consider the map $\varphi : L' / L' \cap I \to (L / I)'$ given by $[x, y] + L' \cap I \mapsto [x, y] + I$. This is well-defined — if $[x_{1}, y_{1}] + L' \cap I = [x_{2}, y_{2}] + L' \cap I$, then $[x_{1}, y_{1}] - [x_{2}, y_{2}] \in L' \cap I \subset I$ so $[x_{1}, y_{1}] + I = [x_{2}, y_{2}] + I$. Further, it is injective for the same reason — $L' \cap I \subset I$. Finally, it is surjective by our construction — clearly it is surjective on the spanning list of brackets $[x, y]$. Essentially, for any $i_{1}, i_{2} \in I$, we have 
$$
[x + i_{1}, y + i_{2}] = [x, y] + [i_{1}, i_{2}] + [i_{1}, y] + [x, i_{2}]
$$
so we can rewrite an element of $(L / I)'$ as an element of $L' / L' \cap I$ and vice versa.

Proceed by induction, using the case $n = 1$ to go from $n$ to $n + 1$.

### Solubility

In analogy with groups, we say that a Lie algebra is soluble if the upper derived series terminates.

##### _definition:_ soluble

$L$ is soluble if there is some $N \in \mathbb{N}$ such that $L^{(N)} = 0$.

"Solvable" is an unfortunate Americanism.

##### _example:_ $\mathfrak{gl}_{2}(F)$ (and $\mathfrak{sl}_{2}(F)$) is not soluble 

[[Lie algebras --- a-lie/notes/Subalgebras, ideals, and quotients#_example _ $ mathfrak{sl}_{2}( mathbb{C}) = mathfrak{gl}_{2}( mathbb{C})'$|We know]] (in the complex case at least) that $\mathfrak{gl}_{2}(F)$ has derived subalgebra $\mathfrak{sl}_{2}(F)$. By a dimension argument, we can see that $\mathfrak{sl}_{2}(F)$ is its own derived subalgebra. Thus, $\mathfrak{gl}_{2}(F)^{(n)}$ is never $0$.

##### _example:_ $\mathfrak{b}_{2}(F)$ is soluble

Since the regular Lie bracket kills the trace of a matrix, any pair of upper-triangular matrices $\mathfrak{b}_{2}(F)$ has a bracket that is strictly upper-triangular. It's not difficult to see that the one entry in the top right corner can be anything — that is, $\mathfrak{b}_{2}(F)' = \mathfrak{n}_{2}(F)$.

The product of two strictly upper-triangular $2$-by-$2$ matrices is just the zero matrix so $\mathfrak{n}_{2}(F) = 0$. Thus, $\mathfrak{b}_{2}(F)$ is soluble.

We can rewrite the condition to be a soluble Lie algebra to look even more like the corresponding definition for groups.

##### _propositions:_ solubility in terms of quotients

$L$ is soluble if and only if there exists a chain of ideals 
$$
0 = I_{N} \subset \dots \subset I_{1} \subset I_{0} = L
$$
such that $I_{n - 1} / I_n$ is abelian for all $n \in \mathbb{N}_{N}$.

###### _proof sketch:_

To show the forward direction, consider the chain
$$
0 = L^{(N)} \subset \dots \subset L^{(1)} \subset L^{(0)} = L.
$$
Commutativity follows from our first lemma on abelian quotients.

To show the reverse direction note that the chain of ideals must contain the upper derived series — since $I_{n - 1} / I_{n}$ is abelian, $I_{n}' \subset I_{n} \subset I_{n - 1}$ and starting inductively from $L' \subset I_{1}$, we get $L^{(n)} \subset I_{n}$.

Some more algebraic properties of solubility hold.

##### _proposition:_ subalgebras of soluble Lie algebras are soluble

If $L$ is soluble, then any subalgebra $K \subset L$ is soluble.

###### _proof sketch:_

$K' \subset L'$, and so $K^{(N)} \subset L^{(N)} = 0$ by induction.

##### _proposition:_ soluble ideal and quotient implies soluble algebra

If $L$ has a soluble ideal $I \subset L$ with soluble quotient $L / I$, $L$ is soluble.

###### _proof:_

To prove this we need a lemma about upper derived subalgebras and quotients.

![[#_lemma _ upper derived subalgebras and quotients]]

Consider $M$ such that $I^{(M)} = 0$ and $N$ such that $(L / I)^{(N)} = 0$. Then since $(L^{(N)} + I) / I = 0$, $L^{(N)} + I \subset I$ — that is, $L^{(N)} \subset I$. Thus, $L^{(M + N)} \subset I^{(M)} = 0$.

##### _proposition:_ sum of soluble ideals is soluble

If $I, J \subset L$ are soluble, then $I + J$ is soluble.

###### _proof:_

Let $M, N \in \mathbb{N}$ give $I^{(M)} = J^{(N)} = 0$. Consider $((I + J) / J)^{(M)}$. By the second isomorphism theorem this is just $(I / I \cap J)^{(M)}$, and by same lemma as above, this is $(I^{(M)} + I \cap J) / I \cap J$. Since $I^{(M)} = 0$, we have
$$
\left( \frac{I + J}{J} \right)^{(M)} \cong \left( \frac{I}{I \cap J} \right)^{(M)} \cong \frac{I^{(M)} + I \cap J}{I \cap J} \cong \frac{I \cap J}{I \cap J} \cong 0.
$$

That is, $(I + J) / J$ is soluble. Since $J$ is soluble and $(I + J) / J$ is soluble, $I + J$ must be soluble.