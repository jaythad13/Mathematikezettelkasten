---
tags:
- math-82/3
- diff-eq
---

Another really nice subclass of [[Differential equations --- math-82/notes/Classifying ordinary differential equations#Order|first order]] differential equations is that of first order [[Differential equations --- math-82/notes/Classifying ordinary differential equations#_definition _ linear differential equation|linear differential equations]]. The best way to see this why they are nice is an example.

##### _example:_ a clever trick to solve differential equations

Suppose we have the differential equation $x y' + y = x^2$. This looks tough to solve at first, but there's a trick.

Notice that
$$
xy' + x = \frac{d(xy)}{dx}
$$
Thus, really, we have the equation
$$
\frac{d(xy)}{x} = x^2.
$$

Integrating with respect to $x$ on both sides gives us that
$$
xy = \frac{x^3}{3} + C
$$
for any constant $C \in \mathbb{R}$.

Thus, $y(x) = x^3/3 + C/x$ is a solution for all $x \in \mathbb{R}\setminus \{ 0 \}$.

---

Here we used the product rule to rewrite the left side of differential equation as one derivative. Can we generalise this trick?

### Solving first order linear differential equations

We won't always have linear differential equations as nice as the first example — it won't always be obvious how to write the $y'$ and $y$ linear combination as the derivative of something else.

##### _example:_ a trickier equation

If we have $x^2 y' - 2x y = 4 x^5$, there isn't an immediately obvious way to do the same thing. However, if we multiply on both sides by $x^{-4}$, we get
$$
x^{-2} y' - \frac{2}{x^3}y = 4x
$$
which we can see clearly is just
$$
\frac{d(x^{-2} y)}{dx} = 4x
$$
and thus, can be solved by the same method.

---

What this is really doing?

To generalise this trick, we need a way to find the function of $x$ to multiply by. Luckily this isn't too hard to find.

##### _proposition, definition:_ solving linear differential equations, the integrating factor

 Consider the linear differential equation $y' + p(x) y = q(x)$. Let $\mu$ be the function defined by $\mu(x) = \operatorname{\exp}\left( \int p(x) \, dx \right)$. Then $y$ satisfies the equation if and only if
$$
y = \frac{1}{\mu(x)} \int \mu(x) q(x) \, dx.
$$

$\mu$ is called the **integrating factor** of the differential equation.

###### _proof:_

Suppose a function $\mu$ satisfies
$$
\frac{d(\mu(x) y)}{dx} = \mu(x) y' + \mu (x) p(x) y.
$$
Then for $y \mu(x) = \int \mu(x) q(x) \, dx$, we can differentiate both sides to get $\mu(x) y' = \mu(x) p(x) y = \mu(x) q(x)$ which is exactly the differential equation.

The condition on $\mu$ is a [[Differential equations --- math-82/notes/Separable differential equations#_definition _ separable differential equation|separable differential equation]] in $\mu$ and $x$. [[Differential equations --- math-82/notes/Separable differential equations#_proposition _ the solution of a separable differential equation|We know how to solve them]].
$$
\mu(x) = \exp\left( \int p(x) \, dx  \right).
$$
---