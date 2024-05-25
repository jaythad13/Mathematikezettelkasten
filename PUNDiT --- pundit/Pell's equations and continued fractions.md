---
tags:
- nt
- alg-nt
- PUNDiT
---

We've already seen various Diophantine equations. One more is
$$
x^2 - d y^2 = 0 
$$
for some integer $d$.

Fermat found a method to solve this for $d = 61$. Brouncker and Wallis figured out how to do this for arbitrary $d$. Pell wrote a book about their work. Finally, Euler read Pell's book and assumed that the theory was Pell's and called them Pell's equations.

Brahmagupta and Bhaskacharya also worked out solutions to the same question earlier.

Remember that any Diophantine equation of the form $x^2 - d y^2 = 0$ has infinitely many rational solutions as it has at least one rational solution $(1, 0)$, and we can then get infinitely many by drawing lines of rational slope. This is boring. What about integer solutions?

##### _example:_ $x - 2y^2 = 0$

Note that for the first five integer solutions
$$
\begin{gathered}
	(x_0, y_0) = (1, 0) \\
	(x_1, y_1) = (3, 2)
\end{gathered}
$$
we have the identity

##### _example:_ $x - 61 y^2 = 1$

One nontrivial integer solution that Fermat found is 
$$
(x_1, y_1) = (1766319049, 226153980).
$$
This is the smallest integer solution to the equation. How did Fermat find this by hand?

##### _theorem:_

For some integer $d$ that is not a square, for the Diophantine equation $x^2 - d y^2 = 1$
- there are infinitely many rational solutions $(x, y)$
- there are infinitely many integer solutions if and only if $d$ is positive.

We sketch out the proof of this theorem today.

### Extensions to the integers

If we want to factor $x^2 - d y^2$, we need to be able to write
$$
x^2 - d y^2 = (x + \sqrt{d} y)(x - \sqrt{d} y)
$$
which leads us to consider the ring
$$
\bb{Z}[\sqrt{d}] = \set{ x + y \sqrt{d} : x, y \in \bb{Z}}.
$$

Note that there is a multiplicative norm on $\bb{Z}[d]$, with $\norm{x + y \sqrt{d}} = x^2 - d y^2$. Obviously, if $\norm{a} = 1$ for some $a \in \bb{Z}[d]$, then $(x, y)$ is a solution for $a = x + y \sqrt{d}$. 

### Using continued fractions


##### _definition:_ continued fraction

Given a real number $x$, the continued fraction approximating $x$ is given by the recurrence relation
$$
\begin{gathered}
	x_0 = x \\
	x_{k+1} = \frac{1}{x_k - {[x_k]}}.
\end{gathered}
$$

We can rewrite each $x - [x_k]$ as an integer $a_k$.

##### _example:_ $\sqrt{2}$ as a continued fraction

$$
\begin{gathered}
	x_0 = \sqrt{2}
\end{gathered}
$$

Thus,
$$
x = \frac{1}{2 + \frac{1}{2 + \frac{1}{2 + \frac{1}{2 + \ldots}}}}.
$$ 
We

##### _theorem:_ 

Fix a positive integer $d$ which is not a square. For $\sqrt{d} = \set{a_0; \overline{a_1, \ldots, a_{h-1}}}$ 