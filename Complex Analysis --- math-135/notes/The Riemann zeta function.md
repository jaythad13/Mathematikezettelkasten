---
tags:
- math-135/23
- math-135/24
- anal
- complex
---

The Riemann zeta function is an important function in analytic number theory. Its importance was first recognised by Euler, who showed that it can be written as an [[Complex analysis --- math-135/notes/Infinite products|infinite product]] related to the [[Superdiscrete --- math-55A/notes/Euclid's algorithm and primes#Primes|primes]].

##### _definition:_ the Riemann zeta function

The Riemann zeta function is
$$
\zeta(s) = \sum_{n = 1}^\infty \frac{1}{n^s}.
$$

Note that this is defined and holomorphic exactly for $s$ with $\operatorname{Re} s > 1$.

##### _proposition:_ zeta is holomorphic for $\operatorname{Re} s > 1$

The Riemann zeta function is holomorphic in $s$ for all $\operatorname{Re} s > 1$.

###### _proof:_


### A meromorphic extension to the right half plane

Before we extend $\zeta$ to all of $\mathbb{C}$, there is an easier way to extend it just to the right half plane (with a pole at $\operatorname{Re} s = 1$ of course)

We use a sequence of functions approximating $\zeta$. In particular, we need to consider the following sequence of error functions.

##### _lemma:_ the error functions $\delta_{n}$

There exists a sequence of functions $(\delta_{n})$ such that 
1) Each $\delta_{n}$ is entire
2) $\lvert \delta_{n}(s) \rvert < \lvert s \rvert / n^{\operatorname{Re} s + 1}$
and
$$
\sum_{n = 1}^{N - 1} \frac{1}{n^s} - \int \frac{1}{x^s} \, dx = \sum_{n = 1}^{N - 1} \delta_{n}(s)
$$

###### _proof sketch:_

Choose
$$
\delta_{n}(s) = \int _{n}^{n + 1} \frac{1}{n^s} - \frac{1}{x^s} \, dx.
$$
Bound the integrand by the mean value theorem, and thus bound $\delta_{n}$ —
$$
\lvert \delta_{n} (s) \rvert < \frac{\lvert s \rvert }{n^{\operatorname{Re} s + 1}}
$$
##### _proposition:_ the extension to the right half plane

For $\operatorname{Re} s > 1$, we have 
$$
\zeta(s) - \frac{1}{s - 1}= H(s)
$$
where
$$
H(s) = \sum_{n = 1}^\infty \delta_{n}(s)
$$
is holomorphic in the right half plane.

##### _corollary:_ the Riemann zeta function has an extension to the right half plane

$\zeta$ can be extended to
$$
\zeta(s) = H(s) + \frac{1}{s - 1}
$$
which is meromorphic on the right half plane with a simple pole at $s = 1$.

Now with $\zeta$ defined in the right half plane, we can prove the Euler product formula!

##### _theorem:_ the Euler product formula

$$
\sum_{n = 1}^\infty \frac{1}{n^s} = \prod_{p \text{ prime}} \frac{1}{1 - 1 / p^s}
$$

###### _proof sketch:_

We will prove this is true for real $s > 0$ by double inequality by comparing finite sums to infinite products and taking limits and vice versa. 

Specifically, for $N \in \mathbb{N}$, and some integer $M > N$, notice that each $n \in \mathbb{N}$ with $n \le N$ [[Superdiscrete --- math-55a/notes/Euclid's algorithm and primes#_theorem _ unique factorisation|has a unique prime factorisation]]. Each prime appears fewer than $M$ times in each factorisation ($p > 1$, so $p^M > M > N$), so
$$
\sum_{n = 1}^N \frac{1}{n^s} \le \prod_{p \text{ prime}, p \le N} \left( 1 + \frac{1}{p} + \dots + \frac{1}{p^{Ms}} \right) \le \prod_{p \text{ prime}} \frac{1}{1 - 1/p^s}.
$$
Also, for any $M, N \in \mathbb{N}$
$$
\prod_{p \text{ prime}, p \le N} \left( 1 + \frac{1}{p} + \dots + \frac{1}{p^{Ms}} \right) \le \sum_{n = 1}^\infty \frac{1}{n^s}.
$$
Thus, taking limits for the partial sums/products on the left as $N \to \infty$, we get double inequality and thus, equality.

Note that this requires showing that the Euler product does actually converge (to a holomorphic function) for all $\operatorname{Re} s > 1$. We can do so by showing that the multiplicands have [[Complex analysis --- math-135/notes/Infinite products#_theorem _ infinite products of holomorphic functions|bounded distance]] from $1$. In particular, on any compact $K \subset \{ s \in \mathbb{C} \mid \operatorname{Re} s > 1 \}$.
$$
\frac{1}{1 - p^{-s}} - 1 = \frac{p^{-s}}{1 - p^{-s}}
$$
has absolute value
$$
\left\lvert  \frac{1}{1 - 1 / p^s}  \right\rvert \left\lvert  \frac{1}{p^s}  \right\rvert < 2 p^{-\sigma}
$$
for $1 < \sigma < \operatorname{Re} s$ — the first term is less than $2$, since $p > 2$.

### Analytic continuation to the complex plane (minus $1$)

While we could use the previous approach to define $\zeta$ on $\mathbb{C}$, there's another way to do this using the theta function.

##### _definition:_ theta function

For $t > 0$, the theta function is
$$
\vartheta(t) = \sum_{n = -\infty}^\infty e^{-\pi n^{2} t}
$$

##### _proposition:_ the functional equation for theta

The theta function satisfies the functional equation
$$
\vartheta(t) = t^{1 / 2} \vartheta\left( \frac{1}{t} \right).
$$

###### _proof sketch:_

Apply the [[Complex analysis --- math-135/notes/Fourier analysis and holomorphic functions#_theorem _ the Poisson summation formula|Poisson summation formula]] to $g(x) = e^{- \pi t (x + a)^{2}}$.

##### _corollary:_ asymptotics for theta

As $t \to \infty$ we have $\lvert \vartheta(t) - 1 \rvert \le C e^{- \pi t}$ and as $t \to 0$, $\vartheta(t) \le C t^{1 / 2}$.

###### _proof:_

The first follows by noticing that $\vartheta$ is even in $n$, and thus,
$$
\vartheta(t) = 1 + 2 \sum_{n = 1}^\infty e^{-\pi n^{2} t}.
$$
Bounding this sum

We are now going to try to get a functional equation for $\zeta$ in terms of [[Complex analysis --- math-135/notes/The gamma function#_definition _ the gamma function|the gamma function]].

##### _theorem:_ functional equation for $\zeta$

For all $s$ in the right half plane of $\mathbb{C}$,
$$
\pi^{-s / 2} \, \Gamma\left( \frac{s}{2} \right) \, \zeta(s) = \pi^{(s - 1)/2} \, \Gamma\left( \frac{1 - s}{2} \right) \, \zeta(1 - s).
$$

###### _proof:_

This proof follows from several lemmas.

##### _lemma:_ gamma, zeta, and theta

If $\operatorname{Re} s > 1$,
$$
\pi^{-s / 2} \, \Gamma\left( \frac{s}{2} \right) \, \zeta(s) = \int_{0}^\infty u^{s / 2 - 1} \frac{\vartheta(u) - 1}{2}  \, dx 
$$

###### _proof:_

We start from the right.

First, by the Lebesgue dominated convergence theorem (if everything lives in a lemon, you're fine theorem), we can exchange summation and integration inside the integral on the right to get
$$
\int_{0}^\infty u^{s / 2}  \, dx 
$$
Letting $u = t / \pi n^{2}$ and changing variables to $t$, we get exactly what we want.

##### _definition:_ the $\xi$ function

The $\xi$ function is defined by
$$
\xi(s) = \pi^{-s / 2} \, \Gamma\left( \frac{s}{2} \right) \, \zeta(s)
$$
for $\operatorname{Re} s > 1$.

Now we can restate our functional equation in terms of $\xi$!

##### _theorem:_ $\xi$ has an meromorphic extension to $\mathbb{C}$

$\xi$ has a meromorphic extension to $\mathbb{C}$ with simple poles at $0$ and $1$ and satisfies the functional equation
$$
\xi(s) = \xi(1 - s)
$$

###### _proof:_

Write $\xi(s)$ in terms of the integral of $\vartheta$ using our previous lemma. Change some variables, and get an integral of a function with exponential delay plus $1 / (s - 1) + 1/s$.

##### _corollary:_ $\zeta$ on the left half plane

$\zeta$ has a meromorphic extension to the complex plane with all zeroes either trivial zeroes in $\{ 0, -2, -4, \dots \}$ or in the critical strip $\{ s \in \mathbb{C} \mid 0 \le \operatorname{Re} s \le 1 \}$ and a single simple pole at $1$.

###### _proof sketch:_

Now it makes sense to state the Riemann hypothesis!

##### _conjecture:_ the Riemann hypothesis

All non-trivial zeroes of $\zeta$ lie on the line $\operatorname{Re} s = 1/2$.
