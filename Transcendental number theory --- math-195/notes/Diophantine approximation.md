---
tags:
- math-195/4
- math-195/5
- math-195/6
---

Over the first part of the 20th century, mathematicians tried to get better and better bounds on $\mu$ such that there are infinitely many rational approximations to algebraic numbers with $\lvert \alpha - p / q \rvert \leq 1 / q^\mu$.

##### _theorem:_ Roth's theorem

Suppose $\alpha$ is a real algebraic number. Then, for each $\varepsilon > 0$, there exist only finitely many $p / q \in \mathbb{Q}$ such that $\lvert \alpha - p / q \rvert \leq 1 / q^{2 + \varepsilon}$.

---

This useful in actually solving Diophantine problems.

##### _theorem:_ Thue's equation has finitely many integer solutions

Let $a, b, c$ be non-zero integers. Then the equation $a x^{3} + b y^{3} = c$ has only finitely many integer solutions.

###### _proof:_

Write $X = ax$, $Y = y$, $B = a^{2} b$, and $C = a^{2} c$. That is, multiply through by $a^{2}$ and make some substitutions to get $X^{3} + B Y^{3} = C$. It suffices to show that there are only finitely many *positive* integer solutions to each $X^{3} - B Y^{3} = C$. The cases of negative solutions are taken care of by positive solutions to $X^{3} - (-B) Y^{3} = C$ and so on. The number of solutions with either $X$ or $Y$ equal to $0$ are clearly finite.

Suppose $B = d^{3}$ for some $d \in \mathbb{Z}$. Then factoring allows us to write the equation as
$$
(X - d Y)(XY^{2} + dXY + dXY + d^{2} Y^{2}) = C.
$$
For each factorisation $C = U V$, we get $X - dY = U$ and $X^{2} + dX Y + d^{2} Y^{2} = V$. Since this is a quadratic form, there are only finitely many solutions to each of these equations.

Now suppose $B$ is not a perfect cube. Let $\alpha = \sqrt[3]{B}$. It is an irrational algebraic number. Again we can factor
$$
X^{3} - B Y^{3} = (X - \alpha Y)(XY^{2} + \alpha XY + \alpha XY + \alpha^{2} Y^{2}) = (X + \alpha Y / 2)^{2} + \frac{3}{4}(\alpha  Y)^{2}
$$
In particular, this tells us that $\lvert C \rvert \geq \lvert X - \alpha Y \rvert \frac{3}{4} \alpha^{2} Y^{2}$. Thus,
$$
\left\lvert  \frac{X}{Y} - \alpha  \right\rvert \leq \frac{\lvert C \rvert 4}{\alpha^{2} Y^{3}}.
$$
Roth's theorem then tells you that there are only finitely many such numbers.

---

##### _definition:_ $C$-set, $\gamma$-set

A set $S \subseteq \mathbb{R}$ is a **$C$-set** for some $C > 1$ if for each pair $x, y \in S$ we have $x \leq Cy$ and $y \leq Cx$.

$S$ is a **$\gamma$-set** if for each pair $x, y \in S$ such that $x < y$ we have $\gamma x \leq y$

---

Note that a $C$-set of integers is finite, but there are arbitrarily large $C$-sets. However, given an element of the $C$-set there is a bound on its size. A $\gamma$ set may be infinite, but a $(C, \gamma)$-set of real numbers is finite and there is a bound on the size of all $(C, \gamma)$-sets for each choice of $C, \gamma$.

##### _lemma:_ bounding $(C, \gamma)$-sets

Let $C, \gamma > 1$. Let $S \subseteq \mathbb{R}$ be a $(C, \gamma)$-set. Then $\#S \leq 1 + \log C / \log \gamma$.

---

##### _definition:_ window of exponential width

A **window of exponential width $C$** is an interval $[w, w^C)$ for $w, C> 1$.

---

Note that $\{ \ln x \mid x \in [w, w^C) \}$ is then a $C$-set.

These definitions allow us to say that even though an irrational number may have infinitely many good approximations (if it is not algebraic), you have to go exponentially far to get them.

##### _theorem:_ good approximations are exponentially far away

Let $\alpha \in \mathbb{R} \setminus \mathbb{Q}$, and let $\delta > 0, C > 1$. Let $N_{C}(\alpha)$ be the number of rational approximations $p / q$ of $\alpha$ such that
$$
\left\lvert  \alpha - \frac{p}{q}  \right\rvert < \frac{1}{2q^{2 + \delta}}.
$$
with $q$ in a specific window of exponential width $C$.

Then $N_{C}(\alpha) = 1 + \frac{\log C}{\log(1 + \delta)}$.

###### _proof:_

Call the approximations we want to count satisfactory.

Suppose $p_{i} / q_{i}$ are satisfactory approximations arranged in increasing order for $1 \leq i \leq n$. Then
$$
\begin{align}
\frac{1}{q_{i} q_{i + 1}} & \leq \left\lvert  \frac{p_{i}}{q_{i}} - \frac{p_{i + 1}}{q_{i + 1}}  \right\rvert  \\
 & = \left\lvert \frac{p_{i}}{q_{i}} - \alpha  + \alpha - \frac{p_{i + 1}}{q_{i + 1}}  \right\rvert \\
 & \leq \left\lvert  \frac{p_{i}}{q_{i}} - \alpha  \right\rvert + \left\lvert  \frac{p_{i + 1}}{q_{i + 1}} - \alpha  \right\rvert \\
\end{align}
$$
Since $1 / q_{i + 1} \leq {1}/{q_{i}^{1 + \delta}}$  so then $(1 + \delta) \log q_{i} < \log q_{i + 1}$. But then $\log q_{n} < C \log q_{1}$. Thus
$$
(1 + \delta)^{n - 1} \log q_{1} \leq \log q_{n} < C \log q_{1}.
$$
Then this gives us the desired bound.

---