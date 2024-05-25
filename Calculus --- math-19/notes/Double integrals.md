---
tags:
- calc
- math-19
lecture: math-19-16
---

Recall how we deal with integrals in single variable calculus. For example, what does 
$$
\int_a^b f(x) \, dx
$$
mean?

It means that we partition the interval $[a, b]$ into small pieces and then sum areas of the rectangles formed. We look at the limit where the partitions become "of size $dx$", and that well approximates the area under the graph of $f(x)$ on the interval $[a, b]$.

![[S2_1dim_integral.jpeg]]

We then receive the pleasant surprise that we don't have to deal with the messy analysis to do with these sums, because this is the same thing as the difference of antiderivatives!

### Why integrate in two dimensions?

Suppose we wanted to know something about the whole state of California but we only had local information, at every point. How would we figure it out?

Integration!

##### _example:_ the population of California

If $\delta(x, y)$ gives us the population density of California at any point $(x, y)$. How do we get the population of California?

We could use the same strategy as in single variable calculus to get this! Since we know that the area derivative is accurate locally, we can add up population of small areas $\Delta A$, given by $\delta(x, y) \Delta A$. If we have a really accurate population density function, we could even take the limit, in which we say the area $\Delta A$ is just $dA$! We write this limiting sum

$$
\iint_R \delta(x, y) \, dA.
$$

##### _examples:_ the meaning of integrals

What does 
$$
\iint_R 1 \, dA
$$
mean?

It's just the area of the region $R$! Or perhaps more accurately, the volume of the prism of face $R$ and height $1$. But they're numerically the same!

What does
$$
\iint_R f(x, y) \, dA
$$
mean?

This is just the signed volume under $f$ over the region $R$. 

For example, if $f$ were altitude with respect to see level, and $R$ were the state of California, then $f$ would be the volume above sea level of California, except that the Death Valley, (and every other valley) would make negative contributions to the volume.

##### _example:_ average values

What's the average temperature in California if $f$ is the local temperature function?

If this were discrete data, we would sum and then divide by the number of datum. We can use the same idea by extending the idea of sums to integration! 

We could add the temperature in each county, scale by the area of the county and then divide by the area of all of California. Or, taking the limit,

$$
\text{average temperature} = \frac{\iint_R f \, dA}{\iint_R \, dA}.
$$

The moral of this is that the integral is the analog of the sum for continuous data.

### How to do integrals in two dimensions

But what really is an integral? What is that limiting process? For this we use Riemann sums again!

##### _definition:_ double integral, integrand, region of integration

If for some function $f : \bb{R}^2 \to \bb{R}$ the limit of all Riemann sums on some (measurable) region $R$ exists, we call $f$ integrable and denote the limit of all the Riemann sums as
$$
\iint_R f \, dA. 
$$

We call $f$ the integrand and $R$ the region of integration.

But doing this with Riemann sums is very tedious. Isn't there a better way to do this? 

There is! We can use how we know to do integrals for single variables to do double integrals.

Suppose a function $f$ that we want is integrable. Since we can choose any partition we want, since they all converge to the same thing. Then we can choose to cut up the region into a grid. Then, we can sum up all the partitions along rows, and then sum those rows, or sum up all the partitions along columns and then sum those columns.

![[S2_iterated_integrals.jpeg]]

Since the width of the row approaches zero as $dy$ approaches zero, summing along the row is just like integrating $f$ with respect to $x$ on that row, keeping $y$ constant. Then summing the rows is just like integrating the value of each row with respect to $y$. The story is similar for $y$.

Note that all we have to do now is parameterise the region. For a region, we can usually get $x \in [h_1(y), h_2(y)]$ and $y \in [a, b]$, or vice-versa.

##### _proposition:_ Fubini's theorem

For a piecewise continuous function $f$ over a measurable region $R$, defined by $x \in [h_1(y), h_2(y)]$ and $y \in [a, b]$
$$
\iint_R f \, dA = \int_a^b \Big (\int_{h_1(y)}^{h_2(y)} f \, dx \Big) \, dy. 
$$
If we can define $R$ by $y \in [g_1(x), g_2(x)]$ and $x \in [a, b]$
$$
\iint_R f \, dA = \int_a^b \Big ( \int_{g_1(x)}^{g_2(x)} f \, dy \Big) \, dx.
$$

That is, the order of integration doesn't matter.

##### _example:_ computing a double integral as an iterated integral

Find the volume under $f(x, y) = x^2 + y^2$ over the rectangle $R$ with vertices $(0, -2), (0, 2), (3, 2), (3, -2)$.
$$
\text{volume} = \iint_R f \, dA = \int_{-2}^{2} \int_0^3 x^2 + y^2 \, dx \, dy
$$
which by some calculus and algebra gives us
$$
\text{volume} = 52.
$$
Note that we should also get
$$
\int_0^3 \int_{-2}^2 x^2 + y^2 \, dy \, dx = 52.
$$
