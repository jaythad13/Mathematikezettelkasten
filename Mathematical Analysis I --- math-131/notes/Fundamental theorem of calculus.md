---
tags:
- math-131/25
- anal
---

The fundamental theorem of calculus is the first (and most "fundamental") in a series of theorems that say that integrating something over a boundary is the same as integrating its derivative over the inside.

##### _theorem:_ the fundamental theorem of calculus

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