---
tags:
- math-19
- calc
lecture: math-19-21
---

Recall [[Green's theorem#_theorem _ Green's theorem|Green's theorem]]. It gives us a way to translate between integrating over areas and integrating over their boundaries.

##### _example:_ calculating areas using a planimeter

A planimeter integrates the field $\bvec{F}$ given by $\bvec{F}(x, y) = (-y, x)$ over any closed path we choose. But for any such closed path $c$, enclosing a region $R$, with only very reasonable conditions
$$
\oint_c \bvec{F} \cdot d\bvec{s} = \iint_R \curl \bvec{F} \, dA = 2 \times \text{area}(R).
$$
This is how a planimeter works! The choice of vector field is so that it is convenient to mechanically integrate over the path.

For example, if we want to calculate the area inside an ellipse $A$, we can do a line integral! An ellipse $c$ is parameterised by
$$
c(t) = (a \cos{t}, b \sin{t})
$$for $t \in [0, 2 \pi]$.

By the formula above,
$$
A = \frac{1}{2}\oint_c \bvec{F} \cdot d\bvec{s} = \frac{1}{2} \oint\bvec{F}(c(t)) \cdot c'(t) \, dt = \frac{1}{2} \int_0^{2 \pi} (-b \sin{t}, a \cos{t}) \cdot (-a \sin{t}, b \cos{t}) \, dt
$$
which is just
$$
A = \frac{ab}{2} \int_0^{2 \pi} \cos^2{t} + \sin^2{t} \, dt = \pi a b.
$$

We can also go the other way - avoiding line integrals by computing areas.

##### _example:_ 

Consider the field $\bvec{F}$ given by $\bvec{F}(x, y) = (0, x^2)$. What is its integral over the rectangle with width $1$ and height $3$ and bottom left corner at $(1, 0)$?

![[S0_DoubleIntegralsAreEasy.jpeg]]

This isn't an unreasonably difficult line integral to calculate, but it does require integrating over the four different parts of the rectangle. We can make it much easier by using Green's theorem - integrating over the area of a rectangle is trivial!
$$
\oint_c \bvec{F} \cdot d\bvec{s} = \iint_R \curl \bvec{F} \, dA = \int_1^2 \int_0^3 2x \, dy \, dx = \int_1^2 6x \, dx = 3x^2 \Big |_1^2 = 9.
$$

Of course, alternatively, we could use some combination of geometric and analytic intuition to approximate this.

### Conservative vector fields

Note that usually the path that you take between two points causes a difference in the line integrals along those. Basically, joining the paths (reversing the direction of one) will give a closed path enclosing a region. Then the integral of the curl of the field over that region is the difference between the line integrals over the different paths by Green's theorem.

##### _example:_ line integrals along different paths

![[S1_lineIntegralsAlongDifferentPaths.jpeg]]

Here we have
$$
\int_{c_1} \bvec{F} \cdot d\bvec{s} - \int_{c_2} \bvec{F} \cdot d\bvec{s} = \int_{c_1 + (- c_2)} \bvec{F} \cdot d\bvec{s} = \iint_R \curl \bvec{F} \, dA
$$

Since the field is given by $\bvec{F}(x, y) = (-y, x)$ with $\curl \bvec{F} = 2$, we get the difference as $2 \times \text{area}(R) = 4 \pi$.

Bu what if the curl of the field is zero? 

Then the difference is zero too! Then the choice of path doesn't matter, and the line integral over any path between two points is the same.

This motivates us to think about fields that we know to have zero curl, specifically, gradient fields. In fact, we will see that they are exactly the gradient fields.

##### _definition:_ conservative vector field

We say a vector field $\bvec{F} : \bb{R}^n \to \bb{R}^n$ is conservative if $\bvec{F} = \nabla f$ for some function $f : \bb{R}^n \to \bb{R}$.

##### _example:_ conservative vector field

The vector field $\bvec{F}$ on $\bb{R}^3$, given by $\bvec{F}(x, y, z) = (2x, 2y, 2z)$ is a conservative vector field because for $f : \bb{R}^3 \to \bb{R}$ given by $f(x, y, z) = x^2 + y^2 + z^2 + C$ for any $C \in \bb{R}$, we have $\bvec{F} = \nabla f$.

### The fundamental theorem of line integrals

Note that for conservative vector fields, computing line integrals becomes trivial, firstly because we can always replace a tricky path to integrate over with a simple one, but also because we can do the following trick:
$$
\int_c \bvec{F} \cdot d\bvec{s} = \int_c \nabla f \cdot \ddx{\bvec{s}}{s} \, ds = \int_c D_{d\bvec{s}}f \, ds
$$
which is just the difference between $f$ evaluated at the endpoints.

This gives us

##### _theorem:_ the fundamental theorem of line integrals

If $c$ is a path $c : [a, b] \to \bb{R}^n$ and $\bvec{F}$ is a conservative vector field on $\bb{R}^n$ with $\bvec{F} = \nabla f$, then
$$
\int_c \bvec{F} \cdot d\bvec{s} = f(c(b)) - f(c(a)).
$$