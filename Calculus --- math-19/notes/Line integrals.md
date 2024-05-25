---
tags:
- calc
- math-19
lecture: math-19-19
---

We've already seen how to integrate a function over areas and volumes and by generalising these, we can think about integrating over $n$-dimensional regions in $\bb{R}^n$. 

But often we want to do something completely different. Often, what we really want to do is deal with really thin things like say, the mass of a thin wire cut out from a big copper sheet along a certain curve, or add up all the small components of work done by friction moving along a path for some force field, or find the average temperature along a certain path. 

To do so, we come up with two ideas of a line integral - a scalar line integral that deals with scalar functions $f : \bb{R}^n \to \bb{R}$ and a vector line integral that deals with vector fields $\bvec{F} : \bb{R}^n \to \bb{R}^n$.

Of course, first we need some rigorous definition of a path.

##### _definition:_ path

A path is a continuous function $c : I \to \bb{R}^n$, where $I$ is some interval in $\bb{R}$.

### Scalar line integrals

When we integrate scalar functions, we want to have the behaviour similar to just integrating a function $f : \bb{R} \to \bb{R}$, since we can think of that as integrating over a line too. That is, we want the line integral to correspond to the intuitive idea of adding up the product of small changes along the curve, and the function at that point.

##### _example:_ the length of a path

For a path $c$, the line integral $\int_c \, ds$ is the length of the path.

##### _example:_ the mass of a wire

If we cut out a thin wire along the curve $c$, from a slab of mass density $\delta(x, y)$, the total mass of the wire is given by
$$
\int_c \delta(x, y) \, ds.
$$

##### _example:_ the average temperature along a path

For a temperature function $T$, the average temperature along the path is
$$
\frac{\int_c T(x, y, z) \, ds}{\int_c \, ds}.
$$

##### _example:_ the area of a fence

If we want to set up a fence along the curve $c$ with height given by the function $h$, we can find the (signed) area of the fence by integrating:
$$
\text{area} = \int_c h(x, y) \, ds.
$$

##### _example:_ estimating line integrals

![[S1_scalarLineIntegralsToEstimate.jpeg]]

Looking at the line integrals of $x$ along each curve above what can we say?

It's obvious that the integral along $c_3$ should be $0$ since $x = 0$ for any point on $c_3$. We can also say that the integral along $c_4$ should be negative since $c_4$ is negative at every point on $c_4$.

We can make more specific statements about $c_1$ and $c_2$. Integrating along $c_1$ should give us a positive value, but also, since $c_1$ is a line symmetric about $2.5$, and so is the function along $c_1$, we should expect the integral to scale the length of the line by a factor of the average of $x$ along $c_1$ - that is, $2.5$!


##### _strategy:_ computing scalar line integral

For a curve parameterised by $c : \bb{R} \to \bb{R}^n$, given by $c(t)$ for $t \in [a, b]$, the line integral of some scalar function $f$ along $c$ is
$$
\int_c f(x_1, \ldots, x_n) \, ds = \int_a^b f(c(t)) \, \norm{c'(t)} \, dt.
$$

That is, we use the chain rule to think about integrating over the parameter of the curve instead of the curve itself. Note that since we're looking at the 'speed' $\norm{c'(t)}$ and not the 'velocity' $c'(t)$, the direction in which we integrate along a curve won't matter

##### _example:_ computing the estimated integrals

We can explicitly compute the integral along $c_1$ from the previous example.

We parameterise $c_1$ as $\set{(1, 1) + (1, 1)t : t \in [0, 1]}$. This gives us $\norm{c'(t)} = \sqrt 2$, and thus
$$
\int_{c_1} x \, ds = \sqrt{2} \int_0^1 1 + t \, dt
$$
which we can easily compute with single variable calculus.

### Vector line integrals

Vector line integrals are similar, but require us to add up the components of a vector field $\bvec{F}$, along the curve we're integrating over. Since dot products give us components, we take the dot products of the vector field and tiny tangent vectors at every point on the path, and then sum them.

![[S2_vFieldComponentsAlongCurve.jpeg]]

##### _notation:_ (vector) line integrals

There are many competing notations for the vector line integral of the vector field $\bvec{F} = (f_1, \ldots, f_n)$ along the path $c$. Some are
$$
\begin{gathered}
\int_c \bvec{F} \cdot d\bvec{s} \\
\int_c f_1 \, dx_1 + \cdots + f_n \, dx_n \\
\int_c \bvec{F} \cdot \hat{t} \, ds
\end{gathered}
$$
where $\hat{t}$ is the unit tangent vector to $c$.

##### _strategy:_ computing vector line integrals

For a path $c$, given by $c(t)$ for $t \in [a, b]$, the line integral of the vector field $\bvec{F}$ along $c$ is
$$
\int_c \bvec{F}(x_1, \ldots, x_n) \cdot d\bvec{s} = \int_a^b \bvec{F} (c(t)) \,  c'(t) \, dt.
$$

This is just using the chain rule in the same way that we did for scalar line integrals.

##### _example:_ computing a vector line integrals

$\bvec{G}$ is the vector field on $\bb{R}^2$ given by $\bvec{G}(x, y) = (-y, x)$. $c$ is the circle of radius $2$, clockwise about $\bvec{0}$. That is $c(t) = 2(\cos{-t}, \sin{-t})$ for $t \in [0, 2 \pi]$. What is the line integral of $\bvec{G}$ along $c$?

Just looking at pictures, we can see that $\bvec{G}$ always points in exactly the opposite direction to the tangent of the circle, and that the magnitude of $\bvec{G}$ at each point on the circle is $2$. Then we should expect to get approximately $-2 \, \text{perimeter}$ for the line integral.

Since, $c'(t) = -2(\sin(t), \cos(t))$, we get
$$
\int_c \bvec{G} \cdot d\bvec{s} = \int_0^{2 \pi} \bvec{G}(c(t)) c'(t) \, dt = \int_0^{2 \pi} -4 (\sin^2{t} + \cos^2{t}) \, dt = -8 \pi
$$
which is twice the negative of the perimeter of a circle of radius $2$, just as we expected.

