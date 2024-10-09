---
tags:
- math-176/18
- alg-geo
---

We've seen that if $C$ is a non-singular projective variety of dimension $d = 1$ and genus $g(C) = 0$, $C$ is either a line (for $e = 1$) or a conic section (for $e = 2$, by [[Algebraic Geometry --- math-176/notes/Pythagorean triples and conic sections#_theorem _ the general solution of a quadratic equation|the parametrisation we have for quadratrics]]). In either case $C \cong \mathbb{P}^1(F)$. Can we do something similar when $e = 3$? Almost!

First, note that we can reduce any cubic to an elliptic curve —

##### _proposition:_ reducing cubics to elliptic curves

Say $\operatorname{char}(F) \neq 2, 3$. Consider the curve
$$
E : y^{2} + a_{1} xy + a_{3} y = x^{3} + a_{2} x^{2} + a_{4} x + a_{6}.
$$
written in Weierstrass form.
Then,
1) By a change of variables, $E$ is can be written as an elliptic curve in short Weierstrass form — $Y^{2} = X^{3} + AX + B$.
2) $E$ has at most one singular point $p$ and $p \neq (0 : 1 : 0)$.
3) $E$ is a [[Algebraic Geometry --- math-176/notes/Non-singular projective varieties#_definition _ non-singular projective variety|non-singular projective variety]] of dimension $1$ if and only if $\Delta(E) = -16(4A^3 + 27 B^{2}) \neq 0$.

###### _proof sketch:_

For 1), we can substitute
$$
\begin{split}
X & = x + \mu \\
Y & = y + \frac{a_{1} x + a_{3}}{2}
\end{split}
$$
for some $\mu \in F$. 

Complete the square in $y$ on the left hand side of the equation to get
$$
y^{2} + 2 \left( \frac{a_{1}x + a_{3}}{2}\right) y + \left( \frac{a_{1} x + a_{3}}{2} \right)^{2} = x^3 + a_{2} x^{2} + a_{4} x + a_{6} + \left( \frac{a_{1} x + a_{3}}{2} \right)^{2}.
$$
We choose $\mu$ so that the $X^{2}$ term vanishes — so as to depress the cubic (see the lecture notes for what exactly that should be). Now we have
$$
Y^{2} = X^{3} + AX + B
$$
as desired.

Consider $f(x, y) = x^3 + A x + B - y^{2}$. This corresponds to the homogenous polynomial $g(x_{1}, x_{2}, x_{0}) = x_{1}^{3} + A x_{1} x_{0}^{2} + B x_{0}^{3} - x_{2}^{2} x_{0}$. When might $g$ have a singular point?

$p = (p_{1} : p_{2} : p_{0})$ is only a singular point if $g(p) = 0$ and all $\frac{ \partial g }{ \partial x_{i} } = 0$ as well. That is, we need
$$
\begin{split}
0 & = p_{1}^{3} + A p_{1} x_{0}^{2} + B p_{0}^{3} - p_{2}^{2} p_{0} \\
0 & = 3 p_{1}^{2} + A p_{0}^{2} \\
0 & = - 2 p_{2} p_{0} \\
0 & = 2 A p_{1} p_{0} + 3 B p_{0}^{2} - p_{2}^{2}
\end{split}
$$
Notice that we must have $p_2 = 0$ or $p_{0} = 0$. If $p_{0} = 0$, then by the first equation the $3 p_{1}^{2} = 0$ and thus, $p_{1} = 0$. Also, by the third equation $- p_{2}^{2} = 0$ and thus, $p_{2} = 0$. Since $(0 : 0 : 0)$ isn't a point, this isn't possible. If $p_{2} = 0$, then by the last equation, $p_{0}(2 A p_{1} + 3 B p_{0}) = 0$, and since we've shown $p_{0} \neq 0$ already. Thus, $p = (3B : 0 : 2A )$.

Then plugging $p$ into $g$ and the other equations, we have that the $4A^{3} + 27 B^{2}$ must be $0$.