---
tags:
- math-176/3
- math-176/5
- alg-geo
---

In 1637, Pierre de Fermat asked "What are the integer solutions to $x^{2} - 61 y^{2} = 1$?". Together with William Brouncker and John Wallis, he found that the smallest positive integer solution is $(1766319049, 226153980)$. They went as far as to prove 

##### _theorem:_ Pell's equations

Given a positive integer $d$ that is not a square, we can always find infinitely many integers $x, y$ satisfying $x^{2} - d y^{2} = 1$.

How did they do that? (Also why are they called Pell's equations?)

### History

After Wallis, Brouncker, and Fermat exchanged letters, in 1659 Pell wrote them up in a textbook. Much later (1766) Euler read the text and called the equations "Pell's equations". Now they're known as Pell's equations. A little later (1771), Lagrange came up with a much simpler proof using abstract algebra.

### Rational solutions

$x^{2} - d y^{2} = 1$ actually looks a lot like the [[Algebraic Geometry --- math-176/notes/Some more Diophantine equations#_definition _ homogenous polynomial|reductions of homogenous polynomials]] we've seen. It's clear that we can get infinitely many rational solutions by the same rational line method we used to solve [[Algebraic varieties --- math-176/notes/Pythagorean triples and conic sections#_theorem _ the general solution of a quadratic equation|conic sections]] in general. On the other hand, it's clear that not all $d$ give us infinitely many solutions —

##### _proposition:_ negative $d$ has finitely many solutions

For a negative integer $d$, there are only finitely many integers $x, y$ that satisfy $x^{2} - d y^{2} = 1$.

###### _proof sketch:_ 

Since $x^{2} + \lvert d \rvert y^{2} = 1$, $\lvert x \rvert$ and $\lvert y \rvert$ are bounded by $1$. There are only finitely many such numbers.

### Algebraic integers

Really, to solve $x^{2} - d y^{2}$, we want to find a way to factorise $x^{2} - d y^{2}$. Usually, we would factorise the difference of squares as $(x + y \sqrt{ d })(x - y \sqrt{ d })$. Then we could just search for all units $(x + y \sqrt{ d })$ with norm $1$. Only, $\sqrt{ d }$ might not exist in the integers. So we adjoin it!

##### _definition:_ algebraic integers

The algebraic integers are $\mathbb{Z}[\sqrt{ d }] \cong \mathbb{Z}[x]/(x^{2} - d)$.

##### _proposition:_ the algebraic integers are a ring

If $d$ is not a square, $\mathbb{Z}[\sqrt{ d }]$ forms an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]].

###### _proof sketch:_

If you're willing to believe $\mathbb{Z}[\sqrt{ d }] \cong \mathbb{Z}[x]/(x^{2} - d)$, then $\mathbb{Z}[\sqrt{ d }]$ is commutative already. Note that $(x^{2} - d)$ is prime — $x^{2} - d$ doesn't factor unless $d$ is a square. Thus, $\mathbb{Z}[x]/(x^{2} - d)$ [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_proposition _ prime ideals have integral domains as quotients|must be an integral domain]].

In analogy with the [[Complex analysis --- math-135/notes/What is complex analysis?#_definition _ complex conjugate, $ overline{z}$|complex numbers]], we define the conjugate of an algebraic integer, and the norm on $\mathbb{Z}[\sqrt{ d }]$ as the product of a number and its norm.

##### _definition:_ conjugates

The conjugate of an algebraic integer $a = x + y \sqrt{ d }$ is $\overline{a} = x - y \sqrt{ d }$.

##### _definition:_ the norm on $\mathbb{Z}[\sqrt{ d }]$

The norm of an algebraic integer $a$ is $Na = a \overline{a}$. For $a = x + y \sqrt{ d }$ note that $Na = x^{2} - d y^{2}$.

Note that this satisfies the definition of a norm in a ring.
![[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ norm|Factorisation in special rings]]

It's easy to see that the conjugate and norm are both multiplicative.

Thus, if we can find one algebraic integer $a$ with norm $1$, we can find infinitely many $a^n$ with norm $1$.

##### _example:_ infinitely many solutions to $x^{2} - 2 y^{2}$

$(x, y) = (3, 2)$ is an obvious solution to the equation. That is, $3 + 2 \sqrt{ 2 }$ has norm $1$ in $\mathbb{Z}[\sqrt{ 2 }]$. Thus, so do $(3 + 2 \sqrt{ 2 })^{2} = 17 + 12 \sqrt{ 2 }$ and so on.

### The group of units

%%lecture 4%%

### Continued fractions and the fundamental unit

It's clear that then that all we have to do is find one non-trivial solution to Pell's equations. Then we'll get infinitely many solutions! We show this by using continued fractions.

##### _definition:_ continued fraction, $n$th convergent

Say $z$ is a real irrational. We construct a sequence of irrational numbers $(z_{n})$ recursively with
$$
\begin{split}
z_{0} & = z \\
z_{k + 1} & = \frac{1}{z_{k} - \lfloor z_{k} \rfloor }
\end{split}
$$
Note here that
$$
z_{k} = \lfloor z_{k} \rfloor + \frac{1}{z_{k + 1}}
$$

Then expanding out $z$, we get
$$
z = a_{0} + \frac{1}{a_{1} + \frac{1}{a_{2} + \frac{1}{a_{3} + \cdots}}}
$$as the continued fraction of $z$ for $a_{k} = \lfloor z_{k} \rfloor$.

The $n$th convergent is the rational
$$
a_{0} + \frac{1}{a_{1} + \frac{1}{a_{2} + \frac{1}{\ddots + \frac{1}{a_{n  -1}}}}}.
$$
This notation is not standard — most books call this is the $(n - 1)$th convergent. It's a fact of analysis that the sequence $n$th convergents converges to $z$, and is also the "best" rational approximation of $z$ in some sense.

##### _example:_ the continued fraction of $\sqrt{ 2 }$

| $k$ | $z_{k}$          | $a_{k}$ |
| --- | ---------------- | ------- |
| $0$ | $\sqrt{ 2 }$     | $1$     |
| $1$ | $\sqrt{ 2 } + 1$ | $2$     |
| $2$ | $\sqrt{ 2 } + 1$ | $2$     |
and from there on we can see that this repeats (it's a one term recurrence that has $z_{1} = z_{2}$ and $a_{1} = a_{2}$). To be precise,

| $k$     | $z_{k}$          | $a_{k}$ |
| ------- | ---------------- | ------- |
| $0$     | $\sqrt{ 2 }$     | $1$     |
| $\ge 1$ | $\sqrt{ 2 } + 1$ | $2$     |
|         |                  |         |
and the continued fraction of $z$ gives us
$$
\sqrt{ 2 } = 1 + \frac{1}{2 + \frac{1}{2 + \frac{1}{2 + \cdots}}}.
$$

##### _theorem:_ the continued fraction of $\sqrt{ d }$ (Lagrange)

Let $d$ be a positive non-square integer. Then the continued fraction of $\sqrt{ d }$ is
$$
\sqrt{ d } = \{ a_{0}; \overline{a_{1}, a_{2}, \dots, a_{h}} \}
$$
where integers repeat after $h$ terms with $a_{h} = 2 a_{0}$. Moreover, the $h$th convergent $x_{h} / y_{h}$ gives $x_{h}^{2} - d y_{h}^{2} = (-1)^h$.

###### _proof:_ see LeVeque/lecture notes

##### _corollary:_ the fundamental unit

$\delta$ given by
$$
\delta = \begin{cases}
x_{h} + y_{h} \sqrt{ d } & h \text{ is even} \\
x_{2h} + y_{2h} \sqrt{ d } = (x_{h} + y_{h} \sqrt{ d })^{2} & h \text{ is odd}
\end{cases}
$$
is a fundamental unit in $\mathbb{Z}[\sqrt{ d }]$.

###### _proof:_ see LeVeque/lecture notes

##### _corollary:_ non-trivial solutions of Pell's equations (Lagrange)

Given a positive integer $d$ that is not a square, there exists an integer solution $(x, y)$ to $x^{2} - d y^{2} = 1$ where $y > 0$. 

##### _example:_ $d = 2$

We already know that the continued fraction of $\sqrt{ 2 }$ repeats at the second convergent $1 + \frac{1}{2} = \frac{3}{2}$. This gives
$$
3^{2} - 2 \cdot 2^{2} = 1
$$
In fact, the fundamental unit is $3 + 2 \sqrt{ 2 }$, and thus, any solutions $(x, y)$ to Pell's equation give us
$$
x + y \sqrt{ 2 } = \pm (3 + 2 \sqrt{ 2 })^n.
$$

But why did Fermat and gang care about $d = 61$? It's pretty bad

##### _example:_ $d = 61$

$\sqrt{ 61 } = \{ 7;\overline{1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 14} \}$ which has 11 terms. To get the solution, we need to look at the 22nd convergent! That has simplest form $(1766319049, 226153980)$. A computer could never brute force its way to this smallest solution!