---
tags:
- math-199DR/16
- cx-geo
- alg-geo
---

Let $X, Y$ be compact, connected Riemann surfaces.

A divisor is a way of packaging information about the zeroes and poles of a [[Riemann surfaces and algebraic curves --- math-199DR/notes/Functions on Riemann surfaces#_definition _ meromorphic|meromorphic function]], but it's even more useful than that. By considering divisors abstractly, we can understand the meromorphic functions that they do and don't represent, and thus, the Riemann surface!

##### _example:_ divisors on $\operatorname{Spec} \mathbb{Z}$

By [[Superdiscrete --- math-55A/notes/Prime numbers#_theorem _ unique factorisation|the fundamental theorem of arithmetic]], we can write any $r \in \mathbb{Q}$ as the ratio of primes in least terms —
$$
r = \frac{p_{1}^{\alpha_{1}} \dots p_{n}^{\alpha_{n}}}{q_{1}^{\beta_{1}} \dots q_{n}^{\beta_{n}}}.
$$
Instead we can package this as a function $r : \operatorname{Spec} \mathbb{Z} \to \mathbb{Z}$ where $(p_{i}) \mapsto \alpha_{i}$ and $(q_{i}) \mapsto \beta_{i}$. So rational numbers which are in some sense the meromorphic functions

##### _definition:_ divisor

A divisor on a Riemann surface $X$ is a function $D : X \to \mathbb{Z}$ which is supported on a discrete set of points.

Note that by [[Topology --- math-147/notes/Compactness#_theorem _ the Bolzano-Weierstrass theorem|Bolzano-Weierstrass theorem]], if $X$ is [[Topology --- math-147/notes/Compactness#_definition _ compact|compact]], then the support of $D$ is finite. 

Note also, that this definition is equivalent to an element of the free abelian group on $X$. In fact, the set of all divisors $\operatorname{Div} X$ is the free abelian group on $X$.

##### _definition:_ degree

The degree of a divisor $D$ on a compact Riemann surface is
$$
\operatorname{deg} D = \sum_{p \in X} D(p).
$$

##### _definition:_ divisors of degree zero

The set of all divisors of degree zero on $X$ is $\operatorname{Div}_{0} X$.

Note that this is obviously a [[Abstract algebra --- math-171/notes/Subgroups#_definition _ subgroup, $ le$|subgroup]] of $\operatorname{Div} X$.

### Principal divisors

The principal divisors allow us to achieve our original goal of keeping track of the zeroes and poles of a (non-zero) meromorphic function.

##### _definition:_ principal divisor

A divisor $D$ on $X$ is principal if it tracks the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Functions on Riemann surfaces#_definition _ order|order]] of a meromorphic function — $D(p) = \operatorname{ord}_{p} f$ for some non-zero meromorphic function $f$ on $X$.

We write such a divisor as $\operatorname{div} f$.

The set of all principal divisors on $X$ is $\operatorname{PDiv} X$.

##### _proposition:_ principal divisors

For (non-zero) meromorphic functions
- $\operatorname{div}(fg) = \operatorname{div} f + \operatorname{div} g$.
- $\operatorname{div}(1/f) = - \operatorname{div} f$.

It follows that the principal divisors are 

##### _proposition:_ principal divisors on a compact Riemann surface have degree zero

Since $X$ is compact, any principal divisor $\operatorname{div} f$ has $\operatorname{deg} (\operatorname{div} f) = 0$.

###### _proof_
follows immediately from the fact that the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#_theorem _ the sum of orders of a meromorphic function|sum of orders of a meromorphic function on a compact Riemann surface]] is $0$.

Thus, $\operatorname{PDiv} X \le \operatorname{Div}_{0} X$ for a compact Riemann surface $X$. Since everything is abelian, we have a well-defined abelian group $\operatorname{Jac} X = \operatorname{Div}_{0} X / \operatorname{PDiv} X$, and in fact, an exact sequence

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
	1 \ar[r, hook] & \mathcal{O}_{X}^*(X) \ar[r, hook] & \mathcal{M}^*_{X}(X) \ar[r, "f \mapsto \mathrm{div} f"] & \mathrm{Div}_{0} X \ar[r, two heads] & \mathrm{Jac} X \ar[r, two heads] & 0.
	\end{tikzcd}
\end{document}
```

We want to understand, when there are no restrictions to a degree $0$ divisors being a principal divisor — when is $\operatorname{Jac} X = 0$ and $\operatorname{PDiv} X = \operatorname{Div}_{0} X$? What does $\operatorname{Jac} X$ look like in general? An exceptional case is in genus $0$ with the Riemann sphere $\mathbb{C}_{\infty}$.

##### _example:_ all degree $0$ divisors on the Riemann sphere are principal

For any $D \in \operatorname{Div}_{0} \mathbb{C}_{\infty}$, consider
$$
f(w : z) = \prod_{[a : b] \in \operatorname{supp} D} (bw - az)^{D(p)}.
$$
Thus, $\operatorname{PDiv} \mathbb{C}_{\infty} = \operatorname{Div}_{0} \mathbb{C}_{\infty}$.

### Canonical divisors

Canonical divisors are like principal divisors, just keeping track of $1$-forms instead of meromorphic functions.

##### _definition:_ canonical divisor

A divisor $D$ on $X$ is canonical if it tracks the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Functions on Riemann surfaces#_definition _ order|order]] of a meromorphic $1$-[[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphic and smooth forms|form]] — $D(p) = \operatorname{ord}_{p} \omega$ for some non-zero meromorphic function $\omega$ on $X$.

We write the canonical divisor corresponding to $\omega$ as $\operatorname{div} \omega$.

The set of all canonical divisors on $X$ is $\operatorname{KDiv} X$.

##### _example:_ canonical divisors on the Riemann sphere

Note that $dz$ on $\mathbb{C}_{\infty}$ just has $\operatorname{div} \omega = -2 \cdot \infty$. Thus, any $\omega = f(z) \, dz$ has $\operatorname{div} \omega = \operatorname{div} f + \operatorname{div} dz$.

In fact this phenomenon holds in general for any meromorphic $1$-form $\omega$ on a compact Riemann surface.

##### _proposition:_ the difference of divisors of meromorphic $1$-forms

For any two meromorphic $1$-forms $\omega_{1}, \omega_{2}$ on $X$, there is a unique meromorphic function $f$ such that $f \omega_{1} = \omega_{2}$.

###### _proof:_

Do the obvious thing with the local forms $\omega_{1} = g_{1}(z) \, dz$ and $\omega_{2} = g_{2}(z) \, dz$.

It obviously follows that the difference of any two canonical divisors is a principal divisor. We can say this more specifically in group theoretic language.

##### _corollary:_ canonical divisors form a coset of the principal divisors

For any meromorphic $1$-form, $\omega$ on $X$ the canonical divisors form are the coset
$$
\operatorname{KDiv} X = \operatorname{div} \omega + \operatorname{PDiv} X.
$$

This fact allows us to get a canonical divisors on a Riemann surface from just the genus and the pullback of the form.

##### _theorem:_ compact Riemann surfaces have canonical divisors of degree $2g - 2$

If $X$ is a compact Riemann surface of [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological invariants of a surface#_definition _ genus|genus]] $g$ with a non-constant meromorphic function, then there is a canonical divisor $\operatorname{div} \eta \in \operatorname{KDiv} X$ with $\operatorname{deg} (\operatorname{div} \eta) = 2g - 2$.

###### _proof:_

For the meromorphic function, let $\pi : X \to \mathbb{C}_{\infty}$ be the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ meromorphic functions are maps to the Riemann sphere|corresponding holomorphism to the Riemann sphere]]. Consider the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphic and smooth forms#_definition _ pullback of forms|pullback]] of $\omega = dz$ on $\mathbb{C}$, call it $\eta = \pi^* \omega$. Using [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#Hurwitz' formula|Hurwitz' formula]] and the formula for the [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphic and smooth forms#_proposition _ the order of the pullback of a form|order of the pullback of a form]], it follows that $\operatorname{div} \eta$ has degree $2g - 2$.
 Specifically, recalling that $\operatorname{div} \omega = -2 \cdot \infty$,
 $$
\begin{align}
\deg (\operatorname{div} \eta) & = \sum_{p \in X} (\operatorname{mult}_{p} \pi - 1)  + \sum_{p \in X} \operatorname{mult}_{p}\pi \operatorname{div}_{\pi(p)} \omega \\
 & = 2g - 2 + 2 \operatorname{deg} \pi - 2 \sum_{p \in \pi^\text{pre}(\{ \infty \})} \operatorname{mult}_{p}\pi \\
 & = 2g - 2 + 2 \operatorname{deg} \pi - 2 \operatorname{deg} \pi \\
 & = 2g - 2.
\end{align}
$$
where the second equality is just Hurwitz' formula.

### Pulling back divisors

Let $\pi : X \to Y$ be a non-constant holomorphism of compact Riemann surfaces. We want a way to pull back divisors in a way that preserves the pullback of meromorphic functions/forms. That is, for a meromorphic form $\omega$ or function $f$ on $Y$, we want $\operatorname{div} (\pi^*f)$ related to $\pi^*(\operatorname{div} f)$ and $\operatorname{div}(\pi^* \omega)$ related to $\pi^*(\operatorname{div} \omega)$.

We get even better! Pulling back divisors also preserves the group structure on the divisors!

We can represent a point $q \in Y$ by a divisor $q$ that is $1$ at $q$ and zero everywhere else. The obvious thing to do is to pull this back to the points that go to $q$ and scale by the multiplicity of each point.

##### _definition:_ the pre-image divisor of a point

The pre-image divisor of a point $q \in Y$ under $\pi$ is given by
$$
\pi^*q(p) = \begin{cases}
\operatorname{mult}_{p}\pi & p \in \pi^\text{pre}(\{ q \}) \\
 0 & \text{otherwise}.
\end{cases}
$$

This is just a special case of how to pullback a divisor in general — we extend this definition on the "basis" of the abelian group/$\mathbb{Z}$-module to all of $\operatorname{Div} X$.

##### _definition:_ pullback of a divisor

The pullback of a divisor $D \in \operatorname{Div} Y$ under $\pi$ is $\pi^* D$ given by
$$
\pi^* D(p) = D(q) \, \pi^* q(p) = \operatorname{mult}_{p} \pi \, D(q)
$$
where $q = \pi(p)$.

##### _proposition:_ algebraic properties of pullback of divisors

Given a non-constant [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphism]] $\pi : X \to Y$, a meromorphic function $f$ on $Y$, and a meromorphic form $\omega$ on $Y$
- $\pi^* : \operatorname{Div} Y \to \operatorname{Div} X$ by $D \mapsto \pi^* D$ is a [[Abstract algebra --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphism]].
- the homomorphism restricts to a homomorphism $\operatorname{PDiv} Y \to \operatorname{PDiv} X$ since the pullback of a principal divisor is principal with $\operatorname{div} (\pi^*f) = \pi^*(\operatorname{div} f)$
- (for $X, Y$ compact) the homomorphism also restricts to a homomorphism $\operatorname{Div}_{0} Y \to \operatorname{Div}_{0} X$ — specifically, $\operatorname{deg} \pi^* D = \operatorname{deg} \pi \operatorname{deg} D$.
- thus, there is an induced homomorphism $\operatorname{Jac} Y \to \operatorname{Jac} X$

###### _proof:_

The homomorphism property follows because we defined the pullback on "basis" elements and then extended $\mathbb{Z}$-linearly.

Since
$$
\begin{align}
\pi^*(\operatorname{div} f)(p) = \operatorname{mult}_{p} \pi \operatorname{ord}_{\pi(p)} \pi
\end{align}
$$
and
$$
\operatorname{div}(\pi^* f) = \operatorname{div}(f \circ \pi) = \operatorname{mult}_{p}\pi \operatorname{ord}_{\pi(p)} \pi
$$
the two are equal, as desired.

Finally,
$$
\begin{align}
\operatorname{deg} \pi^* D  & = \sum_{p \in X} \operatorname{mult}_p \pi \, D(f(p)) \\
 & = \sum_{p \in \pi^\text{pre}(\{ q \})} \operatorname{m u l t}_{p}\pi \sum_{q \in Y} D(q) \\
 & = \operatorname{deg} D \sum_{p \in \pi^\text{pre}(\{ q \})} \operatorname{m u l t}_{p}\pi \\
 & = \operatorname{deg} D \deg \pi.
\end{align}
$$

To get similar results for canonical divisors, we need to introduce divisors that keep track of [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#_definition _ ramification point, branch point|ramification and branching]] — the formula for the pullback of a divisor requires more subtle "Hurwitzing".

##### _definition:_ ramification and branch divisors

The ramification divisor of $\pi$ is a divisor on $X$ defined by $R_{\pi}(p) = \operatorname{mult}_{p} \pi - 1$.

The branch divisor of $\pi$ is a divisor on $Y$ defined by $B_{\pi}(p) =$

The ramification and branch divisors have the same degree which is the error term in [[Riemann surfaces and algebraic curves --- math-199DR/notes/Topological properties of holomorphisms#_theorem _ Hurwitz' formula|Hurwitz' formula]]. Thus, it can be rewritten as
$$
2 g_{X} - 2 = \operatorname{deg} \pi (2 g_{Y} - 2) + \operatorname{deg} R_{\pi}.
$$

##### _proposition:_ pullbacks of canonical divisors

The pullback of a canonical divisor gives $\operatorname{div}(\pi^* \omega) = \pi^*(\operatorname{div} \omega) + R_{\pi}$, where $R_{\pi}$ is the ramification divisor of $\pi$.

###### _proof:_
is all the steps of the proof to get a canonical divisor of degree $2g - 2$.