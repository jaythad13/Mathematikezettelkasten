---
tags:
- math-82/13
- diff-eq
---

If we can't find an explicit solution for a differential equation $a(x) y'' + b(x) y' + c(x) y(x) = 0$ but $a, b, c$ are (simple) polynomials in $x$, then it is often reasonable to approximate the solution by a power series. We will just blindly expand power series in the hopes that they work, but there are good theoretical reasons to do this. This doesn't work well for non-linear equations because it gives rise to non-linear recurrences. 

We demonstrate by example.

##### _example:_ power series methods around ordinary points for Airy's equation

Consider the differential equation $y'' - xy = 0$ (Airy's differential equation). Note that for negative $x$ this should have oscillatory behaviour and for positive $x$ it looks like should have exponential growth or decay. Further suppose the boundary conditions $y(0) = 1$ and $y'(0) = 0$ are imposed.

Then we assume that $y$ has a power series expansion around where the boundary conditions are imposed. Specifically, 
$$
y = \sum_{n = 0}^\infty a_{n} (x - 0)^n = \sum_{n = 0}^\infty a_{n} x^n
$$
for $x$ near $0$. In order for $y$ to satisfy the boundary conditions, we must have $a_{0} = 1$ and $a_{1} = 0$. We must also have $y''(0) = 0$ so $a_{2} = 0$ as well. In general, we can substitute the power series back into the differential equation and thus, require that
$$
\sum_{n = 2}^\infty n(n - 1)a_{n} x^{n - 2} - \sum_{n = 0}^\infty a_{n} x^{n + 1} = 0
$$
or equivalently,
$$
\sum_{n = 2}^\infty n(n - 1)a_{n} x^{n - 2} = \sum_{n = 3}^\infty a_{n - 3} x^{n - 2}
$$
giving the recurrence relation $a_{n} = \frac{a_{n - 3}}{n(n - 1)}$. This gives $a_{3} = a_{0} / 6 = 1/6$ and so on.

If the boundary condition was not given to us, then the two parameters of $a_{0}$ and $a_{1}$ would give the whole solution space.

---

This example worked well because $a(x)$ was simple (just $1$) and so caused no problems. However, when $a(x)$ has roots, we may have $y'' + p_{1}(x) y' + p_{2}(x) y = 0$ with $p_{1}, p_{2}$ not necessarily defined everywhere. Specifically, if $p_{1}$ and $p_{2}$ are analytic near $x_{0}$, we say that is an **ordinary point** and then the method above works. If either one is not, then $x_{0}$ is a **singular point**. If the singularity is not too bad — if $(x - x_{0}) p_{1}(x)$ and $(x - x_{0})^{2} p_{2}(x)$ are analytic, then $x_{0}$ is a **regular singular point** of the differential equation and we can use **Frobenius series**. This is basically the same idea with a slightly modified ansatz.

##### _example:_ using Frobenius series on Bessel's equation

Bessel's equation
$$
x^{2} y'' + x y' + (x^{2} - \nu^{2}) y = 0
$$
has a regular singular point at $0$. Using the ordinary point method only gets us the trivial solution $y = 0$. Instead we assume solutions are of the form
$$
y = x^r \sum_{n = 0}^\infty a_{n} x^n
$$
for some $r \in \mathbb{R}$. This gives more interesting solutions.

Plugging the ansatz into the equation gives
$$
x^{2} \sum_{n = 0}^\infty (n + r)(n + r - 1) a_{n} x^{n + r - 2} + x \sum_{n = 0}^\infty (n + r) a_{n} x^{n + r - 1}  + (x^{2} + \nu^{2}) \sum_{n = 0}^\infty a_{n} x^{n + r} = 0.
$$
The coefficient of $x^r$ gives $a_{0}(r^{2} - \nu^{2}) = 0$. So that $a_{0}$ is free, we choose $r = \pm \nu$. We also get $a_{1}((r + 1)^{2} - \nu^{2}) = 0$ and then $((n + r)^{2} - \nu^{2}) a_{n} + a_{n - 2} = 0$ for all $n \geq 2$. This gives $a_{1} = 0$. Then $a_{n} = \frac{- a_{n - 2}}{n(n + 2 \nu)}$. Thus all odd $a_{n}$ are $0$ and the solution is completely determined by the choice of $a_{0}$. The two choices of $r = \pm \nu$ end up giving two independent solutions.

---