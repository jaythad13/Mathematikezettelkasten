---
tags:
- top
- alg-top
- alg-geo
- rising-sea/2/5
---

Let $X$ be a topological space and let $\{ B_{i} \}_{i \in \mathscr{I}}$ be a base on it. We will use $\mathscr{I}$ and $\mathscr{J}$ to denote not just index sets, but the data of full subcategories of the inclusion category of open sets of $X$ (so that we can take limits over them).

Because the basic gluing blocks of schemes ([[Algebraic geometry --- rising-sea/notes/Affine schemes|affine schemes]]) have a terrible topology (with not-really-describable open sets), we want to be able to define a sheaf on a relatively nice subset of the open sets. We can do this as long as the relatively nice subset forms a [[Topology --- math-147/notes/Bases#_definition _ basis|basis]] of the topology.

First we show that to understand a given sheaf, it suffices to understand it on a basis.

##### _proposition:_ sheaves are base-local

Suppose $\mathscr{F}$ and $\mathscr{G}$ are sheaves on $X$. Suppose $\mathscr{F}(B_{i}) = \mathscr{G}(B_{i})$ and $\operatorname{res}_{\mathscr{F}} : \mathscr{F}(B_{i}) \to \mathscr{F}(B_{j})$ is the same as $\operatorname{res}_{\mathscr{G}} : \mathscr{G}(B_{i}) \to \mathscr{G}(B_{j})$ for all $i, j \in \mathscr{I}$. Then $\mathscr{F} = \mathscr{G}$ (we have $\mathscr{F}(U) = \mathscr{G}(U)$ and $\operatorname{res}_{\mathscr{F}, U, V} = \operatorname{res}_{\mathscr{G}, U, V}$ for all open $U, V \subseteq X$).

###### _proof:_

Consider open subsets $V \subseteq U \subseteq X$. Suppose that $U = \bigcup_{i \in \mathscr{I}} B_{i}$. [[Algebraic geometry --- rising-sea/notes/Sheaves#_proposition _ identity and gluability axioms as a limit|Recall]] then that
$$
\mathscr{F}(U) = \lim_{i \in \mathscr{I}} \mathscr{F}(B_{i}) = \lim_{i \in \mathscr{I}} \mathscr{G}(B_{i}) = \mathscr{G}(U).
$$
Here $\mathscr{I}$ includes not only all the $B_{i}$ covering $U$ but also the data of the basic opens covering their intersections, and the data of the basic opens covering intersections of those basic opens and so on. Similarly, $\mathscr{F}(V) = \mathscr{G}(V)$.

Choosing open covers $U = \bigcup_{i \in \mathscr{I}} B_{i}$ and $V = \bigcup_{j \in \mathscr{J}} B_{j}$ and considering all $\operatorname{res}_{i, j} : \mathscr{F}(B_{i}) \to \mathscr{F}(B_{j})$, we get a unique map of their limits $\mathscr{F}(U) \to \mathscr{F}(V)$ so that
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(U) \ar[r] \ar[d] & \mathcal{F}(V) \ar[d] \\
		\mathcal{F}(B_{i}) \ar[r] & \mathcal{F}(B_{j})
	\end{tikzcd}
\end{document}
```
commutes. Both $\operatorname{res}_{\mathscr{F}, U, V}$ and $\operatorname{res}_{\mathscr{G}, U, V}$ are such maps, and thus, must be the same.

---

Morphisms are determined on the base too.

##### _proposition:_ morphisms of sheaves are base-local

Suppose $\mathscr{F}$ and $\mathscr{G}$ are sheaves on $X$ and $\varphi, \psi$ are sheaf morphisms $\mathscr{F} \to \mathscr{G}$. If $\varphi(B_{i}) = \psi(B_{i})$ for all $i \in \mathscr{I}$, then $\varphi = \psi$.

###### _proof:_

We want to show that $\varphi(U) = \psi(U)$ for each open $U \subseteq X$. Consider $\mathscr{F}(U)$ and $\mathscr{G}(U)$ as limits $\lim_{i \in \mathscr{I}} \mathscr{F}(B_{i})$ and $\lim_{ i \in \mathscr{I} } \mathscr{G}(B_{i})$. Then the $\varphi(B_{i}) = \psi(B_{i})$ define a unique map $\theta(U) = \mathscr{F}(U) \to \mathscr{G}(U)$ so that
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(U) \ar[rr, "\theta(U)"] \ar[d, "\mathrm{res}"] & & \mathcal{G}(U) \ar[d, "\mathrm{res}"] \\
		\mathcal{F}(B_{i}) \ar[rr, "\varphi(B_{i}) = \psi(B_{i})"] & & \mathcal{G}(B_{i})
	\end{tikzcd}
\end{document}
```
commutes. Since $\varphi(U)$ and $\psi(U)$ are both such maps, we have $\varphi(U) = \psi(U)$.

---

This tells us that we can uniquely recover sheaves and their morphisms from a base. But do all "sheaves on a base" come from an honest sheaf? Yes!

##### _definition:_ sheaves on a base, presheaves on a base

A **sheaf on a base** $\mathscr{F}_\text{b}$ (with values in the category $\mathscr{C}$ with a forgetful functor to $\mathsf{Set}$) consists of **presheaf on a base** (a [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|contravariant functor]] from the poset category of $\{ B_{i} \}_{i \in \mathscr{I}}$ with $B_{j} \subseteq B_{i}$ corresponding to $\operatorname{res}_{i, j} : f_{\mid i} \mapsto f_{\mid j}$) such that the following hold.
1) It satisfies **base identity**: if $B = \bigcup_{i \in \mathscr{J} \subseteq \mathscr{I}} B_{i}$ and $f, g \in \mathscr{F}_\text{b}(B)$ have $f_{\mid i} = g_{\mid i}$ for all $i \in \mathscr{J}$, then $f = g$.
2) Sections are **base-gluable**: if $B = \bigcup_{i \in \mathscr{J} \subseteq \mathscr{I}} B_{i}$ and there are $f_{i} \in \mathscr{F}_\text{b}(B_{i})$ such that $f_{i \mid j} = f_{j \mid i}$ for all $i, j \in \mathscr{J}$, then there exists $f \in \mathscr{F}_\text{b}(B)$ such that $f_{\mid i} = f_{i}$.

---

##### _proposition, definition:_ a sheaf on a base induces a sheaf, induced sheaf

Suppose $\mathscr{F}_\text{b}$ is a sheaf on a base of $X$. Then there is a sheaf $\mathscr{F}$ (unique up to unique isomorphism) with isomorphisms $\mathscr{F}(B_{i}) \to \mathscr{F}_\text{b}(B_{i})$ such that the diagram
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(B_{i}) \ar[r] \ar[d, "\mathrm{res}"] & \mathcal{F}_\mathrm{b}(B_{i}) \ar[d, "\mathrm{res}"] \\
		\mathcal{F}(B_{j}) \ar[r] & \mathcal{F}_\mathrm{b}(B_{j}) \\
	\end{tikzcd}
\end{document}
```
We call this sheaf the **induced sheaf** from $\mathscr{F}_{\text{b}}$ and denote it $\mathscr{F}_{\text{b}}^\text{sh}$.

###### _proof:_

Choose $\mathscr{F}(U) = \lim_{ j \in \mathscr{J} }\mathscr{F}_{\text{b}}(B_{j})$ where $U = \bigcup_{j \in \mathscr{J}} B_{j}$. Suppose $U = \bigcup_{i \in \mathscr{I}} U_{i}$. Then to show $\mathscr{F}$ is a sheaf is to show $\mathscr{F}(U) = \lim_{ i \in \mathscr{I} } \mathscr{F}(U_{i})$. Note that this also sort of shows that our definition does not depend on the choice of basic cover of $U$. (Essentially, given two different basic covers of $U$, consider a basic open cover refining them both. The limits over each basic cover are uniquely isomorphic to the limit over the basic cover refining them both).

Choose basic covers $U_{i} = \bigcup_{i_{j} \in \mathscr{I}_{\mathscr{J}}} B_{i_{j}}$. Then $\mathscr{F}(U_{i}) = \lim_{ i_{j} \in \mathscr{I}_{\mathscr{J}} } \mathscr{F}(B_{i_{j}})$ and $\mathscr{F}(U) = \lim_{ i \mathscr{I}, i_{j} \in \mathscr{I}_{\mathscr{J}} } \mathscr{F}(B_{i_{j}})$. But then $\mathscr{F}(U)$ has unique maps $\mathscr{F}(U) \to \mathscr{F}(U_{i})$ that $\mathscr{F}(U) \to \mathscr{F}(B_{i_{j}})$ factor through. By this uniqueness, the maps $\mathscr{F}(U) \to \mathscr{F}(U_{j})$ and $\mathscr{F}(U) \to \mathscr{F}(U_{i}) \to \mathscr{F}(U_{j})$ are the same. That is, the maps commute with restriction.

Now we show $\mathscr{F}(U)$ satisfies the universal property of the limit. Suppose $A$ has maps to each $\mathscr{F}(U_{i})$ commuting with restriction. Then, using further restriction maps $A$ has maps to each $\mathscr{F}(B_{i_{j}})$ commuting with their restrictions. Thus, $A$ has a unique map to $\mathscr{F}(U)$ commuting with the restrictions among $\mathscr{F}(B_{i_{j}})$. But any map $A \to \mathscr{F}(U)$ that commutes with the restrictions among $\mathscr{F}(U_{i})$ also commutes with the restrictions among $\mathscr{F}(B_{i_{j}})$. That is, the map $A \to \mathscr{F}(U)$ is also the unique map commuting with the restrictions among $\mathscr{F}(U_{i})$, or $\mathscr{F}(U)$ satisfies the universal property of the limit.

---

##### _proposition:_ a morphism of sheaves on a base induces a sheaf morphism

If $\varphi_{\text{b}} : \mathscr{F}_{\text{b}} \to \mathscr{G}_{\text{b}}$ is a **morphism of sheaves on a base** — that is, $\varphi_{\text{b}}(B_{i}) : \mathscr{F}_{\text{b}}(B_{i}) \to \mathscr{G}_{\text{b}}(B_{i})$, then there is a unique corresponding [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_definition _ morphism of sheaves|morphism of sheaves]] $\varphi_{\text{b}}^\text{sh} : \mathscr{F}_{\text{b}}^\text{sh} \to \mathscr{G}_{\text{b}}^\text{sh}$ with $\varphi_{\text{b}}^\text{sh}(B_{i}) = \varphi_{\text{b}}(B_{i})$.

###### _proof sketch:_

Choose $\varphi(U)$ to be the limit morphism $\mathscr{F}(U) \to \mathscr{G}(U)$ where each value of sheaves is thought of as the limit of the values of the sheaf on a basic cover. Given $V \subseteq U$, $\mathscr{F}(U) \to \mathscr{G}(U) \to \mathscr{G}(V)$ and $\mathscr{F}(U) \to \mathscr{F}(V) \to \mathscr{G}(V)$ are both maps commuting with restrictions to $\mathscr{G}(B_{i})$ on a basic open cover of $V$. By the universal property of the limit there is a unique such map and so they are the same. That is, $\varphi(U)$ defines a sheaf morphism.

Uniqueness follows since we showed sheaf morphisms are base-local.

---

The fancy statement of what we've proven is that there's an [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|equivalence of categories]] between sheaves on $X$ and sheaves on a base on $X$. We note without proof that this equivalence holds for "$\mathscr{O}_{X}$[[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ $ mathscr{O}_{X}$-modules|-modules]] on a base" as well.

##### _proposition:_ epic morphisms on a base implies epic sheaf morphisms

Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ has each $\varphi(B_{i})$ epic.Then then the corresponding $\varphi$ is an [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ monomorphisms, epimorphisms|epimorphism]].

###### _proof:_

Suppose $\psi, \theta : \mathscr{G} \to \mathscr{H}$ are two morphisms such that the compositions $\mathscr{F} \to \mathscr{G} \to \mathscr{H}$ agree. Then $\psi(B_{i}) \circ \varphi(B_{i}) = \theta(B_{i}) \circ \varphi(B_{i})$ for each basic $B_{i}$. Since $\varphi(B_{i})$ is epic, $\psi(B_{i}) = \theta(B_{i})$ for each $B_{i}$, and since sheaf morphisms are base local, we have $\psi = \theta$.

---

### Stalks are base-local

We did everything above by limit arguments, but these are a little bit sketchy because we're taking limits over diagrams that could be ridiculously large (still sets, but certainly uncountable). In practice, because the [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets|typical basis]] for the Zariski topology on a scheme is closed under intersections, these arguments will work without having to worry even a little. However, there's a different way to do this — all stalk-local properties of a sheaf are in fact base-local, and thus we can determine stalks and [[Algebraic geometry --- rising-sea/notes/Stalk-local properties and compatible germs#_definition _ compatible germs|compatibility of germs]] on a basis. This allows us to recover all sections of a sheaf from its values on a basis and a whole sheaf from values on a basis satisfying base identity and gluability as above.