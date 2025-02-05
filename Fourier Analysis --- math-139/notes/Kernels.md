---
tags:
- math-135/3
- math-135/6
- anal
- fourier
---

Due to properties from complex analysis, it's helpful for us to have kernels — families of functions that have higher and higher bumps at $0$, that are in some sense, in the limit, the Dirac delta function.

### The Dirichlet kernel

##### _definition:_ the Dirichlet kernel

For $N \in \mathbb{N}$, the $N$th Dirichlet kernel is the function $D_{N}$ by
$$
D_{N}(x) = \sum_{n = - N}^N e^{i n x}.
$$

##### _lemma:_ the closed form of the Dirichlet kernel

Equivalently
$$
D_{N}(x) = \frac{\sin\left( \frac{2n + 1}{2}  x\right)}{\sin(x / 2)},
$$

Note that $D_{N}$ is the continuous function with
$$
\hat{D}_{N} = \begin{cases}
1 & -N \le n \le N \\
0.
\end{cases}
$$

### The Poisson kernel

##### _definition:_ the Poisson kernel

For $r \in [0, 1)$, Poisson kernel is the function $P_{r} [-\pi, \pi] \to \mathbb{C}$
$$
P_{r}(\theta) = \sum_{n = - \infty}^\infty r^{\lvert n \rvert } e^{i n \theta}.
$$

Since $\sum_{n} r^{\lvert n \rvert}$ converges as a [[Mathematical Analysis I --- math-131/notes/Series#_example _ the geometric series|geometric series]], the rest converges by [[Complex Analysis --- math-135/notes/Analysis and (metric) topology review#_theorem _ Weierstrass $M$-test|Weierstrass]] $M$-test.

##### _lemma:_ the closed form of the Poisson kernel

$$
P_{r}(\theta) = \frac{1 - r^{2}}{1 + r^{2} - 2r \cos\theta}
$$

###### _proof:_

Given $\omega = r e ^{i \theta}$, we can write
$$
\begin{align}
P_{r}(\theta) & = \sum_{n = 0}^\infty \omega^n + \sum_{n = 1}^\infty \overline{\omega}^n \\
 & = \frac{1}{1 - \omega} + \frac{\overline{\omega}}{1 - \overline{\omega}} \\
 & = \frac{1 - \omega \bar{\omega}}{(1 - \omega) (1 - \bar{\omega})} \\
 & = \frac{1 - \lvert \omega \rvert ^{2}}{\lvert 1 - \omega \rvert ^{2}} \\
 & = \frac{1 - r^{2}}{1 + r^{2} - 2 r \cos\theta}
\end{align}
$$
where the denominator in the last line follows by the law of cosines.

We sort of already proved this in [[Complex Analysis --- math-135/attachments/homework/hw 4/hw 4.pdf|complex analysis]].

### Good kernels — approximations of the identity

What makes a good kernel? As we said, it has big bumps at $0$. The reason we want this is that we want a [[Abstract Algebra I --- math-171/notes/Rings#_definition _ ring with identity|multiplicative identity]] for the [[Fourier Analysis --- math-139/notes/Convolutions#_definition _ convolution|convolution]]. This would be the "Dirac delta function" with mass $0$ every where except for mass $1$ at the identity.

##### _definition:_ good kernel

A sequence of functions $\{ K_{n} : \mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{R} \}_{n \in \mathbb{N}}$ is a family of good kernels (or an approximation of the identity) if its integral over the circle is
$$
\frac{1}{2 \pi} \int_{-\pi}^\pi K_{n}(x) \, dx = 1,
$$
the function has uniformly bounded integral (it is $L^1$ bounded by $M$ independently of $n$) and the mass of the function is more concentrated around $0$ as $n \to \infty$. That is, for any $\delta > 0$
$$
\frac{1}{2 \pi} \int_{\lvert x \rvert > \delta}  \lvert K_{n}(x) \rvert  \, dx \to 0.
$$

This really is an approximation to the identity in practice as well —

##### _theorem:_ good kernels act like the identity

Suppose $f : \mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{C}$ is integrable, $\{ K_{n} \}_{n \in \mathbb{N}}$ is a family of good kernels, and $f$ is continuous at $x_{0}$. Then $(f * K_{n})(x_{0}) \to f(x)$ as $n \to \infty$.

If $f$ is continuous everywhere $f * K_{n} \rightrightarrows f$.

###### _proof:_

Suppose $f$ is continuous at $x_{0}$, and fix some $\varepsilon > 0$. We want to bound the difference between the convolution and the function at $x_{0}$. Consider
$$
\begin{align}
\lvert (f * K_{n})(x_{0}) - f(x_{0}) \rvert & = \left\lvert  \frac{1}{2\pi} \int_{- \pi}^\pi K_{n}(y) f(x_{0} - y) \, dy - f(x_{0})   \right\rvert \\
 & = \frac{1}{2 \pi} \left\lvert  \int_{-\pi}^\pi K_{n}(y) f(x_{0} - y)  \, dy - \int_{-\pi}^\pi K_{n}(y) f(x_{0})  \, dy   \right\rvert  \\
 & \le \frac{1}{2 \pi} \left\lvert  \int_{-\pi}^\pi \lvert K_{n}(y) \rvert  \lvert f(x_{0} - y) - f(x_{0}) \rvert  \, dy   \right\rvert 
\end{align}
$$
Splitting this integral into the integrals over $\lvert y \rvert < \delta$ and $\lvert y \rvert > \delta$ allows us to use the $L^1$ boundedness of $K_{n}$ and the continuity of $f$ to bound the first integral and the boundedness of $f$ and the vanishing integral of $K_{n}$ as $n \to 0$ to bound the second integral.

If $f$ is continuous on all of $[-\pi, \pi]$, $f$ is [[Mathematical Analysis I --- math-131/notes/Uniform continuity#_definition _ uniform continuity|uniformly continuous]], and thus, $\delta$ small enough for the difference between $f(x_{0} - y)$ and $f(x_{0})$ to be small doesn't depend on $x_{0}$. Since $n$ only depends on $\delta$, we have uniform convergence.

### Cesaro summability and Abel means

Good kernels are nice because even if the Fourier series itself doesn't recover the function, we can recover the function using good kernels (that also emp). The Dirichlet kernel isn't a good kernel because it isn't $L^1$, so the Fourier coefficients may not be [[Fourier Analysis --- math-139/notes/Fourier series#_corollary _ recovering a continuous function from Fourier series|absolutely summable]], but Cesaro summability, and Abel means

##### _definition:_ Cesaro mean

Given a series $\sum a_{k}$, let $\left\{ \Sigma_{n} = \sum_{k  =1}^n a_{k}  \right\}$ be the sequence of partial sums.

The $n$th Cesaro mean is the mean of the first $n$ partial sums $\Sigma_{n}$, denoted $\sigma_{n}$.

It's a standard exercise in real analysis to show that if a series converges, it's Cesaro means converge to the same thing. The series summing $(-1)^n$ shows that the converse is not true ($\sigma_{n} \to 1 / 2$ but the series does not converge).