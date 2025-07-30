---
tags:
- math-176/1
- borcherds-ag1/1
- alg-geo
---

Our goal is first to see some applications of algebraic geometry without actually going through what the definitions are.

### Pythagorean triples

How many integer solutions are there to Pythagorean theorem? That is, how can we find integers $a, b, c$ such that $a^{2} + b^{2} = c^{2}$.

We know that the answer isn't none — $3^{2} + 4^{2} = 5^{2}$. In fact, we know that there are certainly infinitely many, since we can scale any answer by an integer. But what are all the triples? Or equivalently, what are all the primitive triples (the ones we can't divide further)?

This actually has an simple number-theoretic solution. 

##### _theorem:_ all Pythagorean triples, number-theoretically

$a, b, c \in \mathbb{Z}$ are a primitive (non-trivial) Pythagorean triple if and only if
$$
a = \frac{r^{2} - s^{2}}{2} \quad b = r^{2} s^{2} \quad c = \frac{r^{2} + s^{2}}{2}
$$
for positive integers $r , s$.

###### _proof:_

Let $a, b, c$ be all [[Superdiscrete --- math-55A/notes/Dividing integers - basic number theory#_definition _ relatively prime|coprime]] ($\gcd(a, b, c) = 1$, rather than pairwise). Then consider the equation $a^{2} + b^{2} = c^{2}$ modulo $4$. Since $a^{2}, b^{2}, c^{2}$ are all squares, they must be $0$ or $1$ modulo $4$ ($2^{2} \equiv 4$ and $3^{2} \equiv 1$ in $\mathbb{Z} / 4 \mathbb{Z}$). For them to be not all even, they must have at least one of the squares odd. If $c^{2}$ is even, then we would have to have both $a^{2}, b^{2}$ odd, giving $a^{2} = b^{2} + c^{2} \equiv 2$ modulo $4$. Thus, $c^{2}$ is odd. One of $a^{2}, b^{2}$ is even, and the other odd. Without loss of generality, choose $a^{2}$ even and $b^{2}$ odd.

Now we rewrite $a^{2} + b^{2} = c^{2}$ as
$$
b^{2} = c^{2} - a^{2} = (c + a) (c - a)
$$
We claim that $c + a$ and $c - a$ are coprime. This follows because $c$ and $a$ being coprime means that $c + a$ and $c - a$ can only have a common factor at most $2$. Since $c$ is odd and $a$ is even, $c + a$ is odd, $2$ isn't a common factor. Thus, in order for there product to be a square, we can argue from the [[Superdiscrete --- math-55A/notes/Euclid's algorithm and primes#_theorem _ unique factorisation|unique factorisation]] or just [[Superdiscrete --- math-55A/notes/Euclid's algorithm and primes#_theorem _ a divisor must divide something or, the important theorem|Euclid's lemma]] that $c + a$ and $c - a$ must themselves be square (or both negatives of squares, which is equivalent by changing sign in the difference).

Choose $r^{2} = c + a$ and $s^{2} = c - a$. By linear algebra $c = (r^{2} + s^{2}) / 2$ and $a = (r^{2} - s^{2}) / 2$. By our factorisation, $b = r^{2} s^{2}$. We've demonstrated that any solution is of the desired form.

It's easy to see that if $a, b, c$ are given by the triples as desired, then they do indeed give a Pythagorean triple —
$$
\left( \frac{r^{2} - s^{2}}{2} \right)^{2} + r^{2} s^{2} = \frac{r^{4} + s^4 - 2 r^{2} s^{2} + 4 r^{2} s ^{2}}{4} = \frac{r^{4} + s^4 + 2 r^{2} s^{2}}{4} = \left( \frac{r^{2} + s^{2}}{2} \right)^{2}.
$$

Thus, the primitive Pythagorean triples can be parameterised by pairs of square integers. 

This answer is unsatisfying because we had to make several assumptions to treat $x$ or $y$ in different ways, and it isn't clear how to generalise this method to find all integer solutions of equations in general. What we can do instead is try to understand the Pythagorean triples geometrically.

If we instead try to understand (the equivalent problem) of finding rationals $x = a / c$ and $y = b / c$ such that $x^{2} + y^{2} = 1$, we obtain a much more general solution by methods of algebraic geometry. In particular we understand $x^{2} + y^{2} = 1$ as points on a circle, and use methods of algebraic geometry to unwrap it into a line except at one point.

##### _theorem:_ the Pythagorean birational equivalence

$x, y \in \mathbb{Q}$ with $(x, y) \neq (-1, 0)$ satisfy $x^{2} + y^{2} = 1$ if and only if 
$$
x = \frac{1 - t^{2}}{1 + t^{2}} \quad y = \frac{2t}{1 + t^{2}}
$$
for some $t \in \mathbb{Q}$. Any $x, y \in \mathbb{Q}$ are non-trivial solutions to $x^{2} + y^{2}$ if and only if they are as above with $t \in \mathbb{Q} \setminus \{ 0 \}$.

###### _proof:_

We can understand the set of solutions $\{ (x, y) \in \mathbb{Q}^{2} \mid x^{2} + y^{2} = 1 \}$ as the rational points on the circle $\mathbb{Q}^{2} \cap S^1 \subseteq \mathbb{R}^{2}$.

Note that $(x, y) = (-1, 0)$ satisfies $x^{2} + y^{2} = 1$. Any other rational solution to the equation has a line between it and $(-1, 0)$ of rational slope, say $t \in \mathbb{Q}$. Conversely, if I pick a rational slope $t$ and consider the line $y = t(x + 1)$ through $(-1, 0)$, I can solve for $x$ in
$$
t^{2}(x + 1)^{2} + x^{2} = 1
$$
as
$$
t^{2}(x + 1)^{2} + (x + 1)(x - 1) = 0
$$
and thus
$$
(x + 1)((t^{2} + 1)x + t^{2} - 1)
$$
to get
$$
x = \frac{1 - t^{2}}{1 + t^{2}}
$$
and thus,
$$
y = \frac{2t}{1 + t^{2}}
$$
or of course, $(x, y) = (-1, 0)$. These points are clearly rational. 

One intuitive reason for getting a rational is Vieta's equations — we have a rational quadratic polynomial and so if one root is rational, and the sum of the roots is rational, the other root is rational.

Another way to understand this is by analysing what this mysterious $t$ is. Algebraically, it's $(y - 1) / x$ at every point except $(1, 0)$ where it is $0$ and $(-1, 0)$ where it is undefined, but could be $\pm \infty$. In some sense, the circle is the an algebraic wrapping of the line. Notice that the line $y = t(x + 1)$ has $y$-intercept $t$. Thus, we really do have a correspondence between rational points on the circle and rational points on a line, with the exception of a single point on the circle. Such a map (that is, an isomorphism given by rational functions except on subsets of codimension $1$), is called a birational equivalence. This notion isn't particularly useful in differential geometry because you can typically cut a surface along a curve to get unions of discs, and similarly in higher dimensions. However, with the topology that we will put on the objects of algebraic geometry, we will see that this really does make sense.

This birational equivalence has a nice application in calculus — we can write $\cos \theta = x$, $y = \sin \theta$, and then we get $t = \tan (\theta / 2)$ which is called the Weierstrass substitution to write an integral involving $\cos \theta$ and $\sin \theta$ as an integral involving rational functions
$$
\frac{1 - t^{2}}{1 + t^{2}} \quad \frac{2t}{1 + t^{2}}.
$$

The geometric idea generalises to more difficult equations to solve. If we can find one non-zero solution $a_{0}, b_{0}, c_{0}$ to a general quadratic equation $A a^{2} + B ab + C b^{2} + D ac + E bc + F c^{2} = 0$. If we consider $x = a/c$, $y = b / c$, $x_{0} = a_{0} / c_{0}$, and $y_{0} = b_{0} / c_{0}$, we can solve for 
$$
\begin{align*}
Ax^2 + Bxy + Cy^{2} + Dx + Ey + F & = 0 \\
y & = t(x - x_{0}) + y_{0}
\end{align*}
$$
where $t  = \frac{y - y_{0}}{x - x_{0}}$. That is, the second equation is a line passing through $(x_{0}, y_{0})$ with rational slope $t$.

Then just do the algebra to solve the system of equations! The exact form of solutions is
$$
(x, y) = (x_{0} - \lambda n, y_{0} - \lambda m)
$$
in terms of $t = m / n$ and
$$
\lambda = \frac{(2 A x_{0} + B y_{0} + D) n + (B x_{0} + 2 C y_{0} + E)m}{A n^{2} + B mn + C m^{2}}.
$$
This gives us that the intersection of the line and curve is a rational point. Again, the fact that any rational point gives us a line of rational slope through itself and $(0, -1)$ means that this gives us all the rational points.