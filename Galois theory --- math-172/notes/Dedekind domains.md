---
tags:
- math-172/9
- alg
- alg-nt
---

Often a domain isn't quite a UFD, but factorisation of the "ideal elements" is unique. For us, these will usually be number rings.

![[Galois theory --- math-172/notes/The ideal class group#_example _ ideal multiplication in $ mathbb{Z}[ sqrt{ -5 }]$|The ideal class group]]

Such rings are called Dedekind domains.

##### _definition:_ Dedekind domain

An integral domain is a **Dedekind domain** if every non-zero proper ideal factors uniquely as a product of prime ideals.

---

In fact, there are many equivalent conditions to be a Dedekind domain which will be useful to us.

##### _proposition:_ equivalent conditions to be a Dedekind domain

For any integral domain $A$ that is not a field, the following conditions are equivalent.
1) $A$ is a Dedekind domain.
2) $A$ is Noetherian, and the localisation $A_{\mathfrak{m}}$ at each maximal ideal $\mathfrak{m} \subseteq A$ is a discrete valuation ring.
3) Every non-zero fractional ideal of $A$ is invertible.
4) $A$ is an integrally closed, Noetherian, and has Krull dimension $1$ (every non-zero prime ideal is maximal).
5) Suppose $\mathfrak{a}, \mathfrak{b} \subseteq A$ are ideals. Then $\mathfrak{a} \subseteq \mathfrak{b}$ if and only if $\mathfrak{b}$ divides $\mathfrak{a}$.

---