---
tags:
- alg-top
- alg
- uc-2026/alg-top/6
- peter-may
---

We want to prove Bott periodicity. Along the way, we will come across the cohomology of $B\mathrm{U}_{n}$. We will see that due to properties of Chern classes of bundles, we see that $H^\bullet(B\mathrm{U}_{n}, \mathbb{Z}) = \mathbb{Z}[c_{1}, \dots, c_{n}]$ has a comultiplication $H^\bullet(B\mathrm{U}_{n}, \mathbb{Z}) \to H^\bullet(B\mathrm{U}_{n}, \mathbb{Z}) \otimes H^\mathrm{\bullet}(B \mathrm{U}_{n}, \mathbb{Z})$ by $c_{n} \mapsto \sum_{i + j = n} c_{i} \otimes c_{j}$. This sends the Chern class of a vector bundle $\mathscr{V}$ on $B\mathrm{U}_{n}$ to the Chern class of the external direct sum $\mathscr{V} \times \mathscr{V}$ on $B \mathrm{U}_{n} \times B \mathrm{U}_{n}$. Something similar is true for $B \mathrm{O}_{n}$ too.

We want to have the algebraic machinery to understand this phenomenon. Specifically, we want to show that this Hopf algebra is self-dual, giving a ring structure on homology.

### Graded algebras

Suppose $R_{\bullet}$ is a (non-negatively) [[Algebraic geometry --- rising-sea/notes/Graded rings#_definition _ $ mathbb{Z}$-graded rings, homogeneous elements, degree|graded ring]]. Then we want to grade $R_{\bullet}$-modules and $R_{\bullet}$-algebras and $R_{\bullet}$-coalgebras in a way that is compatible. Here, we use algebro-topological conventions.

##### _definition:_ graded modules, graded tensor products, graded $\operatorname{Hom}$s, duals

A **graded $R_{\bullet}$-module** $M_{\bullet}$ is a set of modules $M_n$ for each $n \geq 0$.

The **graded tensor product** of graded $R_{\bullet}$-modules $M_{\bullet}$ and $N_{\bullet}$ is given by $(M \otimes N)_{\bullet} = \bigoplus_{i + j = n} M_{i} \otimes N_{j}$.

The **graded $\operatorname{Hom}$-set** of graded $R_{\bullet}$-modules $M_{\bullet}$ and $N_{\bullet}$ is given by $\operatorname{Hom}(M, N)_{\bullet} = \prod_{i}(M_{i}, N_{i + n})$.

For a graded $R_{\bullet}$-module $M_{\bullet}$ we define its dual $M^{\vee}_{\bullet}$ so that $M^{\vee}_{n}$ is a

---

Note that in algebraic topology, the graded modules is not the direct sum of the degree $i$ components. Rather

##### _definition:_ graded algebras

A **graded $R_{\bullet}$-algebra** $A_{\bullet}$ (not necessarily commutative) is an $R_{\bullet}$-module with an associative, unital multiplication $\mu : S_{\bullet} \otimes S_{\bullet} \to S_{\bullet}$ respecting the grading. We usually denote the unit $R_{\bullet} \to S_{\bullet}$ by $\eta$.

We say $A_{\bullet}$ is **graded commutative** if $\mu(f \otimes g) = (-1)^{\deg f \deg g} \mu(g \otimes f)$.

---

### Coalgebras, bialgebras, and Hopf algebras

##### _definition:_ graded coalgebras

A **graded $R_{\bullet}$-coalgebra** $A_{\bullet}$ is an $R_{\bullet}$-module with an coassociative, counital comultiplication $\psi : A_{\bullet} \to A_{\bullet} \otimes A_{\bullet}$ with counit given by $\varepsilon : A_{\bullet} \to R_{\bullet}$ respecting the grading.

---

Since every topological space $X$ has a diagonal map $\delta : X \to X \times X$, the Künneth formula means that the homology of every space is a coalgebra.

##### _definition:_ augmented, coaugmented, indecomposable elements

Suppose $R_{\bullet}$ is a graded ring with the trivial grading (all degree $0$). An $R$-algebra $A$ is **augmented** if there exists a map of $R$-algebras

---

##### _definition:_ bialgebras, graded bialgebras, Hopf algebras

$A$ is a an **$R$-bialgebra** if it is both an algebra and a coalgebra, such that $\varepsilon$ is an augmentation, $\eta$ is a coaugmentation, $\mu$ is a map of coalgebras, and $\psi$ is a map of algebras.

$A_{\bullet}$ is a graded **$R_{\bullet}$-bialgebra** if it is both a graded algebra and a graded coalgebra.

---

##### _example:_ bialgebras

$\mathbb{F}[x]$ is a bialgebra with $\psi : x \mapsto x \otimes x$. $\mathbb{F}(x)$ is a Hopf algebra with the same map.

---