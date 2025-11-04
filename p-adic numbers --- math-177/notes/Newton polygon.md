---
tags:
- math-177/20
- alg-nt
---

The Newton polygon of a polynomial encodes information of the orders of the coefficients of a ($p$-adic) polynomial. Incredibly, this also encodes information about the order of roots of the Newton polynomials, even when they don't live in $\mathbb{Q}_{p}$.

##### _definition:_ Newton polygon

Given a polynomial with $f(x) = \sum_{i = 0}^n a_{i} x^i$, its Newton polygon is $N(f)$, the convex hull of the points $(i, \operatorname{ord}_{p} a_{i})$ in $\mathbb{R}^{2}$.z 

---

We first show that the Newton polygon has the desired properties in a special case, and then reduce the general case to that.

##### _lemma:_ the Newton polygon for $a_{0} = 1$

Suppose $f \in 1 + (x) \subseteq \mathbb{Q}_{p}[x]$. Then the Newton polygon $N(f)$ has a segment of horizontal length $r$ and slope $\lambda$ if and only if it has $r$ roots (in the splitting field of $f$) each of which has order $-\lambda$. 

###### _proof sketch:_

Factor $f$ as
$$
f(x) = \sum_{i = 0}^n a_{i} x^i = \prod_{j = 1}^n \left( 1 - \frac{x}{\alpha_{j}} \right).
$$
Let $\lambda_{j} = \operatorname{ord}_{p}(1 / \alpha_{j}) = - \operatorname{ord}_{p} \alpha_{j}$. Choose the order such that the $\lambda_j$ are non-decreasing. Suppose $\lambda_{1} = \dots = \lambda_{r} < \lambda_{r + 1}$. Writing $a_{i}$ as the sum of products of $i$ elements $1 / \alpha_{j}$, we get that
$$
\operatorname{ord}_{p} a_{i} \geq \min \left\{  \operatorname{ord}_{p} \prod_{k = 1}^i 1/\alpha_{j_{k}}  \right\} \geq \min \left\{  \sum_{k = 1}^i \lambda_{j_{k}} \right\}
$$
If $0 \le i < r$ then some standard manipulations give us that $(i, \operatorname{ord}_{p} a_{i})$ is at or above the line $y = \lambda_{1} x$. If $i = r$, then there is a unique smallest sum. Since [[p-adic numbers --- math-177/notes/The topology of the p-adics#_proposition _ every triangle is isosceles|every triangle is isosceles]], we have $\operatorname{ord}_{p} a_{r} = \min \left\{  \sum_{k = 1}^i \lambda_{j_{k}} \right\} = r \lambda_{1}$. Thus, $(r, \operatorname{ord}_{p} a_{r})$ is on the line $y = \lambda_{1} x$. Finally, if $i > r$, then since $\lambda_{r + 1} > \lambda$, the minimum sum $\lambda_{1} + \dots + \lambda_{r} + \lambda_{r + 1} + \dots + \lambda_{i}$ is greater than $i \lambda_{i}$. That is, $(i, \operatorname{ord}_{p} a_{i})$ is strictly above $y = \lambda_{1} x$. Thus, the first segment of $N(f)$ joins $(0, 0)$ to $(r, \operatorname{ord}_{p} a_{r})$. That is, there are exactly $r$ roots of order $\lambda$ exactly when there are the first $r$ coefficients $a_{1}, \dots, a_{r}$ with $\operatorname{ord}_{p} a_{r} = \lambda r$ and $\operatorname{ord}_{p} a_{0} = 0$.

---

##### _theorem:_ the Newton polygon encodes orders of roots

Suppose $f \in \mathbb{Q}_{p}[x]$. Then the Newton polygon $N(f)$ has a segment of horizontal length $r$ and slope $\lambda$ if and only if it has $r$ roots (in the splitting field of $f$) each of which has order $-\lambda$.

###### _proof:_

Write $f(x) = a_{k} x^k g(x)$ where $g(x) \in 1 + (x) \subseteq \mathbb{Q}_{p}[x]$. The $N(f)$ is $N(g)$, shifted to the right by $k$ and up by $\operatorname{ord}_{p} a_{k}$. The only additional zeroes of $f$ are $0$, with multiplicity $k$, so the Newton polygon property is still preserved.

---

### Consequences...

##### _corollary:_ a criterion for irreducibility

If $f \in \mathbb{Q}_{p}[x]$ is [[p-adic numbers --- math-177/notes/Irreducible polynomials#_definition _ irreducible polynomial|irreducible]] then $N(f)$ consists of exactly one segment.

Equivalently, if $N(f)$ has more than one segment, then $f$ is reducible.

###### _proof:_

If $f$ is irreducible, then $\mathbb{Q}_{p}(\alpha) \cong \mathbb{Q}_{p}(\beta)$ for any roots $\alpha, \beta$ of $f$. Thus, any roots of irreducible $f$ have the same order. Thus, $N(f)$ consists of exactly one segment.

---

##### _definition:_ pure Newton polygon

A Newton polygon $N(f)$ is **pure** if it consists of one segment.

---

This can be stated more generally.

##### _corollary:_ Newton polynomial segments correspond to factors

If $N(f)$ consists of $k$ segments, then $f$ can be factored into at least $k$ polynomials in $\mathbb{Q}_{p}[x]$.

###### _proof sketch:_

If $f(\alpha) = 0$ then the minimal polynomial of $\alpha$ divides $f$. Since there are $k$ $\alpha$s with distinct orders, there are $k$ distinct $p_{\alpha}$s dividing $f$.

---

In fact, there is a partial converse to this as well.

##### _proposition:_ pure and relatively prime slope implies irreducible

If $N(f)$ is pure, running from $(0, 0)$ to $(m, n)$ with $\gcd(m, n) = 1$, then $f$ is irreducible.

###### _proof sketch:_

If $f(x) = g(x) h(x)$ with $g$ of smaller but positive degree, then $N(g)$ would have to be the segment from $(0, 0)$ to $(k, kn / m)$.

---

However, pure doesn't always imply irreducible. For example, $x^{2} + 1 \in \mathbb{Q}_{5}[x]$ has pure Newton polygon (slope $0$, length $2$), but is reducible since $\sqrt{ -1 } \in \mathbb{Q}_{5}$.