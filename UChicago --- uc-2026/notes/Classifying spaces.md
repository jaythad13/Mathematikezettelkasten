---
tags:
- uc-2026/alg-top
- alg-top
---

For any group $G$, we want to have a "moduli space" of $G$-bundles — a space $BG$ such that morphisms $X \to BG$ are in natural bijection with vector bundles on $X$. That is, $BG$ [[Algebraic geometry --- rising-sea/notes/Yoneda's lemma#_definition _ representable functor|represents]] the functor $X \mapsto \operatorname{Bun}_{G}$. More precisely, if $EG \to BG$ is the bundle corresponding to $\operatorname{id} : BG \to BG$, we want the bundle corresponding to $X \to BG$ to be the [[Algebraic geometry --- rising-sea/notes/Fibred products#_definition _ fibred product|pullback]] $EG \times_{BG} X \to X$. 

Finally, if $G$ is a topological group, we want $BG$ to understand this topology — the action $G \circlearrowright EG$ should be continuous and $X \to BG$ should correspond to bundles with a continuous $G$-action.

### Classifying spaces of discrete categories

It turns out that the correct way to do this is to think of $G$ [[Algebraic geometry --- rising-sea/notes/Categories#_example _ every group is an entire category, groupoids, monoids, the fundamental groupoid|as a category]] and in particular, a category internal to $\mathsf{Top}$ when $G$ is a topological group. We can take the classifying space of a category in general! When $\mathscr{G}$ is the one object category corresponding to a group $G$, this recovers the original notion of $G$. More generally $B \mathscr{C}$ represents fibre bundles $E \to X$ where the fibres are diagrams $\mathscr{C} \to \mathsf{Set}$.

We've already done most of the work for the discrete case by understanding [[UChicago --- uc-2026/notes/Simplicial sets#_definition _ simplicial sets, simplex category, simplicial objects|simplicial sets]].

##### _definition:_ classifying space

The **classifying space** of a category $\mathscr{C}$ is $B \mathscr{C} \in \mathsf{Top}$, the [[UChicago --- uc-2026/notes/Simplicial sets#_definition _ geometric realisation|geometric realisation]] of its [[UChicago --- uc-2026/notes/Simplicial sets#_definition _ $K_{ mathsf{Cat}}$, categorical simplices, nerve|nerve]].

If $\mathscr{G}$ is the one object category corresponding to a group $G$, we write $BG = B \mathscr{G}$.

---

We can write out the nerve of $\mathscr{G}$ explicitly. The $n$-simplices are functors $\Delta^n \to \mathscr{G}$. This sends each $i \in [0, n]$ the one object of $\mathscr{G}$. Each $i \leq j$ is sent to some $g_{ij} \in G$. Since $i \leq j \leq k$ is the same as $i \leq k$, it suffices to specify $g_{(i - 1), i}$ or each $i \in \{ 1, \dots, n \}$. That is, $N\mathscr{G}^n = G^n$ as sets. Each $d_{i} : \Delta^{n - 1} \to \Delta^n$ gives $N \mathscr{G}^{n} \to N \mathscr{G}^{n - 1}$ by $(g_{1}, \dots, g_{n}) \mapsto (g_{1}, \dots, g_{i - 1}, g_{i} g_{i + 1}, g_{i + 2}, \dots, g_{n})$ — we skip from $i \leq i + 1$ to $i \leq i + 2$. If $i = 0, n$, $g_{i}$ is dropped. Each $s_{i} : \Delta^{n + 1} \to \Delta^n$ gives $N\mathscr{G}^n \to N \mathscr{G}^{n + 1}$ by $(g_{1}, \dots, g_{n}) \mapsto (g_{1}, \dots, g_{i}, e, g_{i + 1}, \dots g_{n})$ — $i \leq i + 2$ is just the same as $i \leq i + 1$.

##### _example:_ the classifying space of $\mathbb{Z} / 2$ is $\mathbb{R} \mathbb{P}^\infty$

Let $\mathscr{G}$ be the group category corresponding to $G = \mathbb{Z} / 2$. There are $2^n$ $n$-simplices. However the only ones that are not actually degenerate simplices are the simplices $(1, \dots, 1)$.

The non-trivial $2$-simplex $(1, 1)$ has non-trivial face maps $d_{0}$ and $d_{2}$. They both have the same image. $d_{1}$ is just the trivial face $(0)$. We can think of this as the disc with opposite points on the boundary identified. Similarly, the only non-trivial $2$-simplex $(1, 1, 1)$ has non-trivial face maps $d_{0}$ and $d_{3}$, which we can think of as identifying two opposite discs and so on. That is, truncating the nerve at any $n$ gives $\mathbb{R} \mathbb{P}^n$. Thus, in the colimit we get $\mathbb{R} \mathbb{P}^\infty$.

That is, $B\mathbb{Z} / 2 = B\mathrm{O}_{1} \cong \mathbb{R} \mathbb{P}^\infty$. Note, $\mathrm{O}_{1} \cong \mathbb{Z} / 2$.

---

##### _definition:_ (two-sided) bar construction

Let $X, Y$ be diagrams in $\mathsf{Top}$ in the shape of $\mathscr{C}$. Then the **simplicial space of the two-sided bar construction** is the simplicial space $B_{\bullet}(X, \mathscr{C}, Y)$ with $n$-simplices $B_{n}(X, \mathscr{C}, Y) = D$. 

We define the **two-sided bar construction** $B(X, \mathscr{C}, Y)$ to be its geometric realisation. As before, when $\mathscr{G}$ is the one object category corresponding to $G$, we write $B(X, G, Y)$ for $B(X, \mathscr{G}, Y)$. Note that $B \mathscr{C} = B(*, \mathscr{C}, *)$ where $*$ is the one point space.

---

This allows us to construct a universal principle $G$-bundle.

##### _definition, theorem:_ universal principal $G$-bundle

The **universal principal $G$-bundle** is $\xi : B(*, G, G) = EG \to BG = B(*, G, *)$. $EG \to BG$ satisfies the universal property that every principal $G$-bundle $\mathscr{E} \to X$ over a space homotopic to a CW complex, is the [[Algebraic geometry --- rising-sea/notes/Fibred products#_definition _ fibred product|pullback]] in the following square.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		E \ar[r] \ar[d] & EG \ar[d, "\xi"] \\
		X \ar[r, "f"] & BG
	\end{tikzcd}
\end{document}
```
In particular, there is a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural isomorphism]] $\operatorname{Prin}_{G} \cong \operatorname{Mor}_{\mathsf{hTop}}(-, BG)$. 

###### _proof:_

We have the followign

---

### Classifying spaces of topological categories

### The topological Grassmannian

We can give an explicit description of $B\mathrm{O}_{n}$. It's just the real manifold version of [[Algebraic geometry --- rising-sea/notes/The Grassmannian|the Grassmannian]].

##### _definition:_ $n$-frames, configuration space of $n$-frames, Grassmannian

An $n$-frame in a vector space is a list of $n$ linearly independent vectors.

Let $V_{n}(\mathbb{R}^\infty)$ be the **configuration space of $n$-frames** vectors in $\mathbb{R}^\infty$ with the subspace topology obtained from $(\mathbb{R}^\infty)^n$.

The (topological) **Grassmannian** $\operatorname{Gr}_{n}(\mathbb{R}^\infty)$ is the [[Topology --- math-147/notes/Quotient and identification spaces#_definition _ quotient topology, quotient space, quotient map|quotient]] $V_{n}(\mathbb{R}^\infty) / \mathrm{O}_{n}$ by the action of $\mathrm{O}_{n}$ on each $n$-subspace of $\mathbb{R}^\infty$. Note $V_{n}(\mathbb{R}^\infty) \to \operatorname{Gr}_{n}(\mathbb{R}^\infty)$ is a principal $\mathrm{O}_{n}$-bundle.

---

##### _proposition:_ $B\mathrm{O}_{n}$ is the Grassmannian with a choice of vector

$E\mathrm{O}_{n}$ is $V_{n}(\mathbb{R}^\infty) \times \mathbb{R}^n$ and $B \mathrm{O}_{n}$ is $\operatorname{Gr}_{n}(\mathbb{R}^\infty) \times \mathbb{R}^n$ with the $E\mathrm{O}_{n} \to B \mathrm{O}_{n}$ given by the quotient $V_{n}(\mathbb{R}^\infty) \to \operatorname{Gr}_{n}(\mathbb{R}^\infty)$.

---