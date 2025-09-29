---
tags:
- rising-sea/2/3
- alg-top
- alg-geo
- hom-alg
- cat-th
---

Let $X$ be a topological space and $\mathscr{C}$ an arbitrary [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ abelian categories|abelian category]] (unless otherwise specified). 

We will show that [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ presheaves, sections, restriction maps|presheaves]] on $X$ taking values in $\mathscr{C}$, with their [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_definition _ morphism of sheaves|presheaf morphisms]] form an abelian category, essentially open set by open set. It's easy to see (and we state without verification) that they form an additive category.

##### _proposition:_ presheaves of additive categories form an additive category

Let $\mathscr{A}$ be an [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_examples _ additive categories|additive]] (possibly abelian) category. Then $\mathscr{A}_{X}$, the category of presheaves on $X$ with values in $\mathscr{A}$ form an abelian category with zero object $\underline{0}$, addition of morphisms $\varphi, \psi : \mathscr{F} \to \mathscr{G}$ given by $(\varphi + \psi)(U) = \varphi(U) + \psi(U)$, and products of sheaves given by $(\mathscr{F} \times \mathscr{G})(U) = \mathscr{F}(U) \times \mathscr{G}(U)$.

---

##### _definition:_ presheaf kernels, presheaf cokernels

The **kernel** of a presheaf morphism $\varphi : \mathscr{F} \to \mathscr{G}$ is the presheaf $\ker_{\text{pre}} \varphi$ given by $\ker_{\text{pre}} \varphi(U) = \ker \varphi(U)$ with the inclusion morphism $\ker_{\text{pre}} \varphi \xhookrightarrow{} \mathscr{F}$ by $\ker_{\text{pre}} \varphi(U) \xhookrightarrow{} \mathscr{F}(U)$ on each open set $U \subseteq X$.

The **cokernel** of $\varphi$ is the presheaf $\operatorname{coker}_{\text{pre}} \varphi$ given by $\operatorname{coker}_{\text{pre}} \varphi(U) = \operatorname{coker} \varphi(U)$ and with the morphism $\mathscr{G} \to \operatorname{coker}_{\text{pre}} \varphi$ given by $\mathscr{G}(U) \to \operatorname{coker} \varphi(U)$ on each open set $U \subseteq X$.

---

It takes some verification that this really is a presheaf. The idea is that (for open $V \subseteq U \subseteq X$) the restriction map $\operatorname{res}_{U, V}$ restricted to $\ker \varphi(U)$ maps into $\ker \varphi(V)$. That is, the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker_{\mathrm{pre}} \varphi(U) \ar[r, hook] \ar[d, dashed] & \mathcal{F}(U) \ar[r] \ar[d] & \mathcal{G}(U) \ar[d] \\
		0 \ar[r] & \ker_{\mathrm{pre}} \varphi(V) \ar[r, hook] & \mathcal{F}(V) \ar[r] & \mathcal{G}(V)
	\end{tikzcd}
\end{document}
```

Even in an arbitrary (non-set-like) abelian category this follows from the universal property of the kernel $\ker \varphi(V)$. Since the diagram commutes without the dashed arrow, we have a map $\operatorname{ker}_{\text{pre}} \varphi(U) \to \mathscr{F}(U) \to \mathscr{F}(V)$ such that on extending to $\ker_{\text{pre}} \varphi(U) \to \mathscr{F}(V) \to \mathscr{G}(V)$ we have the zero map. Thus, the map $\ker_{\text{pre}} \varphi(U) \to \mathscr{F}(V)$ factors through $\ker_{\text{pre}} \varphi(V) \to \mathscr{F}(V)$. That is the unique map filling the dashed arrow.

##### _proposition:_ presheaf (co)kernels are (co)kernels

The presheaf cokernel of a presheaf morphism $\varphi : \mathscr{F} \to \mathscr{G}$ satisfies [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ kernels, cokernels|the universal property of a cokernel]] of presheaves.

Dually, the presheaf kernel satisfies the universal property of the kernel.

###### _proof:_

Let $\theta : \mathscr{G} \to \operatorname{coker}_{\text{pre}} \varphi$ be the cokernel morphism. Note then that each $\theta(U) : \mathscr{G}(U) \to \operatorname{coker} \varphi(U)$ is the cokernel morphism

Suppose $\psi : \mathscr{G} \to \mathscr{H}$ has $\psi \circ \varphi = 0$. Since $\psi \circ \varphi$ factors through $\underline{0}$, each $\psi(U) \circ \varphi(U)$ factors through $0(U) = 0$, and thus, $\psi(U) \circ \varphi(U) = 0$. Thus, $\psi(U)$ factors through $\theta(U)$. That is, $\psi(U) = \mu(U) \circ \theta(U)$ for some $\mu(U) : \operatorname{coker} \varphi(U) \to \mathscr{H}(U)$. We want to show that these $\mu(U)$ assemble into a presheaf morphism $\mu : \operatorname{coker}_{\text{pre}} \varphi \to \mathscr{H}$. That is, we want to show that
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
	\mathrm{coker} \, \psi(U) \ar[r, "\mu(U)"] \ar[d] & \mathcal{H}(U) \ar[d] \\
	\mathrm{coker} \, \psi(V) \ar[r, "\mu(V)"] & \mathcal{H}(V)
	\end{tikzcd}
\end{document}
```
commutes. This follows since $\operatorname{coker} \psi(U) \to \operatorname{coker} \psi(V)$ is the unique morphism such that $\mu(U)$ factors through $\mu(V)$. That is, we defined the restriction morphism so that $\mu$ is a presheaf morphism.

---

Since kernels and cokernels are defined open set-by-open set, we can do everything open set-by-open set. For example, exactness works like this.

##### _proposition:_ exactness open set-by-open set

For each open $U \subseteq X$, the [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|functor]] $\mathscr{C}_{X} \to \mathscr{C}$ by $\mathscr{F} \mapsto \mathscr{F}(U)$ and $\varphi \mapsto \varphi(U)$ is [[Algebraic geometry --- rising-sea/notes/Exact functors#_definition _ right-exact, left-exact, exact|exact]].

The converse is also true — if $\mathscr{F}(U) \to \mathscr{G}(U) \to \mathscr{H}(U)$ is [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ complexes, exactness, short exact sequence|exact]] for each $U \subseteq X$, then $\mathscr{F} \to \mathscr{G} \to \mathscr{H}$ is exact.

###### _proof sketch:_

Note that by the definition of kernels and cokernels of presheaves, we have that $\operatorname{img}_{\text{pre}} \varphi$
$$
\operatorname{img}_{\text{pre}} \varphi(U) = \ker_{\text{pre}} \operatorname{coker}_{\text{pre}} \varphi (U) = \ker \operatorname{coker} \varphi(U) = \operatorname{img} \varphi(U)
$$
on each open set $U \subseteq X$. 

For $\varphi : \mathscr{F} \to \mathscr{G}$ and $\psi : \mathscr{G} \to \mathscr{H}$, exactness at $\mathscr{G}$ is $\ker_{\text{pre}} \psi = \operatorname{img}_{\text{pre}} \varphi$. This is equivalent to $\ker \psi(U) = \operatorname{img} \varphi(U)$ for each $U$. This is just exactness of $\mathscr{F}(U) \to \mathscr{G}(U) \to \mathscr{H}(U)$.

---

This idea of defining images open set-by-open set extends to [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ subobjects, quotient objects|subobjects and quotients]]. In fact, open set-by-open set, presheaves in any abelian category form an abelian category of their own. This similar to showing that [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_proposition _ complexes form an abelian category|complexes in an abelian category form an abelian category]]. In general, this follows from the fact that the functor category $\mathscr{C}^\mathscr{I}$ is abelian for abelian $\mathscr{C}$ and [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_definition _ small category|small]] $\mathscr{I}$.

##### _proposition:_ presheaves in an abelian category form an abelian category

$\mathscr{C}_{X}^\text{pre}$ is an abelian category.

---

>[!missing]
> proof

### Sheaf-iness?

We would hope that the presheaves forming an abelian category would allow us to directly form an abelian category of [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf|sheaves]]. While there is some hope — the kernel presheaf forms a sheaf — the cokernel dashes this hope. We will need [[Sheafification|sheafification]].

##### _proposition:_ presheaf kernel is a sheaf and a kernel

If $\varphi : \mathscr{F} \to \mathscr{G}$ is a morphism of sheaves, then $\ker_{\text{pre}} \varphi$ is a sheaf with $\ker_{\text{pre}} \varphi \to \mathscr{F}$ satisfying the universal property of a kernel of sheaves.

###### _proof:_

Let $U \subseteq X$ be an open set covered by $U_{i} \subseteq U$.

Suppose $f, g \in \ker_{\text{pre}} \varphi(U)$ and $f_{\mid i} = g_{\mid i}$ for each $i$. Then their images in $f, g \in \mathscr{F}(U)$ also agree on restriction to each $i$. Since $\ker_{\text{pre}} \varphi(U) \to \mathscr{F}(U)$ is injective, $f = g$.

Similarly, if $f_{i} \in \operatorname{ker}_{\text{pre}} \varphi(U_{i})$ and $f_{i \mid j} = f_{j \mid i}$ for each pair $i, j$, then since the $\ker_{\text{pre}} \varphi \to \mathscr{F}$ is a (pre)sheaf morphism, their images in $\mathscr{F}(U_{i})$ also agree on intersections. Thus, they can be glued to a unique $f \in \mathscr{F}(U)$. Let $\varphi(U)(f) = g$. Then $g_{\mid i} = \varphi(U_{i})(f_{\mid i}) = 0$ glue uniquely to $g = 0 \in \mathscr{G}(U)$. Thus, $f \in \ker_{\text{pre}} \varphi(U)$.

Since morphisms of sheaves are exactly morphisms of presheaves, the argument used to show that the presheaf kernel satisfies the universal property of a kernel of presheaves, also shows that it satisfies the universal property of a kernel of sheaves.

---

##### _example:_ presheaf cokernel is not (always) a sheaf — the (presheaf) exponential exact sequence

Consider $\mathbb{C}$ with the Euclidean topology, let $\underline{\mathbb{Z}}$ be the [[Algebraic geometry --- rising-sea/notes/Sheaves#_example _ constant presheaves and constant sheaves|(locally) constant sheaf]] with values in $\mathbb{Z}$, $\mathscr{O}_{\mathbb{C}}$ be the sheaf of holomorphic functions, and let $\mathscr{F}$ be the presheaf of functions admitting a [[Complex analysis --- math-135/notes/The complex logarithm#_definition _ logarithm, the logarithm|holomorphic logarithm]]. Then the following sequence is exact
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \underline{\mathbb{Z}} \ar[r] & \mathcal{O}_{\mathbb{C}} \ar[r] & \mathcal{F} \ar[r] & 0.
	\end{tikzcd}
\end{document}
```
with $\mathscr{O}_{\mathbb{C}} \to \mathscr{F}$ given by $g \mapsto \operatorname{exp}(2 \pi i g)$

This follows because, on each open set $U \subseteq \mathbb{C}$, the sequence below is exact.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \underline{\mathbb{Z}}(U) \ar[r] & \mathcal{O}_{\mathbb{C}}(U) \ar[r] & \mathcal{F}(U) \ar[r] & 0
	\end{tikzcd}
\end{document}
```
Locally constant functions on $U \to \mathbb{Z}$ are holomorphic so they include into $\mathscr{O}_{\mathbb{C}}(U)$, and all $f : U \to \mathbb{C}$ admitting a holomorphic logarithm $g$ have $f = \operatorname{\exp}( 2 \pi i g / 2 \pi i)$, and thus, $\mathscr{O}(U)$ surjects onto $\mathscr{F}(U)$. Finally, $\operatorname{\exp} g = 0$ if and only if $g$ takes only integer values. Since $\mathbb{Z}$ is discrete, this forces $g$ to be locally constant.

Since the sequence is exact, $\mathscr{O}_{\mathbb{C}} \to \mathscr{F}$ is the cokernel of $\underline{\mathbb{Z}} \to \mathscr{O}_{\mathbb{C}}$. However, $\mathscr{F}$ is not a sheaf because we cannot glue the function $z \mapsto z$ on simply connected $U, V \subseteq \mathbb{C} \setminus \{ 0 \}$ to $z \mapsto z$ on $U \cup V = \mathbb{C} \setminus \{ 0 \}$.

---