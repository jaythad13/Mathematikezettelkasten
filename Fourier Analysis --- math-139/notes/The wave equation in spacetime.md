---
tags:
- math-139/22
- math-139/23
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

The harmonic property can be verified by differentiating under the integral sign (which is justified for functions in the [[Fourier analysis --- math-139/notes/The Fourier transform in Euclidean space|Schwartz class]]).

The initial conditions follow by [[Fourier analysis --- math-139/notes/The Fourier transform in Euclidean space|Fourier inversion]] on $\mathbb{R}^d$ (where differentiating under the integral sign is needed for the second one).

Uniqueness, once again, requires us to use "conservation of energy". That is, we show that the "total energy" defined as
$$
E(t) = \int_{\mathbb{R}^d} \left\lvert  \frac{ \partial u }{ \partial t }   \right\rvert ^{2} +  \left\lvert  \frac{ \partial u }{ \partial x_{1} }  \right\rvert^{2} + \dots + \left\lvert  \frac{ \partial u }{ \partial x_{n} }   \right\rvert^{2} \, dx
$$
is a constant function in time. It follows by applying [[Fourier analysis --- math-139/notes/The Fourier transform in Euclidean space|Plancherel's theorem]] to the $t$ and $x_{i}$ parts separately. Then using the fact that
$$
\lvert a \cos \alpha + b \sin \alpha \rvert^{2} + \lvert - a\sin\alpha + b \cos \alpha \rvert ^{2} = \lvert a \rvert ^{2} + \lvert b \rvert ^{2}
$$
(because $(\cos \alpha, \sin\alpha), (-\sin \alpha, \cos \alpha)$ is an orthonormal basis), it follows that $E(t)$ is constant.

### Physical intuition

While this is a completely correct solution to the wave equation, it's not illuminating for the physics. We will show that it can be reinterpreted as
$$
u(x, t) = \frac{ \partial  }{ \partial t } (t M_{t}f + t M_{t} g)
$$
where $M_{t}$ is the spherical mean.

##### _definition:_ spherical mean

For a function $f : \mathbb{R}^3 \to \mathbb{C}$, the spherical mean of $f$ is
$$
\frac{1}{4 \pi} \int_{S^{2}} f(x - t \gamma) \, d\sigma(\gamma) = \frac{1}{4 \pi} \int_{0}^{2 \pi} \int_{0}^\pi f(x - t \gamma) \sin\theta \, d\theta \, d\phi
$$
where $\gamma = (\sin \theta \cos \phi, \sin \theta \sin \phi , \cos \theta)$.

##### _lemma:_ the spherical mean preserves the Shwartz class

If $f \in \mathcal{S}(\mathbb{R}^{3})$, then for each $t$, $M_{t}(f) \in \mathcal{S}(\mathbb{R}^3)$. Further, the function $t \mapsto M_{t}f$ is infinitely differentiable in $t$ with all derivatives in $\mathcal{S}(\mathbb{R}^{3})$.

##### _lemma:_ the Fourier transform of the spherical mean

The Fourier transform of the measure $d \sigma$ is
$$
\frac{1}{4 \pi} \int_{S^{2}} e^{-2 \pi i \xi \cdot \gamma} \, d\sigma(\gamma) = \frac{\sin(2 \pi \lVert \xi \rVert )}{2 \pi \lVert \xi \rVert }.
$$
and thus, the Fourier transform of the spherical mean of a function $f$ is given by
$$
\widehat{M_{t}f}(\xi) = \hat{f}(\xi) \frac{\sin(2 \pi \lVert \xi \rVert t)}{2 \pi \lVert \xi \rVert t}.
$$

###### _proof sketch:_

Notice that the left hand side is [[Fourier analysis --- math-139/notes/The Fourier transform in Euclidean space#_definition _ radial function|radial]]. Thus it suffices to show that the formula holds along a single ray. Choose, $\xi$ such that in polar coordinates $\theta = \phi = 0$. Then
$$
\widehat{d \sigma}(\xi) = \int_{0}^{2 \pi} \int_{0}^\pi e^{- 2 \pi i \rho \cos\theta} \, d\theta \, d\phi = \frac{\sin(2 \pi \rho t)}{2 \pi \rho t}.
$$
			
Now use the same [[Fourier analysis --- math-139/notes/Facts about integration and convergence#_theorem _ Fubini's theorem|Fubini's theorem]] trick that we used to prove [[Fourier analysis --- math-139/notes/Convolutions#_proposition _ the Fourier transform turns convolution into multiplication|convolution-multiplication duality]]. In some sense, this indicates that the spherical mean is a convolution.

##### _proposition:_ the physical intuition for the wave equation

The unique solution $u$ to the wave equation on $\mathbb{R}^{3}$ with initial conditions $f$ and $g$ satisfies
$$
u(x, t) = \frac{ \partial  }{ \partial t } (t M_{t}f) + t M_{t} g
$$

###### _proof sketch:_

For the first term, integrate and differentiate with respect to $t$ under the integral sign, and multiply and divide by $t$. For the second term just multiply and divide by $t$. Then use [[Fourier analysis --- math-139/notes/The Fourier transform in Euclidean space|Fourier inversion]].
$$
\begin{align}
u(x, t) & = \int_{\mathbb{R}^3} \hat{f}(\xi) \cos(2 \pi \lVert \xi \rVert t) e^{2 \pi i x \cdot \xi} \, d\xi + \int_{\mathbb{R}^{3}}  \hat{g}(\xi) \frac{\sin(2 \pi \lVert \xi \rVert t)}{2 \pi \lVert \xi \rVert } e^{2 \pi i x \cdot \xi} \, d\xi \\
 & = \frac{ \partial  }{ \partial t } \int \hat{f}(\xi) \frac{\sin(2 \pi \lVert \xi \rVert   t) t}{2 \pi \lVert \xi \rVert t} e^{2 \pi i x \cdot \xi} \, d\xi + \int \hat{g}(\xi) \frac{\sin(2 \pi \lVert \xi \rVert  t) t}{2 \pi \lVert \xi \rVert  t} e^{2 \pi i x \cdot \xi} \, d\xi \\
 & =  \frac{ \partial }{ \partial t } \left( t \int_{\mathbb{R}^3} \widehat{M_{t} f}(\xi) e^{2 \pi i x \cdot \xi} \, d\xi \right) + t \int_{\mathbb{R}^{3}} \widehat{M_{t} g}(\xi) e^{2 \pi i x \cdot \xi} \, d\xi \\
 & = \frac{ \partial  }{ \partial t }(t M_{t}f) + t M_{t}g. 
\end{align}
$$

Hadamard's method of descent allows us to descend this intuition to the wave equation on $(2 + 1)$-dimensional spacetime. We define a weighted average that simulates extending the wave equation to $\mathbb{R}^{3}$, and then slicing back down to $\mathbb{R}^{2}$.