---
tags:
- calc
- math-19
lecture: math-19-20
---

Remember that we can [[Line integrals#_example _ estimating line integrals|estimate the value of scalar line integrals]] without really performing any computations. It's only natural to try to do the same thing with vector line integrals

##### _example:_ estimating vector line integrals
![[S0_estimatingVectorLineIntegrals.jpeg]]

What is the line integral of the field $\bvec{F}$ given by $\bvec{F}(x, y) = (0, x)$ along the curves $\alpha$, $\beta$, and $\gamma$? 

We can see that $\bvec{F}$ just points parallel to the $y$-axis with the magnitude of the $x$-coordinate of the input. 

Since the $\alpha$ is directed vertically upward and lies in the first quadrant where the $x$-coordinates of every point are positive, we expect $\int_\alpha \bvec{F} \cdot d\bvec{s} > 0$. In fact, since the $\norm {\bvec{F}} = 1$ everywhere on $\alpha$ and they have the same direction, $\bvec{F} \cdot d\bvec{s} = 1$ on $\alpha$, and thus,
$$
\int_\alpha \bvec{F} \cdot d\bvec{s} = \int_\alpha \, d\bvec{s} = \text{length}_\alpha = 1.
$$

We get the exact same thing by explicit computation! Parameterising $\alpha$ as
$$
\alpha = \set{(1, t) : t \in [1, 2]}
$$
we get
$$
\int_\alpha \bvec{F} \cdot d\bvec{s} = \int_1^2 (0, 1) \cdot (0, 1) \, dt = \int_1^2 \, dt = 1.
$$

Similarly we can look at the integrals along $\beta$ and $\gamma$. Since they have the same length and point in opposite directions, we can argue that they have the same magnitude and opposite sign. Specifically, the integral along $\beta$ should be positive and the integral along $\gamma$ should be negative because of the directions in which they point. Also, since $\norm{\bvec{F}}$ is greater along $\beta$ and $\gamma$ than along $\alpha$, we should expect the magnitude of the integrals to be greater too. Explicitly, since $\norm{\bvec{F}} = 2$ everywhere on $\beta$ and $\gamma$.
$$
-\int_\gamma \bvec{F} \cdot d\bvec{s} = \int_\beta \bvec{F} \cdot d\bvec{s} = 2 \int_\beta \, d\bvec{s} = 2 \times \text{length}_\beta.
$$

Again, explicit computation gives us the same thing.

The moral lesson here is that computing line integrals is actually pretty easy as long as the paths you integrate along are reasonable.

##### _definition:_ closed paths

A path $c : [a, b] \to \bb{R}^n$ is closed if $c(a) = c(b)$.

### Closed line integrals and the intuition for them

##### _definition:_ circulation

For a closed path $c$ and a vector field $\bvec{F}$, the circulation of $\bvec{F}$ along $c$ is
$$
\oint_c \bvec{F} \cdot d \bvec{s} = \int_c \bvec{F} \cdot d\bvec{s}.
$$

We call this the circulation because it seems to detect when a vector field circulates along a path - the integral is nonzero when the field circulates along the path.

##### _example:_ circulations detect circulation

If we consider the line integral of $\bvec{F}$ ($\bvec{F}(x, y) = (0, x)$ again), along the curve $c_1 + c_2 + c_3 + c_4$ (addition of curves is just joining them). We should expect this to be positive since the positive contributions of $\bvec{F}$ along $c_2$ are greater than the negative contributions of $\bvec{F}$ along $c_4$.

![[S1_circulationsMeasureCirculation.jpeg]]

In fact, $\bvec{F}$ has positive curl, corresponding exactly to this!

### Green's theorem

##### _theorem:_ Green's theorem

Suppose $c$ is closed path $c: \bb{R} \to \bb{R}^2$ that bounds the region $D$ in $\bb{R}^2$ on its left. Suppose $\bvec{F}$ is a vector field $\bvec{F} : \bb{R}^2 \to \bb{R}^2$ such that $\bvec{F}(x, y) = (M(x, y), N(x, y))$ defined on all of $D$, then
$$
\oint_c \bvec{F} \cdot d\bvec{s} = \iint_D \curl \bvec{F} \, dA.
$$

##### _example:_ Green's theorem makes detecting circulation easier

Green's theorem makes computing the previous integral trivial!
$$
\oint_{c_1 + c_2 + c_3 + c_4} \bvec{F} \cdot d \bvec{s} = \iint_D \curl \bvec{F} \, dA = \iint_D \pardx{(x)}{x} - \pardx{(0)}{y} = \iint_D \, dA = \text{area}(D)
$$
where $D$ is just the square with vertices $(1, 3/2), (1, 5/2), (2, 3/2), (2, 5/2)$. Thus
$$
\text{area}(D) = 1.
$$