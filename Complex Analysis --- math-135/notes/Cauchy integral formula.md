---
tags:
- math-135/1
- math-135/4
- anal
---

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
3) $f$ is analytic

###### _proof:_

We really only need to show that $f$ is analytic. To do so, we perform a geometric series trick. Let $D \subset \Omega$ be a disc centred at $z_{0}$ with $\overline{D} \subset \Omega$ as well. We know that
$$
\begin{split}
f(a) = \frac{1}{2 \pi i} \int_{\gamma} \frac{f(z)}{z - a} \, dz.
\end{split}
$$


### Consequences!

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