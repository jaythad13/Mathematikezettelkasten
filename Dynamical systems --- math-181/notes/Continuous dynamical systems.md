---
tags:
- math-181/1
- math-181/2
- dynamics
---

Dynamical systems is about understanding solutions to differential equations without actually solving them.

For now, our main object of study will be an [[Differential equations --- math-82/notes/Classifying ordinary differential equations#_definition _ autonomous and non-autonomous differential equations|autonomous system]] of differential equations defined by $\dot{x} = f(x)$.

##### _definition:_ state space, solution, trajectory, orbit

Let $\dot{x} = f(x)$ be an autonomous system where $x : U \to \mathbb{R}^n$ and $f : \mathbb{R}^n \to \mathbb{R}^n$ are smooth, and $U \subseteq \mathbb{R}$

Then $\mathbb{R}^n$ is the **state space** of the system.

A **solution** to the differential equation is a function $x$ satisfying $\dot{x} = f(x)$ for all $t \in U$. A **global solution** is a solution for $U = \mathbb{R}$.

A **trajectory** or **orbit** is a parametric curve $x(t)$ traced out by a solution to the differential equation.

---

It will be important to know that we have local solutions to our problems.

##### _theorem:_ existence and uniqueness for autonomous differential equations

Let $t_{0} \in \mathbb{R}, x_{0} \in \mathbb{R}^n$ and let $f : \mathbb{R}^n \to \mathbb{R}^n$ be $C^1$. Then there is some neighbourhood $U \ni t_{0}$ where there exists some $x : U \to \mathbb{R}^n$ such that $\dot{x} = f(x)$ on $U$.

###### _proof sketch:_

This proof technique is called **Picard iteration**. Make a guess $u_{0}(t) = x_{0}$ and inductively define
$$
u_{n + 1}(t) = x_{0} + \int_{0}^t f(u_{n}(s)) \, ds.
$$
Because of the niceness of $f$, this converges to something, and by construction it must converge to a solution.

---

We will study these problems by studying questions of their stability.

##### _definition:_ equilibria, stationary points, fixed points

The **equilibria** or **stationary points** or **fixed points** are points $x_{*} \in \mathbb{R}^n$ where $f(x_{*}) = 0$ (and thus, $\dot{x}(t) = 0$)

---

We want to understand when these equilibrium points are stable or unstable.

##### _definition:_ stable, unstable, asymptotically stable equilibria

Let $x_{*}$ be an equilibrium point of the differential equation $\dot{x} = f(x)$. Let $x$ be a solution satisfying $x(t_{0}) = x_{0}$

$x_{*}$ is **stable** if for each $\varepsilon > 0$ there exists a $\delta > 0$ such that $\lVert x_{0} - x_{*} \rVert < \delta$ implies any solution with $x(t_{0}) = x_{0}$ satisfies $\lVert x(t) - x_{*} \rVert < \varepsilon$ for all $t > t_{0}$.

$x_{*}$ is **unstable** if it is not stable.

$x_{*}$ is **asymptotically stable** if there exists $\delta > 0$ such that $\lVert x_{0} - x_{*} \rVert < \delta$ implies that $\lim_{ t \to \infty } x(t) = x_{*}$.

---

Looking at an example should give a conjecture — if $f'(x_{*}) < 0$ then $x_{*}$ is a stable equilibrium.