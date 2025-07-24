---
tags:
- alg
- math-171/16
---

### Integer-al domains

If rings are meant to be a very broad generalisation of the integers, then integral domains narrow our focus a little more. Like in the integers, non-zero elements can't multiply to give zero.

##### _definition:_ integral domain

An integral domain is a [[Abstract algebra --- math-171/notes/Rings#_definition _ commutative ring|commutative ring with identity]] where every non-zero element is not a [[Abstract algebra --- math-171/notes/Rings#_definition _ zero divisor|zero divisor]].

##### _example:_ integral domain

Integral domains are named for the integers $\mathbb{Z}$. It's the prototypical example! Also $\mathbb{Z} /n\mathbb{Z}$ is an integral domain if and only if $n$ is prime.

### Facts about integral domains

##### _proposition:_ cancellation in integral domains

Suppose $R$ is an integral domain. For $a, b, c \in R$, then if $ab = ac$ we must have $b = c$ or $a = 0$.

###### _proof:_

Suppose $ab = ac$. Then $a(b - c) = 0$. Since there are no non-zero zero-divisors, $a = 0$ or $b = c$.

##### _corollary:_ every finite integral domain is a field

Suppose $R$ is an integral domain with $\lvert R \rvert < \infty$. Then $R$ is a field.

###### _proof:_

We do this showing that multiplication by an non-zero element must be a bijection.

Consider $\alpha : R \to R$ by $r \mapsto rx$. $\alpha$ is injective since if $sx = rx$, since $x \neq 0$, we must have $s = r$. Thus, $\alpha$ is surjective, and there must exist $x^{-1} \in R$ such that $x ^{-1} x = 1$ — $x$ has a multiplicative inverse.