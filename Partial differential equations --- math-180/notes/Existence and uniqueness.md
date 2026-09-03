---
tags:
- math-180/2
- pde
---

##### _definition:_ Lipschitz functions, locally Lipschitz functions

A function $f : X \to Y$ of metric spaces is **Lipschitz** if there exists some Lipschitz constant $\lambda > 0$ such that $d(f(x_{1}), f(x_{2})) < \lambda d(x_{1}, x_{2})$.

$f$ is **locally Lipschitz** if there is a neighbourhood $U_{x}$ of each $x \in X$ where $f_{\mid U_{x}}$ is Lipschitz.

---

Note, if $f$ has bounded derivative, then it is Lipschitz.

##### _example:_ some Lipschitz, locally Lipschitz, and not at all Lipschitz functions

$x \mapsto x$ is Lipschitz, $x \mapsto x^{2}$ is not Lipschitz but is locally Lipschitz, [[Fourier analysis --- math-139/notes/The Weierstrass monster function|the Weierstrass monster function]] is not even locally Lipschitz.

---

Suppose $U \subseteq \mathbb{R}^n$ is open, and we have a continuous tangent vector field $v$. Since $\mathscr{T}_{\mathbb{R}^n}$ is trivial, we can think of $v$ as a continuous map $v : U \to \mathbb{R}^n$. Then it is obvious what we mean by a **(locally) Lipschitz continuous vector field**.

##### _theorem:_ existence and uniqueness for first order equations

Let $U \subseteq \mathbb{R}^n$ be open. If $v : U \to \mathbb{R}^n$ is a locally Lipschitz continuous vector field, then for each $x_{0} \in U$ there is a function $u : [0, \varepsilon) \to \mathbb{R}^n$ such that $u(0) = x_{0}$ and $u'(t) = v(x(t))$ for each $t$. Further, $x$ depends continuously on $x_{0}$.

That is, there exists a unique local solution  

###### _proof:_

Choose a sufficiently small $\delta > 0$ (in fact, we will need $\delta / 4 < 1$) and let $\lambda$ be the Lipschitz constant of $v$ in $Y = B(x, \delta / 4)$. Since $v_{\mid Y}$ is Lipschitz, it is bounded.

Let $X$ be the metric space of continuous functions $[0, \delta / 4 \lambda] \to U$ such that $\lVert u(0) - x \rVert \leq \delta / 4$ always and $\lVert u(t) - x \rVert \leq \delta / 2$ with the supremum metric. Let $\Gamma : X \times Y \to X$ be given by
$$
\Gamma(u, x_{0})(t) = x_{0} + \int_{0}^t v(u(s)) \, ds.
$$
Note $\Gamma(u, x_{0})$ really does lie in $X$. It's clear that $\Gamma(u, x_{0})(0) = x$ which is within $\delta / 4$ of $x_{0}$. Further
$$
\begin{align}
\lVert \Gamma(u, x_{0})(t) - x_{0} \rVert  & \left \lVert x_{0} +  \int_{0}^t v(u(s))\, ds - x \right\rVert  \\
  & \leq \lVert x - x_{0} \rVert + \int_{0}^t \lVert v(u(s)) \rVert \, ds  \\
 & \leq \delta / 4 + \lambda t \\
 & \leq \delta / 4 + \lambda \delta / 4 \lambda \\
 & \leq \delta / 2
\end{align}
$$
so $\Gamma(u, x_{0})$ is always within $\delta / 2$ of $x_{0}$.

Now we show each $u \mapsto \Gamma(u, x_{0})$ is a contraction.
$$
\begin{align}
d(\Gamma)(u_{1}, x_{0}), \Gamma(u_{2}, x_{0})) & = \max_{t}  \left\lVert  \int_{0}^t v(u_{1}(s)) \, ds -  \int_{0}^t v(u_{2}(s)) \, ds   \right\rVert \\
 & \leq \max_{t} \int _{0}^t \lVert v(u_{1}(s)) - v(u_{2})(s) \rVert  \, ds \\
 & \leq \max_{t} \int_{0}^t \lambda \lVert u_{1}(s) - u_{2}(s) \rVert \, ds \\
 & \leq \frac{\delta}{4 \lambda} \lambda d(u_{1}, u_{2}) \\
 & = \frac{\delta}{4} d(u_{1}, u_{2}).
\end{align}
$$
But we chose $\delta$ small enough so that $\delta / 4 < 1$.

Thus, for each $x \in B(x_{0}, \delta / 4)$ [[Analysis --- math-131/notes/Cauchy sequences and completeness#_theorem _ contraction mapping principle, or the Banach fixed point theorem|there is a unique fixed point]] of $u \mapsto \Gamma(u, x_{0})$. Call this fixed point $u$. Then $u$ satisfies $u(t) = x_{0} + \int_{0}^t v(u(s)) \, ds$. But that is just a solution of the differential equation — we have $u(0) = x_{0}$ and $u'(t) = v(u(t))$.

---