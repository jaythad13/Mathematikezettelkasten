---
tags:
- alg-geo
- math-176/25
---

We can define polynomials for rings too, and these polynomials form rings themselves!

##### _definition:_ polynomial, degree, $R[x]$

Given a ring $R$, a polynomial $p$ is a formal sum
$$
a_{n} x^n + \dots + a_{1} x + a_{0}
$$
with $a_{n} \in R$. 

If $n$ is the largest integer with $a_{n} \neq 0$, we say say the degree of $p$ is $\operatorname{deg}(p) = n$. If all coefficients $a_{n}$ are $0$, we say $\operatorname{deg}(p) = -\infty$.

##### _proposition:_ polynomial rings are rings

$R[x]$ is a ring under the obvious multiplication and addition.

##### _proposition:_ polynomials over integral domains are really nice

If $R$ is an integral domain, then $R[x]$ is an integral domain with the same units as $R$ and $\operatorname{deg}(pq) = \operatorname{deg} p + \operatorname{deg} q$ for any $p, q \in R[x]$.

###### _proof:_

Suppose $R$ is an integral domain. Consider any non-zero polynomials $p = \sum a_{j} x^j$ and $q = \sum b_{j} x^j$ of degrees $m$ and $n$ in $R[x]$. Their product has a leading term $a_{m} b_{n} x^{m + n}$ and since $R$ is an integral domain, $a_{m} b_{n} \neq 0$. Thus, $\operatorname{deg}(pq) = p + q > -\infty$ giving $pq \neq 0$. 

The units of $R[x]$ are just the polynomials constant on a unit. This is just isomorphic to the units of $R$.

##### _corollary:_ multivariate polynomial rings

If $R$ is an integral domain, then $R[x_{1}, \dots, x_{n}, x_{n + 1}] = R[x_{1}, \dots, x_{n}][x_{n + 1}]$, defined inductively, is an integral domain.

On $F[x_{1}, \dots, x_{n}]$ for algebraically, closed $F$, we have the following incredibly nice theorem by using the first isomorphism theorem.