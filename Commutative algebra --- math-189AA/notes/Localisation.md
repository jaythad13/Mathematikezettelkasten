---
tags:
- math-189AA/4
- comm-alg
---

Localisation solves the problem of making a ring [[Commutative algebra --- math-189AA/notes/Local rings#_definition _ local rings|local]], and does other things as well. It works by turning everything outside a maximal ideal into a unit.

##### _example:_ making $\mathbb{Z}$ local

We turn the $\mathbb{Z}$ into a local ring with maximal ideal by turning everything not in $(0)$ into a unit. This gives us the field $\mathbb{Q}$.

### What is localisation?

##### _definition:_ multiplicative subsets

A multiplicative subset of a ring $A$ is a subset $S$ such that $1 \in S$ and for any $s_{1}, s_{2} \in S$, we have $s_{1} s_{2} \in S$

##### _definition:_ localisation of a ring, localisations at a prime, fraction field

The localisation of a ring $A$ away from a multiplicative subset $S$ is the ring $S^{-1} A$ with elements of the form $a / s$ with $a \in A, s \in S$ under the equivalence relation $a_{1} / s_{1} = a_{2} / s_{2}$ if and only if $s(s_{2} a_{1} - a_{2} s_{2}) = 0$ for some $s \in S$. Addition is defined by
$$
\frac{a_{1}}{s_{1}} + \frac{a_{2}}{s_{2}} = \frac{s_{2} a_{1} + s_{1} a_{2}}{s_{1} s_{2}}
$$
and multiplication is defined by
$$
\frac{a_{1}}{s_{1}} \times \frac{a_{2}}{s_{2}} = \frac{a_{1} a_{2}}{s_{1} s_{2}}.
$$
Consequently zero is (the equivalence class of) $0 / 1$ and the multiplicative identity is (the equivalence class of) $1 / 1$

When $S = \{ 1, f, f^{2}, \dots \}$ for an element $f \in A$, we denote $S^{-1} A$ by $A_{f}$.

When $S = A \setminus \mathfrak p$ for a [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|prime ideal]] $\mathfrak p$, we denote $S^{-1} A$ by $A_{\mathfrak p}$ and call it the localisation at the prime. Note that then if the ideal $(f)$ is prime, $(f)^{-1} A = A_{f} \neq A_{(f)}$.

Finally if $A$ is an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]] and $S = A \setminus \{ 0 \}$ we call $S^{-1} A$ the fraction field of $A$ and denote it by $K(A)$.

Note that there is a canonical ring map $A \to S^{-1} A$ by $a \mapsto a / 1$, and if $0 \in S$, $S^{-1} A$ is the trivial ring. When $S$ doesn't contain zero divisors, the map is injective. In particular $A \to K(A)$ is injective. However, this is not true otherwise.

##### _proposition:_ injectivity of the localisation map

For a multiplicative subset $S$ of a ring $A$, the canonical map $A \to S^{-1} A$ by $a \mapsto a / 1$ is injective if and only if $S$ contains no [[Abstract algebra --- math-171/notes/Rings#_definition _ zero divisor|zero divisor]].

###### _proof:_

The condition for $a / 1 = 0$ in $S^{-1} A$ is that $a / 1 = 0 / 1$ and thus, $s(1 \times a - 0 \times 1) = sa$ is zero in $A$.

Suppose $S$ contains a zero divisor $s$. Then $as = 0$ for some non-zero $a \in A$. Thus, $a / 1 = 0 / 1$ since $s a = 0$.

Suppose $S$ contains no zero divisors. Then for any non-zero $a \in A$, $a / 1 \neq 0 / 1$ since that can only happen if $sa = 0$ for some $s \in S$ which requires a zero divisor in $S$.

Localisations of $A$ can be characterised in terms of a universal property in the category of $A$-algebras (rings $B$ with a ring homomorphism $A \to B$).

##### _example:_ multiplicative subsets to localise at

1) The set of [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_definition _ nilpotents|nilpotents]] unioned with $1$.
2) The set of non-[[Abstract algebra --- math-171/notes/Rings#_definition _ zero divisor|zero-divisors]].
3) The set of [[Abstract algebra --- math-171/notes/Rings#_definition _ unit|units]].
4) $\mathbb{Z}_{(0)} = \mathbb{Q}$.
5) $\mathbb{Z}_{(3)} =$ ?