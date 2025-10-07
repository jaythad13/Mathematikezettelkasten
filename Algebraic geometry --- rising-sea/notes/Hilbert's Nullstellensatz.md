---
tags:
- rising-sea/3/2
- alg-geo
- comm-alg
---

Let $\mathbb{F}$ be a field and $A$ a ring.

Hilbert's Nullstellensatz (in its modern formulation) encodes the idea that each closed point of affine space over a field corresponds to gluing together all the Galois conjugates of a finite-degree [[p-adic numbers --- math-177/notes/Algebraic field extensions#_definition _ field extension, degree|(algebraic) field extension]]. In particular, the weak Nullstellensatz says that over an algebraically closed field all the maximal ideals have quotients that are just the base field, and the (strong) Nullstellensatz describes them for any field.

##### _theorem:_ Hilbert's weak Nullstellensatz

If $\mathbb{F} = \overline{\mathbb{F}}$ is an algebraically closed field, then the maximal ideals of $\mathbb{F}[x_{1}, \dots, x_{n}]$ are exactly the ideals $(x_{1} - a_{1}, \dots, x_{n} - a_{n})$ with all $a_{i} \in \mathbb{F}$.

---

##### _theorem:_ Hilbert's (strong) Nullstellensatz or Zariski's lemma

Every maximal ideal of $\mathbb{F}[x_{1}, \dots, x_{n}]$ has a residue field that is a finite extension of $\mathbb{F}$.

---

That is, the strong Nullstellensatz says that every field extension that is finitely generated as an $\mathbb{F}$-algebra is also finitely generated as an $\mathbb{F}$-vector space. This idea is useful enough to deserve a name.

##### _definition:_ finite algebra

An $A$-algebra $B$ is finite if it is finitely generated as an $A$-module.

---

##### _proposition:_ strong Nullstellensatz really is stronger.

The strong Nullstellensatz implies weak Nullstellensatz.

That is, if every finitely generated $\mathbb{F}$-algebra is a finite $\mathbb{F}$-algebra, then every maximal ideal of $\overline{\mathbb{F}}$ is $(x_{1} - a_{1}, \dots, x_{n} - a_{n})$.

###### _proof:_

Suppose $\mathfrak{m}$ is a maximal ideal of $A = \overline{\mathbb{F}}[x_{1}, \dots, x_{n}]$. Then $A / \mathfrak{m}$ is a finite field extension of $\mathbb{F}$. Since it is finite, it must be algebraic (all transcendental extensions have an infinite linearly independent set $1, \pi, \pi^{2}, \dots$). That is, $A / \mathfrak{m} = \overline{\mathbb{F}}$. 

Then under $A \to A / \mathfrak{m}$ we must have $x_{i} \mapsto a_{i} \in \overline{\mathbb{F}}$ for each $i$. It follows that $(x_{1} - a_{1}, \dots, x_{n} - a_{n}) \subseteq \mathfrak{m}$. Since $(x - a_{1}, \dots, x_{n} - a_{n})$ is maximal, it is equal to $\mathfrak{m}$.

---

##### _proposition:_ characterising finite $\mathbb{F}$-algebras

If $A$ is a finite $\mathbb{F}$-algebra and an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]], then $A$ is a field.

Equivalently, a prime ideal $\mathfrak{p} \subseteq \mathbb{F}[x_{1}, \dots, x_{n}]$ is maximal if it has a finite dimensional residue ring $\mathbb{F}[x_{1}, \dots, x_{n}] / \mathfrak{p}$.

###### _proof:_

Let $T_{x} : A \to A$ be the $\mathbb{F}$-linear map by $a \mapsto x a$. Since $A$ is integral, $\ker T_{x} = 0$ for all non-zero $x$. Since $A$ is finite-dimensional over $\mathbb{F}$, $T_{x}$ is then an automorphism with inverse $T_{x}^{-1}$. 

Consider $y = T_{x}^{-1}(1)$. Then $xy = T_{x}(y) = 1$. Thus, each non-zero $x$ has multiplicative inverse $y$ and $A$ is a field.

---