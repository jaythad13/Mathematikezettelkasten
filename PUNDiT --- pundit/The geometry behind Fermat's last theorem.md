---
tags:
- nt
- alg-nt
- alg-geo
- PUNDiT
---

av15@rice.edu
##### _theorem:_ Fermat's last theorem

If three integers $x$, $y$, and $z$ satisfy
$$
x^n + y^n = z^n
$$
for some integer $n \ge 3$, then $x y z = 0$.

Note that there are solutions to the equation! They are just always trivial. This is what makes it difficult.

Why are there solutions when $n = 2$?

### The geometry of Pythagorean triples

Consider the solutions where $z \neq 0$. Then
$$
(\frac{x}{z})^2 + (\frac{y}{z})^2 = 1.
$$
For $X = \frac{x}{z}$ and $Y = \frac{y}{z}$ we get
$$
X^2 + Y^2 = 1.
$$This is a circle! This means that we can think of Pythagorean triples as rational points on a circle!

Note that any "equivalent" triples get mapped to the same point on the circle. This means that the circle naturally embeds the "independent" solutions, and partitions the equivalent solutions into equivalence classes.

Now we use geometry!

We start from the point $(0, 1)$, and draw some line between it and some rational point (not necessarily on the circle) $(s, 0)$ - the line $y = -\frac{1}{s}  + 1$. This line must intersect the circle, and thus, we have a new rational point $(X_0, Y_0)$ on the intersection of the line and the circle.

We can solve for this point by substituting in the value of $Y_0$ on the line into the circle equation!

$$
X_0^2 + (-\frac{1}{s} X_0 + 1)^2 = 1
$$

which gives us

$$
(X_0, Y_0) = (\frac{2s}{1+s^2}, \frac{s^2 - 1}{s^2 + 1}).
$$

Since $s$ is rational, we can see that $(X_0, Y_0)$ really is a rational point! Specifically, if $s = \frac{a}{b}$, 
$$
\begin{gathered}
	x = k \cdot 2ab \\
	y = k \cdot (a^2 - b^2) \\
	z = k \cdot (a^2 + b^2).
\end{gathered}
$$
Note that $k$ can be a rational as long as $x$, $y$, $z$ are integers. Specifically, $k$ is an integer if one of $a$ or $b$ is even, or a half integer if $a$ and $b$ are both odd.

This is all the Pythagorean triples!

### Geometry for $n \ge 3$

We can do the same trick with the cases for Fermat's last theorem. For $z \neq 0$, consider
$$
X^n + Y^n = 1
$$
with $X = \frac{x}{z}$ and $Y = \frac{y}{z}$.



### Projective geometry

The Euclidean plane is $\bb{R}^2$, with two coordinates $(X, Y)$. The projective plane $\bb{RP^2}$ is also two dimensional, but has three coordinates $(x, y, z)$.

The intuitive way to get from $\bb{RP}^2$ to $\bb{R}^2$ is to map $(x, y, z)$ to $(\frac{x}{z}, \frac{y}{z})$. But this isn't injective! It maps two points in $\bb{RP}^2$ to $\bb{R}^2$. Then we can't recover points from $\bb{R}^2$.

What can we do? We just consider things in that are mapped to the same thing to be equivalent in $\bb{RP}^2$. That is, in $\bb{RP}^2$, $(x, y, z) \equiv \lambda(x, y, z)$. Then we can map $(X, Y)$ to $(X, Y, 1)$ and always be right...

Except if $z = 0$, we can't get $(X, Y)$. What can we do? Note that
$$
(x, y, 0) \equiv (1, \frac{y}{x}, 0).
$$
which seems to correspond to the slope of a line! This is an extra point that $\bb{R}^2$ doesn't have

Except if $x = 0$ as well, we can't divide through by $x$. But
$$
(0, y, 0) \equiv (0, 1, 0).
$$
This is like the slope of a vertical line.

Finally if $y = 0$ as well, we give up and just exclude $(0, 0, 0)$.

So we get a bunch of extra points corresponding to slopes of lines!

We're quotienting out by lines!

Formally, 
$$
\bb{RP}^2 = \frac{\bb{R}^3 \setminus \set{0}}{\set{(x, y, z) \equiv \lambda (x, y, z)}}.
$$