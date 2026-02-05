---
tags:
- math-195/5
- nt
---

##### _definition:_ continued fractions

A **finite continued fraction** is an expression
$$
[a_{0}; a_{1}, \dots, a_{n}] := a_{0} + \frac{1}{a_{1} + \frac{1}{a_{2} + \frac{1}{\dots + \frac{1}{a_{n}}}}}
$$
for $a_{i} \in \mathbb{Z}$ and $a_{i}$ non-negative for $i \geq 1$.

An **infinite continued fraction** is a limit of finite continued fractions $[a_{0}; a_{1}], [a_{0}; a_{1} a_{2}], \dots$.

---

##### _example:_ $\sqrt{ 2 }$ as a continued fraction

Notice that
$$
\sqrt{ 2 } = 1 + \frac{1}{1 + \sqrt{ 2 }}.
$$
Thus, we can get a good approximation
$$
\sqrt{ 2 } \approx \frac{1}{2 + \frac{1}{2 + \frac{1}{2 + \dots}}}.
$$
In fact, it is good enough that it conveges.


---