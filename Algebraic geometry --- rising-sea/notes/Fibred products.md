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

###### _proof:_

Suppose $U = V \times_{X} W$ and $W = X \times_{Z} Y$. Further, suppose the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P' \ar[rrd, bend left, "pr_{V}'"] \ar[rdd, bend right, "pr_{Y}'"] \\
		& U \ar[r, "pr_{V}"] \ar[d, "pr_{Y}"] & V \ar[d, "\beta"] \\
		& Y \ar[r, "\alpha"] & Z
	\end{tikzcd}
\end{document}
```
Composing $pr_{V}'$ with $V \to X$ to get $pr_{X}'$, the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P' \ar[rrd, bend left, "pr_{X}'"] \ar[rdd, bend right, "pr_{Y}'"] \ar[rd, dashed, "\Pi_{W}"] \\
		& W \ar[r, "pr_{X}"] \ar[d, "pr_{Y}"] & X \ar[d, "\beta"] \\
		& Y \ar[r, "\alpha"] & Z
	\end{tikzcd}
\end{document}
```
But then by the definition of $pr_{X}'$, the following diagram must commute.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P' \ar[rrd, bend left, "pr_{V}'"] \ar[rdd, bend right, "\Pi_{W}"] \ar[rd, dashed, "\Pi_{U}"] \\
		& U \ar[r, "pr_{V}"] \ar[d, "pr_{W}"] & V \ar[d] \\
		& W \ar[r, "pr_{X}"] & X
	\end{tikzcd}
\end{document}
```
Finally, since $pr_{Y}' = pr_{Y} \circ \Pi_{W}$, and all maps from $V$ and $Y$ to $Z$ agree, the following diagram commutes. This proves that $U$ is the desired fibred product.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P' \ar[rrd, bend left, "pr_{V}'"] \ar[rdd, bend right, "pr_{Y}'"] \ar[rd, dashed, "\Pi_{U}"] \\
		& U \ar[r, "pr_{V}"] \ar[d, "pr_{Y} \circ pr_{W}"] & V \ar[d] \\
		& Y \ar[r, "\alpha"] & Z
	\end{tikzcd}
\end{document}
```

##### _lemma:_ morphisms of bases induce morphisms of fibred products

GIven morphisms $X_{1}, X_{2} \to Y$ and $Y \to Z$, show that there is a natural morphism $X_{1} \times_{Y} X_{2} \to X_{1} \times_{Z} X_{2}$ (assuming both fibred products exist).

###### _proof sketch:_

Since $pr_{i} : X_{1} \times_{Y} X_{2} \to X_{i}$ agree on composition to $Y$, they agree on composition to $Z$ and thus, are maps to $X_{i}$ that agree on composition to $Z$. By the universal property of the fibred product, they must factor (uniquely) through $X_{1} \times_{Z} X_{2}$, inducing the natural map $X_{1} \times_{Y} X_{2} \to X_{1} \times_{Z} X_{2}$. 

In the notation of the proof below, $\psi$ is the unique morphism making the following diagram commute.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		X_{1} \times_{Y} X_{2} \ar[rd, "\psi"] \ar[rrd, bend left] \ar[rdd, bend right] \\
		& X_{1} \times_{Z} X_{2} \ar[r, "pr_{2}"] \ar[d, "pr_{1}"] \ar[d] & X_{2} \ar[d, "\beta"] \\
		& X_{1} \ar[r, "\alpha"] & Y \ar[rd] \\
		& & & Z
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

###### _proof:_

We first describe all the morphisms in the Cartesian diagram. The morphism $X_{1} \times_{Y} X_{2} \to X_{1} \times_{Z} X_{2}$ is described in the lemma above. The morphism $X_{1} \times_{Y} X_{2} \to Y$ is either of the (equal) morphisms $X_{1} \times_{Y} X_{2} \to X_{i} \to Y$. The morphism $Y \to Y \times_{Z} Y$ is the natural morphism given by the fact that the two equal morphisms $\operatorname{id}_{Y} : Y \to Y$ agree as morphisms to $Y$. Finally, the morphism $X_{1} \times_{Z} X_{2} \to Y \times_{Z} Y$ is given again by the universal property of $Y \times_{Z} Y$ — the two morphisms $X_{1} \times_{Z} X_{2} \to X_{i} \to Y$ agree on composition to $Z$.

Note that the diagrams below commute, factoring the maps $X_{1} \times_{Y} X_{2} \to Y$ through $Y \times_{Z} Y$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		X_{1} \times_{Y} X_{2} \ar[rd] \\
		& X_{1} \times_{Z} X_{2} \ar[rd] \ar[r] \ar[d] & X_{1} \ar[rd] \\
		& X_{2} \ar[rd] & Y \times_{Z} Y \ar[r] \ar[d] & Y \ar[d] \\
		& & Y \ar[r] & Z
	\end{tikzcd}
\end{document}
```
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		X_{1} \times_{Y} X_{2} \ar[r] \ar[d] & X_{1} \ar[d] \\
		X_{2} \ar[r] & Y \ar[rrd, bend left, "\mathrm{id}_{Y}"] \ar[rdd, bend right, "\mathrm{id}_{Y}"] \ar[rd] \\
		& & Y \times_{Z} Y \ar[r] \ar[d] & Y \ar[d] \\
		& & Y \ar[r] & Z
	\end{tikzcd}
\end{document}
```
By definition of the fibred product $Y \times_{Z} Y$, there is a unique map $X_{1} \times_{Y} X_{2} \to Y \times_{Z} Y$ that the maps $X_{1} \times_{Y} X_{2} \to Y$ factor through. Thus, the two maps $X_{1} \times_{Y} X_{2} \to Y \times_{Z} Y$ above are the same and the square commutes.

Now, labelling the morphisms, we want the following diagram to commute.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P' \ar[rd, dashed, "\exists !"] \ar[rrd, bend left, "\psi'"] \ar[rdd, bend right, "\varphi'"] \\
		& X_{1} \times_{Y} X_{2} \ar[r, "\psi"] \ar[d, "\varphi"] & X_{1} \times_{Z} X_{2} \ar[d, "\gamma"] \\
		& Y \ar[r, "\delta"] & Y \times_{Z} Y
	\end{tikzcd}
\end{document}
```

$P' \to X_{1} \times_{Z} X_{2} \to X_{i}$ (via $\psi'$ and the projections) give maps agreeing on composition to $Y$ (since the projections from the fibred product agreeing on $Y$). Thus, there is a unique map $\Pi : P' \to X_{1} \times_{Y} X_{2}$ that makes the following diagram commute.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P' \ar[rd, "\Pi"] \ar[rrd, bend left, "pr_{2}' = pr_{2} \circ \psi'"] \ar[rdd, bend right, "pr_{1}' = pr_{1} \circ \psi'"'] \\
		& X_{1} \times_{Y} X_{2} \ar[r, "pr_{2} \circ \psi"] \ar[d, "pr_{1} \circ \psi"] & X_{2} \ar[d, "\beta"] \\
		& X_{1} \ar[r, "\alpha"] & Y
	\end{tikzcd}
\end{document}
```
We claim $\Pi$ is the unique map making the previous diagram commute as well. Note also that by the definition of the maps in the diagram above, any morphism that makes the previous diagram commute makes the diagram commute as well. Thus, any such morphism is unique. It only remains to show that $\Pi$ is such a morphism.

First we show that $\Pi$ makes the diagram commute — we show $\varphi' = \varphi \circ \Pi$ and $\psi' = \psi \circ \Pi$. Given the projection $pr_{Y} : Y \times_{Z} Y \to Y$, we have $pr_{Y} \circ \delta = \operatorname{id}_{Y}$, and thus, the following square also commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		X_{1} \times_{Y} X_{2} \ar[r, "\psi"] \ar[d, "\varphi"] & X_{1} \times_{Z} X_{2} \ar[d, "\gamma"] \\
		Y & Y \times_{Z} Y \ar[l, "pr_{Y}"]
	\end{tikzcd}
\end{document}
```
That is, $\varphi = pr_{Y} \circ \gamma \circ \psi$. Similarly, $\varphi' = pr_{Y} \circ \gamma \circ \psi'$. However, by definition of $\gamma$ as the unique map that the maps $X_{1} \times_{Z} X_{2} \to X_{i} \to Y$ (which agree on $Z$) factor through, we have $pr_{Y} \circ \gamma = \alpha \circ pr_{1}$. Thus, we have $\varphi = \alpha \circ pr_{1} \circ \psi$ and $\varphi' = \alpha \circ pr_{1} \circ \psi'$. Finally, we can write
$$
\begin{align}
\varphi' & = \alpha \circ pr_{1} \circ \psi' \\
 & = \alpha \circ pr_{1} \circ \psi \circ \Pi \\
 & = \varphi \circ \Pi.
\end{align}
$$
We claim that $\psi' = \psi \circ \Pi$ because both sides are the unique morphism that make the following diagram commute.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		P' \ar[rd, dashed, "\Pi"] \ar[rrdd, dashed ,bend left, "\psi'"] \ar[rrrdd, bend left, "pr_{2}'"] \ar[rrddd, bend right, "pr_{1}'"] \\
		& X_{1} \times_{Y} X_{2} \ar[rd, dashed, "\psi"] \\
		& & X_{1} \times_{Z} X_{2} \ar[r, "pr_{2}"] \ar[d, "pr_{1}"] & X_{2} \ar[d, "\beta"] \\
		& & X_{1} \ar[r, "\alpha"] & Y \ar[rd] \\
		& & & & Z
	\end{tikzcd}
\end{document}
```
This is true for both just by definition. We define $\Pi$ to be the unique map that the projections from $P'$ factor through, and the projections from $X_{1} \times_{Y} X_{2}$ uniquely factor through $\psi$. Also, we defined $pr_{i}' = pr_{i} \circ \psi'$. We are done!

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

The [[Algebraic geometry --- rising-sea/notes/Tensor products, categorically#_proposition _ tensor product of rings is a ring|tensor product of rings]] $B \otimes_{A} C$ (with $A$-module structures given by $\varphi : A \to B$ and $\psi : A \to C$) makes the following diagram co-Cartesian.
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
Here the morphisms $B \to B \otimes_{A} C$ and $C \to B \otimes_{A} C$ are are given by $b \mapsto b \otimes 1$ and $c \mapsto 1 \otimes c$ respectively. Suppose $P'$ also has maps $pr_{B}' : B \to P'$ and $pr_{C}' : C \to P'$ that agree as maps from $A$. Then these coprojections factor uniquely through $\amalg : B \otimes_{A} C \to P'$ by $b \otimes c \mapsto \varphi(b) \psi(c)$ (since $b \mapsto b \otimes 1 \mapsto \varphi(b)$ and similarly for $C \to P'$) and uniquely so since the ring structure on the tensor product forces $\amalg(b \otimes c) = \amalg(b \otimes 1) \amalg(1 \otimes c)$.