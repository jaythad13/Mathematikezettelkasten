---
tags:
- rising-sea/2/1
- rising-sea/2/2
- alg-top
- alg-geo
---

Let $X$ and $Y$ be a topological spaces (unless otherwise implied to also be a manifold).

Sheaves encode the idea that geometric spaces are best understood in terms of the (relevant, nice, usually continuous) functions on them. A smooth manifold $X$ is the underlying [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]] (locally homeomorphic to $\mathbb{R}^n$) with the data of which continuous functions $X \to \mathbb{R}$ are smooth (defined in a way compatible with the local homeomorphisms to $\mathbb{R}^n$). A complex manifold $X$ (perhaps a [[Riemann surfaces and algebraic curves --- math-199DR/notes/Riemann surfaces#_definition _ (compact, connected) Riemann surface, (holomorphic) atlas, chart|Riemann surface]]) is a topological space (in the case of a Riemann surface, locally homeomorphic to $\mathbb{R}^{2}$) with the data of which functions $X \to \mathbb{C}$ are holomorphic. We can even define morphisms of Riemann surfaces [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ holomorphisms can be checked on sheaves|with just this data]].

### The sheaf of smooth functions on a manifold

We can see many of the general properties of sheaves (and some misleading special cases) in the case of smooth functions on a manifold.

Notice that for any open set $U \subseteq X$, there is a ring of smooth functions. Call it $\mathscr{O}(U)$. Also notice, that a smooth function on a larger open set $f \in \mathscr{O}(V)$ has a restriction to $U$ such that $f \mapsto f_{\mid U}$ respects the ring structure (in part because the ring structure works pointwise). If we have an open cover $\{ U_{i} \}$ of $U$, then we can identify $f \in \mathscr{O}(U)$ by the data of all the $f_{\mid U_{i}}$. Also, given a bunch of $f_{i} \in \mathscr{O}(U_{i})$, we can glue together a unique $f \in \mathscr{O}(U)$ with $f_{\mid U_{i}} = f_{i}$. This works just as well for all the ring of all functions $X \to \mathbb{R}$, all continuous functions $X \to \mathbb{R}$, or even holomorphic functions $X \to \mathbb{C}$.

Note that in some cases we also have a map $\mathscr{O}(U) \to \mathscr{O}(V)$ for $U \subseteq V$. Using partitions of unity, any smooth function on a small open set can be extended to a smooth function on a larger open set. However, there isn't exactly one way to do this that preserves smooth structure and this isn't true in other settings (like holomorphic functions or continuous functions).

In this case, we also have a notion of germs of functions, which characterise the function in the smallest possible neighbourhood around it. To be exact, the germs at a point $p \in X$ consist of $f \in \mathscr{O}(U)$ with $p \in U$ modulo the equivalence $f \sim g \in \mathscr{O}(V)$ if $f_{\mid W} = g_{\mid W}$ for some $W \subseteq U, V$. That is, the set of germs, the stalk $\mathscr{O}_{p}$ at $p$ is the [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_definition _ colimit of a diagram|colimit]] $\operatorname{colim}_{U \ni p} \mathscr{O}(U)$. This defines addition and multiplication for free.

In fact, $\mathscr{O}_{p}$ is a [[Commutative algebra --- math-189AA/notes/Local rings#_definition _ local rings|local ring]]. It has unique maximal ideal $\mathfrak{m}_{p}$ consisting of $f$ with $f(p) = 0$. This is because all other $g \in \mathscr{O}_{p}$ are non-zero in some neighbourhood around $p$, and thus, have multiplicative inverse $1 / g$. Another way to show that it is maximal, is by noticing that [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_proposition _ maximal ideals have fields as quotients|its quotient is a field]]. Considering the map $f \mapsto f(p)$ gives $\mathscr{O}_{p} / \mathfrak{m}_{p} \cong \mathbb{R}$. Also notice that $\mathfrak{m}_{p} / \mathfrak{m}_{p}^{2}$ looks like the first derivatives of all functions vanishing at $p$ modulo non-zero functions with zero derivative. It has an $\mathscr{O}_{p} / \mathfrak{m}_{p}$-module structure, and thus, is a real vector space. It is the cotangent space! Apply these to a tangent vector $v$ by evaluating $D f \mid_{p}v$.

### Sheaves and presheaves

Sheaves are very nicely behave but can be finicky to define — particularly sheaves of not-so-set-like categories. Presheaves are much more easy to define in general. We will only really define presheaves and sheaves of sets and set-like categories since our presheaves will always behave something like functions or vector bundles.

##### _definition:_ presheaves, sections, restriction maps

A **presheaf** (of sets) $\mathscr{F}$ on $X$ is a [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|contravariant functor]] from the [[Algebraic geometry --- rising-sea/notes/Categories#_example _ the inclusion category of subsets or open sets|inclusion category of open sets]] of $X$ to $\mathsf{Set}$.

If $\mathscr{C} \to \mathsf{Set}$ is a reasonable forgetful functor, then a presheaf taking values in $\mathscr{C}$ is a contravariant functor from the inclusion category of open sets of $X$ to $\mathsf{Set}$ factoring through $\mathscr{C} \to \mathsf{Set}$.

Thus, for each open set $U \subseteq X$ we have a set $\mathscr{F}(U)$, sometimes also denoted $\Gamma(U, \mathscr{F})$ or $H^0(U, \mathscr{F})$. The elements of $\mathscr{F}(U)$ are called **sections of $\mathscr{F}$ over $U$**. Sections of $\mathscr{F}$ over $X$ are called **global sections** of $\mathscr{F}$.

Finally, for every inclusion of open sets $U \subseteq V$ we have a **restriction map** $\mathscr{F}(V) \to \mathscr{F}(U)$ denoted by $\operatorname{res}_{V, U} : f \mapsto f_{\mid U}$. 

---

Note that the functoriality of the restriction map implies that for $U \subseteq V \subseteq W$ we have $\operatorname{res}_{U, U} = \operatorname{id}_{\mathscr{F}(U)}$ and $\operatorname{res}_{W, U} = \operatorname{res}_{W, V} \circ \operatorname{res}_{V, U}$.

This allows us to define the stalk of a presheaf, consisting of all of the germs — the very local information about sections.

##### _definition:_ stalks, germs

The **stalk** of a (pre)sheaf $\mathscr{F}$ at $p \in X$ is $\mathscr{F}_{p} = \operatorname{colim}_{U \ni p} \mathscr{F}(U)$. Here 

The **germs of $f \in \mathscr{F}(U)$ at $p \in U$** are the elements $f_{p}$ of the stalk $\mathscr{F}_{p}$ with $f \mapsto f_{p}$ under $\mathscr{F}(U) \to \mathscr{F}_{p}$.

---

Note that by the [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_proposition _ colimits of filtered categories in $ mathsf{Set}$|concrete interpretation of colimits of sets]], we have that $\mathscr{F}_{p}$ consists of equivalence classes of $f \in \mathscr{F}(U)$, with $f \sim g \in \mathscr{F}(V)$ if $f_{\mid W} = g_{\mid W}$ for some $W \subseteq U, V$ (the inclusion category of open sets is [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_definition _ filtered poset, filtered category|filtered]] because unions of open sets are open).

Also note that it doesn't always make sense to interpret $f_{p}$ as evaluating $f$ at $p$.

A sheaf is then a presheaf that allows sections to pieced together uniquely from very small open sets, and in fact, from stalks.

##### _definition:_ sheaf

A presheaf is a **sheaf** if it satisfies two more conditions. Let $U \subseteq X$ be any open set and $\{ U_{i} \}$ any open cover
1) If $f, g \in \mathscr{F}(U)$ and $f_{\mid U_{i}} = g_{\mid U_{i}}$ for each $i$, then $f = g$.
2) If there are $f_{i} \in \mathscr{F}(U_{i})$ such that $f_{i \mid U_{i} \cap U_{j}} = f_{j \mid U_{i} \cap U_{j}}$ for each pair $i, j$, then there is a (unique) $f \in \mathscr{F}(U)$ with $f_{\mid U_{i}} = f_{i}$ for each $i$.

---

The stalks and germs of a sheaf are just its stalks and germs as a presheaf.

The sheaf axioms can be interpreted as the "exactness" of the "equaliser exact sequence"
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdot \ar[r] & \mathcal{F}(U) \ar[r] & \prod_{i} \mathcal{F}(U_{i}) \ar[r, shift right] \ar[r, shift left] & \prod_{i, j} \mathcal{F} (U_{i} \cap U_{j})
	\end{tikzcd}
\end{document}
```
Exactness at $\mathscr{F}(U)$ means that the map $\mathscr{F}(U) \to \prod_{i} \mathscr{F}(U_{i})$ is injective, implying the identity axiom. The two maps $\prod_{i} \mathscr{F}(U_{i}) \to \prod_{i, j} \mathscr{F}(U_{i} \cap U_{j})$ are given by $(s_{i})_{i} \mapsto ((s_{i \mid j})_{i})_{j} \mapsto (s_{i \mid j})_{i, j}$ and $(s_{i})_{i} \mapsto ((s_{i \mid j})_{j})_{i}$. Exactness at $\prod_{i} \mathscr{F}(U_{i})$ means that $(s_{i})_{i}$ and $(s_{i}')_{i}$ get sent to the same thing (agree on all intersections) if and only if they come from some $s \in \mathscr{F}(U)$. This implies gluing.

They can also be interpreted as a certain limit.

##### _proposition:_ identity and gluability axioms as a limit

Let $U_{i} \subseteq X$ be open sets (indexed by $i \in \mathscr{I} \subseteq \mathscr{J}$) and a presheaf $\mathscr{F}$ on $X$. Then if and only if $\mathscr{F}$ is a sheaf, we have
$$
\mathscr{F}\left( \bigcup_{i \in \mathscr{I}} U_{i} \right) = \lim_{j \in \mathscr{J}} \mathscr{F}(U_{i}).
$$
where $\mathscr{J}$ is the diagram of inclusions of open sets $U_{i}$, including all intersections $U_{i} \cap U_{j}$.

###### _proof sketch:_

Let $U = \bigcup_{i \in \mathscr{I}} U_{i} = \bigcup_{j \in \mathscr{J}} U_{j}$. Then we have $\operatorname{res}_{j} : \mathscr{F}(U) \to \mathscr{F}(U_{j})$ that commute with all restrictions $\operatorname{res}_{i, j}$. Thus, we have $\mathscr{F}(U) \to \lim_{ j \in \mathscr{J} } \mathscr{F}(U_{j})$ that all maps into the diagram factor through. By the construction of a [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_proposition _ limits in $ mathsf{Set}$|limit of sets]], $\lim_{j \in \mathscr{J}} \mathscr{F}(U_{j})$ only consists of those products of sections that agree on all intersections, we can always glue any $(u_{j}) \in \lim_{j \in \mathscr{J}}(U_{j})$ to a section over $U$. Call this the gluing map $\lim_{ i \in \mathscr{I} } \mathscr{F}(U_{j}) \to \mathscr{F}(U)$.

Since the maps $\lim_{j \in \mathscr{J}} \mathscr{F}(U_{j}) \to U_{j}$ factor through the gluing map, it follows by reversing [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_example _ the universal property of products|the standard uniqueness of universal property]] argument that $\mathscr{F}(U)$ satisfies the universal property of the limit.

---

Note that all of these equivalent formulations imply that $\mathscr{F}(\text{Ø})$ is the one element set if we "correctly" define the empty product to be the final object in the category.

Presheaves are not necessarily sheaves.

##### _examples:_ presheaves on $\mathbb{C}$ that are not sheaves

1) Bounded functions form a presheaf since a function bounded on a big open set is still bounded on a smaller open set. However, the function $z \mapsto z$ is bounded on each open ball, and these sections do not glue to give a globally bounded function $z \mapsto z$.
2) [[Complex analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$|Holomorphic functions]] admitting a holomorphic square root form a presheaf since you can always restrict a holomorphic function to a smaller open set. However, consider $f : U \to \mathbb{C}$ and $g : V \to \mathbb{C}$ by $z \mapsto z$ with $U \cup V = \mathbb{C}$ but $U, V \subseteq \mathbb{C}$ such that $f$ and $g$ admit holomorphic square roots on $U$ and $V$ respectively. They glue to $\mathbb{C} \to \mathbb{C}$ by $z \to z$ which doesn't admit a holomorphic square root.

---

But, for example, continuous and smooth functions usually are.

##### _examples:_ continuous and smooth functions

1) Smooth functions on a manifold form a sheaf. Here the restriction map is restriction of functions. Since functions are determined by their value at a point, they satisfy the identity axiom. Since smoothness can be checked in an arbitrary small neighbourhood of a point, smooth functions glue.
2) Continuous functions $X \to \mathbb{R}$ form a sheaf. In general, continuous functions $X \to Y$ form a sheaf. Identity follows for the same reason. The [[Topology --- math-147/notes/Continuous functions#_lemma _ the gluing lemma|gluing lemma]] formalises the idea that [[Topology --- math-147/notes/Continuous functions#_definition _ continuous at a point|continuity at a point]] can be checked in a small neighbourhood, and thus, continuous functions glue.

---

### Important examples of sheaves

##### _example:_ restriction presheaves and sheaves

The **restriction of $\mathscr{F}$**, a (pre)sheaf on $X$, to a (pre)sheaf $\mathscr{F}_{\mid U}$ on an open set $U \subseteq X$ by $\mathscr{F}_{\mid U}(V) = \mathscr{F}(V)$ for all open subsets $V \subseteq U$. Note that by the definition of the [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subspace topology]] these are all open. 

Since the open subsets of a subset $V \subseteq U$ are the same as when considering $V \subseteq X$, identity and gluing of $\mathscr{F}_{\mid U}$ are inherited from $\mathscr{F}$ (if it is a sheaf proper).

To restrict a sheaf to an arbitrary subset $U \subseteq X$ will require the notion of inverse image sheaves.

---

##### _example:_ skyscraper sheaves

The **skyscraper sheaf** with value $S \in \mathsf{Set}$ at a point $p \in X$ is $i_{p, *} \underline{S}$, defined by
$$
i_{p, *} \underline{S}(U) = \begin{cases}
S & U \ni p \\
\{ e \} & U \not \ni p
\end{cases}
$$
For a sheaves in a more general category we choose $\{ e \}$ to be the [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ initial, final, and zero objects|final object]].

Note that though it appears that the only non-trivial stalk should be at $p$, this is only true if the space satisfies the right [[Topology --- math-147/notes/Separation properties#_definition _ $T_{1}$ space|separation properties]] (if every neighbourhood of $q \neq p$ also contains $p$, then $q$ also has a non-trivial stalk)

---

##### _example:_ constant presheaves and constant sheaves

The **constant presheaf** with value $S \in \mathsf{Set}$ is $\underline{S}_{\text{pre}}$ defined by $\underline{S}_{\text{pre}}(U) = S$ for every open $U \subseteq X$ with restriction maps just the identity. 

The constant presheaf is not necessarily a sheaf, even if we define $\underline{S}_{\text{pre}}(\text{Ø}) = \{ e \}$ so that it doesn't vacuously fail to be a sheaf. One way to see this is that we could equivalently define $\underline{S}_{\text{pre}}(U)$ to be the set of constant functions $U \to S$. Thus, on a [[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ connectedness|disconnected]] space, we don't have gluing. Under the original definition, pick $s_{1} \neq s_{2} \in S$ and consider the sections $s_{1}$ over $U$ and $s_{2}$ over $V$ with $U \cap V = \text{Ø}$. These sections agree on the intersection. However, since the non-empty restriction maps are identity, there is no $s \in \underline{S}_{\text{pre}}(U \cup V) = S$ such that $s_{\mid U} = s_{1} \neq s_{2} = s_{\mid V}$. That is, the sections cannot be glued. This motivates the definition of the constant sheaf.

The **constant sheaf** (which really should be called the **locally constant sheaf**) with value $S \in \mathsf{Set}$ is $\underline{S}$ with $\underline{S}(U)$ the set of locally constant functions $U \to S$ (with restriction maps just restriction of functions).

This could also be understood as $\mathscr{F}(U)$ being the continuous functions $U \to S$ when $S$ is endowed with the [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete topology]]. This intepretation is the espace étalé interpretation of sheafification of the constant presheaf.

---

One important example of sheaves is pushforwards.

![[Algebraic geometry --- rising-sea/notes/Pushforward sheaves#_definition _ pushforward/direct image presheaves and sheaves|Pushforward sheaves]]

##### _example:_ ringed spaces and $\mathscr{O}_{X}$-modules

The most important example of a sheaf for us will be ringed spaces $X, \mathscr{O}_{X}$ and its $\mathscr{O}_{X}$-modules.

![[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, functions, global functions|Ringed spaces]]

![[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ $ mathscr{O}_{X}$-modules|Ringed spaces]]

---

### La espace étalé

A general sheaf can also be thought of as a bundle. To do this, we show that continuous maps $X \to Y$ form a sheaf in a fancier sense.

##### _definition:_ the sheaf of sections of a map

Given a continuous map $\xi : E \to X$, the **sheaf of sections** of $\xi$ is the sheaf $\mathscr{E}$ on $X$ with $\mathscr{E}(U)$ the set of all continuous maps $s : U \to Y$ such that $\xi \circ s = \operatorname{id}_{U}$.

---

It's relatively easy to show that this forms a sheaf. Since the sections are continuous functions $s_{i} : U_{i} \to Y$, they glue uniquely to a continuous function. Since the property that $\xi \circ s = \operatorname{id}_{U}$ can be checked point-by-point, the glued function also satisfies it.

>[!warning]
>incomplete
