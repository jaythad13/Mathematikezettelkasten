---
tags:
- math-139/8
- fourier
- anal
---

The Dirichlet problem asks for a function $u : \mathbb{R}^{2} \to \mathbb{R}$ that is harmonic inside the unit disc $\mathbb{D}$ with some boundary condition $u = f$ on $\partial \mathbb{D}$. We might conjecture that all solutions are of the form
$$
u(r, \theta) = \sum_{n = -\infty}^\infty \hat{f}(n) r^{\lvert n \rvert } e^{i n \theta}.
$$

##### _theorem:_ the solution to the Dirichlet problem

Let $f : \mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{R}$ be an integrable function. Then $u: \mathbb{R}^{2} \to \mathbb{R}$ given by
$$
u(r, \theta) = f * P_{r}(\theta)
$$
is the [[Fourier analysis --- math-139/notes/Kernels#The Poisson kernel|Poisson integral]] of $f$ and solves the heat equation on the disc. That is, $\Delta u = 0$ on $\mathbb{D}$ and $\lim_{ r \to 1^- } u(r, \theta) = f(\theta)$ so $u$ can be extended to a continuous function that equals $f$ on $\partial \mathbb{D}$. If $f$ is continuous everywhere the convergence is uniform.

Further, if $f$ is continuous $u$ is the unique (twice-differentiable) solution of the heat equation.

###### _proof:_

Since $f$ is integrable, the Poisson integral of $f$ converges absolutely and uniformly on each disc of radius $r < 1$. In fact, so do the derivatives of the partial sums. Thus, we can interchange the infinite sum and differentiation (with respect to $r$ and $\theta$ both). That is, we can take derivatives term by term.

Recall the [[Fourier analysis --- math-139/attachments/homework/hw 2/hw 2.pdf#page=1|polar form of the Laplacian]] 
$$
\begin{align}
\Delta u & = \frac{ \partial^{2} u }{ \partial r^{2} } + \frac{1}{r} \frac{ \partial u }{ \partial r } + \frac{1}{r^{2}} \frac{ \partial^{2} u }{ \partial \theta^{2} } \\
& = \sum_{n = - \infty}^\infty \lvert  n \rvert (\lvert n \rvert  - 1) r^{\lvert n \rvert - 2} e^{i n \theta} + \frac{1}{r} \lvert n \rvert  r^{\lvert n \rvert - 1} e^{i n \theta} + \frac{1}{r^{2}} r^{\lvert n \rvert } (-n^{2}) e^{i n \theta} \\
 & = \sum_{n = -\infty}^\infty 0 \\
 & = 0.
\end{align}
$$

Since the [[Fourier analysis --- math-139/notes/Kernels#_lemma _ the Poisson kernel is a good kernel (as $r to 1 -$)|the Poisson kernel is a good kernel]] it's just true that as $r \to 1$, $u(r, \theta) \to f(\theta)$, and if $f$ is continuous $u(r, \theta) \rightrightarrows f(\theta)$.

Suppose $v$ is a different $\mathcal{C}^2$ harmonic function converging to $f$. [[Fourier analysis --- math-139/notes/Fourier series#_proposition _ $ mathcal{C} 2$ functions have absolutely summable coefficients|Since it is twice differentiable]] it is recovered by its Fourier series on each circle of radius $r$. That is, we can say
$$
v(r, \theta) = \sum_{n = -\infty}^\infty a_{n}(r) e^{i n \theta}
$$
where each
$$
a_{n}(r) = \frac{1}{2 \pi} \int_{-\pi}^\pi v(r, \theta) e^{-i n \theta} \, d\theta.
$$

Since $\Delta v = 0$, we have $\widehat{\Delta v_{r}}(n) = 0$ for each $n$ and each $r$. By the Leibniz differentiation rule, we can pull the Laplacian out to get $\Delta \hat{v}_{r}(n) = 0$. That is, $\Delta a_{n} = 0$ —
$$
a_{n}''(r) + \frac{1}{r} a'_{n} - \frac{n^{2}}{r^{2}} a_{n} = 0
$$
For all $n > 0$, this gives
$$
a_{n}(r) = A_{n} r^n + B_{n} r^{-n}.
$$
If $B_{n} \neq 0$, then $a_{n}$ would not be bounded, which contradicts what we know from it being the result of an integral. Thus, $a_{n} = A_{n} r^n$
$$
A_{n} = \lim_{ r \to 1^- } \widehat{v_{r}}(\theta)
$$
and since $v_{r} \rightrightarrows f$ as $r \to 1$, we can interchange the Fourier coefficient with the limit of $v_{r}$, giving us $A_{n} = \hat{f}(n)$. This forces $a_{n} = \hat{f}(n) r^{n}$ as desired. Arguing similarly for $n \le 0$ we get the similar fact.