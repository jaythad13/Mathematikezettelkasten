---
tags:
- math-199DR/27
- math-199DR/28
- cx-geo
---

Let $X$ be a compact, connected Riemann surface.

Abel's theorem characterises [[Riemann surfaces and algebraic curves --- math-199DR/notes/Divisors#_definition _ principal divisor|principal divisors]] —

##### _theorem:_ Abel's theorem

If $D$ is a divisor of degree $0$ on $X$, then $D$ is the divisor of a meromorphic function if and only if it is in the kernel of the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Periods and the Jacobian#_definition _ Abel-Jacobi map|Abel-Jacobi map]].

Essentially, what we want to prove is that the Abel-Jacobi map gives us a way to show that the missing piece in both of the [[Abstract algebra --- math-171/notes/Exact sequences#_definition _ exact sequence|exact sequences]] below is the Jacobian.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathcal{O}_{X}(X)^* \ar[r] & \mathcal{M}_{X}(X)^* \ar[r, "\mathrm{div}"] & \mathrm{Div}_{0} \, X \ar[r] & ? \ar[r] & 0 \\
		0 \ar[r] & \mathrm{B}_{1}(X) \ar[r] & \mathrm{Z}_{1}(X) \ar[r] & \Omega_{1}(X)^\vee \ar[r] & ? \ar[r] & 0
	\end{tikzcd}
\end{document}
```

### Traces and necessity in Abel's theorem

Suppose $f$ or $\omega$ is a [[Riemann surfaces and algebraic curves --- math-199DR/notes/Functions on Riemann surfaces#_definition _ holomorphic functions|function]] or [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphic and smooth forms|form]] on $Y$ and $\pi : X \to Y$ is a [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphism]]. Then there is a sensible notion of the pullback of the function $\pi^* f = f \circ \pi$ and the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphic and smooth forms#_definition _ pullback of forms|pullback of the form]] $\pi^* \omega$. We can also have a "pushforward" called the trace of the function.

Let $\pi : X \to Y$ be a holomorphism of degree $d$ and $f$ meromorphic on $X$, the trace of $f$ is the function on $Y$ that sends a point $q \in Y$ to the sum of $f(p)$ for all pre-images $p$ of $q$, with multiplicity. To construct this formally is actually a little more complicated since we have to avoid ramification points.

##### _definition:_ trace of a function

The trace of $f$ on $X$ under $\pi : X \to Y$ is $\operatorname{tr}_{\pi} f$ on $Y \setminus \lvert B_{\pi} \rvert$ given by
$$
\operatorname{tr}_{\pi} f(q) = \sum_{n = 1}^d f(p_{n})
$$
where the $p_{n}$ are the $d$ pre-images of $q$ under $\pi$. $\lvert B_{\pi} \rvert$ is the support of the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Divisors#_definition _ ramification and branch divisors|branch divisor]] — the set of branch points of $\pi$.

##### _proposition:_ the trace of a meromorphic function is meromorphic

Given a meromorphic function $f$ on $X$, its trace under a holomorphism $\pi : X \to Y$ extends to a unique meromorphic function on $Y$ that is holomorphic at all $q \in Y$ that have $f$ holomorphic on $\pi^\text{pre}(\{ q \})$.

We will prove this in greater generality just shortly. 

Notice that we can make the exact same construction for forms —

##### _definition:_ the trace of a meromorphic form

The trace of a meromorphic $1$-form $\omega$ on $X$ under $\pi : X \to Y$ is $\operatorname{tr}_{\pi} \omega$ on $Y \setminus \lvert B_{\pi} \rvert$ is
$$
\operatorname{tr}_{\pi} \omega = \sum_{n = 1}^d {\pi_{|V_{i}}^{-1}}^* \omega.
$$

We claim that the trace of meromorphic forms is meromorphic too.

##### _proposition:_ the trace of a meromorphic $1$-form is meromorphic

Given a meromorphic $1$-form $\omega$ on $X$, its trace under a holomorphism $\pi : X \to Y$ extends to a unique meromorphic form on $Y$.

###### _proof:_

The idea here is to use a roots of unity filter to get a power series for $\operatorname{tr}_{\pi} \omega$ in terms of a local coordinate on $Y$. The desired result follows.

Let $q$ be a branch point, and $p$ a pre-image of $q$ under $\pi$, with [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#_definition _ multiplicity|multiplicity]] $m$. That is, in [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#_proposition _ local normal form|local normal form]], we have local coordinates $w$ and $z$ centred at $p$ and $q$ such that $z = w^m$. For non-zero $z$, we have $m$ pre-images $\zeta^{j} w$ for $\zeta = e^{2 \pi i / m}$.

Note then that $dz = m w^{m - 1} \, d w$. Thus, for $\omega = f(w) dw$ and
$$
f(w) = \sum_{n \in \mathbb{Z}} a_{n} z^n
$$
locally, we have
$$
\begin{align}
\operatorname{tr}_{\pi} \omega & = \sum_{j = 0}^{m - 1} f(\zeta^j w) \, dw  \\
& =  \sum_{j = 0}^{m - 1} \sum_{n \in \mathbb{Z}} a_{n} \frac{(\zeta^j w)^n}{m (\zeta^j w)^{m - 1}} \, dz \\
 & = \frac{1}{m} \sum_{n \in \mathbb{Z}} \left( \sum_{j = 0}^{m - 1} \zeta_{j}^{n - m + 1} \right)  w^{n - m + 1} \, dz
\end{align}
$$

If $m$ divides $n - m + 1$, then each of the $\zeta_{j}^k$ terms is just $1$. If $m$ does not divide $n - m + 1$, then the sum of the $\zeta_{j}^k$ terms is $0$. Thus, only the $n - m + 1$ divisible by $m$ survive.

But if $n - m + 1 = km$, then we have
$$
\operatorname{tr}_{\pi} \omega = \sum_{k \in \mathbb{Z}} \frac{a_{(k + 1)m  - 1}}{m} w^{km} \, dz = \sum_{k \in \mathbb{Z}} b_{k} z^k \, dz.
$$

Thus, $\operatorname{tr}_{\pi} \omega$ has a Laurent series, and is meromorphic. Since the Laurent series only has negative terms when the Laurent series of $\omega$ in terms of $w$ does, $\operatorname{tr}_{\pi} \omega$ is holomorphic wherever all of the pre-images have $\omega$ holomorphic.

By pulling back paths as well, we can understand how taking the trace affects the integral of a form.

##### _definition:_ pullback of a path

Given a holomorphism $\pi : X \to Y$ of degree $d$, the pullback of a path $\gamma$ under $\pi$ is the chain
$$
\pi^* \gamma = \gamma_{1} + \dots + \gamma_{d}
$$
where $\gamma_{1}, \dots, \gamma_{d}$ are the $d$ distinct paths obtained by pulling back $\gamma$ at non-branch points.

We can ignore issues of [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#_definition _ ramification point, branch point|ramification and branching]] since they occur at finitely many points. We're only pulling back this path to integrate, and integration doesn't care about finite point sets.

##### _lemma:_ integral of the trace is the integral of the form on pullback chain

Given a path $\gamma$ on $Y$, and a meromorphic $1$-form on $X$,
$$
\int_{\pi^* \gamma} \omega  = \int_{\gamma} \operatorname{tr}_{\pi} \omega.
$$

###### _proof sketch:_

Ignore the measure zero branch points. Just push through computations from the right hand side to the left
$$
\int_{\gamma} \operatorname{tr}_{\pi} \omega = \int_{\gamma} \sum_{j = 1}^d {\pi_{|V_{j}}^{-1}}^* \omega = \sum_{j = 1}^d \int_{\pi_{\mid V_{j}}^\text{pre}(\gamma)} \omega = \int_{\pi^* \gamma} \omega.
$$

##### _theorem:_ necessity in Abel's theorem

If $f$ is a meromorphic function on $X$ then $A_{0}(\operatorname{div} f) = 0$.

###### _proof:_

For $f$, let $\pi_{f} : X \to \mathbb{C}_{\infty}$ be the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ meromorphic functions are maps to the Riemann sphere|corresponding holomorphism to the Riemann sphere]] of [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#_definition _ degree of a map|degree]] $d$. Write
$$
\operatorname{div} f(q) = \begin{cases}
1 & q = z_{j} \\
-1 & q = p_{j} \\
0
\end{cases}
$$
so that the $z_{j}$ are zeroes and $p_{j}$ are poles of $f$ (there are $d$ of each)

Then without loss of generality, we can choose the path we integrate over for $A_{0}(D)$ to be the sum of paths $\gamma_{i}$ from $z_{i}$ to $p_{i}$. Given a form $\omega$ on $X$, we then have
$$
A_{0}(\operatorname{div} f) : \omega \mapsto \sum_{i = 1}^d \int_{\gamma_{i}} \omega = \sum_{i = 1}^d \int_{\gamma} \operatorname{tr}_{\pi_{f}} \omega 
$$

Since $\mathbb{C}_{\infty}$ has genus $0$, it has no non-zero holomorphic $1$-forms. Thus, $\operatorname{tr}_{\pi_{f}} \omega = 0$ and the integral is zero.

### The debauch of the period lemmata

Sufficiency in Abel's theorem (that if $A_{0}(D) = 0$ for a degree $0$ divisor $D$, we have $D = \operatorname{div} f$) requires a lot more lemmatic work. The idea is that, instead of looking for a meromorphic function directly, we look for a meromorphic $1$-form $\omega$ with all simple poles, and residue $\operatorname{res}_{p} \omega = D(p)$ for all $p \in X$, that is also nice in a way that we will make specific.

Essentially, we look at a meromorphic $1$-form that looks like
$$
f(p) = \exp \int_{p_{0}}^p \omega.
$$
Locally, $\omega$ looks like $D(p) / z + g(z) \, dz$.

In order for this to be well-defined (this is the extra niceness, and also the cause for the lemmata) we need that for any loop $\gamma$, we have $\int_{\gamma} \omega = 2 \pi i m$.

By the proof of [[Riemann surfaces and algebraic curves --- math-199DR/notes/Serre duality|Serre duality]], we know that as long as a [[Riemann surfaces and algebraic curves --- math-199DR/notes/Algebraic curves#_definition _ Laurent tail|Laurent tail]] has residues satisfying [[Riemann surfaces and algebraic curves --- math-199DR/notes/The residue theorem#_theorem _ the residue theorem|the residue theorem]]. Thus, we have $\omega$ with all poles simple, and the desired residues. In fact, since each of the values of $D(p)$ is an integer, we have that on each $1$-[[Simplicial homology and random walks --- math-145/notes/Simplicial homology#_definition _ boundaries|boundary]] loop $\gamma$, the integral is indeed an integer multiple of $2 \pi i m$.

##### _definition:_ meromorphic function given by a form

For a closed $1$-form $\sigma$, the meromorphic $1$-form given by $\sigma$ is $f_{\sigma}$ given by
$$
f_{\sigma}(p) = \int_{p_{0}}^p \sigma.
$$

##### _lemma:_ a Stokes' theorem trick

For any closed $1$-form $\sigma$, and meromorphic $1$-form $\tau$ on $X$, where no poles are on loops $a_{i}, b_{i}$, we have
$$
\int_{\partial P} f_{\sigma} \tau = \sum_{i = 1}^g A_{i}(\sigma)  B_{i}(\tau)  - A_{i}(\tau) B_{i}(\sigma)
$$

###### _proof sketch:_

Apply [[Curves and surfaces --- math-142/notes/Integration on a surface#_theorem _ Stokes' theorem for differential forms|Stokes' theorem]] and the definition of the exterior derivative.

##### _lemma:_ the integral of a non-zero holomorphic $1$-form

If $\omega$ is a non-zero holomorphic $1$-form, then $\sum_{i = 1}^g A_{i}(\omega) \overline{B_{i}(\omega)}$ has negative imaginary part.

###### _proof sketch:_

Apply the lemma above to $\omega$ and $\overline{\omega}$ to get through a series of computations that
$$
\iint_{X} \omega \wedge \overline{\omega} = \iint \lvert f(z) \rvert ^{2} (-2i \, dx \wedge dy)
$$
where $\omega = f(z) \, dz$ locally and we write $dz = dx + i \, dy$. Compare to the desired sum.

##### _proposition:_ non-zero holomorphic $1$-forms have non-zero periods

If $\omega$ is a holomorphic $1$-form, with all $a$-periods or $b$-periods $0$, then $\omega = 0$.

###### _proof:_

Plug $\omega$ into the previous lemma. If $\omega$ is non-zero, the alternating sum of integrals has non-zero imaginary part, and thus, we can't have all $a$-periods $0$, nor all $b$-periods $0$.

We can package all of this information into linear maps.

##### _definition:_ period linear maps

The period linear maps are $A, B : \Omega^1(X) \to \mathbb{C}^g$ by $A \omega = (A_{1}\omega, \dots, A_{g}\omega)$, and $B$ defined similarly.

##### _proposition:_ period linear map properties

The period linear maps $A$ and $B$ are non-singular and satisfy
$$
B^\top A - A^\top B = 0.
$$

##### _theorem:_ sufficiency in Abel's theorem

If $A_{0}(D) = 0$ for a degree $0$ divisor $D$, we have $D = \operatorname{div} f$, for some meromorphic function $f$ on $X$.
###### _proof:_

We can write $A_{0}(D)$ explicitly as a row (rho, get it?) vector $\rho = \begin{pmatrix} \rho_{1} & \dots & \rho_{g} \end{pmatrix} \in \mathbb{C}^g$ where
$$
\rho_{k} = \frac{1}{2 \pi i} \sum_{i = 1}^g A_{i}(\omega_{k}) B_{i}(\tau) - A_{i}(\tau) B_{i}(\omega_{k}).
$$
Since $A_{0}(D)$ is zero modulo periods, we must have that $\rho$ is a period. That is, we must have that each $\rho_{k}$ is an integer linear combination of $a$-periods and $b$-periods —
$$
\rho_{k} = \sum_{i = 1}^g m_{i} A_{i}(\omega_{k}) - n_{i} B_{i}(\omega_{k}).
$$

We claim we have a short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \Omega^1(X) \ar[r, "\alpha"] & \Lambda \ar[r, "\beta"] & \mathbb{C}^g \ar[r] & 0
	\end{tikzcd}
\end{document}
```
where $\alpha$ is the product map $(A, B)$ and $\beta$ is the "coproduct map" $(B^\top, -A^\top)$. $\beta \circ \alpha = 0$ by our lemma about period linear maps. Thus we have $\operatorname{img} \alpha \subseteq \ker \beta$. By rank-nullity we can see that they have the same dimension, and so must be equal.

Thus
$$
f(p) = \operatorname{exp} \int_{p_{0}}^p \tau - \omega
$$
is the desired meromorphic function with $D = \operatorname{div} f$.

### Consequences

From Abel's theorem, lots of useful facts follow. 

For one, the Abel-Jacobi map gives a way to embed a Riemann surface into its [[Riemann surfaces and algebraic curves --- math-199DR/notes/Periods and the Jacobian#_definition _ the Jacobian|Jacobian]]. We of course haven't described the complex manifold structure on the Jacobian, nor what it really means to be an embedding, so we will just describe why the Abel-Jacobi maps is an inclusion

##### _proposition:_ the Abel-Jacobi map is an embedding

Let $X$ be a compact Riemann surface of genus $g \geq 1$. Then the general Abel-Jacobi map $A : X \to \operatorname{Jac}(X)$ (with a choice of base point $p_{0}$) is injective.

We can also show ([[Riemann surfaces and algebraic curves --- math-199DR/notes/Linear equivalence of divisors#_theorem _ Abel's theorem for elliptic curves|yet again]]) that every genus $1$ curve is a complex torus $\mathbb{C} / \Lambda$ and gives us that it is an abelian variety — we get the group law of an elliptic curve.

##### _theorem:_ classification of genus $1$ curves

Suppose $X$ is an algebraic curve of genus $1$. Then $\operatorname{Jac} X$ is a complex torus $\mathbb{C} / \Lambda$ of dimension $1$, and the Abel-Jacobi map is an [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ biholomorphism/isomorphism, automorphism|isomorphism]] of Riemann surfaces.

