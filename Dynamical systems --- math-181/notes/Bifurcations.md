---
tags:
- math-181/4
- math-181/5
- dynamics
---

Often we have a bunch of systems depending on a parameter and we want to analyse how the dynamics of the system changes as the parameter changes. Bifurcations are where the behaviour changes suddenly.

##### _example:_ dynamical systems

Consider the system $\dot{x} = r - x^{2}$. If $r < 0$ this has no fixed points, if $r = 0$ it has one unstable, non-hyperbolic fixed point, and if $r > 0$ it has one stable and one unstable fixed point. This behaviour changes suddenly at $r = 0$, but after that, the fixed points vary smoothly with $r$. This is an example of a **saddle-node bifurcation**.

---

##### _definition:_ bifurcation diagram, bifurcation points

For $f_{r} : \mathbb{R}^n \to \mathbb{R}^n$ a family of systems parameterised (continuously, smoothly, ...) by $r$, the **bifurcation diagram** is the subset of $B \subseteq \mathbb{R} \times \mathbb{R}^{n} \times \{ \pm 1 \}$ consisting of tuples $(r, x_{*}, \pm {1})$ where $x_{*}$ is a [[Dynamical systems --- math-181/notes/Continuous dynamical systems#_definition _ equilibria, stationary points, fixed points|fixed point]] of the system $\dot{x} = f_{r}(x)$ and $\pm 1$ indicates its stability.

A **bifurcation point** is a point $r_{0} \in \mathbb{R}$ such that the pre-image size of the projection $B \subseteq \mathbb{R}$ is not constant on any open neighbourhood of $r_{0}$. (That is, the number of fixed points of $f_{r}$ changes at $r_{0}$).

---

By an application of the [[Calculus --- spivak/notes/Inverse and implicit functions#_theorem _ the implicit function theorem|implicit function theorem]], then locally, we can eliminate the possibility of bifurcation points at sensible fixed points.

##### _theorem:_ no bifurcations at hyperbolic fixed points

Let $f_{r} : \mathbb{R}^n \to \mathbb{R}^n$ be a family of smooth functions parameterised smoothly by $r$. Suppose $x_{*}$ is a [[Dynamical systems --- math-181/notes/Continuous dynamical systems#_definition _ hyperbolic and non-hyperbolic equilibria|hyperbolic]] fixed point of $f_{r_{0}}$. Then $(r_{0}, x_{*})$ is not a bifurcation point.

###### _proof:_

Write $f_{r}(x) = f(r, x)$ and notice that $\frac{ \partial f }{ \partial x }(r_{0}, x_{*}) \neq 0$. Apply the implicit function theorem to see that in a small neighbourhood of $(x_{*}, r_{0})$ in which we can write a unique function $x(r)$ so that $f(r, x(r)) = 0$. Since the function is unique this is not a bifurcation point.

---

This is the first example of a more general principle — we can understand bifurcations by doing local analysis on the defining function $f$. We've already shown that for $(r_{0}, x_{*})$ to be a bifurcation point, $x_{*}$ must be a non-hyperbolic fixed point of $r_{0}$. In most cases, it suffices to also require vanishing of some further derivatives.

Essentially, suppose $(0, 0)$ is a non-hyperbolic fixed point of $f$. Then, near $0$, we have $\dot{x} = \alpha r + \beta x^{2} + \gamma x r + \delta r^{2} + O(x^3)$. If $\alpha = 0$ and $\beta \neq 0$, then $\dot{x} \approx rx - x$ so the bifurcation looks like a transcritical bifurcation, if $\alpha \beta \cong 0$, then $\dot{x} \approx r - x^{2}$ so it looks like a saddle-node bifurcation, and if $\alpha = \beta = 0$ and $\gamma \neq 0$, and ${ \partial^{3} f } / { \partial x^{3} } \neq 0$ then it looks like a pitchfork since $\dot{x} \approx rx - x^{3}$.