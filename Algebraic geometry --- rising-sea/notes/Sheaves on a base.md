---
tags:
- top
- alg-top
- alg-geo
- rising-sea/2/5
---

Let $X$ be a topological space and let $\{ B_{i} \}_{i \in \mathscr{I}}$ be a base on it.

Because the basic gluing blocks of schemes ([[Algebraic geometry --- rising-sea/notes/Affine schemes|affine schemes]]) have a terrible topology (with not-really-describable open sets), we want to be able to define a sheaf on a relatively nice subset of the open sets. We can do this as long as the relatively nice subset forms a [[Topology --- math-147/notes/Bases#_definition _ basis|basis]] of the topology.

First we show that to understand a given sheaf, it suffices to understand it on a basis.

##### _proposition:_ sheaves are base-local

Suppose $\mathscr{F}$ and $\mathscr{G}$ are sheaves on $X$ and $\{ B_{i} \}_{i \in \mathscr{I}}$ is a basis of the topology on $X$. Suppose $\mathscr{F}(B_{i}) = \mathscr{G}(B_{i})$ and $\operatorname{res}_{\mathscr{F}} : \mathscr{F}(B_{i}) \to \mathscr{F}(B_{j})$ is the same as $\operatorname{res}_{\mathscr{G}} : \mathscr{G}(B_{i}) \to \mathscr{G}(B_{j})$ for all $i, j \in \mathscr{I}$. Then $\mathscr{F} = \mathscr{G}$ (all sections and all restriction maps are the same).

---

Morphisms are determined on the base too.

##### _proposition:_ morphisms of sheaves are base-local

Suppose $\mathscr{F}$ and $\mathscr{G}$ are sheaves on $X$ and $\varphi, \psi$ are sheaf morphisms $\mathscr{F} \to \mathscr{G}$. If $\varphi(B_{i}) = \psi(B_{i})$ for all $i \in \mathscr{I}$, then $\varphi = \psi$.

---

This suggests that we should be able to define a sheaf just by specifying its sections on the base.

##### _definition:_ (pre)sheaf on a base

A **sheaf on a base** $\mathscr{F}_\text{base}$ (with values in the category $\mathscr{C}$ with a forgetful functor to $\mathsf{Set}$) consists of **presheaf on a base** (a [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|contravariant functor]] from the poset category of $\{ B_{i} \}_{i \in \mathscr{I}}$ with $B_{j} \subseteq B_{i}$ corresponding to $\operatorname{res}_{i, j} : f_{\mid i} \mapsto f_{\mid j}$) such that the following hold.
1) It satisfies **base identity**: if $B = \bigcup_{i \in \mathscr{J} \subseteq \mathscr{I}} B_{i}$ and $f, g \in \mathscr{F}_\text{base}(B)$ have $f_{\mid i} = g_{\mid i}$ for all $i \in \mathscr{J}$, then $f = g$.
2) Sections are **base-gluable**: if $B = \bigcup_{i \in \mathscr{J} \subseteq \mathscr{I}} B_{i}$ and there are $f_{i} \in \mathscr{F}_\text{base}(B_{i})$ such that $f_{i \mid j} = f_{j \mid i}$ for all $i, j \in \mathscr{J}$, then there exists $f \in \mathscr{F}_\text{base}(B)$ such that $f_{\mid i} = f_{i}$.

---

##### _proposition, definition:_ a sheaf on a base induces a sheaf, induced sheaf

Suppose $\mathscr{F}_\text{base}$ is a sheaf on a base of $X$. Then there is a sheaf $\mathscr{F}$ with isomorphisms $\mathscr{F}(B_{i}) \to \mathscr{F}_\text{base}(B_{i})$ such that the diagram
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(B_{i}) \ar[r] \ar[d, "\mathrm{res}"] & \mathcal{F}_\mathrm{base}(B_{i}) \ar[d, "\mathrm{res}"] \\
		\mathcal{F}(B_{j}) \ar[r] & \mathcal{F}_\mathrm{base}(B_{j}) \\
	\end{tikzcd}
\end{document}
```
We call this sheaf the **induced sheaf** from $\mathscr{F}_{\text{base}}$ and denote it $\mathscr{F}_{\text{base}}^\text{sh}$.

---

##### _proposition:_ a morphism of sheaves on a base induces a sheaf morphism

If $\varphi_{\text{base}} : \mathscr{F}_{\text{base}} \to \mathscr{G}_{\text{base}}$ is a **morphism of sheaves on a base** — that is, $\varphi_{\text{base}}(B_{i}) : \mathscr{F}_{\text{base}}(B_{i}) \to \mathscr{G}_{\text{base}}(B_{i})$, then there is a unique corresponding [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_definition _ morphism of sheaves|morphism of sheaves]] $\varphi_{\text{base}}^\text{sh} : \mathscr{F}_{\text{base}}^\text{sh} \to \mathscr{G}_{\text{base}}^\text{sh}$ with $\varphi_{\text{base}}^\text{sh}(B_{i}) = \varphi_{\text{base}}(B_{i})$.

---

The fancy statement of what we've proven is that there's an [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|equivalence of categories]] between sheaves on $X$ and sheaves on a base on $X$. We note without proof that this equivalence holds for "$\mathscr{O}_{X}$[[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ $ mathscr{O}_{X}$-modules|-modules]] on a base" as well

This equivalence preserves epimorphisms.

##### _proposition:_ epimorphisms of sheaves are base-local

Suppose $\varphi_{\text{base}} : \mathscr{F}_{\text{base}} \to \mathscr{G}_{\text{base}}$ with each $\varphi_{\text{base}}(B_{i})$ surjective, then the corresponding $\varphi_{\text{base}}^\text{sh}$ is an [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ monomorphisms, epimorphisms|epimorphism]].