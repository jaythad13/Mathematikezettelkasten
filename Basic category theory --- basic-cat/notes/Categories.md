---
tags:
- cat-th
- basic-cat/1.1
- self-study
---

### An intuitive idea of categories, functors, and natural transformations

A category is a bunch of related (mathematical) things (we call them objects) and the relationships between them (we call them arrows, maps, or morphisms). For example, 
- [[Abstract algebra --- math-171/notes/Rings|rings]] and [[Abstract algebra --- math-171/notes/Ring homomorphisms|ring homomorphisms]]
- topological spaces and continuous maps
or for a more complicated example
- topological spaces with a base point, and homotopy equivalence classes of continuous maps.

While this may look like a every object of a category should be a type of "set with structure" and every arrow should be a "structure-preserving map" categories are broader than just that.

Usually we also have a notion of two objects being equivalent, and after that we don't usually care which one we're working with. It would be senseless to treat every $n$-dimensional vector space over $\mathbb{F}$ as different when [[Prototypical vector spaces|they're all just isomorphic]] to $\mathbb{F}^n$. Similarly for topological spaces, groups, et c.

We can think of categories themselves as objects in the "category of categories" though we don't necessarily think of their collection as that. The "structure-preserving maps" between them are called functors. For example, we can associate with every topological space its $k$th homology group, and then it turns out that continuous maps correspond with homomorphisms between the groups.

Finally, we can think about a further level of abstraction — maps between functors, called natural transformations, that again have some sense of preserving things. It was in order to formalise this notion that Samuel Eilenberg and Saunders Mac Lane formalised the notions of categories and functors as they are now.

### What is a category?

We've seen enough now that the following definition does not need any more motivation.

##### _definition:_ category

A category $\mathscr{A}$ consists of:
 - a collection (by which strictly, we mean [[Formal classes|class]]), of objects, $\operatorname{ob}(\mathscr{A})$,
 - for each pair $A, B \in \operatorname{ob}(\mathscr{A})$, a collection of arrows between them, $\operatorname{Mor}_{\mathscr{A}}(A, B)$,
 - for each $A \in \operatorname{ob}(\mathscr{A})$, an arrow $\operatorname{id}_{A} \in \operatorname{Mor}_{\mathscr{A}}(A, A)$,
and
 - for all $A, B, C \in \operatorname{ob}(\mathscr{A})$, an associative "composition" function $\operatorname{Mor}_{\mathscr{A}}(A, B) \times \operatorname{Mor}_{\mathscr{A}}(B, C) \to \operatorname{Mor}_{\mathscr{A}}(A, C)$ given by $(f, g) \mapsto g \circ f$ that respects identities — for all $f \in \operatorname{Mor}_{\mathscr{A}}(A, B)$ we have $f \circ \operatorname{id}_{A} = f = \operatorname{id}_{B} \circ f$.

##### _(many) abuses of notation:_ categories

For a category $\mathscr{A}$,
1) sometimes we write $A \in \mathscr{A}$ to mean $A \in \operatorname{ob}(\mathscr{A})$,
2) we often use function notation $f : A \to B$ or $A \xrightarrow{f} B$ to denote arrows $f \in \operatorname{Mor}_{\mathscr{A}}(A, B)$, even though [[#Atypical categories|arrows need not be functions]],
3) we often write $f \in \operatorname{Mor}(A, B)$, omitting the subscript $\mathscr{A}$, if the category we're working in is obvious,
4) we often write $gf$ to denote $g \circ f$.

##### _note:_ the category "axioms" force unique arrow composition

Given a string $A_{0} \xrightarrow{f_{1}} A_{1} \xrightarrow{f_{2}} \dots \xrightarrow{f_{n}} A_{n}$, there is exactly one way to construct an arrow $A_{0} \xrightarrow{f} A_{n}$ (as long as all $A_{i}$ are distinct). Specifically, all sensible compositions are equal to $f_{1} f_{2} \cdots f_{n}$. Of course if $A_{i} = A_{j}$ we could get rid of the maps between them, and if we know of $A_{0} \xrightarrow{g_{1}} A_{1}$, we can get a different map by using $g_{1}$ instead, and so on, but in the general case, there is only one sensible way.

##### _definition:_ domain, codomain

Carrying on with the analogy that arrows are like functions, for $A \xrightarrow{f} B$ we say $A$ is the domain of $f$ and $B$ is the codomain of $f$. 

##### _examples:_ categories

1) The simplest (non-trivial) example of a category is $\mathsf{Set}$, the with sets as objects and where an arrow $A \xrightarrow{f} B$ is a function $f : A \to B$. The choice for identity function is obvious ($\operatorname{id}_{A} : a \mapsto a$), and so is the composition — just regular function composition.

Note that while we did specify them for sets, usually the identity and compositions for a category are obvious and are thus, not specified.

2) $\mathsf{Grp}$ is a category with [[Abstract algebra --- math-171/notes/Groups, and why you should care#_definition _ group, identity, inverse|groups]] as objects and [[Abstract algebra --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphisms]] as arrows, and similarly, $\mathsf{Ring}$ is a category with rings as objects and ring homomorphisms as arrows, and $\mathsf{Vect}_{k}$ is a category with vector spaces as objects and linear maps as arrows. We can define similarly, $\mathsf{CRing}$ for commutative rings, $\mathsf{Field}$ for fields, and $\mathsf{Mod}_{R}$ for modules over commutative $R$ (or specify with some similar symbol the category of left/right modules over non-commutative $R$)
3) $\mathsf{Top}$ is the category with topological spaces as objects and continuous maps as arrows.

Finally, something that clearly all of these have in common, and in fact we can define more generally, is the idea of an isomorphism.

##### _definition:_ isomorphism

Given a category, $\mathscr{A}$, $A, B \in \mathscr{A}$, and $A \xrightarrow{f} B$, we say $f$ is an isomorphism if there exists some $B \xrightarrow{g} A$ such that $g \circ f = \operatorname{id}_{A}$ and $f \circ g = \operatorname{id}_{B}$.

##### _examples:_ isomorphisms in different categories

1) The isomorphisms in $\mathsf{Set}$ are just the bijections.
2) The isomorphisms in categories of algebraic structures (like $\mathsf{Grp}$, $\mathsf{CRing}$, $\mathsf{R}_{R}$ et c.) are just the arrows that are also bijections (the regular of these algebraic structures).
3) The isomorphisms in $\mathsf{Top}$ are the homeomorphisms. Note that this isn't just the arrows that are bijections because not every invertible continuous map has a continuous inverse. For example, $f : [0, 1) \to S^1$ by $t \mapsto e^{2 \pi i t}$ (where we think of $S^1$ as embedded in $\mathbb{C}$) is bijective and continuous, but $f^{-1}$ is not continuous at $1 \in \mathbb{C}$.

### Atypical categories

Even though categories typically look like collections of sets with structure with structure-preserving-maps as their morphisms, categories don't have to look like this at all. I call these atypical, but it's important to note they aren't trivial or pathological, or even to be avoided. In fact, they can be really useful!

First, however, let's look at some silly trivial examples.

##### _example:_ discrete categories

The minimal categories are those where the only maps are the identities of the object. Of these, the most silly is the category with no objects and no morphisms.

##### _example:_ every group is an entire category, groupoids, monoids

$\mathsf{Grp}$ is the category of all groups in an obvious way, but we can also think of each group $G$ as a whole category in itself. Specifically, a group is a category with only one object, where every map is an isomorphism. The object is just the set $G$, and each isomorphism is left or right multiplication by some $g \in G$.

We can also more generally define groupoids and monoids — categories where the only morphisms are isomorphisms, and categories of only one object respectively.

##### _example:_ preorders and posets

A preorder is a reflexive transitive binary relation $\le$. A preordered set is a set $\mathscr{A}$ with a preorder $\le$ on it. A poset (partially ordered set) is a preordered set where if $A \le B$ and $B \le A$, we must have $A = B$.

Our notation is suggestive  — the categorical notion corresponding to a preordered set is a category $\mathscr{A}$ where there is at most one arrow in $\operatorname{Mor}(A, B)$. A partially ordered set corresponds to the only isomorphisms in the category being the identities.

Note that we can choose $A \le B$ to correspond to an arrow in $\operatorname{Mor}(A, B)$ or an arrow in $\operatorname{Mor}(B, A)$. [[Basic category theory --- basic-cat/attachments/texts/Basic Category Theory.pdf#page=27|Leinster]] chooses the former. [[Algebraic geometry --- rising-sea/attachments/texts/The Rising Sea.pdf#page=31|Vakil]] chooses the latter. This motivates a definition to describe this phenomenon.

### Two ways to make new categories

Posets aren't the only example of this idea that. In fact, every time we chose a real object (even the sets with structure and the functions between them) we made an arbitrary choice about which way the arrows should point — a function $f : A \to B$ can just as naturally be thought about as a morphism from $B$ to $A$, it's just that our usual imagery of functions as arrows makes one way more natural.

This turns out to be way more useful than it seems — because they are essentially the same thing, basically every categorical definition, theorem, and proof has a dual by reversing the arrows.

##### _definition:_ opposite (or dual) categories

Given a category $\mathscr{A}$, its opposite (or dual) category $\mathscr{A}^\text{op}$ is the category with $\operatorname{ob(\mathscr{A})} = \operatorname{ob}(\mathscr{A}^\text{op})$ and $\operatorname{Mor}_{\mathscr{A}^\text{op}}(A, B) = \operatorname{Mor}_{\mathscr{A}}(B, A)$ for all objects of $A, B$.

##### _example:_ $\mathsf{Vect}_{k}^\text{op}$

The opposite category of vector spaces over $k$ is just all of the vector spaces over $k$ with an arrow $t$ between $V$ and $W$ corresponding to a linear map $T : W \to V$. If there's also an arrow $s$ between $U$ and $V$, then there's a linear map $S : V \to U$. Thus, there's an arrow $s \circ t$ between $U$ and $W$ corresponding to the linear map $T \circ S : W \to U$. That is, morphism composition is reversed from the original category.

There's also a really nice (explicit) definition of the product of categories that seems appropriate to include with the opposite category construction. It's exactly what you'd think —

##### _definition:_ product categories

Given categories $\mathscr{A}$ and $\mathscr{B}$, the product category $\mathscr{A} \times \mathscr{B}$ is defined by
$$
\begin{split}
\operatorname{ob}(\mathscr{A} \times \mathscr{B}) & = \operatorname{ob}{\mathscr{A}} \times \operatorname{ob} \mathscr{B} \\
\operatorname{Mor}_{\mathscr{A} \times \mathscr{B}}((A, B), (A', B')) & = \operatorname{Mor}_{\mathscr{A}}(A, A') \times \operatorname{Mor}_{\mathscr{B}}(B, B').
\end{split}
$$

Informally, everything in $\mathscr{A} \times \mathscr{B}$ is a pair of corresponding things in $\mathscr{A}$ and $\mathscr{B}$. The rest of the details (composition, identities) are left as an [[Basic category theory --- basic-cat/attachments/exercises/ex 1/ex 1.1/ex 1.1.pdf#page=3|exercise]].