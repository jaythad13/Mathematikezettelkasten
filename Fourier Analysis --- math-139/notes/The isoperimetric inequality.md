---
tags:
- anal
- fourier
- math-139/12
---

A natural question is what curve (of a given length) encloses the largest area? We can answer this with the Fourier analysis we've developed so far. But first, what is a curve?

### Curves and areas

Recall the definition of a [[Complex Analysis --- math-135/notes/Complex integration#_definition _ (oriented) curve, curve parametrisation|curve]] —

##### _definition:_ (simple, closed) curve, parametrisation

A curve $\Gamma$ is the image of a continuously differentiable function $\mathbf{x}_{\Gamma} : [a, b] \to \mathbb{R}^{2}$ such that $\mathbf{x}_{\Gamma}' \neq 0$. We call $\mathbf{x}_{\Gamma}$ its parametrisation (it is not unique).

We say $\Gamma$ is simple if it doesn't intersect itself and closed if $\mathbf{x}_{\Gamma}(a) = \mathbf{x}_{\Gamma}(b)$.

Note that we can extend the parametrisation of a simple closed curve to a $(b - a)$-periodic function on $\mathbb{R}$.

We can change parametrisations using bijective maps.

##### _definition:_ reparametrisation

If $s : [c, d] \to [a, b]$

Its [[Complex Analysis --- math-135/notes/Complex integration#_definition _ length|length]] is defined in terms of a certain parametrisation but is independent of the choice of parametrisation.

##### _definition:_ length

The length of a curve $\Gamma$ with parametrisation $\mathbf{x}_{\Gamma}$

We can use Green's theorem to calculate the area of a region enclosed by $\Gamma$.

The arc length parametrisation is one such that $\lVert \mathbf{x}_{\Gamma}' \rVert = 1$

##### _definition:_ area

If $\Gamma$ is a simple closed curve parametrised by $\mathbf{x}_{\Gamma} = (x, y)$, the area enclosed by $\Gamma$ is
$$
\mathfrak{A}(\Gamma) = \frac{1}{2} \left\lvert  \int_{\Gamma} x \, dy - y \, dx   \right\rvert = \int_{a}^b x(s) y'(s) - y(s) x'(s) \, dx 
$$

### The isoperimetric inequality

Now we can state the isoperimetric inequality!

##### _theorem:_ the isoperimetric inequality

Suppose $\Gamma \subseteq \mathbb{R}^{2}$ is a simple closed curve of length $\ell$ and enclosing area $\mathfrak A$. Then
$$
\mathfrak A \le \frac{\ell^{2}}{4 \pi}.
$$

###### _proof:_

Our main tool here is [[Fourier Analysis --- math-139/notes/Square convergence of Fourier series#_corollary _ Parseval's identity|Parseval's identity]].

We will assume without loss of generality $\Gamma$ has length $2 \pi$ with $\mathbf{x}_{\Gamma} = (x, y) : [0, 2 \pi] \to \mathbb{R}^{2}$ an arclength parametrisation. Thus, we want to show $\mathfrak A \le \pi$.

Since $\mathbf{x}_{\Gamma}$ is an arclength parametrisation,
$$
\lVert x' \rVert_{L^{2}} + \lVert y' \rVert _{L^{2}} = \frac{1}{2 \pi} \int_{0}^{2 \pi} (x'(s))^{2} + (y'(s))^{2}  \, ds = \frac{1}{2 \pi} \int_{0}^{2 \pi} \lVert \mathbf{x}_{\Gamma}(s) \rVert  \, ds = \ell = 1.
$$
Then by Parseval's identity, the $\ell^{2}$ (this is not $\ell$ as in length) norms of the Fourier coefficients of $x'$ and $y'$ also satisfy the same identity. It's an exercise on the homework to show $\hat{f'}(n) = -in \hat{f}(n)$. Thus,
$$
\sum_{n = -\infty}^\infty n^{2} (\lvert a_{n} \rvert ^{2} + \lvert b_{n} \rvert ^{2}) = 1
$$
for $\hat{x}(n) = a_{n}$ and $\hat{y}(n) = b_{n}$

We can play a similar trick with the area, viewing it as an [[Fourier Analysis --- math-139/notes/Square convergence of Fourier series#_proposition, definition _ the $L 2$ inner product, $ mathcal{R}$|inner product]]
$$
\left< x, y' \right>_{L^{2}} - \left< y, x' \right>_{L^{2}} = \frac{1}{2 \pi} \int_{0}^{2 \pi} x(s) y'(s) + y(s) x'(s) \, dx = \mathfrak A
$$
and obtaining the same identity for the $\ell^{2}$ [[Fourier Analysis --- math-139/notes/Square convergence of Fourier series#_definition _ the inner product space of $ ell {2}$ sequences|inner products]]. Thus,
$$
\begin{align}
\mathfrak{A} & = \pi \left\lvert  \sum_{n = -\infty}^\infty a_{n} (-i n \overline{b}_{n}) - \sum_{n = - \infty}^\infty b_{n} (-in \overline{a}_{n})  \right\rvert  \\
 & \leq \pi \sum_{n = -\infty}^\infty \lvert n \rvert \lvert a_{n} \overline{b}_{n} - b_{n} \overline{a}_{n} \rvert  \\
 & \le \pi \sum_{n = -\infty}^\infty \lvert n \rvert (2 \lvert a_{n} \rvert  \lvert b_{n} \rvert ) \\
 & \le \pi \sum_{n = -\infty}^\infty \lvert n \rvert (\lvert a_{n} \rvert ^{2} + \lvert b_{n} \rvert ^{2}) \\
 & \le \pi \sum_{n = -\infty}^\infty \lvert n \rvert ^{2} (\lvert a_{n} \rvert ^{2} + \lvert b_{n} \rvert^{2}) \\
 & = \pi
\end{align}
$$
where the second and third inequalities follow from the triangle inequality and the fact that $(a - b)^{2} \ge 0$. Thus, we've shown the inequality!

For equality to hold, all of the inequalities must be equalities. Working backwards, since $\lvert n \rvert^{2} \ge \lvert n \rvert$ for all $n$ with equality exactly when $\lvert n \rvert \leq 1$. Thus, we must have $a_{n} = b_{n} = 0$ when $\lvert n \rvert > 1$. 

Further, from [[Fourier Analysis --- math-139/attachments/homework/hw 2/hw 2.pdf|from the homework]] we know that real $x, y$ must have $a_{1} = \overline{a}_{-1}$ and $b_{1} = \overline{b}_{-1}$. By our first formula obtained from Parseval's identity on the length of $\Gamma$, $2 (\lvert a_{1} \rvert^{2} + \lvert b_{1} \rvert^{2}) = 1$ giving $\lvert a_{1} \rvert^{2} + \lvert b_{1} \rvert^{2} = 1 / 2$. Since we have the equality $(\lvert a_{n} \rvert - \lvert b_{n} \rvert)^{2} = 0$ for each $n$, we have $\lvert a_{1} \rvert \lvert b_{1} \rvert = 1 / 4$. Finally, we have $\lvert a_{1} \rvert = \lvert b_{1} \rvert = 1 / 2$. This means we can write $a_{1} = e^{i \alpha} / 2$ and $b_{1} = e^{i \beta} / 2$.

Going back one more equality, we get $1 = 2 \lvert a_{1} \overline{b}_{1} - \overline{a}_{1} b_{1} \rvert$ which implies $\lvert \sin (\alpha - \beta) \rvert = 1$ and thus, $\alpha - \beta = \pi (2k + 1) /2$ for some integer $k \in \mathbb{Z}$. We're left with
$$
x(s) = a_{0} + \cos(\alpha + s) \quad y(s) = b_{0} \pm \sin(\alpha + s)
$$
which is a circle.


