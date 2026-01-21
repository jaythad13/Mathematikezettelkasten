---
tags:
- alg-geo
- rising-sea/7
---

Let $X, Y$ be schemes and $A, B$ be rings.

### Motivation from smooth geometry

We want to define morphisms of schemes so that the morphisms of affine schemes $\operatorname{Spec} A \to \operatorname{Spec} B$ are the ring homomorphisms $B \to A$. Specifically, we want them to look like the following morphisms of ringed spaces.

![[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_definition _ the induced morphism of ringed spaces of affine schemes|Morphisms of affine schemes]]

We also want this to be like a morphism of manifolds in the following sense.

![[Algebraic geometry --- rising-sea/notes/Ringed spaces#_example _ smooth manifolds as (local) ringed spaces|Ringed spaces]]

Since functions on schemes aren't actual functions, a continuous map $\pi : X \to Y$ doesn't actually define pullback of functions. Thus, a morphism of schemes needs to come with a defined $\pi^\sharp : \mathscr{O}_{Y} \to \pi_{*} \mathscr{O}_{X}$. This is one example of a morphism of ringed spaces.

### Morphisms of schemes

One tentative definition of a morphism of schemes is the following.

##### _definition:_ morphism of schemes

A **morphism of schemes** $\pi : X \to Y$ is a [[Algebraic geometry --- rising-sea/notes/Morphisms of ringed spaces#_definition _ morphism of ringed spaces|morphism of ringed spaces]] such that, for every affine open $\operatorname{Spec} A \subseteq X$ with $\pi^\text{img}(\operatorname{Spec} A) \subseteq \operatorname{Spec} B$, the morphism $\pi_{\mid \operatorname{Spec} A}$ is [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_definition _ the morphism of ringed spaces of affine schemes|induced by a ring morphism]] $B \to A$.

---

The problem with this definition is that it requires checking every affine open. While this property is affine local, it's much easier to show this using the notion of [[Algebraic geometry --- rising-sea/notes/Morphisms of ringed spaces#Morphisms of local ringed spaces|morphisms of local ringed spaces]].

##### _definition:_ morphism of schemes

A **morphism of schemes** $\pi : X \to Y$ is a [[Algebraic geometry --- rising-sea/notes/Morphisms of ringed spaces#_definition _ morphism of local ringed spaces|morphism of local ringed spaces]].

---

##### _proposition:_ the two definitions of morphisms of schemes are equivalent

Let $\pi : X \to Y$ be a morphism of ringed spaces. Let $X = \bigcup_{i \in I} \operatorname{Spec} A_{i}$ and $Y = \bigcup_{i \in I} \operatorname{Spec} B_{i}$, be [[Algebraic geometry --- rising-sea/notes/Schemes#_proposition, definition _ open subschemes, affine open subscheme|affine open]] covers with $\pi^\text{img}(\operatorname{Spec} A_{i}) \subseteq \operatorname{Spec} B_{i}$. The following are equivalent.
1) $\pi$ is a morphism of local ringed spaces. 
2) For every affine open $\operatorname{Spec} A \subseteq X$ with $\pi^\text{img}(\operatorname{Spec} A) \subseteq \operatorname{Spec} B$, the morphism $\pi_{\mid \operatorname{Spec} A} : \operatorname{Spec} A \to \operatorname{Spec} B$ is a [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#The morphism of affine schemes|morphism of affine schemes]] (induced by a ring homomorphism $B \to A$).
3) For every $\operatorname{Spec} A_{i}$, $\pi_{\mid \operatorname{Spec} A_{i}} : \operatorname{Spec} A_{i} \to \operatorname{Spec} B_{i}$ is a morphism of schemes.

###### _proof:_

Suppose $\pi$ is a morphism of local ringed spaces. Let $\operatorname{Spec} A \subseteq X$ have $\pi^\text{img}(\operatorname{Spec} A) \subseteq \operatorname{Spec} B$. Write $\rho$ for the restricted map $\operatorname{Spec} A \to \operatorname{Spec} B$. Since $\rho^\sharp(V) = \pi^\sharp_{\mid \operatorname{Spec} A}(V)$ for all opens, $\rho^\sharp_{q} = \pi^\sharp_{\mid \operatorname{Spec} A, q} : \mathscr{O}_{\operatorname{Spec} B, q} \to \mathscr{O}_{\operatorname{Spec} A, p}$. In turn, $\pi^\sharp_{\mid \operatorname{Spec} A}$ is the composition of $\pi^\sharp$ which preserves the maximal ideals of stalks and $\pi_{*} \mathscr{O}_{X} \to (\pi_{\mid U})_{*} \mathscr{O}_{X}$ which gives an isomorphism of stalks by some colimit argument that isn't worth writing out. Thus, $\rho : \operatorname{Spec} A \to \operatorname{Spec} B$ is a map of local ringed spaces, [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_proposition _ morphisms of local ringed spaces are morphisms of affine schemes|and thus]], a morphism of affine schemes.

If $\pi_{\mid \operatorname{Spec} A}$ is a morphism of affine schemes for every affine open, it's certainly true on an affine cover.

Since the morphisms $\pi_{\mid \operatorname{Spec} A_{i}}$ extend to codomain all of $Y$ and then [[Algebraic geometry --- rising-sea/notes/Morphisms of ringed spaces#_proposition _ morphisms of ringed spaces glue|glue to a unique morphism of ringed spaces]] $X \to Y$, $\pi$ must agree with the construction of that gluing. But in that construction, for small enough $V$ (that is, for $V \subseteq \operatorname{Spec} A_{i}$) the morphisms $\pi^\sharp(V)$ are just the morphisms $\pi_{\mid \operatorname{Spec} A_{i}}^\sharp(V)$. Thus, the stalk maps $\pi^\sharp_{q} : \mathscr{O}_{Y, q} \to \mathscr{O}_{X, p}$ are just the same as the stalk maps $(\pi^\sharp_{\mid \operatorname{Spec} A_{i}})_{q}$ which are local ring morphisms. Thus, $\pi, \pi^\sharp$ is a morphism of local ringed spaces.

---

One enlightening example of how morphisms of schemes are obtained by gluing together morphisms of affine schemes is the following.

##### _example:_ affine $(n + 1)$-space covers projective $n$-space

Just as there is a "quotient map" of manifolds $\mathbb{C}^{n + 1} \setminus \{ 0 \} \to \mathbb{C} \mathbb{P}^n$, there should be a map $\mathbb{A}_{\mathbb{F}}^{n + 1} \setminus \{ 0 \} \to \mathbb{P}^n_{\mathbb{F}}$ given in affine and homogeneous coordinates by $x_{i} \mapsto x_{i}$ (and on closed points by $(a_{0}, a_{1}, \dots, a_{n}) \mapsto (a_{0} : a_{1} : \dots : a_{n})$ for algebraically closed $\mathbb{F}$)

Write $\mathbb{A}_{\mathbb{F}}^{n + 1} \setminus \{ 0 \}$ as the union of all the distinguished opens $D(x_{i}) \cong \operatorname{Spec} \mathbb{F}[x_{0}, x_{1}, \dots, x_{n}]_{x_{i}}$. We want to map these to [[Algebraic geometry --- rising-sea/notes/Projective schemes#_definition _ homogeneous vanishing sets, projective distinguished open|projective distinguished opens]] $D_{+}(x_{i}) = \operatorname{Spec} (\mathbb{F}[x_{0}, x_{1}, \dots, x_{n}]_{x_{i}})_{0}$. There's an obvious map here — just the inclusion of the degree $0$ part into the whole ring. They agree on intersections — on $D(x_{i} x_{j}) \to D_{+}(x_{i} x_{j})$ they both restrict to the map induced by the inclusion $(\mathbb{F}[x_{0}, x_{1}, \dots, x_{n}]_{x_{i} x_{j}})_{0} \to \mathbb{F}[x_{0}, x_{1}, \dots, x_{n}]_{x_{i} x_{j}}$. Thus, they glue to give a scheme map.

---

We have shown already that [[Algebraic geometry --- rising-sea/notes/Morphisms of ringed spaces#_definition _ the category of ringed spaces|morphisms of ringed spaces compose]]. It's clear that the composition of a morphism of local rings is still a morphism of local rings. Since the stalk morphisms of the composition are just compositions of the stalk morphisms with some extra $\pi_{*} \mathscr{O}_{X, p} \to \mathscr{O}_{X, p}$ bits in between this means that morphisms of local ringed spaces, and thus, morphisms of schemes compose too. Clearly this gives a category of schemes. We denote this category by $\mathsf{Sch}$.

### Morphisms to affine schemes

Even when the source is not affine, morphisms to affine schemes have a nice interpretation in terms of morphisms of rings.

##### _proposition:_ morphisms to affine schemes

Morphisms of schemes $X \to \operatorname{Spec} A$ are in natural bijection with ring homomorphisms $A \to \mathscr{O}_{X}(X)$. That is, the [[Algebraic geometry --- rising-sea/notes/Functors#_example _ the functor of points and its opposite|functor of points]] $h_{\operatorname{Spec} A}$ is [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|naturally isomorphic]] to the functor $X \to \operatorname{Hom}_{\mathsf{Ring}}(A, \mathscr{O}_{X}(X))$.

###### _proof:_

We first describe the bijection between $\operatorname{Mor}_{\mathsf{Sch}}(X, \operatorname{Spec} A)$ and $\operatorname{Hom}_{\mathsf{Ring}}(A, \mathscr{O}_{X}(X))$. [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_definition _ morphism of affine schemes|We have already shown]] the bijection when $X$ is affine.

For general $X$, a morphism of schemes $X \to \operatorname{Spec} A$ gives a ring homomorphism of global sections $A \to \mathscr{O}_{X}(X)$. 

Conversely, a ring homomorphism of global sections $A \to \mathscr{O}_{X}(X)$ extends to a homomorphism $A \to \mathscr{O}_{X}(X) \to \mathscr{O}_{X}(\operatorname{Spec} B)$, and thus, a morphism of schemes $\operatorname{Spec} B \to \operatorname{Spec} A$ for any affine open $\operatorname{Spec} B \subseteq X$. Choose some affine cover $X = \bigcup_{i \in I} \operatorname{Spec} B_{i}$. Since the ring homomorphisms agree on intersections of the affine opens, so do the scheme morphisms $\operatorname{Spec} B_{i} \to \operatorname{Spec} A$. Thus, they glue to a morphism of schemes $X \to \operatorname{Spec} A$. Note that $\mathscr{O}_{X}(X)$ is the limit of all the $\mathscr{O}_{X}(\operatorname{Spec} B_{i})$ and their intersections. Since the ring maps $A \to B_{i}$ factor through the original morphism $A \to \mathscr{O}_{X}(X)$, the original morphism satisfies the universal property of the limit of the maps $A \to B_{i}$. Thus, [[Algebraic geometry --- rising-sea/notes/Morphisms of ringed spaces#_proposition _ morphisms of ringed spaces glue|by definition]] the morphism of schemes recovers the original ring morphism as the morphism of global sections.

Finally, we show naturality. Suppose there is a scheme morphism $\pi : X \to Y$. This induces the map $\operatorname{Mor}_{\mathsf{Sch}}(Y, \operatorname{Spec} A) \to \operatorname{Mor}_{\mathsf{Sch}}(X, \operatorname{Spec} A)$ by precomposing with $\pi$. This also gives a morphism of global sections $\pi^\sharp : \mathscr{O}_{Y}(Y) \to \mathscr{O}_{X}(X)$ that induces a map $\operatorname{Hom}_{\mathsf{Ring}}(A, \mathscr{O}_{Y}(Y)) \to \operatorname{Hom}_{\mathsf{Ring}}(A, \mathscr{O}_{X}(X))$ by precomposing with $\pi^\sharp$. But the diagram
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Mor}(Y, \mathrm{Spec} \, A) \ar[r] \ar[d] & \mathrm{Mor}(X, \mathrm{Spec} \, A) \ar[d] \\
		\mathrm{Hom}(A, \mathcal{O}_{Y}(Y)) \ar[r] & \mathrm{Hom}(A, \mathcal{O}_{X}(X))
	\end{tikzcd}
\end{document}
```
commutes because in either case, a scheme morphism $\rho : Y \to \operatorname{Spec} A$ is taken to $\rho^\sharp \circ \pi^\sharp$.

---

For example, this gives a natural "structure morphism" $\operatorname{Proj} S_{\bullet} \to \operatorname{Spec} A$ for any [[Algebraic geometry --- rising-sea/notes/Projective schemes#_definition _ projective $A$-schemes, quasiprojective $A$-schemes|projective]] $A$-scheme (given by the inclusion $A \to S_{\bullet}$), and a natural morphism $X \to \operatorname{Spec} \mathscr{O}_{X}(X)$ for any scheme $X$.

In general, this expresses the global sections functor and the $\operatorname{Spec}$ functor as [[Algebraic geometry --- rising-sea/notes/Adjoint functors#_definition _ adjoint functors, left adjoint, right adjoint, adjoint pair|adjoints]].

It also gives a universal description of $\operatorname{Spec} \mathbb{Z}$, and a way to more generally describe the notion of a [[Algebraic geometry --- rising-sea/notes/Schemes over a ring#... categorically|scheme over a ring]].

##### _corollary:_  $\operatorname{Spec} \mathbb{Z}$ is the [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ initial, final, and zero objects|final object]] of $\mathsf{Sch}$

---

Using the fact that tensor products of rings are [[Algebraic geometry --- rising-sea/notes/Fibred products#_example _ the tensor product of rings is the co-fibred products|co-fibred products]], a [[Algebraic geometry --- rising-sea/notes/Yoneda's lemma#_lemma _ Yoneda's lemma|Yoneda]]-style argument gives that $\operatorname{Spec} A \times \operatorname{Spec} B = \operatorname{Spec} (A \otimes_{\mathbb{Z}} B)$ and more generally, $\operatorname{Spec} A \times_{\operatorname{Spec} C} \operatorname{Spec B} = \operatorname{Spec} (A \otimes_{C} B)$.

### Morphisms from affine schemes and scheme-valued points