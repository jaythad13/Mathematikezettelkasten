---
tags:
- rising-sea/2/3
- rising-sea/2/6
- alg-top
- alg-geo
- hom-alg
- cat-th
---

Let $X$ be a topological space and $\mathscr{C}$ an arbitrary [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ abelian categories|abelian category]]. All sheaves are valued in $\mathscr{C}$ (unless otherwise specified). 

We will show that [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ presheaves, sections, restriction maps|presheaves]] on $X$ taking values in $\mathscr{C}$, with their [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_definition _ morphism of sheaves|presheaf morphisms]] form an abelian category, essentially open set by open set. This follows because (as we will see) the presheaf kernel and cokernel are just defined by taking the kernel and cokernel on each open set. This does not work for sheaves in general (you have to [[Algebraic geometry --- rising-sea/notes/Sheafification#_definition _ sheafification|sheafify]]). However, the analogous result does hold at the level of stalks. This 

### Presheaves valued in abelian categories

It's easy to see (and we state without verification) that they form an additive category.

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

For $\varphi : \mathscr{F} \to \mathscr{G}$ and $\psi : \mathscr{G} \to \mathscr{H}$, exactness at $\mathscr{G}$ is $\ker_{\text{pre}} \psi = \operatorname{img}_{\text{pre}} \varphi$. This is equivalent to $\ker \psi(U) = \operatorname{img} \varphi(U)$ for each $U$. This is exactly the definition of exactness of each $\mathscr{F}(U) \to \mathscr{G}(U) \to \mathscr{H}(U)$.

---

This idea of defining images open set-by-open set extends to [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ subobjects, quotient objects|subobjects and quotients]].

##### _proposition:_ monomorphisms are determined on open sets

$\varphi : \mathscr{F} \to \mathscr{G}$ is monic if and only if each $\varphi(U) : \mathscr{F}(U) \to \mathscr{G}(U)$ is monic.

###### _proof:_

Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ is monic. Suppose that there are two morphisms $\psi(U), \theta(U) : K \to \mathscr{F}(U)$ such that $\varphi(U) \circ \psi(U) = \varphi(U) \circ \theta(U)$. 

We construct a presheaf $\mathscr{K}$ such that $\psi(U), \theta(U)$ extend to morphisms $\psi, \theta : \mathscr{K} \to \mathscr{F}$. Choose $\mathscr{K}(V) = K$ for any $V \subseteq U$ and $\mathscr{K}(V) = 0$ otherwise. Let the restrictions $K \to K$ be given by the identity. The restrictions $0 \to K$ and $0 \to 0$ are each uniquely determined. There are only a few cases to check that this forms a presheaf. Suppose $V_{1} \subseteq V_{2} \subseteq V_{3}$. If $\mathscr{K}(V_{3}) = 0$ then the functoriality of restrictions follows from the uniqueness of maps from $0$. Else, $V_{1} \subseteq V_{2} \subseteq V_{3} \subseteq U$ and $\mathscr{K}(V_{i}) = K$ so all the restrictions are just $\operatorname{id}_{K}$.

Further, we can define morphisms $\psi, \theta : \mathscr{K} \to \mathscr{F}$ by choosing $\psi(V) = \operatorname{res}_{\mathscr{F} \mid V \subseteq U} \circ \psi(U) \circ \operatorname{id}_{K}^{-1}$ for $V \subseteq U$ and $\psi(V) = 0$ otherwise. The naturality of $\psi$ follows from checking only a few cases. Suppose $V_{1} \subseteq V_{2}$. If $\mathscr{K}(V_{2}) = 0$ then naturality follows from the uniqueness of maps from $0$. Else, $V_{1} \subseteq V_{2} \subseteq U$ and $\mathscr{K}(V_{i}) = K$. The map is defined exactly so that it is natural in this case.

Since $\varphi(U) \circ \psi(U) = \varphi(U) \circ \theta(U)$, we have $\varphi \circ \psi = \varphi \circ \theta$, and since $\varphi$ is monic, $\psi = \theta$. Thus, $\psi(U) = \theta(U)$. That is, $\varphi(U)$ is monic.

[[Algebraic geometry --- rising-sea/notes/Stalk-local properties and compatible germs#_proposition _ monomorphisms are stalk-local|The converse is easy]].

---

##### _proposition:_ epimorphisms are determined on open sets

$\varphi : \mathscr{F} \to \mathscr{G}$ is epic if and only if each $\varphi(U) : \mathscr{F}(U) \to \mathscr{G}(U)$ is epic.

###### _proof:_

Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ is epic. Suppose further that there are two morphisms $\psi(U), \theta(U) : \mathscr{G}(U) \to H$ such that $\psi(U) \circ \varphi(U) = \theta(U) \circ \varphi(U)$. 

We can construct a sheaf $\mathscr{H}$ dual to how we did $\mathscr{K}$ before — we choose $\mathscr{H}(V) = H$ for $V \supseteq U$ and $\mathscr{H}(V) = 0$ otherwise. The restrictions $H \to H$ are the identity and the restrictions $H \to 0$ and $0 \to 0$ are determined uniquely. We can also define morphisms $\psi, \theta : \mathscr{G} \to \mathscr{H}$ dually. We choose $\psi(V) = \psi(U) \circ \operatorname{res}_{U \subseteq V}$ for $V$ containing $U$ and $\psi(V) = 0$ otherwise. Again, the naturality of $\psi$ follows from checking only a few cases.

Since $\psi(U) \circ \varphi(U) = \theta(U) \circ \varphi(U)$, we have $\psi \circ \varphi = \theta \circ \varphi$, and since $\varphi$ is epic, $\psi = \theta$. Thus, $\psi(U) = \theta(U)$. That is, $\varphi(U)$ is epic.

[[Algebraic geometry --- rising-sea/notes/Sheaves on a base#_proposition _ epic morphisms on a base implies epic sheaf morphisms|The converse is easy]].

---

All of this means that presheaves in any abelian category form an abelian category of their own. This similar to showing that [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_proposition _ complexes form an abelian category|complexes in an abelian category form an abelian category]]. In general, this follows from the fact that the functor category $\mathscr{C}^\mathscr{I}$ is abelian for abelian $\mathscr{C}$ and [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_definition _ small category|small]] $\mathscr{I}$. The proof below easily generalises to functors valued in $\mathscr{C}$ on any small category $\mathscr{I}$.

##### _proposition:_ presheaves valued in an abelian category form an abelian category

$\mathscr{C}_{X}^\text{pre}$ is an abelian category.

###### _proof:_

We know that monomorphisms, epimorphisms, kernels, and cokernels are all determined at the level of open sets. We have also shown that kernels and cokernels exist for every map.

Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ is a monomorphism. Let $\psi : \mathscr{G} \to \operatorname{coker}_{\text{pre}} \varphi$ be the cokernel morphism. Each $\varphi(U) : \mathscr{F}(U) \to \mathscr{G}(U)$ is monic. Since $\mathscr{C}$ is abelian, each $\varphi(U)$ is the kernel of each $\psi(U) : \mathscr{G}(U) \to \operatorname{coker} \varphi(U)$. Thus, $\ker_{\text{pre}} \psi = \varphi$. That is, $\varphi$ is the kernel of its cokernel.

Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ is epic. Let $\psi : \ker_{\text{pre}} \varphi \to \mathscr{F}$ be the kernel morphism. Each $\varphi(U) : \mathscr{F}(U) \to \mathscr{G}(U)$ is epic. Since $\mathscr{C}$ is abelian, each $\varphi(U)$ is the cokernel of each $\psi(U) : \ker_{\text{pre}} \varphi(U) \to \mathscr{F}(U)$. Thus, $\operatorname{coker}_{\text{pre}} \psi = \varphi$. That is, $\varphi$ is the cokernel of its kernel.

---

### Sheaves valued in abelian categories

We would hope that the presheaves forming an abelian category would allow us to directly form an abelian category of [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf|sheaves]]. While there is some hope — the kernel presheaf forms a sheaf — the cokernel dashes this hope. We will need [[Sheafification|sheafification]].

Further, to prove some of these results, we will have to restrict from the case of a general abelian category to that of a sufficiently nice one. Specifically, we will need filtered colimits and finite limits to commute. This is certainly true for algebraic categories over set, for example. In particular, the results will hold for sheaves valued in $\mathsf{Ab}$ and $\mathsf{Mod}_{A}$. For the rest of this note, assume $\mathscr{C}$ is such a "nice" abelian category.

##### _proposition:_ presheaf kernel is a sheaf and a kernel
 
If $\varphi : \mathscr{F} \to \mathscr{G}$ is a morphism of sheaves, then $\ker_{\text{pre}} \varphi$ is a sheaf with $\ker_{\text{pre}} \varphi \to \mathscr{F}$ satisfying the universal property of a kernel of sheaves.

###### _proof:_

Let $U \subseteq X$ be an open set covered by $U_{i} \subseteq U$.

Suppose $f, g \in \ker_{\text{pre}} \varphi(U)$ and $f_{\mid i} = g_{\mid i}$ for each $i$. Then their images in $f, g \in \mathscr{F}(U)$ also agree on restriction to each $i$. Since $\ker_{\text{pre}} \varphi(U) \to \mathscr{F}(U)$ is injective, $f = g$.

Similarly, if $f_{i} \in \operatorname{ker}_{\text{pre}} \varphi(U_{i})$ and $f_{i \mid j} = f_{j \mid i}$ for each pair $i, j$, then since the $\ker_{\text{pre}} \varphi \to \mathscr{F}$ is a (pre)sheaf morphism, their images in $\mathscr{F}(U_{i})$ also agree on intersections. Thus, they can be glued to a unique $f \in \mathscr{F}(U)$. Let $\varphi(U)(f) = g$. Then $g_{\mid i} = \varphi(U_{i})(f_{\mid i}) = 0$ glue uniquely to $g = 0 \in \mathscr{G}(U)$. Thus, $f \in \ker_{\text{pre}} \varphi(U)$.

Since morphisms of sheaves are exactly morphisms of presheaves, the argument used to show that the presheaf kernel satisfies the universal property of a kernel of presheaves, also shows that it satisfies the universal property of a kernel of sheaves.

---

##### _example:_ presheaf cokernel is not (always) a sheaf — the (presheaf) exponential exact sequence

Consider $\mathbb{C}$ with the Euclidean topology, let $\underline{\mathbb{Z}}$ be the [[Algebraic geometry --- rising-sea/notes/Sheaves#_example _ constant presheaves and constant sheaves|(locally) constant sheaf]] with values in $\mathbb{Z}$, $\mathscr{O}_{\mathbb{C}}$ be the sheaf of holomorphic functions, and let $\mathscr{F}$ be the presheaf of functions admitting a [[Complex analysis --- math-135/notes/The complex logarithm#_definition _ logarithm, the logarithm|holomorphic logarithm]]. Then the following sequence of presheaves is exact
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \underline{\mathbb{Z}} \ar[r] & \mathcal{O}_{\mathbb{C}} \ar[r] & \mathcal{F} \ar[r] & 0.
	\end{tikzcd}
\end{document}
```
with $\mathscr{O}_{\mathbb{C}} \to \mathscr{F}$ given by $g \mapsto \operatorname{exp}(2 \pi i g)$.

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
Locally constant functions on $U \to \mathbb{Z}$ are holomorphic so they include into $\mathscr{O}_{\mathbb{C}}(U)$. All $f : U \to \mathbb{C}$ admitting a holomorphic logarithm $g$ have $f = \operatorname{\exp}( 2 \pi i (g / 2 \pi i))$, and thus, $\mathscr{O}(U)$ surjects onto $\mathscr{F}(U)$. Finally, $\operatorname{\exp} 2 \pi i g = 0$ if and only if $g$ takes only integer values. Since $\mathbb{Z}$ is discrete, this forces $g$ to be locally constant.

Since the sequence is exact, $\mathscr{O}_{\mathbb{C}} \to \mathscr{F}$ is the presheaf cokernel of $\underline{\mathbb{Z}} \to \mathscr{O}_{\mathbb{C}}$. However, $\mathscr{F}$ is not a sheaf because we cannot glue the function $z \mapsto z$ on simply connected $U, V \subseteq \mathbb{C} \setminus \{ 0 \}$ to $z \mapsto z$ on $U \cup V = \mathbb{C} \setminus \{ 0 \}$.

---

For this reason, we need to sheafify the presheaf cokernel.

##### _proposition:_ sheafification of the presheaf cokernel is the cokernel

Let $\varphi : \mathscr{F} \to \mathscr{G}$ be a morphism of sheaves. Let $\mathscr{H}_{\text{pre}} = \operatorname{coker}_{\text{pre}} \varphi$ and let $\mathscr{H} = \mathscr{H}_{\text{pre}}^\text{sh}$ be its [[Algebraic geometry --- rising-sea/notes/Sheafification#_definition _ sheafification|sheafification]]. Then $\mathscr{H}$ satisfies the [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ kernels, cokernels|universal property of the cokernel]] of $\varphi$.

###### _proof:_

Since  $\mathscr{H}_{\text{pre}}$ is the presheaf cokernel of $\varphi$, it has a presheaf morphism $\psi_{\text{pre}} : \mathscr{G} \to \mathscr{H}_{\text{pre}}$. It also has a sheafification morphism $\text{sh} : \mathscr{H}_{\text{pre}} \to \mathscr{H}$. Thus, we can define a sheaf morphism $\psi = \text{sh} \circ \psi_{\text{pre}}$. We claim $\psi : \mathscr{G} \to \mathscr{H}$ satisfies the universal property of the cokernel.

Suppose $\mathscr{H}'$ is a sheaf with $\psi' : \mathscr{G} \to \mathscr{H}'$ such that $\psi' \circ \varphi = 0$. Then as a morphism of presheaves, $\psi'$ factors uniquely through $\psi_{\text{pre}}$. That is, $\psi'$ factors as $\mathscr{G} \to \mathscr{H}_{\text{pre}} \to \mathscr{H}'$ uniquely. But then by the universal property of sheafification, $\mathscr{H}_{\text{pre}} \to \mathscr{H}'$ factors uniquely as $\mathscr{H}_{\text{pre}} \to \mathscr{H}_{\text{pre}}^\text{sh} \to \mathscr{H}'$ which means that $\psi'$ factors uniquely as $\mathscr{G} \to \mathscr{H} \to \mathscr{H}'$. (It requires a little thinking to show that the factorisation is unique).

---

Now we can actually state the result that essentially proves that sheaves valued in an abelian category form an abelian category.

##### _proposition:_ kernels and cokernels are [[Algebraic geometry --- rising-sea/notes/Stalk-local properties and compatible germs#Stalk-local properties|stalk-local]]

Let $\varphi : \mathscr{F} \to \mathscr{G}$ be a morphism of sheaves. Then the stalk at $p$ of the (co)kernel sheaf is the (co)kernel of the stalk morphism at $p$.

###### _proof:_

This follows easily from abstract nonsense. By hypothesis, filtered colimits commute with limits, so stalks commute with kernels, and [[Algebraic geometry --- rising-sea/notes/Exact functors#_proposition _ limits commute with limits (and colimits commute with colimits)|colimits commute with colimits]], so stalks commute with cokernels. We also give more enlightening proofs, by using some explicit forgetful functor $\mathscr{C} \to \mathsf{Set}$ for kernels, and by spelling out the argument for commutativity of stalks and cokernels in arbitrary $\mathscr{C}$.

Write $\mathscr{K} = \ker \varphi$ with $\psi : \mathscr{K} \to \mathscr{F}$ and write $K = \ker \varphi_{p}$. Similarly, write $\mathscr{H} = \operatorname{coker} \varphi$ with $\theta : \mathscr{G} \to \mathscr{H}$ the cokernel morphism and write $H = \operatorname{coker} \varphi_{p}$. 

$\psi_{p} \circ \varphi_{p} : \mathscr{K}_{p} \to \mathscr{F}_{p} \to \mathscr{G}_{p}$ composes to zero, so $\psi_{p}$ factors through some $\Pi_{p} : \mathscr{K}_{p} \to K$. In fact, since $\psi$ is monic, so is $\psi_{p}$, and thus, so is $\Pi_{p} : \mathscr{K}_{p} \to K$. As subsets of $\mathscr{F}_{p}$, this is $\mathscr{K}_{p} \subseteq K$. Suppose conversely, that some $f_{p} \in K \subseteq \mathscr{F}_{p}$. Choose, some $f^p \in \mathscr{F}(U)$ with $f^p_{p} = f_{p}$. Then, since $\varphi_{p}(f_{p}) = 0$, we have $\varphi(U)(f^p)_{p} = 0$. But then $\varphi(U)(f^p)_{\mid V} = 0$ for some $V \subseteq U$. It follows that $f^p_{\mid V} \in \mathscr{K}(V) = \operatorname{img} \psi(V) \subseteq \mathscr{F}(V)$. Taking stalks, this gives us $f^p_{p} \in \mathscr{K}_{p} = \operatorname{img} \psi_{p} \subseteq \mathscr{F}_{p}$.

Now we show that $\theta_{p} : \mathscr{G}_{p} \to \mathscr{H}_{p}$ satisfies the universal property of $H$. Suppose that the composition $\theta_{p}' \circ \varphi_{p} : \mathscr{F}_{p} \to \mathscr{G}_{p} \to H'$ is zero for some $\theta_{p}' : \mathscr{G}_{p} \to H'$. Let $\mathscr{H}'$ be the [[Algebraic geometry --- rising-sea/notes/Sheaves#_example _ skyscraper sheaves|skyscraper sheaf]] $i_{p, *} \underline{H'}$ at $p$. Note that $\mathscr{H}'_{p} = H'$. This gives a morphism $\theta' : \mathscr{G} \to \mathscr{H}'$ such that $\theta' \circ \varphi = 0$. Specifically, choose $\theta'(U) : \mathscr{G}(U) \to \mathscr{H}'(U)$ to factor as $\mathscr{G}(U) \to \mathscr{G}_{p} \to H' = \mathscr{H}'(U)$ for $p \in U$, and choose the $0$ map otherwise.

By the universal property of the cokernel, $\theta'$ factors uniquely through $\theta$ as $\amalg \circ \theta$. Thus, $\theta'_{p}$ factors as $\amalg_{p} \circ \theta_{p}$. In fact, this factorisation is unique. Suppose $\theta'_{p} = \amalg_{p}' \circ \theta_{p}$. Then since $\amalg_{p}'$ is a map $\mathscr{H}_{p} \to \mathscr{H}_{p}'$, it defines a map $\amalg' = \mathscr{H} \to \mathscr{H}'$ defined by $\amalg(U) = 0$ if $p \not\in U$ and $\amalg'(U) : \mathscr{H}(U) \to \mathscr{H}_{p} \to H' = \mathscr{H}'(U)$ otherwise. This means that $(\amalg' \circ \theta)_{q} = \theta_{q}'$ at every point $q$ (they agree at $p$ by definition of $\amalg'$ and are both $0$ everywhere else). But then, $\amalg' \circ \theta = \theta'$, implying $\amalg' = \amalg$, and finally, $\amalg' = \amalg$.

---

Combined with the [[Algebraic geometry --- rising-sea/notes/Stalk-local properties and compatible germs#_proposition _ monomorphisms are stalk-local|stalk-locality]] of monomorphisms and epimorphisms, this is sufficient to prove that $\mathscr{C}_{X}$ is an abelian category, using the argument [[#_proposition _ presheaves valued in an abelian category form an abelian category|for presheaves]].

##### _theorem:_ sheaves valued in abelian categories form an abelian category

$\mathscr{C}_{X}$ is an abelian category.

---

In fact, it follows again exactly from these arguments that images, and thus, exactness is also determined stalk-locally.

##### _proposition:_ exactness is stalk local

Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ and $\psi : \mathscr{G} \to \mathscr{H}$ are two morphisms of sheaves. Then
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F} \ar[r, "\varphi"] & \mathcal{G} \ar[r, "\psi"] & \mathcal{H}
	\end{tikzcd}
\end{document}
```
is exact if and only if, for each $p \in X$
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}_{p} \ar[r, "\varphi_{p}"] & \mathcal{G}_{p} \ar[r, "\psi_{p}"] & \mathcal{H}_{p}
	\end{tikzcd}
\end{document}
```
is exact.

---

Since taking sections over $U$ still preserves kernels, it is almost exact.

##### _proposition:_ taking sections is left exact

The functor $\Gamma(U, -) : \mathscr{C}_{X} \to \mathscr{C}$ given by $\mathscr{F} \mapsto \mathscr{F}(U)$ on objects and $\varphi \mapsto \varphi(U)$ on morphisms is [[Algebraic geometry --- rising-sea/notes/Exact functors#_definition _ right-exact, left-exact, exact|left-exact]].

###### _proof:_

Suppose
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathcal{F} \ar[r, "\varphi"] & \mathcal{G} \ar[r, "\psi"] & \mathcal{H}
	\end{tikzcd}
\end{document}
```
is exact. Then $\varphi : \mathscr{F} \to \mathscr{G}$ is exactly the kernel of $\psi$. But $(\ker \psi)(U) = \ker \psi(U)$ so $\mathscr{F}(U) = \ker \psi(U)$ with kernel map $\varphi(U) : \mathscr{F}(U) \to \mathscr{G}(U)$. That is,
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathcal{F}(U) \ar[r, "\varphi(U)"] & \mathcal{G}(U) \ar[r, "\psi(U)"] & \mathcal{H}(U)
	\end{tikzcd}
\end{document}
```
is exact.

---

This is in fact a special case of the left exactness of the pushforward.

![[Algebraic geometry --- rising-sea/notes/Pushforward sheaves#_proposition _ pushforward is left-exact|Pushforward sheaves]]

Finally, we have a sheafy analogue of the fact that taking $\operatorname{Hom}$ in any abelian category $\mathscr{C}$ [[Algebraic geometry --- rising-sea/notes/Exact functors#_example _ $h M$ is (covariant) left-exact|is left exact]]. This is of course also true for $\mathscr{C}_{X}$, but not only we do we get a version for $\operatorname{Hom}_{\mathscr{C}_{X}}(\mathscr{F}, \mathscr{G}) \in \mathsf{Ab}$, but also for $\mathcal{Hom}_{\mathscr{C}_{X}}(\mathscr{F}, \mathscr{G}) \in \mathscr{C}_{X}$.

##### _proposition:_ sheaf $\mathcal{Hom}$ is left-exact

The functors $\mathscr{C}_{X} \to \mathscr{C}_{X}$ by $\mathscr{F} \mapsto \mathcal{Hom}(\mathscr{F}, \mathscr{G})$ and $\mathscr{G} \mapsto \mathcal{Hom}(\mathscr{F}, \mathscr{G})$ are both left-exact.

> [!missing]
> proof

---

### $\mathscr{O}_{X}$-modules and tensor products

It turns out that all of these ideas work even in the category of $\mathscr{O}_{X}$[[Algebraic geometry --- rising-sea/notes/Ringed spaces#_example _ sheaves of abelian groups are $ mathscr{O}_{X}$-modules|-modules]]. Specifically, they also form an abelian category.

##### _theorem:_ $\mathscr{O}_{X}$ modules form an abelian category

---

Specifically, kernels are the presheaf kernels, cokernels are the sheafification of presheaf kernels, exactness is talk local, taking sections over an open set is left-exact, pushforwards are left-exact, and so are $\mathscr{F} \mapsto \mathcal{Hom}(\mathscr{F}, \mathscr{G})$ and $\mathscr{G} \mapsto \mathcal{Hom}(\mathscr{F}, \mathscr{G})$.

More importantly, our arguments here will allow us to define the tensor product. Suppose $\mathscr{F}, \mathscr{G}$ are $\mathscr{O}_{X}$-modules.

##### _definition:_ bilinear maps of $\mathscr{O}_{X}$-modules, tensor products of $\mathscr{O}_{X}$-modules

Suppose $\mathscr{F}, \mathscr{G}, \mathscr{H}$ are $\mathscr{O}_{X}$-modules. A **bilinear map** $\beta : \mathscr{F} \times \mathscr{G} \to \mathscr{H}$ is a collection of bilinear maps $\beta(U) : \mathscr{F}(U) \times \mathscr{G}(U) \to \mathscr{H}(U)$ such that for each $U \subseteq V$, the diagram below commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(V) \times \mathcal{G}(V) \ar[r, "\beta(V)"] \ar[d, "\mathrm{res}"] & \mathcal{H}(V) \ar[d, "\mathrm{res}"] \\
		\mathcal{F}(U) \times \mathcal{G}(U) \ar[r, "\beta(U)"] & \mathcal{H}(U) \\
	\end{tikzcd}
\end{document}
```

The **tensor product** of $\mathscr{F}, \mathscr{G}$ is a sheaf $\mathscr{F} \otimes_{\mathscr{O}_{X}} \mathscr{G}$ (often denoted without the subscript) equipped with a bilinear map $\tau : \mathscr{F} \times \mathscr{G} \to \mathscr{F} \otimes \mathscr{G}$ such that each bilinear map $\mathscr{F} \times \mathscr{G} \to \mathscr{H}$ factors uniquely as $\varphi \circ \tau$ for some linear map $\mathscr{F} \otimes \mathscr{G} \to \mathscr{H}$.

---

This definition, and the rest of this section uses the fact that the sheaf product is $(\mathscr{F} \times \mathscr{G})(U) = \mathscr{F}(U) \times \mathscr{G}(U)$ on open sets and $(\mathscr{F} \times \mathscr{G})_{p} = \mathscr{F}_{p} \times \mathscr{G}_{p}$ without any special mention.

##### _proposition:_ tensor product is the sheafification of the presheaf tensor product

Let $\mathscr{T}_{\text{pre}}$ be the presheaf defined by $\mathscr{T}_{\text{pre}}(U) = \mathscr{F}(U) \otimes_{\mathscr{O}_{X}(U)} \mathscr{G}(U)$ and with restrictions given by $\operatorname{res}_{\mathscr{F}} \otimes \operatorname{res}_{\mathscr{G}}$. Then its sheafification $\mathscr{T}_{\text{pre}}^\text{sh}$ satisfies the universal property of $\mathscr{F} \otimes_{\mathscr{O}_{X}} \mathscr{G}$.

###### _proof sketch:_

Define $\tau_{\text{pre}} : \mathscr{F} \times \mathscr{G} \to \mathscr{T}_{\text{pre}}$ by universal maps $\tau_{\text{pre}}(U) : (\mathscr{F} \times \mathscr{G})(U) \to \mathscr{F}(U) \otimes \mathscr{G}(U)$. Suppose $\tau_{\text{pre}}$ satisfies the universal property of the tensor product in the category of $\mathscr{O}_{X}$-presheaf modules. This should be easy to show by doing things at the level of open sets.

Assuming this, we claim $\tau = \mathrm{sh} \circ \tau_{\text{pre}} : \mathscr{F} \times \mathscr{G} \to \mathscr{T}$ satisfies the universal property of the sheaf tensor product. Suppose $\beta : \mathscr{F} \times \mathscr{G} \to \mathscr{H}$ is a bilinear map. Then the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F} \times \mathcal{G} \ar[r, "\tau_{\mathrm{pre}}"] \ar[rd, "\beta"] & \mathcal{T}_{\mathrm{pre}} \ar[r, "\mathrm{sh}"] \ar[d, "\varphi_{\mathrm{pre}}"] & \mathcal{T} \ar[ld, "\varphi"] \\
		& \mathcal{H}
	\end{tikzcd}
\end{document}
```
That is, $\beta$ factors through $\tau$ as $\varphi \circ \tau$.

We claim this factorisation is unique. Suppose $\beta = \varphi' \circ \tau$ is a factorisation (in the category of sheaves). Then $\beta = \varphi' \circ \mathrm{sh} \circ \tau_{\text{pre}}$ is a factorisation in the category of presheaves. Since the factorisation in the category of presheaves is unique, this gives $\varphi' \circ \mathrm{sh} = \varphi_{\text{pre}}$. But by the universal property of sheafification, there is a unique sheaf morphism $\varphi$ with $\varphi \circ \mathrm{sh} = \varphi_{\text{pre}}$. Thus, $\varphi' = \varphi$.

---

It isn't clear immediately, but we will later see that sheafification is necessary by considering line bundles on $\mathbb{P}^1$.

##### _proposition:_ tensor products are stalk local

There is an isomorphism $\tau_{p} : \mathscr{F}_{p} \times \mathscr{G}_{p} \to (\mathscr{F} \otimes_{\mathscr{O}_{X}} \mathscr{G})_{p}$ satisfies the universal property of $\mathscr{F}_{p} \otimes_{\mathscr{O}_{X, p}} \mathscr{G}_{p}$.

###### _proof sketch:_

This is a colimits commute with colimits thing

Write $\mathscr{T} = \mathscr{F} \otimes \mathscr{G}$ and write $T = \mathscr{F}_{p} \otimes \mathscr{G}_{p}$. Suppose $\beta_{p} : \mathscr{F}_{p} \times \mathscr{G}_{p} \to T'$ is a bilinear map. Let $\mathscr{T}' = i_{p, *} \underline{T'}$. Clearly $\mathscr{T}'_{p} = T'$. We can define a bilinear map $\beta : \mathscr{F} \times \mathscr{G} \to \mathscr{T}'$ by factoring through stalks for $U \ni p$ and $0$ otherwise. Then $\beta$ factors through $\tau : \mathscr{F} \times \mathscr{G} \to \mathscr{T}$, and so $\beta_{p}$ factors through $\tau_{p}$, say as $\beta_{p} = \varphi_{p} \circ \tau_{p}$. 

This factorisation is unique — we can upgrade any different factorisation $\beta_{p} = \varphi_{p}' \circ \tau_{p}$ to a factorisation $\beta = \varphi \circ \tau$, obtain $\varphi' = \varphi$ by uniqueness of the universal map, and then get $\varphi_{p}' = \varphi_{p}$.

---