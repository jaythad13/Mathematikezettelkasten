---
tags:
- math-139/2
- anal
---

The motto of Fourier analysis (on $\mathbb{R} / \mathbb{Z}$) is to decompose things into oscillations. This idea comes from physics.

### Simple harmonic motion

It's a fact of physics that if you pull a spring with a mass on the end of it, the force opposing you is proportional to how much you displaced the mass. In particular, for a displacement (as a function of time) $y(t)$, the corresponding force from the wall is $-k y(t)$. Since force is mass times acceleration, we have the differential equation
$$
-k y(t) = m \ddot{y}(t) \iff \ddot{y}(t) + c^{2} y(t) = 0
$$
(writing $c^{2} = k / m$). This has general solution
$$
y(t) = A \cos(c t) + B \sin(c t).
$$

### The wave equation on $\mathbb{R}$

In physics we often want to consider waves — periodic functions $u$ that denote the verticle displacement of particles in both position and time. For example, consider a string fixed across length $L$. Physical considerations imply that if $u$ is twice differentiable, it must satisfy the differential equation
$$
\frac{1}{c^{2}} \frac{ \partial^{2} u }{ \partial t^{2} } = \frac{ \partial^{2}u }{ \partial x^{2} }  
$$
for some positive real $c$. Of course $u(L, t) = u(0, t) = 0$ at every time $t$.

We can first rescale the distance so that the length of the wave $L = \pi$ and then so that $c = 1$. This gives us
$$
\frac{ \partial^{2} u }{ \partial t^{2} } = \frac{ \partial^{2}u }{ \partial x^{2} }.
$$

We want to be able to solve this in general for $u$.

### D'Alembert's solution

D'Alembert's solution used the insight that (with our rescaling) moving in time is just the same as moving in space. Thus, for any twice differentiable function $F : \mathbb{R} \to \mathbb{R}$, $u(x, t) = F(x + t)$, a wave travelling in the negative direction and $u(x, t) = F(x - t)$, a wave travelling in the positive direction are both possible solutions. It turns out this uniquely characterises the solutions.

##### _proposition:_ the general solution to the wave equation

Any twice differentiable solution to the wave equation must be the sum of travelling waves in opposing directions.

###### _proof sketch:_

Let $u : (x, t) \mapsto u(x, t)$ and define the change of variables $\xi = x + t$ and $\eta = x - t$. Define the function $v : (\xi, \eta) \mapsto u(x, t)$. Using the chain rule and the obvious inverse of the change of variables, we get
$$
\frac{ \partial^{2} v }{ \partial \xi \partial \eta } = \frac{1}{4} \left( \frac{ \partial^{2} u }{ \partial x^{2}} + \frac{ \partial^{2} u }{ \partial t^{2} }   \right).
$$
Integrating, we get
$$
u(x, t) = v(\xi, \eta)= F(\xi) + G(\eta) = F(x + t) + G(x - t).
$$
This is exactly the decomposition we wanted!

Returning to our wave function $u$ for the string, we can extend it to all of $\mathbb{R}$ by making it an odd function on $[-\pi, \pi]$ and then extending it to the whole real line as a periodic function. By fixing $u(x, 0) = f(x)$ and ${ \partial u } / { \partial t } (x, 0) = g(x)$, plus some algebra, we can uniquely determine $F$ and $G$ as functions of $f$ and $g$.

### Superposition of standing waves

To motivate Fourier analysis however, it makes sense to think of wave solutions as linear combinations of standing wave solutions
$$
u(x, t) = \varphi(x) \psi(t)
$$
(with the same initial conditions).