---
tags:
- math-82/10
- diff-eq
---

To determine when solutions to a (linear) differential equation span the solution space, we want an easy way to compute whether they are linearly independent.

##### _definition:_ Wronskian

The **Wronskian** of two $C^r(U)$ real functions $f$ and $g$ is the function $W_{f, g}$ given by
$$
W_{f, g}(t) = \det \begin{pmatrix}
f(t) & g(t) \\
f'(t) & g'(t)
\end{pmatrix}.
$$

---

##### _proposition:_ linearly dependent implies vanishing Wronskian

Suppose $f, g: U \to \mathbb{R}$ are two $C^r$ real functions. If $f$ and $g$ are linearly dependent, then $W_{f, g}(t) = 0$ for all $t \in U$.

###### _proof sketch:_

Since $f, g$ are linearly dependent, write $c_{1} f + c_{2} g = 0$ for some $c_{1}, c_{2} \in \mathbb{R}$ with $c_{2} \neq 0$.

If $f(t)$ is $0$, then it is easy to see that the Wronskian is zero in a neighbourhood of $t$. Else, suppose $f$ is non-vanishing in a neighbourhood of $t$. Then $g(t) / f(t) = -c_{1} / c_{2}$. Differentiating gives $W_{f, g}(t) = f(t) g'(t) - f'(t) g(t) = 0$ (the numerator of the derivative must be $0$).

---