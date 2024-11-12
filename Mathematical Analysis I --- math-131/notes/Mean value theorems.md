---
tags:
- math-131/20
- math-131/21
- anal
---

If the [[Mathematical Analysis I --- math-131/notes/Differentiability#_definition _ differentiability, the derivative|derivative]] gives you the instantaneous rate of change of a function, then what is its relationship to the average rate of change of the function? The mean value theorem gives us the answer.

##### _theorem:_ the generalised mean value theorem

If $f$ and $g$ are continuous on $[a, b]$ and differentiable in $(a, b)$, then there exists $x \in (a, b)$ such that 
$$
(f(b) - f(a)) g'(x) = (g(b) - g(a)) f'(x).
$$

###### _proof:_

Consider $h : [a, b] \to \mathbb{R}$ by
$$
h(x) = (f(b) - f(a)) g(x) - (g(b) - g(a)) f(x).
$$
Notice that
$$
h(a) = f(b) g(a) - f(a) g(b) = h(b)
$$
and $h$ is [[Mathematical Analysis I --- math-131/notes/Continuity#_proposition _ continuity of operations on the complex numbers|continuous]] on $[a, b]$ and [[Mathematical Analysis I --- math-131/notes/Differentiability#Differentiability rules|differentiable]] on $(a, b)$ by the corresponding sum and product rules.

Since $[a, b]$ is compact, $h$ has a [[Mathematical Analysis I --- math-131/notes/Continuity#_corollary _ the image of a compact set has a maximum and minimum|maximum and a minimum]] in the $[a, b]$. If $h$ achieves its maximum and minimum on the boundary of $[a, b]$, then $h$ must be constant on $(a, b)$ with $h' = 0$ everywhere. If $h$ has a maximum or minimum inside $(a, b)$ then $h'$ [[Mathematical Analysis I --- math-131/notes/Extrema#_theorem _ the derivative vanishes at extrema|must vanish there]].

Note that this gives us the usual mean value theorem as a corollary, taking $g$ to be the identity function —

##### _theorem:_ mean value theorem

If $f$ is continuous on $[a, b]$ and differentiable in $(a, b)$, then there exists $x \in (a, b)$ such that
$$
f'(x) = \frac{f(b) - f(a)}{b - a}.
$$

### Incredible corollaries

The mean value theorem has some incredible consequences. For instance, we can also use the mean value theorem to get an analogue of [[Mathematical Analysis I --- math-131/notes/Continuity#_corollary _ intermediate value theorem|intermediate value theorem]] for derivatives, even though the derivative of a function need not be continuous.

##### _corollary:_ intermediate value theorem for derivative

If $f$ is differentiable on some $[a, b]$ (on some open interval containing it), then, for any $\lambda \in (f'(a), f'(b))$, (assuming without loss of generality that $f'(a) < f'(b)$) then there exists $x$ such that $f'(x) = \lambda$.

###### _proof:_

Consider $g : [a, b] \to \mathbb{R}$ by $g(t) = f(t) - \lambda t$. Then $g'(t) = f'(t) - \lambda t$. Since $[a, b]$ is compact, $g'(a) < 0$, and $g'(b) > 0$, $g$ does not attain its maximum on the boundary $[a, b]$, but instead at a point $x$ in its interior. There $g'(x) = 0$ and thus, $f'(t) = \lambda$.

Note that this means that discontinuous functions must have fairly complicated discontinuities — they cannot just be jump discontinuities since that would break the intermediate value condition.

##### _theorem:_ L'Hôpital's rule

For any differentiable $f, g : (a, b) \to \mathbb{R}$, if
$$
\lim_{ x \to a^+ } \frac{f'(x)}{g'(x)} = A
$$
and
$$
\lim_{ x \to a^+ } f(x) = \lim_{ x \to a^+ } g(x) = 0
$$
or
$$
\lim_{ x \to a^+ } f(x) = \lim_{ x \to a^+ } g(x) = \infty
$$
then
$$
\lim_{ x \to a^+ } \frac{f(x)}{g(x)} = A.
$$

###### _proof:_

For any $\varepsilon > 0$, consider $\delta > 0$ such that for all $t \in (a, a + \delta)$, then
$$
\left\lvert  \frac{f'(t)}{g'(t)} - A  \right\rvert < \frac{\varepsilon}{2}.
$$

Suppose the functions both go to zero. Thus, we can choose $y$ sufficiently close to $a$ so that
$$
\left\lvert  \frac{f(x) - f(y)}{g(x) - g(y)} - \frac{f(x)}{g(x)}  \right\rvert < \frac{\varepsilon}{2}.
$$
But then, by the mean value theorem, there exists $t \in (y, x)$ such that $f'(t) / g'(t)$ is the difference quotient —
$$
\left\lvert  \frac{f'(t)}{g'(t)} - \frac{f(x)}{g(x)}  \right\rvert < \frac{\varepsilon}{2}.
$$
Thus, applying the triangle inequality,
$$
\left\lvert  \frac{f(x)}{g(x)} - A  \right\rvert \le \left\lvert  \frac{f'(t)}{g'(t)} - \frac{f(x)}{g(x)}  \right\rvert + \left\lvert  \frac{f'(t)}{g'(t)} - A  \right\rvert < \varepsilon.
$$

Suppose now that the functions blow up near $a$. Choose some $y \in (a, a + \delta)$, and $x \in (a, y)$ so that some $t \in (a, a + \delta)$ gives
$$
\frac{f(x) - f(y)}{g(x) - g(y)} = \frac{f'(t)}{g'(t)} = r \in (A - \varepsilon / 2, A + \varepsilon / 2).
$$

Thus,
$$
\frac{f(x)}{g(x)} = r \frac{(g(x) - g(y))}{g(x)} + \frac{f(y)}{g(x)} = r - r \frac{g(y)}{g(x)} + \frac{f(y)}{g(x)}
$$
Since $g(x) \to \infty$, we can choose $\delta'$ so that the remaining terms are smaller than $\varepsilon /2$. Thus, for $x$ within $\min \{ \delta, \delta' \}$ of $a$,
$$
\begin{split}
\left\lvert  \frac{f(x)}{g(x)} - A  \right\rvert &  \le \lvert r - A \rvert + \left\lvert  - r \frac{g(y)}{g(x)} + \frac{f(y)}{f(x)}  \right\rvert  \\
 & < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} \\
 & = \varepsilon
\end{split}
$$