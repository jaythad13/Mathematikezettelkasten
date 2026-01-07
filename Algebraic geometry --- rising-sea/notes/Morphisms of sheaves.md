---
tags:
- rising-sea/2/3
- alg-top
- alg-geo
---

Let $X$ be a topological space.

### Categories of sheaves

[[Algebraic geometry --- rising-sea/notes/Sheaves#Sheaves and presheaves|Sheaves]] (and [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ presheaves, sections, restriction maps|presheaves]]) on $X$ with values in a particular category, form a category of their own, once we know what it means for there to be a morphism of sheaves.

##### _definition:_ morphism of sheaves

A **morphism of (pre)sheaves** $\varphi : \mathscr{F} \to \mathscr{G}$ comprises morphisms $\varphi(U) : \mathscr{F}(U) \to \mathscr{G}(U)$ for each open $U \subseteq X$, commuting with restriction morphisms —
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(U) \ar[r, "\varphi(U)"] \ar[d, "\mathrm{res}_{U, V}"] & \mathcal{G}(U) \ar[d, "\mathrm{res}_{U, V}"] \\
		\mathcal{F}(V) \ar[r, "\varphi(V)"] & \mathcal{G}(V)
	\end{tikzcd}
\end{document}
```

Equivalently, a morphism of (pre)sheaves is a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformation]] of the corresponding contravariant functors.

---

It follows from this natural transformation interpretation that (pre)sheaves, with morphisms of sheaves form a category. Note that the composition $\psi \circ \varphi : \mathscr{F} \to \mathscr{G} \to \mathscr{H}$ is defined by $\psi \circ \varphi(U) = \psi(U) \circ \varphi(U)$.

We denote the category of sheaves on $X$ with values in $\mathscr{C}$ by $\mathscr{C}_{X}$ (for example, sheaves of sets form the category $\mathsf{Set}_{X}$) and presheaves on $X$ with values in $\mathscr{C}$ by $\mathscr{C}_{X}^\text{pre}$. We denote the category of $\mathscr{O}_{X}$[[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ $ mathscr{O}_{X}$-modules|-modules]] by $\mathsf{Mod}_{\mathscr{O}_{X}}$.

Since morphisms of sheaves are exactly their morphisms as presheaves, $\mathscr{C}_{X}$ is a [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ faithful, full, fully faithful|full]] [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ subcategory|subcategory]] of $\mathscr{C}_{X}^\text{pre}$.

##### _proposition:_ "stalkification" is functorial

Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ is a morphism of presheaves on $X$ and $p \in X$. Then there is an induced morphism of stalks $\varphi_{p} : \mathscr{F}_{p} \to \mathscr{G}_{p}$ so that $\mathscr{F} \mapsto \mathscr{F}_{p}$ is functorial.

###### _proof:_

Recall that $\mathscr{F}_{p}$ and $\mathscr{G}_{p}$ are the colimits of all $\mathscr{F}(U)$ and $\mathscr{G}(U)$ (respectively) with $U \ni p$. Thus, for all $U \ni p$, there are maps $\mathscr{G}(U) \to \mathscr{G}_{p}$ commuting with the restriction maps. By the definition of a morphism of presheaves, we can extend to $\mathscr{F}(U) \to \mathscr{G}(U) \to \mathscr{G}_{p}$ commuting with the restriction maps on $\mathscr{F}$. Thus, by the universal property of the colimit, there is a natural morphism $\mathscr{F}_{p} \to \mathscr{G}_{p}$ that the $\mathscr{F}(U) \to \mathscr{G}_{p}$ factor through

This is also functorial by the universal property of the colimit — the morphisms $\mathscr{F}(U) \to \mathscr{H}_{p}$ also factor through $\mathscr{F}_{p} \to \mathscr{G}_{p} \to \mathscr{H}_{p}$ and thus the composition is the same as the morphism $\mathscr{F}_{p} \to \mathscr{H}_{p}$.

---

### Sheaf $\operatorname{\mathcal{Hom}}$

The notion of sheaf morphisms allows us to define a sheaf of sheaf morphisms, called sheaf $\operatorname{\mathcal{Hom}}$. (Sheaves don't always form an additive category, but sheaf $\operatorname{\mathcal{Mor}}$ sounds worse).

##### _definition:_ sheaf $\operatorname{\mathcal{Hom}}$

Suppose $\mathscr{F}$ and $\mathscr{G}$ are (pre)sheaves on $X$ taking values in the category $\mathscr{C}$. Then their **sheaf $\operatorname{\mathit{Hom}}$** is $\operatorname{\mathcal{Hom}}_{\mathscr{C}_{X}}(\mathscr{F}, \mathscr{G})$, the sheaf (of sets) defined by
$$
\operatorname{\mathcal{Hom}}_{\mathscr{C}_{X}}(\mathscr{F}, \mathscr{G})(U) = \operatorname{Mor}_{\mathscr{C}_{U}}(\mathscr{F}_{\mid U}, \mathscr{G}_{\mid U}).
$$
We drop the subscript when $\mathscr{C}_{X}$ is clear.

---

It needs verifying that when $\mathscr{F}, \mathscr{G}$ are sheaves that $\operatorname{\mathcal{Hom}}(\mathscr{F}, \mathscr{G})$ is a sheaf. Morphisms of presheaves restrict to morphisms of restricted presheaves, so $\operatorname{\mathcal{Hom}}(\mathscr{F}, \mathscr{G})$ is at least a presheaf with restriction $\varphi_{\mid U} \mapsto \varphi_{\mid V}$ by $\varphi_{\mid V}(W) = \varphi_{\mid U}(W)$. 

If $\varphi_{i} : \mathscr{F}_{\mid U_{i}} \to \mathscr{G}_{\mid U_{i}}$ are sheaf morphisms that agree on restriction to each $U_{i} \cap U_{j}$, we can glue them to get $\varphi : \mathscr{F}_{\mid U} \to \mathscr{G}_{\mid U}$ by $(\varphi(U) s)_{\mid U_{i}} = \varphi(U_{i}) s_{\mid U_{i}}$ for $s \in \mathscr{F}(U_{i})$. These sections glue to a unique $\varphi(U) s \in \mathscr{G}(U)$ since $\mathscr{G}$ is a sheaf.

Note that $\operatorname{\mathcal{Hom}}$/$\operatorname{Hom}$ does not commute with taking stalks. That is, $\operatorname{\mathcal{Hom}}(\mathscr{F}, \mathscr{G})_{p} \not \cong \operatorname{Hom}(\mathscr{F}_{p}, \mathscr{G}_{p})$.

##### _examples:_ sheaf $\operatorname{\mathcal{Hom}}$

1) If $\mathscr{F}$ is a sheaf of sets on $X$, then $\operatorname{\mathcal{Hom}}_{\mathsf{Sets}_{X}}(\underline{\{ e \}}, \mathscr{F}) \cong \mathscr{F}$. This is because $\operatorname{Mor}(\{ e \}, \mathscr{F}(U))$ is canonically isomorphic to $\mathscr{F}(U)$ (since $\{ e \}$ only has one element, we have $\underline{\{ e \}}(U) \cong \{ e \}$ canonically as well).
2) If $\mathscr{F}$ is an $\mathscr{O}_{X}$[[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ $ mathscr{O}_{X}$-modules|-module]], then $\operatorname{\mathcal{Hom}}_{\mathsf{Mod}_{\mathscr{O}_{X}}}(\mathscr{O}_{X}, \mathscr{F}) \cong \mathscr{F}$. Again, this is because $\operatorname{Hom}(\mathscr{O}_{X}(U), \mathscr{F}(U)) \cong \mathscr{F}(U)$. When $\mathscr{F}$ is just a sheaf of abelian groups, [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_example _ sheaves of abelian groups are $ mathscr{O}_{X}$-modules|and thus]], a $\underline{\mathbb{Z}}$-module, we have $\operatorname{\mathcal{Hom}}(\underline{\mathbb{Z}}, \mathscr{F}) \cong \mathscr{F}$.

---