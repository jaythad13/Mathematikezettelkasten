---
tags:
- rising-sea/1/3
- cat-th
---

Many of the examples of definition by [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?|universal property]] are special cases of limits and colimits. For example, $p$-[[Geometric group theory --- rtg-2025/notes/The p-adic numbers#_definition _ $p$-adic integers, $ mathbb{Z}_{p}$|adic integers]] and formal power series are examples of limits, while fractions and [[Algebraic geometry --- rising-sea/notes/Localisation, categorically|localisation]] are examples of colimits. The limit and colimit of a diagram are the final and initial objects in the category of "objects with morphisms to or from a commutative diagram" respectively. To make this formal, we make precise what we mean by a diagram

### Diagrams indexed by a category

##### _definition:_ small category

A **small category** is a [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ (locally small) categories, objects, morphisms|(locally small) category]] where the objects form a set.

##### _definition:_ diagram indexed by a category, index category

If $\mathscr{I}$ is a small category and $\mathscr{C}$ is any category, a **diagram** in $\mathscr{C}$ indexed by $\mathscr{I}$ is a [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|(covariant) functor]] $F : \mathscr{I} \to \mathscr{C}$.

We typically write it by $i \mapsto A_{i}$ on objects $i \in \mathscr{I}$ and call $\mathscr{I}$ an **index category**.

Index categories are typically [[Algebraic geometry --- rising-sea/notes/Categories#_example _ preorders and posets|posets]], but other categories can be useful.

### Limits

##### _definition:_ limit of a diagram

The **limit of a diagram** $F : \mathscr{I} \to \mathscr{C}$ (if it exists) is the final object $\lim_{\mathscr{I}} A_{i}$ with maps $f_{j} : \lim_{ \mathscr{I}} A_{i} \to A_{j}$ so that for each $j, k \in \mathscr{I}$ and $m : j \to k$ the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\lim A_{i} \ar[d, "f_{j}"] \ar[rd, "f_{k}"] \\
		A_{j} \ar[r, "F(m)"] & A_{k}.
	\end{tikzcd}
\end{document}
```

Specifically, for any $A'$ with maps $f_{j}' : A' \to A_{j}$ so that the same diagram commutes, there is a unique morphism $g : A' \to \lim_{\mathscr{I}} A_{i}$ such that $f_{i}' = f_{i} \circ g$ (for each $i \in \mathscr{I}$).

##### _examples:_ products and fibred products as limits

The [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ products|categorical product]] is really the limit of the index category described by the poset below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\bullet & \bullet 
	\end{tikzcd}
\end{document}
```
In general, if $\mathscr{I}$ is a set (the only morphisms are identities), then the limit of a diagram indexed by $\mathscr{I}$ is just the product $\prod_{i \in \mathscr{I}} A_{i}$. This is actually a reasonable definition of a product indexed by a set.

The [[Algebraic geometry --- rising-sea/notes/Fibred products#_definition _ fibred product|fibred product]] is the limit of the index category described by the poset below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& \bullet \ar[d] \\
		\bullet \ar[r] & \bullet
	\end{tikzcd}
\end{document}
```

Limits are actually familiar objects!

##### _example:_ formal power series are a limit

The formal power series ring $A[[x]]$ can be defined unnaturally as the ring containing elements $a_{0} + a_{1} x + a_{2} x^{2} + \dots$ with addition and multiplication defined in the obvious way. However they can be described more naturally as the limit of the diagram
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & A[x] / (x^{3}) \ar[r] & A[x] / (x^{2}) \ar[r] &  A[x] / (x)
	\end{tikzcd}
\end{document}
```
in the category of rings.

Similarly, the $p$-adic numbers can also be understood as a limit.

##### _example:_ $p$-adic numbers are a limit

$\mathbb{Z}_{p}$ and its natural maps to each $\mathbb{Z} / (p^e)$ satisfy the universal property that for any ring $A$ with maps $A \to \mathbb{Z} / (p^e)$ that commute with $\mathbb{Z} / p^j \to \mathbb{Z} / p^i$ for exponents $j > i \in \mathbb{N}$. 

That is, the following diagram of rings commutes for each $j > i$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		A \ar[rdd] \ar[rrdd, bend left] \ar[rd, dashed, "\exists !"] \\
		& \mathbb{Z}_{p} \ar[d] \ar[rd] \\
		& \mathbb{Z} / (p^j) \ar[r, two heads] & \mathbb{Z} / (p^i)
	\end{tikzcd}
\end{document}
```

Limits are powerful because they allow us to do things like [[Algebraic geometry --- rising-sea/notes/Fibred products#_theorem _ the diagonal base-change diagram|the diagonal base change diagram]] easily.

##### _theorem:_ the diagonal base change diagram again

Given morphisms $X_{1}, X_{2} \to Y$ and a morphism $Y \to Z$, (assuming they both exist) $X_{1} \times_{Y} X_{2}$ and $Y \times_{Y \times_{Z} Y} (X_{1} \times_{Z} X_{2})$ are naturally isomorphic as they are both the limit of the diagram
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		X_{1} \ar[rd] \\
		& Y \ar[r] & Z. \\
		X_{2} \ar[ur]
	\end{tikzcd}
\end{document}
```

###### _proof:_

$X_{1} \times_{Y} X_{2}$ is the limit of this diagram by the universal property of the fibred product.

>[!missing]

Note of course that the real difference between this and the prior proof of diagonal base change is that we constructed the isomorphism going the other way.

We also usually know when limits exist.

##### _reality check:_ limits of posets with initial elements exist

If $\mathscr{I}$ is a poset and has an [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ initial, final, and zero objects|initial]] object $e$, then the limit of any diagram indexed by $\mathscr{I}$ exists.

###### _proof:_

We are working with the convention that $x \geq y$ corresponds to a morphism $x \to y$.

For any diagram , we claim $A_{e} = F(e)$ is the limit of the diagram.

By the definition of $e$ being initial, it has morphisms to each $j \in \mathscr{I}$, and thus, $A_{e}$ has morphisms to each $A_{j}$. These morphisms commute since the morphisms $i \to j \to k$ compose and functors preserve composition.

Suppose $A'$ has morphisms $f_{j} : A' \to A_{j}$ that commute with $F(m)$ for each $m : j \to k$. Then $A'$ has a morphism $g = f_{e}' : A' \to A_{e}$ such that $f'_{j} = f_{j} \circ g$. This morphism is unique since any $g' : A' \to A_{e}$ such that all $f'_{j} = f_{j} \circ g'$ must have $f'_{e} = f_{e} \circ g'$. However, $f_{e}$ is obviously just the identity $\operatorname{id}_{A_{e}}$ (by the initiality of $e$). Thus, $g' = f'_{e} = g$.

We can also interpret limits in any category with a forgetful functor to $\mathsf{Set}$ as a special subset of the product. This gives us limits in $\mathsf{Mod}_{A}$ and $\mathsf{Ring}$, to name just two.

##### _proposition:_ limits in $\mathsf{Set}$

For any (small) index category $\mathscr{I}$, a diagram $F : \mathscr{I} \to \mathsf{Set}$ has limit
$$
\lim_{\mathscr{I}} A_{i} = \left\{  (a_{i})_{i \in \mathscr{I}} \in \prod_{i \in \mathscr{I}} A_{i} \mid F(m)(a_{j}) = a_{k} \text{ for all } m : j \to k  \right\}.
$$
(with projection maps $f_{j} : \lim_{\mathscr{I}} A_{i} \to A_{j}$ by $(a_{i})_{i \in \mathscr{I}} \mapsto a_{j}$).

###### _proof:_

It's clear that the projection maps $f_{j}$ make the desired diagram commute — for $m : j \to k$ we have 
$$
\begin{align}
F(m) \circ f_{j}((a_{i})_{i \in \mathscr{I}}) & = F(m)(a_{j}) \\
 & = a_{k} \\
 & = f_{k}((a_{i})_{i \in \mathscr{I}}).
\end{align}
$$
Suppose  has maps $f_{j}' : A' \to A_{j}$ so that the desired diagram commutes for all $m : j \to k$. Then consider the map $g : A' \to \lim_{\mathscr{I}} A_{i}$ by $a' \mapsto (f_{i}(a'))_{i \in \mathscr{I}}$. This map does indeed have the desired codomain since $F(m)(f_{j}(a')) = f_{k}(a')$ by the commutative diagram, and clearly $f_{j}' = f_{j} \circ g$ by construction. It only remains to show that this map is unique.

Suppose $g' : A' \to \lim_{\mathscr{I}} A_{i}$ also has $f_{j}' = f_{j} \circ g$ for all $j$. Writing $g'(a') = (a_{i})_{i \in \mathscr{I}}$, we must then have $a_{i} = f_{i}(a')$ for each $i$ and each $a'$. Thus, $g'(a') = (f_{i}(a'))_{i \in \mathscr{I}} = g(a')$ for each $a' \in A'$. This is just $g = g'$.

### Colimits

Colimits will be more immediately relevant for us. They are defined dually to limits by flipping the arrows in the definition. Specifically,

##### _definition:_ colimit of a diagram

The **colimit of a diagram** $F : \mathscr{I} \to \mathscr{C}$ (if it exists) is the initial object $\operatorname{colim}_{\mathscr{I}} A_{i}$ with maps $f_{j} : A_{j} \to \operatorname{colim}_{ \mathscr{I}} A_{i}$ so that for each $j, k \in \mathscr{I}$ and $m : j \to k$ the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		A_{j} \ar[r, "F(m)"] \ar[d, "f_{j}"] & A_{k} \ar[ld, "f_{k}"] \\
		\mathrm{colim} A_{i} \\
	\end{tikzcd}
\end{document}
```
Specifically, for any $A'$ with maps $f_{j}' : A_{j} \to A'$ so that the same diagram commutes, there is a unique morphism $g : \lim_{\mathscr{I}} A_{i} \to A'$ such that $f_{i}' = g \circ f_{i}$ (for each $i \in \mathscr{I}$).

##### _examples:_ divisors

The abelian group $5^{-\infty} \mathbb{Z}$ of rational numbers with denominators that are powers of $5$ is the colimit of the diagram below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathbb{Z} \ar[r] & 5^{-1} \mathbb{Z} \ar[r] & 5^{-2} \mathbb{Z} \ar[r] & \cdots
	\end{tikzcd}
\end{document}
```
More generally, we can understand the rational numbers as $\operatorname{colim} \frac{1}{n} \mathbb{Z}$.

##### _example:_ unions are colimits

The union of subsets of a given set can be interpreted as a colimit (in the [[Algebraic geometry --- rising-sea/notes/Categories#_example _ the inclusion category of subsets or open sets|inclusion category of subsets]]). Specifically, it has inclusions from each of the subsets that are compatible with the inclusions between them. Since it is the smallest such set, it includes (uniquely) into any other set with such inclusions.

Again, colimits do not always exist (not even in $\mathsf{Set}$) but as with limits we can understand exactly when they do. Dually (to special subset of the product) we understand them as a special quotient of the coproduct.

##### _definition:_ filtered poset, filtered category

A non-empty poset $S$ is **filtered** if for each $i, j \in S$ there is a $k \in S$ such that $i, j \geq k$.

A non-empty category $\mathscr{I}$ is **filtered** if for each $i, j \in \mathscr{I}$ there is a $k \in \mathscr{I}$ with morphisms $i \to k$ and $j \to k$ and for each pair of morphisms $m_{1}, m_{2} : i \to j$, there is a morphism $u : j \to k$ so that the morphisms agree on $k$ (that is, $u \circ m_{1} = u \circ m_{2}$).

##### _proposition:_ colimits of filtered categories in $\mathsf{Set}$

Suppose $\mathscr{I}$ is filtered. Any diagram $F : \mathscr{I} \to \mathsf{Set}$ has colimit
$$
\operatorname{colim}_{\mathscr{I}} A_{i} = \{ (a_{i}, i) \in \coprod_{i \in \mathscr{I}} A_{i} \} / \sim
$$
where $(a_{j}, j) \sim (a_{k}, k)$ if and only if there are $f : A_{j} \to A_{\ell}$ and $g : A_{k} \to A_{\ell}$ in the diagram for which $f(a_{j}) = g(a_{k})$ and the "coprojection" maps are $pr_{i} : a_{i} \mapsto (a_{i}, i)$ for each $a_{i} \in A_{i}$

###### _proof:_

First we show that $\sim$ is an equivalence relation. It's clearly reflexive (choose $f, g = \operatorname{id}_{A_{j}}$) and is defined so that it is symmetric. Suppose $(a_{i}, i) \sim (a_{j}, j)$ with morphisms $f_{\ell}, g_{\ell}$ agreeing on $A_{\ell}$ and $(a_{j}, j) \sim (a_{k}, k)$ with morphisms $g_{m}, h_{m}$ agreeing on $A_{m}$. We want to show $(a_{i}, i) \sim (a_{k}, k)$ with morphisms (say $f_{n}, h_{n}$) agreeing on $A_{n}$. Since $\mathscr{I}$ is filtered, there is some $A_{n_{0}}$ with morphisms from $A_{\ell}$ and $A_{m}$ and we can choose some $A_{n}$ so that the two morphisms $A_{j} \to A_{m} \to A_{n_{0}}$ and $A_{j} \to A_{\ell} \to A_{n_{0}}$ agree on composition to $A_{n}$. Since the morphisms from $A_{i}$ and $A_{k}$ agree with the morphisms from $A_{j}$ on $A_{\ell}$ and $A_{m}$ respectively, they agree with each other on composition to $A_{n}$. Note that proving $\sim$ is an equivalence relation relies on $\mathscr{I}$ being filtered.

Now we show that our expression for the colimit really does satisfy the universal property of the colimit. First we show that the coprojections $pr_{i}$ really do commute with

Suppose $A'$ has coprojections $pr_{i}' : A_{i} \to A'$ commuting with all the maps $A_{j} \to A_{k}$. Then the maps factor uniquely through the coprojections to the coproduct (the disjoint union). That is, there is a unique map $g_{\amalg} : \coprod_{i \in \mathscr{I}} A_{i} \to A'$ such that $pr_{i}' = g_{\amalg} \circ pr_{\amalg, i}$ (where $pr_{\amalg, i}$ are the coprojections to the coproduct). We claim $g_{\amalg}$ identifies all equivalence classes $(a_{j}, j) \sim (a_{k}, k)$. Thus, $g_{\amalg}$ factors uniquely through $g : \coprod_{i \in \mathscr{I}} A_{i} \to \left\{  (a_{i}, i) \in \coprod_{i \in \mathscr{I}} A_{i}  \right\} / \sim$ proving that it is the colimit. Since $pr_{i} = g \circ pr_{\amalg, i}$, this, gives us $pr_{i}' = h \circ pr_{i}$ uniquely (where we factor $g_{\amalg} = h \circ g$).

Suppose $(a_{j}, j) \sim (a_{k}, k)$. Then some $f, g : A_{j}, A_{k} \to A_{\ell}$ (respectively) have $f(a_{j}, j) = g(a_{k}, k)$. Since the coprojections $pr_{i}'$ commute with the maps, we have 
$$
pr_{j}'(a_{j}, j) = pr_{\ell}'(f(a_{j}, j)) = pr_{\ell}'(g(a_{k}, k)) = pr_{k}'(a_{k}, k).
$$
Since $pr_{j}(a_{j}, j) \neq pr_{k}(a_{k}, k)$ unless $(a_{j}, j) = (a_{k}, k)$, we must have $g_{\amalg}(a_{j}) = g_{\amalg}(a_{k})$ already.

##### _example:_ colimit of $A$-modules

The colimit of $A$-modules $M_{i}$ can be interpreted as the colimit set with addition as follows. The sum of $m_{j} \in M_{j}$ and $m_{k} \in M_{k}$ with $f : M_{j} \to M_\ell$ and $g : M_{k} \to M_\ell$ is $f(m_{j}) + g(m_{k}) \in M_{\ell}$. In particular $m_{j} \in M_{j}$ is only $0$ if it is in the kernel of some $f : M_{j} \to M_{\ell}$ in the diagram.

In fact, since $A$-modules have a group structure and thus, a notion of "generated by", we have colimits even without filtered index categories — we can force an equivalence relation.

##### _proposition:_ not-necessarily filtered colimits of $A$-modules

A diagram of $A$-modules $\mathscr{I} \to \mathsf{Mod}_{A}$ has colimit $\operatorname{colim}_{\mathscr{I}} M_{i} = \bigoplus_{i \in \mathscr{I}} M_{i} / U$ where $U$ is the subspace generated by "vectors" $m_{j} - f(m_{j})$ for each $f : M_{j} \to M_{k}$ in the diagram.

##### _proposition:_ localisation is a colimit

Suppose $S$ is a multiplicative subset and $A$ is an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|Integral domains]], then the [[Algebraic geometry --- rising-sea/notes/Localisation, categorically#_definition _ localisation of a ring, localisations at a prime, fraction field|localisation]] $S^{-1} A$ can be interpreted as $\operatorname{colim} \frac{1}{s} A$ where the colimit is over $s \in S$ and in the category of $A$-modules.

In general this can work even with $A$ not an integral domain with $S^{-1} A = \operatorname{colim} A_{s}$.