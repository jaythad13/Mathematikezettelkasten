---
tags:
- alg
- math-172
---

Let $A$ be a (commutative, unital) ring.

##### _definition:_ polynomial ring

The **polynomial ring (in one variable) over $A$** is $A[x]$, the ring of functions $\mathbb{N}_{0} \to A$ by $n \mapsto a_{n}$ written as polynomials $a_{0} + a_{1} x + \dots + a_{n} x^n$. The multiplication is the obvious convolution product
$$
(a_{0} + a_{1} x + \dots + a_{n} x^n)(b_{0} + b_{1} x + \dots + b_{m} x^m) = \sum_{i = 0}^n \left( \sum_{j, k}  \right)
$$

It is a [[Algebraic geometry --- rising-sea/notes/Graded rings#_definition _ $ mathbb{Z}$-graded rings, homogeneous elements, degree|non-negatively graded ring]] with degree given by the largest $n$ such that $a_{n} \neq 0$.

The polynomial ring in $n$ variables over $A$ is $A[x_{1}, \dots, x_{n}] = A[x_{1}, \dots, x_{n - 1}][x]$.

---
