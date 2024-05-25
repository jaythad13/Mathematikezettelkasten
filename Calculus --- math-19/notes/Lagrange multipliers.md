---
tags:
- calc
- math-19
lecture: math-19-15
---

### Optimisation is hard

[[Optimisation|Recall]] how we found the maxima and minima of a function $f : \bb{R}^n \to \bb{R}$: we looked for points where $Df = 0$, or was undefined to find critical points. Then, we checked if the function had a maximum or minimum at the point, we check the determinant of the Hessian! (remember the eigenvalue argument)

This is often a non-trivial calculation, especially when there are constraints on the input. For example, the point on a plane closest to the origin.

##### _example:_ the second derivative test is difficult

Consider $f(x, y) = x^2 y + 3x y^2 + x y$. What are its extrema?

Note that
$$
Df \Big |_{(x, y)} = \begin{bmatrix} 2xy + 3y^2 + y & x^2 + 6xy + y \end{bmatrix}.
$$
At a critical point  $Df = 0$. This means we have to solve the system of equations
$$
\begin{gathered}
	y(2x + 3y + 1) = 0 \\
	x(x + 6y + 1) = 0.
\end{gathered}
$$
This gives us four different linear systems, and thus, up to four different critical points!

$$
\begin{gathered}
	x = 0 \\
	y = 0
\end{gathered}
$$
gives us $(x, y) = (0, 0)$.
$$
\begin{gathered}
	y = 0 \\
	x + 6y + 1 = 0
\end{gathered}
$$
gives us $(x, y) = (-1, 0)$.
$$
\begin{gathered}
	2x + 3y + 1 = 0 \\
	x = 0
\end{gathered}
$$
gives us $(x, y) = (0, -\frac{1}{3})$. Finally
$$
\begin{gathered}
	2x + 3y + 1 = 0 \\
	x + 6y + 1 = 0
\end{gathered}
$$
gives us $(-\frac{1}{3}, -\frac{1}{9})$.

The discriminant is
$$
\Delta = f_{xx} f_{yy} - f_{xy}^2 = (2y)(6x) - (2x + 6y + 1)^2.
$$

We can calculate this at each of the critical points
$$
\begin{gathered}
	\Delta(0, 0) = 0 - (0 + 1)^2 < 0 \\
	\Delta(-1, 0) = 0 - (-2 + 1)^2 < 1\\
	\Delta (0, -\frac{1}{3}) = 0 - (-6 \frac{1}{3} + 1)^2 < 0\\
	\Delta (-\frac{1}{3}, -\frac{1}{9}) = (-\frac{2}{3})(-\frac{6}{9}) - (-\frac{2}{3}- \frac{6}{9} + 1)^2 = (\frac{2}{3})^2 - (\frac{1}{3})^2 > 0
\end{gathered}
$$
Thus, we have saddles at all of the critical points except $(-\frac{1}{3}, -\frac{1}{9})$, which is a local maximum.

Note that we got lucky with the ease of computation for the discriminant here, but it was still not trivial.

### Optimising with constraints: Lagrange multipliers

[[Optimisation|Earlier]], we saw how to optimise a function with a constraint, and used the second derivative test to do it. But despite taking various steps to make our lives easier, it still amounted to a non-trivial calculation for what was really a simple geometric optimisation.

Also, our constraint was a simple plane, so we could easily solve for one of the variables (we chose $z$) in terms of the others, but our constraint could easily have been more difficult.

Let's look at this geometrically instead!

##### _example:_ a bug on a curve

Where is the bug warmest on the green curve?

![[S2_bug_on_curve.jpeg]]

Note that at the points where it's warmest, the level sets of temperature are tangent to the constraint curve. At these points, we can say that the gradient of the temperature function $T$ is perpendicular to the curve!

Also, note that we can write the constraint as the level set of some two variable function $g$. Then at these points the gradient of $g$ is perpendicular to the curve too!

Then the two gradients must be parallel! This is what Lagrange's method is!

##### _theorem:_ Lagrange's method

If some point $\bvec{p}$ maximises $f$ on some level set of $g$ given by $g = 0$, then
$$
\nabla f(\bvec{p}) = \lambda \nabla g(\bvec{p}) 
$$
or
$$
\nabla g(\bvec{p}) = 0.
$$

##### _example:_

Find a point on the plane $x + 2y + z = 6$ closest to $\bvec{0}$. 

To do so we want to optimise the distance squared function $f(x, y, z) = x^2 + y^2 + z^2$, with respect to the constraint $g = 0$ where $g(x, y, z) = x + 2y + z - 6 = 0$.

At such that closest point $\bvec{p}$ we must have 
$$
\nabla f (\bvec{p}) = \lambda \nabla g (\bvec{p}).
$$
That is, we have the system of equations
$$
\begin{gathered}
	2x = \lambda \\
	2y = 2 \lambda \\ 
	2z = \lambda \\
	x + 2y + z - 6= 0
\end{gathered}
$$

We can write each variable in terms of $\lambda$, and then substitute them into the plane equation:
$$
	\frac{\lambda}{2} + 2 \lambda + \frac{\lambda}{2} = 6
$$
giving us $\lambda = 2$.

Thus, $\bvec{p} = (1, 2, 1)$ is a critical point the same thing we got last time!

By geometry we can argue that this is a minimum, and then we are done!

##### _definition:_ Lagrange multiplier

If for some extremum of $f$ on some constraint given by $g = 0$, at some point $\bvec{p}$ we have
$$
\nabla f (\bvec{p}) = \lambda \nabla g(\bvec{p}),
$$
we say $\lambda$ is the Lagrange multiplier at that point.

Note that the Lagrange multiplier has a meaning! It relates how small changes in the constraint correspond to changes in the extremum of the function that we want to optimise.

##### _theorem:_ extreme value theorem

If a function $f : K \to \bb{R}$, where $K$ is a [[Compactness|compact]] subset of $\bb{R}^n$, is continuous, then $f$ achieves a global maximum and a minimum on $X$.

This means that we can employ the following strategy on to find global extrema on a compact set.

##### _strategy:_ to find global extrema on a compact set

For a compact subset of $\bb{R}^n$, $K$ and a function $f : K \to \bb{R}$, we can find the global extrema of $f$ on $K$ as by 
1) finding critical points in the interior of the set
and then
2) optimising $f$ on the boundary of $K$ and finding the constrained critical points.

##### _example:_ extrema on the closed unit disk

What are the extrema $f(x, y) = x^2 + y^2 - x$ on the closed unit disk?

First we find the critical points on the interior open unit disk.
$$
Df \Big |_{(x, y)} = \begin{bmatrix} 2x - 1 & 2y \end{bmatrix}
$$
Solving for $Df \Big |_{(x, y)} = 0$ gives us only $(x, y) = (\frac{1}{2}, 0)$ as a critical point.

On the boundary of the disk we have $x^2 + y^2 - 1 = 0$. Consider $g(x, y) = x^2 + y^2 - 1$ to be the constraint function. Then for any critical point $\bvec{p}$ on the boundary, we must have
$$
\nabla f (\bvec{p}) = \lambda \nabla g (\bvec{p})
$$
which gives us the system of equations
$$
\begin{gathered}
	2x - 1 = \lambda 2x \\
	2y = \lambda 2y \\
	x^2 + y^2 - 1 = 0.
\end{gathered}
$$
Since $\lambda = 1$ gives a contradiction: $2x - 1 = 2x$, we must have $y = 0$, forcing $x = \pm 1$. Then we have the possible extrema $(1, 0)$ and $(-1, 0)$. Then we check all the possible extrema to find the global extrema on the disk.
$$
\begin{gathered}
	f(\frac{1}{2}, 0) = -\frac{1}{4} \\
	f(1, 0) = 0 \\
	f(-1, 0) = 2.
\end{gathered}
$$
Thus, $f(-1, 0)$ is the global maximum and $f(\frac{1}{2}, 0)$ is the global minimum on the  disk.
