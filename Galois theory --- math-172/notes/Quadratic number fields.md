---
tags:
- alg-nt
- math-172/6
---

Galois theory is about finding roots to polynomials. The simplest case is that of quadratic number fields.

##### _definition:_ (real, imaginary) quadratic number fields

A **quadratic number field** is $\mathbb{Q}[\sqrt{ d }]$ for some square free $d \in \mathbb{Q}$.

Equivalently, it is a [[Transcendental number theory --- math-195/notes/Number fields#_definition _ number field|number field]] of degree $2$.

If $d > 0$, then $\mathbb{Q}[\sqrt{ d }]$ is a **real quadratic number field**. Else, $\mathbb{Q}[\sqrt{ d }]$ is an **imaginary quadratic field**.

---

Note, $\mathbb{Q}[\sqrt{ d }]$ is in fact a field. It's a domain ($x^{2} - d$ is irreducible and thus, prime), finite-dimensional over $\mathbb{Q}$. Since multiplication by any number is $\mathbb{Q}$-linear and injective, multiplication by any number has an inverse.

![[Algebraic geometry --- rising-sea/notes/Integral dependence and integral homomorphisms#_example _ quadratic integer rings|Integral dependence and integral homomorphisms]]

### Imaginary quadratic number fields

##### _definition:_ norm

Suppose $\mathbb{Q}(\sqrt{ d })$ is an imaginary quadratic number field. Suppose $\alpha = a + b \sqrt{ d }$.

The **norm** is $N : \mathscr{O}_{\mathbb{Q}(\sqrt{ d })} \to \mathbb{Z}$ by $\alpha \mapsto a^{2} - b^{2} d$. It is multiplicative and positive definite.

---

This is a useful definition!

##### _proposition:_ characterising units in an imaginary quadratic number field

Suppose $\mathbb{K}$ is an imaginary quadratic number field. Then $\alpha \in \mathscr{O}_{\mathbb{K}}$ is a unit if and only if $N(\alpha) = 1$.

###### _proof:_

Suppose $N(\alpha) = \alpha  \overline{\alpha} = 1$. Then, by definition $\alpha$ is a unit.

Suppose $\alpha$ is a unit. Then $N(\alpha \alpha ^{-1}) = N(\alpha) N(\alpha ^{-1}) = 1$. Thus, $N(\alpha)$ is a unit. Since $N$ is positive definite, $N(\alpha) = 1$.

---

This also controls the splitting of prime integers into non-primes in higher number fields.

##### _example:_ $3$ is a prime in the Gaussian integers, $5$ splits, and $2$ is ramified

If $3 = \alpha \beta$ is a non-trivial factorisation in $\mathbb{Z}[i]$, then we would have $N(3) = N(\alpha) N(\beta)$, and thus, $9 = N(\alpha) N(\beta)$. By unique factorisation, we must have $N(\alpha) = 3$, but there are no integer solutions to $a^{2} + b^{2} = 3$.

Conversely, $(2 + i)(2 - i) = 5$.

What's even weirder is that $2 = (1 + i)(1 - i)$ and these two factors are in fact associates.

---