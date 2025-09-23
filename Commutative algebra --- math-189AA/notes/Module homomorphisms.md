---
tags:
- comm-alg
- math-189AA/7
- math-189AA/8
- math-189AA/9
---

Let $A$ be a (commutative, unital) ring.

Module homomorphisms are the only thing they can be. Essentially, they are $A$-linear transformations.

##### _definition:_ $A$-module homomorphisms, $\operatorname{Hom}_{A}(M, N)$

If $M$ and $N$ are $A$-modules, then a map $\varphi : M \to N$ is an **$A$-module homomorphism** if it is a [[Abstract algebra --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphism]] and $\varphi(am) = a \varphi(m)$ for all $a \in A$, $m \in M$.

The set of all $A$-module homomorphisms $M \to N$ is $\operatorname{Hom}_{A}(M, N)$ (dropping the subscript if the ring is understood).

We say $A$-module homomorphisms $M \to M$ are **endomorphisms** and denote the set of all of them by $\operatorname{End}_{A} M$.

---

Note that $\operatorname{Hom}(M, N)$ is an abelian group under addition of functions. In fact, $\operatorname{Hom}_{A}(M, N)$ is an $A$-module since we can define $(a \varphi)(m) = a \varphi(m)$. This is clearly additive. It is linear because $(a_{1} \varphi)(a_{2} m) = a_{1} a_{2} \varphi(m) = a_{2} (a_{1} \varphi)(m)$. Note that this requires commutativity of $A$.

Since linearity means that composition distributes over addition, $\operatorname{End}_{A} M$ is a not-necessarily-commutative-ring. In fact $M$ is a (left) $\operatorname{End}_{A} M$-module. This is the maximal ring since the definition of a ring action is a homomorphism $A \to \operatorname{End} M$ (where $\operatorname{End} M$ is the (not-necessarily-commutative) ring of abelian group endomorphisms).

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

### Studying homsets

In fact, $\operatorname{Hom}_{A}(M, N)$ forms an $A$-module under pointwise addition and scaling. It can be useful to study this $A$-module structure.

##### _example:_ $\mathbb{Q}$ as a $\mathbb{Z}$-module

$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}, \mathbb{Q}) \cong \mathbb{Q}$ since we have free choice of where to send $1$, and the whole homomorphism is determined by that choice. $\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Q}, \mathbb{Z}) \cong 0$ since there are no $\mathbb{Z}$-module homomorphisms $\mathbb{Q} \to \mathbb{Z}$ (for roughly the same reason that $\mathbb{Z}$ [[Commutative algebra --- math-189AA/notes/Modules#_examples and non-examples _ modules|is never]] a $\mathbb{Q}$-module).

In general $\operatorname{Hom}_{A}(A, M) \cong M$ since each homomorphism is determined by a free choice of $1 \mapsto m$.

---

##### _example:_ another zero homset

Suppose $\mathbb{F}$ is a field. Then what is $\operatorname{Hom}_{\mathbb{F}[x]}(\mathbb{F}[x] / (x^{2}), \mathbb{F}[x])$? Since $x^{2} \varphi(1) = \varphi(x^{2}) = 0$, we must have $\varphi(1) = 0$. Since $\mathbb{F}[x] / (x^{2})$ is generated by $1$, we have $\varphi = 0$.

In general $\operatorname{Hom}_{A}(T(M), N / T(N)) \cong 0$ for similar reasons.

---

In general, homsets can be understood via [[Algebraic geometry --- rising-sea/notes/Functors#_example _ the functor of points and its opposite|the two "functors of points"]]. That is, we have a (covariant) functor $h^M : N \mapsto \operatorname{Hom}(M, N)$ that acts on maps by pushing forward and a (contravariant) functor $h_{M} : N \mapsto \operatorname{Hom}(N, M)$ by pulling back maps $\varphi : N \to P$ to maps $\operatorname{Hom}(P, M) \mapsto \operatorname{Hom}(N, M)$.

##### _example:_ homming scaling

Let $\mu_{a} \in \operatorname{End} M$ be given by $m \mapsto am$. Then $h_{N}(a) : N \to M$ is given by $\varphi \mapsto a \varphi$.

---

We want to know if this functor preserves properties of modules, and thus, if it preserves properties of morphisms of modules. 

##### _example:_ $h^N$ is not right-exact

Consider the canonical $\mathbb{Z}$-module surjection $\varphi : \mathbb{Q} \to \mathbb{Q} / \mathbb{Z}$. Consider the functor $h^{\mathbb{Z} / (2)}(\varphi)$. It sends $\psi : \mathbb{Z} / (2) \to \mathbb{Q}$ to $\varphi \circ \psi : \mathbb{Z} / (2) \to \mathbb{Q} / \mathbb{Z}$. Since $\mathbb{Z} / (2)$ is torsion and and $\mathbb{Q}$ is not, $\operatorname{Hom}(\mathbb{Z} / (2), \mathbb{Q}) = 0$. Since $\operatorname{Hom}(\mathbb{Z} / (2), \mathbb{Q} / \mathbb{Z})$ contains $\mathbb{Z} / (2) \to \mathbb{Z}$ by $0 \mapsto 0$ and $1 \mapsto 1 / 2$, we have that $h^{\mathbb{Z} / (2)}(\varphi) : \operatorname{Hom}(\mathbb{Z} / (2), \mathbb{Q}) \to \operatorname{Hom}(\mathbb{Z} / (2), \mathbb{Q} / \mathbb{Z})$ is not surjective. That is, $h^{\mathbb{Z} / 2}(\varphi)$ does not preserve surjectivity.