---
tags:
- math-139/22
- fourier
- anal
---

Recall that the $d$-dimensional Laplacian is the sum of second partials —

##### _dimension:_ the Laplacian on $\mathbb{R}^d$

For a function $f : \mathbb{R}^d \to \mathbb{R}$, the Laplacian of $f$ is $\Delta f : \mathbb{R}^d \to \mathbb{R}$ given by
$$
\Delta f(x) = \frac{ \partial^{2} f }{ \partial x_{1}^{2} } + \dots + \frac{ \partial^{2} f }{ \partial x_{n} }.
$$

The wave equation is to find some $u : \mathbb{R}^d \times \mathbb{R} \to \mathbb{R}$ such that $\Delta u = { \partial^{2} u }/{ \partial t^{2} }$ and satisfying the boundary condition $u(x, 0) = f(x)$ and $({\partial u} / {\partial t}) (x, 0) = g(x)$.

Taking the Fourier transform everywhere, we can solve to get that we must have
$$
\hat{u}(\xi, t) = \hat{f}(\xi) \cos(2 \pi \lVert \xi \rVert t) + \hat{g}(\xi) \frac{\sin(2 \pi \lVert \xi \rVert t)}{2 \pi \lVert \xi \rVert }.
$$
Thus, we claim that its Fourier inverse is a solution to the wave equation. Specifically,

##### _theorem:_ solution to the wave equation in spacetime

Given boundary conditions $u(x, 0) = f(x)$ and $({\partial u} / {\partial t}) (x, 0) = g(x)$,
$$
u(x, t) = \int_{\mathbb{R}^d} \left( \hat{f}(\xi) \cos(2 \pi \lVert \xi \rVert t) + \hat{g}(\xi) \frac{\sin(2 \pi \lVert \xi \rVert t)}{2 \pi \lVert \xi \rVert } \right) e^{2 \pi i x \cdot \xi} \, d\xi .
$$
is the unique solution to the wave equation with $\Delta u = { \partial^{2} u }/{ \partial t^{2} }$ and satisfying the boundary conditions.

###### _proof sketch:_

The harmonic property can be verified by differentiating under the integral sign (which is justified for functions in the [[Fourier Analysis --- math-139/notes/The Fourier transform in Euclidean space|Schwartz class]]).

The initial conditions follow by [[Fourier Analysis --- math-139/notes/The Fourier transform in Euclidean space|Fourier inversion]] on $\mathbb{R}^d$ (where differentiating under the integral sign is needed for the second one).

Uniqueness, once again, requires us to use "conservation of energy". That is, we show that the "total energy" defined as
$$
E(t) = \int_{\mathbb{R}^d} \left\lvert  \frac{ \partial u }{ \partial t }   \right\rvert ^{2} +  \left\lvert  \frac{ \partial u }{ \partial x_{1} }  \right\rvert^{2} + \dots + \left\lvert  \frac{ \partial u }{ \partial x_{n} }   \right\rvert^{2} \, dx
$$
is a constant function in time. It follows by applying [[Fourier Analysis --- math-139/notes/The Fourier transform in Euclidean space|Plancherel's theorem]] to the $t$ and $x_{i}$ parts separately. Then using the fact that
$$
\lvert a \cos \alpha + b \sin \alpha \rvert^{2} + \lvert - a\sin\alpha + b \cos \alpha \rvert ^{2} = \lvert a \rvert ^{2} + \lvert b \rvert ^{2}
$$
(because $(\cos \alpha, \sin\alpha), (-\sin \alpha, \cos \alpha)$ is an orthonormal basis).