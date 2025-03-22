---
tags:
- math-139/17
- fourier
- anal
---

The Fourier inversion formula answers our wishes with a way to convert the data of the Fourier transform of a (nice) function back into the data of the original function. Along the way we get nice identities!

### The Fourier inversion formula

It will be useful to know that the Fourier transform is [[Linear algebra done right --- ladr/notes/Self-adjoint operators#_definition _ self-adjoint operator|self-adjoint]] — that $\langle \hat{f}, g \rangle = \left< f, \hat{g} \right>$.

##### _lemma:_ the multiplication formula

For $f, g$ in the Schwartz class
$$
\int_{-\infty}^\infty f(x) \hat{g}(x) \, dx = \int_{-\infty}^\infty \hat{f}(x) g(x) \, dx
$$

###### _proof:_
follows from [[Fourier Analysis --- math-139/notes/Facts about integration and convergence#_theorem _ Fubini's theorem|Fubini's theorem]] — just expand and change the order of integration.

##### _theorem:_ the Fourier inversion formula

For any [[Fourier Analysis --- math-139/notes/The Fourier transform#_definition _ Schwartz class, $ mathcal{S}( mathbb{R})$|Schwartz function]] $f : \mathbb{R} \to \mathbb{C}$, and any $x \in \mathbb{R}$
$$
f(x) = \int_{-\infty}^\infty \hat{f}(\xi) e^{2 \pi i x \xi} \, d\xi.
$$

###### _proof:_

Note that we can use the duality of [[Fourier Analysis --- math-139/notes/The Fourier transform#_proposition _ translation is dual to modulation|translation and modulation]] to reduce this to proving the case $x = 0$. For $g : a \mapsto f(a + x)$, we can use
$$
f(x) = g(0) = \int_{-\infty}^\infty \hat{g}(\xi)  \, d\xi = \int_{-\infty}^\infty \hat{f}(\xi) e^{2 \pi i (0 + x) \xi}\, d\xi.
$$

Thus, now we are only left to show that
$$
f(0) = \int_{-\infty}^\infty \hat{f}(\xi) \, d\xi.
$$
We can use the [[Fourier Analysis --- math-139/notes/The Gaussian kernel#_theorem _ the Gaussian kernel is a good kernel|Gaussian good kernel]] to prove this. By the fact of the Gaussian kernel being a good kernel, the left hand side is just $\lim_{ \delta \to 0^+ } (f * K_{\delta})(0)$. Since the Gaussian kernel is just $e^{- \pi x^{2}}$ dilated by $\delta$, there is some $G_{\delta} : \mathbb{R} \to \mathbb{C}$ with $\hat{G}_{\delta} = K_{\delta}$ (using the duality of [[Fourier Analysis --- math-139/notes/The Fourier transform#_proposition _ dilation is dual to scaling|scaling and dilation]], we get $G_{\delta}(x) = e^{- \pi \delta x^{2}}$). Thus, by the multiplication formula, we have
$$
f(0) = \lim_{ \delta \to 0 } \int_{-\infty}^\infty f(x) K_{\delta}(x) \, dx = \lim_{ \delta \to 0 } \int_{\infty}^\infty \hat{f}(x) e^{- \pi \delta x^{2}} \, dx.
$$
We can split the difference of the right hand side and the desired integral $\int_{-\infty}^\infty \hat{f}(\xi) \, d\xi$ into two parts — one where $\hat{f}$ is small (by virtue of being Schwartz) and one over a bounded interval where $e^{-\pi \delta x^{2}}$ can be forced to be close to $1$ by small $\delta$ regardless of $x$. We get
$$
\lim_{ \delta \to 0 } \int_{\infty}^\infty \hat{f}(x) e^{- \pi \delta x^{2}} \, dx = \int_{-\infty}^\infty \hat{f}(\xi) \, d\xi.
$$
This gives us the desired result.

##### _definition:_ inverse Fourier transform

Given a Schwartz function $f : \mathbb{R} \to \mathbb{C}$, the inverse Fourier transform of $f$ is the function $\check{f} : \mathbb{R} \to \mathbb{C}$ by
$$
\check f(x) = \int_{-\infty}^\infty f(\xi) e^{2 \pi i x \xi} \, d\xi.
$$

### Consequences ...

Plancherel's theorem is the analogue of [[Fourier Analysis --- math-139/notes/Square convergence of Fourier series#_corollary _ Parseval's identity|Parseval's identity]].

##### _theorem:_ Plancherel's theorem

For a Schwartz function $f : \mathbb{R} \to \mathbb{C}$,
$$
\int_{-\infty}^\infty \lvert f(x) \rvert ^{2} \, dx = \int_{-\infty}^\infty \lvert \hat{f}(\xi) \rvert  \, d\xi. 
$$

###### _proof:_

Consider $f^\flat : \mathbb{R} \to \mathbb{C}$ given by $f^\flat(x) = \overline{f(-x)}$. Further, consider $h = f * f^\flat$ Then we can write $h(0)$ in two ways — either as
$$
h(0) = (f * f^\flat)(0) = \int_{-\infty}^\infty f(x) \overline{f(0 - (-x))} \, dx = \int_{-\infty}^\infty \lvert f(x) \rvert^{2} \, dx 
$$
or as
$$
h(0) = \int_{-\infty}^\infty \hat{h}(\xi) \, d\xi = \int_{-\infty}^\infty \hat{f}(\xi) \widehat{f^\flat}(\xi) \, d\xi = \int_{-\infty}^\infty \hat{f}(\xi) \overline{\hat{f}(\xi)} \, d\xi = \int_{-\infty}^\infty \lvert \hat{f}(\xi) \rvert \, d\xi.
$$
Here the second equality follows by the duality of [[Fourier Analysis --- math-139/notes/Convolutions#_proposition _ the Fourier transform turns convolution into multiplication|convolution and multiplication]] and the third equality requires calculating $\widehat{f^\flat}$ directly.

This theory also yields a proof of the Weierstrass approximation theorem.

##### _theorem:_ the Weierstrass approximation theorem

For any continuous function $f : [a, b] \to \mathbb{C}$, for each $\varepsilon > 0$ there exists a polynomial $p$ such that
$$
\sup_{x \in [a, b]} \lvert f(x) - p(x) \rvert < \varepsilon.
$$
###### _proof sketch:_

Create a continuous function $g : \mathbb{R} \to \mathbb{C}$ with $g = f$ on $[a, b]$ and $g = 0$ outside some $[-M, M]$ containing $[a, b]$. Notice that $g * K_{\delta}$ is then an approximation of $f$ as $\delta \to 0^+$. But we can approximate $K_{\delta}$ by polynomials $p_{\delta}$ (the Taylor series, since the exponential is analytic) and it isn't difficult to show that $g * p_{\delta}$ is a polynomial by direct computation.