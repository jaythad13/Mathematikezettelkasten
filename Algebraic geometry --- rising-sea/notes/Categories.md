---
tags:
- cat-th
- rising-sea/1/1
---

Categories are the language for dealing with objects of a certain type and the maps between them, functors are the maps between categories, and natural transformations are the deformations of functors into each other.

##### _definition:_ (locally small) categories, objects, morphisms

A category $\mathscr C$ is a collection of objects denoted $\operatorname{obj} \mathscr{C}$ or just $\mathscr{C}$ by abuse of notation and a set of morphisms between each pair of objects $A, B \in \mathscr{C}$, denoted $\operatorname{Mor}_{\mathscr{C}}(A, B)$ (with the subscript dropped when the category is clear from context) such that the following hold.

There is an associative composition function $\operatorname{Mor}(B, C) \times \operatorname{Mor}(A, B) \to \operatorname{Mor}(A, C)$ by $(g, f) \mapsto g \circ f$. For each $A \in \mathscr{C}$ there is an identity function $\operatorname{id}_{A}$ such that $f \circ \operatorname{id}_{A} = f$ for $f \in \operatorname{Mor}(A, B)$ and $\operatorname{id}_{A} \circ f = f$ for $f \in \operatorname{Mor}(B, A)$.

It is not hard to see that the identity morphism on a category is unique.

An element $f \in \operatorname{Mor}(A, B)$ is typically denoted $f : A \to B$ and is said to have domain or source $A$ and codomain or target $B$.

Categories have an obvious notion of isomorphisms.

##### _definition:_ isomorphisms, inverse morphisms

Given a category $\mathscr{C}$, $A, B \in \mathscr{C}$, and $f : A \to B$, we say $f$ is an isomorphism if there exists some $g: B \to A$ such that $g \circ f = \operatorname{id}_{A}$ and $f \circ g = \operatorname{id}_{B}$.

We say $f, g$ are inverses of each other, denoted $f = g^{-1}$ and $g = f^{-1}$.

This of of course gives rise to the notion of automorphisms, the set of which form a group.

##### _definition:_ automorphisms, automorphism group

An isomorphism $f : A \to A$ is an automorphism.

The set of all automorphisms forms a [[Abstract Algebra I --- math-171/notes/Groups, and why you should care#_definition _ group, identity, inverse|group]] $\operatorname{Aut} A$ under composition with $\operatorname{id}_{A}$ the identity and inverse morphisms the inverses.

Finally, just as there is a notion of subspaces in most categories we're familiar with, there is a notion of a subcategory.

##### _definition:_ subcategory

A subcategory $\mathscr{A}$ of a (super)category $\mathscr{B}$ is a category with $\operatorname{obj} \mathscr{A} \subseteq \operatorname{obj} \mathscr{B}$ (ignoring set-theoretic issues) such that for each $A, B \in \mathscr{A}$, we have $\operatorname{Mor}_{\mathscr{A}}(A, B) \subseteq \operatorname{Mor}_{\mathscr{B}}(A, B)$ with the endomorphisms of any $A \in \mathscr{A}$ including $\operatorname{id}_{\mathscr{A}}$, and including all compositions of morphisms.

We have defined a subcategory so that it really is a category with the same composition as the supercategory it sits in (we could remove the "is a category" from the definition).

The notion of a subcategory is perhaps better explained with the notion of a [[Algebraic geometry --- rising-sea/notes/Functors and natural transformations#_definition _ functor|functor]] (there is an inclusion functor from any subcategory to the supercategory)

### Lots of examples

##### _example:_ nice categories

1) The simplest (non-trivial) example of a category is $\mathsf{Set}$, the with sets as objects and where an arrow $f: A \to B$ is a function $A \to B$. The choice for identity function is obvious ($\operatorname{id}_{A} : a \mapsto a$), and so is the composition — just regular function composition.

Note that while we did specify them for sets, usually the identity and compositions for a category are obvious and are thus, not specified.

2) $\mathsf{Grp}$ is a category with [[Abstract Algebra I --- math-171/notes/Groups, and why you should care#_definition _ group, identity, inverse|groups]] as objects and [[Abstract Algebra I --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphisms]] as arrows, and similarly, $\mathsf{Ring}$ is a category with ([[Abstract Algebra I --- math-171/notes/Rings#_definition _ ring with identity, unital rings|unital]]) [[Abstract Algebra I --- math-171/notes/Rings#_definition _ rings|rings]] as objects and [[Abstract Algebra I --- math-171/notes/Ring homomorphisms#_definition _ ring homomorphisms|ring homomorphisms]] as arrows, and $\mathsf{Vec}_{k}$ is a category with [[Linear algebra done right --- ladr/notes/Vector spaces#_definition _ vector space|vector spaces]] as objects and [[Linear maps|linear maps]] as arrows. We can define similarly $\mathsf{Ab}$ for [[Abstract Algebra I --- math-171/notes/Groups, and why you should care#_definition _ abelian group, commutative group|abelian groups]],  $\mathsf{CRing}$ for [[Abstract Algebra I --- math-171/notes/Rings#_definition _ commutative ring|commutative rings]], $\mathsf{Field}$ for [[Abstract Algebra I --- math-171/notes/Fields#_definition _ fields|fields]], and $\mathsf{Mod}_{A}$ for modules over commutative ring $A$ (or specify with some similar symbol the category of left/right modules over non-commutative $A$). In fact, $\mathsf{Ab}$, $\mathsf{Vec}_{k}$, and $\mathsf{Mod}_{A}$ are all examples of [[Abelian categories|abelian categories]] with the first two subcategories of the latter in the special cases $A = \mathbb{Z}$ and $A = k$.
3) $\mathsf{Top}$ is the category with [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological spaces]] as objects and [[Topology --- math-147/notes/Continuous functions#_definition _ continuity|continuous maps]] as arrows.

All these examples are nice because they are sets with additional structure — the objects are sets, their morphisms are some subset of all set functions between them, and their composition is function composition. However, we can get categories that don't obviously correspond in this way.

##### _example:_ discrete categories

The minimal categories are those where the only maps are the identities of the object. Of these, the most silly is the category with no objects and no morphisms.

##### _example:_ every group is an entire category, groupoids, monoids, the fundamental groupoid

$\mathsf{Grp}$ is the category of all groups in an obvious way, but we can also think of each group $G$ as a whole category in itself. Specifically, a group is a category with only one object, where every map is an isomorphism. The object is just the set $G$, and each isomorphism is left or right multiplication by some $g \in G$ with the identity morphism corresponding to the identity. If we identify $G$ with a category $\mathscr{G}$ then $G \cong \operatorname{Aut} \mathscr{G}$.

This is a special case of both groupoids and monoids. A groupoid is a category where every map is an isomorphism, and a monoid is a category with only one object. This definition of a monoid can be reconciled with the usual one in exactly the same way as for groups. A group is then a groupoid that is also a monoid.

An example of a groupoid is the subcategory of $\mathsf{Grp}$ containing all $\mathbb{Z} / p \mathbb{Z}$ with $p$ prime and no trivial morphisms. Distinct $\mathbb{Z} / p \mathbb{Z}$ and $\mathbb{Z} / q \mathbb{Z}$ have no non-trivial morphisms between them (by [[Abstract Algebra I --- math-171/notes/Lagrange's theorem#_theorem _ Lagrange's theorem|Lagrange's theorem]] a non-trivial morphism would force $\gcd(p, q) > 1$) and no non-trivial non-invertible endomorphisms for the same reason. Thus, the groupoid would just consist of $\mathbb{Z} / p \mathbb{Z}$s and their automorphisms.

A more interesting example of a groupoid is the fundamental groupoid of a topological space $X$. It is the category with objects corresponding to points $x \in X$ and morphisms between them corresponding to [[Topology --- math-147/notes/The fundamental group#_definition _ path homotopy, equivalence|homotopy classes of paths]] between them. Then the automorphism group of any point $x_{0} \in X$ is [[Topology --- math-147/notes/The fundamental group#_definition _ fundamental group|the fundamental group]] $\pi(X, x_{0})$ based at $x_{0}$.

##### _example:_ preorders and posets

A preorder is a reflexive transitive binary relation $\le$. A preordered set is a set $\mathscr{C}$ with a preorder $\le$ on it. A poset (partially ordered set) is a preordered set where if $A \le B$ and $B \le A$, we must have $A = B$.

Our notation is suggestive  — the categorical notion corresponding to a preordered set is a category $\mathscr{C}$ where there is at most one arrow in $\operatorname{Mor}(A, B)$. A partially ordered set corresponds to the only isomorphisms in the category being the identities.

Note that we can choose $A \le B$ to correspond to an arrow in $\operatorname{Mor}(A, B)$ or an arrow in $\operatorname{Mor}(B, A)$. [[Basic category theory --- basic-cat/attachments/texts/Basic Category Theory.pdf#page=27|Leinster]] chooses the former. [[Algebraic geometry --- rising-sea/attachments/texts/The Rising Sea.pdf#page=31|Vakil]] chooses the latter. This phenomenon is explained by opposite/dual categories

##### _definition:_ opposite (or dual) categories

Given a category $\mathscr{C}$, its opposite (or dual) category $\mathscr{C}^\text{opp}$ is the category with $\operatorname{obj (\mathscr{C})} = \operatorname{obj} (\mathscr{C}^\text{opp})$, $\operatorname{Mor}_{\mathscr{C}^\text{opp}}(A, B) = \operatorname{Mor}_{\mathscr{C}}(B, A)$ for all objects $A, B$.

Note that the composition in the opposite category goes the opposite way — for $f : A \to B$ and $g : B \to C$ in $\mathscr{C}$, we have $g \circ f : A \to C$. However, since $f : B \to A$ and $g : C \to B$ in $\mathscr{C}^\text{opp}$, their composition is $f \circ g : C \to A$. For this reason, we sometimes denote the opposite category morphism corresponding to $f : A \to B$ by $f^\text{opp} : B \to A$.

##### _example:_ the inclusion category of subsets or open sets

An important example coming from preorders and posets is that of the inclusion category. Given a set $X$, this is the poset on its set of subsets $2^X$ by inclusion — for subsets $U, V$ there is a morphism $U \to V$ exactly if $U \subseteq V$.

For a topological space $(X, \mathcal{T})$ we often restrict this category to open subsets $U, V \in \mathcal{T}$.