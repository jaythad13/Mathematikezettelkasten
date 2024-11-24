---
tags:
- math-131/20
- math-131/21
- math-131/22
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

##### _corollary:_ the intermediate value property of derivatives

If $f$ is differentiable on some $[a, b]$ (on some open interval containing it), then, for any $\lambda \in (f'(a), f'(b))$, (assuming without loss of generality that $f'(a) < f'(b)$) then there exists $x$ such that $f'(x) = \lambda$.

###### _proof:_

Consider $g : [a, b] \to \mathbb{R}$ by $g(t) = f(t) - \lambda t$. Then $g'(t) = f'(t) - \lambda t$. Since $[a, b]$ is compact, $g'(a) < 0$, and $g'(b) > 0$, $g$ does not attain its maximum on the boundary $[a, b]$, but instead at a point $x$ in its interior. There $g'(x) = 0$ and thus, $f'(t) = \lambda$.

Note that this means that discontinuous derivatives must have fairly complicated discontinuities — they cannot just be jump discontinuities since that would break the intermediate value condition.

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

### Taylor's theorem

Taylor's theorem allows us to estimate a function using its [[Mathematical Analysis I --- math-131/notes/Differentiability#_definition _ higher-order derivatives|higher order derivatives]] — it gives a mean value style formula in terms of the $n$th power of the difference between points and the $n$th derivative of a function. If we have reasonable bounds on the size of the $n$th derivative of the function, this allows us to approximate the function by a polynomial.

##### _theorem:_ Taylor's theorem

Suppose $f : [a, b] \to \mathbb{R}$ is $n$ times differentiable with $f^{(n)}$ continuous on $[a, b]$. For any two $\alpha, \beta \in [a, b]$, there is some $x_{0}$ between $\alpha$ and $\beta$ such that
$$
f(\beta) - p(\beta) = \frac{f^{(n)}(x_{0})}{n!} (\beta - \alpha)^n
$$
for the polynomial $p$ with
$$
p(x) = \sum_{j = 0}^{n - 1} \frac{f^{j}(\alpha)}{i!} (x - \alpha)^j
$$

###### _proof:_

Define the real $M$ so that $f(\beta) - p(\beta) = M (\beta - \alpha)^n$. We want to show that there is some $x_{0}$ with $f^{(n)}(x_{0}) / n! = M$. Consider
$$
g(x) = f(x) - p(x) + M (x - \alpha)^n.
$$

This has $n$th derivative
$$
g^{(n)}(x) = f^{(n)}(x) - n! M
$$
so if we have $g^{(n)}(x) = 0$ at some point between $\alpha$ and $\beta$ we are done.

Notice that since $f^{(j)}(\alpha) = p^{(j)}(\alpha)$ for all positive integers $j < n$ (by our construction), we have $g^{(j)}(\alpha) = 0$ for all $j < n$. Since $g(\beta) = 0$ we can apply the mean value theorem to find some $x_{1}$ between $\alpha$ and $\beta$ where 
$$
g'(x_{1}) = \frac{g(\beta) - g(\alpha)}{\beta - \alpha} = 0
$$
and similarly, using the mean value theorem on $x_{j}$ we can get $x_{j + 1}$ where
$$
g^{j + 1}(x_{j + 1}) = \frac{g^{j}(x_{j}) - g^{j}(\alpha)}{x_{j} - \alpha} = 0
$$
for all $j < n$.

Thus, there is some $x_{0} = x_{n}$ in $[a, b]$ where $g^{(n)}(x_{0}) = 0$ and thus,
$$
\frac{f^{(n)}(x_{0})}{n!} = M.
$$