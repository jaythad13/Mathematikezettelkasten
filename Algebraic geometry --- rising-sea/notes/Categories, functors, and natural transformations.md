---
tags:
- cat-th
- rising-sea/1
---

Essentially we want to know category theory to make precise the sense in which [[Sheaves|sheaves]] of abelian groups and modules as well as [[Schemes|schemes]] behave like abelian groups, modules, and rings (respectively). That is, we want to eventually understand the notion of an [[Abelian categories|abelian category]].

Why do this through category theory? Because it's the cleanest language to do it in. The best elementary example of this is the [[Universal properties|universal property]] of the product.

##### _example:_ product

There are many types of products — of sets, [[Linear algebra done right --- ladr/notes/Product spaces|vector spaces]], groups, topological spaces, even of manifolds. We usually define each type of product separately, but really they all possess the same "universal property". The idea is that there isn't one single product, but rather, any two products have a unique isomorphism between them. Consider, for example, the product of sets.

Both $\{ \{ u, \{ v \} \} \mid u \in U, v \in V \}$ and $\{ \{ \{ u \}, v \} \mid u \in U, v \in V \}$ are reasonable definitions of $U \times V$, and there's an obvious sense in which it doesn't matter which one you pick. Similarly, it doesn't matter how you cut up two manifolds into charts, take products and glue them back together — there's some sense in which all these encodings are the same.

A product $M \times N$ of $M$ and $N$ is a set (object) with projection functions (morphisms) $\mu, \nu$ to $M$ and $N$ respectively, such that for any $P'$ with projections $\mu, \nu'$ to $M$ and $N$, there is a unique $p' : P' \to P$ so that $\mu' = \mu \circ p'$ and $\nu = \nu \circ p'$ as below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P' \ar[rrd, "\nu'", bend left] \ar[ddr, "\mu'"', bend right] \ar[rd, "\exists ! p'"] \\
		& M \times N \ar[r, "\nu"'] \ar[d, "\mu"] & N \\
		& M
	\end{tikzcd}
\end{document}
```

Now if $M \times_{1} N$ and $M \times_{2} N$ are both products, then there exist $p_{1} : M \times_{1} N \to M \times_{2} N$ and $p_{2} : M \times_{2} N \to M \times_{1} N$ with the projection maps to $M$ factoring as $\mu_{1} = \mu_{2} \circ p_{1}$ and $\mu_{2} = \mu_{1} \circ p_{2}$. Thus, $\mu_{1} = \mu_{1} \circ (p_{2} \circ p_{1})$, and similarly $\nu_{1} = \nu_{1} \circ (p_{2} \circ p_{1})$. 

That is, $p_{2} \circ p_{1}$ is a map from $M \times_{1} N$ to itself such that the projection maps factor through it. But $\operatorname{id}_{M \times_{1} N}$ is already such a map and this map is unique. Thus $p_{2} \circ p_{1} = \operatorname{id}_{M \times_{1} N}$ and a similar argument shows $p_{1} \circ p_{2} = \operatorname{id}_{M \times_{2} N}$. That is, $p_{1}$ and $p_{2}$ give the bijection (isomorphism) $M \times_{1} N \cong M \times_{2} N$.