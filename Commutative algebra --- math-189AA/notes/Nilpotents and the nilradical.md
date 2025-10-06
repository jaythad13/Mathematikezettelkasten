---
tags:
- comm-alg
- math-189AA/3
---

A nilpotent element of a ring is exactly what its name says it is — it powers to $0$.

##### _definition:_ nilpotents

An element $x \in A$ is a **nilpotent** if there is some positive integer $n$ such that $x^n = 0$.

---

##### _example:_ nilpotents modulo $12$

 In $\mathbb{Z}/(12)$, the only non-zero nilpotent element is $6$ (since every nilpotent element must represent some $x \in \mathbb{Z}$ divisible by both $2$ and $3$). Thus, the nilpotent elements are the ideal $(6)$. Note that this is the intersection of the [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|primes]] $(2)$ and $(3)$. This pattern continues in general.

---

##### _definition:_ nilradical

The **nilradical** $\mathfrak{N}_{A}$ (abbreviated to $\mathfrak{N}$ when the ring is clear) of a ring $A$ is the set of all nilpotent elements of a ring.

---

##### _proposition:_ the nilradical is an ideal and the intersection of primes

The nilradical $\mathfrak{N}$ of a ring $A$ is the intersection of all prime ideals $\mathfrak{p} \subseteq A$, and thus, an ideal.

###### _proof:_

Suppose $\mathfrak{p} \subseteq A$ is a prime ideal and $x \in \mathfrak{N}$. Then $x^n = 0 \in \mathfrak{p}$. Thus, by definition of primeness, $x \in \mathfrak{p}$. Thus, $\mathfrak{N} \subseteq \mathfrak{p}$ for every prime $\mathfrak{p}$, and then $\mathfrak{N} \subseteq \bigcap \mathfrak{p}$.

Suppose $x \not\in \mathfrak{N}$. Then $S = \{ 1, x, x^{2}, \dots \}$ does not contain zero. [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_definition _ localisation of a ring, localisations at a prime, fraction field|Thus]], $S^{-1} A$ is not the zero ring. By Zorn's lemma, it contains a maximal, and thus, a prime ideal. But the prime ideals of $S^{-1} A$ [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_proposition _ primes of the localisation are primes that don't meet $S$|are in bijection with]] the prime ideals of $A$ not meeting $S$. Thus, there is a prime in $A$ not containing $x$.

---