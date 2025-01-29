---
tags:
- math-139/3
- anal
---

The $n$th Fourier coefficient of an integrable function is the inner product with the $n$th element of the [[Fourier Analysis --- math-139/notes/Fourier analysis in physics#Superposition of standing waves|orthogonal list]] $e^{2 \pi i n x}$.

##### _definition:_ Fourier coefficient

Given an [[Mathematical Analysis I --- math-131/notes/Riemann integration#_definition _ Riemann integrable|integrable]] function $f : [a, b] \to \mathbb{R}$, the $n$th Fourier coefficient of $f$ is
$$
\hat{f}(n) = \frac{1}{L} \int f(x) e^{-2 \pi i n x / L} \, dx
$$
where $L = b - a$.

The hope is that this data is enough to recover $f$. This isn't always possible — a priori there's no guarantee that the Fourier series will converge, much less to to the original function. (Say, change the function at finitely many points, the Fourier series stays the same, the function is different). However, there are lots of examples where it is.

##### _example:_ an example of convergent Fourier series

For $f : \theta \mapsto \theta(\pi - \theta)$ on $[0, \pi]$, extended to an odd function on $[-\pi, \pi]$ and then a periodic function on all of $\mathbb{R}$, we have
$$
\hat{f}(n) = \begin{cases}
\frac{4}{n^3 \pi i}  & n \text{ is odd} \\
0
\end{cases}
$$
By calculation, one can check that
$$
f(\theta) = \sum_{n \text{ odd}} \frac{4}{n^{3} \pi i} e^{i n x}
$$
almost everywhere.

##### _definition:_ Fourier series, $N$th partial sum

The Fourier series of a (integrable) function $f$ periodic on an interval of length $L$ (if it converges) is
$$
\sum_{n = -\infty}^\infty \hat{f}(n) e^{2 \pi i n x / L}.
$$

The $N$th partial sum is the function $S_{N}f$ with
$$
S_{N}f(x) = \sum_{n = - N}^N \hat{f}(n) e^{2 \pi i n x /L}.
$$

Convergence of the Fourier series is then exactly equivalent to convergence of the partial sums.

We said earlier that the Fourier series cannot recover functions uniquely since you could change functions on a set of [[Calculus --- spivak/notes/Measure#_definition _ measure $0$|measure]] zero without changing their Fourier series. However, when $f$ is continuous, we can! The idea is to show that the only continuous function orthogonal to every element of the orthonormal list of functions $e^{i n x}$.

##### _theorem:_ 

If $f$ is integrable on $[-\pi, \pi]$, $\hat{f}(n) = 0$ for all $n \in \mathbb{Z}$, and $f$ is continuous at $\theta_{0}$, then $f(\theta_{0}) = 0$.

##### _corollary:_

If $f$ is continuous on $[-\pi, \pi]$ and $\hat{f}(n) = 0$ for all $n \in \mathbb{Z}$, then $f$ is identically $0$.

##### _corollary:_

There is a unique continuous function $f$ with Fourier coefficients $\hat{f}(n)$.

