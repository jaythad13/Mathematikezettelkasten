---
tags:
- alg-nt
- galois
- comm-alg
- math-177/15
---

Let $A$ be a ring and $A[x]$ be the ring of polynomials over it.

##### _definition:_ irreducible polynomial

A polynomial $f(x) \in A[x]$ is **irreducible** if whenever , one of $g$ and $h$ is constant.

---

### Eisenstein's criterion

When doing algebraic number theory, it can be useful to be able tell that a polynomial is irreducible relatively quickly. Eisenstein's criterion does this. This works over [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domains]] in general.

##### _theorem:_ Eisenstein's criterion

Let $A$ be an integral domain. Suppose $f(x) = \sum_{i = 0}^n a_{i} x^i \in A[x]$, and there exists a [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|prime ideal]] $\mathfrak{p}$ such that $a_{i} \in \mathfrak{p}$ for each $i \neq n$, $a_{n} \not\in \mathfrak{p}$ and $a_{0} \not\in \mathfrak{p}^{2}$. Then $f$ is irreducible.

###### _proof:_

Suppose by way of contradiction that $f(x) = g(x) h(x)$ with non-constant $g, h$. Consider its image $\overline{f}(x) = \overline{a_{n}} x^n \in A / \mathfrak{p}[x]$. Since $\overline{g} \overline{h} = \overline{f}$, we must have that $\overline{g}, \overline{h}$ are both monomials. Since $g$ and $h$ are non-constant, $\overline{g}(0) = \overline{h}(0) = 0 \in A / \mathfrak{p}$, and so $g(0), h(0) \in \mathfrak{p}$. But then $a_{0} = f(0) \in \mathfrak{p}^{2}$, contrary to our assumption that it was not.

---

##### _example:_ a $p$-adic example

Consider $f(x) = (x^p - 1) / (x - 1) = x^{p - 1} + x^{p - 2} + \dots + x + 1$. We claim this is irreducible. This follows because
$$
g(x) = f(x + 1) = \frac{(x + 1)^p - 1}{x} = \sum_{i = 1}^p \binom{p}{i} x^{i - 1}
$$
satisfies Eisenstein's criterion. If we had $f(x) = p(x) q(x)$ reducible, we would have $g(x) = p(x + 1)q(x + 1)$ reducible.

Let $\zeta$ be a root of $f(x)$. Then $\zeta - 1$ is a root of $g(x)$. Then by [[p-adic numbers --- math-177/notes/Extension of norms#_proposition _ extension of norms|extension of the norm]] to $\mathbb{Q}_{p}(\zeta)$ we have $\lvert \zeta - 1 \rvert_{p} = \lvert g(0) \rvert^{1 / {p - 1}} = 1 / p^{1 / (p - 1)}$. That is $\zeta = 1 + \varepsilon$ where $\lvert \varepsilon \rvert_{p}$ is large but less than $1$. Another, way to put this is $\lvert p \rvert_{p} < \lvert \zeta - 1 \rvert_{p} < 1$.

In some sense this tells us that ramification has occurred — we have $\lvert (\zeta - 1)^{p - 1} \rvert_{p} = \lvert p \rvert_{p}$ and so we might have $(p) \subseteq \mathscr{O}_{\mathbb{Q}_{p}(\zeta)}$ not prime anymore.

---