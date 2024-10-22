---
tags:
- math-131/15
---

Recall the definition of absolute convergence, and that it is a strictly stronger condition than convergence.

![[Mathematical Analysis I --- math-131/notes/Series#_definition, proposition _ absolute convergence, absolute convergence implies convergence.|Series]]

It turns out that the absolute convergence is an even stronger condition than we thought.

### Rearrangements

##### _definition:_ rearrangement

Let $f : \mathbb{N} \to \mathbb{N}$ be a bijection. Then the series $\sum a_{f(n)}$ is a rearrangement of the series $\sum a_{n}$.

If a series converges absolutely, then rearrangements don't matter at all.

##### _theorem:_ absolutely convergent series are invariant under rearrangement

If $\sum a_{n}$ converges absolutely, then $\sum a_{f(n)} = \sum a_{n}$.

###### _proof:_

First we show that the rearrangement converges. If $\sum a_{n}$ converges absolutely, then the tail sums of absolute values must go to zero. That is, for all $\varepsilon > 0$, there is some $N$ such that
$$
\sum_{n = m}^M \lvert a_{n} \rvert < \varepsilon.
$$
for all $M \ge m \ge N$

Now choose $n_{0}, \dots, n_{N - 1}$ such that $f(n_{i}) = i$ and let $m' = \max \{ n_{0}, \dots, n_{N - 1} \}$. Thus,
$$
\sum_{n = m + 1}^\infty \lvert a_{f(n)} \rvert \le \sum_{n = N}^\infty \lvert a_{n} \rvert < \varepsilon.
$$
since each of the partial sums of the rearrangement's tail contains strictly fewer terms than that on the tail of the original series.

Now suppose the series converged to $L$. We know that the rearrangement converges, so we know it's tail goes to zero. With $m$ as before, note that
$$
\begin{split}
\left\lvert  L - \sum_{n = 0}^{m + 1} a_{f(n)}   \right\rvert & \le \left\lvert  L - \sum_{n = 0}^{N}  \right\rvert
\end{split}
$$

##### _theorem:_ non-absolutely convergent series can be anything


