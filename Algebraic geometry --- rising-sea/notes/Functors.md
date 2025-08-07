---
tags:
- rising-sea/1/1
- cat-th
---

Functors are the "morphisms of [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ (locally small) categories, objects, morphisms|categories]]". They give function on objects as well as a function on morphisms that preserves their source and target. If each category is a multi-graph, then a functor is a [[Geometric group theory --- rtg-2025/notes/Graph actions and Cayley graphs#_definition _ graph morphism, graph isomorphism, graph automorphism|graph morphism]] between them.

##### _definition:_ (covariant, contravariant) functors

For categories $\mathscr{A}$ and $\mathscr{B}$, a covariant functor $F : \mathscr{A} \to \mathscr{B}$ is a map $F : \operatorname{obj} \mathscr{A} \to \operatorname{obj} \mathscr{B}$, and for each pair $A_{1}, A_{2} \in \operatorname{obj} \mathscr{A}$, a function $\operatorname{Mor}_{\mathscr{A}}(A_{1}, A_{2}) \to \operatorname{Mor}_{\mathscr{B}}(F(A_{1}), F(A_{2}))$ such that the following hold. (By abuse of notation, we write the function of morphisms also as $f \mapsto F(f)$.)

- $F(\operatorname{id}_{A}) = \operatorname{id}_{F(A)}$ for each $A \in \mathscr{A}$
- $F(g \circ f) = F(g) \circ F(f)$ for $f : A_{1} \to A_{2}$ and $g : A_{2} \to A_{3}$.

A contravariant functor $F : \mathscr{A} \to \mathscr{B}$ is a covariant functor $F : \mathscr{A}^\text{opp} \to \mathscr{B}$ (from the [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ opposite (or dual) categories|opposite category]]) or equivalently the pair of a map on objects, and a function $\operatorname{Mor}_{\mathscr{A}}(A_{1}, A_{2}) \to \operatorname{Mor}_{\mathscr{B}}(F(A_{2}), F(A_{1}))$ preserving identities and having $F(g \circ f) = F(f) \circ F(g)$.

Functors compose naturally —

##### _definition:_ composition of functors

For functors $F : \mathscr{A} \to \mathscr{B}$ and $G : \mathscr{B} \to \mathscr{C}$, the composition $G \circ F : \mathscr{A} \to \mathscr{C}$ is defined by $A \mapsto G(F(A))$ on objects and $f \mapsto G(F(f))$ on morphisms as well.

Note that this, with the identity functor on a category would suggest that there is a category of categories but this requires set theory to really deal with.

##### _examples:_ trivial functors

The identity functor is the identity on objects and morphisms of any category $\mathscr{A}$.

Forgetful functors are less trivial. We will characterise them fully later, but they are fully explained by examples like $\mathsf{Vec}_{k} \to \mathsf{Set}$ that just forgets the vector space structure on a set, an preserves morphisms, or similarly, $\mathsf{Mod}_{A} \to \mathsf{Ab}$.

##### _examples:_ functors from topology

The map that sends pointed [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological spaces]] $(X, x_{0})$ to their [[Topology --- math-147/notes/The fundamental group#_definition _ fundamental group|fundamental group]] $\pi_{1}(X, x_{0})$ is actually functorial, with (pointed) continuous maps $f : (X, x_{0}) \to (Y, f(x_{0}))$ inducing group homomorphisms $f_{*} : \pi_{1} (X, x_{0}) \to \pi_{1}(Y, f(x_{0}))$.

Similarly, each $n$th homology is a covariant functor $\mathsf{Top} \to \mathsf{Ab}$.

##### _example:_ the functor of points and its opposite

On any category $\mathscr{C}$, the contravariant functor of $A$-points is $h_{A}$ by $B \mapsto \operatorname{Mor}(B, A)$ on objects. On morphisms, for each $f : B \to C$ we have $\operatorname{Mor}(C, A) \to \operatorname{Mor}(B, A)$ by $g \mapsto g \circ f$ (for each $g : C \to A$). It's called the functor of points because, the $B$-points of a scheme $A$ are just morphisms $B \to A$.

For example, the functor $\mathsf{Vec}_{k} \to \mathsf{Vec}_{k}$ by taking duals and dual maps in $\mathsf{Vec}_{k}$ is the functor of $k$-points and the pullback of continuous (real) functions on topological spaces is the functor of $\mathbb{R}$-points $\mathsf{Top} \to \mathsf{Ring}$. In these examples, it's also reasonable to call these functors "points" since the continuous real maps on $X$ look like sections of $\mathbb{R}$ varying over $X$.

There is a similar covariant functor $h^A$ by $B \mapsto \operatorname{Mor}(A, B)$ on objects and sending each $f : B \to C$ to the map $\operatorname{Mor}(A, B) \to \operatorname{Mor}(A, C)$ by $g \mapsto f \circ g$ (for each $g : A \to B$). 

### Faithfulness and fullness

Functors have properties that look a lot like injectivity and surjectivity. However, instead of the relevant injectivity and surjectivity being on objects, the right notions are on morphisms

##### _definition:_ faithful, full, fully faithful

A (covariant) functor $F : \mathscr{A} \to \mathscr{B}$ is faithful/full if, for each $A_{1}, A_{2} \in \mathscr{A}$ the map $\operatorname{Mor}_{\mathscr{A}}(A_{1}, A_{2}) \to \operatorname{Mor}_{\mathscr{B}}(F(A_{1}), F(A_{2}))$ is injective/surjective respectively. 

$F$ is fully faithful if it is faithful and full.

Contravariant functors $F : \mathscr{A} \to \mathscr{B}$ are faithful/full exactly when the corresponding covariant functors $\mathscr{A}^\text{opp} \to \mathscr{B}$ are faithful/full respectively.

This notion allows us to define a forgetful functor explicitly. A forgetful functor $F : \mathscr{A} \to \mathscr{B}$ is a faithful functor so that the injection on morphisms is actually just an inclusion of the subset $\operatorname{Mor}_{\mathscr{A}}(A_{1}, A_{2}) \subseteq \operatorname{Mor}_{\mathscr{B}}(F(A_{1}), F(A_{2}))$.