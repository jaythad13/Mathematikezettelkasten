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

Suppose $\pi : X \to Y$ is a morphims of local ringed spaces. Then, for every affine open $\operatorname{Spec} A \subseteq X$ with $\pi^\text{img}(\operatorname{Spec} A) \subseteq \operatorname{Spec} B$, the morphism $\pi_{\mid \operatorname{Spec} A} : \operatorname{Spec} A \to \operatorname{Spec} B$ is a [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#The morphism of affine schemes|morphism of affine schemes]] (induced by a ring homomorphism $B \to A$).