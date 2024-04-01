---
tags:
- math-171
- alg
lecture:
- math-171-16
---

We've seen enough about groups to rush through the theory of rings doing "similar things". Recall all of our [[An introduction to rings and fields#Rings|definitions]] and [[An introduction to rings and fields#Things about rings|basic results]]. These are some more.

### More ring things

Here $R$ denotes a ring (with identity).

##### _definition:_ unit

A unit of a ring is an element with a multiplicative inverse

##### _definition:_ zero divisor

A zero divisor in a ring is an element $a \in R$ such that there exists nonzero $b \in R$ with $ab = 0$ or $ba = 0$.

##### _example:_ unit, zero divisors in familiar rings

1) In $\mathbb{Z}$, $1, -1$ are the only units. Note that here they are self-inverse, but in general, they don't have to be
2) In $\mathbb{Z} / 6\mathbb{Z}$, $\overline{2}$ is a zero divisor since $\overline{2} \times  \overline{3} = \overline{6} = \overline{0}$.
3) In $\mathbb{Z}/n\mathbb{Z}$ all $a$ coprime with $n$ mean give $\overline{a}$ as unit (see [[Dividing integers - basic number theory#_theorem _ Bezout's theorem|Bezout's theorem]]).

##### _proposition:_ every unit is not a zero divisor

For any unit $r \in R$, there is no $a \in R$ such that $ra = 0$.

###### _proof:_

Suppose $a \in R$ gives $ra = 0$. Then
$$
\begin{split}
r^{-1} (ra) & = r^{-1}0 \\
 & = 0.
\end{split}
$$
and
$$
\begin{split}
(r^{-1}r)a & = 1a \\
 & = a.
\end{split}
$$
Then, by associativity, $a = 0$, and thus, $r$ cannot be a zero divisor.

### Special rings

Let's look at some examples of rings so we can develop different classes of rings

##### _definition:_ polynomial rings

For any commutative ring with identity and some indeterminate $x$ (that is, $x \not\in R$), $R[x]$ is the ring of polynomials in $x$ with coefficients in $R$.

##### _definition:_ matrix rings

For any ring $R$, and $n \in \mathbb{N}$, we have the matrix ring $\mathcal{M}_{n}(R)$, the group of $n \times n$ matrices with elements in $R$ under matrix addition and multiplication.

##### _definition:_ group rings

For any commutative ring with identity $1 \neq 0$ (that is, $R$ is not the trivial ring) and any finite group $G = \{ g_{1}, \dots, g_{n} \}$, 
$$
RG = \{ a_{1} g_{1} + \dots + a_{n} g_{n} \mid a_{i} \in R, g_{i} \in G  \}
$$
under component-wise addition and group multiplication (after distribution).

##### _example:_ group rings

$\mathbb{C}S_{3}$ is a ring (where $S_{3}$ is the symmetric group on $\mathbb{N}_{3}$). Then for $\alpha = 3e + 2(1 \, 2 \, 3)$ and $\beta = 4(1 \, 2) - 5(1 \, 3) + (1 \, 2 \, 3)$, we have
$$
\alpha + \beta = 3e + 4(1 \, 2) - 5(1\, 2) + 3(1 \, 2 \, 3)
$$
and
$$
\alpha \beta = 12(1 \, 2) - 7 (1 \, 3) + 3 (1 \, 2 \, 3) + 2(1 \, 3 \, 2) - 10(3 \, 2).
$$

##### _definition:_ division ring

A division ring is a (non-trivial) ring where every nonzero element is a unit.

##### _definition:_ integral domain

An integral domain is a commutative ring with identity where every nonzero element is not a zero divisor.

##### _example:_ integral domain

Integral domains are named for the integers.

##### _proposition:_ cancellation in integral domains

Suppose $R$ is an integral domain. For $a, b, c \in R$, then if $ab = ac$ we must have $b = c$ or $a = 0$.

###### _proof:_

Suppose $ab = ac$. Then $a(b - c) = 0$. Since there are no nonzero zero-divisors, $a = 0$ or $b = c$.

##### _corollary:_ every finite integral domain is a field

Suppose $R$ is an integral domain with $\lvert R \rvert < \infty$. Then $R$ is a field.

###### _proof:_

We do this showing that multiplication by an nonzero element must be a bijection.

Consider $\alpha : R \to R$ by $r \mapsto rx$. $\alpha$ is injective since if $sx = rx$, since $x \neq 0$, we must have $s = r$. Thus, $\alpha$ is surjective, and there must exist $x^{-1} \in R$ such that $x ^{-1} x = 1$ — $x$ has a multiplicative inverse.

### Substructures of rings

Rings have subrings, but also something stronger that we will see we can quotient out by.

##### _definition:_ subring

A subring of a ring $R$ is a subgroup of $(R, +)$ that is also closed under multiplication.

##### _example:_ subring

$\mathbb{R}$ is a subring of $\mathbb{C}$.

##### _definition:_ (left and right) ideals

Let $R$ be a ring. A nonempty subset $I \subset R$ is a left ideal provided
1) $I$ is a subring of $R$
2) $ri \in I$ if $i \in I$ for left ideals 
or
2) $ir \in I$ if $i \in I$ for right ideals. 