---
tags:
- math-176/35
- math-176/36
- alg-geo
---

How can we understand what it means for an [[Algebraic varieties --- math-176/notes/Non-singular projective varieties|affine variety]] to be non-singular in terms of the algebra that defines it?

Recall that we have a [[Algebraic varieties --- math-176/notes/Spectra#_proposition _ primes as points|correspondence]] between points on a variety $X$ and primes in its coordinate ring $\mathcal{O}(X)$. Thus, we claim

##### _proposition:_ algebraic condition for non-singularity

An affine variety $X = Z(f_{1}, \dots, f_{m})$ is non-singular if and only if $\dim M_{p} / M_{p}^{2} = n - m$ for all $p \in X$.

###### _proof sketch:_

We need to show that the Jacobian of $f : x \mapsto (f_{1}(x), \dots, f_{m}(x))$ has rank $m$ at $p$ if and only if $\dim M_{p}/M_{p}^{2} = n - m$.

We do this by showing that $M_{p} / M_{p}^{2} \cong \mathrm{T}_{p}X$ (the tangent space of $X$ at $p$, which is just the kernel of the Jacobian of $f$ at $p$). This follows by noticing that
$$
\begin{align*}
\varphi & : \mathrm{T}_{p}X \times M_{p}/M_{p}^{2} \to F \\
& : ((x_{1}, \dots, x_{n}), f) \mapsto \sum_{k = 1}^n \frac{ \partial f }{ \partial x_{k} } \Big |_{p} x_{k}.
\end{align*}
$$

Note that with some more commutative algebra, we can express the case $n = m + 1$ in terms of the localisation of $\mathcal{O}(X)$ at $p$, called $\mathcal{O}_{p}$ — $X$ non-singular is equivalent to each of the following conditions.
1) $\mathcal{O}_{p}$ is a discrete valuation ring
2) $\mathcal{O}_{p}$ is integrally closed.

But how do we turn this into a global condition that we can check all at once?At the very

##### _proposition:_ non-singularity 

The following are equivalent for a variety $X = Z(I)$ for $I \in \operatorname{Spec} R$ with
1) $X$ is non-singular at all $M \in \operatorname{mSpec}(\mathcal{O})$.
2) $\dim (M / M^{2}) = 1$ for all $M \in \operatorname{mSpec}(\mathcal{O})$.
3) $\mathcal{O}$ is a Dedekind domain — an [[Abstract algebra --- math-171/notes/Integral domains|integral domain]] that is [[Abstract algebra --- math-171/notes/Unique factorisation#_theorem _ Every PID is a UFD|Noetherian]], integrally closed, and has $\dim \mathcal{O} = 1$.

This means we can define curves abstractly, by just picking any Dedekind domain!

##### _definition:_ abstract non-singular curve

For any Dedekind domain $\mathcal{O}$, we say $X = \operatorname{Spec} \mathcal{O}$ is an abstract non-singular curve.

##### _example:_ elliptic curves

Consider the elliptic curve $E : y^{2} = x^3 + A x + B$. We know that the points on $E$ form an affine variety, and adding the point at infinity gives us a projective variety. Then there is an obvious bijection between the max spectrum of
$$
\mathcal{O}(E) = F[x, y] / (y^{2} - x^{3} - Ax - B)
$$
and the affine points of $E$. Further, the $\operatorname{mSpec} \mathcal{O}$ differs from $\operatorname{Spec} \mathcal{O}$ only by the zero ideal, so we can identify the point at infinity with the zero ideal.

A more abstract example is

##### _example:_ $\operatorname{Spec} \mathbb{Z}$

It turns out that all [[Abstract algebra --- math-171/notes/Unique factorisation#_definition _ principal ideal domain|PIDs]] are Dedekind domains, so $X = \operatorname{Spec} \mathbb{Z}$ is a non-singular curve where all the points are the primes!