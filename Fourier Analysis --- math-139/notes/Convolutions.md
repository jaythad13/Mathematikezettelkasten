---
tags:
- math-139/4
- math-139/5
- anal
- fourier
---

Convolutions allow one to compute something like a weighted average of a function against another.

##### _definition:_ convolution

Given two $2\pi$ periodic functions $f, g : \mathbb{R} \to \mathbb{C}$, the convolution of $f$ with $g$ is 
$$
f * g(x) = \frac{1}{2 \pi} \int_{- \pi}^\pi f(y) g(y - x)  \, dy 
$$

It's an exercise in change of variables to show that $f * g = g * f$.

##### _example:_ convolving with a characteristic function

Consider $f = \chi_{[-1 / 2, 1/2]}$. Then $f * g$ for any $g$ is
$$
\frac{1}{2\pi} \int_{-\pi}^{\pi} \chi_{[-1 / 2, 1 / 2]} g(y - x) \, dy = \frac{1}{2 \pi} \int_{- 1 / 2}^{1 / 2} g(y - x) \, dy 
$$
Then $(f * g)(x)$ is the average of $g$ on the interval $[x - 1 / 2, x + 1 / 2]$.

##### _example:_ convolving with the [[Fourier Analysis --- math-139/notes/A couple kernels#_definition _ the Dirichlet kernel|Dirichlet kernel]]

Check that
$$
(f * D_{N})(x) = \sum_{n = -N}^N \hat{f}(n) e^{i n x}
$$
the $N$th [[Fourier Analysis --- math-139/notes/Fourier series#_definition _ Fourier series, $N$th partial sum|partial sum]]. Basically, since the Dirichlet kernel looks like the Dirac delta function as $N \to \infty$, the integrals approach the value of the function much like the Fourier series does.

### Properties of convolution

Convolution is a really nice operation. In particular, it turns $2\pi$-periodic integrable functions into a commutative Banach algebra. In addition,

##### _proposition:_ convolutions are continuous

For any integrable functions $f, g : \mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{C}$, the convolution $f * g$ is continuous.

###### _proof:_

[[Fourier Analysis --- math-139/notes/Facts about integration and convergence#_lemma _ integrable functions are approximated by continuous functions|Recall]] that for $f$ integrable (and thus, bounded by $B$) on $[a, b]$, there exists a sequence $\{ f_{n} \}_{n \in \mathbb{N}}$, such that
$$
\lim_{ n \to \infty } \int_{a}^b \lvert f(x) - f_{n}(x) \rvert  \, dx.
$$

Thus, first, we will show that the proposition holds under the additional hypothesis that $f, g$ are continuous. That is, given any $\varepsilon > 0$, we want to give a $\delta > 0$ such that $\lvert x_{1} - x_{2} \rvert < \delta$ forces
$$
\frac{1}{2 \pi} \left\lvert  \int_{-\pi}^\pi f(y) g(x_{1} - y) - f(x) g(x_{2} - y)  \, dy   \right\rvert < \varepsilon.
$$

Since $g$ is continuous on the compact interval $[a, b]$, there is a $\delta > 0$ such that for any $z_{1}, z_{2}$ within $\delta$ of each other, $g(z_{1}), g(z_{2})$ are within $2 \pi \varepsilon / B$ of each other. Now, see that
Note that (by the [[Mathematical Analysis I --- math-131/notes/Properties of the Riemann integral#_proposition _ the triangle inequality for integrals|triangle inequality for integrals]])
$$
\begin{align}
\frac{1}{2 \pi} \left\lvert  \int_{-\pi}^\pi f(y) g(x_{1} - y) - f(x) g(x_{2} - y)  \, dy   \right\rvert & \le \frac{1}{2 \pi} \int_{-\pi}^\pi \lvert f(y) \rvert \lvert g(x_{1} - y) - g(x_{2} - y) \rvert  \, dy \\
 & < \frac{1}{2 \pi} \int_{-\pi}^\pi B \frac{\varepsilon}{B} \, dx  \\
 & \le \frac{1}{2\pi} 2 \pi \epsilon \\
 & = \varepsilon
\end{align}
$$

Now, given $f, g$ integrable and continuous sequences $f_{n} \to f$ and $g_{n} \to g$ (in the $L^1$ norm) it suffices to show that $f_{n} * g_{n} \to f * g$ uniformly (since ). That is, given any $\varepsilon > 0$, we want to show that there exists some $N$ such that for all $n > N$
$$
\lvert (f_{n} * g_{n})(x) - (f * g)(x) \rvert < \varepsilon
$$
at each $x \in [-\pi, \pi]$. The trick here, is to rewrite the left hand side as
$$
\lvert (f_{n} * g_{n})(x) - (f * g_{n})(x) + (f * g_{n})(x) - (f * g)(x) \rvert \leq \lvert (f_{n} * g_{n})(x) - (f * g_{n})(x) \rvert + \lvert (f * g_{n})(x) - (f * g)(x) \rvert 
$$
Then using the fact that

##### _proposition:_ the Fourier transform turns convolution into multiplication

For any integrable functions $f, g : \mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{C}$, the Fourier coefficients of their convolution are the product of the corresponding Fourier coefficients of the functions. That is
$$
\widehat{f * g}(n) = \hat{f}(n) \hat{g}(n)
$$

###### _proof:_

Again, first assume that $f, g$ are continuous. Then the right hand side is just
$$
\begin{align}
\hat{f}(n) \hat{g}(n) & = \left( \frac{1}{2\pi} \int_{-\pi}^\pi f(y) e^{-in y} \, dy  \right) \left( \frac{1}{2\pi} \int_{-\pi}^\pi g(x) e^{-in x} \, dx \right) \\
 & = \frac{1}{2 \pi} \int_{-\pi}^\pi f(y) e^{- in y} \left( \frac{1}{2\pi} \int_{-\pi}^\pi g(x) e^{-i n x} \, dx  \right) \, dy \\
 & = \frac{1}{2\pi} \int_{-\pi}^\pi  f(y) e^{-i n y} \left( \frac{1}{2\pi} \int_{-\pi}^\pi g(x - y) e^{-i n (x - y)} \, dx  \right) \, dy \\
 & = \frac{1}{2\pi} \int_{-\pi}^\pi \frac{1}{2 \pi} e^{-i n x} \int_{-\pi}^\pi f(y) g(x - y) \, dy  \, dx  \\
 & = \widehat{f * g}(x)
\end{align}
$$
Here we use a change of variables in the third equality (we don't need to change the bounds because of $2 \pi$-periodicity), and [[Fourier Analysis --- math-139/notes/Facts about integration and convergence#_theorem _ Fubini's theorem|Fubini's theorem]] in the fourth equality to switch the order of integration.

If $f_{n} \to f$ and $g_{n} \to g$ are continuous sequences converging in the $L^1$ norm, then since $f_{n} * g_{n} \rightrightarrows f * g$ and the Fourier transform is just an integral, we can switch the order of integration and limits to get
$$
\widehat{f * g}(n) = \widehat{\lim_{ k \to \infty } f_{k} * g_{k}(n)} = \lim_{ k \to \infty } \widehat{f_{k} * g_{k}}(n) = \lim_{ k \to \infty } \hat{f_{k}}(n) \hat{g}_{k}(n)
$$
and the limit of the Fourier coefficients is the Fourier coefficient of the limit because the Fourier coefficient is integral based.
