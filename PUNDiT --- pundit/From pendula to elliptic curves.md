---
tags:
- alg-geo
---

##### _definition:_ congruent numbers

A number $n$ is congruent if it is the area of a right triangle with rational sides of length $a$, $b$, and $c$.

It turns out that integer is a congruent number if and only if there are rational points on an equation
$$
y^2 = x^3 - n^2 x
$$

##### _definition:_ Heron triangle
A triangle with rational sides of rational length $a$, $b$, and $c$ and having rational area $n$ is said to be a Heron triangle.

All Heron triangles correspond to points on the curve
$$
y^2 = 
$$
### What is an elliptic curve

Why is an equation of the form $y^2 = x^3 + Ax + B$ an _elliptic_ curve?

It turns out that elliptic curves come from physics.

What is the period of a pendulum of length $l$ given an initial angle $\theta_0$?

Galileo said the period is approximately $2 \pi \sqrt{\frac{l}{g}}$. He was very close, but only close.

##### _proposition:_ pendulum periods

%% check slides %%

##### _proposition:_ ellipse arc lengths

%%check slides%%

The circumference of an ellipse has a very similar form! This is where the word elliptic comes from!

##### _proposition:_ lemniscate arc length

The arc length of the lemniscate
$$
(x^2 + y^2)^2 = a^2 (x^2 - y^2)
$$
is some expression in terms of elliptic integrals of the first kind. %% check slides %%

It turns out that evaluating elliptic integrals can get a little bit horrible. Even for an easy example, like
$$
\int_0^w \frac{1}{\sqrt{1 - x^2}} \, dx = \arcsin{x},
$$
the integral is not defined always.

It turns out that using similar techniques, we can reduce reciprocals of square roots of cubics to elliptic integrals that are solvable, but are still horrible.

##### _definition:_ Jacobi elliptic function

The Jacobi elliptic function is $\sin_{\text{gen}}{z} = w(z)$, given by
$$
z = \int_0^{w(z)} \frac{1}{\sqrt{(1 - x^2)(1 - k^2 x^2)}} = F(\arcsin{w}, k).
$$

The periodicity of this function gives us a periodic lattice in the complex plane. Quotient out by the whole periodic lattice so that you only have to look at one square. Since the square is "Pacman-y" it's really a torus. Then you can connect solutions to $y^2 = (1 - x^2)(1 - k^2 x^2)$ to that torus.

It also turns out that we can construct an abelian group on the points on the curve by using a generalisation of the angle addition formula for $\sin_{\text{gen}}$ that Euler proved.

We can then transform the quartic curve to a cubic curve, specifically an elliptic curve! Moreover, since we drop down a degree, this turns all the parabolic geometric constructions to prove the angle addition formula into simpler linear constructions, which we can use to construct a similar abelian group on solutions to the elliptic curve.

##### _definition:_ elliptic curves

An elliptic curve is an equation of the form
$$
y^2 = x^3 + Ax + B
$$
such that $4A^3 + 27B^2 \neq 0$.

### Adding points on an elliptic curve

##### _definition:_ $E(k)$

For some field $k$ and some elliptic curve $E$, let $E(k)$ be the set of solutions to $E$ over $k$, including the point at infinity, with the following operation
$$
\oplus : E(k) \times E(k) \to E(k)
$$
defined by
$P \oplus Q$ is the point you get by drawing the line from $P$ to $Q$, and then reflecting it's third intersection with the elliptic curve in the $x$-axis.

##### _theorem:_ $E(k)$ is abelian

For any field $k$, $E(k)$ is an abelian group.