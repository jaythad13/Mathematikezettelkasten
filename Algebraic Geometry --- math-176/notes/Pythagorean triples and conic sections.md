---
tags:
- math-176/1
- alg-geo
---

### Pythagorean triples

How many integer solutions are there to Pythagorean theorem? That is, how can we find integers $a, b, c$ such that $a^{2} + b^{2} = c^{2}$.

We know that the answer isn't none — $3^{2} + 4^{2} = 5^{2}$. In fact, we know that there are certainly infinitely many, since we can scale any answer by an integer. But what are all the triples? Or equivalently, what are all the triples we can't divide further?

For any triple, consider $t = \frac{a}{c - b}$. Then we can rewrite the equation as $(t(c - b))^2 = c^2 - b^2$ which gives us that $t^2 = \frac{c + b}{c - b}$ as long as we don't have the silly triangle with $a = 0$ and $c = b$. We can rewrite this as $\frac{b}{c} = \frac{t^2 - 1}{t^{2} + 1}$ using just algebraic manipulation. Then, we can get $\frac{a}{c} = \frac{2t}{t^{2} + 1}$ by substituting back $a = t(c - b)$. That is, we can get ratios!

| $a$ | $b$  | $c$  | $t$ |
| --- | ---- | ---- | --- |
| $3$ | $4$  | $5$  | $3$ |
| $8$ | $15$ | $17$ | $4$ |
| $6$ | $8$  | $10$ | $3$ |

The fact that $3, 4, 5$ and $6, 8, 10$ have the same $t$, and the fact that $t$ determines the ratios $\frac{a}{b}$ and $\frac{b}{c}$ suggests the following result.

##### _proposition:_ the character of a Pythagorean triple

Let $a, b, c$ be a Pythagorean triplet. Then there exists a rational number $t$ such that
$$
a : b : c = 2t : t^{2} - 1 : t^{2} + 1
$$
where we write $a_{1} : b_{1} : c_{1} = a_{2} : b_{2} : c_{2}$ if there is a nonzero rational number $\lambda$ such that $(a_{1}, b_{1}, c_{1}) = \lambda(a_{2}, b_{2}, c_{2})$.

Where does the magical $t$ come from? That's what algebraic geometry helps us figure out.

If we think of the equation $a^{2} + b^{2} = c^{2}$ as $x^{2} + y^{2} = 1$, then we can rewrite $t$ as
$$
\begin{split}
t & = \frac{a}{c - b} \\
 & = \frac{c + b}{a} \\
 & = \frac{1 + y}{x}.
\end{split}
$$

That is, we have another equation that says $y = tx - 1$. If we look at the circle $x^{2} + y^{2} = 1$ and the line $y = tx - 1$ geometrically, we can see that the line intersects the circle at two points — $(0, -1)$ and $\left(\frac{2t}{t^{2} + 1}, \frac{t^{2} - 1}{t^{2} + 1} \right )$. Thus, by choosing a rational slope $t$, we get a rational point on the circle. Conversely, notice that every rational point on the circle gives us a line of rational slope passing through itself and $(0, -1)$.

### Conic sections

The geometric idea in the previous case generalises to more difficult equations to solve. If we can find one non-zero solution $a_{0}, b_{0}, c_{0}$ to a general quadratic equation $A a^{2} + B ab + C b^{2} + D ac + E bc + F c^{2} = 0$. If we consider $x = a/c$, $y = b / c$, $x_{0} = a_{0} / c_{0}$, and $y_{0} = b_{0} / c_{0}$, we can solve for 
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

Specifically,

##### _theorem:_ the general solution of a quadratic equation

Suppose $A a^{2} + B ab + C b^{2} + D ac + E bc + F c^{2} = 0$ has at least one non-zero integral solution $a_0, b_{0}, c_{0}$. Then, assuming $c_{0} \neq 0$ (without loss of generality) the general solution is of the following form for some integers $m$ and $n$.
$$
a : b : c =
$$