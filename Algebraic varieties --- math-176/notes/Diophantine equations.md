---
tags:
- alg-geo
- math-176/2
---

We've seen how to find [[Algebraic varieties --- math-176/notes/Pythagorean triples and conic sections#_theorem _ the general solution of a quadratic equation|integer solutions of a conic section]] — that is the general solution of a quadratic polynomial in three variables? What about polynomials in general? This the question first considered by Diophantus of Alexandria.

##### _definition:_ Diophantine equation

A Diophantine equation refers to seeking integers $a, b, c$ with $f(a, b, c) = 0$ for some polynomial $f$ with integer coefficients.

Since we don't really think of the integer point, $(a, b, c)$, but rather the integer points upto scaling, $(a : b : c)$, we want to consider the case where the polynomial doesn't really care about the scaling. That is, we want to focus on homogenous polynomials.

##### _definition:_ homogenous polynomial

A homogenous polynomial of degree $e$ ($e \in \mathbb{N}$) is a polynomial $f$ such that $f(\lambda x_{1}, \dots, \lambda x_{n}) = \lambda^e f(x_{1}, \dots, x_{n})$ for any scalar $\lambda$.

Note that these homogenous polynomials preserve roots under scaling. This also formalises what we've been doing by considering rational solutions $(x, y)$ instead of integer solutions $(a, b, c)$ — just choose $\lambda = 1 / c$ for $c \neq 0$. Then, it is sufficient to consider $g(x, y) = f(x, y, 1)$ along with the special case $f(x, y, 0)$.

### Heron triangles

One good example of a Diophantine equation is that of Heron triangles. Heron's formula tells us that we can get the area of a triangle just by knowing the lengths of its sides.

##### _theorem:_ Heron's formula

The area $A$ of a triangle with sides $a, b, c$ satisfies
$$
A^{2} = s(s - a)(s - b)(s - c)
$$
where $s$ is the semi-perimeter $\frac{a + b + c}{2}$.

Naturally, a Heron triangle is a rational solution of this equation.

##### _definition:_ Heron triangles

A Heron triangle is a triangle with rational area and sides of rational length.

Note that any Pythagorean triple $(a, b, c)$ is obviously a Heron triangle — the area formula for a right angle as $\frac{ab}{2}$ gives us a rational area! Are there any Heron triangles that are not right triangles? Yes! Just put two right triangles together to form an isosceles Heron triangle. Are there any others?

##### _proposition:_ Heron triangles are points on a quartic

Given an isosceles Heron triangle $(l, b, l)$ (formed from two Pythagorean triples). All Heron triangles with the same base $b$ and same area $A$ correspond to rational points $(x, y)$ on the quartic
$$
y^{2} = (1 - x^{2})(1 - k^{2} x^{2})
$$
where $k = 2l / b$.

###### _proof sketch:_

Notice that fixing the base and area is equivalent to fixing the base and height.

First suppose $(a, b, c)$ is a Heron triangle with area $A$. Note that $A = \frac{bh}{2}$ where $h$ is the height relative to base $b$. Use the Pythagorean theorem to get $h$ in terms of $l$ and $b$. Substitute $x = \frac{b}{a + c}$ and $y = \frac{a - c}{b} \frac{(a + c)^{2} - b^{2}}{(a + c)^{2}}$. Then using Heron's formula which writes the area squared as the product of four things, write $y^{2} = (1 - x)(1 + x)(1 - kx)(1 + kx)$.

### Congruent numbers

Another triangular example of a Diophantine equation answers the following question. Which rational numbers $\mathfrak A$ are the area of some right triangle with rational sides $a, b, c$?

##### _definition:_ congruent numbers

A congruent number is a rational $\mathfrak{A}$ that is the area of some right triangle with rational sides $a, b, c$.

##### _proposition:_ 

$\mathfrak A$ is congruent if and only if there's a rational point $(x, y)$ on
$$
y^{2} = x^{3} - A^{2} x
$$
satisfying $x > A$.

###### _proof sketch:_

Check 
$$
a = \frac{x^{2} - \mathfrak A ^{2}}{y} \quad b = \frac{2nx}{y} \quad c = \frac{x^{2} + \mathfrak A^{2}}{y}.
$$
Why? We didn't have time to discuss this.