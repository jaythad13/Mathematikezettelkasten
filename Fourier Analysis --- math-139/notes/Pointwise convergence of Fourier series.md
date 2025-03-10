---
tags:
- anal
- fourier
- math-139/10
- math-139/11
---

Square convergence in $L^{2}$ doesn't guarantee convergence at any point (we'll see an example soon). However, we can use facts about square convergence to prove pointwise convergence for differentiable functions

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
which is the sum of two integrals that the [[Fourier Analysis --- math-139/notes/Square convergence of Fourier series#_corollary _ Riemann-Lebesgue lemma|Riemann-Lebesgue lemma]] tells us must go to $0$ as $N \to \infty$.

Thus, $S_{N}f(x_{0}) \to f(x_{0})$.

##### _corollary:_ Riemann's localisation principle

If $f, g : \mathbb{R} / 2 \pi \mathbb{Z}$ are integrable with $f = g$ in the neighbourhood of $x_{0}$, then
$$
\lim_{ N \to \infty } S_{N} f(x_{0}) - S_{N}g(x_{0}) = 0
$$

###### _proof sketch:_

$f - g$ is $0$ in a neighbourhood of $x_{0}$ so $(f - g)'(x_{0}) = 0$. Since $f - g$ is differentiable, $S_{N}(f - g) \to f - g =  0$.

This is bizarre because the convergence only depends on behaviour around $x_{0}$. While [[Complex Analysis --- math-135/notes/Cauchy integral formula#_theorem _ identity theorem|the identity theorem]] which is also true for real analytic functions, can be expected since power series are created from local information, the Fourier series is not obtained from local information and it is surprising that its convergence only depends on that.

### Fourier series of continuous functions need not converge

We might hope that we can extend this to convergence of the Fourier series for all continuous functions, but we can't. There is a counterexample. Recall the sawtooth function from [[Fourier Analysis --- math-139/attachments/homework/hw 2/hw 2.pdf|the second homework]]. It's a non-continuous function that has Fourier series $\sum_{n \neq 0} \frac{e^{i n x}}{n}$ everywhere. By breaking this into two sums, we can break the Fourier series

##### _lemma:_ sufficient condiitons for bounded partial sums

Suppose $\sum c_{n}$ is an infinite series with bounded [[Fourier Analysis --- math-139/notes/Kernels#_definition _ Abel mean, Abel summability|Abel means]] as $r \to 1$ (which implies $c_{n} = O(1 / n)$). Then the partial sum sequence $S_{N} = \sum_{n = 1}^N c_{n}$ is bounded.

###### _proof sketch:_

Consider 
$$
\lvert S_{N} - A_{r} \rvert = \left\lvert  \sum_{n = 1}^N c_{n} - \sum_{n = 1}^N c_{n} r^n - \sum_{n = N + 1}^\infty c_{n} r^n  \right\rvert = \left\lvert  \sum_{n = 1}^N c_{n} (1 - r^n) + \sum_{n = N + 1}^\infty c_{n} r^n  \right\rvert .
$$

Using the partial sums of the geometric series and the fact that $r \leq 1$, we get $(1 - r^n) < n(1 - r)$. Thus,
$$
\lvert S_{N} - A_{r} \rvert \le \sum_{n = 1}^{N} n \lvert c_{n} \rvert \lvert 1 - r \rvert + \sum_{n = N + 1}^\infty \lvert c_{n}  \rvert \lvert r \rvert ^n
$$

Since $c_{n} = O(1 / n)$, $n \lvert c_{n} \rvert \le M$ for some bound $M$, and for $n \ge N + 1$, $\lvert c_{n} \rvert \le M / N$. Thus, for each $r$
$$
\lvert S_{N} - A_{r} \rvert \le M N(1 - r) + \frac{M}{N} \sum_{N + 1}^\infty r^n \le M N(1 - r) + \frac{M}{N} \frac{1}{1 - r}
$$

Choosing $r = 1 - 1 /N$ minimises this expression, to give $2 M$. As $N \to \infty$, $r \to 1$ where we know $A_{r}$ is bounded. Since the distance between it and $S_{N}$ is bounded, we know $S_{N}$ is bounded.

Since the Abel means of the Fourier series, are just the Abel means of the sawtooth function, which is bounded, the Abel means of the Fourier series are bounded. Thus, we have that $f_{N}(x) = \sum_{1 \le \lvert n \rvert \le N} \frac{e^{i n x}}{n}$ is uniformly (since the bound is only in terms of $n$) bounded.

Consider also $\tilde{f}_{N}(x) = \sum_{n = -1}^{-N} \frac{e^{i n x}}{n}$. It's easy to see (by the integral test) that this is greater than $c \log N$. We can use this to force the 

We will shift the "frequencies" of these functions — we write $P_{N}(x) = e^{i 2 N x} f_{N}(x)$ and $\tilde{P}_{N} = e^{i 2 N x} \tilde{f}_{N}(x)$. Note that chopping the sum that defines $P_{N}(x)$ in half just gives us $\tilde{P}_{N}(x)$.

We choose a positive convergent series $\sum \alpha_{k}$ and we choose a sequence $\{ N_{k} \}$ such that $N_{k + 1} > 3 N_{k}$ and $\lim_{ k \to \infty } \alpha_{k} \log N_{k} \to \infty$. Now let
$$
f(x) = \sum_{k = 1}^\infty \alpha_{k} P_{N_{k}}(x)
$$
We use $S_{M}$ to denote chopping the defining sums of the function (as if taking a partial sum of the whole series). We claim $\lvert S_{2 N_{m}}f(0) \rvert \ge c \alpha_{m} \log N_{m} + O(1)$. This follows by breaking the sum into parts where the chopped frequencies agree and don't. Thus, the partial sums of the Fourier series diverge at $0$.
