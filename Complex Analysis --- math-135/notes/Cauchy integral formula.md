---
tags:
- math-135/1
- math-135/4
- math-135/5
- math-135/6
- math-135/7
- anal
---

### The formula

##### _theorem:_ Cauchy integral formula

If $f : \Omega \to \mathbb{C}$ is a differentiable function from a region $\Omega$. Then for any simple closed curve $\gamma$ in $\Omega$ with interior $R$, and any $a \in R$ we have
$$
f(a) = \frac{1}{2 \pi i} \int_{\gamma} \frac{f(z)}{z - a} \, dz.
$$

###### _proof sketch:_

Consider the keyhole contour $\Gamma_{\delta, \varepsilon}$ with (anti-clockwise) $\gamma$ outside, a (clockwise) circle $\overline{\gamma_{\varepsilon}}$ of radius $\varepsilon$ around $a$, and a narrow path of width $\delta$ between them. Then since $\frac{f(z)}{z - a}$ is holomorphic everywhere on the region bounded by $\Gamma_{\delta, \varepsilon}$, we have
$$
\int_{\Gamma_{\delta, \varepsilon}} \frac{f(z)}{z - a}  \, dz = 0.
$$
As $\delta, \varepsilon \to 0$,
$$
\int_{\Gamma_{\delta, \varepsilon}} \frac{f(z)}{z - a} \, dz = \int_{\gamma} \frac{f(z)}{z - a}  \, dz + \int_{\overline{\gamma_{\varepsilon}}} \frac{f(z)}{z - a}  \, dz   
$$
and thus,
$$
\int_{\gamma} \frac{f(z)}{z - a}  \, dz = - \int_{\overline{\gamma_{\varepsilon}}} \frac{f(z)}{z - a}  \, dz = \int_{\gamma_{\varepsilon}} \frac{f(z)}{z - a}  \, dz.
$$

Now we just need to show that
$$
\int_{\gamma_{\varepsilon}} \frac{f(z)}{z - a}  \, dz = 2 \pi i f(a)
$$
We can add a judicious zero to get
$$
\int_{\gamma_{\varepsilon}} \frac{f(z)}{z - a}  \, dz = \int_{\gamma_{\varepsilon}} \frac{f(z) - f(a)}{z - a} + \frac{f(a)}{z - a} \, dz.
$$

For small enough $\varepsilon$, the first term of the integrand approaches $f'(z)$. Thus, we can bound the quotient. Then the $ML$ bound gives us that the first part of the integral as $L \to 0$. It's a simple verification to show that the integral of $\frac{1}{z - a}$ around a disc centred at $a$ is $2 \pi i$. Thus, we have the desired result.

##### _corollary:_ the derivative form (holomorphic functions are smooth and analytic)

Suppose $\Omega$ is an open set in $\mathbb{C}$ with $f : \Omega \to \mathbb{C}$ holomorphic. Then
1) $f$ is smooth (infinitely differentiable)
2) the $n$th derivative of $f$ is given by $f^{(n)}(a) = \frac{n!}{2 \pi i} \int \frac{f(z - a)}{(z - a)^{n + 1}} \, dz$
3) $f$ is analytic (with a power series expansion about $z_{0}$ on every disc $D_{r}(z_{0})$ with $\overline{D_{r}(z_{0})} \subset \Omega$)

###### _proof:_

We really only need to show that $f$ is analytic with the given coefficients. To do so, we perform a geometric series trick. Let $D \subset \Omega$ be a disc centred at $z_{0}$ with $\overline{D} \subset \Omega$ as well. We know that
$$
\begin{split}
f(a) & = \frac{1}{2 \pi i} \int_{\gamma} \frac{f(z)}{z - a} \, dz \\
 & = \frac{1}{2 \pi i} \int \frac{f(z)}{z - z_{0} - (a - z_{0})} \, dz \\
 & = \frac{1}{2 \pi i} \int \frac{f(z)}{z - z_{0}}\frac{1}{1 - \frac{a - z_{0}}{z - z_{0}}} \, dz  \\
 & = \frac{1}{2 \pi i} \int \sum_{n = 0}^\infty \left( \frac{a - z_{0}}{z - z_{0}} \right)^n \frac{f(z)}{z - z_{0}}  \, dz 
\end{split}
$$

Since the sum converges uniformly (for varying $z$), we can interchange the order of integration and summation to get a power series
$$
\begin{split}
f(a) & = \sum_{n = 0}^\infty \left( \frac{1}{2 \pi i} \int \frac{f(z)}{(z - z_{0})^{n + 1}} \, dz  \right) (a - z_{0})^n
\end{split}
$$
with the desired coefficients.

Note that you could prove this directly by considering the difference between the quotients and the derivative. This proof showed us that if we define
$$
g(a) = \frac{1}{2 \pi i} \int \frac{f(z)}{z - a} \, dz 
$$
for some continuous function $f$, then $f$ is holomorphic. We will need this to prove [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#_theorem _ Riemann's theorem on removable singularities|Riemann's theorem on removable singularities]].

### Consequence

##### _proposition:_ Cauchy inequalities

If $f$ is holomorphic in an open set that contains the closure of a disc $D$ centred at $z_{0}$ and of radius $R$, then
$$
\lvert f^{(n)}(z_{0}) \rvert \le \frac{n! \sup_{z \in C} \lvert f(z) \rvert }{R^n}
$$

###### _proof sketch:_

Apply the $ML$ bound to the Cauchy derivative formula.

##### _theorem:_ Liouville's theorem

If $f : \mathbb{C} \to \mathbb{C}$ is entire and bounded, it is constant.

###### _proof sketch:_

Suppose $\lvert f(z) \rvert < M$ everywhere. Then the Cauchy inequalities apply to give $\lvert f'(z) \rvert < M /R$ for any radius $R$. Consider bigger and bigger radiuses to get $f'(z) = 0$, and thus, that $f$ is constant.

The fundamental theorem of algebra is now just a simple application of Liouville's theorem!

##### _theorem:_ the fundamental theorem of algebra

Any non-constant polynomial $p : \mathbb{C} \to \mathbb{C}$ has a root.

###### _proof sketch:_

Suppose $p$ has no roots. We will show that $1 / p$ is holomorphic and bounded.

Note that
$$
\frac{p(z)}{z^n} = a_{n} + \left( \frac{a_{n - 1}}{z} + \dots + \frac{a_{0}}{z^n} \right).
$$
Thus, $p(z)$ gets arbitrarily close to $a_{n} z^n$ as we increase $\lvert z \rvert$. Then, there is some $R$ such that for all $z$ with $\lvert z \rvert > R$, we have $\lvert p(z) \rvert \ge \lvert a_{n} z^n \rvert/2$. That is, $p$ is bounded from below outside the disc. Since $p$ has no zeroes and is continuous on the compact set that is the closure of the disc we also have $0 < b < p$. That is, $p$ is bounded from below inside the disc as well. That is, $p$ is bounded from below everywhere, and thus, $1/p$ is bounded from above everywhere.

$1/p$ is clearly holomorphic (just use the [[Complex Analysis --- math-135/notes/Holomorphic functions|quotient rule]]). Thus, by applying Liouville's theorem, we get that $1/p$ is constant, and thus, $p$ is constant.

##### _theorem:_ identity theorem

Suppose $f$ is holomorphic on a region $\Omega$. If the set of zeroes of $f$ on $\Omega$, $Z = \{ z \in \Omega \mid f(z) = 0 \}$. has a limit point in $\Omega$, then $f$ is identically $0$ on $\Omega$.

###### _proof:_

Let $z_{0} \in \Omega$ be the limit point of $Z$. We know that we have a power series expansion about $z_{0}$ in some $D_{r}(z_{0})$ with $\overline{D_{r}(z_{0})} \subset \Omega$. Suppose, by way of contradiction, this power series expansion were nonzero.

Then we can pick the first nonzero coefficient $a_{m}$ and write $f(z) = a_{m} (z - z_{0})^m(1 + g(z))$. On a sequence in $Z$, $w_{n} \to z_{0}$ and choose $w_{n} \neq 0$. Then we have $f(w_{n}) = a_{m}(w_{n} - z_{0})^n(1 + g(z))$. $f(w_{n}) = 0$, 

Now we have that $f = 0$ on a disc around $z_{0}$, we can move the disc all the way to any other point $z$. Given the curve $\gamma$ that connects $z_{0}$ to $z$, we know that there is a [[Complex Analysis --- math-135/notes/(Metric) topology review#_proposition _ distance lemma|finite distance]] $\delta$ between $\gamma$ and $\partial \Omega$. Pick points $z_{0}, z_{1}, \dots, z$ along $\gamma$ such that no consecutive points are more than $\delta / 2$ apart. Then we keep getting $z_{n}$ as limit points and we can move along discs of radius $\delta / 2$ all the way to $z$.

##### _corollary:_ unique analytic continuation

If $\{ z \in \Omega \mid f(z) = g(z) \}$ has a limit point, then $f = g$ on $\Omega$.

##### _theorem:_ Morera's theorem

Let $D$ be an open disk. Suppose $f : D \to \mathbb{C}$ is continuous. If, for all triangles $\Delta \subset D$, $\int_{\partial \Delta} f(z)  \, dz = 0$, then $f$ is holomorphic.

###### _proof sketch:_

In the same way as the proof of [[Complex Analysis --- math-135/notes/Cauchy-Goursat theorem#_corollary _ Cauchy's theorem|Cauchy's theorem]], this gives us an antiderivative $F$ with $F' = f$. But then $F$ is indefinitely differentiable, and thus, it's derivative $f$ must be holomorphic.

Morera's theorem allows us to create holomorphic functions out of holomorphic functions by processes that preserve integrals.

##### _proposition:_ uniform convergence preserves holomorphicity

Suppose $f_{n} : \Omega \to \mathbb{C}$ is a sequence of holomorphic functions that converges to $f$ uniformly on every compact subset of $\Omega$. Further $f'_{n}$ converges uniformly to $f'$ on every compact subset of $\Omega$.

###### _proof:_

Pick an open disc $D$. By uniform convergence, on any triangle $\Delta$ in compact $\overline{D}$, we have
$$
\begin{split}
\int_{\partial \Delta} f(z) \, dz & = \int_{\partial \Delta} \lim_{ n \to \infty } f_{n}(z) \, dz \\
 & = \lim_{ n \to \infty } \int_{\partial \Delta} f_{n}(z) \, dz  \\
 & = 0.
\end{split}
$$
Then, by Morera's theorem, $f$ is holomorphic on $D$. Then we can just cover $\Omega$ with discs $D$.

Consider compact subsets $\Omega_{\delta}$ with a distance $\delta$ from the boundary of $\Omega$. Then bound $(f_{n} - f)'$ uniformly using [[#_proposition _ Cauchy inequalities|Cauchy inequalities]].

##### _proposition:_ holomorphic functions defined by integrals

For any continuous $F : \Omega \times [0, 1] \to \mathbb{C}$ with holomorphic sections $F_{s_{0}} : z \mapsto F(z, s_{0})$, the "average" of these sections, $f$, defined by
$$
f(z) = \int_{0}^1 F(z, s)  \, ds 
$$
is holomorphic.

###### _proof:_

By Morera's theorem it is sufficient to show that $\int_{\partial \Delta} f(z) \, dz$ for all triangles $\Delta$ in compact disks $\overline{D}$ in $\Omega$. 

Note that if we have Fubini's theorem, we can just exchange the order of integration as follows
$$
\begin{split}
\int_{\partial \Delta} f(z) \, dz & = \int_{\partial \Delta} \int_{0}^1 F(z, s) \, ds   \, dz \\
 & = \int_{0}^1 \int_{\partial \Delta} F(z, s) \, dz   \, ds \\
 & = 0
\end{split} 
$$
since [[Complex Analysis --- math-135/notes/Cauchy-Goursat theorem#Goursat's theorem|Goursat's theorem]] gives us that the integral of a holomorphic function $F(z, s_{0})$ over a closed triangle is $0$.

Since we don't we will show that the Riemann sums
$$
f_{n} = \sum_{k = 1}^n \frac{F(z, k/n)}{n}
$$
uniformly converge to $f$. Thus, the integral of $f$ is just the limit of the integrals of these $f_{n}$. Since each $f_{n}$ is holomorphic, each of their integrals is $0$, and thus, the limit of the integrals is $0$.

To see that they converge uniformly, note that $F$ is continuous on $\Omega$, and thus uniformly continuous on each disk $\overline{D}$. Consider
$$
\begin{split}
\lvert f_{n}(z) - f(z) \rvert & = \left\lvert  \sum_{k = 1}^n \frac{F(z, k/n)}{n} - \int_{0}^1 F(z, s) \, ds   \right\rvert \\
& = \left\lvert  \sum_{k = 1}^n \int_{ (k - 1) / n}^{k / n} F(z, k/n) - F(z, s)  \, ds   \right\rvert.
\end{split}
$$
Note that on each interval $\left[ \frac{k - 1}{ n}, \frac{k}{n} \right]$, $s$ is within $1/n$ of $\frac{k}{n}$, and thus, for sufficiently large $n$, we can get $\lvert F(z, k / n) - F(z, s) \rvert < \varepsilon$ for all $s$ and all $k$ (by the uniform continuity of $F$ on $\overline{D}$). Thus,
$$
\lvert f_{n}(z) - f(z) \rvert \le \sum_{k = 1}^n \frac{\varepsilon}{n} = \varepsilon 
$$
Thus, the integral of $f$ over $\partial \Delta$ for any triangle $\Delta$ is the limit of the integral of $f_{n}$, and that is just $0$. By Morera's

##### _theorem:_ Runge's theorem

Any function $f$ holomorphic in a neighbourhood of a compact set $K$ can be approximated uniformly on $K$ by rational functions whose only singularities are in $K^c$. If $K^c$ is connected, $f$ can be approximated uniformly on $K$ by polynomials.

###### _proof sketch:_

Get $f(a)$ at each $a \in K$ by using the Cauchy integral formula on a lattice with squares small enough that you can cover $K$ with squares that do not intersect $\Omega^c$. 

Approximate the integrands using the same Riemann sum.

For $z_{1}$ outside a disc of radius $r$ containing $K$, and $z \in K$ approximate $1/(z - z_{1})$ uniformly by polynomials by using a geometric series trick. Then use connectedness the same way we did to prove the identity theorem to approximate $1/(z - z_{0})$ uniformly by $1 / (z - z_{1})$ for any $z_{0} \not\in K$.