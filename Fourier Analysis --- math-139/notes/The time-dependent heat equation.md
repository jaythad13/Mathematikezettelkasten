---
tags:
- diff-eq
- fourier
- anal
- math-139/18
---

The time dependent heat equation on $\mathbb{R}$ is to find $u : \mathbb{R} \times \mathbb{R}_{\geq 0} \to \mathbb{R}$ that gives the temperature at position $x$ and time $0$, satisfying the partial differential equation
$$
\frac{ \partial u }{ \partial t } = \frac{ \partial^{2} u }{ \partial x^{2} }
$$
and the initial condition $u(x, 0) = f(x)$ for some $f : \mathbb{R} \to \mathbb{R}$.

We proceed "formally" not worrying about whether things actually work. In particular, we take the Fourier transform in the first variable $x$ to get
$$
\frac{ \partial \hat{u} }{ \partial t } (\xi, t) = - 4 \pi^{2} \xi^{2} \hat{u}(\xi, t)
$$
(since the Fourier transform in one variable commutes with differentiation in a different variable). Now, solving this as a [[Differential equations --- math-82/notes/Separable differential equations#_definition _ separable differential equation|separable differential equation]] in $t$, and substituting the initial condition $f$, we get
$$
\hat{u}(\xi, t) = \hat{f}(\xi) e^{- 4 \pi^{2} \xi^{2} t}
$$

Thus, $u(x, y) = f(x) * H_{t}(x)$ with $H_{t}$ such that $\hat{H_{t}}(\xi) = e^{-4 \pi^{2} \xi^{2} t}$. But then, this is just a dilate of the [[Fourier analysis --- math-139/notes/The Gaussian kernel#_definition _ the Gaussian kernel|the Gaussian kernel]]. In particular, $H_{t}(x) = \text{something}$, so it is Schwartz too! In fact, this really does work.

##### _theorem:_ the solution to the time-dependent heat equation

For $f \in \mathcal{S}(\mathbb{R})$, let $u(x, t) = f * H_{t}(x)$. Then
1) $u \in \mathcal{C}^{2}(\mathbb{H}^{2})$ and solves the heat equation
2) $u(x, t) \rightrightarrows f(x)$ (uniformly) in $x$ as $t \to 0$, and thus, is continuous on $\overline{\mathbb{H}^{2}}$.
3) $u(x, t) \to f(x)$ in $L^{2}$ as $t \to 0$.

###### _proof sketch:_

The first part follows from differentiating under the integral sign using dominated convergence (from Schwartz) and checking that it does indeed solve the heat equation. Since it is Schwartz, we are guaranteed the smoothness of the derivatives and we really can do all of this.

##### _corollary:_ $u$ is Schwartz uniformly in $t$

Given any $T > 0$, for fixed, $k, \ell > 0$, we have
$$
\sup_{x \in \mathbb{R}} \lvert x \rvert^k \left\lvert  \frac{ \partial^\ell u }{ \partial x^\ell }   \right\rvert < \infty
$$
for all positive $t < T$.

##### _theorem:_ uniqueness of solutions to the heat equation

Suppose $u : \overline{\mathbb{H}^{2}} \to \mathbb{R}$ satisfies
$$
\frac{ \partial u }{ \partial t } = \frac{ \partial^{2} u }{ \partial x^{2} } \text{ and } u(x, 0) = 0
$$
with $u$ continuous on $\overline{\mathbb{H}^{2}}$ and $u(x, t)$ Schwartz in $x$, uniformly in $t$. Then $u$ is identically $0$.