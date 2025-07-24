---
tags:
- math-131/1
- anal
---

### $\mathbb{N}_{0}$

$\mathbb{N}_{0}$ is the set $\{ 0, 1, 2, \dots \}$. It can be defined by the Peano axioms (which can in turn be proven by Zermelo-Fraenkel-Choice). These are

##### _definition:_ the Peano axioms

1) There is a natural number $0 \in \mathbb{N}_{0}$.
2) Every natural number $n$ has a successor $n + 1$.
3) The successor function $n \mapsto n + 1$ is injective — that is, $n + 1 = m + 1$ only if $n = m$.
4) There is no natural number such that $n + 1 = 0$.
5) $\mathbb{N}_{0}$ is well-ordered — for any non-empty $A \subset \mathbb{N}_{0}$, there is a minimum element of $\mathbb{N}_{0}$.

Note that the last axiom can equivalently stated
5) $\mathbb{N}_{0}$ satisfies the induction property — if $A \subset \mathbb{N}_{0}$ contains $0$, and if $n + 1 \in A$ for every $n \in A$, then $A$ is the whole set $\mathbb{N}_{0}$.

We can define the familiar addition and multiplication using these axioms (we won't bother doing this). However, neither of them have inverses — there are missing numbers. That's why we define the integers.

### $\mathbb{Z}$

We can define $\mathbb{Z}$ by taking formal differences of natural numbers and setting some of them to be equal in the obvious way.

##### _definition:_ $\mathbb{Z}$, the integers

$\mathbb{Z}$ is the set of all pairs of natural numbers under the equivalence relation $m_{1} - n_{1} \sim m_{2} - n_{2}$ if $m_{1} + n_{2} = m_{2} + n_{1}$.

Again, we can define the familiar addition and multiplication on $\mathbb{Z}$. We define addition component wise and the product of $m_{1} - n_{1}$ and $m_{2} - n_{2}$ as $m_{1} m_{2} +n_{1}n_{2} - (m_{1} n_{1} + m_{2} n_{2})$. We can also define an order on $\mathbb{Z}$. Specifically, $m_{1} - n_{1} > m_{2} - n_{2}$ if $m_{1} + n_{2} > m_{2} + n_{1}$.

Note that with these operations and this order $\mathbb{N}_{0}$ is embedded in $\mathbb{Z}$ — the map $n \mapsto n - 0$ preserves order, addition, and multiplication (we don't verify this). However, multiplication still doesn't have inverses. This is why we introduce the rationals.

### $\mathbb{Q}$ and its holes

We can use the same trick again to define the rationals as pairs of integers under some equivalence, and the order, addition, and multiplication on them. However, we still aren't done — $\mathbb{Q}$ has some glaring gaps.

##### _proposition:_ $\mathbb{Q}$ doesn't contain $\sqrt{ 2 }$.

There is no rational $q$ with $q^{2} = 2$.

###### _proof:_

By way of contradiction, suppose we had a rational square root of $2$ — $q$. Suppose we had $q = m /n$ in least terms. Then $m^{2} = 2 n^{2}$. But then $2 \mid m^2$, and thus, $2 \mid m$ since $2$ is prime, [[Superdiscrete --- math-55A/notes/Euclid's algorithm and primes#_theorem _ a prime divisor divides a part of a product or, the theorem of prime importance|and thus]], must appear in the prime factorisation of $m$ to appear in the prime factorisation of $m^{2}$. Say $m = 2k$. Then $2 n^{2} = 4 k^{2}$, or $n^{2} = 2 k^{2}$, and thus, $2 \mid n$ as well, contradicting our assumption that $m, n$ were in least terms.

Worse yet, it turns out that you can always get rationals with squares closer to $2$. For any positive rational $p$, consider $q = p - \frac{p^{2} - 2}{p + 2} =  \frac{2p + 2}{p + 2}$. Then $q^{2} - 2 = \frac{2(p^{2} - 2)}{(p + 2)^{2}}$. Note that $p - q$ and $q^{2} - 2$ have the same sign as $p^{2} - 2$. Thus, $p^{2} < q^{2} < 2$ or $2 < q^{2}< p^{2}$.