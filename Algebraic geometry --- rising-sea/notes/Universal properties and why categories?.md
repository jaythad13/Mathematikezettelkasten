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

A product $M \times N$ of $M$ and $N$ is a set (object) with projection functions (morphisms) $\mu, \nu$ to $M$ and $N$ respectively, such that for any $P$ with projections $\mu', \nu'$ to $M$ and $N$, there is a unique $p : P \to M \times N$ so that $\mu' = \mu \circ p$ and $\nu = \nu \circ p$ as below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P \ar[rrd, "\nu'", bend left] \ar[ddr, "\mu'"', bend right] \ar[rd, "\exists ! p", dashed] \\
		& M \times N \ar[r, "\nu"'] \ar[d, "\mu"] & N \\
		& M
	\end{tikzcd}
\end{document}
```

Now if $M \times_{1} N$ and $M \times_{2} N$ are both products, then there exist $p_{1} : M \times_{1} N \to M \times_{2} N$ and $p_{2} : M \times_{2} N \to M \times_{1} N$ with the projection maps to $M$ factoring as $\mu_{1} = \mu_{2} \circ p_{1}$ and $\mu_{2} = \mu_{1} \circ p_{2}$. Thus, $\mu_{1} = \mu_{1} \circ (p_{2} \circ p_{1})$, and similarly $\nu_{1} = \nu_{1} \circ (p_{2} \circ p_{1})$. 

That is, $p_{2} \circ p_{1}$ is a map from $M \times_{1} N$ to itself such that the projection maps factor through it. But $\operatorname{id}_{M \times_{1} N}$ is already such a map and this map is unique. Thus $p_{2} \circ p_{1} = \operatorname{id}_{M \times_{1} N}$ and a similar argument shows $p_{1} \circ p_{2} = \operatorname{id}_{M \times_{2} N}$. That is, $p_{1}$ and $p_{2}$ give the unique bijection (isomorphism) $M \times_{1} N \cong M \times_{2} N$.

Note that the universal property doesn't construct a product of sets, it just uniquely characterises it. This is true of universal properties in general. (Also note that the notion of universal property is not formally defined).


With the language of category theory we can characterise constructions like the product in general [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ (locally small) categories, objects, morphisms|categories]]. We will show that these constructions are unique up to unique [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ isomorphisms, inverse morphisms|isomorphism]]. The uniqueness of the isomorphism is important! This is an informal definition of what it means to be defined by universal property. Again, as we noted previously, this doesn't guarantee existence in every category. 

### Definitions by universal property

For the rest of this note let $\mathscr{C}$ be a category. We already showed that products are unique up to unique isomorphism. Just replace set with object, function with morphism, bijection with isomorphism et c. in the example above.

##### _construction:_ products

A product $M \times N$ of $M, N \in \mathscr{C}$ is the unique object with projection morphisms $\mu, \nu$ to $M$ and $N$ respectively, such that for any $P$ with morphisms $\mu', \nu'$ to $M$ and $N$, there is a unique $\pi : P \to M \times N$ that each of the morphisms factors through — we have $\mu' = \mu \circ \pi$ and $\nu = \nu \circ \pi$ as below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P \ar[rrd, "\nu'", bend left] \ar[ddr, "\mu'"', bend right] \ar[rd, "\exists ! p", dashed] \\
		& M \times N \ar[r, "\nu"'] \ar[d, "\mu"] & N \\
		& M
	\end{tikzcd}
\end{document}
```

Products of $M_{i} \in \mathscr{C}$ indexed by $i \in \mathscr{I}$ are defined as the unique object $\prod_{i \in \mathscr{I}} M_{i}$ with projection morphisms $\mu_{i}$ to each $M_{i}$ such that the analogous universal property follows for $P$ with morphisms to each $M_{i}$.

##### _construction:_ initial, final, and zero objects

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




