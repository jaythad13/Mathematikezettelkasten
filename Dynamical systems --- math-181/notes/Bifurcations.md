---
tags:
- math-181/4
- dynamics
---

Often we have a bunch of systems depending on a parameter and we want to analyse how the dynamics of the system changes as the parameter changes. Bifurcations are where the behaviour changes suddenly.

##### _example:_ dynamical systems

Consider the system $\dot{x} = r - x^{2}$. If $r < 0$ this has no fixed points, if $r = 0$ it has one unstable, non-hyperbolic fixed point, and if $r > 0$ it has one stable and one unstable fixed point. This behaviour changes suddenly at $r = 0$, but after that, the fixed points vary smoothly with $r$. This is an example of a **saddle-node bifurcation**.

---

##### _definition:_ bifurcation diagram, bifurcation points

For $f_{r} : \mathbb{R}^n \to \mathbb{R}^n$ a family of systems parameterised (continuously, smoothly, ...) by $r$, the **bifurcation diagram** is the subset of $\mathbb{R} \times \mathbb{R}^{n} \times \{ \pm 1 \}$ consisting of tuples $(r, x_{*}, \pm {1})$ where $x_{*}$ is a [[Dynamical systems --- math-181/notes/Continuous dynamical systems#_definition _ equilibria, stationary points, fixed points|fixed point]] of the system $\dot{x} = f_{r}(x)$ and $\pm 1$ indicates its stability.

A bifurcation point is essentially a branch point of the projection $\mathbb{R} \times \mathbb{R}^n \times \{ \pm 1 \} \to \mathbb{R}$.

---
