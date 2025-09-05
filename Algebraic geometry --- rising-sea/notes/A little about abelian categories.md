---
tags:
- rising-sea/1/5
- cat-th
- hom-alg
---

Abelian categories generalise the notions of kernels, cokernels, and the like from linear algebra (over arbitrary rings) to complexes and sheaves of them and other similar objects. We will not show, however, that our generalisations are "correct" in that they behave like we expect them to.

### Additive categories

Additive categories are abelian categories without all the bells and whistles. Some prototypical examples are the category of free $A$-modules or the category of $\mathbb{C}$-Banach spaces

##### _definition:_ additive category, homomorphism, additive functor

A category $\mathscr{C}$ is **additive** if it satisfies the following properties
1) For each $A, B \in \mathscr{C}$, the set of morphisms $\operatorname{Mor}_{\mathscr{C}}(A, B)$ is also an [[Abstract algebra --- math-171/notes/Groups, and why you should care#_definition _ abelian group, commutative group|abelian group]] such that composition of morphisms distributes over addition.
2) It has a [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ initial, final, and zero objects|zero object]] denoted $0$.
3) It has [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ products|products]] of any pair of objects, and thus, by induction [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_examples _ products and fibred products as limits|products of any finite number of objects]]

In an additive category, the morphisms are often called **homomorphisms** and denoted $\operatorname{Hom}(A, B)$.

A functor between additive categories, that is a [[Abstract algebra --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphism]] on morphisms is an **additive functor**.

A number of important facts follow by abstract nonsense and this definition. 
- Finite products are also finite coproducts are also finite direct sums. We use $\oplus$ for all of them.
- Additive functors preserve $0$ objects (since $Z = 0$ if and only if $\operatorname{id}_{Z} = 0$)
- The $0$ object is so named because every $0$ morphism $A \to B$ factors as $A \to 0 \to B$.
- One can define an additive category  (as Lurie does) so that we naturally get a commutative monoid on $\operatorname{Hom}(A, B)$ by the composition $A \to B \times B \to B \oplus B \to B$ (with the first map $(f, g)$). Requiring this commutative monoid to be an abelian group is sufficient to get an abelian category.

##### _examples:_ additive categories

Clearly $\mathsf{Mod}_{A}$ (and as a special case $\mathsf{Ab}$) are additive categories. However, they satisfy the stricter axioms of an abelian category as well are additive catgegories,. oHowever, they asatisfiy the stroiricter axioms of an aebelian category as well.

### Abelian categories

Abelian categories preserve some extra jazz — notably kernels and cokernels.

##### _definition:_ kernels, cokernels

Let $\mathscr{C}$ be a category with a $0$-object (and thus, $0$-morphisms). The **kernel** (unique up to unique isomorphism if it exists) of a morphism $\varphi : A \to B$ is an object $\ker f$ with an (inclusion) morphism $i : \ker f \to A$ such that $\varphi \circ i = 0$ and any $i' : K \to A$ with $f \circ i' = 0$ factors uniquely through $i$.

Equivalently, the kernel is the limit of the diagram
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& 0 \ar[d] \\
		A \ar[r, "f"] & B
	\end{tikzcd}
\end{document}
```

The **cokernel** is the colimit of the diagram below. That is, it is an object $\operatorname{coker} f$ with a morphism $j : B \to \operatorname{coker} f$ such that $j \circ f = 0$ and any $j' : A \to K$ with $j' \circ f = 0$ factors uniquely through it.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		A \ar[d] \ar[r, "f"] & B \\
		0
	\end{tikzcd}
\end{document}
```

##### _definition:_ subobjects, quotient objects

If $i : A \to B$ is a [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ monomorphisms, epimorphisms|monomorphism]], then $A$ is a **subobject** of $B$.

If $j : A \to B$ is an [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ monomorphisms, epimorphisms|epimorphism]], then $B$ is a **quotient object** of $A$.

##### _definition:_ abelian categories

An abelian category is an additive category satisfying three additional properties.
1) The kernel and cokernel exist for every map.
2) Every monomorphism is the kernel of its cokernel.
3) Every epimorphism is the cokernel of its kernel.

In some really nice abelian categories, the last two conditions are saying the following. For $f : A \to B$ injective we have $\operatorname{img} f = A$ and for $f$ surjective, $B \cong A / \ker f$ (which is just the [[Abstract algebra --- math-171/notes/Group isomorphism theorems#The first isomorphism theorem|first isomorphism theorem]]). These generalise to definitions of the image and quotient.

##### _definition:_ images

The **image** of a morphism $f : A \to B$ is $\operatorname{img} f = \ker (\operatorname{coker} f)$.

$f$ factors uniquely through $\operatorname{img} f \to B$ whenever it exists. $A \to \operatorname{img} f$ is an epimorphism and the cokernel of $\ker f \to A$. These are not easy to prove

##### _definition:_ quotients

The **quotient** of a monomorphism $f : A \to B$ is $\operatorname{coker} f$, denoted $B / A$.

### Freyd–Mitchell and diagram chasing

Typically one proves facts about abelian categories by following elements through the diagram. However, there are many abelian categories with objects that don't actually have "elements" because they are not "sets with additional structure". The Freyd–Mitchell embedding theorem allows to chase diagrams anyway — it says any abelian category $\mathscr{C}$ has an exact, [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ faithful, full, fully faithful|fully faithful functor]]  into $\mathscr{C} \to \mathsf{Mod}_{A}$ for some (not-necessarily commutative) ring $A$. We probably won't need this anyway.