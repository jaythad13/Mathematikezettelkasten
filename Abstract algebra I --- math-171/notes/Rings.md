---
tags:
  - alg
  - math-171
lecture:
- math-171-4
- math-171-16
---

### Warm up

Let's play "Are These Groups?"

##### _examples:_ Are These Groups?

1) $\mathbb{Z}$ under addition? Yes!
2) $\mathbb{Z}$ under multiplication? No
3) $\mathbb{R}$ under addition? Yes!
4) $\mathbb{R}$ under multiplication? No
5) $\mathbb{R} \setminus \{ 0 \}$ under multiplication? Yes!
6) $\mathcal{M}_{n}(\mathbb{R})$ under addition? Yes!
7) $\mathcal{M}_{n}(\mathbb{R}) \setminus \{ \mathbf{0} \}$ under multiplication? No

Notice how things that are groups under "addition" often fail to be groups under "multiplication" by some trivial failure to have a multiplicative inverse for the additive identity This leads to define rings.

### What's a ring?

##### _definition:_ rings

A ring $R$ is a set with two binary operations (typically $+$ and $\times$) such that
- $(R, +)$ is an abelian group with identity zero, denoted $0$,
- $\times$ is associative,
- $\times$ distributes over $+$. That is, $(a + b) \times c = (a \times c) + (b \times c)$ and $a \times(b + c) = (a \times b) + (b \times c)$

##### _definition:_ commutative ring

A ring $R$ is commutative if its multiplication $\times$ is [[Motivating groups#_definition _ commutativity|commutative]].

##### _definition:_ ring with identity

A ring $R$ is said to have identity if it contains some $1 \in R$ such that $1 \times a = a \times 1 = a$ for all $a \in R$.

##### _examples:_ rings

1) $\mathcal{M}_{n}(\mathbb{R})$
2) $\mathbb{Z}$
3) $2\mathbb{Z}$ — the even integers
4) $\mathbb{Z}/n\mathbb{Z}$ — the integers modulo $n$.

##### _examples and non-examples:_ commutative rings with identity

1) $\mathcal{M}_{n}(\mathbb{R})$ is a non-commutative ring with unity $I$
2) $\mathbb{C}$ is a commutative ring with identity $1$
3) $2 \mathbb{Z}$ is a commutative ring without identity! Pay attention to this example!

There's a special subtype of commutative rings with identity — [[Abstract Algebra I --- math-171/notes/Fields|fields]]. Essentially, a ring is a field when the multiplication doesn't fail to be a group.

![[Abstract Algebra I --- math-171/notes/Fields#_definition _ fields|Fields]]

### Things about rings

Here are some basic facts about any ring $R$, and any elements $a, b \in R$. $0$ is the additive identity, and if $R$ has a multiplicative identity, we denote it by $1$.

##### _proposition:_ multiplying by zero gives zero

$$
0a = a0 = 0
$$

###### _proof sketch:_

$$
\begin{split}
& 0a = (0 + 0)a \\
\implies & 0a - 0a = 0a + 0a - 0a \\
\implies & 0 = 0a
\end{split}
$$
and similarly for right multiplication.

##### _proposition:_ multiplying by additive inverses gives additive inverses

$$
(-a)b = a(-b) = - ab
$$

###### _proof sketch:_

$$
\begin{split}
& (a - a)b = 0 \\
\implies & ab + (-a)b = 0 \\
\implies & (a)b = -ab
\end{split}
$$
and similarly for right multiplication.

##### _corollary:_ multiplying two additive inverses is the same as multiplying two numbers

$$
(-a)(-b) = ab
$$

###### _proof sketch:_

$$
\begin{split}
(-a)(-b) & = - a(-b) \\
& = - (-ab) \\
& = ab
\end{split}
$$

##### _proposition:_ the identity is unique

If $R$ has identity $1$, it is unique.

###### _proof sketch:_

Suppose $1'$ is another multiplicative identity. Then
$$
\begin{split}
1 & = 1 \times 1' \\
& = 1'
\end{split}
$$

##### _corollary:_ the identity gives inverses

 $(-1)a = -a$ for $a \in R$.
 
###### _proof:_

Note that
$$
\begin{split}
(-1) a & = -(1a) \\
& = - a
\end{split}
$$
(since [[#_proposition _ multiplying by additive inverses gives additive inverses|multiplying by additive inverses gives additive inverses]]) giving us that $(-1)a$ is the unique additive inverse of $a$, $-a$. Note that we need the uniqueness of the identity to talk about *the* identity giving inverses.

By now, we've seen enough about groups to rush through the theory of rings doing "similar things". It may also be obvious by now that (most of the time) it's only really worth thinking about rings with identity.

### Things about rings with identity

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

### Lots of examples!
 
Some rings fall into a large class of examples — the familiar polynomial rings and matrix rings are just two of them!

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

One of the most important classes of rings is integral domains.

![[Abstract Algebra I --- math-171/notes/Integral domains#Integer-al domains|Integral domains]]

### Substructures of rings

Rings have subrings, but also something stronger that we will see we can quotient out by.

##### _definition:_ subring

A subring of a ring $R$ is a subgroup of $(R, +)$ that is also closed under multiplication.

##### _example:_ subring

$\mathbb{R}$ is a subring of $\mathbb{C}$.

While we can quotient out a subgroup $(S, +) \le (R, +)$ to get $(R, +)/(S, +)$ this doesn't say anything about the multiplicative structure. Notably, we want the natural projection from $R$ to $R/S$ to be a [[Abstract Algebra I --- math-171/notes/Ring homomorphisms|ring homomorphism]]. Since we can't ensure this with a [[Abstract Algebra I --- math-171/notes/Centralisers, centre, normalisers, and stabilisers#_definition _ normaliser, $N_{G}(A)$|normality condition]] (we probably don't have multiplicative inverses), we just require absorption under multiplication by any element of $R$, not just the substructure.

![[Abstract Algebra I --- math-171/notes/Ideals and quotients#_definition _ ideal]]