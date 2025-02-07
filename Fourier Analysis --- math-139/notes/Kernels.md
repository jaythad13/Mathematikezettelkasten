---
tags:
- math-139/3
- math-139/6
- math-139/7
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

Good kernels are nice because even if the Fourier series itself doesn't recover the function, we can recover the function using good kernels (that also emp). The Dirichlet kernel isn't a good kernel because it isn't $L^1$, so the Fourier coefficients may not be [[Fourier Analysis --- math-139/notes/Fourier series#_corollary _ recovering a continuous function from Fourier series|absolutely summable]], but Cesaro summability and Abel means provide a way to get around this.

##### _definition:_ Cesaro mean

Given a series $\sum a_{n}$, let $\left\{ \Sigma_{N} = \sum_{n  = 1}^N a_{n}  \right\}$ be the sequence of partial sums.

The $n$th Cesaro mean is the mean of the first $n$ partial sums $\Sigma_{N}$, denoted $\sigma_{N}$.

It's a standard exercise in real analysis to show that if a series converges, it's Cesaro means converge to the same thing. The series summing $(-1)^n$ shows that the converse is not true ($\sigma_{n} \to 1 / 2$ but the series does not converge). That's essentially why this is useful — the idea of the Fejér kernel is to consider the Cesaro means of the partial sums of the Fourier series — we consider $f * \frac{1}{N} \sum_{k = 0}^{N - 1} D_{n}$.

##### _definition:_ Fejér kernel

The $N$th Fejér kernel $F_{N}$ is a function $\mathbb{R} \to \mathbb{R}$ given by
$$
F_{N}(x) = \frac{1}{N} \sum_{n = 1}^N D_{n}(x).
$$

This is a good kernel! As a result, $(f * F_{N})(x) \to f(x)$ as $N \to \infty$.

##### _lemma:_ the closed form of the Fejér kernel

$$
F_{N}(x) = \frac{1}{N} \frac{\sin ^{2}\left( Nx / 2 \right)}{\sin ^{2}(x / 2)}.
$$

###### _proof:_
is left to the homework.

##### _proposition:_ the Fejér kernel is a good kernel

###### _proof:_

By the closed form, $F_{N}$ is positive, so if we show that $F_{N}$ has integral $1$ over $\mathbb{R} / 2 \pi \mathbb{Z}$, we simultaneously show it is $L^1$. Since each $D_{n}$ has integral $1$ over $\mathbb{R} / 2\pi \mathbb{Z}$ (the integrals of positive and negative characters cancel) and $F_{N}$ is their average, $F_{N}$ also has integral $1$ on the circle.

Since $\sin ^{2}(Nx / 2) \le 1$ and $\sin ^{2}(x / 2)$ increases away from the origin (and thus, $\lvert x \rvert > \delta$ gives $\sin ^{2}(x / 2) \ge \sin ^{2}(\delta / 2)$ for any $\delta > 0$), we have the bound
$$
F_{N}(x) \le \frac{1}{N} \frac{1}{\sin ^{2}(\delta / 2)}
$$
for $x$ with $\lvert x \rvert > \delta$. Thus, as $N \to \infty$, $F_{N} \to 0$ outside $[-\delta, \delta]$.

##### _corollary:_ Fejér kernels recover continuous functions

Any continuous function on the circle can be uniformly approximated by trigonometric polynomials.

###### _proof:_

$f * F_{N}$ is a trigonometric polynomial.

Abel means use the convergence of a [[Mathematical Analysis I --- math-131/notes/Power series|power series]] to verify summability. Recall that for a power series with coefficients $a_{n}$ to converge on radius $1$ we only need $\limsup \lvert a_{n} \rvert^{1 / n}$ to be less than $1$.  This is even weaker than Cesaro summability (for example $\sum_{n} (-1)^n (n + 1)$ is Abel summable but not Cesaro summable).

##### _definition:_ Abel mean, Abel summability

Given a series $\sum a_{n}$, the Abel sum is
$$
A(r) = \sum_{n = 0}^\infty a_{n} r^n
$$

If $A(r)$ converges for each non-negative $r < 1$, and $\lim_{ r \to 1 } A(r) = s$, we say $\sum a_{n}$ is summable to $s$.

Given an integrable function, we do this

##### _definition:_ Abel mean of a Fourier series

Given an integrable function $f$ with $\hat{f}(n) = a_{n}$, the Abel mean of $f$ is $A_{r}f$ given by
$$
A_r f(x) = \sum_{n = -\infty}^\infty a_{n} r^{\lvert n \rvert } e^{i n x}
$$

##### _lemma:_ the Abel mean is convolution with the Poisson kernel

$$
A_{r} f (x) = (f * P_{r})(x)
$$

###### _proof sketch:_

They have the same (absolutely summable) Fourier coefficients (the convolution of $f * P_{r}$ has coefficients that are the [[Fourier Analysis --- math-139/notes/Convolutions#_proposition _ the Fourier transform turns convolution into multiplication|product]] $\hat{f}(n) \hat{P_{r}}(n)$). Since they are continuous and  absolutely summable, [[Fourier Analysis --- math-139/notes/Fourier series#_corollary _ recovering a continuous function from Fourier series|the functions are recovered from the Fourier coefficients]].