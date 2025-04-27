---
tags:
- math-139/29
- math-139/30
- math-139/31
- fourier
- nt
- anal
---

It's been known since antiquity that there are infinitely many [[Superdiscrete --- math-55a/notes/Euclid's algorithm and primes#_definition _ prime numbers|primes]].

##### _theorem:_ the infinitude of the primes

There are infinitely many primes in $\mathbb{Z}$.

###### _proof:_

Suppose, by way of contradiction, that $p_{1}, p_{2}, \dots, p_{n}$ was a finite enumeration of all the primes. Then $p_{1} p_{2} \dots p_{n} + 1$ is a number not divisible by any of the primes in the enumeration. It is either a prime itself, or divisible by some other prime not in $p_{1}, \dots, p_{n}$.

It's clear that most of these primes (all but one of them, actually) are either $4k + 1$ or $4k + 3$ for some $k \in \mathbb{N}_{0}$. We can use a similar proof to prove that there are infinitely many primes of the form $4k + 3$.

##### _theorem:_ infinitude of primes of the form $4k + 3$

There are infinitely many primes in $\mathbb{Z}$ of the form $4k + 3$.

###### _proof:_

Suppose, by way of contradiction, that $p_{2}, \dots, p_{n}$ was an enumeration of all primes of the form $4k + 3$, excluding $p_{1} = 3$. Then consider $p = 4 p_{2} \dots p_{n} + 3$.

$p$ is not divisible by any of the $p_{i}$. This is clear for $i > 1$ since $p$ has residue $3$ modulo each of those $p_{i}$. Further, $p$ is not divisible by $3$ since that would force $4 p_{2} \dots p_{n}$ to be divisible by $3$ which it is not (since $3$ is manifestly not in its prime factorisation).

If $p_{2}, \dots, p_{n}$ were all the primes of the form $4k + 3$, $p$ would have to be the product of primes $q_{1}, \dots, q_{m}$ of the form $4k + 1$. But the product of primes of the form $q_{i} = 4k_{i} + 1$ is 
$$
q_{1} q_{2} \dots q_{n} = 4 (k_{1} k_{2} \dots k_{n} + \dots k_{1} + \dots + k_{n}) + 1
$$
of the form $4k + 1$. Thus, $p$ must be divisible by a different prime of the form $4k + 3$.

We can't do the same thing to check whether there are infinitely many primes of the form $4k + 1$. More generally when are there infinitely many primes of the form $\ell + q k$? The most elementary obstruction to having primes of the form $\ell + q k$ occur when $\gcd(\ell, q) > 1$, and thus $\gcd(\ell, q) \mid \ell + q k$ for all $k$. We might hope that this is the only obstruction — if an arithmetic sequence can contain any (odd) primes at all, it contains infinitely many. Legendre conjectured this more general statement to prove quadratic reciprocity, and Dirichlet ultimately proved it.

##### _theorem:_ Dirichlet's theorem on arithmetic progressions

If $q$ and $\ell$ are relatively prime, then the arithmetic sequence $\{ \ell + k q \mid k \in \mathbb{Z} \}$ contains infinitely many primes.

### The simplest case of Dirichlet's theorem

The idea behind Dirichlet's theorem is the same as that of, an admittedly ridiculous, analytic proof of the infinitude of primes — Euler's proof that the sum of the reciprocals of the primes diverges. Of course, this is the simplest case where $\ell = 1$, $q = 2$ (since the proof we're about to give holds even after ignoring the even prime).

##### _lemma:_ log approximation

For all $\lvert x \rvert < 1/2$,
$$
\ln(1 + x) = x + E(x)
$$
where the magnitude of the error term $E(x)$ is bounded — $\lvert E(x) \rvert \le x^{2}$.

###### _proof:_

Consider the [[Mathematical Analysis I --- math-131/notes/Power series#_definition _ power series|power series expansion]] of the [[Complex Analysis --- math-135/notes/Cauchy integral formula#_corollary _ the derivative form (holomorphic functions are smooth and analytic)|analytic function]]
$$
\ln(1 + x) =  x - \frac{x^{2}}{2} + \frac{x^{3}}{3} - \frac{x^4}{4} + \cdots.
$$
Then the error term is bounded
$$
\lvert E(x) \rvert \leq \frac{x^{2}}{2} + \frac{x^3}{3} + \frac{x^4}{4} + \cdots = \frac{x^{2}}{2} (1 + \lvert x \rvert + \lvert x \rvert ^{2} + \cdots).
$$
For $\lvert x \rvert < 1 / 2$, the geometric sum is bounded by $2$, and thus, $\lvert E(x) \rvert \le x^{2}$.

##### _lemma:_ approximating the Riemann zeta function

[[Complex Analysis --- math-135/notes/The Riemann zeta function#_definition _ the Riemann zeta function|The Riemann zeta function]] $\zeta$ is approximated
$$
\sum_{p \text{ prime}} \frac{1}{p^s} = \ln \zeta(s) + C
$$
for all real $s > 1$.

###### _proof:_

We can take logarithms on both sides of the [[Complex Analysis --- math-135/notes/The Riemann zeta function#_theorem _ Euler's product formula|Euler product formula]] to get
$$
\ln \zeta(s) = - \sum_{p \text{ prime}} \ln \left( 1 - \frac{1}{p^s} \right).
$$

By our previous lemma approximating the logarithm
$$
\ln \zeta(s) \le - \sum_{p \text{ prime}} \left( - \frac{1}{p^s} + \frac{1}{p^{2s}} \right) =  \sum_{p \text{ prime}} \frac{1}{p^s}  - \sum_{p \text{ prime}} \frac{1}{p^{2s}}.
$$
Since $\sum 1 / (p^s)^{2} \le \sum 1 / (n^s)^{2} < \infty$, and the inequality in the logarithm approximation is only in the $\sum 1/p^{2s}$ term, we have the desired approximation
$$
\ln \zeta(s) = \sum_{\text{p} \text{ prime}} \frac{1}{p^s} - C.
$$

##### _theorem:_ the sum of the reciprocals of primes diverges

The sum
$$
\sum_{p \text{ prime}} \frac{1}{p}
$$
diverges.

###### _proof:_

We can write
$$
\sum_{p \text{ prime}} \frac{1}{p} \geq \liminf_{s \to 1^+} \sum_{p \text{ prime}} \frac{1}{p^s} = \liminf_{s \to 1^+} \ln \zeta(s) + C.
$$
However,
$$
\liminf_{s \to 1^+} \zeta(s) = \liminf_{s \to 1^+} \sum_{n = 1}^\infty \frac{1}{n^s} > \sum_{n = 1}^M 1 / n.
$$
for every $M$, and thus, diverges. Thus, the $\liminf$ of $\ln \zeta(s)$ diverges too, and finally, so does the sum of the reciprocals of the primes.

##### _corollary:_ the infinitude of the primes

There are infinitely many primes.

### Reducing the theorem

We want to use the same idea to prove Dirichlet's theorem in general. That is, we want to prove that there are infinitely many primes of the form $qk + \ell$ where $\gcd(q, \ell) = 1$ by proving that the sum
$$
\sum_{p \text{ prime}, p = kq + \ell} \frac{1}{p}
$$
diverges.

At this point, we introduce some notation to make our lives easier.

##### _notation:_ Weierstrass $\wp$ for primes

The set of all primes is denoted $\wp$.

##### _notation:_ modular equivalence

When $q$ is obvious, we write $p \equiv \ell$ to mean $p = \ell \pmod q$.

Our goal is now to reduce this result to something that we can say about [[Fourier Analysis --- math-139/notes/Dirichlet characters and series|Dirichlet characters and series]]. Note that, we can define the characteristic function of $\ell$ modulo $q$ which gives a convenient way to express the infinite sum we want to show diverges, and simultaneously gives a way to utilise the tools of [[Fourier Analysis --- math-139/notes/Finite Fourier analysis|finite Fourier analysis]] and thus, Dirichlet characters and series.

##### _definition:_ the modular characteristic function

The modular characteristic function of $\ell \in \mathbb{Z} / q \mathbb{Z}^*$ is the function
$$
\begin{align}
\delta_{\ell}  & : \mathbb{Z} / q \mathbb{Z}^* \to \mathbb{C} \\
 & : m \mapsto \begin{cases}
1 & m = \ell \\
0 &
\end{cases}
\end{align}
$$
extended to a function on $\mathbb{Z} / q \mathbb{Z}$, supported on $\mathbb{Z} / q \mathbb{Z}^*$ and extended periodically to $\mathbb{Z}$ (by the canonical surjection $\mathbb{Z} \to \mathbb{Z} / q \mathbb{Z}$).

Note that
$$
\sum_{p \in \wp, p \equiv \ell} \frac{1}{p^s} = \sum_{p \in \wp} \frac{\delta_{\ell}(p)}{p^s}
$$
for all $s > 1$ (all $s$ where the sum on the left is guaranteed to converge). Using finite Fourier analysis, we can decompose this sum. For convenience, we give it a name.

##### _definition:_ the modular characteristic series

The modular characteristic series of $\ell \in \mathbb{Z} / q \mathbb{Z}^*$ is the sum
$$
\sum_{p \in \wp} \frac{\delta_{\ell}(p)}{p^s}.
$$
Note that this is not an $L$-[[Fourier Analysis --- math-139/notes/Dirichlet characters and series|series]] proper since $\delta_{\ell}$ is not a [[Fourier Analysis --- math-139/notes/Finite Fourier analysis#_definition _ character, the dual group|character]] on $G$.

##### _lemma:_ Fourier decomposition of the modular characteristic series

For any $\ell \in \mathbb{Z} / q \mathbb{Z}^*$ the modular characteristic series decomposes as
$$
\sum_{p \in \wp} \frac{\delta_{\ell}(p)}{p^s} = \frac{1}{\lvert G \rvert } \sum_{\xi \in \widehat{G}} \overline{\chi_{\xi}(\ell)} \sum_{p \in \wp} \frac{\chi_{\xi}(p)}{p^s}.
$$

###### _proof:_

By [[Fourier Analysis --- math-139/notes/Finite Fourier analysis#_theorem _ Fourier inversion|Fourier inversion]], we have (as functions on $\mathbb{Z} / q \mathbb{Z}^*$)
$$
\delta_{\ell} = \sum_{\xi \in \widehat{\mathbb{Z} / q \mathbb{Z}^*}} \hat{\delta}_{\ell}(\xi) \, \xi.
$$

However, because $\delta_{\ell}$ is so simple, its [[Fourier Analysis --- math-139/notes/Finite Fourier analysis#_definition _ Fourier coefficient|Fourier coefficients]] $\hat{\delta}_{\ell}$ will be simple too. Explicitly,
$$
\hat{\delta}_{\ell}(\xi) = \frac{1}{\lvert G \rvert } \sum_{m \in G} \delta_{\ell}(m) \overline{\xi(m)} = \frac{\overline{\xi(\ell)}}{\lvert G \rvert }
$$
since $\delta_{\ell}$ is only nonzero when $m = \ell$. Extending this formula to all of $\mathbb{Z}$ and extending the $\xi$ to their [[Fourier Analysis --- math-139/notes/Dirichlet characters and series#_definition _ Dirichlet character|Dirichlet characters]] $\chi_{\xi}$, we get
$$
\delta_{\ell}(m) = \frac{1}{\lvert G \rvert } \sum_{\xi \in \widehat{G}} \overline{\chi_{\xi}(\ell)} \chi_{\xi}(m).
$$
as functions on $\mathbb{Z}$. Plugging this into the definition of the modular characteristic series gives the desired formula.

##### _lemma:_ the trivial part of the modular characteristic series diverges as $s \to 1^+$

Let $1$ be the trivial character in $\widehat{G}$. Then 
$$
\sum_{p \in \wp} \frac{\chi_{1}(p)}{p^s} \to \infty
$$
as $s \to 1^+$.

###### _proof:_

$1(p) = 1$ for all $p \in \mathbb{Z} / q \mathbb{Z}^*$. Thus, $\chi_{1}(p) = 0$ only if $\gcd(p, q) \neq 1$. There are only finitely many such $p$ (all primes greater than $q$ are coprime with $q$). Thus,
$$
\sum_{p \in \wp} \frac{\chi_{1}(p)}{p^s} = \sum_{p \in \wp} \frac{1}{p^s} - \sum_{p \in \wp, p < q} \frac{1}{p^s}.
$$
As $s \to 1^+$ the sum on the left diverges (to $\infty$) and the sum on the right is finite, so their difference diverges (to $\infty$) as well.

##### _theorem:_ reduction of Dirichlet's theorem

If for any non-trivial character $\chi \in \widehat{G}$, its Dirichlet $L$-[[Fourier Analysis --- math-139/notes/Dirichlet characters and series#_definition _ Dirichlet $L$-series|series]] converges as $s \to 1^+$, then Dirichlet's theorem follows.