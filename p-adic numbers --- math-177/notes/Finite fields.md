---
tags:
- alg
- math-177/18
---

There are "surprisingly few" finite fields. That is, we can classify them all in a nice way.

Suppose $\mathbb{F}$ is a finite field. Recall the notion of characteristic

##### _definition:_ characteristic

The characteristic of a ring $A$ is $\operatorname{char} A = \min \{ n \mid \underbrace{1 + \dots + 1}_{n \text{ times}} = 0 \}$.

---

Note that if $\mathbb{F}$ is finite, it must have finite characteristic. In fact, we can do even better.

##### _proposition:_ finite fields have prime characterstic

A finite field must have [[Superdiscrete --- math-55A/notes/Prime numbers#_definition _ prime numbers|prime]] characteristic $p$.

###### _proof:_

Let $A$ be a finite ring of characteristic $n$. Write elements of the image of $\mathbb{Z}$ as $n, k, \ell$ et c. Write $n = k \ell$. Then $k \ell = 0$. If $k, \ell < n$, then $k, \ell \neq 0$ by minimality of the characteristic $n$. Thus, $k, \ell$ become zero-divisors.

Suppose $A$ is a field. Then it has no zero-divisors. Thus, its characteristic has no pair of divisors both less than it. Equivalently, its characteristic is prime.

---

##### _corollary:_ every finite field is a finite extension of $\mathbb{F}_{p}$

###### _proof sketch:_

Notice that $\mathbb{Z} \to \mathbb{F}$ has kernel $(p)$, and so $\mathbb{Z} / (p) \to \mathbb{F}$ is a map. [[Abstract algebra --- math-171/notes/Ideals and quotients#_corollary _ fields map out injectively|It is an injection]].

---

##### _proposition:_ 

A degree $k$ finite field extension $\mathbb{F} / \mathbb{F}_{p}$ has size $\# \mathbb{F} = p^k$.

---

##### _theorem:_ characterising finite fields

Every finite field $\mathbb{F}$ is a finite degree $k$ extension of $\mathbb{F}_{p}$ and the [[p-adic numbers --- math-177/notes/Algebraic field extensions#_definition _ splitting field|splitting field]] of $x^{p^k - 1} - 1$.

###### _proof:_

The previous result implies, $\# \mathbb{F}^\times = p^k - 1$. It follows by [[Abstract algebra --- math-171/notes/Lagrange's theorem#_theorem _ Lagrange's theorem|Lagrange's theorem]] that every element of $\mathbb{F}^\times$ has order dividing $p^k - 1$, and thus is a root of $x^{p^k - 1} - 1 = 0$.

These are in fact all the roots of $x^{p^k - 1} - 1$ (it has at most $p^k - 1$ roots).

---

##### _corollary:_ finite field extensions of given degree are unique
