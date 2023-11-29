---
tags:
- math-19
- calc
lecture: math-19-23
---

Just as with [[Line integrals|line integrals]] we compute surface integrals by parameterising the surface and the function we integrate on the surface, and then integrating with respect to the parameter. Where line integrals can be reformulated as single integrals, we try to reformulate the surface integral as a double integral.

##### _example:_ parameterising very simple surfaces

Suppose $\mathcal S$ is a graph of $g(x, y) = y^3$ over the rectangle $(x, y) \in [0, 1] \times [0, 2]$. How can we integrate the mass density $\delta(x, y, z) = z$ to get the mass of the surface? How do we measure the flux of the field $\bvec{F}(x, y, z) = (x, y, z)$ through the surface?

We can think of the surface as the level set of $f(x, y, z) = z - y^3$, where $f = 0$. Then, the gradient of $f$ is normal to the level surface everywhere on it. That is
$$
\nabla f(x, y, z) = (0, -3y^2, 1)
$$
is perpendicular to $\mathcal{S}$ everywhere. Importantly, it also reflects the size of the area element! The norm of the gradient (actually the derivative) gives us how $dx \, dy$ scales under $g$. This is because
$$
dS = \sqrt{1 + g_x^2} \sqrt{1 + g_y^2} \, dx \, dy \equiv_{\text{in the limit}} \sqrt{g_x^2 + g_y^2 + 1}.
$$

Thus, to integrate this, we just write
$$
\iint_{\mathcal S} \, \delta(x, y, z) \, dS = \int_0^2 \int_0^1 \delta(x, y, g(x, y)) \, \norm{(0, -3y^2, 1)} \, dx \, dy
$$
We can compute this as
$$
\int_0^2 \int_0^1 y^3 \sqrt{9y^4 + 1} \, dx \, dy = \int_0^2 y^3 \sqrt{9y^4 + 1} \, dy = \frac{1}{36} \frac{2}{3 }(9y^4 + 1)^{3/2} \Big |_0^2 \approx 32.
$$

We can safely choose the orientation of $\mathcal{S}$ such that the normal to it has positive $z$-coordinate. Again, the gradient of $f$ reflects this orientation.
$$
\iint_{\mathcal{S}} \bvec{F} \cdot d\bvec{S} = \int_0^2 \int_0^1 (x, y, y^3) \cdot (0, -3y^2, 1) \, dx \, dy = \int_0^2 \int_0^1 -2y^3 \, dx \, dy
$$
We can compute this as
$$
\int_0^2 \int_0^1 -2y^3 \, dx \, dy = \int_0^2 -2y^3 \, dy = -\frac{1}{2} y^4 \Big |_0^2 = -8.
$$

##### _strategy:_ to parameterise surfaces in $\bb{R}^2$

1) Use two parameters, say $u, v$.
2) Look at the tangents $T_u = (x_u, y_u, z_u) \, du$ and $T_v$.
3) We get $d\bvec{S} = T_u \times T_v$ and thus, $dS = \norm{T_u \times T_v}$.

For special surfaces (with spherical, cylindrical symmetry), these are already computed for us.

%% add the geometric intuition from Prof Su's lecture 23 notes for our class. Remember to think about how x, y, z are dependent on the radius of the sphere/cylinder as well.%%