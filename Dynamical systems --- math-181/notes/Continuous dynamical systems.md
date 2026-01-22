---
tags:
- math-181/1
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

##### _definition:_ equilibria, stationary points, fixed points

The **equilibria** or **stationary points** or **fixed points** are points where $\dot{x} = 0$.

---