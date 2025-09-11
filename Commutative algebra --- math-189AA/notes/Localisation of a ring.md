---
tags:
- math-189AA/4
- math-189AA/5
- comm-alg
---

Localisation solves the problem of making a ring [[Commutative algebra --- math-189AA/notes/Local rings#_definition _ local rings|local]], and does other things as well. In the typical case of localising at a prime, it works by turning everything outside the prime into a unit, and thus, making the prime the unique maximal ideal.

##### _example:_ making $\mathbb{Z}$ local

We turn the $\mathbb{Z}$ into a local ring with maximal ideal by turning everything not in $(0)$ into a unit. This gives us the field $\mathbb{Q}$.

---

### What is localisation?

##### _definition:_ multiplicative subsets

A multiplicative subset of a ring $A$ is a subset $S$ such that $1 \in S$ and for any $s_{1}, s_{2} \in S$, we have $s_{1} s_{2} \in S$.

---

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

If $A$ is any ring and $S$ is the set of non-zero-divisors, then $S^{-1} A$ is called the total quotient ring of $A$ (since $S$ is the maximal multiplicative set such that $S^{-1} A \neq 0$). This is denoted by $Q(A)$. If $A$ is an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]] then $Q(A)$ is a field called the fraction field of $A$.

---

Note that there is a canonical ring map $A \to S^{-1} A$ by $a \mapsto a / 1$, and if $0 \in S$, $S^{-1} A$ is the trivial ring. When $S$ doesn't contain zero divisors, the map is injective. In particular $A \to Q(A)$ is injective. However, this is not true otherwise.

##### _proposition:_ injectivity of the localisation map

For a multiplicative subset $S$ of a ring $A$, the canonical map $A \to S^{-1} A$ by $a \mapsto a / 1$ is injective if and only if $S$ contains no [[Abstract algebra --- math-171/notes/Rings#_definition _ zero divisor|zero divisor]].

###### _proof:_

The condition for $a / 1 = 0$ in $S^{-1} A$ is that $a / 1 = 0 / 1$ and thus, $s(1 \times a - 0 \times 1) = sa$ is zero in $A$.

Suppose $S$ contains a zero divisor $s$. Then $as = 0$ for some non-zero $a \in A$. Thus, $a / 1 = 0 / 1$ since $s a = 0$.

Suppose $S$ contains no zero divisors. Then for any non-zero $a \in A$, $a / 1 \neq 0 / 1$ since that can only happen if $sa = 0$ for some $s \in S$ which requires a zero divisor in $S$.

---

Localisations can be characterised in terms of a [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?|universal property]] in the category of $A$-algebras (rings $B$ with a ring homomorphism $A \to B$). 

![[Algebraic geometry --- rising-sea/notes/Localisation, categorically#_proposition _ the universal property of localisation|Localisation, categorically]]

##### _example:_ multiplicative subsets to localise at

1) The set of [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_definition _ nilpotents|nilpotents]] unioned with $1$.
2) The set of non-[[Abstract algebra --- math-171/notes/Rings#_definition _ zero divisor|zero-divisors]].
3) The set of [[Abstract algebra --- math-171/notes/Rings#_definition _ unit|units]].
4) $\mathbb{Z}_{(0)} = \mathbb{Q}$, or equivalently $K(\mathbb{Z}) = Q(\mathbb{Z}) = \mathbb{Q}$.
5) $\mathbb{Z}_{(3)}$ is the set of rationals without any multiples of $3$ in the denominator.
6) $\mathbb{F}[x]_{(x)}$ is rational functions with no pole at $0$.

---

Note that localisation doesn't just commute with direct sums ([[Algebraic geometry --- rising-sea/notes/Localisation, categorically#_proposition _ localisation commutes with finite products and all coproducts|as proved by universal property]]). It also commutes with quotients and intersections.

##### _proposition:_ localisation commutes with quotients

For $S$ a multiplicative subset of $A$, and $\mathfrak{i} \subseteq A$ an ideal, we have
$$
S^{-1}(A / \mathfrak{i}) \cong S^{-1} A / S^{-1} \mathfrak{i}.
$$

---

##### _proposition:_ localisation commutes with finite intersections

For $S$ a multiplicative subset of $A$ and $\mathfrak{i}, \mathfrak{j} \subseteq A$ ideals, we have
$$
S^{-1}(\mathfrak{i} \cap \mathfrak{j}) = S^{-1} \mathfrak{i} \cap S^{-1} \mathfrak{j}.
$$

---

We don't prove these results here, but rather as a more general result about localisation of $A$-modules.

### Ideals of the localisation 

We want to understand the ideal structure of $S^{-1} A$.

##### _proposition:_ ideals of the localisation are extended

All ideals $\mathfrak{j} \subseteq S^{-1} A$ is [[Commutative algebra --- math-189AA/notes/Contraction and extension#_definition _ extension|extended]] from the natural map $A \to S^{-1} A$.

###### _proof:_

It's a simple property of extension that $\mathfrak{j}^\text{ce} \subseteq \mathfrak{j}$. We seek to prove the opposite inclusion. Suppose $a / s \in \mathfrak{j}$. Then $a / 1 \in \mathfrak{j}$ which has $a \mapsto a / 1$. Thus, $a /s \in (S^{-1} A) \mathfrak{j}^\text{c} = \mathfrak{j}^\text{ce}$.

---

##### _proposition:_ primes of the localisation are primes that don't meet $S$

Primes ideals $\mathfrak{q} \subseteq S^{-1} A$ are in bijection with primes in $A$ that have no intersection with $S$. Equivalently, $\mathfrak{q} \subseteq \mathfrak{p}$ for $S = A \setminus \mathfrak{p}$.

---

We can understand the ideals of $S^{-1} A$ better with [[Commutative algebra --- math-189AA/notes/Annihilators#_definition _ annihilator|annihilators]]. If $\operatorname{Ann}_{A} \mathfrak{i}$ is not a subset of $A \setminus S$, then $S^{-1}\mathfrak{i}$ is annihilated by some unit in $S^{-1} A$, and thus, is just $0$.

##### _example:_ $(\mathbb{Z} / (6))_{(2)}$



### Algebro-geometric intuition for localisation

Localisation corresponds to examining a geometric object locally. However, to understand what this means requires understanding localisation.

How can you think of the solutions to an equation? Consider $y^{2} = x^{3} + x^{2}$ over $\mathbb{C}$. An analyst might imagine this as a curve of points $(x, y) \in \mathbb{C}^{2}$ parameterised in neighbourhoods by some parameter $t \in \mathbb{R}$. We want to think of this algebraically.

##### _example:_ $\mathbb{C}[x, y] / (y^{2} - x^{3} - x^{2})$

Call the ring $A$. The maximal ideals of $A$ are just those of $\mathbb{C}[x, y]$ that contain $(y^{2} - x^{3} - x^{2})$. These, in turn are just those ideals $(x - a, y - b)$ so that $b^{2} - a^{3} = 0$ (by Hilbert's Nullstellensatz). Thus, the maximal ideals correspond to points of the curve. The ring itself then corresponds to functions with values at point $(a, b) \in \mathbb{C}^{2}$ corresponding to values modulo $\mathfrak{m} = (x - a, y - b)$.

Now it's clear that the localisation away from a maximal ideal $A_{\mathfrak{m}}$ is just allowing denominators such that they don't have a pole at that point. Thus, $A_{\mathfrak{m}}$ is just the ring of functions in a small neighbourhood of the point corresponding to $\mathfrak{m}$.