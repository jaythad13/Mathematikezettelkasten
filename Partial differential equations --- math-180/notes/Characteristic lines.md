---
tags:
- math-180/5
- pde
---

We always want to solve partial differential equations by reducing them to ordinary differential equations that we know how to solve. One way to do this is by interpreting a linear condition on the partial derivatives as coming from the chain rule along a curve.

##### _example:_ characteristic lines

Suppose we want to solve for $\partial_{x} u + \partial_{y} u = u^{2}$ for some function $u : \mathbb{R}^2 \to \mathbb{R}$. Suppose further, that we want $u(x, 0) = g(x)$.

Then, we can interpret this as $D u (1, 1) = u^{2}$. If we write $v(t) = u(x(t), y(t))$ for functions $x, y : \mathbb{R} \to \mathbb{R}$ with $x' = y' = 1$. In particular, since $dy / dx = 1$, we have $y = x + c_{1}$ for some $c_{1} \in \mathbb{R}$. That is, $x, y$ lie on a **characteristic line**. 

Then the differential equation is equivalent to $Dv = v^{2}$. By separation of variables, we know $v(t) = -1 / (t + c_{2})$ for some $c_{2} \in \mathbb{R}$. Suppose $y(t) = t$ (we can choose this freely). Then $x(t) = t - c_{1}$. Since we require $u(x, 0) = g(x)$, we require $v(0) = g(x(0))$. Note, $y - x = c_{1} = -x(0)$. Thus, $g(x - y) = -1 / c_{2}$. Thus,
$$
u(x, y) = -\frac{1}{y - 1 / g(x - y)} = \frac{-g(x - y)}{y g(x - y) - 1}.
$$

---

##### _example:_ characteristic lines of a quasi-linear equation can intersect

Suppose we want to solve $u \partial_{x} u + \partial_{y} u = 0$ with $u(x, 0) = g(x)$.

Then again, we can interpret this as $Du (x'(t), y'(t)) = 0$. In particular, we have $x' = u$, $y' = 1$, and writing $v(t) = u(x(t), y(t))$, we have $v'(t) = 0$. Thus, $dy / dx = 1 / u(t) = 1 / g(x(0))$. This leads to some interesting behaviour. Suppose $g(x) > g(x')$. Then the characteristic line containing $x$ has lesser slope than the characteristic line containing $x'$. But these two lines of different slope must intersect, and $u$ must be constant along each of these lines (if a solution $u$ exists). Thus, $u$ only exists in the domain where these characteristic lines do not intersect.

---

##### _theorem:_ solutions 

Suppose $a, b, c$ are [[Partial differential equations --- math-180/notes/Existence and uniqueness#_example _ some Lipschitz, locally Lipschitz, and not at all Lipschitz functions|locally Lipschitz]] functions $\mathbb{R}^3 \to \mathbb{R}$. Given an initial condition $u(x(t), y(t)) = g(t)$ such that the parametric curve $(x(t), y(t))$ intersects the projection of each solution to
$$
x'(t) = a(x(t), y(t), g(t)), y'(t) = b(x(t), y(t), g(t)), z' = c(x(t), y(t), z(t))
$$
onto the $x, y$ plane, there exists a neighbourhood of each $(x(t), y(t))$ on which athere is a unique function such that 
$$
a(x, y, u) \partial_{x} u + b(x, y, u) \partial_{y} u = c(x, y, u).
$$

---