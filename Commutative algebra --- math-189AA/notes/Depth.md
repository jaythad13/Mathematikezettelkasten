---
tags:
- math-189AA/23
- comm-alg
---

Depth provides one such example.

##### _example:_ depth of a polynomial ring

Let $A = \mathbb{F}[x, y, z]$. Not only are $x, y, z$ non-unit, non-zero-divisors, they are also non-zero-divisors in sequence. That is, $x$ is not a zero divisor in $A$, $y$ is not a zero divisor in $A / (x)$, and $z$ is not a zero divisor in $A / (x, y)$. Finally, $A / (x, y, z) = \mathbb{F}$, which has no more non-unit non-zero-divisors left to mod out by. We say $A$ has depth $3$. This is exactly what we might expect by looking at the ring.

---

By Noetherianness, adding finitely many non-units will eventually get us to a maximal ideal, and then we will have nothing no more non-zero non-units to mod out by. Thus, depth is a sensible notion of Noetherian rings.

##### _example:_ depth of $\mathbb{Z}$-modules

Consider $M = \mathbb{Q} / \mathbb{Z}$ as a $\mathbb{Z}$-module. Evert $n \in \mathbb{Z}$ kills the non-zero $1 / n \in M$. Thus, every $n \in \mathbb{Z}$ is a zero-divisor on $M$. Since there are no non-zero-divisors on $M$, it has depth $0$.

$N = \mathbb{Q}$ as a $\mathbb{Z}$-module has depth $1$. Any $a \in \mathbb{Z}$ is a non-zero divisor, but then $\mathbb{Q} / a \mathbb{Q} = 0$ and we are done.

---

We define some language to capture this notion of non-zero-divisors on a module.

##### _definition:_ regular elements on a module, regular sequence, maximal regular sequence

Let $M$ be an $A$-module. $x \in A$ is $M$-regular or regular on $M$ if $xm = 0$ implies $m = 0$.

A sequence of elements $x_{1}, \dots, x_{n} \in A$ is $M$-regular if $x_{i}$ is regular on $M / (x_{1}, \dots, x_{i - 1}) M$ and $M / (x_{1}, \dots, x_{n}) M$ is regular.

An $M$-regular sequence is maximal if it cannot be extended to a longer $M$-regular sequence.

---

##### _example:_ a surprising example

For $\mathbb{F}[x, y, z, w] / (x, y) \cap (z, w)$ we surprisingly have a regular sequence of length $1$. Specifically, $x + z$ is a maximal regular sequence.

---

It's only natural that we should define depth as the maximal length of a regular sequence. However, it's not obvious that this is well-defined. This is only true when $A$ is local as well. We will use homological algebra to prove this.

##### _definition:_ depth

Let $A$ be a Noetherian local ring, and $M$ a finitely generated $A$-module. The **depth** of $M$ is the length of a maximal sequence of $M$-regular elements in $A$.

---

##### _proposition:_ depth is well-defined

Let $A$ be a local Noetherian ring. Let $M$ be a finitely generated $A$-module. Then $\operatorname{depth}_{A} M = \min \{ i \mid \operatorname{Ext}^i_{A}(A / \mathfrak{m}, M) \neq 0 \}$. Thus, depth is well-defined.

---