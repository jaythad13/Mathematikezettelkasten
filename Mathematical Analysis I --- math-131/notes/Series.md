---
tags:
- math-131/12
- math-131/13
- anal
---

We know what it means for a sequence to converge, now what does it mean for a sum to converge?

##### _definition:_ convergent series

Given a sequence of complex numbers $\{ a_{n} \}_{n}$, we say the series $\sum_{n = 1}^\infty a_{n}$ converges to $S$ if the sequences of partial sums $s_{n} = a_{1} + \dots + a_{n} \to S$.

Note that since $\mathbb{C}$ is a [[Mathematical Analysis I --- math-131/notes/Cauchy sequences#_definition _ completeness|complete metric space]], the sum converges if and only if $\{ s_{n} \}_{n}$ is a [[Mathematical Analysis I --- math-131/notes/Cauchy sequences#_definition _ Cauchy sequence|Cauchy sequence]]. Using this, and other results about convergent sequences, we can get conditions for a series to converge —

##### _proposition:_ absolute convergence implies convergence

If $\sum_{n = 1}^\infty \lvert a_{n} \rvert$ converges, then $\sum_{n = 1}^\infty a_{n}$ converges.

###### _proof:_

Let $\overline{s}_{n}$ be the partial sums of the absolute values and $s_{n}$ be the regular partial sums. If $\sum_{n = 1}^\infty \lvert a_{n} \rvert$ converges, then given any $\varepsilon > 0$, there exists $N$ such that for $N < m < n$, we have $\lvert s_{n} - s_{m} \rvert = \lvert \lvert a_{m + 1} \rvert + \dots + \lvert a_{n} \rvert \rvert < \varepsilon$. Since all of the terms are absolute values (and thus, non-negative), we have $\lvert a_{m + 1} \rvert + \dots + \lvert a_{n} \rvert < \varepsilon$. Thus, by triangle inequality, $\lvert s_{n} - s_{m} \rvert = \lvert a_{m + 1} + \dots + a_{n} \rvert \le \lvert a_{m + 1} \rvert + \dots + \lvert a_{n} \rvert < \varepsilon$. That is, $\{ s_{n} \}_{n}$ is Cauchy, and thus, the series converges.

##### _proposition:_ partials sums of a positive series must be bounded

If $a_{n} \ge 0$ for all $n$ and $\sum_{n = 1}^\infty a_{n}$ converges, then the sequence of partial sums, $\{ s_{n} \}_{n}$ must be bounded.

###### _proof:_

If $a_{n} \ge 0$, then $\{ s_{n} \}_{n}$ is monotonically increasing, and [[Mathematical Analysis I --- math-131/notes/Sequences and convergence#_proposition _ monotonic sequences blow up or converge|thus]], must be bounded in order to converge.

##### _example:_ the geometric series

One very important series is the geometric series $\sum_{n = 0}^\infty x^n$. We can compute this using partial sums. Notice that $s_{n} = 1 + x + \dots + x^n$ and thus, $(1 - x) s_{n} = 1 - x^{n + 1}$. Then we have
$$
\begin{split}
\sum_{n = 0}^\infty x^n & = \lim_{ n \to \infty } s_{n} \\
 & = \lim_{ n \to \infty } \frac{1 - x^{n + 1}}{1 - x} \\
 & = \frac{1 - \lim_{ n \to \infty } x^{n + 1}}{1 - x} \\
 & = \frac{1}{1 - x}.
\end{split}
$$
Here, the last equality follows since the [[Mathematical Analysis I --- math-131/notes/Sequences and convergence#_proposition _ sequences of powers and roots|the limit vanishes]].

### Results for evaluating series

These results turn out to be very useful for evaluating series —

##### _proposition:_ sampling every $2^k$th partial sum

If $\{ a_{n} \}_{n}$ is a monotonically decreasing sequence, then $\sum_{n = 1}^\infty a_{n}$ converges if and only if $\sum_{k = 0}^\infty 2^k a_{2^k}$ converges.

###### _proof:_

Notice that by monotonicity, $a_{2^k} + a_{2^k + 1} + \dots + a_{2^{k + 1} - 1} \le 2^k a_{2^k}$. Also, bounding in the opposite direction, $a_{2^{k - 1} + 1} + a_{2^{k - 1} + 2} + \dots + a_{2^k} \ge 2^{k - 1} a_{2^k}$. Thus, for each partial sum
$$
\frac{1}{2} \sum_{k = 0}^n 2^k a_{2^k} \le \sum_{k = 1}^{2^n} a_{k} \le \sum_{k = 0}^n 2^k a_{2^k}.
$$

Note that since the partials sums of all these series are monotonically increasing, the series converge if and only if their partial sums are bounded. If the partials sums of the sampling series are bounded, then so must be the partial sums of the full series. If the partial sums of the full series are bounded, then so must be the halves partial sums of the sampling series, and thus, the partial sums of the sampling series.

This has a nice application to the zeta function!

##### _example:_ the Riemann zeta function

The series
$$
\zeta(p) = \sum_{n = 1}^\infty \frac{1}{n^p}
$$
converges if and only if $p > 1$. In fact, for complex $p$, we can show that this converges if and only if $\operatorname{Re} p > 1$.

We can show this by noting that $\zeta(p)$ converges if and only if
$$
\sum_{k = 0}^\infty 2^k \frac{1}{(2^k)^p} = \sum_{k = 0}^p (2^{1 - p})^k
$$
converges. As a geometric series, this converges if and only if $2^{1 - p} < 1$. Thus, it converges if and only $p > 1$.

##### _example:_ adding a log $n$ factor

We can also show that the harmonic series, $\sum_{n = 1}^\infty \frac{1}{n}$, which doesn't converge, will converge if we add a small but growing term to the denominator. Specifically, the series
$$
\sum_{n = 2}^\infty \frac{1}{n (\ln n)^p}
$$
converges if and only if
$$
\sum_{k = 1}^\infty \frac{2^k}{2^k (\ln (2^k))^p} = \sum_{k = 1}^\infty \frac{1}{k^p (\ln 2)^p}
$$
converges. But this is just a geometric series which converges for $p > 1$.