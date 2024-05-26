---
tags:
- math-82
- diff-eq
lecture:
- math-82-4
---

While numerical solutions are really valuable, it's always useful to be able to confirm that our approximations really are converging to something. Existence and uniqueness theorems allow us to confirm exactly where the numerical approximation "works". Note that they don't necessarily give us a way to find the solution — they just confirm that one exists.

##### _example:_ a special case of the Ricatti equation

Consider the differential equation $y' = x^2 + y^2$ with $y(0) = 1$. It turns out that this differential equation blows up at $x = 1$, and thus, any solution should not be defined at $x = 1$. However, any approximation method will of course only add finite real numbers to get to $(x_{n}, y_{n})$ where $x_{n} = 1$. Thus, any approximation will have its error blow up at $x = 1$ as well.

### First order linear differential equations

We can avoid this kind of problem for first order linear equations.

##### _theorem:_ existence and uniqueness for first order linear differential equations

If $p$ and $q$ are continuous on the open interval $(a, b)$, then the solution of the differential equation $y' + p(x) y = q(x)$ with $y(x_{0}) = y_{0}$ exists and is unique for all $x \in (a, b)$.