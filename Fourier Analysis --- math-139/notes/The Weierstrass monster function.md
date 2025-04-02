---
tags:
- math-139/14
- fourier
- anal
---

> An outrage against common sense

\- Henri Poincaré

It's easy to construct a continuous everywhere function that is not differentiable at some particular point — $\lvert x \rvert$ is one such example. One can even get the function not differentiable on a set of [[Calculus --- spivak/notes/Measure#_definition _ measure $0$|measure zero]]. However, for a long time it was suspected that a continuous everywhere function must be differentiable. Weierstrass showed this is not true.

By constructing a "lacunary" Fourier series where there are large gaps in frequencies, Weierstrass constructed a function with fractal structure. The function is continuous everywhere, but also has spikes (like those of the absolute value function) everywhere, and thus, is differentiable nowhere.

##### _theorem:_ the Weierstrass monster function

For $\alpha \in (0, 1)$
$$
f_{\alpha}(x) = \sum_{n = 0}^\infty 2^{-n \alpha} e^{i 2^n x}
$$
is continuous everywhere but [[Mathematical Analysis I --- math-131/notes/Differentiability#_definition _ differentiability, the derivative|differentiable]] nowhere.

It's clear that this is continuous — since the Fourier coefficients $2^{- n \alpha}$ are [[Fourier Analysis --- math-139/notes/Fourier series#_corollary _ absolutely summable Fourier series recover continuous functions|absolutely summable]], they recover a continuous function.

To prove that this really is not differentiable requires a new [[Fourier Analysis --- math-139/notes/Kernels|kernel]].

### Delayed means

The delayed means "delay" the convergence of convolution with [[Fourier Analysis --- math-139/notes/Kernels#_definition _ Fejér kernel|the Fejér kernel]].

##### _definition:_ delayed means

The $N$th delayed mean of a function $g$ is
$$
\Delta_{N}g = 2 g * F_{2N} - g * F_{N}.
$$

By the [[Fourier Analysis --- math-139/notes/Kernels#_proposition _ the Fejér kernel is a good kernel|good kernel]] convergence of the (convolution with) the Fejér kernel, $\Delta_{N}$ has the same convergence properties.

If the Fejér kernel corresponds to multiplying Fourier coefficients by a decreasing slope that gets flatter as $N \to \infty$, the delayed mean corresponds to multiplying by a trapezoid-shaped function that gets longer and flatter as $N \to \infty$.

##### _proposition:_ Fourier coefficients of the delayed mean

$$
\widehat{\Delta_{N}g} = \begin{cases}
\hat{g}(n) & \lvert n \rvert \le N \\
2 \hat{g}(n) \left( 1 - \frac{\lvert n \rvert }{2 N} \right) & N \le \lvert n \rvert  \le 2 N \\
0 & \lvert n \rvert > 2N.
\end{cases}
$$

### Back to the monster

Our goal is to analyse the growth of the derivative of the difference of the delayed means of $f_{\alpha}$. We will show this is polynomial in $N$ for $f_{\alpha}$, but that for differentiable functions, the growth should be bounded by $\log n$ for differentiable functions.

##### _proposition:_ the growth of the derivative of the difference of delayed means

The growth of $\Delta_{2N}f_{\alpha}'(x_{0}) - \Delta_{N}f_{\alpha}'(x_{0})$ is as $C N^{1 - \alpha}$.

###### _proof sketch:_

Choose $2N = 2^n$, and thus, $N = 2^{n - 1}$. Then $(\Delta_{2N}f_{\alpha} - \Delta_{N}f_{\alpha})(x) = 2^{- n \alpha} e^{i 2^n x}$. This has derivative
$$
(\Delta_{2N}f_{\alpha} - \Delta_{N}f_{\alpha})'(x_{0}) = i (2^{n})^{1 - \alpha} e^{i 2^n x} = i N^{1 - \alpha} e^{i 2^n x}
$$
which grows at least as fast as $N^{1 - \alpha}$. This is faster than $\log N$.

##### _theorem:_ the growth of derivatives of Cesàro means of a differentiable function

If $g : \mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{R}$ is continuous and differentiable at $x_{0}$, then
$$
(F_{N} *g)'(x_{0}) = O(\log N).
$$

###### _proof:_

We can move the differentiability into the integral and use [[Fourier Analysis --- math-139/notes/Convolutions#Properties of convolution|commutativity of convolution]] to get
$$
(F_{N} * g)'(x_{0}) = \int_{-\pi}^\pi F_{N}'(x_{0} - t) g(t) \, dt = \int_{-\pi}^\pi F_{N}'(t) g(x_{0} - t) \, dt
$$
Since
$$
\int_{-\pi}^\pi F_{N}'(t) \, dt = F_{N}(\pi) - F_{N}(-\pi)
$$
and $F_{N}$ is $2 \pi$-periodic, we can slide in the integral of $F_{N}'$ times any constant. That is, we can rewrite
$$
(F_{N} * g)'(x_{0}) = \int_{-\pi}^\pi F_{N}'(t) g(x_{0} - t) \, dt - g(x_{0}) \int_{-\pi}^\pi F_{N}(t) \, dt  = \int_{-\pi}^\pi F_{N}'(t)(g(x_{0} - t) - g(x_{0})) \, dt.
$$

Since $g$ is differentiable at $x_{0}$, there is some $\delta$ such that for $\lvert t \rvert < \delta$, the difference looks like the derivative times $\lvert t \rvert$ — $\lvert g(x_{0} - t) - g(x_{0}) \rvert \le C \lvert t \rvert$.  For $\delta < \lvert t \rvert$ we can bound the difference by twice the maximum of of $g$. Thus,
$$
\left\lvert  \int_{-\pi}^\pi F_{N}'(t) (g(x_{0} - t) - g(x_{0})) \, dt  \right\rvert  \le C \int_{-\pi}^\pi F_{N}'(t) \lvert t \rvert  \, dt.
$$

By bounding the integral near and away from $t = 0$, and using the fact that $\lvert F_{N}'(t) \rvert \le A N^{2}$ and $\lvert F_{N}'(t) \rvert \le A / \lvert t \rvert^{2}$ (the first bound is easy the second bound is harder) we get the desired $\log N$ bound —
$$
\begin{align}
\lvert (F_{N} * g)'(x_{0}) \rvert & \le C \int_{\lvert t \rvert \ge 1 / N} \lvert F'_{N}(t) \rvert \lvert t \rvert  \, dt + C \int_{\lvert t \rvert  \le 1 / N} \lvert F'_{N}(t) \rvert \lvert t \rvert  \, dt  \\
 & \le C A \int_{\lvert t \rvert  \ge 1 / N} \, \frac{dt}{\lvert t \rvert } + C A N \int_{\lvert t \rvert  \leq 1 / N} \, dt  \\
 & = O(\log N) + O(1) \\
 & = O(\log N).
\end{align}
$$

Note that this forces $(\Delta_{N}g)'(x_{0})$ to also grow like $\log N$ at $x_{0}$. Thus, $f_{\alpha}$ cannot be differentiable.

By the [[Calculus --- spivak/notes/Differentiability theorems#_theorem _ the projection principle holds for differentiability|the projection principle]], the real and complex parts of $f_{\alpha}$ also satisfy the same properties — specifically,
$$
\sum_{n = 0}^\infty 2^{-n \alpha} \cos(2^n x)
$$
is continuous everywhere and and differentiable nowhere.