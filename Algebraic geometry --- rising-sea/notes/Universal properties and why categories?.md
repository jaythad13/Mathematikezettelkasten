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

For the rest of this note let $\mathscr{C}$ be a category. We already showed that products are unique up to unique isomorphism. Just replace set with object, function with morphism, bijection with isomorphism et c. in the example above.

##### _construction:_ products

A product $M \times N$ of $M, N \in \mathscr{C}$ is the unique object with projection morphisms $\mu, \nu$ to $M$ and $N$ respectively, such that for any $P$ with morphisms $\mu', \nu'$ to $M$ and $N$, there is a unique $p : P \to M \times N$ that each of the morphisms factors through — we have $\mu' = \mu \circ p$ and $\nu = \nu \circ p$ as below.
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

### Localisation of rings and modules

One very important example of a definition by universal property is that of localisation (of rings and modules). Recall the constructive definition of localisation as follows:

##### _definition:_ multiplicative subsets

A multiplicative subset of a ring $A$ is a subset $S$ such that for any $s_{1}, s_{2} \in S$, we have $s_{1} s_{2} \in S$.

##### _definition:_ localisation of a ring, localisations at a prime, fraction field

The localisation of a ring $A$ away from a multiplicative subset $S$ is the ring $S^{-1} A$ with elements of the form $a / s$ with $a \in A, s \in S$ under the equivalence relation $a_{1} / s_{1} = a_{2} / s_{2}$ if and only if $s(s_{2} a_{1} - a_{2} s_{2}) = 0$ for some $s \in S$. Addition is defined by
$$
\frac{a_{1}}{s_{1}} + \frac{a_{2}}{s_{2}} = \frac{s_{2} a_{1} + s_{1} a_{2}}{s_{1} s_{2}}
$$
and multiplication is defined by
$$
\frac{a_{1}}{s_{1}} \times \frac{a_{2}}{s_{2}} = \frac{a_{1} a_{2}}{s_{1} s_{2}}.
$$
Consequently zero is (the equivalence class of) $0 / 1$ and the multiplicative identity is (the equivalence class of) $1 / 1$

When $S = \{ 1, f, f^{2}, \dots \}$ for an element $f \in A$, we denote $S^{-1} A$ by $A_{f}$.

When $S = A \setminus \mathfrak p$ for a [[Abstract Algebra I --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|prime ideal]] $\mathfrak p$, we denote $S^{-1} A$ by $A_{\mathfrak p}$ and call it the localisation at the prime. Note that then if the ideal $(f)$ is prime, $(f)^{-1} A = A_{f} \neq A_{(f)}$.

Finally if $A$ is an [[Abstract Algebra I --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]] and $S = A \setminus \{ 0 \}$ we call $S^{-1} A$ the fraction field of $A$ and denote it by $K(A)$.

Note that there is a canonical ring map $A \to S^{-1} A$ by $a \mapsto a / 1$, and if $0 \in S$, $S^{-1} A$ is the trivial ring. When $S$ doesn't contain zero divisors, the map is injective. In particular $A \to K(A)$ is injective. However, this is not true otherwise.

##### _proposition:_ injectivity of the localisation map

For a multiplicative subset $S$ of a ring $A$, the canonical map $A \to S^{-1} A$ by $a \mapsto a / 1$ is injective if and only if $S$ contains no [[Abstract Algebra I --- math-171/notes/Rings#_definition _ zero divisor|zero divisor]].

###### _proof:_

The condition for $a / 1 = 0$ in $S^{-1} A$ is that $a / 1 = 0 / 1$ and thus, $s(1 \times a - 0 \times 1) = sa$ is zero in $A$.

Suppose $S$ contains a zero divisor $s$. Then $as = 0$ for some non-zero $a \in A$. Thus, $a / 1 = 0 / 1$ since $s a = 0$.

Suppose $S$ contains no zero divisors. Then for any non-zero $a \in A$, $a / 1 \neq 0 / 1$ since that can only happen if $sa = 0$ for some $s \in S$ which requires a zero divisor in $S$.

Localisations of $A$ can be characterised in terms of a universal property in the category of $A$-algebras (rings $B$ with a ring homomorphism $A \to B$).

##### _proposition:_ the universal property of modules

$S^{-1} A$ is initial among $A$-algebras $B$ where every element of $S$ is sent to an invertible element in $B$.

From this definition it's obvious that if $A$ is a field, then its localisation by any multiplicative set is just itself. We can use this fact to extend to a definition of localisation of modules.

##### _definition:_ the localisation of a module

Suppose $M$ is an $A$-module and $S \subseteq A$ is multiplicative. $S^{-1} M$ is initial $A$-module in the category of modules $N$ with a distinguished $A$-module map $M \to N$ such that the action of $S$ is invertible (as a module map) on $N$.

Recall that we still need to show that the localisation of a module exists.

##### _proposition:_ localisation commutes with finite products and all coproducts

If $M_{1}, \dots, M_{n}$ are $A$-modules, then there is an isomorphism (of $A$-modules and $S^{-1} A$-modules) $S^{-1} (M_{1} \times \dots \times M_{n}) \to S^{-1} M_{1} \times \dots \times S^{-1} M_{n}$.

If $\{ M_{i} \}_{i \in \mathscr{I}}$ is a collection of modules, then there is an isomorphism (of $A$-modules and $S^{-1} A$-modules)
$$
S^{-1} \bigoplus_{i \in \mathscr{I}} M_{i} \to \bigoplus_{i \in \mathscr{I}} S^{-1}M_{i}.
$$


Note that localisation does not necessarily commute with infinite products — in particular the unique
$$
S^{-1} \prod_{i \in \mathscr{I}} M_{i} \to \prod_{i \in \mathscr{I}} S^{-1} M_{i}
$$
is not necessarily an isomorphism
