---
tags:
- math-139/3
- math-139/4
- anal
- fourier
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

### Uniqueness

We said earlier that the Fourier series cannot recover functions uniquely since you could change functions on a set of [[Calculus --- spivak/notes/Measure#_definition _ measure $0$|measure]] zero without changing their Fourier series. However, when $f$ is continuous, we can! The idea is to show that the only continuous function orthogonal to every element of the orthonormal list of functions $e^{i n x}$.

##### _theorem:_ vanishing Fourier series implies vanishing at continuous points

If $f$ is integrable on $[-\pi, \pi]$, $\hat{f}(n) = 0$ for all $n \in \mathbb{Z}$, and $f$ is continuous at $\theta_{0}$, then $f(\theta_{0}) = 0$.

###### _proof:_

Without loss of generality, assume $\theta_{0} = 0$, and suppose by way of contradiction that $f(0) > 0$. By continuity, $f(x) > f(x)/2 > 0$ in some neighbourhood $(-\delta, \delta)$.

Since $\hat{f} = 0$, we should have $f$ orthogonal to all trigonometric polynomials (finite linear combinations of $e^{i n x}$). We will create a sequence where this is not true. Consider first
$$
p(x) = \cos (x) + \varepsilon
$$
where $\varepsilon$ is chosen so that outside $(-\delta, \delta)$ in $[-\pi, \pi]$ we have $\lvert p(x) \rvert < 1 - \varepsilon / 2$. This means that after bumping a cosine up by $\varepsilon$, $p$ is still not too big. By the continuity of $\cos$, we can choose some $\eta < \delta$ so that within $(-\eta, \eta)$, the polynomial is still bigger than $1$. In particular $\lvert p(x) \rvert > 1 + \varepsilon / 2$.

Consider now all $p_{k} = p^k$. We can try to estimate the integral of $f$ against $p_{k}$ as $k \to \infty$. Inside $(- \eta, \eta)$ the integral blows up (use the lower bound $f > f(0) / 2$), outside $(-\delta, \delta)$ the integral goes to $0$, and between the two intervals, $f$ is positive. Thus, as $k \to \infty$ the integral blows up on $[-\pi, \pi]$.

This means that $\hat{f}$ cannot be $0$ ($p$ is the real part of $e^{i k x}$ which we have to integrate against).

##### _corollary:_ vanishing Fourier series implies vanishing continuous function

If $f$ is continuous on $[-\pi, \pi]$ and $\hat{f}(n) = 0$ for all $n \in \mathbb{Z}$, then $f$ is identically $0$.

##### _corollary:_ each Fourier series comes from a unique continuous function

There is a unique continuous function $f$ with Fourier coefficients $\hat{f}(n)$.

From what we've just proved, we can even get that (continuous) $f$ are recovered from Fourier series.

##### _corollary:_ recovering a continuous function from Fourier series

For a continuous $f : [-\pi, \pi] \to \mathbb{C}$ with $\sum \lvert \hat{f}(n) \rvert < \infty$, the Fourier series $\sum_{n \in \mathbb{Z}} \hat{f}(n) e^{i n x}$ converges uniformly to $f$.

###### _proof:_

By [[Complex Analysis --- math-135/notes/Analysis and (metric) topology review#_theorem _ Weierstrass $M$-test|Weierstrass]]' $M$-test the Fourier series converges uniformly. Since each of the function is continuous, they converge uniformly to a continuous function. This function must have the same Fourier series as $f$ so it is just $f$.

This raises the question of when it is true that $\sum \lvert \hat{f}(n) \rvert < \infty$. One answer is the [[Complex Analysis --- math-135/notes/Fourier analysis and holomorphic functions#_theorem _ the Poisson summation formula|Poisson summation formula]]. However, we can get a more analytic flavour of answer.

##### _proposition:_ $\mathcal{C}^2$ functions have absolutely summable coefficients

If $f : [-\pi, \pi] \to \mathbb{C}$ is twice continuously differentiable, then $\hat{f}(n) = O(1/n^{2})$. That is, there exists a positive constant $C$ with $\lim_{ x \to \infty } n^{2} \hat{f}(n) \le C$.

###### _proof:_

We can use [[Mathematical Analysis I --- math-131/notes/Fundamental theorem of calculus#_corollary _ integration by parts|integration by parts]]. We can write
$$
\begin{align}
2 \pi \hat{f}(n) & = \int_{-\pi}^{\pi} f(x) e^{-i n x} \, dx \\
 & =  \\
 & = 0 + \frac{-1}{n^{2}} \int f''(x) e^{- i n x} \, dx 
\end{align}
$$

In fact, a stronger result holds — we only need Holder continuity of order $\alpha > 1 / 2$ for Fourier coefficients to converge absolutely.