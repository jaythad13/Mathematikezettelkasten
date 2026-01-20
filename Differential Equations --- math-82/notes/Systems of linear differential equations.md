---
tags:
- math-82/14
- math-82/15
- math-82/16
- math-82/17
- math-82/18
- diff-eq
---

Systems of (first order) linear differential equations are really useful! Most importantly, any higher order differential equation can be rewritten as a system of first order differential equations, so solving systems solves everything!

We can always assume all of the equations are [[Differential equations --- math-82/notes/Classifying ordinary differential equations#_definition _ autonomous and non-autonomous differential equations|autonomous]] — if they depend on some dependent variable $t$, then just add an equation $t' = 1$ to the system. This allows us to define equilibirum points easily.

##### _definition:_ equilibrium points

A point $x_{0}$ is an **equilibrium point** of the system $x' = f(x)$ (where $x$ is a function $\mathbb{R} \to \mathbb{R}^n$ and $f$ is a function $\mathbb{R}^n \to \mathbb{R}^n$) if $f(x_{0}) = 0$.

---

Existence and uniqueness holds for systems of $n$ first order, homogeneous, linear systems as well, and the solution space is $n$-dimensional. 

##### _definition:_ fundamental matrix

A **fundamental matrix** of a linear homogeneous system of first order differential equations is a matrix $\Psi(t)$ whose columns are $n$ linearly independent solutions to the system.

---

### Homogeneous, constant-coefficient, linear systems

When we solve homogeneous, constant coefficient systems of the form $x' = A x$ for some matrix $A : \mathbb{R}^n \to \mathbb{R}^n$, linear algebra makes things particularly nice.

##### _proposition:_ solving diagonal systems

Consider the differential equation $x' = A x$ for some matrix $A : \mathbb{R}^n \to \mathbb{R}^n$. Suppose $A$ is diagonalisable with $P ^{-1} A P = D$ having eigenvalues $\lambda_{1}, \dots, \lambda_{n}$ on the diagonal (with repeats). Then $x(t) = c_{1} v_{1} e^{\lambda_{1} t} + \dots c_{n} v_{n} e^{\lambda_{n} r}$ is the general solution of the equation for $P = (v_{1}, \dots, v_{n})$ and free choice of $c_{i}$.

###### _proof sketch:_

Let $x = P y$ or equivalently, $y = P ^{-1} x$. Then $x' = A x$ is equivalent to $P ^{-1} x = P ^{-1} A x$. Writing $x = P y$ on the right hand side, this is equivalent to $y = P ^{-1} A P y = D y$. Solving each equation for $y$ individually, choosing $c_{i}$. Then write $x = P y$.

---

This is just the first case of a more general solution. First we need to define the matrix exponential.

##### _definition:_ matrix exponential

For a matrix $A$, the **matrix exponential** denoted $e^{A}$ or $\exp A$ is the matrix
$$
I + A + \frac{1}{2!} A^{2} + \frac{1}{3!} A^3 + \dots + = \sum_{i = 0}^n \frac{A^n}{n!}.
$$

---

##### _theorem:_ the solution of a homogeneous, constant-coefficient, linear system

The unique solution to the differential equation $x' = A x$ with initial condition $x(0) = x_{0}$ is $x(t) = e^{A t} x_{0}$.

###### _proof sketch:_

It is a fact that $e^{A t}$ has derivative $A e^{A t}$ with respect to $t$. Thus, $x(t) = e^{A t} x_{0}$ satisfies the differential equation and initial condition.

---
 
This recovers the original theorem since if $D$ is diagonal with eigenvalues $\lambda_{1}, \dots, \lambda_{n}$ on the diagonal, then $e^{Dt}$ has entries $e^{\lambda_{1} t}, \dots, e^{\lambda_{n} t}$ on the diagonal.

Since $A$ is just an object of linear algebra, we can understand the equilibrium points of the corresponding differential equation qualitatively. For example, if $A$ is invertible, then the only equilibrium point is at the origin, but if $A$ is not, then there is a whole linear subspace worth of equilibrium points. With an understanding of $A$'s [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_definition _ eigenvalue, eigenvector|eigenvalues]], we can say even more. For example, along an expanding eigenspace, the solution is "unstable" but a contracting eigenspace can create a stable equilibrium at the origin. This is described in [[Differential equations --- math-82/attachments/texts/lecture notes/lecture 18.pdf#page=4|the lecture notes]].

For a $2$-by-$2$ matrix we can obtain this information without actually computing the eigenvalues — we can just compute the trace and determinant and use the fact that any eigenvalues $\lambda$ satisfy $\lambda^{2} - \operatorname{tr}(A) \lambda + \det A = 0$. Write $T$ for the trace and $D$ for the determinant. Note that $T$ is the sum of the eigenvalues and $D$ their product. If $T^{2} \geq D$ then the eigenvalues are real. If $T$ and $D$ are positive, then both eigenvalues are positive. If $D$ is positive and $T$ negative then both are negative. If $D$ is negative, then they are both different. If $T^{2} < 4D$ then $T$ describes the real part of the complex eigenvalues. If it is positive, so is the real part, if it is $0$ the eigenvalues are imaginary, if it is negative, then they are negative.

### Upper-triangular systems

In some special cases, we can solve more general linear systems with varying coefficients. In particular, if $A(t)$ is always upper or lower triangular, we can solve each differential equation one at a time.

### Variation of parameters and undetermined coefficients

[[Differential equations --- math-82/notes/Variation of parameters|Variation of parameters]] and the method of [[Differential equations --- math-82/notes/Undetermined coefficients|undetermined coefficients]] work pretty much just as they did for single equations.

##### _theorem:_ variation of parameters for systems

Suppose $\Psi(t)$ is a fundamental matrix of the system $x' = A(t) x$. Then
$$
x(t) = \Psi(t) \Psi(t_{0})^{-1} x(t_{0}) + \int_{t_{0}}^t \Psi(s)^{-1} f(s) \, ds
$$
is a solution to the linear system $x' - A(t) x = f(t)$.

---

In the special case where $A$ is constant $\Psi(t) = e^{A t}$ so
$$
x(t) = e^{A(t - t_{0})} x(t_{0}) + e^{A t} \int_{t_{0}}^t e^{-A s} f(s) \, ds
$$
is the solution.

For undetermined parameters, again just guess some sufficiently general form for $x(t)$ based on the form of $f(t)$ and muck around with the coefficients so that it works.