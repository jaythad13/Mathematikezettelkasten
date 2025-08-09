---
tags:
- cat-th
- rising-sea/1
- rising-sea/1/2
---

Universal properties answer the question "why categories?"

We want to know category theory to make precise the sense in which [[Sheaves|sheaves]] of abelian groups and modules as well as [[Schemes|schemes]] behave like abelian groups, modules, and rings (respectively). This is given by the language of category theory. In the first two cases in particular, want categories that have isomorphism theorems, kernels, cokernels, images, subspaces, and quotients — we want the notion of an [[Abelian categories|abelian category]].

Why do this through category theory? Because it's the cleanest language to do it in, with the best "invariant" definitions of kernels, cokernels, et c given by universal properties. The best elementary example of this is the universal property of the product.

##### _example:_ the universal property of products

There are many types of products — of sets, [[Linear algebra done right --- ladr/notes/Product spaces|vector spaces]], groups, [[Topology --- math-147/notes/Product spaces#_definition _ (finite) product topology|topological spaces]], even of manifolds. We usually define each type of product separately, but really they all possess the same "universal property" which we will define.

The idea is that there isn't one single product, but rather, any two products have a unique isomorphism between them. Consider, for example, the product of sets. Both $\{ \{ u, \{ v \} \} \mid u \in U, v \in V \}$ and $\{ \{ \{ u \}, v \} \mid u \in U, v \in V \}$ are reasonable definitions of $U \times V$, and there's an obvious sense in which it doesn't matter which one you pick. Similarly, it doesn't matter how you cut up two manifolds into charts, take products and glue them back together — there's some sense in which all these encodings are the same.

A product $M \times N$ of $M$ and $N$ is a set (object) with projection functions (morphisms) $pr_{M}, pr_{N}$ to $M$ and $N$ respectively, such that for any $P'$ with projections $pr_{M}', pr_{N}'$ to $M$ and $N$, there is a unique $\Pi = \Pi_{P} : P' \to M \times N$ so that $pr_{M}' = pr_{M} \circ p$ and $pr_{N}' = pr_{N} \circ \Pi$ as below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P' \ar[rrd, "pr_{N}'", bend left] \ar[ddr, "pr_{M}'"', bend right] \ar[rd, "\exists ! \Pi", dashed] \\
		& M \times N \ar[r, "pr_{N}"'] \ar[d, "pr_{M}"] & N \\
		& M
	\end{tikzcd}
\end{document}
```

Now if $M \times_{1} N$ and $M \times_{2} N$ are both products, then there exist $\Pi_{1} : M \times_{1} N \to M \times_{2} N$ and $\Pi_{2} : M \times_{2} N \to M \times_{1} N$ with the projection maps to $M$ factoring as $pr_{M, 1} = pr_{M, 2} \circ \Pi_{1}$ and $pr_{M, 2} = pr_{M, 1} \circ \Pi_{2}$. Thus, $pr_{M, 1} = pr_{M, 1} \circ (\Pi_{2} \circ \Pi_{1})$, and similarly $pr_{N, 1} = pr_{N, 1} \circ (\Pi_{2} \circ \Pi_{1})$. 

That is, $\Pi_{2} \circ \Pi_{1}$ is a map from $M \times_{1} N$ to itself such that the projection maps factor through it. But $\operatorname{id}_{M \times_{1} N}$ is already such a map and this map is unique. Thus $\Pi_{2} \circ \Pi_{1} = \operatorname{id}_{M \times_{1} N}$ and a similar argument shows $\Pi_{1} \circ \Pi_{2} = \operatorname{id}_{M \times_{2} N}$. That is, $\Pi_{1}$ and $\Pi_{2}$ give the unique bijection (isomorphism) $M \times_{1} N \cong M \times_{2} N$.

Note that the universal property doesn't construct a product of sets, it just uniquely characterises it. This is true of universal properties in general. (Also note that the notion of universal property is not formally defined).

With the language of category theory we can characterise constructions like the product in general [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ (locally small) categories, objects, morphisms|categories]]. We will show that these constructions are unique up to unique [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ isomorphisms, inverse morphisms|isomorphism]]. The uniqueness of the isomorphism is important! This is an informal definition of what it means to be defined by universal property. Again, as we noted previously, this doesn't guarantee existence in every category. 

### Definitions by universal property

For the rest of this note let $\mathscr{C}$ be a category. We already showed that products are unique up to unique isomorphism. Just replace set with object, function with morphism, bijection with isomorphism et c. in the example above.

##### _definition:_ products

A product $M \times N$ of $M, N \in \mathscr{C}$ is the unique object with projection morphisms $pr_{M}, pr_{N}$ to $M$ and $N$ respectively, such that for any $P'$ with morphisms $pr_{M}', pr_{N}'$ to $M$ and $N$, there is a unique $\Pi = \Pi_{P'} : P' \to M \times N$ that each of the morphisms factors through. That is, we have $pr_{M}' = pr_{M} \circ \Pi$ and $pr_{N}' = pr_{N} \circ \Pi$ so that the diagram below commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P' \ar[rrd, "pr_{N}'", bend left] \ar[ddr, "pr_{M}'"', bend right] \ar[rd, "\exists ! \Pi", dashed] \\
		& M \times N \ar[r, "pr_{N}"'] \ar[d, "pr_{M}"] & N \\
		& M
	\end{tikzcd}
\end{document}
```


Products of $M_{i} \in \mathscr{C}$ indexed by $i \in \mathscr{I}$ are defined as the unique object $\prod_{i \in \mathscr{I}} M_{i}$ with projection morphisms $pr_{M}$ to each $M_{i}$ such that the analogous universal property follows for $P$ with morphisms to each $M_{i}$. 

As part of a more general theme where valid statements in category theory can be obtained by reversing all the arrows, we can obtain coproducts by reversing all the arrows in the definition of the product.

##### _definition:_ coproducts, direct sums

The coproduct of $M_{i} \in \mathscr{C}$ indexed by $i \in \mathscr{I}$ is the unique object $\coprod_{i \in \mathscr{I}} M_{i}$ with maps $pr_{i} : M_{i} \to \coprod M_{i}$ such that, for every $P'$ with maps $pr_{i}' : M_{i} \to P'$, there is a unique $\amalg = \amalg_{P'} : \coprod_{i \in \mathscr{I}} M_{i} \to P'$ with $pr_{i}' = \amalg_{P'} \circ pr_{i}$.

In many of the categories that we are concerned with, the coproduct is the direct sum.

##### _example:_ coproducts of sets

are disjoint unions.

##### _definition:_ initial, final, and zero objects

Let $A \in \mathscr{C}$. $A$ is the unique initial object if there is a unique morphism from $A$ to each $B \in \mathscr{C}$.

$A$ is the unique final object if there is a unique morphism from each $B \in \mathscr{C}$ to $A$.

$A$ is the unique zero object if it is both initial and final.

###### _proof of uniqueness:_

Suppose $A$ and $A'$ in $\mathscr{C}$ are both initial. Then $A$ and $A'$ have unique morphisms (say $a$ and $a'$) to the other. They also have unique morphisms to themselves — the identity morphisms $\operatorname{id}_{A}$ and $\operatorname{id}_{A'}$. Then since $a \circ a' : A' \to A'$, we have $a \circ a' = \operatorname{id}_{A'}$ and similarly $a' \circ a = \operatorname{id}_{A}$. That is, $a$ and $a'$ are inverse isomorphisms and unique.

Now suppose $A, A' \in \mathscr{C}$ are both final. Then $A$ and $A'$ have unique morphisms from the other (again say $a$ and $a'$), and unique morphisms to themselves (the identity morphisms). Since $a \circ a' : A \to A$ we have $a \circ a' = \operatorname{id}_{A}$ and similarly we have $a' \circ a' = \operatorname{id}_{A'}$. Thus, $a$ and $a'$ are unique inverse isomorphisms.

##### _example:_ initial and final objects in specific categories

1) The initial object in $\mathsf{Set}$ is the empty set $\text{Ø}$. The final object is the singleton set $\{ * \}$.
2) The initial object in $\mathsf{Ring}$ is $\mathbb{Z}$ by the map $\mathbb{Z} \to A$ generated by $1 \mapsto 1_{A}$ (recall that $\mathsf{Ring}$ only includes unital rings). The final object is the trivial ring. Note that the trivial ring is not initial because ring homomorphisms should send multiplicative identities to multiplicative identities.
3) The initial object in $\mathsf{Top}$ is the empty set and the final object is the one point space $\{ * \}$, just like in $\mathsf{Set}$.

[[Algebraic geometry --- rising-sea/notes/Localisation, categorically|Localisation of rings and modules]] can both be defined by universal property as can [[Tensor products, categorically|tensor products]]. [[Fibred products]] will be an important construction for geometry, defined by universal property as well.

Two more examples of properties defined by universal property are monomorphisms and epiomorphisms, categorifying the notions of injections and surjections respectively.

##### _definition:_ monomorphisms, epimorphisms

A morphism $\pi : X \to Y$ is a monomorphism if any two morphisms $\mu_{1}, \mu_{2} : Z \to X$ that agree on composition with $\pi$ to $Y$ (that is, $\pi \circ \mu_{1} = \pi \circ \mu_{2}$) are the same morphism (that is, $\mu_{1} = \mu_{2}$). Equivalently, $h^Z(\pi) : \operatorname{Mor}(Z, X) \to \operatorname{Mor}(Z, Y)$ is injective.

A morphism $\pi : X \to Y$ is an epimorphism if any two morphisms $\mu_{1}, \mu_{2} : Y \to Z$ that agree on (pre-)composition with $\pi$ as morphisms $X \to Z$ (that is, $\mu_{1} \circ \pi = \mu_{2} \circ \pi$) are the same morphism (that is, $\mu_{1} = \mu_{2}$). Equivalently, $h_{Z}(\pi) : \operatorname{Mor}(Y, Z) \to \operatorname{Mor}(X, Z)$ is injective.

In any concrete category (with a faithful functor to $\mathsf{Set}$), any injection is a monomorphism and any surjection is an epimorphism. However, the converse is not true. In $\mathsf{Ring}$, $\mathbb{Z} \to \mathbb{Q}$ is an epimorphism (since a morphism $\mathbb{Q} \to A$ is determined by the values it takes at $\mathbb{Z}$). Similarly $\mathbb{Q} \to \mathbb{Q} / \mathbb{Z}$ is a monomorphism of (divisible) groups

Monomorphisms can also be characterised by their interaction with fibred products.

##### _proposition:_ monomorphisms induce diagonal isomorphisms

A morphism $\pi : X \to Y$ is a monomorphism if and only if the [[Algebraic geometry --- rising-sea/notes/Fibred products#_definition _ fibred product|fibred product]] $X \times_{Y} X$ exists and the induced diagonal morphism $\delta_{\pi} : X \to X \times_{Y} X$ is an isomorphism.

##### _proposition:_ monomorphisms of bases induce isomorphisms of fibre products

If $Y \to Z$ is a monomorphism (and there are morphisms $X_{1}, X_{2} \to Y$, and all relevant fibred products exist), then [[Algebraic geometry --- rising-sea/notes/Fibred products#_lemma _ morphisms of bases induce morphisms of fibred products|the morphism]] $X_{1} \times_{Y} X_{2} \to X_{1} \times_{Z} X_{2}$ is an isomorphism.