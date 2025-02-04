---
tags:
- math-135/8
- math-135/9
- math-135/10
- math-135/11
- anal
- complex
---

### Argument principle

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

### Winding number

The notion of winding number allows to rephrase Rouche's theorem in geometric terms.

##### _lemma:_ winding around a simple pole

Let $\gamma$ be a piecewise smooth closed curve that doesn't pass through $z_{0}$. Then $\int_{\gamma} \frac{dz}{z - z_{0}}$ is a multiple of $2 \pi i$.

###### _proof:_

Let $z_{\gamma} : [a, b] \to \mathbb{C}$ be a parametrisation of $\gamma$. Define
$$
*h(t) = \int_{a}^t \frac{z_{\gamma}'(t)}{z_{\gamma}(t) - z_{0}} \, dz.*
$$
Note that $h$ is continuous on $[a, b]$ and is differentiable where $\gamma$ is continuous with derivative $\frac{z_{\gamma}'(t)}{z_{\gamma}(t) - z_{0}}$. Also note that $h(b)$ is the integral we want to evaluate.

Consider $e^{-h(t)} (z_{\gamma}(t) - z_{0})$. It has derivative zero, so it is constant. Thus,
$$
e^{- h(t)}(z_{\gamma}(t) - z_{0}) = e^{- h(a)} (z_{\gamma}(a) - z_{0}) 
$$
and then
$$
e^{h(t)} = \frac{z_{\gamma(t)} - z_{0}}{z_{\gamma}(a) - z_{0}}
$$

But since $z_{\gamma}(b) = z_{\gamma}(a)$, we have $e^{h(b)} = 1$. Thus, $h(b) = n 2 \pi i$ for some integer $n \in \mathbb{Z}$.

##### _definition:_ winding number

The winding number of a curve $\gamma$ with respect to a point $z_{0}$ is
$$
n(\gamma, z_{0}) = \frac{1}{2 \pi i} \int _{\gamma} \frac{dz}{z - z_{0}} 
$$
Sometimes this is called the index of $z_{0}$ with respect to $\gamma$.

Now we can prove the cutest little generalisation of [[Complex Analysis --- math-135/notes/Cauchy integral formula#_theorem _ Cauchy integral formula|Cauchy's integral formula]] — 

##### _corollary:_ Cauchy's integral formula with winding number

If $f$ is holomorphic on a region $\Omega$, $\gamma$ is a closed curve in $\Omega$, and $a$ is a point somewhere in $\Omega$. Then
$$
\frac{1}{2 \pi i} \int \frac{f(z)}{z - a} \, dz = n(\gamma, a) f(a) 
$$

###### _proof sketch:_

Let
$$
F(z) = \frac{f(z) - f(z_{0})}{z - z_{0}}
$$

We can reinterpret the argument principle and Rouche's theorem geometrically using the notion of winding number.

We can also show the open mapping theorem in a new way —

##### _lemma:_ the "$n$-to-one" lemma

If $f$ is holomorphic and non-constant on some region $\Omega \subset \mathbb{C}$. Let $z_{0} \in \Omega$ and let $n$ be the multiplicity of $z_{0}$ as a zero of $g : z \mapsto f(z) - f(z_{0})$. For sufficiently small $\varepsilon > 0$ there exists a $\delta > 0$ such that for every point $w \in N_{\delta}^*(f(z_{0}))$, there exist $n$ distinct points $z_{1}, \dots, z_{n}$ in $B_{\varepsilon}^*(z)$ with $f(z_{j}) = f(z_{0})$ for all $j$.

###### _proof sketch:_

We sort of already showed this in the proof of the open mapping theorem. Note that $g(z_{0})$ is an isolated zero. Thus, there exists a neighbourhood $B_{\varepsilon_{1}}^*(z_{0})$ in which $g$ has no zeroes, and further, we can also choose a neighbourhood $B_{\varepsilon_{2}}^*(z_{0})$ in which $f'$ is non-zero. Choose $\varepsilon < \min{\{ \varepsilon_{1}, \varepsilon_{2} \}}$.

Now consider the image of $\partial B_{\varepsilon}(z_{0})$ (parametrised positively or negatively) under $f$. This wraps around $f(z_{0})$ since $\partial B_{\varepsilon}(z_{0})$ is in $B_{\varepsilon}^*(z_{0})$ and thus cannot hit $f(z_{0})$. Choose $\delta < \lvert f(\partial B_{\varepsilon}(z_{0})) - f(z_{0}) \rvert$. That is, choose $\delta$ less than the distance between the image of the boundary and $f(z_{0})$.

##### _theorem:_ Hurwitz's theorem

Suppose $\{ f_{n} \}_{n}$ is a sequence of holomorphic functions $\Omega \to \mathbb{C}$ with $f_{n} \to f \neq 0$ uniformly. Then $f(z_{0}) = 0$ if and only if there is a sequence of points $\{ z_{n} \}_{n}$ converging to $z_{0}$ such that $f_{n}(z_{n}) = 0$.

###### _proof sketch:_

We will first show that for any simple closed curve there is some $N$ for which $n > N$ gives us that $f_{n}$ and $f$ have the same number of zeroes in the region bounded by the curve. Either use the argument principle and argue that the integrals converge, or use the argument principle and Rouche's theorem — $\lvert f - f_{n} \rvert < m < \lvert f \rvert$ if $f$ takes minimum $m$ on the curve.

Just consider smaller and smaller curves around for larger and larger $n$ to get the convergent sequence (pick points inside the region bounded by the curve).