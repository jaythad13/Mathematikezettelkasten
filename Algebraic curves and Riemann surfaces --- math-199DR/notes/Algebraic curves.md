---
tags:
- math-199DR/20
- cx-geo
- alg-geo
---

Let $X$ be a compact Riemann surface.

Algebraic curves have the nicest properties of any Riemann surface — they are the compactifications of zero sets of polynomials. 

Typically, we would define algebraic curves to be these compactifications of zero sets, but here we will just define them as having the property we want — enough meromorphic functions.

##### _definition:_ separating points, separating tangents

A subset of $\mathcal{M}_{X}(X)$ is said to separate points if for every pair of points $p, q$ it contains a meromorphic function $f$ with $f(p) \neq f(q)$.

It is said to separate tangents if for each point $p \in X$ there is a meromorphic function with ([[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ meromorphic functions are maps to the Riemann sphere|associated map to the Riemann sphere having]]) [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ multiplicity|multiplicity]] $1$ at $p$.

It's obvious what separating points means, but separating tangents is more subtle. Separating tangents can be thought of as either having a map to the Riemann sphere that induces an isomorphism of tangent/cotangent spaces, or (when $f$ isn't a pole) having a [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological properties of holomorphisms#_example _ charts have multiplicity $1$|chart]] at $p$ that extends to a meromorphic function on all of $X$.

It's easy to see that an "algebraically defined curve" $X$ has $\mathcal{M}_{X}(X)$ separating points and tangents — for any pair of points $p, q \in X$ there is an open neighbourhood containing both of them where $X$ looks like the zero set of some $r \in \mathbb{C}[x_{1}, \dots, x_{n}]$ (to be exact, this is true for quasi-projective schemes of finite type over some field). If $p = (p_{1}, \dots, p_{n})$ and $q = (q_{1}, \dots, q_{n})$ differ in the first coordinate choose $f(x_{1}, \dots, x_{n}) = x_{1} - p_{1}$. This separates $p$ and $q$ and has multiplicity $1$ at $p$.

It's harder to show that if a Riemann surface has $\mathcal{M}_{X}(X)$ separating points and tangents that it is then defined by a polynomial, but it can be done. From $z$, a meromorphic function of [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ degree of a map|degree]] $n$, and another meromorphic function $f$ on $X$ we can create functions in $z$ that look like symmetric functions of $f$ applied to the $n$ pre-images of each (non-[[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ ramification point, branch point|branched]] points) of $\mathbb{C}_{\infty}$. That is,
$$
\begin{align}
r_{k}(z) = (-1)^n \sum_{n_{1} < \dots < n_{k}}^n f(p_{n_{1}}) \cdots f(p_{n_{k}})
\end{align}
$$
Then it turns out that
$$
f^n + r_{1}(z) f^{n - 1} + \dots + r_{n - 1}(z) f + r_{n}(z) = 0
$$
so mapping $p \mapsto (z, f)$ gives $X$ as an algebraic curve.

Thus, we define an algebraic curve by this "having enough meromorphic functions" property.

##### _definition:_ algebraic curve

A compact Riemann surface $X$ is an algebraic curve if $\mathcal{M}_{X}(X)$ separates points and tangents of $X$.

It turns out that all compact Riemann surfaces separate points and tangents, and are thus algebraic curves. One can either show this generally for compact complex manifolds using cohomology theory from complex analytic geometry or just for Riemann surfaces by showing that there exists a non-constant meromorphic function on every compact Riemann surface and then using the Narasimhan proof to get algebraicity.

### Laurent series approximation

Let $X$ be an algebraic curve. It turns out that this condition is sufficient to create [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ meromorphic|meromorphic functions]] with desired behaviour at finitely many points on $X$. Ultimately our goal is to create a meromorphic function with specified behaviour at finitely many points and possibly arbitrary behaviour everywhere else. 

The behaviour we want to specify is the tail of the Laurent series of the function.

##### _definition:_ Laurent tail

A Laurent polynomial $r(z) = \sum_{n = m}^M a_{n} z^n$ ($m \leq M$ integers, possibly negative) is the Laurent tail of a Laurent series $f$ if $f(z) - r(z)$ has all terms of degree (strictly) greater than $M$.

This aligns exactly with our intuition for the "left" "tail" of a series.

Our result follows from a series of lemmas. First we get a meromorphic function of arbitrary order at a point —

##### _lemma:_ functions with specified order at a point

Given a point $p \in X$ and an integer $m$, there is a meromorphic function $f$ on $X$ with $\operatorname{ord}_{p}f = m$.

###### _proof sketch:_

Choose $f = g^m$ where $g$ is the meromorphic function that separates tangents at $p$.

By induction on the number of terms, this allows us to get a meromorphic function with arbitrary Laurent tail at a point.

##### _lemma:_ functions with specified Laurent tail at a point

Given a point $p \in X$, a local coordinate $z$ centred at $p$, and a Laurent polynomial $r$ in $z$, there exists a meromorphic function $f \in \mathcal{M}_{X}(X)$ that has Laurent series with Laurent tail $r$.

###### _proof:_

Note that the meromorphic function that separates tangents at $p$ can be translated to have a zero at $p$ and written as $\lambda z$ in local coordinates. Then for a Laurent tail $a_{m} z^m$ with just one term it suffices to choose the meromorphic function with order $m$.

Suppose $r(z) = \sum_{n = m}^M a_{n} z^n$ has $k + 1$ terms. Then by the case for $k = 1$, there is a meromorphic function $g$ with Laurent tail $a_{m} z^m$. Now $g - r$ has Laurent series $\sum_{n = m + 1}^\infty b_{n} z^n$. Since $s(z) = \sum_{n = m + 1}^M b_{n} z^n$ has $k$ terms, by induction there is some $h$ with Laurent tail $s$. Thus, $g - h - r$ has Laurent series $\sum_{n = M + 1}^\infty c_{n} z^n$. That is, $g - h$ has Laurent tail $r$.

##### _lemma:_ functions with specified zero and pole

Given distinct points $p, q \in X$, there is a meromorphic function $f \in \mathcal{M}_{X}(X)$ with a zero at $p$ and a pole at $q$.

###### _proof sketch:_

Let $g$ be the meromorphic function that separates $p$ and $q$. Choose $f = (g - g(p))/(g - g(q))$ (alter appropriately or use $1 / g$ instead if $g$ has a pole or zero at $p$ or $q$).

We can extend this again by induction to finitely many poles.

##### _lemma:_ functions with specified zero and (finitely many) poles

Given points $p, q_{1}, \dots, q_{n} \in X$ (with $p \neq q_{i}$) there is a meromorphic function $f \in \mathcal{M}_{X}(X)$ with a zero at $p$ and a pole at each $q_{i}$ (with multiplicity).

###### _proof sketch:_

If $g$ has a zero at $p$ and poles at $q_{1}, \dots, q_{n - 1}$ then $f = g/(g - g(q_{n}))$ is the desired meromorphic function.

Finally, we can get a function of order greater 

##### _lemma:_ functions with order bounded below at finitely many points

For points $p, q_{1}, \dots, q_{n} \in X$ and any positive integer $M$, there is a meromorphic function $f \in \mathcal{M}_{X}(X)$ with $\operatorname{ord}_{p}(f - 1) \geq M$ and $\operatorname{ord}_{q_{i}} f \geq M$.

###### _proof:_

Let $g$ be the function with a zero at $p$ and poles at $q_{1}, \dots, q_{n}$. Then $f = 1 / (1 + g^M)$ is the desired function.

Finally, we get the desired result.

##### _proposition:_ Laurent series approximation

For finitely many points $p_{1}, \dots, p_{n} \in X$, corresponding local coordinates $z_{1}, \dots, z_{n}$ at each point, and Laurent polynomials $r_{1}, \dots, r_{n}$ there is a meromorphic function $f \in \mathcal{M}_{X}(X)$ such that $f$ has Laurent tail $r_{i}$ at each $p_{i}$. 

###### _proof:_

Choose a positive integer $M$ such that $\deg r_{i} < M$ for all $r_{i}$ (where degree is just the largest integer exponent). For a function not to interfere with a Laurent tail $r_{i}$ at $p_{i}$ it's sufficient to show the function has order at least $M$ at $p_{i}$.

Let each $g_{i}$ be a meromorphic function with Laurent tail $r_{i}$ at $p_{i}$. Let $m$ be the minimum of the orders $\operatorname{ord}_{p_{i}} r_{i}$. Also let $h_{i}$ be a meromorphic function with $\operatorname{ord}_{p_{i}}(h_{i} - 1) \ge M - m$ and $\operatorname{ord}_{q_{i}}h_{i} \geq M - m$. Then $f = \sum_{i = 1}^n g_{i} h_{i}$ is the desired meromorphic function.

At $p_{i}$, $g_{i} h_{i}$ has $h_{i} = 1$ and so $g_{i} h_{i} - r_{i}$ has order at least $M$. For $j \neq i$, each $g_{j} h_{j}$ has order greater than $M - m + m = M$, and thus, doesn't interfere. So $f$ has Laurent tail $r_{i}$ at $p_{i}$.

##### _corollary:_ meromorphic functions with finitely many specified orders

For finitely many points $p_{1}, \dots, p_{n} \in X$ and corresponding integers $m_{1}, \dots, m_{n}$, there is a meromorphic function $f \in \mathcal{M}_X(X)$ such that $\operatorname{ord}_{p_{i}} = m_{i}$ for each $i$.

### Meromorphic functions form a function field

Function fields in one variable are "nice" [[Abstract algebra --- math-171/notes/Fields#_definition _ fields|fields]]. 

##### _definition:_ function field

A function field (in one variable, over $\mathbb{C}$) is a finite extension of a purely transcendental extension $\mathbb{C}(z)$ of $\mathbb{C}$ of transcendence degree $1$.

Our goal is to show that the field of meromorphic functions is one of them.

##### _theorem:_ the field of meromorphic functions is a function field

The field $\mathcal{M}_{X}(X)$ is an extension of $\mathbb{C}$ of transcendence degree $1$.

###### _proof:_

The fact that $\mathcal{M}_{X}(X)$ has transcendence degree $1$ can be shown immediately, using our [[Algebraic curves and Riemann surfaces --- math-199DR/notes/The Riemann-Roch spaces of a divisor#_proposition _ the Riemann-Roch space is finite dimensional|our bound on the size of the Riemann-Roch space]]. Suppose $f, g$ are algebraically independent, and thus, linearly independent meromorphic functions. Then choosing $D$ sufficiently large that $f, g \in \mathcal{L}(D)$, we get
$$
f^i g^j \in \mathcal{L}(nD)
$$
for all $i, j$ with $i + j \le n$.

By [[Superdiscrete --- math-55A/notes/Multisets#_theorem _ the multichoose theorem|stars and bars]], this gives
$$
\binom{n + 2}{s} \le \mathcal{L}(n D)
$$
but we have
$$
\dim \mathcal{L}(D) \le 1 + n \deg D.
$$
Since the former is quadratic and the latter is linear, we have a contradiction.

To prove $\mathcal{M}_{X}(X)$ is finitely generated is harder, but in the process we prove some useful lemmas.

##### _lemma:_ a polynomial in $f$ with poles at poles of $f$

Let $D$ be a divisor on $X$ and let $\operatorname{div}_{\infty} f$ be the divisor of poles of $f$. Then there is a positive integer $n$, and a polynomial in $f$, say $g = r \circ f$ such that $D  - \operatorname{div} g \le n \operatorname{div}_{\infty} f$.

###### _proof sketch:_

Choose
$$
r(f) = \prod_{D(p) \ge 1, f(p) \in \mathbb{C}} (f - f(p))^{D(p)}.
$$
$g$ has zeroes of order $D(p)$ everywhere that $D$ is positive and $f$ doesn't have a pole. If $f$ has a pole them $n \div_{\infty} f+ \operatorname{div} g$ cancels to $0$ for $n = 1$, and by increasing $n$ can be made to be greater than $D$. (Recall that $\operatorname{div}_{\infty} f$ is positive at poles of $f$).

##### _corollary:_ products with poles at poles of $f$

For $f, h$ meromorphic functions on $X$ there is a polynomial such that $(r \circ f) h$ has no poles outside the poles of $f$.

###### _proof sketch:_

Take $D = - \operatorname{div} h$ in the previous theorem. It follows that $g h \in \mathcal{L}(n \operatorname{div}_{\infty} f)$.

##### _corollary:_ lower bound on the dimension of Riemann–Roch spaces

Given a meromorphic function $f$ on $X$, there is a constant positive integer $m$ such that for all $n > m$, and any $k \le \deg \mathcal{M}_{X}(X) / \mathbb{C}(f)$
$$
\dim \mathcal{L}(n D) \ge (n - m + 1)k.
$$

###### _proof sketch:_

Choose $k$ linearly independent elements of $\mathcal{M}_{X}(X)/\mathbb{C}(f)$, say $g_{1}, \dots, g_{k}$. Then $h_{i} = (r \circ f) g_{i}$ are linearly independent, have poles only at poles of $f$ and have $h_{i} \in \mathcal{L}(m D)$ for some $n$. 

The functions $f^i h_{j}$ with $i < n - m$ are all linearly independent and in $\mathcal{L}(n D)$.

##### _theorem:_ the degree of the function field

For $f$ a non-constant meromorphic function on $X$, the function field $\mathcal{M}_X(X)$ is an extension $\mathcal{M}_{X}(X) / \mathbb{C}(f)$ of degree $\deg (\operatorname{div}_{\infty} f)$.

###### _proof sketch:_

Suppose by way of contradiction that $\mathcal{M}_{X}(X) \geq 1 + \operatorname{deg} \operatorname{div}_{\infty} f$. Then we would have
$$
1 + n \deg (\operatorname{div}_{\infty} f) \ge \mathcal{L}(n \operatorname{div}_{\infty} f) \le (n - m_{0} + 1)(1 + \deg \operatorname{div}_{\infty} f)
$$
which is false for large enough $n$. So $\mathcal{M}_{X}(X) \leq \deg (\operatorname{div}_{\infty} f)$.

Using Laurent series approximation choose $g_{ij}$ with $g_{ij}$ having a pole of order $j$ at $p_{i}$. Then the list of all $g_{ij}$ such that $1 \le j \le \operatorname{div}_{\infty }f(p_{i})$. Proving this takes work.