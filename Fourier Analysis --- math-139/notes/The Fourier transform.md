---
tags:
- math-139/15
- math-139/17
- fourier
- anal
---

Until now, we've been converting the data of (nice) functions $f : \mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{C}$ to the data of equivalent functions — their Fourier coefficients $\hat{f} : \mathbb{Z} \to \mathbb{C}$. Now we want to convert the data of (very nice functions) $f : \mathbb{R} \to \mathbb{C}$ to equivalent functions $\hat{f} : \mathbb{R} \to \mathbb{C}$. These are both special cases of the more general idea of Fourier analysis — to take functions on a [[Abstract algebra --- math-171/notes/Groups, and why you should care#_definition _ group, identity, inverse|group]] $f : G \to \mathbb{C}$ and convert into the data of functions on the dual group $\hat{G}$. The dual group of $\mathbb{R} / 2 \pi \mathbb{Z}$ is $\mathbb{Z}$ and the dual group of $\mathbb{R}$ is itself.

The Fourier transform takes a (nice) function and outputs a function that gives the density of each frequency $\xi \in \mathbb{R}$. 

##### _definition:_ the Fourier transform

Given a function $f : \mathbb{R} \to \mathbb{C}$ of [[Fourier analysis --- math-139/notes/Facts about integration and convergence#_definition _ functions of moderate decrease|moderate decrease]] the Fourier transform is the function $\hat{f} : \mathbb{R} \to \mathbb{C}$ given by
$$
\hat{f}(\xi) = \int_{-\infty}^\infty f(x) e^{-2 \pi i x \xi} \, dx.
$$

Our hope is that the Fourier transform of a function carries all the data of the function. One way to do this is to prove an inversion formula — integrating $\hat{f}$ against the opposite character $e^{2 \pi i x \xi}$ should recover $f$. Unfortunately, even though $\hat{f}(\xi) \to 0$ as $\lvert \xi \rvert \to \infty$, we don't have $\hat{f}$ of moderate decrease. Thus, we can't even really make sense of the inversion formula.

Thus, we define a nicer space of functions that is closed under the Fourier transform and has nice enough decay conditions to make everything work.

### The Schwartz space — the nicest functions for Fourier analysis

The Schwartz space consists of functions that have lots of derivatives, and satisfies good decay conditions.

##### _definition:_ rapidly decreasing

A function $f : \mathbb{R} \to \mathbb{C}$ is rapidly decreasing if, for each $k \geq 0$, we have that the function $\lvert x \rvert^k \lvert f(x) \rvert$ is bounded.

##### _definition:_ Schwartz class, $\mathcal{S}(\mathbb{R})$

If $f : \mathbb{R} \to \mathbb{C}$ has all [[Analysis --- math-131/notes/Differentiability#_definition _ higher-order derivatives|higher order derivatives]] and it, and all its derivatives are rapidly decreasing, then $f$ is in the Schwartz class, denoted $f \in \mathcal{S}(\mathbb{R})$.

From here on, let $f : \mathbb{R} \to \mathbb{C}$ be Schwartz, $h$ be some real constant, and $\delta > 0$ be some positive real constant. By proving some really nice properties of $f$ we will see that $\mathcal{S}(\mathbb{R})$ is also closed under the Fourier transform.

##### _proposition:_ translation is dual to modulation

For any $h \in \mathbb{R}$, the function $g_{1}(x) = f(x + h)$ has Fourier transform $\hat{g}_{1}(\xi) = \hat{f}(\xi) e^{2 \pi i h \xi}$ and the function $g_{2}(x) = e^{2 \pi i h x} f(x)$ has Fourier transform $\hat{g}_{2}(\xi) = \hat{f}(\xi + h)$.

##### _proposition:_ dilation is dual to scaling

For any $\delta > 0$, the function $g(x) = f(\delta x)$ has Fourier transform $\hat{g}(\xi) = f(\xi / \delta) / \delta$.

##### _proposition:_ derivatives and multiplication 

For a function $f \in \mathcal{S}(\mathbb{R})$, the function $g(x) = -2 \pi i x f(x)$ has Fourier transform given by $\hat{g} = \frac{d \hat{f}}{d \xi}$. The derivative $f'$ has Fourier transform $\widehat{f'}(\xi) = - 2 \pi i \xi \hat{f}(\xi)$.

###### _proof sketch:_

We want to show that for each $\varepsilon > 0$ there is small enough $h$ such that
$$
\left\lvert  \frac{\hat{f}(\xi + h) - \hat{f}(\xi)}{h} - \hat{g}(\xi)  \right\rvert < \varepsilon.
$$

We can rewrite the difference as
$$
\left\lvert  \int_{-\infty}^\infty f(x) e^{2 \pi i x \xi} \left( \frac{e^{-2 \pi i x h} - 1}{h} + 2 \pi i x \right) \, dx   \right\rvert.
$$

Since $f$ is Schwartz, there is a positive integer $N$ giving $\int_{\lvert x \rvert > N} \lvert x \rvert \lvert f(x) \rvert \, dx < \varepsilon$. For all $x$ with $\lvert x \rvert > N$ we can actually bound the other factor in the integral to be $O(x)$, so this bound is useful. Specifically, we write
$$
\begin{align}
\left\lvert  \frac{e^{-2 \pi i x h} - 1}{h} + 2 \pi i x  \right\rvert & = \left\lvert  \frac{e^{- \pi i x h}(e^{-\pi i x h} - e^{\pi i x h})}{h} + 2 \pi i x \right\rvert  \\
 & \le \lvert e^{-\pi i x h} \rvert \left\lvert  2 \frac{\sin(\pi x h)}{h}  \right\rvert + \lvert 2 \pi i x h \rvert  \\
 & \le c_{1} \lvert \pi x \rvert + c_{2} \lvert x \rvert  \\
 & \le c \lvert x \rvert.
\end{align}
$$
for some positive constant $c$. Here the second inequality follows by the small angle approximation which holds for small enough $h$.

In the compact set $\lvert x \rvert \le N$, we can turn the pointwise convergence of $(e^{-2 \pi i x h} - 1) / h \to - 2 \pi i x$ (from [[Analysis --- math-131/notes/Mean value theorems#_theorem _ L'Hôpital's rule|L'Hôpital's rule]]) into uniform convergence (by the compactness of $[-N, N]$). Thus, for sufficiently small $h$ we have
$$
\left\lvert  \frac{e^{- 2 \pi i x h} - 1}{h} + 2 \pi i x  \right\rvert \le \frac{\varepsilon}{N}
$$
for all $x$ with $\lvert x \rvert \le N$.

Splitting the integral, we get the whole thing controlled by some constant times $\varepsilon$.

##### _corollary:_ Schwartz functions are closed under the Fourier transform

If $f$ is Schwartz, then its Fourier transform $\hat{f}$ is also Schwartz.

###### _proof:_

We want to show that all derivatives of $f$ are rapidly decreasing. Note that since the Schwartz class is closed under differentiation and multiplication by polynomials, the function
$$
g(x) = \frac{1}{(2 \pi i)^k} \frac{d^k}{dx^k} ((-2 \pi i x)^\ell f(x)).
$$
is Schwartz. It has Fourier transform
$$
\hat{g}(x) = \xi^k \frac{d^\ell}{d \xi} \hat{f}(\xi)
$$
which must then be bounded. But then, taking arbitrary $k$ and $\ell$ we can show that any $\ell$th derivative of $\hat{f}$ is of rapid decrease, and thus, that $\hat{f}$ is Schwartz.