---
tags:
- diff-eq
- math-82/6
- math-82/7
---

[[Differential Equations --- math-82/notes/Classifying ordinary differential equations#Order|Second order]], [[Differential Equations --- math-82/notes/Classifying ordinary differential equations#Linearity|linear]], [[Differential Equations --- math-82/notes/Classifying ordinary differential equations#_definition _ homogenous and non-homogenous linear differential equation|homogenous]] constant-coefficient differential equations are exactly what you think they are. They're second order linear homogenous differential equations where the coefficients of the dependent variable and its derivatives are all constant factors.
Lots of important examples of these are oscillating physical systems.
![[Differential Equations --- math-82/notes/Oscillating physical systems#_example _ mass-spring systems|Oscillating physical systems]]


### Solving them

We want to solve the differential equation
$$
ay'' + by' + cy = 0
$$
for arbitrary constants $a, b, c \in \mathbb{R}$. 

We can just guess at a solution! A bad guess would be just any polynomial function of the independent variable. For example,

##### _example:_ a bad guess

$y(x) = x^2$ gives us that we must have
$$
cx^2 + 2bx + 2c = 0
$$
for the differential equation to hold. At best, this holds at two isolated points in $\mathbb{R}$, and it may not even hold at one.

A much better guess would take into account that the fact that for the equation to hold everywhere, the function and its first and second derivatives should all look alike everywhere. The exponential function looks like this!

##### _example:_ a better guess

Suppose $y(x) = e^{\lambda x}$ for some $\lambda \in \mathbb{R}$. Then, for the equation to hold we must have
$$
(a \lambda^2 + b \lambda + c)y(x) = 0
$$
at all $x$. Then either, $y(x) = 0$ always which is always a solution of a homogenous equation, or $\lambda$ is a root of $az^2 + bz + c$. We have an interesting possible solution! Does a $\lambda$ a root of $az^2 + bz + c$ always give $e^{\lambda x}$ as a solution of the differential equation? Yes! Are these all the solutions? Sometimes!

##### _proposition:_ the solutions of $ay'' + by' + c = 0$

Let $az^2 + bz + c$ be the characteristic polynomial of $ay'' + by' + c = 0$. Then the characteristic polynomial has either

- two distinct real roots $\lambda_{1}, \lambda_{2}$, in which case any solution of the differential equation must satisfy $y(x) = c_{1} e^{ \lambda_{1} x } + c_{2} e^{ \lambda_{2} x }$ for constants $c_{1}, c_{2} \in \mathbb{R}$,
- two distinct (non-real) complex roots $\lambda_{1}, \lambda_{2}$. in which case any solution of the differential equation must satisfy $y(x) = e^{ \sigma x }(c_{1} \cos(\omega x) + c_{2} \sin(\omega x))$ for constants $c_{1}, c_{2} \in \mathbb{R}$, where $\lambda_{1} = \sigma + \omega i$,
or
- one real root $\lambda$, in which case any solution of the differential equation must satisfy $y(x) = c_{1}e^{ \lambda x } + c_{2} x e^{ \lambda x }$ for constants $c_{1}, c_{2} \in \mathbb{R}$.

###### _proof:_

Note that $y(x) = e^{ \lambda x }$ is only a solution if
$$
e^{ \lambda x }(a \lambda^{2} + b \lambda + c) = 0
$$
for all $x$. Since $e^{ \lambda x }$ is always nonzero, we must have that $a \lambda^{2} + b \lambda + c = 0$. That is, $\lambda$ is a root of the characteristic polynomial.

Note that we need the following ![[#_lemma _ the solution space of $ay'' + by' + cy = 0$ has dimension $2$]]
If we have two distinct real roots $\lambda_{1}, \lambda_{2} \in \mathbb{R}$, then note that the two solutions $e^{ \lambda_{1} x }, e^{ \lambda_{2} x }$ are linearly independent and thus span all solutions.

If we have two distinct (non-real) complex roots $\lambda_{1}, \lambda_{2} \in \mathbb{C} \setminus \mathbb{R}$, then we know that $e^{ \lambda_{1} x }, e^{ \lambda_{2} x }$ technically satisfy our differential equation, but we don't want to use them because they are complex-valued functions. 

Instead, we can notice that $\lambda_{1}, \lambda_{2}$ must be complex conjugates, and thus, for $\lambda_{1} = \sigma + \omega i$ we have $\lambda_{2} = \sigma - \omega i$. Then
$$
\begin{split}
e^{ \lambda_{1} x } & = e^{ (\sigma + \omega i)x } \\
 & = e^{ \sigma x }e^{ \omega ix } \\
 & = e^{ \sigma x } (\cos(\omega x) + i \sin(\omega x))
\end{split}
$$
by Euler's formula. Similarly, $e^{ \lambda_{2} x} = e^{ \sigma x }(\cos(\omega x) - i \sin(\omega x))$.

Adding and dividing by $2$ or subtracting and dividing by $2i$ preserves the fact that the functions satisfy the differential equation and gives us the linearly independent solutions $e^{ \sigma x } \cos(\omega x)$ and $e^{ \sigma x } \sin(\omega x)$ respectively.

Finally, if we have just one real root, $\lambda$, then $e^{ \lambda x }$ is clearly a solution. Note that we must have $\lambda = -b/2$. Let a second linearly independent solution to the differential equation be $y(x) = v(x) e^{ \lambda x }$ for some non-constant function $v$. Then we have
$$
y' = v' e^{ \lambda x } + \lambda v e^{ \lambda x }
$$
and
$$
y'' = \lambda^2 v e^{ \lambda x } + 2 \lambda v' e^{ \lambda x } + v'' e^{ \lambda x }.
$$
Plugging these into $ay'' + by' + cy = 0$ gives us
$$
v(\lambda^2 e^{ \lambda x } + \lambda e^{ \lambda x } + e^{ \lambda x }) + v'' e^{ \lambda x } + v'(2 \lambda e^{  \lambda x } + b e^{ \lambda x }) = 0
$$
which reduces to
$$
v'' e^{ \lambda x } + v'(2 \lambda e^{ \lambda x } + b e^{  \lambda x }) = 0
$$

Now in two steps, we can solve for $v$. First,
$$
\frac{v''}{v'} = - 2 \lambda - b
$$
giving us
$$
\log v' = -x(2 \lambda + b)
$$
or
$$
v' = e^{ -2 \lambda x - bx }.
$$
But since $\lambda = - b/2$, this is just $v' = 1$ and thus, $v = x$. Thus, $e^{ \lambda x }$ and $x e^{  \lambda x }$ form two linearly independent solutions that span the space of solutions.

Note that this result has a [[Differential Equations --- math-82/notes/Oscillating physical systems#Damping|physical interpretation in terms of damping]]

##### _lemma:_ the solution space of $ay'' + by' + cy = 0$ has dimension $2$

The subset $U$ of all functions into $\mathbb{R}$ such that all $u \in U$ give $au'' + bu' + cu = 0$ is a $2$-dimensional subspace of all functions into $\mathbb{R}$.

###### _proof:_

Note that the set of all solutions to the differential equation forms a vector space over $\mathbb{R}$ ([[Differential Equations --- math-82/notes/Existence and uniqueness#_proposition _ solutions of (homogenous) linear differential equations form a vector space|we showed this here]]).

We claim it has dimension $2$. This is due to the [[Differential Equations --- math-82/notes/Existence and uniqueness#_theorem _ existence and uniqueness for second order linear differential equations|second order existence and uniqueness theorem]]. Since every pair of initial conditions $(y(0), y'(0))$ has a unique solution corresponding to it, we have a bijection between $\mathbb{R}^2$ and the space of all solutions. This bijection is linear since evaluating at a point and taking derivatives at a point are both linear maps. That is, $\mathbb{R}^2$ is isomorphic to $U$. Thus, $\dim U = 2$.

Note that this proof applies more generally to differential equations $y'' + p_{1}(x) y' + p_{2}(x) y = 0$ with non-constant coefficients as well.