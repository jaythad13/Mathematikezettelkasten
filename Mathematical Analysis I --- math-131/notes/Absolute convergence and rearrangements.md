---
tags:
- math-131/15
- anal
---

Recall the definition of absolute convergence, and that it is a strictly stronger condition than convergence.

![[Mathematical Analysis I --- math-131/notes/Series#_definition, proposition _ absolute convergence, absolute convergence implies convergence.|Series]]

It turns out that the absolute convergence is an even stronger condition than we thought.

### Rearrangements

##### _definition:_ rearrangement

Let $f : \mathbb{N} \to \mathbb{N}$ be a bijection. Then the series $\sum a_{f(n)}$ is a rearrangement of the series $\sum a_{n}$.

##### _theorem:_ non-absolutely convergent series can be rearranged to anything

Let $\sum a_{n}$ be a series that converges but not absolutely. For any $\alpha \le \beta$ in the extended real numbers, there exists a rearrangement $\sum a_{f(n)}$ with partial sums $s_{n}'$ such that
$$
\liminf_{n \to \infty } s_{n}' = \alpha
$$
and
$$
\limsup_{ n \to \infty } s_{n}' = \beta.
$$

###### _proof sketch:_

Notice that if $\sum a_{n}$ converges but not absolutely, then we must have infinitely many positive and negative $a_{n}$. We also must have that the series of negative terms and the series of positive terms both diverge to $\pm \infty$.

Consider sequences $\alpha_{n} \to \alpha$ and $\beta_{n} \to \beta$. Then rearrange first however many positive terms so that their sum exceeds $\beta_{1}$, then arrange negative terms so that the sum of all the terms (the first few positive and these negatives) is less than $\alpha_{1}$, and so on and so forth. We can do this since the positive and negative subseries diverge.

It's clear by choosing alternate partial sums that we have the desired upper and lower limits.



However, if a series converges absolutely, then rearrangements don't matter at all.

##### _theorem:_ absolutely convergent series are invariant under rearrangement

If $\sum a_{n}$ converges absolutely, then $\sum a_{f(n)} = \sum a_{n}$.

###### _proof:_

If $\sum a_{n}$ converges absolutely, then the tail sums of absolute values must go to zero. That is, for all $\varepsilon > 0$, there is some $N$ such that
$$
\sum_{n = m}^M \lvert a_{n} \rvert < \varepsilon.
$$
for all $M \ge m \ge N$

Now choose $n_{0}, \dots, n_{N - 1}$ such that $f(n_{i}) = i$ and let $M' > \max \{ n_{0}, \dots, n_{N - 1} \}$. Now consider the difference of partial sums
$$
\begin{split}
\lvert s_{M'} - s'_{M'} \rvert  & = \left\lvert  \sum_{n = 1}^{M'} a_{n} - \sum_{n = 1}^{M'} a_{f(n)}  \right\rvert \\
 & = \left\lvert  \sum_{n = N}^{M'} a_{n} - \sum_{n \neq n_{i}}^{M'} a_{f(n)}  \right\rvert \\
 & \le \sum_{n = N}^{M'} \lvert a_{n} \rvert  - \sum_{n \neq n_{i}}^{M'} \lvert a_{f(n)} \rvert \\
 & \le \sum_{n = N}^M' \lvert a_{n} \rvert \\
  & < \varepsilon.
\end{split}
$$
for large enough $M'$. Thus, the rearrangement converges to the same value.