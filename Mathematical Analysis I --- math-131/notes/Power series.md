---
tags:
- math-131/14
- math-131/15
---

What if we want to go from an infinites series into an infinite polynomial? We get power series!

##### _definition:_ power series

Given a sequence $\{ a_{n} \}_{n}$, a power series is the sum
$$
\sum_{n = 0}^\infty a_{n} z^n
$$
which may or may not converge for $z \in \mathbb{C}$.

##### _theorem:_ every power series has a radius of convergence (Abel)

Given any power series $\sum a_{n} z^n$, there exists $R \in [0, \infty]$ such that
- if $\lvert z \rvert < R$, the series converges absolutely (and uniformly)
- if $\lvert z \rvert > R$, the series diverges

###### _proof sketch:_

The [[Mathematical Analysis I --- math-131/notes/Series#_theorem _ the root test|the root test]] gives us that $\limsup_{n \to \infty} \lvert a_{n} z^n \rvert ^{1/n}$ should be less than $1$. That is, $R = 1/\limsup_{n \to \infty} \lvert a_{n} \rvert^{1 / n}$.

##### _example:_ the geometric series

The geometric series is also an example of a power series (with all coefficients $1$). This has radius of convergence $1$.

##### _example:_ the exponential

The series $\sum \frac{z^n}{n!}$ converges on the whole complex plane. We can see this by using the relationship between the root and ratio test to get
$$
\limsup_{n \to \infty} \left( \frac{1}{n!} \right)^{1/n} \leq \limsup_{n \to \infty} \left( \frac{n!}{(n + 1)!} \right) \le 0.
$$

Thus, the radius of convergence is $\infty$.

Now we just want to show that the coefficients of a power series do indeed define unique power series.

##### _theorem:_ power series are determined by their coefficients

Suppose $\sum a_{n} z^n = 0$ for all $z$ in its radius of convergence. Then all coefficients $a_{n} = 0$.

###### _proof:_

Suppose by way of contradiction that the power series is identically zero, but there exist non-zero coefficients. Choose $m$ to be the smallest $n$ such that $a_{n} \neq 0$. Then
$$
a_{m} z^m + \sum_{n = m + 1}^\infty a_{n} z^n = 0
$$
and thus,
$$
a_{m} z^{m} + z^{m + 1} \sum_{n = 0}^\infty a_{n + m + 1} z^n = 0.
$$
That is, we have
$$
a_{m} = -z \sum_{n = 0}^\infty a_{n + m + 1} z^n
$$
But note that this second series also converges in the same ball —
$$
\limsup_{n \to \infty} \lvert a_{n + m + 1} \rvert ^{1/n} = \limsup_{ n \to \infty } (\lvert a_{n + m + 1} \rvert^{1/(n + m + 1)})^{({n + m + 1})/{n}} = \limsup_{ n \to \infty } (\lvert a_{n + m + 1} \rvert ^{1/(n + m + 1)}). 
$$
Now we can bound $a_{m}$.

##### _corollary:_

$\sum a_{n} z^n = \sum b_{n} z^n$ if and only if $a_{n} = b_{n}$ for each $n$.**