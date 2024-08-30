---
tags:
- math-176/3
- alg-geo
---

In 1637, Pierre de Fermat asked "What are the integer solutions to $x^{2} - 61 y^{2} = 1$?". Together with William Brouncker and John Wallis, he found that the smallest positive integer solution is $(1766319049, 226153980)$. They went as far as to prove 

##### _theorem:_ Pell's equations

Given a positive integer $d$ that is not a square, we can always find infinitely many integers $x, y$ satisfying $x^{2} - d y^{2} = 1$.

How did they do that? (Also why are they called Pell's equations?)

### History

After Wallis, Brouncker, and Fermat exchanged letters, in 1659 Pell wrote them up in a textbook. Much later (1766) Euler read the text and called the equations "Pell's equations". Now they're known as Pell's equations. A little later (1771), Lagrange came up with a much simpler proof using abstract algebra.

### Rational solutions

$x^{2} - d y^{2} = 1$ actually looks a lot like the [[Algebraic Geometry --- math-176/notes/Diophantine equations#_definition _ homogenous polynomial|reductions of homogenous polynomials]] we've seen. It's clear that we can get infinitely many rational solutions by the same rational line method we used to solve [[Algebraic Geometry --- math-176/notes/Pythagorean triples and conic sections#_theorem _ the general solution of a quadratic equation|conic sections]] in general. On the other hand, it's clear that not all $d$ give us infinitely many solutions —

##### _proposition:_ negative $d$ has finitely many solutions

For a negative integer $d$, there are only finitely many integers $x, y$ that satisfy $x^{2} - d y^{2} = 1$.

###### _proof sketch:_ 

Since $x^{2} + \lvert d \rvert y^{2} = 1$, $\lvert x \rvert$ and $\lvert y \rvert$ are bounded by $1$. There are only finitely many such numbers.

### Algebraic integers

Really, to solve $x^{2} - d y^{2}$, we want to find a way to factorise $x^{2} - d y^{2}$. Usually, we would factorise the difference of squares as $(x + y \sqrt{ d })(x - y \sqrt{ d })$. Then we could just search for all units $(x + y \sqrt{ d })$ with norm $1$. Only, $\sqrt{ d }$ might not exist in the integers. So we adjoin it!

##### _definition:_ algebraic integers

The algebraic integers are $\mathbb{Z}[\sqrt{ d }] \cong \mathbb{Z}[x]/(x^{2} - d)$.

##### _proposition:_ the algebraic integers are a ring

If $d$ is not a square, $\mathbb{Z}[\sqrt{ d }]$ forms an [[Abstract Algebra I --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]].

###### _proof sketch:_

If you're willing to believe $\mathbb{Z}[\sqrt{ d }] \cong \mathbb{Z}[x]/(x^{2} - d)$, then $\mathbb{Z}[\sqrt{ d }]$ is commutative already. Note that $(x^{2} - d)$ is prime — $x^{2} - d$ doesn't factor unless $d$ is a square. Thus, $\mathbb{Z}[x]/(x^{2} - d)$ [[Abstract Algebra I --- math-171/notes/Prime and maximal ideals#_proposition _ prime ideals have integral domains as quotients|must be an integral domain]].

In analogy with the [[Complex Analysis --- math-135/notes/What is complex analysis?#_definition _ complex conjugate, $ overline{z}$|complex numbers]], we define the conjugate of an algebraic integer, and the norm on $\mathbb{Z}[\sqrt{ d }]$ as the product of a number and its norm.

##### _definition:_ conjugates

The conjugate of an algebraic integer $a = x + y \sqrt{ d }$ is $\overline{a} = x - y \sqrt{ d }$.

##### _definition:_ the norm on $\mathbb{Z}[\sqrt{ d }]$

The norm of an algebraic integer $a$ is $Na = a \overline{a}$. For $a = x + y \sqrt{ d }$ note that $Na = x^{2} - d y^{2}$.

Note that this satisfies the definition of a norm in a ring.
![[Abstract Algebra I --- math-171/notes/Factorisation in special rings#_definition _ norm|Factorisation in special rings]]

It's easy to see that the conjugate and norm are both multiplicative.

Thus, if we can find one algebraic integer $a$ with norm $1$, we can find infinitely many $a^n$ with norm $1$.

##### _example:_ infinitely many solutions to $x^{2} - 2 y^{2}$

$(x, y) = (3, 2)$ is an obvious solution to the equation. That is, $3 + 2 \sqrt{ 2 }$ has norm $1$ in $\mathbb{Z}[\sqrt{ 2 }]$. Thus, so do $(3 + 2 \sqrt{ 2 })^{2} = 17 + 12 \sqrt{ 2 }$ and so on.