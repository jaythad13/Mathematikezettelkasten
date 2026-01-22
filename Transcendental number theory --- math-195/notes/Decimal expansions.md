---
tags:
- math-195/2
- nt
---

An important tool in transcendental number theory is that of decimal expansions, and more generally, $b$-ary expansions. We could work in general base $b$, but we will only ever work in base $10$.

##### _definition:_ decimal expansions, $b$-ary expansion

A **decimal expansion** of $\alpha \in [0, 1)$ is a sequence $\{ d_{n} \}_{n \in \mathbb{N}}$ with $d_{n} \in [0, 9] \cap \mathbb{N}$ such that $\alpha = \sum_{n = 1}^\infty {d_{n}} / {10^n}.$

For integer $b \geq 2$, a **$b$-ary expansion** of $\alpha$ is a sequence $\{ d_{n} \}_{n \in \mathbb{N}}$ with $d_{n} \in [0, b - 1] \cap \mathbb{N}$ such that $\alpha = \sum_{n = 1}^\infty d_{n} / b^n$.

---

By comparison with the geometric series $\sum_{n = 1}^\infty (b - 1) / b^n$, it's clear to see that every possible sequence of $\{ d_{n} \}_{n \in \mathbb{N}}$ forms a a convergent sequence. However, can we write every real number like this?

##### _theorem:_ every number in $[0, 1)$ has a unique decimal expansion

Each $\alpha \in [0, 1)$ has a $b$-ary expansion. This expansion is unique modulo the equivalence $1 / b^k = \sum_{n = k + 1}^\infty (b - 1) / b^n$.

###### _proof:_

Let $d_{1}$ be the maximal integer such that $\alpha \geq d_{1} / b$. Then, build $\{ d_{n} \}_{n \in \mathbb{N}}$ recursively by choosing $d_{n}$ to be the maximal integer such that $\alpha \geq \sum_{i = 1}^n d_{i} / b^i$. Note that at each stage, the fact that $x < 1$ implies $0 \leq d_{n} \leq b - 1$. By maximality of each $d_{i}$, at each $n$, $\left\lvert  \alpha - \sum_{i = 1}^n d_{i} / b^i  \right\rvert < 1 / b^i$, so as $n \to \infty$ the series converges to $\alpha$.

---

Decimals give us a useful characterisation of rational numbers.

##### _definition:_ periodic and eventually periodic decimal expansions, period

$\alpha \in [0, 1)$ has a **periodic decimal expansion** $\{ d_{n} \}_{n \in \mathbb{N}}$ if there is some **period** $m \in \mathbb{N}$ such that $d_{n} = d_{n + m}$ for all $n$. We write this as $\alpha = 0.\overline{d_{1} \dots d_{m}}$.

$\alpha$ has an **eventually periodic decimal expansion** if there is some $b \in \mathbb{N}$ such that $10^m(\alpha - b / 10^m)$ has a periodic decimal expansion. 

---

##### _theorem:_ eventually periodic decimal expansions are rational

$\alpha \in [0, 1)$ has an eventually periodic decimal expansion if and only if $\alpha \in \mathbb{Q}$.

###### _proof:_

Suppose $\alpha = p / q \in \mathbb{Q}$. Then the fact that the decimal expansion of $\alpha$ follows from long division. All remainders of $p$ divided by $q$ are between $0$ and $q$, and so there is eventually a repeat. Since remainders form a "Markov chain", from this cycle on, the decimal expansion is periodic.

It's clear to see that finite decimal expansions are rational. Thus, it suffices to prove that periodic decimal expansions are rational. Let $D = \sum_{n = 1}^m d_{n} / 10^n$. Then we can write the periodic decimal expansion extending $d_{1}, \dots, d_m$ as
$$
\sum_{n = 1}^\infty \frac{d_{n}}{10^n} = D \sum_{n = 1}^\infty \frac{1}{10^{mn}}
$$
which is rational by geometric series. Thus, periodic decimal expansions are rational.

---

One natural question is how large the period of the decimal expansion of a rational number can be. In the simplest case, we can ask about $1 / p$ for $p$ [[Superdiscrete --- math-55A/notes/Prime numbers#_definition _ prime numbers|prime]]. Sometimes, like with $1 / 7 = 0.\overline{142857}$ we have that the period is $p - 1$. 

##### _theorem:_ periods of reciprocals of primes

Let $p \neq 2, 5$. Then the period of the decimal expansion of $p$. The period of $1 / p$ is the smallest $m \geq 1$ such that $10^m \equiv 1 \pmod p$.

###### _proof:_

Suppose $p = 0.\overline{d_{1} \dots d_{m}}$. Then the standard geometric series manipulations give
$$
1 / p = \frac{\sum_{n = 1}^m d_{n} 10^{m - n}}{10^m - 1} = \frac{z}{10^m - 1}
$$
for some integer $z$. Then it follows that $z p = 10^m - 1$. But then $10^m \equiv 1 \pmod p$.

>[!missing]
>why can you always choose the smallest such $m$?

---

Note that by [[Superdiscrete --- math-55A/notes/Fermat's little theorem and Euler's theorem#_theorem _ Fermat's little theorem|Fermat's little theorem]] $m$ always exists, and in particular, is at most $p - 1$. If $p - 1$ is the smallest $m$ such that $a^m \equiv 1$, then $a$ is a **primitive root** modulo $p$. Thus, the existence of infinitely many primes such that the period of $1 / p$ is $p - 1$ is equivalent to $10$ being a primitive root modulo infinitely many primes. We have no idea if this is true.