---
tags:
- math-19
- calc
lecture: math-19-18
---

We already know how to [[Double integrals#How to do integrals in two dimensions|integrate a function over a two dimensional region]] in $\bb{R}^2$. But sometimes we want to do the same things we wanted to do in two dimensions in three dimensions. How do we do that?

We can just do the same thing! Partition the region into small pieces, then take the sum of the function times the area, and then look at the limit as the small pieces get very small!

### Things to integrate in the third dimension

There's a really easy example of integration: the integral of a function that is $1$ everywhere.

##### _example:_ the trivial integral

$$
\iiint_W 1 \, dV  = V_W
$$

where $V_W$ is the volume of the region $W$.

We can also get the average of a function over a region by a method similar to the one for double integrals.

##### _example:_ the average of $x$ on the unit ball

For $W$, the unit ball centred at $\bvec{0}$
$$
\overline{x} = \frac{\iiint_W x \, dV}{\iiint_W \, dV}.
$$
Note that we can use similar [[Parameterising 2-dimensional regions#_example _ symmetry in double integrals|symmetry arguments]] about $x$ to show that
$$
\overline{x} = 0.
$$

Of course, we can also use geometric intuitions to bound what reasonable answers for an integral should look like.

##### _example:_ heuristics of $x^2$ on the unit ball

For $W$, the unit ball centred at $\bvec{0}$, since $0 \le x^2 \le 1$ on $W$, we can bound its integral on $W$:
$$
0 \le \iiint_W x^2 \, dV \le \iiint_W \, dV = \frac{4}{3} \pi.
$$

### How to integrate things in the third dimensions

How do we actually compute the integrals by hand? We use another idea we've already seen for double integrals: iterated integrals!

It turns out that all of the definitions and theorems about double integrals transfer really nicely to triple integrals.

##### _example:_ volume of a quarter cylinder by iterated integrals

What is the volume of $W$, the region in the first octant bounded by the surfaces $x^2 + z^2 = 4$ and the plane $y = 3$. This is just the quarter cylinder with radius $2$ and height $3$!

Thus, we can parameterise it by considering $z \in [0, \sqrt{4 - x^2}]$, $x \in [0, 2]$, and $y \in [0, 3]$

$$
V_W = \iiint_W \, dV = \int_0^3 \int_0^2 \int_0^{\sqrt{4 - x^2}} \, dz \, dx \, dy. 
$$

##### _example:_ finding the mass of objects of non-uniform density

What is the mass of $W$, an object of density $\delta$ given by $\delta(x, y, z) = x^2 z$, defined by the region bounded by $6x + 3y + 2z = 6$ in the first octant.

We can parameterise $W$ by looking at the interval from $0$ to the plane for each variable, and then projecting down, to the line, and so on. Then
$$
\iiint_W \, dV = \int_0^2 \int_0^{1 - \tfrac{y}{2}} \int_0^{\tfrac{6 - 6x - 3y}{2}} \delta(x, y, z) \, dz \, dx \, dy.
$$