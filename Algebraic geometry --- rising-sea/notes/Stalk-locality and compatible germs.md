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

Let $\mathscr{F}$ be a presheaf, $\mathscr{G}$ a sheaf, and $\varphi : \mathscr{F} \to \mathscr{G}$ a presheaf morphism. Then the following diagram commutes
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

Continuing the trend, this is not true for general (or even separated presheaves). For example, let $\mathscr{F}$ be (the presheaf of) [[Complex analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$|holomorphic functions]] on $\mathbb{C}$ admitting a [[Complex analysis --- math-135/notes/The complex logarithm#_definition _ logarithm, the logarithm|holomorphic logarithm]] and $\mathscr{O}_{\mathbb{C}}^*$ invertible holomorphic functions. Then $\mathscr{F}(U) \subseteq \mathscr{O}_{\mathbb{C}}^*(U)$ gives a presheaf morphism $\varphi$. Since $\varphi_{p}$ is given by $\mathscr{F}_{p} \subseteq \mathscr{O}_{\mathbb{C}, p}^*$ but $\mathscr{F}_{p} = \mathscr{O}_{\mathbb{C}, p}^*$ each $\varphi_{p}$ is an isomorphism. Yet $\mathscr{F} \to \mathscr{O}_{\mathbb{C}, p}^*$ is not an isomorphism — check sections over $\mathbb{C} \setminus \{ 0 \}$.

### Compatible germs

The injectivity of $\mathscr{F}(U) \to \prod_{p \in U} \mathscr{F}_{p}$ raises an important question. What is the image of the map? The image would give an isomorphism between the sections over $U$ and some subset of the product of stalks. 

##### _definition:_ compatible germs

An tuple $(s_{p})_{p \in U} \in \prod_{p \in U} \mathscr{F}_{p}$ consists of **compatible germs** such that for each $p \in U$, there is some representative $t^p \in \mathscr{F}(U_{p})$ (for some open neighbourhood $U_{p} \ni p$) with germ $t^p_{q} = s_{q}$ for all $q \in U_{p}$.

---

It's clear that the image of any $s \in \mathscr{F}(U)$ under $\mathscr{F}(U) \to \prod_{p \in U} \mathscr{F}_{p}$ consists of compatible germs — we have $s \mapsto (s_{p})_{p \in U}$ and choose $t^p = s_{\mid U_{p}}$. We show that *all* such tuples of compatible germs come from sections.

##### _proposition:_ sections are exactly tuples of compatible germs

Let $P \subseteq \prod_{p \in U} \mathscr{F}_{p}$ be the set of tuples of compatible germs. $P$ is the image of $\mathscr{F}(U) \to \prod_{p \in U} \mathscr{F}_{p}$.

###### _proof:_

We sketched above why the image is contained in $P$. We show that $P$ is contained in the image — every tuple of compatible germs comes from a section.

Suppose $(s_{p})_{p \in U}$ is a tuple of compatible germs with corresponding sections $t^p \in \mathscr{F}(U_{p})$. It suffices to show that $t^p_{\mid U_{q}} = t^q_{\mid U_{p}}$. Then we can glue the $t^p$s to a unique $t$ with germ $s_{p}$ at each $p \in U$. Since the stalks of $t^p_{\mid U_{q}}$ and $t^q_{\mid U_{p}}$ are the same everywhere on $U_{p} \cap U_{q}$ and the map $\mathscr{F}(U_{p} \cap U_{q}) \to \prod_{x \in U_{p} \cap U_{q}} \mathscr{F}_{x}$ is injective, we have exactly what we want.

---

Note that a tuple $(s_{p})_{p \in U}$ consists of compatible germs if and only if $\{ s_{p} \}$ is an open set of the [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ la espace étalé of a sheaf|space of sections]] of $\mathscr{F}$.  