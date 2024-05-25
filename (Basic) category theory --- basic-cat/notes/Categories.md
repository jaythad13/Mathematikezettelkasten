---
tags:
- cat-th
- basic-cat
- self-study
---

### An intuitive idea of categories, functors, and natural transformations

A category is a bunch of related (mathematical) things (we call them objects) and the relationships between them (we call them arrows, maps, or morphisms). For example, 
- rings and ring homomorphisms
- topological spaces and continuous maps
or for a more complicated example
- topological spaces with a base point, and homotopy equivalence classes of continuous maps.

While this may look like a every object of a category should be a type of "set with structure" and every arrow should be a "structure-preserving map" categories are broader than just that.

Usually we also have a notion of two objects being equivalent, and after that we don't usually care which one we're working with. It would be senseless to treat every $n$-dimensional vector space over $\mathbb{F}$ as different when [[Prototypical vector spaces|they're all just isomorphic]] to $\mathbb{F}^n$. Similarly for topological spaces, groups, et c.

We can think of categories themselves as objects in the "category of categories" though we don't necessarily think of it as that. The "structure-preserving maps" between them are called functors. For example, we can associate with every topological space its $k$th homology group, and then it turns out that continuous maps correspond with homomorphisms between the groups.

Finally, we can think about a further level of abstraction — maps between functors, called natural transformations, that again have some sense of preserving things. It was in order to formalise this notion that Samuel Eilenberg and Saunders Mac Lane formalised the notions of categories and functors as they are now.

### What is a category?

We've seen enough now that the following definition does not need any more motivation.

##### _definition:_ category

A category $\mathscr{A}$ consists of:
 - a collection (by which strictly, we mean [[Formal classes|class]]), of objects, $\operatorname{ob}(\mathscr{A})$,
 - for each pair $A, B \in \operatorname{ob}(\mathscr{A})$, a collection of arrows between them, $\operatorname{Hom}_{\mathscr{A}}(A, B)$,
 - for each $A \in \operatorname{ob}(\mathscr{A})$, an arrow $\operatorname{id}_{A} \in \operatorname{Hom}_{\mathscr{A}}(A, A)$,
and
 - for all $A, B, C \in \operatorname{ob}(\mathscr{A})$, an associative "composition" function $\operatorname{Hom}_{\mathscr{A}}(A, B) \times \operatorname{Hom}_{\mathscr{A}}(B, C) \to \operatorname{Hom}_{\mathscr{A}}(A, C)$ given by $(f, g) \mapsto g \circ f$ that respects identities — for all $f \in \operatorname{Hom}_{\mathscr{A}}(A, B)$ we have $f \circ \operatorname{id}_{A} = f = \operatorname{id}_{B} \circ f$.

##### _(many) abuses of notation:_ categories

For a category $\mathscr{A}$,
1) sometimes we write $A \in \mathscr{A}$ to mean $A \in \operatorname{ob}(\mathscr{A})$,
2) we often use function notation $f : A \to B$ or $A \xrightarrow{f} B$ to denote arrows $f \in \operatorname{Hom}_{\mathscr{A}}(A, B)$, even though [[#_example:_ posets are categories|arrows need not be functions]],
3) we often write $f \in \operatorname{Hom}(A, B)$, omitting the subscript $\mathscr{A}$, if the category we're working in is obvious,
4) we often write $gf$ to denote $g \circ f$.

##### _note:_ the category "axioms" force unique arrow composition

Given a string $A_{0} \xrightarrow{f_{1}} A_{1} \xrightarrow{f_{2}} \dots \xrightarrow{f_{n}} A_{n}$, there is exactly one way to construct an arrow $A_{0} \xrightarrow{f} A_{n}$ (as long as all $A_{i}$ are distinct). Specifically, all sensible compositions are equal to $f_{1} f_{2} \cdots f_{n}$. Of course if $A_{i} = A_{j}$ we could get rid of the maps between them, and if we know of $A_{0} \xrightarrow{g_{1}} A_{1}$, we can get a different map by using $g_{1}$ instead, and so on, but in the general case, there is only one sensible way.

##### _definition:_ domain, codomain

Carrying on with the analogy that arrows are like functions, for $A \xrightarrow{f} B$ we say $A$ is the domain of $f$ and $B$ is the codomain of $f$. 

##### _examples:_ categories

1) The simplest (non-trivial) example of a category is $\mathsf{Set}$, the with sets as objects and where an arrow $A \xrightarrow{f} B$ is a function $f : A \to B$. The choice for identity function is obvious ($\operatorname{id}_{A} : a \mapsto a$), and so is the composition — just regular function composition.

Note that while we did specify them for sets, usually the identity and compositions for a category are obvious and are thus, not specified.

2) $\mathsf{Grp}$ is a category with groups as objects and group homomorphisms as arrows, and similarly, $\mathsf{Ring}$ is a category with rings as objects and ring homomorphisms as arrows, and $\mathsf{Vect}_{k}$ is a category with vector spaces as objects and linear maps as arrows. We can define similarly, $\mathsf{CRing}$ for commutative rings, $\mathsf{Field}$ for fields, and $\mathsf{Mod}_{R}$ for modules over commutative $R$ (or specify with some similar symbol the category of left/right modules over non-commutative $R$)
3) $\mathsf{Top}$ is the category with topological spaces as objects and continuous maps as arrows.

Finally, something that clearly all of these have in common, and in fact we can define more generally, is the idea of an isomorphism.

##### _definition:_ isomorphism

Given a category, $\mathscr{A}$, $A, B \in \mathscr{A}$, and $A \xrightarrow{f} B$, we say $f$ is an isomorphism if there exists some $B \xrightarrow{g} A$ such that $g \circ f = \operatorname{id}_{A}$ and $f \circ g = \operatorname{id}_{B}$.

##### _examples:_ isomorphisms in different categories

1) The isomorphisms in $\mathsf{Set}$ are just the bijections.
2) The isomorphisms in categories of algebraic structures (like $\mathsf{Grp}$, $\mathsf{CRing}$, $\mathsf{R}_{R}$ et c.) are just the arrows that are also bijections (the regular isomorphisms of these algebraic structures).
3) The isomorphisms in $\mathsf{Top}$ are the homeomorphisms. Note that this isn't just the arrows that are bijections because not every invertible continuous map has a continuous inverse. For example, $f : [0, 1) \to S^1$ by $t \mapsto e^{2 \pi i t}$ (where we think of $S^1$ as embedded in $\mathbb{C}$) is bijective and continuous, but $f^{-1}$ is not continuous at $1 \in \mathbb{C}$.

