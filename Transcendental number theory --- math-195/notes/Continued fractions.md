---
tags:
- math-195/5
- math-195/8
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
In fact, it is good enough that it converges.

---

##### _theorem:_ continued fractions give best approximations

Suppose $\alpha \in \mathbb{R} \setminus \mathbb{Q}$. Let $p_{n} / q_{n}$ be its $n$th convergent. Then for each $p / q \in \mathbb{Q}$ with $q \leq q_{n}$ (such that $p / q \neq p_{n} / q_{n}$) we have $\lvert \alpha - p_{n} / q_{n} \rvert < \lvert \alpha - p / q \rvert$.

---

##### _theorem:_ Euler–Lagrange's theorem on periodic continued fractions

$\alpha$ has an eventually periodic continued fraction if and only if $\alpha$ is a quadratic irrational.

###### _proof:_

It is a fact from linear algebra that
$$
\begin{pmatrix}
a_{0} & 1 \\
1 & 0
\end{pmatrix} \begin{pmatrix}
a_{1} & 1 \\
1 & 0
\end{pmatrix} \dots \begin{pmatrix}
a_{n} & 1 \\
1 & 0
\end{pmatrix} = \begin{pmatrix}
p_{n} & p_{n + 1} \\
q_{n} & q_{n + 1}
\end{pmatrix}
$$
This makes it natural to define
$$
[a_{0}; a_{1}, a_{2}, \dots, a_{n}, x] = \frac{x p_{n} + p_{n - 1}}{x q_{n} + q_{n - 1}}.
$$

Note that it suffices to prove the result for periodic continued fractions — the sum of a rational and a quadratic irrational is also a quadratic irrational. In particular, if $\beta$ has quadratic minimal polynomial $f(x)$, then any $\alpha$ with $\alpha - \beta \in \mathbb{Q}$ has minimal polynomial $f(x - (\alpha - \beta))$.

If $\alpha$ has periodic continued fraction of period $\ell$, then we can write
$$
\alpha = \frac{\alpha p_{m + \ell} + p_{m + \ell - 1}}{\alpha q_{m + \ell} + q_{m + \ell - 1}}
$$
which gives a quadratic polynomial $f(x) \in \mathbb{Q}[x]$ that has $f(\alpha) = 0$.

Now suppose $\alpha$ is a root of some quadratic $f(x) = a x^{2} + bx + c$. We can assume $f(x)$ is irreducible — if it isn't $\alpha$ is rational, for which we already know that $\alpha$ has finite continued fraction. Let $\alpha = [a_{0}; a_{1}, \dots]$. For each $n \geq 0$ let $r_{n} = [a_{n} ; a_{n + 1}, \dots]$. Then we can also write 
$$
\alpha = [a_{0}; a_{1}, \dots, a_{n - 1}, r_{n}] = \frac{r_{n} p_{n - 1} + p_{n - 2}}{r_{n} q_{n - 1} + q_{n - 2}}.
$$
We can plug this into $f(x)$ and clear denominators to get
$$
A_{n} r_{n}^{2} + B_{n} r_{n} + C_{n} = 0
$$
where $A_{n}, B_{n}, C_{n}$ are integer expressions in $p_{n}, q_{n}$. Further, it happens to be true that the discriminants of the polynomials are equal. That is, $B_{n}^{2} - A_{n}^{2} C_{n}^{2} = b^{2} - 4 ac$. 

It then suffices to prove the $A_{n}, B_{n}, C_{n}$ are bounded. It would then follow that there are only finitely many possible $A_{n}, B_{n}, C_{n}$, and thus, only finitely many possible roots $r_{n}$. But then $r_{n}$ must repeat itself. This shows that $\alpha$ has eventually periodic expansion.

We can get a bound $\lvert A_{n} \rvert < 2 \lvert a \alpha \rvert + \lvert a \rvert + \lvert b \rvert$. This also bounds $C_{n} = A_{n}$. Since the discriminants are equal, we have a bound on $B_{n}$ as well.

---