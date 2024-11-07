---
tags:
- math-131/20
- anal
---

Using [[Mathematical Analysis I --- math-131/notes/Differentiability#_definition _ differentiability, the derivative|derivatives]], we can study the extrema of a function — points at which they are locally minimised or maximised.

##### _definition:_ local extrema

Let $f : (a, b) \to \mathbb{R}$. We say that $f$ has a local minimum at $x_{0}$ if there is a $\delta > 0$ such that $f(x) \ge f(x_{0})$ for all $x \in (x_{0} - \delta, x_{0} + \delta)$.

We say $f$ has a local maximum at $x_{0}$ if there is a $\delta > 0$ such that $f(x) \le f(x_{0})$ for all $x \in (x_{0} - \delta, x_{0} + \delta)$.

The main theorem we have here is that the derivative always vanishes at the extrema —

##### _theorem:_ the derivative vanishes at extrema

If $f$ is differentiable at $x_{0}$, where it has a local maximum or minimum, then $f'(x_{0}) = 0$.

###### _proof sketch:_

Consider [[Mathematical Analysis I --- math-131/notes/Limits#Limits on the real and complex numbers|left and right limits]] separately — show that they can be neither less nor greater than $0$.