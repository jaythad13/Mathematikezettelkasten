---
tags:
- rising-sea/2/7
- alg-top
- alg-geo
---

For this note, let $\pi : X \to Y$ be a continuous map of topological spaces. All sheaves are valued in a (nice) category $\mathscr{C}$ unless otherwise specified.

Suppose $\mathscr{E}$ is a [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf, separated presheaf|sheaf]] on $Y$. Then using the [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ la espace étalé of a sheaf|espace étalé]] interpretation of $\mathscr{E}$ as a continuous map $\xi : E \to Y$ we can define pulled back sections of $\mathscr{E}$ on $U \subseteq X$ as continuous maps $\sigma : U \to E$ such that $\xi \circ \sigma = \pi_{\mid U}$. We will see that this is functorial and [[Algebraic geometry --- rising-sea/notes/Adjoint functors#_definition _ adjoint functors, left adjoint, right adjoint, adjoint pair|left adjoint]] to the [[Algebraic geometry --- rising-sea/notes/Pushforward sheaves#_definition _ pushforward/direct image presheaves and sheaves|pushforward]]. We will also give an alternate definition in terms of sections locally. This definition will be harder than that of the pushforward, but we will use it to understand sheaves on schemes. 

We will denote this by $\pi ^{-1}$ and call it the inverse image sheaf, not $\pi^*$ and the pullback sheaf. We reserve the pullback name for the left adjoint to the pushforward as a functor $\mathsf{Mod}_{\mathscr{O}_{X}} \to \mathsf{Mod}_{\mathscr{O}_{Y}}$ rather than just sheaves in a general category.

##### _definition:_ inverse image functor

We define the **inverse image functor** $\pi^{-1} : \mathscr{C}_{Y} \to \mathscr{C}_{X}$ to be the left adjoint functor to the pushforward functor $\pi_{*} : \mathscr{C}_{X} \to \mathscr{C}_{Y}$.

$\pi ^{-1} \mathscr{F}$ is the **inverse image** of a sheaf $\mathscr{F}$ on $Y$.

---

While this uniquely determines $\pi ^{-1}$ upto natural isomorphism, it doesn't prove the existence of such a functor. We give a concrete construction below.

##### _definition:_ inverse image presheaf

The sections of the **inverse image presheaf** of a sheaf $\mathscr{F}$ on $Y$ are given by
$$
\pi ^{-1}_{\text{pre}} \mathscr{F}(U) = \operatorname{colim}_{V \supseteq \pi^\text{img}(U)} \mathscr{F}(V)
$$
where the [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_definition _ colimit of a diagram|colimit]] is taken over the [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_definition _ diagram indexed by a category, index category|diagram]] of restrictions $\mathscr{F}(W) \to \mathscr{F}(V)$ induced by inclusions $V \subseteq W$. 

For $U_{1} \subseteq U_{2}$, the restriction maps are given by the universal property of the colimit. Each $V$ containing $\pi^\text{img}(U_{2})$ also contains $\pi^\text{img}(U_{1})$ and so $\pi ^{-1}_{\text{pre}} \mathscr{F}(U_{1})$ admits maps from each $\mathscr{F}(V)$ for $V$ containing $\pi^\text{img}(U_{2})$.

---

Note that this really does define a presheaf. Suppose $U_{1} \subseteq U_{2} \subseteq U_{3}$. The restriction $\mathscr{F}(U_{3}) \to \mathscr{F}(U_{1})$ is the unique map that each $\mathscr{F}(V) \to \mathscr{F}(U_{1})$ factors through (as $V$ varies over $V \supseteq U_{3}$, ). However, each $\mathscr{F}(V) \to \mathscr{F}(U_{1})$ also uniquely factors as $\mathscr{F}(V) \to \mathscr{F}(U_{2}) \to \mathscr{F}(U_{1})$ and $\mathscr{F}(V) \to \mathscr{F}(U_{2})$ factors as $\mathscr{F}(V) \to \mathscr{F}(U_{3}) \to \mathscr{F}(U_{2})$. Thus, $\mathscr{F}(U_{3}) \to \mathscr{F}(U_{1})$ is the same as $\mathscr{F}(U_{3}) \to \mathscr{F}(U_{2}) \to \mathscr{F}(U_{1})$, as desired.

##### _definition, proposition:_ inverse image presheaf functor

Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ is a morphism of sheaves on $Y$. Then $\pi^{-1}_{\text{pre}} \varphi : \pi^{-1}_{\text{pre}} \mathscr{F} \to \pi ^{-1}_{\text{pre}}\mathscr{G}$ is the morphism of sheaves defined by $\pi^{-1}_{\text{pre}}\varphi(U) = \operatorname{colim}_{V \supseteq \pi^\text{img}(U)} \varphi(V)$. 

This choice of $\pi ^{-1}_{\text{pre}} \varphi$ is functorial, defining the **inverse image presheaf functor** $\pi^{-1}_{\text{pre}} : \mathscr{C}_{Y}^\text{pre} \to \mathscr{C}_{X}^\text{pre}$.

###### _proof sketch:_

More specifically, for each $V \supseteq \pi^\text{img}(U)$ we have a map $\mathscr{F}(V) \to \mathscr{G}(V) \to \pi ^{-1}_{\text{pre}}\mathscr{G}(U)$ (the first map is $\varphi(V)$). By the universal property of the colimit, this gives a map $\pi^{-1}_{\text{pre}} \mathscr{F}(U) \to \pi ^{-1}_{\text{pre}} \mathscr{G}(U)$. 

For $U_{1} \subseteq U_{2}$, the maps $\pi^{-1}_{\text{pre}} \mathscr{F}(U_{2}) \to \pi ^{-1}_{\text{pre}} \mathscr{F}(U_{1}) \to \pi ^{-1}_{\text{pre}} \mathscr{G}(U_{1})$ and $\pi^{-1}_{\text{pre}} \mathscr{F}(U_{2}) \to \pi ^{-1}_{\text{pre}}\mathscr{G}(U_{2}) \to \pi ^{-1}_{\text{pre}} \mathscr{G}(U_{1})$ both are the unique map that all $\mathscr{F}(V) \to \pi ^{-1}_{\text{pre}} \mathscr{G}(V)$ factor through. That is, the presheaf diagram commutes.

Trust me, this is functorial in $\varphi$.

---

Now we can turn this into a functor between categories of sheaves by [[Algebraic geometry --- rising-sea/notes/Sheafification#_definition _ sheafification|sheafifying]].

##### _proposition:_ sheafification of inverse image presheaf is inverse image sheaf

Let $F = (\pi^{-1}_{\text{pre}})^\text{sh}$ be the functor $\mathscr{C}_{Y} \to \mathscr{C}_{X}$ given by $\mathscr{F} \mapsto (\pi ^{-1}_{\text{pre}} \mathscr{F})^\text{sh}$ on objects and by $\varphi \mapsto (\pi ^{-1}_{\text{pre}} \varphi)^\text{sh}$ on morphisms. Then $F$ is left adjoint to the pushforward functor $\pi_{*}$.

---

##### _proposition:_ inverse image sheaf has the right espace étalé



---

### Inverse images are nice

The adjointness of $\pi ^{-1}$ and $\pi_{*}$ mean that we get a lot of nice facts about $\pi ^{-1}$ for free.

##### _example:_ stalk and skyscraper are an adjoint pair

If $i : \{ p \} \to Y$ is the inclusion of a point, then $\pi ^{-1} \mathscr{F}$ is given by the stalk $\mathscr{F}_{p}$. In fact, adjointness gives a natural bijection between maps $\pi ^{-1} \mathscr{F} = \mathscr{F}_{p} \to S$ and maps $\mathscr{F} \to i_{*} \underline{S}$. That is, maps to a skyscraper sheaf are given by maps from the stalk at the point it is supported at. We have implicitly used this fact before to prove that [[Algebraic geometry --- rising-sea/notes/Stalk-local properties and compatible germs#_proposition _ epimorphisms are stalk-local|epimorphisms are stalk-local]].

---

A less obvious fact is that the inverse image sheaf has the same stalks.

##### _proposition:_ inverse image sheaves have the same stalks

For $q = \pi(p)$, there is a natural isomorphism $\mathscr{F}_{q} \to \pi ^{-1} \mathscr{F}_{p}$.

---

##### _proposition:_ inverse images of open embeddings are restrictions

Suppose $i : U \to Y$ gives the inclusion $U \subseteq Y$. Then $i^{-1} \mathscr{F}$ is naturally isomorphic to $\mathscr{F}_{\mid U}$.

---

Using this niceness, we can show that taking inverse images is exact.

##### _proposition:_ the inverse image functor is exact

Suppose $\mathscr{C}$ is a (sufficiently nice) [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ abelian categories|abelian category]]. Then $\pi ^{-1} : \mathscr{C}_{Y} \to \mathscr{C}_{X}$ is an exact functor.

---

Finally, inverse images give us a good notion of restricting a sheaf to a closed subset of a space.

##### _proposition:_ inverse images under closed embeddings

Suppose $\mathscr{F}$ is a sheaf on $X$ with [[Algebraic geometry --- rising-sea/notes/Sheaves valued in abelian categories#_definition _ support of a sheaf|support]] $\operatorname{supp} \mathscr{F} \subseteq Z$ contained in some closed subset $i : Z \subseteq X$. Then $\mathscr{F} \to i_{*}i^{-1}\mathscr{F}$ is an isomorphism of sheaves.

---

### The push-pull map

Suppose the following diagram of topological spaces commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		W \ar[r, "\beta'"] \ar[d, "\alpha'"] & X \ar[d, "\alpha"] \\
		Y \ar[r, "\beta"] & Z
	\end{tikzcd}
\end{document}
```
Then, for each sheaf $\mathscr{F}$ on $X$ we can get a good comparison between the two sheaves on $Y$ obtained by push-pull and pull-push.

The **push-pull map** $\beta ^{-1} \alpha_{*} \mathscr{F} \to \alpha'_{*} (\beta')^{-1} \mathscr{F}$ is a morphism of sheaves on $Y$ defined as follows. Consider $\operatorname{id} : (\beta')^{-1} \mathscr{F} \to (\beta')^{-1} \mathscr{F}$. By adjointness, this gives a unique map $\mathscr{F} \to \beta_{*}' (\beta')^{-1} \mathscr{F}$. Pushing forward along $\alpha$ gives a map $\alpha_{*} \mathscr{F} \to \alpha_{*} \beta'_{*} (\beta')^{-1} \mathscr{F}$. [[Algebraic geometry --- rising-sea/notes/Pushforward sheaves#_proposition _ pushforward is functorial|Functoriality]] means we can rewrite this as $\alpha_{*} \mathscr{F} \to (\alpha \circ \beta')_{*} (\beta') ^{-1} \mathscr{F}$ and commutativity of the diagram means $(\alpha \circ \beta')_{*} = (\beta \circ \alpha')_{*}$.  Thus, we have $\alpha_{*} \mathscr{F} \to \beta_{*} \circ \alpha'_{*} (\beta')_{^{-1}} \mathscr{F}$ which gives a unique map $\beta ^{-1} \alpha_{*} \mathscr{F} \to \alpha'_{*}(\beta')^{-1} \mathscr{F}$ by adjointness.

Note that this construction is natural in $\mathscr{F}$ — a morphism $\mathscr{F} \to \mathscr{G}$ yields the corresponding commutative diagram. That is, we have a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformation]] of functors $\beta ^{-1} \alpha_{*}$ and $\alpha_{*}' (\beta')^{-1}$. We will see that this still holds when specialising these functors to $\mathscr{O}_{X}$-modules, quasicoherent sheaves, and even cohomology.

It is a very difficult fact that starting from the identity $\alpha_{*} \mathscr{F} \to \alpha_{*} \mathscr{F}$ gives the same result.