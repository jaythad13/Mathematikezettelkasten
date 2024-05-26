---
tags:
- math-82
- diff-eq
lecture:
- math-82-4
---

Euler's method uses the fact that [[The derivative|linear approximations are remarkably good]] to describe approximate solutions to [[Classifying ordinary differential equations#Order|first order]] differential equations. Essentially, it takes an initial point $(x_{0}, y_{0})$, gets the value of $y'$ at $(x_{0}, y_{0})$ and then approximates $(x_{1}, y_{1})$ for a solution of the differential equation by $y_{1} \approx y_{0} + y'(x_{0}, y_{0}) \Delta x$ for $\Delta x = x_{1} - x_{0}$. Then you just keep going.

##### _algorithm:_ Euler's method

Given a first order differential equation
$$
\frac{dy}{dx} = F(x, y),
$$
an initial value $y(x_{0}) = y_{0}$, and a small fixed $\Delta x$, define
$$
x_{n + 1} = x_{n} + \Delta x 
$$
and
$$
y_{n + 1} = y_{n} + F(x_{n}, y_{n}) \Delta x.
$$

While this produces points that are remarkably good for a linear approximation and only gets better for smaller $\Delta x$, there are much better and more computationally efficient numerical approximations. One popular example is 4th-order Runge-Kutta.

##### _algorithm:_ 4th-order Runge-Kutta

Given a first order differential equation
$$
\frac{dy}{dx} = F(x, y)
$$
an initial value, $y(x_{0}) = y_{0}$ and a small fixed $\Delta x$, define
$$
\begin{split}
a & = F(x_{n}, y_{n}) \Delta x \\
b & = F(x_{n} + \Delta x/2, y_{n} + a/2) \Delta x \\
c & = F(x_{n} + \Delta x/2, y_{n} + b/2) \Delta x \\
d & = F(x_{n} + \Delta x, y_{n} + c/2) \Delta x
\end{split}
$$
and
$$
y_{n + 1} = y_{n} + \frac{a + 2b + 2c + d}{6}.
$$

This gives $y_{n} \approx y(x_{n})$ with much better accuracy.