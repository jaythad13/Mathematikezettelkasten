---
tags:
- math-82/11
- diff-eq
---

Abel's theorem offers a converse that [[Differential equations --- math-82/notes/The Wronskian#_proposition _ linearly dependent implies vanishing Wronskian|linear dependence implies vanishing of the Wronskian]] in the case that the two functions are solutions to a linear differential equation.

For the rest of this note, suppose $p, q$ are continuous functions on $U \subseteq \mathbb{R}$ and $y_{1}, y_{2}$ both satisfy the differential equation $y'' + p(x) y' + q(x)y = 0$. 

##### _theorem:_ Abel's theorem on linear independence

There is some $C \in \mathbb{R}$ such that $W_{y_{1}, y_{2}}(t) = C e^{- \int  p(t) \, dt}$.

###### _proof sketch:_

By definition $W = y_{1} y_{2}' - y_{2} y_{1}'$. Differentiating and substituting the differential equation for the second derivatives gives $W' = - p W$. Thus, $W$ has the desired form.

---

##### _corollary:_ the Wronskian vanishes everywhere or nowhere

Either $W_{y_{1}, y_{2}}(t) = 0$ for all $t \in U$ or $W_{y_{1}, y_{2}}(t) \neq 0$ for all $t \in U$.

---

##### _corollary:_ vanishing Wronskian is equivalent to linear dependence

The following are equivalent
1) $y_{1}, y_{2}$ are linearly independent.
2) $W_{y_{1}, y_{2}}(t) \neq 0$ for some $t \in U$.
3) $W_{y_{1}, y_{2}}(t) \neq 0$ for all $t \in U$.

---

This is a very useful result. For example, it proves that our differential equation has a solution space of dimension $2$. Basically, construct a solution set that has non-zero Wronskian (by constructing the initial value problem corresponding to the identity matrix). Because of the Wronskian, the solution set is linearly independent. Because it's constructed as the identity matrix, choose the obvious linear combination to solve any initial value problem.

##### _theorem:_ the solution space of a linear homogeneous differential equation

The solution space of an $n$th order, linear, homogeneous differential equation has dimension $n$.

---