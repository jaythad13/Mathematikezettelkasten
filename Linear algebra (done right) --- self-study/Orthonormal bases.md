---
tags:
- self-study
- lin-alg
---

We've already tried to generalise the idea of like $(1, 0, 0), (0, 1, 0), (0, 0, 1)$ in $\bb{F}^3$ to [[Bases|bases]] in abstract vector spaces. However, bases don't always preserve all of the properties of the standard basis of $\bb{F}^3$: basis vectors can have any "length" and can lie at any "angle" (except $0$ or $\pi$) to one another, whereas with the standard basis of $\bb{F}^3$ the basis vectors all have the same length - $1$ and are all perpendicular to each other. We call such a list of vectors orthnormal.

##### _definition:_ orthonormal

A list of vectors is called orthonormal if each vector in the list has norm $1$ and is orthogonal to each of the other vectors in the list. In other words, a $e_1, \ldots, e_m$ of vectors in $V$ is orthonormal if
$$
\langle e_j, e_k \rangle = \begin{cases}
								1 & \text{if } j = k \\
								0 & \text{if } j \neq k.
							\end{cases}
$$

##### _examples:_ orthonormal lists

1) Obviously, the standard basis in $\bb{F}^n$ is an orthonormal list, and in fact, the prototypical example of an orthonormal list.
2) $(\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}), (\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}, 0)$ is an orthonormal list in $\bb{F}^3$.
3) $(\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}), (\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}, 0), (\frac{1}{\sqrt{6}}, \frac{1}{\sqrt{6}}, -\frac{2}{\sqrt{6}})$ is an orthonormal list in $\bb{F}^3$

Working with orthonormal lists simplifies many computations in $n$-dimensional vector spaces to familiar versions on $\bb{F}^n$
##### _proposition:_ The norm of a linear an orthonormal linear combination

If $e_1, \ldots, e_m$ is an orthonormal list of vectors in $V$, then
$$
\norm{a_1 e_1 + \cdots + a_m e_m} = \abs{a_1}^2 + \cdots + \abs{a_m}^2
$$
for all $a_1, \ldots, a_m \in \bb{F}$.

##### _proof:_

Note that by additivity in the second slot and conjugate scaling that if $v$ is orthogonal to $u$ and $w$, then $v$ is orthogonal to any linear combination of $v$ and $w$:
$$
\langle u, \alpha v + \beta w \rangle = \langle u, \alpha v \rangle + \langle u, \beta w \rangle = \bar{\alpha} \langle u, v \rangle + \bar{\beta} \langle u, w \rangle = 0.
$$
