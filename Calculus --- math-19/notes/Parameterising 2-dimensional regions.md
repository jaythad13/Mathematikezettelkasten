---
tags:
- calc
- math-19
lecture: math-19-17
---

Recall that we expressed double integrals like $\iint_R f \, dA$ as the [[Double integrals#_proposition _ Fubini's theorem|repeated application of single integrals]] by parameterising the region $R$ with respect to $x$ and $y$. In the trivial example where $R$ is a rectangle, the limits of integration for $x$ and $y$ are independent constants and thus, changing the order in which we integrate over $x$ and $y$ is trivial. But what about more complicated regions? How do we parameterise them and how do those parameterisations behave with order changes.

### Useful things to do with clever parameterisations

We can integrate over more complicated regions by choosing parameterisations with the curves at the boundary of the regions.

##### _example:_ a more complicated region

Consider the region $R$ given by the upper-half disk of radius $2$. For some $f : \bb{R}^2 \to \bb{R}$, how do we compute $\iint_R f \, dA$ ?

Again, to do this we can compute the integral by splitting $R$ into small pieces along the $x$ and $y$ axes, and then integrating with respect to $y$!

Say we want to integrate with respect to $y$ first. At any point $x$, we need to integrate with respect to $y$ from the bottom of the semicircle to the top: that is, from $0$ to $\sqrt{4 - x^2}$. Then we need to integrate these slices of the graph from the left edge of the semicircle to the right edge of the semicircle: from $-2$ to $2$. 
![[S1_halfDiskVertFirst.jpeg]]
That is,
$$
\iint_R f \, dA = \int_{-2}^2 \int_0^{\sqrt{4 - x^2}} f \, dy \, dx.
$$

What if we want to integrate with respect to $x$ first? Note that unlike for $y$, the bounding curve is two functions of $y$, not one function. Specifically, we need to integrate with respect to $x$ from $-\sqrt{4 - y^2}$ to $\sqrt{4 - y^2}$. Then we just integrate up the slices of the graph with respect to $y$ from $0$ to $2$. 
![[S1_halfDiskHorizFirst.jpeg]]
That is,
$$
\iint f \, dA = \int_0^2 \int_{-\sqrt{4 - y^2}}^{\sqrt{4 - y^2}} f \, dx \, dy.
$$

Note that here, changing the order of integration is very nontrivial. Switching the order of integration isn't just switching the limits! It's switching the whole parameterisation of the region.

Integrating over complicated regions allows us to [[Double integrals#_examples _ the meaning of integrals|get their area]]!

##### _example:_ the area of regions bounded by curves

Note that if we write $f = 1$, then $\iint_R f \, dA$ is just the area of $R$. In the case where the $R$ is the upper-half disk of radius $2$ as in the previous example, we can get the area of a semicircle of radius $2$ as
$$
\int_{-2}^2 \int_0^{\sqrt{4 - x^2}} \, dy \, dx = \int_{-2}^2 \sqrt{4 - x^2} \, dx.
$$
That's just the area under the curve $\sqrt{4 - x^2}$, just like we'd expect!

Using symmetry in the region, we can use clever arguments to evaluate an integral without actually doing any computations.

##### _example:_ symmetry in double integrals

What is $\iint_R x \, dA$, where $R$ is the same region as before? We could calculate the integral by doing all of the work, or we could use symmetry!

For every vertical line in the semicircle $x = a$, there is another line in the semicircle $x = -a$, with the same height! It's like an odd function on an interval $[-a, a]$: the integral has to evaluate to zero!

By switching orders of integration we can integrate functions that don't even have an elementary function expression for their integrals.

##### _example:_ integrating "unintegrable" functions

What is
$$
\int_0^1 \int_x^1 e^{y^2} \, dy \, dx \, ?
$$

The inner integral has no expression as an elementary function, so it seems like we can't compute this. However, instead of thinking of this as an iterated integral, we can think of it as a double integral over the region $R$ between the line $y = x$ and $y = 1$, and then express it as an iterated integral with a different order of integration!

![[S1_convenientTriangleParameterisation.jpeg]]

That is, 
$$
\int_0^1 \int_x^1 e^{y^2} \, dy \, dx = \int_0^1 \int_0^y e^{y^2} \, dx \, dy = \int_0^1 y e^{y^2} \, dy = \frac{e^{y^2}}{2} \Big|_0^1 = \frac{e - 1}{2}.
$$
This is completely reasonable, because it's between the area of the triangle times the minimum value of the function and the area of the triangle times the maximum value of the function.

The point is that choosing the order of the integration wisely can make things easier!

Typically, if the vertically bounding curves are functions, integrating with respect to $y$ first is easier and the other way round for nice horizontal bounding curves and $x$. Sometimes neither is the case so we divide the region into such nice regions.

### Integrating in polar coordinates

We've seen that it can be made easier to integrate functions over a region by choosing good parameterisations with respect to $x$ and $y$. Sometimes we can make things even easier for ourselves by integrating with a different coordinate system, like polar coordinates.

Typically we use polar coordinates when its easier to write $f$ or $R$ in polar coordinates. A region $R$ that's easier to write in polar coordinates typically looks like it's composed of sectors of circles. a function that's easy to write in polar coordinates typically involves some function of $x^2 + y^2$, which is just $r^2$ in polar coordinates.

Polar coordinates cut up the plane into small regions of area
$$
dA = r \, dr \, d\theta.
$$
Thus,
$$
\iint_R f \, dA = \iint_R f \, dx \, dy = \iint_R f \, r \, dr \, d\theta.
$$

##### _example:_ area of a semicircle

We can calculate the same integral we did earlier much more easily if we use polar coordinates:
$$
\iint_R \, dA = \int_0^\pi \int_0^2 r \, dr \, d\theta
$$
which is trivial!