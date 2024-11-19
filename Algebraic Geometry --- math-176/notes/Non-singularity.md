---
tags:
- math-176/35
- alg-geo
---

How can we understand what it means for an [[Algebraic Geometry --- math-176/notes/Non-singular projective varieties|affine variety]] to be non-singular in terms of the algebra that defines it?

Recall that we have a [[Algebraic Geometry --- math-176/notes/Spectra#_proposition _ primes as points|correspondence]] between points on a variety $X$ and primes in its coordinate ring $\mathcal{O}(X)$. Thus, we claim

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