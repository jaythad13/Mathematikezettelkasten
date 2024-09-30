---
tags:
- math-176/15
---

The easiest case we will consider is non-singular and projective.

### Non-singular projective varieties

##### _definition:_ non-singular projective variety

Let $F$ be a field. A subset
$$
V(F) = \{ p \in \mathbb{P}^n(F) \mid f_{1}(p) = \dots = f_m(p) = 0 \}
$$
is called a non-singular projective variety of dimension $d$ if the following axioms hold.
1) Homogeneity: each $f_{k}$ is a [[Algebraic Geometry --- math-176/notes/Diophantine equations#_definition _ homogenous polynomial|homogenous]] polynomial in ,of degree $e_{k}$ in $F[x_{1}, \dots, x_{n}, x_{0}]$.
2) Non-singularity: the $m$-by-$(n + 1)$ Jacobian of the function $f = (f_{1}, \dots, f_{m})$ has rank $m$ for all points $p \in \mathbb{P}^n(\overline{F})$ where $\overline{F}$ is the algebraic closure of $F$.
3) Irreducibility: if $S(e)$ is the collection of homogenous polynomials of degree $e$ in $F[x_{1}, \dots, x_{n}, x_{0}]$. Then the ideal
$$
I(V) = \bigoplus_{e \ge 1} \{ f(x_{1}, \dots, x_{n}, x_{0}) \in S(e) \mid f(p) = 0 \text{ for all } p \in V(F) \}
$$
is a [[Abstract Algebra I --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|prime ideal]] in the graded polynomial ring $S = \bigoplus_{e \ge 1} S(e)$.
4) The dimension is $d = n - m$.

Often for $d = 1$ we say $V$ is a surface, for $d = 2$, we say $V$ is a surface, and for $d = 3$, we say $V$ is a $3$-fold.