---
tags:
- diff-eq
- math-82/1
---

### What are they?

The best way to understand what a differential equation is or why we might care about them is to see one.

##### _example:_ a (very simple) model for population growth

A very simple model for population growth is $P' = P$. That is, population as a function of time, $P$, is equal to its own time derivative at every point in time — $P(t) = P'(t)$ for all $t \in \mathbb{R}_{\ge 0}$. Note how this time variable was suppressed when we first wrote the equation.

One obvious family of solutions for this differential equation is $P(t) = C e^{ t }$ where $C$ can be any constant in $\mathbb{R}$. We can see this because for $P(t) = Ce^{ t }$ it's obviously true that $y'(t) = P e^{ t }$ everywhere and thus, $P' = P$.

Note that here we get a family of solutions instead of a single solution. That is, there are infinitely many possible solutions to this differential equation. In order to get just one, we need more specific information about the function we're looking for.

##### _example:_ a (slightly less simple) model for population growth

Say we don't just know that the population scales in proportion to its size, but also that initially, the population is $100$. That is, we have $P' = r P$ for some constant $r \in \mathbb{R}$ and $P(0) = 100$. 

Then, from the differential equation we get $P(t) = Ce^{ rt }$, and since $P(0) = 100$, $C = 100$. Thus, we get a specific solution $P(t) = 100 e^{ rt }$. (Here $r$ is a specific constant given to us, unlike $C$ in the previous example which could be any real number).

Now that we know what a simple differential equation can look like, we can define them. Ordinary differential equations are problems only dealing with one variable.

##### _definition:_ ordinary differential equations

An ordinary differential equation is an equation involving a function of one independent variable and its derivatives.

More broadly, we can define differential equations.

##### _definition:_ differential equations

A differential equation is an equation involving a function and its derivatives.

### A note on solutions

Usually, a solution to a differential equation is a function such that it and its derivatives satisfy the equation. Most of this class is about solving ordinary differential equations. That is, this class is about ways to look at a differential equation and find a function that satisfies it. However, this turns out to be very difficult, and in fact, is often impossible. Most differential equations don't have an exact solution in terms of well-known functions. This class is still valuable because
- a lot of important differential equations *do* have analytic solutions
-  we can approximate differential equations that don't have these solutions with ones that do
- we will learn about other techniques to determine the behaviour of a differential equation even when it can't be solved analytically