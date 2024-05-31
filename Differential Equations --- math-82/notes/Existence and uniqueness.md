---
tags:
- math-82
- diff-eq
lecture:
- math-82-4
- math-82-5
---

While numerical solutions (like [[Euler's method]]) are really valuable, it's always useful to be able to confirm that our approximations really are converging to something. Existence and uniqueness theorems allow us to confirm exactly where the numerical approximation "works". Note that they don't necessarily give us a way to find the solution — they just confirm that one exists.

##### _example:_ a special case of the Ricatti equation

Consider the differential equation $y' = x^2 + y^2$ with $y(0) = 1$. It turns out that this differential equation blows up at $x = 1$, and thus, any solution should not be defined at $x = 1$. However, any approximation method will of course only add finite real numbers to get to $(x_{n}, y_{n})$ where $x_{n} = 1$. Thus, any approximation will have its error blow up at $x = 1$ as well.

### First order differential equations

We can avoid this kind of problem for most nice [[Classifying ordinary differential equations#Order|first order]] differential equations with the following two theorems.

##### _theorem:_ existence and uniqueness for first order linear differential equations

If $p$ and $q$ are continuous on the open interval $(a, b)$ containing $x_{0}$, then there exists a unique solution of the differential equation $y' + p(x) y = q(x)$ with $y(x_{0}) = y_{0}$ for all $x \in (a, b)$

##### _theorem:_ existence and uniqueness for first order differential equations

If $f$ and $\frac{ \partial f }{ \partial y }$ are continuous on the open intervals $(a, b)$ and $(c, d)$ with $(x_{0}, y_{0}) \in (a, b) \times (c, d)$, then there exists a unique solution of the differential equation $y'(x) = f(x, y)$ with $y(x_{0}) = y_{0}$. on some interval $(x_{0} - h, x_{0} + h)$ for some $h > 0$.

This has a nice corollary —

##### _corollary:_ solutions cannot intersect

If $f$ and $\frac{ \partial f }{ \partial y }$ are continuous on the open intervals $(a, b)$ and $(c, d)$ with $(x_{0}, y_{0}) \in (a, b) \times (c, d)$, then no two solution curves $y_{1}(x), y_{2}(x)$, satisfying $y'(x) = f(x, y)$ with $y(x_{0}) = y_{0}$, can intersect at just one point $(x_{0}, y_{0})$.

###### _proof:_

Since the solution is unique in some small neighbourhood around $x_{0}$, the solution curves will have to be equal in the whole neighbourhood.

Note that both theorems are not if and only if theorems — their hypotheses are sufficient for the existence of solutions, but are not necessary. Also note that both of these theorems are *hard*, with proofs that require techniques from analysis.

##### _examples:_ the strongest existence statement is...

1) $y' + \sin y = \sin x$ with $y(0) = 1$ has a unique solution in some small neighbourhood around $0$.
2) $y' + \sqrt{ x + 1 } \, y = (x - 2)^{-2}$ with $y(1) = 1$ has a unique solution for all $x \in (-1, 2)$.
3) $\sin (t) \, x' + \cos (t) \, x = 1$ with $x(\pi/2) = 2$ has a unique solution for all $t \in (0, \pi)$.
4) $y' = \frac{y + \sqrt{ x^2 + y^{2} }}{x}$ with $y(0) = \alpha$ is not guaranteed any solution by these theorems since the function $\frac{y + \sqrt{ x^2 + y^{2} }}{x}$ is not continuous at $x_{0}$.

### Higher order linear differential equations

We also have some as-nice-as-we-could-wish-for theorems for higher order linear differential equations.

##### _theorem:_ existence and uniqueness for second order linear differential equations

If $p_{1}$, $p_{2}$ and $q$ are continuous on the open interval $(a, b)$, then there exists a unique solution of the differential equation $y'' + p_{1}(x) y' + p_{2}(x) y = q(x)$ with $y(x_{0}) = y_{0}$ and $y'(x_{0}) = y_{0}'$, for all $x \in (a, b)$.

##### _theorem:_ existence and uniqueness for third order linear differential equations

If $p_{1}$, $p_{2}$, $p_3$ and $q$ are continuous on the open interval $(a, b)$, then there exists a unique solution of the differential equation $y'' + p_{1}(x) y' + p_{2}(x) y = q(x)$ with $y(x_{0}) = y_{0}$ and $y'(x_{0}) = y_{0}'$, for all $x \in (a, b)$.

In fact an analogous theorem holds true for $n$th order linear differential equations.

Finally, a really nice fact about linear differential equations — their solutions form a vector space!

##### _proposition:_ solutions of (homogenous) linear differential equations form a vector space

If $y_{1}$ and $y_{2}$ satisfy the [[Classifying ordinary differential equations#_definition _ homogenous and non-homogenous linear differential equation|homogenous]] second order linear differential equation $y'' + p_{1}(x)y' + p_{2}(x)y = 0$, then $c_{1} y_{1} + c_{2} y_{2}$ is a solution for any constants $c_{1}, c_{2} \in \mathbb{R}$.

###### _proof:_

Follows easily from the linearity of the derivative and multiplication by "coefficients" in the ring of functions on $\mathbb{R}$.

This generalises easily to $n$th order linear differential equations.