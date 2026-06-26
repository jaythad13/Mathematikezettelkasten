---
tags:
- alg-geo
- uc-2026/de-rham/1
- uc-2026/de-rham/3
- michael-barz
---

Because schemes are hard, we won't use them. Instead we will use algebraic prespaces. They are the most basic abstraction we could ask for — all we ask for is that they have a realisation over every number system (every ring).

##### _definition:_ algebraic prespaces, morphisms of prespaces

An **(algebraic) prespace** is a (covariant) [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|functor]] $X : \mathsf{Ring} \to \mathsf{Set}$, or equivalently, a contravariant functor $X : \mathsf{AffSch} \to \mathsf{Set}$.

A **morphism of prespaces** is a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformation]] of functors.

Together these define the category of algebraic prespaces $\mathsf{PreSpc}$.

---

We can identify schemes with corresponding prespaces. By [[Algebraic geometry --- rising-sea/notes/Yoneda's lemma#_lemma _ Yoneda's fanciest lemma|Yoneda's lemma]], this identifies an [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition _ affine scheme|affine scheme]] $\operatorname{Spec} A$ with its functor of ring-valued points $B \mapsto (\operatorname{Spec} A)(B) = \operatorname{Mor}_{\mathsf{Ring}}(A, B)$. In general, a scheme $X$ corresponds to the (contravariant) functor of $\operatorname{Spec} A$[[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_definition _ scheme-valued points of a scheme|-points]] of $X$, with $A \mapsto \operatorname{Mor}(\operatorname{Spec} A, X) = X(A)$. Note that since this is contravariant on affine schemes, it is covariant on rings. Also, the category of algebraic prespaces has a final object $\operatorname{Spec} \mathbb{Z}$.

### Morphisms of algebraic prespaces

It will be useful for us to have some language of types of morphisms of algebraic prespaces.

##### _definition:_ basic open and closed embeddings or immersions

A **basic closed embedding (immersion) of affine schemes** is a [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_definition _ morphism of affine schemes|morphism]] $\operatorname{Spec} A / \mathfrak{i} \to \operatorname{Spec} A$ (for some ring $A$ and ideal $\mathfrak{i} \subseteq A$).

A **basic open embedding (or immersion) of affine schemes** is a morphism $\operatorname{Spec} A[f^{-1}] \to \operatorname{Spec} A$ (for some ring $A$ and $f \in A$).

A **closed embedding** of algebraic prespaces is a morphism $X \to Y$.

---

##### _definition:_ formally étale

A prespace $X$ is **formally étale** if, for any [[p-adic numbers --- math-177/notes/Hensel's lemma#_definition _ square-zero extension|square-zero extension]] $\varphi : A \to B$, the morphism $X\varphi : X(A) \to X(B)$ is a bijection

---