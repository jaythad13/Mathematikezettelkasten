---
tags:
- rising-sea/2/7
- alg-top
- alg-geo
---

For this note, let $\pi : X \to Y$ be a continuous map of topological spaces. All sheaves are valued in a (nice) category $\mathscr{C}$ unless otherwise specified.

Suppose $\mathscr{E}$ is a [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf, separated presheaf|sheaf]] on $Y$ corresponding to [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ la espace étalé of a sheaf|espace étalé]] $\xi : E \to Y$. We can define the section of the inverse image sheaf $\pi ^{-1}\mathscr{E}$ on $U \subseteq X$ to be continuous maps $\sigma : U \to E$ such that $\xi \circ \sigma = \pi_{\mid U}$. Equivalently, sections of the projection $E \times_{Y} X \to X$. This is functorial and [[Algebraic geometry --- rising-sea/notes/Adjoint functors#_definition _ adjoint functors, left adjoint, right adjoint, adjoint pair|left adjoint]] to the [[Algebraic geometry --- rising-sea/notes/Pushforward sheaves#_definition _ pushforward/direct image presheaves and sheaves|pushforward]]. We will also give an alternate definition in terms of sections locally. This definition will be harder than that of the pushforward, but we will use it to understand sheaves on schemes.

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

For this proposition, let $\pi ^{-1} = (\pi^{-1}_{\text{pre}})^\text{sh}$ denote the functor $\mathscr{C}_{Y} \to \mathscr{C}_{X}$ given by $\mathscr{F} \mapsto (\pi ^{-1}_{\text{pre}} \mathscr{F})^\text{sh}$ on objects and by $\varphi \mapsto (\pi ^{-1}_{\text{pre}} \varphi)^\text{sh}$ on morphisms.

$\pi^{-1}$ is left adjoint to the pushforward functor $\pi_{*}$.

---

##### _proposition:_ the espace étalé of the inverse image sheaf is the fibre product

Suppose $\mathscr{E}$ is a sheaf on $Y$ with espace étalé $\xi : E \to Y$. Then $\pi ^{-1} \mathscr{E}$ has the [[Algebraic geometry --- rising-sea/notes/Fibred products#_definition _ fibred product|fibred product]] [[Topology --- math-147/notes/Product spaces#_definition _ (finite) product topology|of topological spaces]] with the natural projection $\xi_{X} : E \times_{Y} X \to X$ as its espace étalé.

---

### Inverse images are nice

The adjointness of $\pi ^{-1}$ and $\pi_{*}$ mean that we get a lot of nice facts about $\pi ^{-1}$ for free.

##### _example:_ stalk and skyscraper are an adjoint pair

If $i : \{ p \} \to Y$ is the inclusion of a point, then $\pi ^{-1} \mathscr{F}$ is given by the stalk $\mathscr{F}_{p}$. In fact, adjointness gives a natural bijection between maps $\pi ^{-1} \mathscr{F} = \mathscr{F}_{p} \to S$ and maps $\mathscr{F} \to i_{*} \underline{S}$. That is, maps to a skyscraper sheaf are given by maps from the stalk at the point it is supported at. We have implicitly used this fact before to prove that [[Algebraic geometry --- rising-sea/notes/Stalk-local properties and compatible germs#_proposition _ epimorphisms are stalk-local|epimorphisms are stalk-local]].

---

A less obvious fact is that the inverse image sheaf has the same stalks.

##### _proposition:_ inverse image sheaves have the same stalks and the same stalk morphisms

Let $\mathscr{F}$ be a sheaf on $Y$. For $q = \pi(p)$, there is a natural isomorphism $\mathscr{F}_{q} \to \pi ^{-1} \mathscr{F}_{p}$. If $\varphi : \mathscr{F} \to \mathscr{G}$ is a morphism of sheaves on $Y$, then the stalk morphisms $\varphi_{q} : \mathscr{F}_{q} \to \mathscr{G}_{q}$ and $\pi ^{-1} \varphi_{q} : \mathscr{F}_{p} \to \mathscr{G}_{p}$ are the same morphism. 

###### _proof sketch:_

[[Algebraic geometry --- rising-sea/notes/Sheafification#_proposition _ sections and tuples of compatible germs have the same stalks|There is a natural isomorphism]] $\pi ^{-1}_{\text{pre}}\mathscr{F}_{p} \to \pi ^{-1} \mathscr{F}_{p}$. Let $U$s be open subsets of $X$ and $V$s be open subsets of $Y$. Then
$$
\begin{align}
\pi ^{-1}_{\text{pre}} \mathscr{F}_{p} & = \operatorname{colim}_{U \ni p} \pi^{-1}_{\text{pre}}\mathscr{F}(U) \\
 & = \operatorname{colim}_{U \ni p} \operatorname{colim}_{V \supseteq \pi^\text{img}(U)} \mathscr{F}(V) \\
 & = \operatorname{colim}_{V \ni q} \mathscr{F}(V) \\
 & = \mathscr{F}_{q}.
\end{align}
$$
Note that the second-to-last equality requires some statement about [[Algebraic geometry --- rising-sea/notes/Exact functors#_proposition _ limits commute with limits (and colimits commute with colimits)|colimits commuting with colimits]], but can be easily seen to be true. Thus, we have isomorphisms $\mathscr{F}_{q} \cong \pi ^{-1}_{\text{pre}} \mathscr{F}_{p} \cong \pi ^{-1} \mathscr{F}_{p}$.

Using a similar commutativity of colimits argument, we can show that the stalk morphisms are the same. In particular, $\varphi_{q} : \mathscr{F}_{q} \to \mathscr{G}_{q}$ is the colimit of all the morphisms $\mathscr{F}(V) \to \mathscr{G}(V) \to \mathscr{G}_{q}$ over all $V \ni q$. Similarly, $\pi ^{-1} \varphi_{p} : \pi ^{-1}\mathscr{F}_{p} \to \pi ^{-1} \mathscr{G}_{p}$ is the colimit of morphisms $\pi ^{-1} \mathscr{F}(U) \to \pi ^{-1} \mathscr{G}(U) \to \pi ^{-1} \mathscr{G}_{p}$ over all $U \ni p$. However, the morphism $\pi ^{-1}\varphi(U) : \pi ^{-1} \mathscr{F}(U) \to \pi ^{-1} \mathscr{G}(U)$ is the colimit $\mathscr{F}(V) \to \mathscr{G}(V) \to \pi ^{-1} \mathscr{G}(U)$ over all $V \supseteq \pi ^{\text{img}}(U)$. Thus, we can write $\pi ^{-1} \varphi_{p}$ as the colimit of
$$
\mathscr{F}(V) \to \mathscr{G}(V) \to \pi ^{-1} \mathscr{G}(U) \to \pi ^{-1} \mathscr{G}_{p} = \mathscr{G}_{q}
$$
over all $V \ni q$. This is exactly the same as the colimit expression of $\varphi_{q}$.

---

Using this nice interaction with stalks, we can show that taking inverse images is exact. Note that right-exactness could also [[Algebraic geometry --- rising-sea/notes/Exact functors#_proposition _ right adjoints preserve limits|from left-adjointness]].

##### _proposition:_ the inverse image functor is exact

Suppose $\mathscr{C}$ is a (sufficiently nice) [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ abelian categories|abelian category]]. Then $\pi ^{-1} : \mathscr{C}_{Y} \to \mathscr{C}_{X}$ is an exact functor.

###### _proof:_

Suppose
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F} \ar[r, "\varphi"] & \mathcal{G} \ar[r, "\psi"] & \mathcal{H}
	\end{tikzcd}
\end{document}
```
is an exact sequence of sheaves on $Y$. [[Algebraic geometry --- rising-sea/notes/Sheaves valued in abelian categories#_proposition _ exactness is stalk local|Then]], for each $q \in Y$, the corresponding sequence of stalks
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}_{q} \ar[r, "\varphi_{q}"] & \mathcal{G}_{q} \ar[r, "\psi_{q}"] & \mathcal{H}_{q}
	\end{tikzcd}
\end{document}
```
is an exact sequence in $\mathscr{C}$. But [[#_proposition _ inverse image sheaves have the same stalks and the same stalk morphisms|this is the exact same sequence]] as
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\pi ^{-1} \mathcal{F}_{p} \ar[r, "\pi ^{-1} \varphi_{p}"] & \pi ^{-1}\mathcal{G} \ar[r, "\pi ^{-1}\psi_{p}"] & \pi ^{-1}\mathcal{H}_{p}.
	\end{tikzcd}
\end{document}
```
Thus, the sequence above is exact for each $p$. [[Algebraic geometry --- rising-sea/notes/Sheaves valued in abelian categories#_proposition _ exactness is stalk local|Thus]],
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\pi ^{-1} \mathcal{F} \ar[r, "\pi ^{-1} \varphi"] & \pi ^{-1} \mathcal{G} \ar[r, "\pi ^{-1} \psi"] & \pi ^{-1} \mathcal{H}
	\end{tikzcd}
\end{document}
```
is exact — *exactly* what we wanted to show.

---

##### _proposition:_ inverse images of open embeddings are restrictions

Suppose $i : U \to Y$ gives the inclusion $U \subseteq Y$. Then $i^{-1} \mathscr{F}$ is naturally isomorphic to $\mathscr{F}_{\mid U}$.

###### _proof:_

We show that the functor $\mathscr{F} \mapsto \mathscr{F}_{\mid U}$ is left adjoint to the functor $\mathscr{G} \to i_{*} \mathscr{G}$. 

Suppose we have a morphism of sheaves on $U$, $\varphi : \mathscr{F}_{\mid U} \to \mathscr{G}$. Then, for each $W \subseteq U$ we have a morphism $\varphi(W) : \mathscr{F}(W) \to \mathscr{G}(W)$. For each $V \subseteq Y$, $i_{*}\mathscr{G}(V) = \mathscr{G}(U \cap V)$. Thus, we can define $\psi(V) = \varphi(U \cap V) \circ \operatorname{res}_{\mathscr{F} \mid U \cap V \subseteq V} : \mathscr{F}(V) \to i_{*} \mathscr{G}(V)$. The collection of all $\psi(V)$ forms a sheaf morphism. For $V_{1} \subseteq V_{2}$ the appropriate diagram commutes because
$$
\begin{align}
\operatorname{res}_{\mathscr{G} \mid W_{1} \subseteq W_{2}} \circ \psi(V_{2}) & = \operatorname{res}_{\mathscr{G} \mid W_{1} \subseteq W_{2}} \circ \varphi(W_{2}) \circ \operatorname{res}_{\mathscr{F} \mid W_{2} \subseteq V_{2}} \\
 & = \varphi(W_{1}) \circ \operatorname{res}_{\mathscr{F} \mid W_{1} \subseteq W_{2}} \circ \operatorname{res}_{\mathscr{F} \mid W_{2} \subseteq V_{2}} \\
 & = \psi(V_{1}) \circ \operatorname{res}_{\mathscr{F} \mid W_{1} \subseteq V_{1}} \circ \operatorname{res}_{\mathscr{F} \mid V_{1} \subseteq V_{2}} \\
 & = \psi(V_{1}) \circ \operatorname{res}_{\mathscr{F} \mid V_{1} \subseteq V_{2}}.
\end{align}
$$
We write $\psi = i_{*} \varphi$.

Conversely, suppose we have a morphism of sheaves on $Y$, $\psi : \mathscr{F} \to i_{*} \mathscr{G}$. It's clear that $i_{*} \mathscr{G}_{\mid U} = \mathscr{G}$. Restricting gives a morphism $\varphi = \psi_{\mid U} : \mathscr{F}_{\mid U} \to \mathscr{G}$ with $\psi_{\mid U}(W) = \psi(W)$ for $W \subseteq U$. 

We claim these constructions are inverses. It's clear that $(i_{*} \varphi)_{\mid U} = \varphi$ since the restriction corresponding to $U \cap W \subseteq W$ is the identity when $W \subseteq U$. Conversely, suppose $\psi : \mathscr{F} \to i_{*} \mathscr{G}$ is a sheaf morphism. Then $\psi_{\mid U}(W) = \psi(W)$ for each $W \subseteq U$. Suppose $V \subseteq Y$ and write $W = U \cap V$. Note that $\operatorname{res} : i_{*} \mathscr{G}(V) \to i_{*} \mathscr{G}(W) = \mathscr{G}(W)$ is the identity. Thus, $\operatorname{res}_{\mathscr{G} \mid W \subseteq V} \circ \psi(V) = \psi(V)$. By commutativity of the sheaf morphism diagram, we have $\operatorname{res}_{\mathscr{G} \mid W \subseteq V} \circ \psi(V) = \psi(W) \circ \operatorname{res}_{\mathscr{F} \mid W \subseteq V}$. Thus,
$$
\begin{align}
i_{*}(\psi_{\mid U})(V) & = \psi(W) \circ \operatorname{res}_{\mathscr{F} \mid W \subseteq V} \\
 & = \operatorname{res}_{\mathscr{G} \mid W \subseteq V} \circ \psi(V) \\
 & = \psi(V).
\end{align}
$$
That is, $i_{*}(\psi_{\mid U}) = \psi$ and our construction is a bijection.

Finally, [[Algebraic geometry --- rising-sea/notes/Adjoint functors#_definition _ adjoint functors, left adjoint, right adjoint, adjoint pair|we need to show]] that the following diagrams commute.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Mor}(\mathcal{F}'_{\mid U}, \mathcal{G}) \ar[r] \ar[d] & \mathrm{Mor}(\mathcal{F}_{\mid U}, \mathcal{G}) \ar[d] \\
		\mathrm{Mor}(\mathcal{F}', i_{*} \mathcal{G}) \ar[r] & \mathrm{Mor}(\mathcal{F}, i_{*} \mathcal{G})
	\end{tikzcd}
	\begin{tikzcd}
		\mathrm{Mor}(\mathcal{F}_{\mid U}, \mathcal{G}) \ar[r] \ar[d] & \mathrm{Mor}(\mathcal{F}_{\mid U}, \mathcal{G}') \ar[d] \\
		\mathrm{Mor}(\mathcal{F}, i_{*} \mathcal{G}) \ar[r] & \mathrm{Mor}(\mathcal{F}, i_{*} \mathcal{G}')
	\end{tikzcd}
\end{document}
```

Let $f : \mathscr{F} \to \mathscr{F}'$ be a morphism of sheaves and choose $\varphi' \in \operatorname{Mor}(\mathscr{F}_{\mid U}', \mathscr{G})$. Going clockwise around the commutative diagram we get $\varphi = \varphi' \circ f_{\mid U}$ and then $\psi : \mathscr{F} \to i_{*} \mathscr{G}$ with $\psi(V) = \varphi(U \cap V) \circ \operatorname{res}_{\mathscr{F} \mid U \cap V \subseteq V}$. Going counterclockwise, we first get $\psi' : \mathscr{F}' \to i_{*} \mathscr{G}$ with $\psi'(V) = \varphi'(U \cap V) \circ \operatorname{res}_{\mathscr{F}' \mid U \cap V \subseteq V}$ and then $\psi' \circ f$ which has
$$
\begin{align}
(\psi' \circ f)(V) & = \varphi'(U \cap V) \circ \operatorname{res}_{\mathscr{F}' \mid U \cap V \subseteq V} \circ f(V) \\
 & = \varphi'(U \cap V) \circ f(U \cap V) \circ\operatorname{res}_{\mathscr{F} \mid U \cap V \subseteq V} \\
 & = \varphi'(U \cap V) \circ f_{\mid U}(U \cap V) \circ \operatorname{res}_{\mathscr{F} \mid U \cap V \subseteq V} \\
 & = (\varphi \circ f_{\mid U})(U \cap V) \circ \operatorname{res}_{\mathscr{F} \mid U \cap V \subseteq V} \\
 & = \psi(V)
\end{align}
$$
as desired.

The case of naturality in some $g : \mathscr{G} \to \mathscr{G}'$ follows similarly.

---

Finally, inverse images give us a good notion of restricting a sheaf to a closed subset of a space.

##### _proposition:_ inverse images under closed embeddings

Suppose $\mathscr{F}$ is a sheaf on $Y$ with [[Algebraic geometry --- rising-sea/notes/Sheaves valued in abelian categories#_definition _ support of a sheaf|support]] contained in some closed subset $i : Z \subseteq Y$. Then the natural map $\mathscr{F} \to i_{*}i^{-1}\mathscr{F}$ is an isomorphism of sheaves.

###### _proof sketch:_

For this proposition, we let $i^{-1} \mathscr{F}$ denote presheaf inverse image instead of its sheafification. We use the fact that we can just sheafify at the end to recover the desired result without proof — this requires sheafification to commute with a bunch of stuff.

We already have a natural isomorphism $\mathscr{F}_{p} \to i^{-1} \mathscr{F}_{p}$. For pushforwards its not hard to see that we have an isomorphism $\mathscr{G}_{p} \cong i_{*}\mathscr{G}_{p}$ when $p \in Z$ and $i_{*} \mathscr{G}_{p} = 0$ otherwise. Thus, for $\operatorname{supp} \mathscr{F} \subseteq Z$ we always have a canonical isomorphism $\mathscr{F}_{p} \to i_{*} i^{-1} \mathscr{F}_{p}$.

If $p \not\in Z$, then $\varphi_{p}$ is a map $0 \to 0$ and thus must be an isomorphism. Assume $p \in Z$. The map $\varphi : \mathscr{F} \to i_{*} i^{-1} \mathscr{F}$ is $\tau(i^{-1} \operatorname{id}_{\mathscr{F}})$. Here $\tau : \operatorname{Mor}(i^{-1} \mathscr{F}, i^{-1} \mathscr{F}) \to \operatorname{Mor}(\mathscr{F}, i_{*} i^{-1} \mathscr{F})$ is the bijection giving adjointness of inverse image and pushforward functors. For each open set $U \ni p$, we have $\varphi(U) : \mathscr{F}(U) \to i_{*}i^{-1} \mathscr{F}(U) = i^{-1}\mathscr{F}(Z \cap U)$, and thus, a map $\mathscr{F}(U) \to i^{-1} \mathscr{F}(Z \cap U) \to i_{*} i^{-1}\mathscr{F}_{p}$. By the colimit definition of $i^{-1} \mathscr{F}(Z \cap U)$ these factor through $\mathscr{F}(V)$ for each $V \supseteq Z \cap U$. Since all of the $\mathscr{F}(V) \to i_{*} i^{-1} \mathscr{F}_{p}$ factor uniquely through the canonical isomorphism, so does $\mathscr{F}(U) \to i_{*}i^{-1} \mathscr{F}_{p}$.

The corresponding stalk morphism $\varphi_{p} : \mathscr{F}_{p} \to i_{*}i^{-1} \mathscr{F}_{p}$ is given as follows. The $\mathscr{F}(U) \to i_{*}i^{-1}\mathscr{F}_{p}$ factor uniquely through the colimit $\mathscr{F}(U) \to \mathscr{F}_{p} \to i_{*}i^{-1}\mathscr{F}_{p}$. We just showed that this unique factorisation is through the canonical isomorphism. [[Algebraic geometry --- rising-sea/notes/Stalk-local properties and compatible germs#_proposition _ sheaf isomorphisms are stalk-local (if the morphism exists)|Isomorphisms are stalk local]], so $\varphi$ is an isomorphism.

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