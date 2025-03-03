---
tags:
- math-139/15
- math-139/16
- fourier
- anal
---

The Fourier transform is a function on all of $\mathbb{R}$ that takes a (nice) function and outputs a function that gives the density of each frequency $\xi \in \mathbb{R}$. 

##### _definition:_ the Fourier transform

Given a function $f : \mathbb{R} \to \mathbb{C}$ of [[Fourier Analysis --- math-139/notes/Facts about integration and convergence#_definition _ functions of moderate decrease|moderate decrease]] the Fourier transform is the function $\hat{f} : \mathbb{R} \to \mathbb{C}$ given by
$$
\hat{f}(\xi) = \int_{-\infty}^\infty f(x) e^{-2 \pi i x \xi} \, dx.
$$

Our hope is that the Fourier transform of a function carries all the data of the function. One way to do this is to prove an inversion formula — integrating $\hat{f}$ against the opposite character $e^{2 \pi i x \xi}$ should recover $f$. Unfortunately, even though $\hat{f}(\xi) \to 0$ as $\lvert \xi \rvert \to \infty$, we don't have $\hat{f}$ of moderate decrease. Thus, we can't even really make sense of the inversion formula.

Thus, we define a nicer space of functions that is closed under the Fourier transform and has nice enough decay conditions to make everything work.

### The Schwartz space — the nicest functions for Fourier analysis

By proving some really nice properties of these functions we will see that

From here on, let $f : \mathbb{R} \to \mathbb{C}$ be Schwartz, $h$ be some real constant, and $\delta > 0$ be some positive real constant.

##### _proposition:_ translation and modulation

The function $g_{1}(x) = f(x + h)$ has Fourier transform $\hat{g}_{1}(\xi) = \hat{f}(\xi) e^{2 \pi i h \xi}$ and $g_{2}(x) = e^{2 \pi i h x} f(x)$ has Fourier transform $\hat{g}_{2}(\xi) = \hat{f}(\xi + h)$.

##### _proposition:_ dilation and scaling

##### _proposition:_ Fourier inversion of the derivative of the Fourier transform

For a function $f \in \mathcal{S}(\mathbb{R})$, the function $g : x \mapsto -2 \pi i x f(x)$ has Fourier transform given by $\hat{g} = \frac{d \hat{f}}{d \xi}$.

###### _proof sketch:_

We want to show that for each $\varepsilon > 0$ there is small enough $h$ such that
$$
\left\lvert  \frac{\hat{f}(\xi + h) - \hat{f}(\xi)}{h} - \hat{g}(\xi)  \right\rvert < \varepsilon.
$$

We can rewrite the difference as
$$
\left\lvert  \int_{-\infty}^\infty f(x) e^{2 \pi i x \xi} \left( \frac{e^{-2 \pi i x h} - 1}{h} + 2 \pi i x \right) \, dx   \right\rvert.
$$

Since $f$ is Schwartz, there is a positive integer $N$ giving $\int_{-\infty}^\infty \lvert x \rvert \lvert f(x) \rvert \, dx < \varepsilon$. Conversely, in the compact set $\lvert x \rvert \le N$, we can turn the pointwise convergence of $(e^{-2 \pi i x h} - 1) / h \to - 2 \pi i x$ (from [[Mathematical Analysis I --- math-131/notes/Mean value theorems#_theorem _ L'Hôpital's rule|L'Hôpital's rule]]) into uniform convergence. Thus, we have
$$
\left\lvert  \frac{e^{- 2 \pi i x h} - 1}{h} + 2 \pi i x  \right\rvert \le \frac{\varepsilon}{N}. 
$$

Splitting the integral cleverly, we get the whole thing controlled by some constant times $\varepsilon$.

##### _corollary:_ Schwartz functions are closed under the Fourier transform

If $f$ is Schwartz, then its Fourier transform $\hat{f}$ is also Schwartz.

###### _proof:_

We want to show that all derivatives of $f$ are rapidly decreasing. Note that since multiplication and differentiation preserve the Schwartz class, the function
$$
g(x) = \frac{1}{(2 \pi i)^k} \frac{d^k}{dx^k} ((-2 \pi i x)^\ell f(x)).
$$