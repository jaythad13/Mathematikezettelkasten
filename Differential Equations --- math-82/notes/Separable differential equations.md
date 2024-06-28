---
tags:
- math-82/2
- diff-eq
---

Separable differential equations are just one small class of differential equations, even among the small class of differential equations we will learn how to solve. In fact, they are a small subset of even [[Classifying ordinary differential equations#Order|first order]] ordinary differential equations. However, they are the easiest to solve and come up naturally in modelling problems fairly often!

### What are separable differential equations

##### _definition:_ separable differential equation

A differential equation in $y$, a function of $x$, is separable if it can be written as
$$
\frac{dy}{dx} = f(x) g(y)
$$
for some functions $f$ and $y$.

Note that this equation could be non-linear but have greater order than first order.

##### _examples:_ separable differential equations

1) $y' = x^2 y$
2) $y' = \sin y$
3) $y' - ty^2 = t$
4) $dP/dt = rP(1 - P/k)$
are all separable. Notice that in the fourth example, there isn't a unique way to separate out functions of $t$ and $P$ — we could choose $r$ as a constant function of $t$ or $1$ as a constant function of $t$. In general, constant terms behave like this. We will see why this doesn't matter when we solve the differential equations.

##### _non-example:_ separable differential equation

${dx}/{dt} = x + t$ is simple example of a non-separable differential equation.

### Solving a separable differential equation

We can solve a separable differential equation by "treating the derivative like a fraction" and then integrating. While this works mechanically, what's really happening is this.

##### _proposition:_ the solution of a separable differential equation

Given a differential equation,
$$
\frac{dy}{dx} = f(x)g(y)
$$
any solution, $y(x_{0})$ must satisfy
$$
\int_{y(a)}^{y(x_{0})} \frac{1}{g(y)} \, dy = \int_{a}^{x_{0}} g(x) \, dx 
$$
for any $a \in \mathbb{R}$.

###### _proof:_

This just follows from the change of variables formula for integrals. We already have
$$
\frac{1}{g(y)} \frac{dy}{dx} = f(x).
$$
Then, integrating with respect to $x$, on $[a, x_{0}]$ we have
$$
\int_{a}^{x_{0}} \frac{1}{g(y)} \frac{dy}{dx} \, dx = \int_{a}^{x_{0}} f(x) \, dx 
$$
which, by change of variables is equivalent to
$$
\int_{y(a)}^{y(x_{0})} \frac{1}{g(y)}  \, dy = \int_{a}^{x_{0}} f(x) \, dx.
$$

Notice that then, given a boundary value $y(a) = c$, (and a nice enough derivative for $g$), we can solve this for $y$.

##### _example:_ a boundary value problem for a separable differential equation

Find a solution $y(x)$ for the differential equation $y' y = -x$ with boundary value $y(0) = 1$.

Note that we must have
$$
\int_{y(0)}^{y(x_{0})} y \, dy = \int_{0}^{x_{0}} -x \, dx
$$
and thus,
$$
\int_{1}^{y(x_{0})} y \, dy = \left( -\frac{x^2}{2} \right) \Big |_{0}^{x_{0}}.
$$

This gives us
$$
\left( \frac{y^2}{2} \right) \Big |_{1}^{y(x_{0})} = -\frac{x_{0}^2}{2}
$$
and thus,
$$
\frac{y(x_{0})^2}{2} - \frac{1}{2} = - \frac{x_{0}^2}{2}.
$$

Finally, we have
$$
y(x)^2 + x^2 = 1
$$
This could be solved by either branch of $y(x) = \pm \sqrt{ 1 - x^2 }$, but only the positive branch satisfies $y(0) = 1$. Thus, we have $y(x) = \sqrt{ 1 - x^{2} }$ as a solution.

Note that here a solution only exists for $\lvert x \rvert \le 1$. Often the solution of a differential equation is restricted like this. This motivates the following definition.

##### _definition:_ domain of existence

The domain of existence of a solution to a differential equation is the maximal domain over which the solution is defined and satisfies the differential equation.

### Separable differential equation models

As we said, these easy to solve equations are actually useful! In general, the rate of change of a variable is often proportional to the variable itself. 

##### _example:_ the law of mass action

The best example of this is in reaction rates, where the rate of the reaction is often proportional to the some power of concentration of the reactant. Thus, the concentration of the reactant decreases quickly as the reaction proceeds quickly at the start of the reaction. Specifically the law of mass action says

> Reaction rate is proportional to the product of concentrations of participating molecules.

For example, if $x(t)$ is the concentration of a reactant undergoing dimerisation, the rate of the reaction might be proportional to $x^2$ (since two molecules of the reactant are required for the reaction). Thus,
$$
\begin{split}
\frac{dx}{dt} & = - \text{rate} \\
 & = -k x^2.
\end{split}
$$
This can be solved by the same method to get (for initial condition $x(0) = x_{0}$)
$$
x(t) = \frac{1}{kt + {1}/{x_{0}}}.
$$