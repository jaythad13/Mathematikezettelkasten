---
tags:
- alg-geo
- uc-2026/de-rham/1
- michael-barz
---

Because schemes are hard, we won't use them. Instead we will use algebraic prespaces. They are the most basic abstraction we could ask for — all we ask for is that they have a realisation over every number system (every ring).

##### _definition:_ algebraic prespaces, morphisms of prespaces

An **(algebraic) prespace** is a (covariant) [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|functor]] $X : \mathsf{Ring} \to \mathsf{Set}$.

A **morphism of prespaces** is a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformation]] of functors.

We can identify schemes with corresponding prespaces. The scheme $X$ corresponds to the (contravariant) functor of $\operatorname{Spec} A$[[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_definition _ scheme-valued points of a scheme|-points]] of $X$, with $A \mapsto \operatorname{Mor}(\operatorname{Spec} A, X) = X(A)$. Note that since this is contravariant on affine schemes, it is covariant on rings.

---