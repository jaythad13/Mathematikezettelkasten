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

Clearly, this gives a category of schemes. We have shown already that [[Algebraic geometry --- rising-sea/notes/Morphisms of ringed spaces#_definition _ the category of ringed spaces|morphisms of ringed spaces compose]]. It's clear that the composition of a morphism of local rings is still a morphism of local rings. Since the stalk morphisms of the composition are just compositions of the stalk morphisms with some extra $\pi_{*} \mathscr{O}_{X, p} \to \mathscr{O}_{X, p}$ bits in between this means that morphisms of local ringed spaces, and thus, morphisms of schemes compose too.

One enlightening example of how morphisms of schemes are obtained by gluing together morphisms of affine schemes is the following.

##### _example:_ affine $(n + 1)$-space covers projective $n$-space

Just as there is a "quotient map" of manifolds $\mathbb{C}^{n + 1} \setminus \{ 0 \} \to \mathbb{C} \mathbb{P}^n$, there should be a map $\mathbb{A}_{\mathbb{F}}^{n + 1} \setminus \{ 0 \} \to \mathbb{P}^n_{\mathbb{F}}$ given in affine and homogeneous coordinates by $x_{i} \mapsto x_{i}$ (and on closed points by $(a_{0}, a_{1}, \dots, a_{n}) \mapsto (a_{0} : a_{1} : \dots : a_{n})$ for algebraically closed $\mathbb{F}$)

Write $\mathbb{A}_{\mathbb{F}}^{n + 1} \setminus \{ 0 \}$ as the union of all the distinguished opens $D(x_{i}) \cong \operatorname{Spec} \mathbb{F}[x_{0}, x_{1}, \dots, x_{n}]_{x_{i}}$. We want to map these to [[Algebraic geometry --- rising-sea/notes/Projective schemes#_definition _ homogeneous vanishing sets, projective distinguished open|projective distinguished opens]] $D_{+}(x_{i}) = \operatorname{Spec} (\mathbb{F}[x_{0}, x_{1}, \dots, x_{n}]_{x_{i}})_{0}$. There's an obvious map here — just the inclusion of the degree $0$ part into the whole ring. They agree on intersections — on $D(x_{i} x_{j}) \to D_{+}(x_{i} x_{j})$ they both restrict to the map induced by the inclusion $(\mathbb{F}[x_{0}, x_{1}, \dots, x_{n}]_{x_{i} x_{j}})_{0} \to \mathbb{F}[x_{0}, x_{1}, \dots, x_{n}]_{x_{i} x_{j}}$. Thus, they glue to give a scheme map.

---