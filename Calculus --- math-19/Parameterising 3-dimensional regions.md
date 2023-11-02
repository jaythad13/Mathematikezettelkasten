---
tags:
- math-19
- calc
lecture: math-19-18
---

There are some alternate coordinate systems that make certain integrals much, much easier.

### Cylindrical coordinates for $\bb{R}^3$

Cylindrical coordinates allow us to take advantage of cylindrical symmetries in functions or regions - radial symmetries about a particular axis.

##### _definition:_ cylindrical coordinates

Cylindrical coordinates assign to each point $\bvec{p} \in \bb{R}^3$ a triple $(r, \theta, z)$, with $r \ge 0$, $\theta \in [0, 2 \pi]$, and $z \in \bb{R}$. For $\bvec{p} = (x, y, z)$,
$$
\begin{gathered}
r = \sqrt{x^2 + y^2} \\
\theta = \arctan{\frac{y}{x}} \pm n \pi \\
z = z
\end{gathered}.
$$
That is, $r$ is the distance from the $z$ axis, $\theta$ is the angle from the positive $x$ axis, and $z$ is just the same as in rectilinear coordinates.

##### proposition: $dV$ in cylindrical coordinates

$$
dV = r \, dr \, d\theta \, dz
$$

##### _proof sketch:_

Look at the determinant of the Jacobian of the coordinate transformation function.

##### _example:_

What is the mass of $W$, the region bounded by the plane $z = 3$ and the surface $z = \sqrt{x^2 + y^2}$ where the density of $W$ is given by $\delta$ where $\delta(x, y, z) = x^2 + y^2 + z^2$?

Instead of thinking about all of the $x, y, z$ rubbish, we can make our lives easier by recognising that the region is bounded by a cone with cylindrical symmetry. Then we can notice that $W$ is bounded by $z = r$ and $z = 3$, we can consider radii up to the radius at the intersection of the plane and the surface $r \in [0, 3]$, and we can consider all angles $\theta \in [0, 2 \pi]$. We can also simplify $\delta$ to $r^2 + z^2$

Thus,
$$
\text{mass}_W = \iiint_W \delta(x, y, z) \, dV = \int_0^{2 \pi} \int_0^3 \int_r^3 r^2 + z^2 \, dz \, dr \, d\theta.
$$

### Spherical coordinates for $\bb{R}^3$

Spherical coordinates allow us to take this further and take advantages of spherical symmetries - complete radial symmetries about a point.

##### _definition:_ spherical coordinates

Spherical coordinates assign to each point $\bvec{p} \in \bb{R}^3$, a triple $(\rho, \theta, \phi)$ with $\rho \ge 0$, $\theta \in [0, 2 \pi]$, and $\phi \in [0, \pi]$. For $\bvec{p} = (x, y, z)$,
$$
\begin{gathered}
	\rho = x^2 + y^2 + z^2 \\
	\theta = \arctan{\frac{y}{x}} \pm n \pi \\
	\phi = \arctan {\frac{r}{z}}
\end{gathered}
$$
where $r = \sqrt{x^2 + y^2}$.


##### _proposition:_ $dV$ in spherical coordinates

$$
dV = \rho^2 \sin{\phi} \, d\rho \, d\phi \, d\theta
$$

##### _proof sketch:_

Look at the determinant of the Jacobian of the coordinate transformation function.



