---
tags:
- comm-alg
- math-189AA/7
---

Let $A$ be a (commutative, unital) ring.

Module homomorphisms are the only thing they can be. Essentially, they are $A$-linear transformations.

##### _definition:_ $A$-module homomorphisms

If $M$ and $N$ are $A$-modules, then a map $\varphi : M \to N$ is an $A$-module homomorphism if it is a [[Abstract algebra --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphism]] and $\varphi(am) = a \varphi(m)$ for all $a \in A$, $m \in M$.

---

##### _examples:_

1) If $N \subseteq M$ is a [[Commutative algebra --- math-189AA/notes/Modules#_definition _ submodule, proper submodule|submodule]] and then there is a canonical surjection $M \to M / N$ to the [[Commutative algebra --- math-189AA/notes/Modules#_definition _ quotient module|quotient module]] by $m \mapsto m + N$.
2) The containment $\mathbb{R} \subseteq \mathbb{C}$ is an $\mathbb{R}$-module homomorphism.
3) $\mathbb{Z} \to (2) \to \mathbb{Z}$ by multiplying by $2$ is a $\mathbb{Z}$-module homomorphism.

---

Module homomorphisms satisfy basic properties.

##### _proposition:_ basic algebraic properties of module homomorphisms

Suppose $M, N$ are $A$-modules and $\varphi : M \to N$ is an $A$-module homomorphism. Then
1) $\varphi(0) = 0$.
2) $\varphi(-m) = - \varphi(m)$.

---

Module homomorphisms also satisfy reasonable properties that mean that they form a [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ (locally small) categories, objects, morphisms|category]], and in fact an [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ abelian categories|abelian category]].

##### _proposition:_ $A$-modules form a category

Morphisms of $A$-modules compose (associatively).

There is an identity morphism $\operatorname{id}_{M} : M \to M$ on each $A$-module $M$ such that $\operatorname{id}_{M} \circ \varphi = \varphi$ and $\varphi \circ \operatorname{id}_{M} = \varphi$ for all $\varphi : N \to M$ and $\varphi : M \to N$ respectively.

---

##### _definition:_ kernels, cokernels, and images

Let $\varphi : M \to N$ be a morphism of $A$-modules

Then the **kernel** of $\varphi$ is the submodule $\ker \varphi = \{ m \in M \mid \varphi(m) = 0 \} \subseteq M$ with the inclusion $\ker \varphi \to M$.

The **image** of $\varphi$ is the submodule $\operatorname{img} \varphi = \{ n \in N \mid \exists m \in M, \varphi(m) = n \} \subseteq N$ with the inclusion $\operatorname{img} \varphi \to N$

The **cokernel** of $\varphi$ is $\operatorname{coker} \varphi = N / \operatorname{img} \varphi$ with the map $N \to \operatorname{coker} \varphi$.

---

Note that these all satisfy [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ kernels, cokernels|their definitions in an arbitrary abelian category]].