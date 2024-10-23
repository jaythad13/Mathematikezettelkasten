---
tags:
- math-135/3
- anal
---

Power series are central to complex analysis because it turns out that every holomorphic function has one! Essentially, any holomorphic function is just an infinite polynomial.

##### _definition:_ power series

Any expansion of the form $\sum_{n \geq 0} a_{n} z^n$ is a power series in $z$ with coefficients $a_{n}$.

Importantly, we can define a radius of convergence for any power series! (It might be zero though).

![[Mathematical Analysis I --- math-131/notes/Power series#_theorem _ every power series has a radius of convergence (Abel)|Power series]]

The theorem that should follow is that the derivative of a convergent power series is the obvious one.

##### _theorem:_ term-by-term differentiation of power series

Suppose $f(z) = \sum_{n \ge 0} a_{n} z^n$. Then
1) $f$ is holomorphic within the radius of convergence.
2) $f'(z) = \sum_{n \ge 0} n a_{n} z^{n - 1}$.
3) $f'$ has the same radius of convergence as $f$.

###### _proof sketch:_

We only really need to prove 2) — the first bit then follows. 3) follows from the root test.

We can split $f$ into a polynomial part $S_{N}(z)$ and a tail part $E_{N}(z)$
$$
f(z) = \sum_{n = 0}^N a_{n} z^n + \sum_{n = N + 1}^\infty a_{n} z^n.
$$
We also write our proposed derivative as $g(z)$. Then, by sneaking in a $S_{N}'(z_{0}) - S_{N}'(z_{0})$ we can write
$$
\begin{split}
\frac{f(z_{0} + h) - f(z_{0})}{h} - g(z_{0}) & = \frac{S_{N}(z_{0} + h) - S_{N}(z_{0})}{h} - S_{N}'(z_{0}) \\
 & + S_{N}'(z_{0}) - g(z_{0}) \\
 & + \frac{E_{N}(z_{0} + h) - E_{N}(z_{0})}{h}
\end{split}
$$
The first two terms converge for obvious reasons for $h$ inside the radius of convergence. In particular, choose $h$ so that $\lvert z_{0} + h \rvert < r< R$. The last term is more complicated. Write it as a difference of squares, then show it is bounded by the tail of the convergent sequence $\sum_{n \ge 0} n a_{n} r^{n - 1}$. Then the tail of convergent series should converge to $0$. Thus, everything converges under taking limits as $N \to \infty$ and $h \to 0$.

Note —

##### _corollary:_ analytic functions are infinitely differentiable

A function defined by a power series is infinitely differentiable on its radius of convergence.