---
tags:
- math-131/24
- math-131/25
- anal
---

### Linearity

The Riemann integral is actually a linear operator on the [[Linear algebra done right --- ladr/notes/Vector spaces#_definition _ vector space|vector space]] of [[Analysis --- math-131/notes/Riemann integration#_definition _ Riemann integrable|Riemann integrable functions]] on $[a, b]$. (Note we still need to show that the Riemann integrable functions form a vector space)

##### _proposition:_ the Riemann integral is additive

If $f, g : [a, b] \to \mathbb{R}$ are Riemann integrable, then $f + g$ is also Riemann integrable with
$$
\int_{a}^b (f + g)(x) \, dx = \int_{a}^b f(x) \, dx + \int_{a}^b g(x) \, dx.
$$

###### _proof sketch:_

The critical idea is that
$$
\sup (f + g) \le \sup f + \sup g
$$
and
$$
\inf(f + g) \ge \inf f + \inf g
$$
so the upper and lower sums of $f + g$ are bounded between the sums of the lower and upper sums of $f$ and $g$. Thus, their difference is bounded by the sum of the differences for $f$ and $g$, giving us that $f + g$ is integrable too.

Considering the difference
$$
\begin{align}
\int_{a}^b f + g \, dx - \left( \int_{a}^b f(x) \, dx + \int_{a}^b f(x) \, dx  \right) & \le U(P, f + g) - L(P, f) - L(P, g) \\
 & \le U(P, f) + U(P, g) - L(P, f) - L(P, g).
\end{align}
$$
with the argument above, we see that it must be less than any positive $\varepsilon$, and thus $0$.

It's also easy to see that

##### _proposition:_ the Riemann integral is homogeneous

If $f : [a, b] \to \mathbb{R}$ is Riemann integrable, then $\lambda f$ is integrable for each $\lambda \in \mathbb{R}$ with
$$
\int_{a}^b \lambda f(x) \, dx = \lambda \int_{a}^b f(x) \, dx.
$$

### Changing limits

Using arguments similar to those for the additivity of the Riemann integral, we can see that we can split off the Riemann into two parts at any point.

##### _proposition:_ splitting intervals

For any Riemann integrable $f : [a, b] \to \mathbb{R}$ and $c \in [a, b]$, we have
$$
\int_{a}^b f(x)  \, dx = \int_{a}^c f(x) \, dx + \int_{c}^b f(x)  \, dx.
$$

### Continuous compositions

One incredibly useful theorem is that the composition of a Riemann integrable function is Riemann integrable. This allows us to integrate a whole new range of functions

##### _theorem:_ composition of a continuous and integrable function

If $f$ is Riemann integrable and $g : [-M, M]$ is continuous, then $h = g \circ f : [a, b] \to \mathbb{R}$ is Riemann integrable.

###### _proof:_

By bounding the difference between upper and lower sums of $f$ by say $\delta^{2}$, show that the intervals of partitions where the difference between the maximum and minimum of $f$ is bigger than $\delta$, are also smaller in length than $\delta$. Bound by the maximum of the function and the length of the intervals on those. On the rest, since we can bound the difference between its maximum and minimum by $\delta$, 

Note that it is not sufficient for both functions to be integrable –

##### _example:_ Thomae's function and non-integrable compositions

Consider
$$
f = \begin{cases}
0 & x = 0 \\
1 & x \neq 0
\end{cases}
$$
and Thomae's function
$$
g = \begin{cases}
0 & x \not\in\mathbb{Q} \\
\frac{1}{q} & x = \frac{p}{q} \in \mathbb{Q}.
\end{cases}
$$

$f$ is clearly continuous everywhere except at $0$ and $g$ is continuous on the irrationals since approximating an irrational by rationals requires denominators $q \to \infty$, so both $f$ and $g$ are continuous almost everywhere.

However, $f \circ g$ is just the Dirichlet function which we already showed is not integrable.

##### _corollary:_ absolute values are integrable

If $f$ is Riemann integrable, $\lvert f \rvert$ is Riemann integrable (on $[a, b]$ for both).

##### _corollary:_ squares are integrable

If $f$ is Riemann integrable, $f^{2}$ is Riemann integrable (on $[a, b]$ for both).

##### _corollary:_ products are integrable

If $f, g$ are Riemann integrable, $fg$ is Riemann integrable (on $[a, b]$ for both).

###### _proof sketch:_

Write
$$
fg = \frac{(f + g)^{2} - f^{2} - g^{2}}{2}
$$
and use the results we have already.

### Inequalities

If a function dominates another, then its integral is greater too.

##### _proposition:_ integrals are order-preserving

Suppose $f, g : [a, b] \to \mathbb{R}$ are integrable with $f(x) \le g(x)$ everywhere in $[a, b]$. Then
$$
\int_{a}^b f(x) \, dx \le \int_{a}^b g(x) \, dx.
$$

##### _proposition:_ the triangle inequality for integrals

Suppose $f : [a, b] \to \mathbb{R}$ is integrable. Then
$$
\left\lvert  \int_{a}^b f(x) \, dx   \right\rvert \le \int_{a}^b \lvert f(x) \rvert  \, dx.
$$
