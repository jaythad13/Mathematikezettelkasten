---
tags:
- calc
- math-19
lecture: math-19-14
---

How do you find maxima or minima for multivariable functions ($f: \bb{R}^n \to \bb{R}$)?

Remember that for functions $f: \bb{R} \to \bb{R}$, whenever we have a maximum or minimum at a point, the derivative at that point is $0$ or undefined. This is because
$$
f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}.
$$
If $f(a)$ is a maximum, then there is some region around $a$ where $f(x) - f(a)$ is always non-positive. In the same region, to the left of $a$, $x - a$ is always negative, while to the right of $a$, $x - a$ is always positive. Then, if the derivative does exist, it is the limit of something that has non-negative left hand limit and non-positive right hand limit, and thus, must be zero.

The image below illustrates this.
![[S0_1dimMaximaMinima.jpeg]]

##### _theorem:_ Fermat's theorem

If $f: \bb{R} \to \bb{R}$ is differentiable and has local maximum or minimum at $a$, then $f'(a) = 0$.

##### _theorem:_ Fermat's theorem for multivariable functions

If $f: \bb{R}^n \to \bb{R}$ is differentiable and has a local maximum or minimum at $\bvec{a}$, then $Df \Big|_\bvec{a} = \bvec{0}$.

##### _proof:_

If $f$ has a maximum or minimum at $\bvec{a}$, then the curves given by looking at the slices along the $j$th coordinate must also have maxima or minima respectively, at $\bvec{a}$. Then by Fermat's theorem, the $j$th partials should be $0$, and thus, $Df \Big|_\bvec{a} = \bvec{0}$.

How then do you know that a critical point is a maximum or minimum?

Remember that for functions $f: \bb{R} \to \bb{R}$, we consider the best parabolic approximation to the function, a Taylor polynomial:
$$
f(x) \approx f(a) + f'(a) (x - a) + \frac{f''(a)}{2} (x - a)^2.
$$
Since at the maximum $f'(a) = 0$, a good approximation for points near $a$ is $f(x) \approx f(a) + \frac{f''(a)}{2} (x - a)^2$. Since $(x - a)^2$ is always positive, in some small neighbourhood around $a$, $f''(a) < 0$ means that a small step away from $a$ always results in a decrease in $f$, meaning that $f(a)$ is a maximum. Similarly, in that small neighbourhood $f''(a) > 0$ means that a small step away from $a$ always results in an increase in $f$, giving us $f(a)$ as a minimum.

But we can consider a second order approximation of multivariable functions too! This is particularly easy for $f: \bb{R}^2 \to \bb{R}$. We just need to ensure the approximation has all the same second partials (including mixed partials):
$$
f(x, y) \approx f(a, b) + f_x(a, b) (x - a) + f_y(a, b) (y - b) + \frac{f_{xx}}{2}(a, b) (x - a)^2 +\frac{f_{yy}}{2}(a, b) (y - b)^2 + f_{xy}(a, b) (x - a)(y - a).
$$
Note that $f_{xy}$ is not divided by $2!$ and $f_{yx}$ is not mentioned. This is because for differentiable $f$ we have $f_{xy} = f_{yx}$ and thus, $\frac{f_{xy}}{2}(a, b)(x - a)(y - a) + \frac{f_{yx}}{2}(a, b)(x - a)(y - a)$.

Also note that we can make this abhorrently large formula nicer:

$$
f(x, y) \approx f(a, b) + Df \Big|_{(a, b)} 
\begin{bmatrix}
x - a \\ 
y - b
\end{bmatrix} +
\begin{bmatrix}
x - a \\ 
y - b
\end{bmatrix} \cdot
\begin{bmatrix}
f_{xx}(a. b) & f_{xy}(a, b) \\ 
f_{yx}(a, b) & f_{yy}(a, b)
\end{bmatrix} 
\begin{bmatrix}
x - a \\ 
y - b
\end{bmatrix}. 
$$
Again, since $Df \Big|_{(a, b)} = 0$ at a minimum or maximum, we can approximate the function with just its second order terms:
$$
f(x, y) \approx f(a, b) + \frac{f_{xx}}{2}(a, b) (x - a)^2 +\frac{f_{yy}}{2}(a, b) (y - b)^2 + f_{xy}(a, b) (x - a)(y - a).
$$
Let's rewrite this as $f(x, y) \approx f(a, b) + A x^2 + B xy + C y^2$  ($A = \frac{f_{xx}}{2}, B = f_{xy}, C = \frac{f_{yy}}{2}$) which, by completing the square, we can again rewrite as
$$
f(x, y) \approx f(a, b) = A(h(x, y)^2 + \frac{4AC - B^2}{4A^2}(y - a)^2)
$$
Then, for any small change from $(a, b)$ we have a small positive change plus a change with the sign of $\frac{4AC - B^2}{4A^2}$. This gives us the following theorem.

##### _theorem:_ The second derivative tests for $f: \bb{R}^2 \to \bb{R}$

If $f : \bb{R}^2 \to \bb{R}$ is a $\mathcal{C}^2$ function and gives us $Df \Big|_{(a, b)} = 0$, then we can use the following criteria to tell whether $f(a, b)$ is a maximum or minimum:

For $\Delta = f_{xx}(a, b) f_{yy}(a, b) - f_{xy}(a, b)^2$:
- If $\Delta < 0$, then $f(a, b)$ is a saddle point
- If $\Delta > 0$ and $f_{xx} > 0$, then $f(a, b)$ is a local minimum
- If $\Delta > 0$ and $f_{xx} < 0$, then $f(a, b)$ is a local maximum
- If $\Delta = 0$, then the test is inconclusive.

##### _example:_ optimisation problem

Find a point on the plane $x + 2y + z = 6$ closest to $\bvec{0}$. Note that we don't need calculus to solve this! Just think about orthogonality!

We want to minimise the distance from the origin, but that is unpleasant:

$$
d(x, y, z) = \sqrt{x^2 + y^2 + z^2}.
$$

Instead, we can choose to minimise the square of the distance from the origin:
$$
f(x, y, z) = x^2 + y^2 + z^2.
$$
where $(x, y, z)$ is on the plane, and thus, $z = 6 - (x + 2y)$. Thus, we really want to minimise the function of two variables
$$
f(x, y) = x^2 + y^2 + (6 - x - 2y)^2.
$$
Now we just solve!

Note that we can rewrite $f$ as something simpler
$$
f(x, y) = x^2 + y^2 + x^2 + 4y^2 + 36 -12x - 24y +4xy.
$$
That is
$$
f(x, y) = 36 - 12x -24y + 2x^2 + 5y^2 + 4xy.
$$
Thus,
$$
Df = \begin{bmatrix} 4x + 4y - 12 & 10y + 4x - 24 \end{bmatrix}.
$$

At any critical point $Df = 0$, giving us the system of equations
$$
\begin{gathered}
	4x + 4y - 12 = 0 \\
	4x + 10y - 24 = 0
\end{gathered}
$$
which has the solution $(x, y) = (1, 2)$.

Note that
$$
\begin{gathered}
	f_{xx} = 4 \\
	f_{yy} = 10 \\
	f_{xy} = 4.
\end{gathered}
$$
Thus, the discriminant $\Delta$ has value
$$
\Delta = 4 \times 10 - 4^2 = 24.
$$
Since $\Delta > 0$ and $f_{xx}(1, 2) > 0$, $f(1, 2)$ is a minimum of the function.

By the geometry of the plane, any local minimum must also be the absolute minimum. Thus, the point $(1, 2, 1)$ on the plane is the 