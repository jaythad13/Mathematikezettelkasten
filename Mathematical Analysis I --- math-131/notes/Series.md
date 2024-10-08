---
tags:
- math-131/12
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

