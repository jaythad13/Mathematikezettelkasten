---
tags:
- math-172/3
- alg
- rep-th
---

Let $G$ be a finite group, let $\mathbb{F}$ be a field.

##### _definition:_ representations of finite groups, degree

A **finite dimensional (linear) representation of a finite group** $G$ is a finite $\mathbb{F}$-dimensional $\mathbb{F}[G]$[[Representation theory --- math-174/notes/Modules over a rng#_definition _ modules over a rng|-module]] $M$. Morphisms of representations are [[Representation theory --- math-174/notes/Modules over a rng#_definition _ module homomorphisms, isomorphisms|homomorphisms]] of $\mathbb{F}[G]$-modules. 

More generally, the category of ($\mathbb{F}$-linear) representations of $G$ is $\operatorname{\mathsf{Rep}_{\mathbb{F}}} G$ and is isomorphic to $\mathsf{finMod}_{\mathbb{F}[G]}$, the category of finite $\mathbb{F}$-dimensional $\mathbb{F}[G]$-modules.

Note, an $\mathbb{F}[G]$-module $M$ is equivalent to a group homomorphism $\rho : G \to \mathrm{GL}(V)$ where $V$ is the $\mathbb{F}$-module structure on $M$.

The **degree** of a representation is the $\mathbb{F}$-dimension of $V$.

---

This second equivalent definition will be very convenient for us.

The equivalence follows since $G \subseteq \mathbb{F}[G]^\times$, so the image of $G$ lies in the units of $\operatorname{End} V$, which are just $\mathrm{GL}(V)$. Since $\mathbb{F}[G]$ is just linear combinations of $G$, this data recovers the original $\mathbb{F}[G] \to \operatorname{End}_{\mathsf{Ab}} M$ by extending $\mathbb{F}$-linearly (using the $\mathbb{F}$-module structure we have on $M =_{\mathsf{Ab}} V$).

The notion of degree has something to do with the degree of the characteristic polynomial of an irreducible representation.

Lots of words that are adjectives for $\mathbb{F}[G]$-modules are also adjectives for representations of $G$. For example, [[Representation theory --- math-174/notes/Modules over a rng#_definition _ irreducible modules|irreducible]] is the same, submodule becomes subrepresentation, et c.

##### _example:_ the permutation representation of $\mathfrak{S}_{2}$.

Let $\mathfrak{S}_{2}$ be the symmetric group acting on the set of the standard basis of $\mathbb{C}^{\oplus 2}$. Then this gives a [[Representation theory --- math-174/notes/Modules over a rng#_example _ modules over group rings, or the fundamental representation-theoretic example, or permutation modules|permutation representation]] $\mathfrak{S}_{2} \to \mathrm{GL}(\mathbb{C}^{\oplus 2}) \to \mathrm{GL}_{2}(\mathbb{C})$. 

We can get an equivalent representation with a different choice of basis $(1, 1), (1, -1)$. Then $\rho(g)$ is always a diagonal matrix. In particular $\rho(g) = 1$ and $\rho((1 \, 2)) = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.

This basis allows us to see that this representation is made of two different subrepresentations — we have two different one-dimensional $\mathbb{C}[G]$-submodules whose direct sum is the whole $\mathbb{C}[G]$-module.

---
