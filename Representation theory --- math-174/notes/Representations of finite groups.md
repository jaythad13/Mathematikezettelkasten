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

There is a final equivalent definition from interpreting $G$ as a [[Algebraic geometry --- rising-sea/notes/Categories#_example _ every group is an entire category, groupoids, monoids, the fundamental groupoid|one object category]] $\mathscr{G}$. Then $\mathbb{F}$-linear representations of $G$ are just [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|functors]] $\mathscr{G} \to \mathsf{Vect}_{\mathbb{F}}$. If $V$ is the vector space on which the representation acts, then the one object of $\mathscr{G}$ is sent to $V$. Morphisms of representations are just [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformations]] of those functors. A morphism from $\rho : G \to \mathrm{GL}(V)$ to $\pi : G \to \mathrm{GL}(W)$ is just a morphism $T : V \to W$ such that the diagram below commutes for each $g \in G$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		V \ar[r, "\rho(g)"] \ar[d, "T"] & V \ar[d, "T"] \\
		W \ar[r, "\pi(g)"] & W
	\end{tikzcd}
\end{document}
```
If $T$ is an isomorphism of vector spaces, then it is an isomorphism of representations. Thus, an isomorphism of representations expresses $\pi(g) = T \rho(g) T^{-1}$ for each $g$, where $T$ is a change of basis matrix (not depending on $g$).

The etymology of degree for the dimension of $V$ has something to do with the degree of the characteristic polynomial of an irreducible representation.

Lots of words that are adjectives for $\mathbb{F}[G]$-modules are also adjectives for representations of $G$. For example, [[Representation theory --- math-174/notes/Modules over a rng#_definition _ irreducible modules|irreducible]] is the same, submodule becomes subrepresentation, et c.

##### _example:_ the permutation representation of $\mathfrak{S}_{2}$.

Let $\mathfrak{S}_{2}$ be the symmetric group acting on the set of the standard basis of $\mathbb{C}^{\oplus 2}$. Then this gives a [[Representation theory --- math-174/notes/Modules over a rng#_example _ modules over group rings, or the fundamental representation-theoretic example, or permutation modules|permutation representation]] $\mathfrak{S}_{2} \to \mathrm{GL}(\mathbb{C}^{\oplus 2}) \to \mathrm{GL}_{2}(\mathbb{C})$. 

We can get an equivalent representation with a different choice of basis $(1, 1), (1, -1)$. Then $\rho(g)$ is always a diagonal matrix. In particular $\rho(g) = 1$ and $\rho((1 \, 2)) = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.

This basis allows us to see that this representation is made of two different subrepresentations — we have two different one-dimensional $\mathbb{C}[G]$-submodules whose direct sum is the whole $\mathbb{C}[G]$-module.

---
