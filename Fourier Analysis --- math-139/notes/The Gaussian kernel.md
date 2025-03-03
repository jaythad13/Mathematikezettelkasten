---
tags:
- math-139/16
- fourier
- anal
---

We hoped that [[Fourier Analysis --- math-139/notes/The Fourier transform#_definition _ the Fourier transform|the Fourier transform]] contained all the information necessary to recover the original function from it. For the nice enough class of Schwartz functions, this is true!

Just like the [[Fourier Analysis --- math-139/notes/Kernels#_proposition _ the Fejér kernel is a good kernel|Fejér]] and [[Fourier Analysis --- math-139/notes/Kernels#_lemma _ the Poisson kernel is a good kernel (as $r to 1 -$)|Poisson]] kernels are good kernels that recover the function, we will define a good kernel (just on the real line). The definition will be the same, we just integrate over all of $\mathbb{R}$ and don't divide by $2 \pi$. Then convolving against this kernel will recover the original function.

![[Fourier Analysis --- math-139/notes/Kernels#_definition _ good kernel|Kernels]]


##### _definition:_ Gaussian functions

A function $x \mapsto  e^{-a x^{2}}$ is a Gaussian function.

Note that a Gaussian is in [[Fourier Analysis --- math-139/notes/The Fourier transform#The Schwartz space — the nicest functions for Fourier analysis|the Schwartz space]], and $\int_{-\infty}^\infty e^{- \pi x^{2}} \, dx = 1$.

##### _proposition:_ the canonical Gaussian is its own Fourier transform

If $f(x) = e^{- \pi x^{2}}$, its Fourier transform is given by $\hat{f} = f$.

###### _proof:_
has probably been done in some #math-135 homework by contour integration.

##### _definition:_ the Gaussian kernel

For $\delta > 0$, the corresponding Gaussian kernel is given by
$$
K_{\delta}(x) = \frac{1}{\sqrt{ \delta }} e^{- \pi x^{2}/\sqrt{ \delta }}.
$$

##### _proposition:_ Fourier transform of the Gaussian kernel

$$
\hat{K}_{\delta}(\xi) = e^{-\pi \delta \xi^{2}}.
$$

##### _theorem:_ the Gaussian kernel is a good kernel

As $\delta \to 0$, $K_{\delta}$ satisfies the same properties as a good kernel.

###### _proof:_

We've already shown that $\int_{-\infty}^\infty K_{\delta}(x) \, dx = 1$. Since $K_{\delta}$ is positive this also serves as a proof that it is $L^1$ bounded. Thus, we are only left to show that $K_{\delta}$ satisfies concentration of mass.

We want to show that for any $\eta > 0$,
$$
\int_{\lvert x \rvert > \eta} \lvert K_{\delta}(x) \rvert  \, dx \to 0
$$
as $\delta \to 0$.

By change of variables, the integral we want to consider is really
$$
\int_{\lvert y \rvert > \eta / \sqrt{ \delta }} e^{- \pi y^{2}} \, dy
$$
but then as $\delta \to 0$ and since $K_{\delta}$ is rapidly decreasing, the integral goes to zero.

Note that if it were a function, the Dirac delta function would have Fourier transform constant at $1$ everywhere. We can't convolve against it directly with the theory that we have right now, but notice that $\hat{K}_{\delta}(\xi) \to 1$ pointwise as $\delta \to 0$.

Just like when our domain was $\mathbb{R} / 2 \pi \mathbb{Z}$, we can recover functions by convolving with good kernels. First, however, we should define what convolution even means.

##### _definition:_ convolution over $\mathbb{R}$

For $f, g$ in the Schwartz class, their convolution is given by
$$
(f * g)(x) = \int_{-\infty}^\infty f(x - t) g(t) \, dt.
$$
It's a fact that $f * g$ is Schwartz (since $f, g$ are Schwartz). Further, $\widehat{f * g} = \hat{f} \hat{g}$.

##### _corollary:_ convolving with the Gaussian good kernels recovers the function 

Given any $f$ in the Schwartz class,
$$
\lim_{ \delta \to 0^+ } (f * K_{\delta})(x) = f(x)
$$
uniformly.

###### _proof:_
[[Fourier Analysis --- math-139/notes/Kernels#_theorem _ good kernels act like the identity|is very similar to the proof in the bounded case]].

##### _lemma:_ the multiplication formula

For $f, g$ in the Schwartz class
$$
\int_{-\infty}^\infty f(x) \hat{g}(x) \, dx = \int_{-\infty}^\infty \hat{f}(x) g(x) \, dx
$$

###### _proof:_
follows from [[Fourier Analysis --- math-139/notes/Facts about integration and convergence#_theorem _ Fubini's theorem|Fubini's theorem]] — just change the order of integration.