---
tags:
- rising-sea/2/4
- alg-geo
- alg-top
---

Let $X$ be a topological space and $\mathscr{F}, \mathscr{G}$ sheaves (of sets, say) on $X$, unless otherwise noted.

Here, we will show that for [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf, separated presheaf|sheaves]] (though not necessarily [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ presheaves, sections, restriction maps|presheaves]]), [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ stalks, germs|stalks]] are really powerful. Recall the definition of a stalk (and germs).

![[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ stalks, germs|Sheaves]]

We will show that a sheaf (and its morphisms) really is determined by its stalks. We call such properties of a sheaf **stalk-local**. We will show how to piece the stalks together to recover the sheaf, which will eventually be the idea we use for [[Algebraic geometry --- rising-sea/notes/Sheafification|sheafification]].

### Stalk-local properties

A section over $U$ is determined by its germ at every point. This doesn't even require $\mathscr{F}$ to be a sheaf — just [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf, separated presheaf|separated]]. However, it relies on identity and so doesn't hold for presheaves in general. For example, on any disconnected space $U \sqcup V$, let $\mathscr{F}(U) = \mathscr{F}(V) = \{ 0 \}$ and let $\mathscr{F}(U \sqcup V) = \{ 0, 1 \}$. Then the global sections $0$ and $1$ both have the same values over every open set of $U$ and $V$, and thus have the same stalks.

##### _proposition:_ sections are stalk-local

The natural map $\mathscr{F}(U) \to \prod_{p \in U} \mathscr{F}_{p}$ is injective.

###### _proof:_

Note that the map is the [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ products|product]] of the colimit-defining maps $\mathscr{F}(U) \to \mathscr{F}_{p}$.

Suppose $s, t \in \mathscr{F}(U)$ have $s_{p} = t_{p}$ for all $p \in U$. By definition of the stalk, for each $p \in U$ there is then some $U_{p}$ with $s_{\mid U_{p}} = t_{\mid U_{p}}$. Since the $U_{p}$ cover all of $U$, identity forces $s = t$.

---

Morphisms are also determined by stalks. Proving this uses something that's worth its own statement as a lemma.

##### _lemma:_ the sheaf morphism to stalk morphism diagram commutes

Let $\mathscr{F}, \mathscr{G}$ be presheaves and $\varphi : \mathscr{F} \to \mathscr{G}$ a presheaf morphism. Then the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(U) \ar[r, "\varphi(U)"] \ar[d] & \mathcal{G}(U) \ar[d] \\
		\prod_{p \in U} \mathcal{F}_{p} \ar[ r, "\prod_{p} \varphi_{p}" ] & \prod_{p \in U } \mathcal{G}_{p}
	\end{tikzcd}
\end{document}
```

###### _proof sketch:_

Follows since for each $p \in U$, the following diagram commutes, [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_proposition _ "stalkification" is functorial|by definition of the stalk map]] $\varphi_{p} : \mathscr{F}_{p} \to \mathscr{G}_{p}$ .
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(U) \ar[r, "\varphi(U)"] \ar[d] & \mathcal{G}(U) \ar[d] \\
		\mathcal{F}_{p} \ar[r, "\varphi_{p}"] & \mathcal{G}_{p}
	\end{tikzcd}
\end{document}
```

---

##### _proposition:_ sheaf morphisms are stalk-local

Let $\mathscr{F}$ be a presheaf, $\mathscr{G}$ a sheaf, and $\varphi, \psi : \mathscr{F} \to \mathscr{G}$ a presheaf morphisms. If $\varphi, \psi$ induce the same morphisms on each stalk (or equivalently, the same morphism $\prod_{p \in U} \mathscr{F}_{p} \to \prod_{p \in U} \mathscr{G}_{p}$) then $\varphi = \psi$.

###### _proof:_

Since $\mathscr{G}(U) \to \prod_{p \in U} \mathscr{G}_{p}$ is injective, it is [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ monomorphisms, epimorphisms|monic]]. Thus, there is at most one map $\mathscr{F}(U) \to \mathscr{G}(U)$ so that $\mathscr{F}(U) \to \mathscr{G}(U) \to \prod_{p \in U} \mathscr{G}_{p}$ agrees with $\mathscr{F}(U) \to \prod_{p \in U} \mathscr{F}_{p} \to \prod_{p \in U} \mathscr{G}_{p}$. Since $\varphi(U)$ and $\psi(U)$ are both such maps, they must agree. Since $\varphi(U) = \psi(U)$ on every open set, $\varphi = \psi$.

---

This too is true for $\mathscr{G}$ separated, but not true for $\mathscr{G}$ a general presheaf. Return to our example from previously — on a disconnected space $U \sqcup V$, let $\mathscr{F}(U) = \mathscr{F}(V) = \{ 0 \}$ and let $\mathscr{F}(U \sqcup V) = \{ 0, 1 \}$. Then the morphism $\mathscr{F} \to \mathscr{F}$ by switching $0$ and $1$ is no different from the identity morphism at the level of stalks.

Finally, whether a morphism is an isomorphism is determined by stalks. Note that this does not mean that sheaves with isomorphic stalks are isomorphic.

##### _proposition:_ sheaf isomorphisms are stalk-local (if the morphism exists)

Let $\varphi : \mathscr{F} \to \mathscr{G}$ be a morphism of sheaves. $\varphi$ is an isomorphism if and only if it induces an isomorphism of all stalks.

###### _proof:_

Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ is an isomorphism of sheaves (with inverse $\varphi ^{-1}$). Note that $\varphi ^{-1}(U) = \varphi(U)^{-1}$ for each open $U \subseteq X$. Consider $\varphi_{p}$ and $\varphi ^{-1}_{p}$ (the stalk map of $\varphi ^{-1}$, not presuming the existence of an inverse of $\varphi_{p}$). Each of the squares, and thus, the whole of the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(U) \ar[r, "\varphi(U)"] \ar[d] & \mathcal{G}(U) \ar[r, "\varphi^{-1}(U)"] \ar[d] & \mathcal{F}(U) \ar[d] \\
		\mathcal{F}_{p} \ar[r, "\varphi_{p}"] & \mathcal{G}_{p} \ar[r, "\varphi_{p}^{-1}"] & \mathcal{F}_{p}
	\end{tikzcd}
\end{document}
```
The outer square of this diagram is the following.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(U) \ar[rrr, "\varphi^{-1}(U) \circ \varphi(U) = \mathrm{id}_{\mathcal{F}(U)}"] \ar[d] &&& \mathcal{F}(U) \ar[d] \\
		\mathcal{F}_{p} \ar[rrr, "\varphi_{p}^{-1} \circ \varphi_{p}"] &&& \mathcal{F}_{p}
	\end{tikzcd}
\end{document}
```
Thus, $\varphi_{p}^{-1} \circ \varphi_{p} : \mathscr{F}_{p} \to \mathscr{F}_{p}$ is equal to the unique map $\operatorname{id}_{\mathscr{F}_{p}}$ that the $\mathscr{F}(U) \to \mathscr{F}_{p}$ factor through. Similarly, $\varphi_{p} \circ \varphi_{p}^{-1} = \operatorname{id}_{\mathscr{G}_{p}}$ so we have $\mathscr{F}_{p} \cong \mathscr{G}_{p}$ induced by $\varphi_{p}$.

Now suppose $\varphi_{p}$ is an isomorphism for each $p$. First we show that $\varphi(U)$ is injective for each $U \subseteq X$. If $\varphi(U)(s) = \varphi(U)(s')$, then $\varphi(U) (s)_{p} = \varphi(U)(s')_{p}$. But then $\varphi_{p}(s_{p}) = \varphi_{p}(s'_{p})$. Since each $\varphi_{p}$ is injective, $s_{p} = s_{p}'$ (for each ). Since sections are determined by stalks, $s = s'$.

Now we show that $\varphi(U)$ is also surjective for each $U \subseteq X$. Let $t \in \mathscr{G}(U)$. For each $t_{p} \in \mathscr{G}_{p}$ there exists some $s^p_{p} \in \mathscr{F}_{p}$ with $\varphi_{p}(s_{p}^p) = t_{p}$. This $s^p_{p}$ comes from some section $s^p \in \mathscr{F}(U_{p})$ ($U_{p}$ is an open neighbourhood of $p$). Since
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(U) \ar[r, "\varphi(U)"] \ar[d] & \mathcal{G}(U) \ar[d, hook] \\
		\prod_{p \in U} \mathcal{F}_{p} \ar[ r, "\prod_{p} \varphi_{p}" ] & \prod_{p \in U } \mathcal{G}_{p}
	\end{tikzcd}
\end{document}
```
commutes, $\varphi(U_{p})(s^p)_{q} = t_{q}$ for all $q \in U_{p}$, and so $\varphi(U_{p})(s^p) = t_{\mid U_{p}}$. Since $\varphi(U_{p} \cap U_{q})$ is injective and $\varphi(U_{p} \cap U_{q})(s^p) = t_{\mid U_{p} \cap U_{q}} = \varphi(U_{p} \cap U_{q})(s^q)$, the $s^p$ agree on intersections of an open cover of $U$. Let them glue to $s \in \mathscr{F}(U)$. Then $\varphi(U)(s)_{\mid U_{p}} = t_{\mid U_{p}}$ on each $U_{p}$, so $\varphi(U)(s) = t$.

---

This is also true for monomorphisms and epimorphisms.

##### _proposition:_ monomorphisms are stalk-local

Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ is a morphism of sheaves. The following are equivalent.
1) $\varphi$ is a [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ monomorphisms, epimorphisms|monomorphism]].
2) $\varphi_{p} : \mathscr{F}_{p} \to \mathscr{G}_{p}$ is monic at each point $p$.
3) $\varphi(U) : \mathscr{F}(U) \to \mathscr{G}(U)$ is monic at each open set $U \subseteq X$.

###### _proof:_

> [!warning]
> as is, the proof is only valid for $\mathscr{F}, \mathscr{G} \in \mathsf{Set}_{X}$

Suppose $\varphi$ is monic and consider some $p \in X$. Suppose two morphisms $S \to \mathscr{F}_{p}$ agree on composition to $\mathscr{G}_{p}$.

Suppose $\varphi_{p}$ is monic for each $p \in X$. Then $\prod_{p \in X} \varphi_{p}$ is also monic. Suppose there is a pair of morphisms $S \to \mathscr{F}(U)$ that agree on composition to $\mathscr{G}(U)$. Then the pair of morphisms $S \to \mathscr{F}(U) \to \prod_{p \in X} \mathscr{F}_{p}$ agree on composition to $\prod_{p \in X} \mathscr{G}_{p}$. Since $\prod_{p \in X} \varphi_{p}$ is monic, the pair of morphisms $S \to \mathscr{F}(U) \to \prod_{p \in X} \mathscr{F}_{p}$ agree. But then, since $\mathscr{F}(U) \to \prod_{p \in X} \mathscr{F}_{p}$ is monic, the two maps $S \to \mathscr{F}(U)$ must be the same. That is, $\varphi(U)$ is monic.

Suppose $\varphi(U)$ is monic for each $U \subseteq X$. Suppose $\psi, \theta : \mathscr{K} \to \mathscr{F}$ are two morphisms that agree on composition to $\mathscr{G}$. That is, $\varphi(U) \circ \psi(U) = \varphi(U) \circ \theta(U)$ for each $U$. Since $\varphi(U)$ is monic, this implies $\psi(U) = \theta(U)$ for each $U$, and thus, $\psi = \theta$.

We could have directly shown that all $\varphi_{p}$ monic implies $\varphi$ monic. If each stalk morphism were monic, then whenever $\varphi \circ \psi = \varphi \circ \theta$, we have $\varphi_{p} \circ \psi_{p} = \varphi_{p} \circ \theta_{p}$ and thus, $\psi_{p} = \theta_{p}$ at each $p$. Since morphisms are determined by stalks, $\psi = \theta$.

When $\mathscr{F}, \mathscr{G}$ are sheaves, of sets, the following argument with the "indicator sheaf" is useful. Suppose $\varphi$ is monic. Let $1_{U}$ be the sheaf taking value $\{ 1 \}$ on open subsets of $U$ and $\text{Ø}$ everywhere else. Sheaf morphisms $1_{U} \to \mathscr{F}$ are defined exactly by $\{ 1 \} \to \mathscr{F}(U)$. Thus, any pair of morphisms $\{ 1 \} \to \mathscr{F}(U)$ that agree on composition to $\mathscr{G}(U)$ define two morphisms $1_{U}\to \mathscr{F}$ that agree on composition to $\mathscr{G}$. Since $\varphi$ is monic, the two morphisms $1_{U} \to \mathscr{F}$ and thus, the two morphisms $\{ 1 \} \to \mathscr{F}(U)$ are the same. That is, $\varphi(U)$ is injective.

---

##### _proposition:_ epimorphisms are stalk-local

Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ is a morphism of sheaves. The following are equivalent.
1) $\varphi$ is an [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ monomorphisms, epimorphisms|epimorphism]].
2) $\varphi_{p} : \mathscr{F}_{p} \to \mathscr{G}_{p}$ is epic at each point $p$.

###### _proof:_

Suppose $\varphi$ is not epic. Then choose distinct $\psi, \theta : \mathscr{G} \to \mathscr{H}$ such that $\psi \circ \varphi = \theta \circ \varphi$. Since sheaf morphisms are determined by stalks, there must be some point $p \in X$ where $\psi_{p}$ and $\theta_{p}$ are distinct stalk morphisms. At this point, $\varphi_{p}$ is not epic.

Suppose there is some $p \in X$ where $\varphi_{p}$ is not epic. Thus, there are two different morphisms $\mathscr{G}_{p} \to S$ such that the two compositions $\mathscr{F}_{p} \to \mathscr{G}_{p} \to S$ are the same. This defines two different morphisms $\mathscr{G} \to i_{p, *}\underline{S}$ to the skyscraper at $p$, each by $\mathscr{G}(U) \to \mathscr{G}_{p} \to S$ for $U \subseteq X$ containing $p$. However, the two compositions $\mathscr{F} \to \mathscr{G} \to i_{p, *} \underline{S}$ are the same since they are the same morphism $\mathscr{F}_{p} \to \mathscr{G}_{p} \to S$ at the level of stalks.

---

Note that this stalk-local characterisation is not true for general (or even separated presheaves). All of these can be seen to break with the two-section sheaf on the two-point discrete space (or any disconnected space) that we used earlier.

Also, note that epic sheaf morphisms are not necessarily epic on open sets.

##### _example:_ hinting at the [[Algebraic geometry --- rising-sea/notes/Presheaves in abelian categories#_example _ presheaf cokernel is not (always) a sheaf — the (presheaf) exponential exact sequence|exponential exact sequence]]

Let $\mathscr{F}$ be the (presheaf of) [[Complex analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$|holomorphic functions]] on $\mathbb{C}$ admitting a [[Complex analysis --- math-135/notes/The complex logarithm#_definition _ logarithm, the logarithm|holomorphic logarithm]] and $\mathscr{O}_{\mathbb{C}}^*$ the invertible holomorphic functions. Then $\mathscr{F}(U) \subseteq \mathscr{O}_{\mathbb{C}}^*(U)$ gives a presheaf morphism $\varphi$. Since $\varphi_{p}$ is given by $\mathscr{F}_{p} \subseteq \mathscr{O}_{\mathbb{C}, p}^*$ and $\mathscr{F}_{p} = \mathscr{O}_{\mathbb{C}, p}^*$ each $\varphi_{p}$ is an isomorphism. Yet $\mathscr{F} \to \mathscr{O}_{\mathbb{C}, p}^*$ is not an isomorphism — check sections over $\mathbb{C} \setminus \{ 0 \}$. Thus, as presheaves, $\mathscr{O}_{\mathbb{C}}^*$ is not the cokernel of the map of $2 \pi i \underline{\mathbb{Z}} \to \mathscr{O}_{\mathbb{C}}$.

However, for sheaves, the morphism $\exp : \mathscr{O}_{X} \to \mathscr{O}_{X}^*$ given by exponentiating on each open set is epic — each holomorphic function invertible near $p$ has a logarithm near $p$, so $\exp_{p} : \mathscr{O}_{X, p} \to \mathscr{O}_{X, p}^*$ is surjective. Note that it is not surjective on open sets — the identity function on $\mathbb{C} \setminus \{ 0 \}$ is invertible but does not have a logarithm.

---

However, we will see that [[Algebraic geometry --- rising-sea/notes/Sheaves on a base#_proposition _ epic morphisms on a base implies epic sheaf morphisms|the converse is true]] — sheaf morphisms that are epic on every open set (or even just enough to form a basis) are epic.

### Compatible germs

The injectivity of $\mathscr{F}(U) \to \prod_{p \in U} \mathscr{F}_{p}$ raises an important question. What is the image of the map? The image would give an isomorphism between the sections over $U$ and some subset of the product of stalks. 

##### _definition:_ compatible germs

An tuple $(s_{p})_{p \in U} \in \prod_{p \in U} \mathscr{F}_{p}$ consists of **compatible germs** if, for each $p \in U$, there is some representative $t^p \in \mathscr{F}(U_{p})$ (for some open neighbourhood $U_{p} \ni p$) with germ $t^p_{q} = s_{q}$ for all $q \in U_{p}$.

---

It's clear that the image of any $s \in \mathscr{F}(U)$ under $\mathscr{F}(U) \to \prod_{p \in U} \mathscr{F}_{p}$ consists of compatible germs — we have $s \mapsto (s_{p})_{p \in U}$ and choose $t^p = s_{\mid U_{p}}$. We show that *all* such tuples of compatible germs come from sections.

##### _proposition:_ sections are exactly tuples of compatible germs

Let $P \subseteq \prod_{p \in U} \mathscr{F}_{p}$ be the set of tuples of compatible germs. $P$ is the image of $\mathscr{F}(U) \to \prod_{p \in U} \mathscr{F}_{p}$.

###### _proof:_

We sketched above why the image is contained in $P$. We show that $P$ is contained in the image — every tuple of compatible germs comes from a section.

Suppose $(s_{p})_{p \in U}$ is a tuple of compatible germs with corresponding sections $t^p \in \mathscr{F}(U_{p})$. It suffices to show that $t^p_{\mid U_{q}} = t^q_{\mid U_{p}}$. Then we can glue the $t^p$s to a unique $t$ with germ $s_{p}$ at each $p \in U$. Since the stalks of $t^p_{\mid U_{q}}$ and $t^q_{\mid U_{p}}$ are the same everywhere on $U_{p} \cap U_{q}$ and the map $\mathscr{F}(U_{p} \cap U_{q}) \to \prod_{x \in U_{p} \cap U_{q}} \mathscr{F}_{x}$ is injective, we have exactly what we want.

---

Note that a tuple $(s_{p})_{p \in U}$ consists of compatible germs if and only if $\{ s_{p} \}$ is an open set of the [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ la espace étalé of a sheaf|space of sections]] of $\mathscr{F}$.  