---
tags:
- math-19
- calc
- anal
lecture: math-19-13
---

Recall the notion of the [[Directional derivatives and the gradient|gradient]] of a function $f: \bb{R}^n \to \bb{R}$. The gradient, $\nabla f : \bb{R}^n \to \bb{R}^n$ feels like a sort of derivative of $f$.

We have similar notions of a derivative for [[Vector fields|vector fields]]. Particularly, for a vector field $\bvec{F}$ on $\bb{R}^2$ or $\bb{R}^3$, we have the curl of $\bvec{F}$ and the divergence of $\bvec{F}$, which measure properties of "change", like the gradient does.

##### _definition:_ divergence

If $\bvec{F}$ is a vector field in $\bb{R}^n$ with component functions $f_1, \ldots, f_n$, then the divergence of $\bvec{F}$ is
$$
\div{\bvec{F}} = \nabla \cdot \bvec{F} = \pardx{f_1}{x_1} + \cdots + \pardx{f_n}{x_n}.
$$

##### _definition:_ curl

If $\bvec{F}$ is a vector field in $\bb{R}^3$ with differentiable component functions $f_1$, $f_2$, and $f_3$, then the curl of $\bvec{F}$ is 
$$
\curl{\bvec{F}} = \nabla \times \bvec{F} = (\pardx{f_3}{y} - \pardx{f_2}{z}, \pardx{f_1}{z} - \pardx{f_3}{x}, \pardx{f_2}{x} - \pardx{f_1}{y}).
$$

Note that notation we use for divergence and curl reflects that if we think of $\nabla$ as a "vector of differential operators" given by 
$$
\nabla = (\pardx{}{x_1}, \ldots, \pardx{}{x_n})
$$
then we can think of the divergence of any vector field $\bvec{F}$ as 
$$
\nabla \cdot \bvec{F}
$$
and the curl of any vector field on $\bb{R}^3$ as
$$
\nabla \times \bvec{F}.
$$

### Geometric intuitions for divergence and curl

But why would we every care to do these? What do the curl and divergence of a vector field even mean?

The divergence of a vector field at a point is a scalar that tells us about how the field expands away from, or contracts into that point. Specifically, it is positive if the field expands, and negative if it contracts, with magnitude proportional to the "rate of expansion/contraction"

The curl of a vector field at a point is a vector that tells us about how a field "spins" at that point. Specifically, the curl has direction given by the "axis of greatest spin" (according to the right-hand rule) and magnitude that is proportional to the "rate of spin" about that axis.

This makes more sense with some examples:

##### _examples:_ divergence and curl of vector fields

Consider the vector fields $\bvec{E}$, $\bvec{F}$, $\bvec{G}$, and $\bvec{H}$ such that
$$
\begin{gathered}
	\bvec{E}(x, y, z) = (0, 0, y^2) \\
	\bvec{F}(x, y, z) = (x, y, z) \\
	\bvec{G}(x, y, z) = (0, y^2, 0) \\
	\bvec{H}(x, y, z) = (-y, x, 0).
\end{gathered}
$$

![[Divergence_and_curl_S1_vfieldE.jpeg]]

With $\bvec{E}$, we can have $\bvec{p_1}$ and $\bvec{p_2}$, points that are each other reflected in the $z$ axis. At both points, as we go further from origin in the $y$ direction, the magnitude of the vector field (which is only in the $z$ direction) increases. 

We can imagine that a ball left to drift from $\bvec{p_1}$ would curl in counterclockwise towards the origin, while at $\bvec{p_2}$ a ball would curl in clockwise, both around the $x$-axis. Thus, we expect that the curl should be equal in magnitude and opposite in direction, along the $x$-axis.

Computing, we get
$$
\curl{\bvec{E}} = (2y, 0, 0)
$$
which is, as we expected, directed along the $x$-axis always - curling counterclockwise for positive $y$ and clockwise for negative $y$.

![[Divergence_and_curl_S1_vfieldF.jpeg]]

We can see that for $\bvec{F}$, at every point, the vectors converging on the point from the origin are of lesser magnitude than the vectors diverging from the point to infinity. Thus, we should expect that $\div{\bvec{F}} > 0$ everywhere.

$\bvec{F}$ also does not seem to increase in magnitude as you move perpendicular to it, and so appears to have no curl anywhere

Explicitly, we see that
$$
\div{\bvec{F}} = 3
$$
which is always positive, just like we expected. Furthermore, we see

$$
\curl{\bvec{F}} = 0
$$
again, like we expected.

![[Divergence_and_curl_S1_vfieldG.jpeg]]

For $\bvec{G}$ at points with $y < 0$ (like $\bvec{p_2}$) we see the vectors of the field converge together and should expect to see negative divergence. For points with $y > 0$ (like $\bvec{p_1}$) the vectors race away from each other and we should expect positive divergence.

Computing the divergence gives us
$$
\div{\bvec{G}} = 2y
$$
which is positive for $y > 0$ and negative for $y < 0$ as expected.

![[Divergence_and_curl_S1_vfieldH.jpeg]]

For $\bvec{H}$ at each point, we can clearly see the vector field rotating counterclockwise around the $z$-axis. Thus, we should expect to see non-zero curl along the $z$-axis, with positive $z$ componenet

Calculating the curl shows us
$$
\curl{\bvec{H}} = (0, 0, 2)
$$
which is exactly as we expected.

### Curl for vector fields on $\bb{R}^2$

For vector fields on any $\bb{R}^n$ we have a sensible notion of divergence. The cross product, and the resultant rule for computing curl, are only defined on $\bb{R}^3$.

However, we can definitely still think about curl of fields on $\bb{R}^2$. For example, the vector field $\bvec{F}(x, y) = (-y, x)$ clearly curls counterclockwise about some axis not contained in $\bb{R}^2$. In fact, any "curling" vector field in $\bb{R}^2$ curls around the $z$-axis, and we can think of them as doing so by embedding the vector field in $\bb{R}^3$.

For a vector field in $\bb{R}^2$, $\bvec{F}$, defined by $\bvec{F}(x, y) = (f_1(x, y), f_2(x, y))$, consider the vector field in $\bvec{G}$ in $\bb{R}^3$ given by $\bvec{G}(x, y, z) = (f_1(x, y), f_2(x, y), 0)$. If we compute the curl of $\bvec{G}$ we get 
$$
\nabla \times \bvec{G} = (0, 0, \pardx{f_2}{x} - \pardx{f_1}{y})
$$
which is dependent only on the vector field we already had, and gives us an axis of rotation about the $z$-axis just like we expected. Thus, typically, we talk about the scalar curl of vector fields on $\bb{R}^2$ as the $z$-component of the "embedded vector field" on $\bb{R}^2$.

##### _definition:_ scalar curl

For a vector field $\bvec{F}$ on $\bb{R}^2$ with component functions $f_1$ and $f_2$ the scalar curl of $\bvec{F}$ is

$$
\curl \bvec{F} = \pardx{f_2}{x} - \pardx{f_1}{y}.
$$

### Curl and divergence in physics

If a vector field $\bvec{F}$ represents the velocity field of a fluid divergence and curl have interesting physical meaning:
- if $\nabla \cdot \bvec{F} = 0$, the fluid is incompressible
- if $\nabla \times \bvec{F} = 0$, the fluid is irrotational

For any inverse square law vector field $\bvec{F}$ ($\bvec{F} = C \dfrac{\bvec{r}}{\norm{\bvec{r}}^3}$ for some constant $C$) we have $\nabla \cdot F = 0$ and $\nabla \times \bvec{F}$ which is what makes so many of the 