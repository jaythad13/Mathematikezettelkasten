---
tags:
- anal
- fourier
- math-139/10
---

Square convergence in $L^{2}$ doesn't guarantee convergence at any point (we'll see an example soon). However, we can use facts about square convergence to prove pointwise convergence.

##### _theorem:_ pointwise convergence of Fourier series

If $f : \mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{C}$ is integrable and [[Mathematical Analysis I --- math-131/notes/Differentiability#_definition _ differentiability, the derivative|differentiable]] at $x_{0}$, then $S_{N} f (x_{0}) \to f(x_{0})$.

###### _proof:_

We will write the difference $S_{N}f(x_{0}) - f(x_{0})$ in terms of the slope of $f$ near $x_{0}$ and then show that it is a sum of Fourier coefficients which must go to $0$. 

Recall that though the [[Fourier Analysis --- math-139/notes/Kernels#_definition _ the Dirichlet kernel|the Dirichlet kernel]] is not a good kernel, it has integral $2 \pi$. Thus, we can write
$$
\begin{align}
S_{N}f(x_{0}) - f(x_{0}) & = (f * D_{N})(x_{0}) - f(x_{0}) \\
 & = (f * D_{N})(x_{0}) - \frac{1}{2 \pi} \int_{-\pi}^\pi f(x_{0}) D_{N}(t) \, dt \\
 & = \frac{1}{2 \pi} \int_{-\pi}^\pi (f(x_{0} - t) - f(x_{0})) \, D_{N}(t) \, dt.
\end{align}
$$

Consider the negative slope function 
$$
\Delta f(t) = \begin{cases}
\frac{f(x_{0} - t) - f(x_{0})}{t} & t \neq 0, \lvert t \rvert < \pi \\
-f'(x_{0}).
\end{cases}
$$
which is integrable since $f$ is differentiable. (In fact, this is the key step, and holds even if $f$ is just Lipschitz continuous — if $\lvert f(x) - f(x_{0}) \rvert < M \lvert x - x_{0} \rvert$).

Substituting this in gives
$$
S_{N}f(x_{0}) - f(x_{0}) = \frac{1}{2 \pi} \int_{-\pi}^\pi t \Delta f(t) D_{N}(t) \, dt.
$$

Substituting [[Fourier Analysis --- math-139/notes/Kernels#_lemma _ the closed form of the Dirichlet kernel|the closed form of the Dirichlet kernel]] $D_{N}$, we get
$$
S_{N}f(x_{0}) - f(x_{0}) = \frac{1}{2 \pi} \int_{-\pi}^\pi \Delta f(t) \frac{t}{\sin(t / 2)} \left(  \sin(Nt) \cos\left( \frac{t}{2} \right) + \cos(N t) \sin\left( \frac{t}{2} \right) \right)   \, dt.
$$

But this is just
$$
S_{N}f(x_{0}) - f(x_{0}) = \frac{1}{2 \pi} \left( \int_{-\pi}^\pi t \cot(t / 2) \Delta f(t) \sin(N t) \, dt + \int_{-\pi}^\pi t \Delta f(t) \cos(N t) \, dt \right)
$$
which is the sum of two integrals that the [[Fourier Analysis --- math-139/notes/Square convergence of Fourier series#_corollary _ Riemann-Lebesgue lemma|Riemann-Lebesgue lemma]] tells us must go to $0$.

Thus, $S_{N}f(x_{0}) \to f(x_{0})$.

##### _corollary:_ Riemann's localisation principle

If $f, g : \mathbb{R} / 2 \pi \mathbb{Z}$ are integrable with $f = g$ in the neighbourhood of $x_{0}$, then
$$
\lim_{ N \to \infty } S_{N} f(x_{0}) - S_{N}g(x_{0}) = 0
$$

###### _proof sketch:_

$f - g$ is $0$ in a neighbourhood of $x_{0}$ so $(f - g)'(x_{0}) = 0$. Since $f - g$ is differentiable, $S_{N}(f - g) \to f - g =  0$.

This is bizarre because the convergence only depends on behaviour around $x_{0}$. While [[Complex Analysis --- math-135/notes/Cauchy integral formula#_theorem _ identity theorem|the identity theorem]] which is also true for real analytic functions, can be expected since power series are created from local information, the Fourier series is not obtained from local information and it is surprising that its convergence only depends on that.
