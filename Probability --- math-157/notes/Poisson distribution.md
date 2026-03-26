---
tags:
- math-157/1
- prob
---

The Poisson distribution behaves approximately like a [[Probability --- math-157/notes/Geometric and binomial distributions#_definition _ binomial distribution|binomial distribution]] for large $n$ and small $p$. That is, it models the number of events for some exponentially rare event. Specifically, let $\lambda = \mathbb{E}(X) = np$ where $X \sim \operatorname{Bin}(n, p)$. Then we can write
$$
\begin{align}
\lim_{n \to \infty}  \mathbb{P}(X = k) & = \lim_{n \to \infty} \binom{n}{k} p^k (1 - p)^{n - k} \\
 & = \lim_{ n \to \infty } \frac{n(n - 1) \cdots (n - k)}{k!} p^k (1 - p)^{n - k} \\
 & = \lim_{ n \to \infty } \frac{(np)^k}{k!} \left( 1 - \frac{\lambda}{n} \right)^n \\
 & = \frac{\lambda^k e^{-\lambda}}{k!}.
\end{align}
$$

##### _definition:_ Poisson distribution

A random variable $X$ has **Poisson distribution with parameter $\lambda$**, abbreviated $X \sim \operatorname{Poi}(\lambda)$, if its probability function is supported on non-negative integers with $f(k) = \lambda^k e^{-\lambda} / k!$.

---

Again this really is a [[Probability --- math-157/notes/Discrete probability#_definition _ probability, probability function|probability function]] — we have $\sum_{k = 0}^\infty f(k) = e^{-\lambda} \sum_{k = 0}^\infty \lambda^k / k! = 1$.

The Poisson distribution really does have the expected value we want it to.

##### _proposition:_ expectation of a Poisson random variable

Suppose $X \sim \operatorname{Poi}(\lambda)$. Then $\mathbb{E}(X) = \lambda$.

###### _proof:_

$$
\begin{align}
\mathbb{E}(X) & = \sum_{k = 0}^\infty k \frac{\lambda^k e^{- \lambda}}{k!} \\
 & = 0 + \sum_{k = 1}^\infty \frac{\lambda^k e^{- \lambda}}{(k - 1)!} \\
 & = \lambda e^{- \lambda} \sum_{j = 0}^\infty \frac{\lambda^j}{j!} \\
 & = \lambda.
\end{align}
$$
The second-to-last equality follows by writing $j = k - 1$.

---