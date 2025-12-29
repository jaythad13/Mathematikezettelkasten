---
tags:
- math-82/9
- diff-eq
---

Like with [[Differential equations --- math-82/notes/Variation of parameters|variation of parameters]], the idea of undetermined coefficients is to obtain the general solution to a second order linear differential equation by guessing one particular solution and using the general solution to the homogeneous equivalent.

That is, any two solutions to $Dy = f(x)$ differ by a solution to the equation $Dy = 0$. If we know the general form of $\ker D$ (say, by knowing a basis of solutions, $y_{1}, \dots, y_{n}$) then we know that the general solution to $Dy = f(x)$ is given by $y_{0} + y_{1} + \dots + y_{n}$.

Specifically, we guess that $y$ is an $\mathbb{R}$-linear combination of $f(t)$ and its linearly independent derivatives and then mess choose the coefficients so that this works. If none of the coefficients work, go back to the start.