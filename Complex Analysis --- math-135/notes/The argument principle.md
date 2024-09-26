---
tags:
- math-135/8
- math-135/9
- anal
---

One of the most striking applications of meromorphic functions is the argument principle.

##### _theorem:_ the argument principle

If $f : \Omega \to \mathbb{C}$ is meromorphic on $\Omega$. Let $D$ be a disc with closure $\overline{D}$ in $\Omega$. Then, if $f$ has no poles or zeroes on $\partial D$
$$
\int_{\partial D} \frac{f'(z)}{f(z)} \, dz = Z - P
$$
where $Z$ is the number of zeroes of $f$ and $P$ is the number of poles (counted with multiplicity, inside $D$).

###### _proof sketch:_

Write out derivatives as power series. Then every order $n$ zero at $z_{0}$ gives you a term of $\frac{n}{z - z_{0}}$ and every order $n$ pole at $z_{p}$ gives you a term of $-\frac{n}{z - z_{0}}$.

##### _theorem:_ Rouche's theorem

Suppose $f, g$ are holomorphic functions on some open $\Omega \subset \mathbb{C}$. Suppose $D$ is a disc with $\overline{D} \subset \Omega$ and its interior. If $\lvert f(z) \rvert > \lvert g(z) \rvert$ everywhere on $\partial D$, then $f$ and $f + g$ have the same number of zeroes inside $D$.

Note that for $f, g$ meromorphic it is true that for $f$ and $f + g$, $Z - P$ is the same.

###### _proof sketch:_

Consider $f_{t} : \Omega \to \mathbb{C}$ by $f_{t} = f + t g$ for $t \in [0, 1]$. Then by the argument theorem, the number of zeroes $Z$ of $f_{t}$ in $D$ is given by
$$
Z(t) = \int_{\partial D} \frac{f_{t}'(z)}{f_{t}(z)} \, dz.
$$

But then $Z$ is a continuous function $f : [0, 1] \to \mathbb{Z}$, and thus, must be constant. Thus, $Z(0) = Z(1)$ and $f + g$ and $f$ have the same number of zeroes.

##### _example:_ an application!

Take some polynomial $p(z) = z^n + a_{n - 1} z^{n - 1} + \dots + a_{0}$. Let $f(z) = z^n$, $g(z) = a_{n - 1} z^{n - 1} + \dots + a_{0}$. Since on a large enough circle $\lvert f \rvert > \lvert g \rvert$, $p = f + g$ must have the same number of zeroes as $f$. $f$ has $n$ zeroes, so now so does $p$! This is an alternative proof of the [[Complex Analysis --- math-135/notes/Cauchy integral formula#_theorem _ the fundamental theorem of algebra|fundamental theorem of algebra]].

Another cool, and unexpected application of Rouche's theorem is to the open mapping theorem —

##### _theorem:_ open mapping theorem

If $\Omega \subset \mathbb{C}$ is open and $f : \Omega \to \mathbb{C}$ is holomorphic and non-constant on $\Omega$, then $f^\text{img}(\Omega)$ is open.

###### _proof:_

We want to show that, for any $w_{0} = f(z_{0}) \in f^\text{img}(\Omega)$, there exists a neighbourhood $N_{\varepsilon}(w_{0})$ such that $f$ hits every $w$ in $N_{\varepsilon}(w_{0})$. We will show that for $\varepsilon$ sufficiently small, every $f(z) - w$ has as many zeroes as $f(z) - w_{0}$.

We know that we can choose some $\delta$ such that on the circle $\lvert z - z_{0} \rvert = \delta$ we have $f(z) \neq w_{0}$. Else, there would be a sequence of points $z_{n}$ with $f(z_{n}) = w_{0}$ with limit point $z_{0}$ and this would force $f = w_{0}$ constant everywhere. 

There must be some $\varepsilon$ such that $\lvert f(z) - w_{0} \rvert > \varepsilon$ everywhere on on the boundary of the disc (otherwise $f(z) \to w_{0}$ and since it is continuous, $f(z) = w_{0}$ at some point on the circle). Given this $\varepsilon$, we can now choose $w \in N_{\varepsilon}(w_{0})$. Then $\lvert w - w_{0} \rvert < \varepsilon$. Thus, $g = w_{0} - w$ is a constant holomorphic function with $\lvert g(z) \rvert < \lvert f(z) \rvert$ for $z$ on the circle $\lvert z - z_{0} \rvert = \delta$. 

Then by Rouche's theorem, $f + g = f(z) - w$ has a zero (specifically, has a zero for some $z$ with $\lvert z - z_{0} \rvert < \delta$). Thus, for any $w \in N_{\varepsilon}(w_{0})$, there is some $z$ with $f(z) = w$ — $N_{\varepsilon}(w_{0}) \subset f^\text{img}(\Omega)$.

This reduces the maximum modulus principle to a corollary —

##### _theorem:_ the maximum modulus principle

If $f : \Omega \to \mathbb{C}$ is a non-constant holomorphic function on the region $\Omega$, $\lvert f \rvert$ cannot attain a maximum on $\Omega$.

###### _proof sketch:_

$f^\text{img}(\Omega)$ is open, so at any point, you can wiggle your way a little further from the origin.

##### _corollary:_ compact sets have maximums only on the boundary

If $f : \Omega \to \mathbb{C}$ is holomorphic on the region $\Omega$, and $f$ has a continuous extension to compact $\overline{\Omega}$.

###### _proof:_

Since $\overline{\Omega}$ is compact, $f$ must attain a maximum on $\Omega$. If $f$ is constant, the maximum occurs on the boundary because the maximum occurs everywhere. If $f$ is non-constant, the maximum occurs on the boundary because it can't occur anywhere on $\Omega$.