---
tags:
- rising-sea/1/2
- cat-th
---

For this note let $\mathscr{C}$ be any category with objects $X, Y, Z$.

In doing algebraic geometry, we often consider the data of schemes *over* some base scheme $S$. This is because varieties are defined over a particular field $\mathbb{F}$. The product of objects $X, Y$ over $S$ (with specific choice of $S$) in the category of objects over $S$ is just the fibred product. In particular, in the category of varieties over an algebraically closed field, the classical product of varieties is the fibre product of corresponding schemes (over the scheme corresponding to the field). It is defined by universal property, and thus, doesn't necessarily exist in every category.

##### _definition:_ fibred product

Given morphisms $\alpha : X \to Z$ and $\beta : Y \to Z$, the fibred product (if it exists) is the unique final object $X \times_{Z} Y$ with projection morphisms $pr_{X} : X \times_{Z} Y \to X$ and $pr_{Y} : X \times_{Z} Y \to Y$ that agree on composition to $Z$ such that the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P' \ar[dr, dashed, "\exists !"] \ar[rrd, bend left, "pr_{X}'"] \ar[ddr, bend right, "pr_{Y}'"] \\
		& X \times_{Z} Y \ar[r, "pr_{Y}"] \ar[d, "pr_{X}"] & Y \ar[d, "\beta"] \\
		& X \ar[r, "\alpha"] & Z.
	\end{tikzcd}
\end{document}
```

The uniqueness (up to unique isomorphism) of the fibred product is by the same argument [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_construction _ products|as for products]].

We sometimes say that $X \times_{Z} Y$ is a fibred product by saying that
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		X \times_{Z} Y \ar[r, "pr_{Y}"] \ar[d, "pr_{X}"] & Y \ar[d, "\beta"] \\
		X \ar[r, "\beta"] & Z
	\end{tikzcd}
\end{document}
```
is a fibred/pullback/Cartesian diagram/square.

##### _definition:_ diagonal morphism

If $\pi : X \to Y$ is a morphism and $X \times_{Y} X$ exists, then pair consisting of identity morphisms $X \to X$ agree as morphisms to $Y$, and thus, determines the diagonal morphism $\delta_{\pi} : X \to X \times_{Y} X$.

##### _example:_ the fibred product of sets

In $\mathsf{Set}$, the universal property of the fibred product of $X$ and $Y$ over $Z$ (with corresponding maps $\alpha$ and $\beta$ as above) is satisfied by
$$
P = \{ (x, y) \in X \times Y \mid \alpha(x) = \beta(y) \}.
$$
Specifically, for any $P'$ with maps $pr'_{X}$ and $pr'_{Y}$ to $X$ and $Y$ that agree on composition to $Z$, the map $\pi : P' \to P$ by $p \mapsto (pr'_{X}(p), pr'_{Y}(p))$ is the unique function with $pr_{X} \circ \pi = pr_{X}'$ and $pr_{Y} \circ \pi = pr'_{Y}$.

##### _example:_ fibred products in the [[Algebraic geometry --- rising-sea/notes/Categories#_example _ the inclusion category of subsets or open sets|inclusion category of open sets]]

are intersections (since the map between any two objects is unique).

##### _proposition:_ the fibred product over the final object

The fibred product of $X$ and $Y$ over the final object $Z$ in a category is (uniquely isomorphic to) the [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ products|product]] $X \times Y$.

##### _proposition:_ towers of Cartesian diagrams are Cartesian

If the two squares in the following commutative diagram are Cartesian, then the outer rectangle is a Cartesian diagram. That is, if $U = V \times_{X} W$ and $W = X \times_{Z} Y$, then $U = V \times_{Z} Y$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		U \ar[r] \ar[d] & V \ar[d] \\
		W \ar[r] \ar[d] & X \ar[d] \\
		Y \ar[r] & Z
	\end{tikzcd}
\end{document}
```

##### _theorem:_ the diagonal base-change diagram

Given morphisms $X_{1}, X_{2} \to Y$ and $Y \to Z$, show that the following diagram is Cartesian
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		X_{1} \times_{Y} X_{2} \ar[r] \ar[d] & X_{1} \times_{Z} X_{2} \ar[d] \\
		Y \ar[r] & Y \times_{Z} Y.
	\end{tikzcd}
\end{document}
```
(assuming all relevant fibred products exist).

##### _lemma:_ morphisms of bases induce morphisms of fibred products

GIven morphisms $X_{1}, X_{2} \to Y$ and $Y \to Z$, show that there is a natural morphism $X_{1} \times_{Y} X_{2} \to X_{1} \times_{Z} X_{2}$ (assuming both fibred products exist).

### Co-fibred products

Co-fibred products are "dual" to fibred products, defined by reversing all the arrows in the definition of the fibred product (as in the [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ coproducts, direct sums|coproduct]])

##### _definition:_ co-fibred product

Given morphisms $\alpha : Z \to X$ and $\beta : Z \to Y$, the co-(rresponding fibred product) is the initial object $P$ with morphisms $pr_{X} : X \to P$ and $pr_{Y} : Y \to P$ that agree as morphisms from $Z$ such that the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
	P' \\
		& P \ar[ul, dashed, "\exists !"] & \ar[l, "pr_{Y}"] \ar[llu, bend right, "pr_{Y}'"] Y \\
		& X \ar[u, "pr_{X}"] \ar[uul, bend left, "pr_{X}'"] & Z \ar[l, "\alpha"] \ar[u, "\beta"]
	\end{tikzcd}
\end{document}
```


##### _example:_ the tensor product of rings is the co-fibred products

The [[Algebraic geometry --- rising-sea/notes/Tensor products, categorically#_proposition _ tensor product of rings is a ring|tensor product of rings]] $B \otimes_{A} C$ makes the following diagram co-Cartesian.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		B \otimes_{A} C & \ar[l] C \\
		B \ar[u] & A \ar[l] \ar[u]
	\end{tikzcd}
\end{document}
```