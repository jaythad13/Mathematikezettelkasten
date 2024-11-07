---
tags:
- math-131/20
- anal
---

If the [[Mathematical Analysis I --- math-131/notes/Differentiability#_definition _ differentiability, the derivative|derivative]] gives you the instantaneous rate of change of a function, then what is its relationship to the average rate of change of the function? The mean value theorem gives us the answer.

##### _theorem:_ the generalised mean value theorem

If $f$ and $g$ are continuous on $[a, b]$ and differentiable in $(a, b)$, then there exists $x \in (a, b)$ such that 
$$
(f(b) - f(a)) g'(x) = (g(b) - g(a)) f'(x).
$$

###### _proof:_

Consider $h : [a, b] \to \mathbb{R}$ by
$$
h(x) = (f(b) - f(a)) g(x) - (g(b) - g(a)) f(x).
$$
Notice that
$$
h(a) = f(b) g(a) - f(a) g(b) = h(b)
$$
and $h$ is [[Mathematical Analysis I --- math-131/notes/Continuity#_proposition _ continuity of operations on the complex numbers|continuous]] on $[a, b]$ and [[Mathematical Analysis I --- math-131/notes/Differentiability#Differentiability rules|differentiable]] on $(a, b)$ by the corresponding sum and product rules.

Since $[a, b]$ is compact, $h$ has a [[Mathematical Analysis I --- math-131/notes/Continuity#_corollary _ the image of a compact set has a maximum and minimum|maximum and a minimum]] in the $[a, b]$. If $h$ achieves its maximum and minimum on the boundary of $[a, b]$, then $h$ must be constant on $(a, b)$ with $h' = 0$ everywhere. If $h$ has a maximum or minimum inside $(a, b)$ then $h'$ [[Mathematical Analysis I --- math-131/notes/Extrema#_theorem _ the derivative vanishes at extrema|must vanish there]].