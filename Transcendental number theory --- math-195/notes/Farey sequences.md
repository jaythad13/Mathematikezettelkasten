---
tags:
- math-195/9
- nt
---

Farey sequences give a new way to think about the rational numbers between $[0, 1]$.

##### _definition:_ Farey sequences, Farey neighbours

The **Farey sequence of order $n$**, denoted $F_{n}$ is the ascending sequence of rationals in the interval $[0, 1]$ with denominator at most $n$.

Neighbouring fractions in $F_{n}$ are called **Farey neighbours of order $n$**.

---

##### _proposition:_ Farey neighbours are given by $\mathrm{SL}_{2}$-orbits

$c / d < a / b$ are Farey neighbours if and only if $ad - bc = 1$.

###### _proof:_

Suppose $c / d, a / b$ have $ad - bc = 1$. Then for any $x / y$ with $c / d < x / y < a / b$, we must have $y > \max \{ b, d \}$. Thus, $c / d, a / b$ are Farey neighbours of order $\max \{ b, d \}$.

Conversely, suppose $c / d < a / b$ are Farey neighbours. Specifically, let them be neighbours of order at least $bd$. Then $a / b - c / d = (ad - bc) / bd$. If $ad - bc > 1$ then $c / d + 1 / bd$ would lie between $c / d$ and $a / b$.

---

##### _proposition:_ Farey neighbours are given by mediants

Suppose that $c / d < x / y < a / b$. Then $x / y = (a + c) / (b + d)$.

---

##### _proposition:_ 