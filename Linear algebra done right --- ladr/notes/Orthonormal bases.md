---
tags:
- ladr/6B
- self-study
- lin-alg
---

We've already tried to generalise the idea of like $(1, 0, 0), (0, 1, 0), (0, 0, 1)$ in $\bb{F}^3$ to [[Bases|bases]] in abstract vector spaces. However, bases don't always preserve all of the properties of the standard basis of $\bb{F}^3$: basis vectors can have any "length" and can lie at any "angle" (except $0$ or $\pi$) to one another, whereas with the standard basis of $\bb{F}^3$ the basis vectors all have the same length - $1$ and are all perpendicular to each other. We call such a list of vectors orthonormal.

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

Orthonormal lists containing unit elements


### Basic properties of orthonormal lists

Now that we have formally defined them, we can prove some basic properties about orthonormal lists.

##### _proposition:_ the norm of an orthonormal linear combination

If $e_1, \ldots, e_m$ is an orthonormal list of vectors in $V$, then
$$
\norm{a_1 e_1 + \cdots + a_m e_m}^2 = \abs{a_1}^2 + \cdots + \abs{a_m}^2
$$
for all $a_1, \ldots, a_m \in \bb{F}$.

###### _proof:_

Note that by additivity in the second slot and conjugate scaling that if $v$ is orthogonal to $u$ and $w$, then $v$ is orthogonal to any linear combination of $v$ and $w$:
$$
\langle u, \alpha v + \beta w \rangle = \langle u, \alpha v \rangle + \langle u, \beta w \rangle = \bar{\alpha} \langle u, v \rangle + \bar{\beta} \langle u, w \rangle = 0.
$$
By repeated application of this we see that for an orthonormal list $e_1, \ldots, e_m$ each $e_j$ is orthogonal to every linear combination of $e_{j+1}, \ldots, e_{m}$. Then by repeated application of [[Orthogonality|Pythagoras' theorem]] we get
$$
\begin{gathered}
	\norm{a_1 e_1 + a_2 e_2 + \cdots + a_m e_m}^2 \\
	 = \abs{a_1} \norm{e_1}^2 + \norm{a_2 e_2 + \cdots + a_m e_m}^2 \\
	\vdots \\ 
	 = \norm{a_1 e_1}^2 + \cdots + \norm{a_m e_m}^2.
\end{gathered}
$$
Using the [[Inner product spaces#norm|scaling property of the norm]] and the fact that $\norm{e_j} = 1$ for all $j \in \bb{N}_m$ reduces the last expression to
$$
\abs{a_1}^2 + \cdots + \abs{a_m}^2
$$
as desired.

##### _proposition:_ an orthonormal list is linearly independent

Every orthonormal list of vectors is linearly independent.

###### _proof:_

Suppose $e_1, \ldots, e_m$ is an orthonormal list of vectors, and suppose $a_1 e_1 + \cdots + a_m e_m = 0$. 

Then we must have, for each $e_j$,
$$
\langle a_1 e_1 + \cdots a_m e_m, e_j \rangle = 0.
$$
Using additivity and scaling in the first slot and the definition of an orthonormal list, this gives us
$$
a_j \langle e_j, e_j \rangle = 0
$$
for each $j$. Since $\langle e_j, e_j \rangle = 1$ and is thus non-zero, $a_j$ must be $0$ for each $j$.

Thus, $a_1 e_1 + \cdots + a_m e_m = 0$ forces $a_1 = \cdots = a_m = 0$. that is, $e_1, \ldots, e_m$ is linearly independent.

### Orthonormal bases

##### _definition:_ orthonormal basis

An orthonormal basis of $V$ is a an orthonormal list of vectors in $V$ that is also a basis of $V$.

##### _example:_ orthonormal bases

The following are orthonormal bases
- the standard basis of $\bb{F}^n$, $(1, 0, 0), (0, 1, 0), (0, 0, 1)$
- the previous example $(\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}), (\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}, 0), (\frac{1}{\sqrt{6}}, \frac{1}{\sqrt{6}}, -\frac{2}{\sqrt{6}})$ in $\bb{F}^3$.

##### _proposition:_ an orthonormal list of the right length is an orthonormal basis

Every orthonormal list of vectors in $V$ of length $\dim V$ is an orthonormal basis of $V$.

###### _proof:_

Since every orthonormal list is linearly independent, every orthonormal list of length $\dim V$ is also a linearly independent list of length $\dim V$, and thus, a basis of $V$.

##### _example:_ proof by right length

Show that
$$
\Big(\frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2} \Big), \Big( \frac{1}{2}, \frac{1}{2}, -\frac{1}{2}, -\frac{1}{2} \Big), \Big( \frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}, \frac{1}{2} \Big), \Big( -\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}, \frac{1}{2} \Big)
$$
is an orthonormal basis of $\bb{F}^4$ (with the Euclidean inner product).

We will denote the vectors $v_1, \ldots, v_4$.

For each vector it is trivial to show that $\norm{v_j} = 1$. In fact, they all have the same proof:
$$
\norm{v_j}^2 = (\pm \frac{1}{2})^2 + (\pm \frac{1}{2})^2 + (\pm \frac{1}{2})^2 +(\pm \frac{1}{2})^2 = \frac{1}{4} + \frac{1}{4} + \frac{1}{4} + \frac{1}{4} = 1.
$$

Since any two distinct vectors $v_j$ and $v_k$ have exactly two components with different signs and exactly two components with the same sign, 
$$
\langle v_j, v_k \rangle = 2 \frac{1}{2^2} + 2 \frac{(-1)}{2^2} = 0.
$$
Thus, the list is an orthonormal list.

Since it has length $4$ and $\dim \bb{F}^4 = 4$, it must also be an orthonormal basis.

##### _proposition:_ the coordinates of a vector in an orthonormal basis

Suppose $e_1, \ldots, e_m$ is an orthonormal basis of $V$. Then we can write any $v \in V$ as a linear combination of $e_1, \ldots, e_m$ as follows.
$$
v = \langle v, e_1 \rangle e_1 + \cdots + \langle v, e_m \rangle e_m.
$$

###### _proof:_

Since $e_1, \ldots, e_m$ is a [[Bases|basis]], there must be some way to write $v$ as a linear combination of it, for any $v \in V$. Say
$$
v = a_1 e_1 + \cdots + a_m e_m.
$$

Then, for each $j \in \bb{N}_m$ consider taking the inner product with $e_j$ in the right slot on both sides. With linearity, this gives us
$$
\langle v, e_j \rangle = 0 + a_j \langle e_j, e_j \rangle.
$$
That is,
$$
a_j = \langle v, e_j \rangle
$$
for each $j \in \bb{N}_m$.

##### _corollary:_ the norm of a vector in an orthonormal basis

Suppose $e_1, \ldots, e_m$ is an orthonormal basis of $V$. Then, for any $v \in V$
$$
\norm{v}^2 = \abs{\langle v, e_1 \rangle}^2 + \cdots + \abs{\langle v, e_m \rangle}^2
$$
###### _proof:_

We know that [[#_proposition _ the norm of an orthonormal linear combination|the norm of an orthonormal linear combination]] is given by
$$
\norm{v}^2 = \abs{a_1}^2 + \cdots \abs{a_m}^2
$$
for coefficients $a_1, \ldots, a_m$.

Then, using the coefficients from above, we get, for an orthonormal basis $e_1, \ldots, e_m$ in $V$ that
$$
\norm{v}^2 = \abs{\langle v, e_1 \rangle}^2 + \cdots + \abs{\langle v, e_m \rangle}^2.
$$
for any $v \in V$.