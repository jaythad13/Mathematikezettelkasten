---
tags:
- math-131/25
- math-131/26
- anal
---

The fundamental theorem of calculus is the first (and most "fundamental") in a series of theorems that say that integrating something over a boundary is the same as integrating its derivative over the inside.

##### _theorem:_ the (converse of) fundamental theorem of calculus

Suppose $f : [a, b] \to \mathbb{R}$ is Riemann integrable and
$$
F(x) = \int_{a}^x f(t) \, dt 
$$
Then $F$ is differentiable at $x$ with $F'(x) = f(x)$.

###### _proof sketch:_

Consider
$$
\frac{F(x + h) - F(x)}{h} = \frac{\int_{x}^{x + h} f(t) \, dt }{h}
$$
for positive $h$.

Bounding $f$ by the upper sum and lower sums over the partition that treats $[x, x + h]$ as a single [[Mathematical Analysis I --- math-131/notes/Riemann integration#_definition _ partition|sub-rectangle]], we get
$$
\inf_{t \in [x, x + h]} \le \frac{F(x + h) - F(x)}{h} \le \sup_{t \in [x, x + h]} f(t)
$$
Since $f$ is [[Mathematical Analysis I --- math-131/notes/Continuity#_definition _ continuity|continuous]], by choosing $f$ small enough we can bound this to
$$
f(x) - \varepsilon \le \frac{F(x + h) - F(x)}{h} \le f(x) + \varepsilon
$$
so
$$
\lim_{ h \to 0^+ } \frac{F(x + h) - F(x)}{h} = f(x)
$$
and similarly for the left hand limit.

While this is often called the first fundamental theorem of calculus, what is more often meant by the fundamental theorem of calculus is the following —

##### _theorem:_ the fundamental theorem of calculus

Let $f : [a, b] \to \mathbb{R}$ be continuous and differentiable in $(a, b)$. If $f'$ is [[Mathematical Analysis I --- math-131/notes/Riemann integration#_definition _ Riemann integrable|Riemann integrable]], then
$$
\int_{a}^b f'(x) \, dx = f(b) - f(a).
$$

###### _proof:_

The main idea here is to use the [[Mathematical Analysis I --- math-131/notes/Mean value theorems#_theorem _ mean value theorem|mean value theorem]] and telescoping sums.

Since $f'$ is Riemann integrable, there exists a [[Mathematical Analysis I --- math-131/notes/Riemann integration#_definition _ partition|partition]] of $[a, b]$ (say the partition $P$ is $a = x_{0} < x_{1} < \dots < x_{n - 1} < x_{n} = b$) with [[Calculus --- spivak/notes/Integration over closed rectangles#_theorem _ integrable upper and lower sums get arbitrarily close|upper and lower sums arbitrarily close]] (say within $\varepsilon$ of each other). That is,
$$
L(P, f) \le \int_{a}^b f'(x) \, dx \le U(P, f) 
$$
with $U(P, f) - L(P, f) < \varepsilon$.

But we can also put $f(b) - f(a)$ between the upper and lower sums using mean value theorem. Write
$$
\begin{align}
f(b) - f(a) & = (f(x_{n}) - f(x_{n - 1})) + \dots + (f(x_{1}) - f(x_{0})) \\
 & = f'(c_{n}) (x_{n} - x_{n - 1}) + \dots + f'(c_{1})(x_{1} - x_{0})
\end{align}
$$
where $c_{i} \in [x_{i- 1}, x_{i}]$ is that $c_{i}$ guaranteed by the mean value theorem to give $f'(c_{i}) = f(x_{i}) - f(x_{i - 1})$. But now clearly we can bound
$$
L(P, f) \le f(b) - f(a) \le U(P, f).
$$ 

##### _corollary:_ integration by parts

Suppose $f, g : [a, b] \to \mathbb{R}$ are continuous and differentiable with Riemann integrable $f', g'$, then
$$
\int_{a}^b f'(x) g(x) \, dx = f(b) g(b) - f(a) g(a) - \int_{a}^b f(x) g'(x) \, dx.
$$

###### _proof sketch:_

Apply the fundamental theorem of calculus and [[Mathematical Analysis I --- math-131/notes/Differentiability#_proposition _ the product rule|the product rule]] to see that
$$
\int_{a}^b f'(x) g(x) + f(x) g'(x) \, dx = f(b) g(b) - f(a) g(a).
$$
Then use the [[Mathematical Analysis I --- math-131/notes/Properties of the Riemann integral#_proposition _ the Riemann integral is additive|additivity of the Riemann integral]].