---
tags:
- alg
- math-172/1
- math-172/2
---

Let $A$ be a (commutative, unital) ring.

##### _definition:_ polynomial ring

The **polynomial ring (in one variable) over $A$** is $A[x]$, the ring of functions $\mathbb{N}_{0} \to A$ by $n \mapsto a_{n}$ written as polynomials $a_{0} + a_{1} x + \dots + a_{n} x^n$. The multiplication is the obvious convolution product
$$
(a_{0} + a_{1} x + \dots + a_{n} x^n)(b_{0} + b_{1} x + \dots + b_{m} x^m) = \sum_{i = 0}^n \left( \sum_{j + k = i} a_{j} b_{k}  \right) x^i.
$$

It is the [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?|universal]] $A$-algebra such that, for each $b \in B \in \mathsf{Alg}_{A}$, there is a unique $A$-algebra homomorphism $A[x] \to B$. In our construction it's just the structure map $A \to B$ extended by $x \mapsto b$. That is, it [[Algebraic geometry --- rising-sea/notes/Yoneda's lemma#_definition _ representable functor|(co)represents]] the covariant forgetful functor $\mathsf{Alg}_{A} \to \mathsf{Set}$.

It is a [[Algebraic geometry --- rising-sea/notes/Graded rings#_definition _ $ mathbb{Z}$-graded rings, homogeneous elements, degree|non-negatively graded ring]] with degree given by the largest $n$ such that $a_{n} \neq 0$.
 
The **polynomial ring in $n$ variables over $A$** is $A[x_{1}, \dots, x_{n}] = A[x_{1}, \dots, x_{n - 1}][x]$. It corepresents the covariant functor $\mathsf{Alg}_{A} \to \mathsf{Set}$ by $B \mapsto \prod_{i = 1}^n B$.

---

There is a natural inclusion $A \subseteq A[x]$. Also, for each $a \in A$ there is an evaluation map $A[x] \to A$ by $f(x) \mapsto f(a)$. More generally, for each choice of $a_{1}, \dots, a_{n} \in A$ there is an evaluation homomorphism $A[x_{1}, \dots, x_{n}] \to A$.

Polynomial rings are not generally [[Abstract algebra --- math-171/notes/Unique factorisation#_definition _ Euclidean domain|Euclidean domains]], even when they are over a Euclidean domain. For example, $\mathbb{Z}[x]$ has non-principal ideal $(2, x)$ and so is not Euclidean. However, they have something pretty close to a division algorithm when the divisor is monic.

##### _proposition:_ division with remainder

If $f, g \in A[x]$ are monic polynomials, then there is a unique division of $g$ by $f$ with remainder $r$ — there is a unique $q \in A[x]$ and $r \in A[x]$ such that $g(x) = f(x) q(x) + r(x)$ with $\deg r < \deg f$.

---

##### _corollary:_ factor theorem

Suppose $a \in A$ and $g \in A[x]$. Then $g(a) = 0$ if and only if $x - a$ divides $g$.

###### _proof:_

Apply division with remainder to divisor $x - a$. The remainder is always $g(a)$.

---

##### _corollary:_ multivariate factor theorem

Suppose $f \in A[x_{1}, \dots, x_{n - 1}]$ and $g \in A[x_{1}, \dots, x_{n}]$.

---

