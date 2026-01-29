---
tags:
- rising-sea/2/4/4
- alg-geo
- alg-top
---

Every sheaf is a presheaf, and in fact, the morphisms of $\mathscr{F}$ and $\mathscr{G}$ as sheaves are exactly their morphisms as presheaves. Thus, $\mathscr{C}_{X}$ is a [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ faithful, full, fully faithful|fully faithful]] [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ subcategory|subcategory]] of $\mathscr{C}_{X}^\text{pre}$. As always, there is a [[Algebraic geometry --- rising-sea/notes/Adjoint functors#_definition _ adjoint functors, left adjoint, right adjoint, adjoint pair|left adjoint]] to this forgetful functor $\mathscr{C}_{X} \to \mathscr{C}_{X}^\text{pre}$. We first define this left adjoint, sheafification, by universal property.

##### _definition:_ sheafification

The **sheafification** of a presheaf $\mathscr{F}$ (if it exists) is a sheaf $\mathscr{F}^\text{sh}$ and a presheaf morphism $\mathrm{sh} : \mathscr{F} \to \mathscr{F}^\text{sh}$ such that, for each sheaf $\mathscr{G}$, each presheaf morphism $\mathscr{F} \to \mathscr{G}$ factors through $\mathrm{sh}$ and a *unique* sheaf morphism $\mathscr{F}^\mathrm{sh} \to \mathscr{G}$. 

That is, for any $\varphi : \mathscr{F} \to \mathscr{G}$, the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F} \ar[r, "\mathrm{sh}"] \ar[rd, "\varphi"] & \mathcal{F}^\mathrm{sh} \ar[d, "\exists !", dashed] \\
		& \mathcal{G}
	\end{tikzcd}
\end{document}
```

---

Sheafification is unique upto unique isomorphism. Suppose $\mathscr{F}^\mathrm{sheaf}$ also sheafified $\mathscr{F}$. Then the sheafification $\mathrm{sheaf} : \mathscr{F} \to \mathscr{F}^\mathrm{sheaf}$ would factor uniquely through $\mathscr{F}^\mathrm{sh} \to \mathscr{F}^\mathrm{sheaf}$. Similarly $\mathrm{sh} : \mathscr{F} \to \mathscr{F}^\mathrm{sh}$ factors through $\mathscr{F}^\mathrm{sheaf} \to \mathscr{F}^\mathrm{sh}$. Thus, $\mathscr{F}^\mathrm{sh} \to \mathscr{F}^\mathrm{sheaf} \to \mathscr{F}^\mathrm{sh}$ is a map that $\mathscr{F} \to \mathscr{F}^\mathrm{sh}$ factors through. $\operatorname{id}_{\mathscr{F}^\mathrm{sh}}$ is already such a unique map, so $\mathscr{F}^\mathrm{sh} \to \mathscr{F}^\mathrm{sheaf} \to \mathscr{F}^\mathrm{sh}$ is the identity. Similarly, $\mathscr{F}^\mathrm{sheaf} \to \mathscr{F}^\mathrm{sh} \to \mathscr{F}^\mathrm{sheaf}$ is the identity, thus $\mathscr{F}^\mathrm{sh} \to \mathscr{F}^\mathrm{sheaf}$ is an isomorphism.

If $\mathscr{F}$ is already a sheaf, $\operatorname{id}_{\mathscr{F}}$ already satisfies the universal property of sheafification, so the sheafification of a sheaf is just itself.

##### _proposition:_ sheafification is functorial

If $\varphi : \mathscr{F} \to \mathscr{G}$ is a morphism of presheaves, then there is a corresponding morphism of sheaves $\varphi^\mathrm{sh} : \mathscr{F}^\mathrm{sh} \to \mathscr{G}^\mathrm{sh}$ so that  sheafification is functorial.

###### _proof sketch:_

Since $\mathscr{F} \to \mathscr{G} \to \mathscr{G}^\mathrm{sh}$ is a morphism to a sheaf, it factors as $\mathscr{F} \to \mathscr{F}^\mathrm{sh} \to \mathscr{G}^\mathrm{sh}$ giving the desired $\varphi^\mathrm{sh} : \mathscr{F}^\mathrm{sh} \to \mathscr{G}^\mathrm{sh}$. Functoriality follows since the diagrams below commute
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F} \ar[r, "\varphi"] \ar[d] & \mathcal{G} \ar[r, "\psi"] \ar[d] & \mathcal{H} \ar[d] \\
		\mathcal{F}^\mathrm{sh} \ar[r, "\varphi^\mathrm{sh}"] & \mathcal{G}^\mathrm{sh} \ar[r, "\psi^\mathrm{sh}"] & \mathcal{H}^\mathrm{sh}
	\end{tikzcd}
	\begin{tikzcd}
\mathcal{F} \ar[r, "\mathrm{id}"] \ar[d] & \mathcal{F} \ar[d] \\
\mathcal{F}^\mathrm{sh} \ar[r, "\mathrm{id}"] & \mathcal{F}^\mathrm{sh}
\end{tikzcd}
\end{document}
```

---

##### _proposition:_ sheafification is left-adjoint to forgetting

$\mathscr{F} \mapsto \mathscr{F}^\mathrm{sh}$ is left adjoint to $\mathscr{F} \mapsto \mathscr{F}^\mathrm{pre}$ where $\mathscr{F}^\mathrm{pre}$ is $\mathscr{F}$ thought of as a presheaf.

###### _proof sketch:_

Consider presheaves $\mathscr{E}, \mathscr{F}$ and sheaves $\mathscr{G}, \mathscr{H}$. There is a bijection $\tau_{\mathscr{F} \mathscr{G}} : \operatorname{Mor}(\mathscr{F}^\mathrm{sh}, \mathscr{G}) \to \operatorname{Mor}(\mathscr{F}, \mathscr{G}^\mathrm{pre})$ because the morphisms $\mathscr{F}^\mathrm{sh} \to \mathscr{G}$ are exactly the factors of morphisms $\mathscr{F} \to \mathscr{G} = \mathscr{G}^\text{pre}$ (as presheaves). We want to show that the following diagrams commute (for $\varphi : \mathscr{E} \to \mathscr{F}$ and $\psi : \mathscr{G} \to \mathscr{H}$).
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Mor} (\mathcal{F}^\mathrm{sh}, \mathcal{G}) \ar[r, "\varphi^{\mathrm{sh} *}"] \ar[d, "\tau_{\mathcal{F} \mathcal{G}}"] & \mathrm{Mor} (\mathcal{E}^\mathrm{sh}, \mathcal{G}) \ar[d, "\tau_{\mathcal{E} \mathcal{G}}"] \\
		\mathrm{Mor} (\mathcal{F}, \mathcal{G}^\mathrm{pre}) \ar[r, "\varphi^*"] & \mathrm{Mor}(\mathcal{E}, \mathcal{G}^\mathrm{pre})
	\end{tikzcd}
	\begin{tikzcd}
\mathrm{Mor} (\mathcal{F}^\mathrm{sh}, \mathcal{G}) \ar[r, "\psi^{\mathrm{sh} *}"] \ar[d, "\tau_{\mathcal{F} \mathcal{G}}"] & \mathrm{Mor} (\mathcal{F}^\mathrm{sh}, \mathcal{H}) \ar[d, "\tau_{\mathcal{F} \mathcal{H}}"] \\
		\mathrm{Mor} (\mathcal{F}, \mathcal{G}^\mathrm{pre}) \ar[r, "\psi^*"] & \mathrm{Mor}(\mathcal{F}, \mathcal{H}^\mathrm{pre})
\end{tikzcd}
\end{document}
```
In the first diagram, a morphism $\mathscr{F}^\mathrm{sh} \to \mathscr{G}$ goes to $\mathscr{E} \to \mathscr{E}^\mathrm{sh} \to \mathscr{F}^\mathrm{sh} \to \mathscr{G} = \mathscr{G}^\mathrm{pre}$ or $\mathscr{E} \to \mathscr{F} \to \mathscr{F}^\mathrm{sh} \to \mathscr{G} = \mathscr{G}^\mathrm{pre}$. Since $\mathscr{E} \to \mathscr{E}^\mathrm{sh} \to \mathscr{F}^\mathrm{sh}$ is the same as $\mathscr{E} \to \mathscr{F} \to \mathscr{F}^\mathrm{sh}$, the diagram commutes. Similarly, the second diagram sends $\mathscr{F}^\mathrm{sh} \to \mathscr{G}$ to $\mathscr{F} \to \mathscr{F}^\mathrm{sh} \to \mathscr{G} \to \mathscr{H} = \mathscr{H}^\mathrm{pre}$ or $\mathscr{F} \to \mathscr{F}^\mathrm{sh} \to \mathscr{G}^\mathrm{pre} \to \mathscr{H}^{\mathrm{pre}}$. Since $\mathscr{G} \to \mathscr{H}$ is the same as $\mathscr{G}^\mathrm{pre} \to \mathscr{H}^\mathrm{pre}$, these are the same and the diagram commutes.

---

This can be really useful. For example, it gives an abstract nonsense proof of the fact that the [[Algebraic geometry --- rising-sea/notes/Presheaves and sheaves valued in abelian categories#_proposition _ presheaf kernel is a sheaf and a kernel|presheaf kernel is also the sheaf kernel]]. Since forgetting is right adjoint to sheafification, forgetting [[Algebraic geometry --- rising-sea/notes/Exact functors#_proposition _ right adjoints preserve limits|preserves limits]]. The [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ kernels, cokernels|kernel is a limit]], so the sheaf kernel is the presheaf kernel.

### Constructing the sheafification

The sections of the sheafification just comprise the [[Algebraic geometry --- rising-sea/notes/Stalk-local properties and compatible germs#_definition _ compatible germs|tuples of compatible germs]].

##### _proposition:_ constructing the sheafification

Suppose $\mathscr{F}$ is any presheaf on $X$. Then the sheaf $\mathscr{F}^\text{sh}$ of tuples of compatible germs of $\mathscr{F}$ with
$$
\mathscr{F}^\mathrm{sh}(U) = \left\{  (s_{p})_{p \in U} \in \prod_{p \in U} \mathscr{F}_{p} \mid(s_{p})_{p \in U} \text{ is compatible}  \right\}.
$$
satisfies the universal property of the sheafification of $\mathscr{F}$.

###### _proof sketch:_

It requires verification that $\mathscr{F}^\mathrm{sh}$ forms a sheaf. This can be seen below by understanding the sheafification in terms of la espace étalé.

Consider $\mathrm{sh} : \mathscr{F} \to \mathscr{F}^\mathrm{sh}$ with $\mathscr{F}(U) \to \mathscr{F}^\mathrm{sh}(U)$ by $s \mapsto (s_{p})_{p \in U}$. Since taking stalks commutes with restriction, this defines a genuine [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_definition _ morphism of sheaves|presheaf morphism]]. 

Suppose $\mathscr{G}$ is a sheaf and $\varphi : \mathscr{F} \to \mathscr{G}$ is a (pre)sheaf morphism. Consider then $\varphi^\mathrm{sh} : \mathscr{F}^\mathrm{sh} \to \mathscr{G}$ with $\varphi ^\mathrm{sh}(U)(s_{p})_{p \in U}$ defined by gluing all $\varphi^\mathrm{sh}(U)(s^p)$ where $(s_{p})_{p \in U_{p}} = (s^p_{p})_{p \in U_{p}}$ in some neighbourhood $U_{p} \ni p$. Since the stalks of $\mathscr{F}$ and $\mathscr{F}^\mathrm{sh}$ are the same, $\varphi^\mathrm{sh}$ is [[Algebraic geometry --- rising-sea/notes/Stalk-local properties and compatible germs#_proposition _ sheaf morphisms are stalk-local|determined uniquely by the maps of stalks]] $\varphi^\mathrm{sh}_{p} = \varphi_{p}$.

---

Above we used the fact that $\mathscr{F}$ and (our construction of) $\mathscr{F}^\mathrm{sh}$ have the same stalks. This requires proof.

##### _proposition:_ sections and tuples of compatible germs have the same stalks

A presheaf $\mathscr{F}$ and the sheaf of its compatible germs $\mathscr{F}^\mathrm{sh}$ have isomorphic stalks at each $p$ with isomorphism given by $\mathrm{sh}_{p} : \mathscr{F}_{p} \to \mathscr{F}^\mathrm{sh}_{p}$.

###### _proof sketch:_

The germs in $\mathscr{F}_{p}^\mathrm{sh}$ are equivalence classes of sections $t \in \mathscr{F}^\mathrm{sh}(U_{p})$ that agree on restriction to some smaller open neighbourhood of $p$. Any germ $s_{p} \in \mathscr{F}_{p}$ comes from an equivalence class of sections $s \in \mathscr{F}(U_{p})$, and thus, determines a germ $\mathrm{sh}_{p}(s_{p}) \in \mathscr{F}_{p}$ in the equivalence class of $\mathrm{sh}(U_{p})(s)$. Since different $s_{p}, s_{p}'$ in $\mathscr{F}_{p}$ correspond to different $s, s' \in \mathscr{F}(U_{p})$ and $\mathscr{F} \to \mathscr{F}^\mathrm{sh}$ is injective at the level of open sets, different $s_{p}, s_{p}'$ give different $\mathrm{sh}_{p}(s_{p})$ and $\mathrm{sh}_{p}(s_{p}')$. That is, $\mathrm{sh}$ is injective.

Suppose $t_{p} \in \mathscr{F}_{p}^\mathrm{sh}$ is the germ of some $t \in \mathscr{F}^\mathrm{sh}(U)$. There is a neighbourhood $U_{p} \ni p$ where $t_{\mid U_{p}}$ satisfies the compatibility condition. Thus, $t_{\mid U_{p}}$ is the image of some $s \in \mathscr{F}(U_{p})$ under $\mathrm{sh}(U_{p})$ and $\mathrm{sh}_{p} : s_{p} \mapsto t_{p}$. That is, $\mathrm{sh}_{p}$ is surjective.

---

Sheafification can also be understood in terms of la espace étalé.

##### _proposition:_ sheafification is the sheaf of sections of la espace étalé

The sheafification of a presheaf $\mathscr{F}$ is the sheaf of sections of the space of sections $F \to X$.

###### _proof:_

The tuples $(s_{p})_{p \in U}$ are exactly functions to the [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ la espace étalé of a sheaf|the space of sections]] $F \to X$ of $\mathscr{F}$ with $U \to F \to X$ the identity on $U$. Tuples of compatible germs correspond to continuous sections because the pre-image of $\{ t_{p} \mid t \in \mathscr{F}(V), p \in V \}$ under a section of compatible germs $\sigma : p \mapsto s_{p}$ is the locus where $t_{p} = s_{p}$. Since $s_{p}$ comes from a section $s^p_{p} \in \mathscr{F}(U_{p})$, this locus is covered by open sets where $t = s^p$. That is, $\sigma : p \to s_p$ is a continuous section.

Conversely, for each $p \in U$ a continuous section $\sigma : U \to F$ has open neighbourhoods $U_{p} \ni p$ with [[Topology --- math-147/notes/Continuous functions#_proposition _ equivalent definitions of continuity|image contained in an open neighbourhood]] of $\sigma(p)$ — $\sigma^\mathrm{img}(U_{p}) \subseteq \{ s^p_{p} \mid s^p \in \mathscr{F}(V), p \in V \}$. This is just saying that in a small neighbourhood of each point, $\sigma$ comes from a section — $(s_{p})_{p \in U}$ by $s_{p} = \sigma(p)$ is a tuple of compatible germs. Thus, the sheafification of a presheaf $\mathscr{F}$ is the [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ the sheaf of sections of a map|sheaf of sections]] of its space of sections $F \to X$.

---