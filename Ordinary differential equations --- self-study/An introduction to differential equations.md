---
tags:
- diff-eq
- self-study
---

### A rough idea of what differential equations are

We are used to solving "algebraic equations" that involve dependent and independent variables like
$$
y = 2x + 7
$$
or
$$
e^y = 9xz.
$$

Differential equations deal with dependent and independent variables as well as derivatives (typically derivatives of the dependent variable with respect to the independent variables). For example
$$
y' + y = 3x \sin{x}
$$
or
$$
\pardx{z}{x} - \pardx{z}{y} = z.
$$

In this course we will deal with differential equations with one independent variable (usually one dependent, but sometimes multiple dependent variables). These are ordinary differential equations.

### The classical taxonomy of differential equations

We use the terms "order" and "linearity" to classify ordinary differential equations.

##### _definition:_ order

The order of a differential equation is the order of the highest derivative in the differential equation.

##### _definition:_ linear, non-linear

A differential equation is linear if it is a linear combination of the $k$th derivatives of the dependent variable with respect to the independent variable (with scalars from the ring of functions in the dependent variable).

##### _examples:_ order and linearity of differential equations

1) $$\dot{y} + \sin (t) \, y - t^3 = 0$$ is a first order linear differential equation.
2) $$\ddx{y}{x} - \sin (xy) = 0$$ is a first order non-linear differential equation.
3) $$y'' + x \sin(x) \, y = 1 $$ is a second order linear differential equation.
4) $$y'' y = y'$$ is a second order non-linear differential equation.

### Almost trivial differential equations

The easiest differential equations to solve are of the form
$$
\ddx{y}{x} = f(x).
$$
By the [[Fundamental theorem of calculus|fundamental theorem of calculus]], we know that the solution to this differential equation is just an antiderivative of $f$. That is,
$$
y = \int_{x_0}^x f(x) \, dx
$$
which we could just write as
$$
y = \int f(x) \, dx + C.
$$

##### _example:_ a non-trivial almost trivial differential equation

The solution to the differential equation
$$
\ddx{y}{x} = \frac{x^3}{\sqrt{1 - x^2}}
$$
is given by 
$$
y = \int \frac{x^3}{\sqrt{1 - x^2}} \, dx + C.
$$

We can evaluate this integral with the trigonometric substitution $x = \sin{\theta}$. Then $\ddx{x}{\theta} = \cos{\theta}$. This gives us
$$
\begin{split}
	y &= \int \frac{x^3}{\sqrt{1 - x^2}} \, dx + C \\
	& = \int \frac{\sin^3{\theta}}{\cos{\theta}} \, \ddx{x}{\theta} \, d\theta + C \\
	& = \int \frac{\sin^3{\theta}}{\cos{\theta}} \cos{\theta} \, d\theta + C \\
	& = \frac{1}{4} \int 3 \sin{\theta} - \sin{3 \theta} \, d\theta + C \\
	& = \frac{1}{4} (\frac{\cos{3 \theta}}{3} - 3 \cos{\theta}) + C \\
	& = \frac{\cos^3{\theta}}{3} - \cos{\theta} + C \\
	& = \frac{(\sqrt{1 - x^2})^3}{3} - \sqrt{1 - x^2} + C.
\end{split}
$$

If we have an initial value for the problem, for example, $y = 0$ when $x = 0$, then we can determine the value of $C$ as well.

##### _example:_ a non-trivial almost trivial differential equation with an initial value

The differential equation from the example above gives us
$$
y = \frac{(\sqrt{1 - x^2})^3}{3} - \sqrt{1 - x^2} + C.
$$
With the initial condition that $y = 0$ for $x = 0$, we must have
$$
0 = \frac{1}{3} - 1 + C
$$
giving us $C = \frac{2}{3}$, and thus, a unique solution to the differential equation.




