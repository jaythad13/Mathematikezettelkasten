---
tags:
- rising-sea/1/5/6
- math-189AA/19
- hom-alg
---

Let $\mathscr{C}$ be an  that all the objects we care about live in.

Homology measures the degree to which a [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ complexes, exactness, short exact sequence|complex]] is not exact. Specifically

##### _definition:_ homology, boundaries, cycles, cohomology

If the sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & A \ar[r, "f"] & B \ar[r, "g"] & C \ar[r] & \cdots
	\end{tikzcd}
\end{document}
```
is a complex at $B$, then there is an induced [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ monomorphisms, epimorphisms|monomorphism]] $\operatorname{img} f \to \ker g$. The **homology** of the sequence at $B$ is the [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ quotients|quotient]] $\ker g / \operatorname{img} f$.

We say that $\ker g$ consists of **cycles** and $\operatorname{img} f$ consists of **boundaries**.

The $i$th homology of a complex $A_{\bullet}$ is the homology at $A_{i + 1} \to A_{i} \to A_{i - 1}$, denoted $H_{i}(A_{\bullet})$ or $H_{i}$ when the complex in question is clear.

If the complex is indexed in increasing order the indices are written as superscripts and the homology at $A^{i - 1} \to A^i \to A^{i + 1}$ is called the $i$th **cohomology**, denoted $H^i(A^{\bullet})$.

We often write the dimensions of $H_{i}$ and $H^i$ as $h_{i}$ and $h^i$ respectively.

---

This definition naturally means that just as an [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_proposition _ factoring long exact sequences|exact sequence factors into short exact sequences]], we can factor a complex $A^{\bullet}$ into (pairs of) short exact sequences as below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker f^i \ar[r] & A^i \ar[r] & \mathrm{img} \, f^i \ar[r] & 0 \\
		0 \ar[r] & \mathrm{img} \, f^{i - 1} \ar[r] & \ker f^i \ar[r] & H^i(A^\bullet) \ar[r] & 0
	\end{tikzcd}
\end{document}
```

However, less obvious is that homology can be used to factor a complex into exact sequences involving cokernels instead. This gives a dual definition of homology.

##### _proposition:_ dually factoring complexes into short exact sequences

A complex $A^\bullet$ given by $f^i : A^i \to A^{i + 1}$, is uniquely determined by (pairs of) short exact sequences as below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathrm{img} \, f^i \ar[r] & A^{i + 1} \ar[r] & \mathrm{coker} \, f^{i} \ar[r] & 0 \\
		0 \ar[r] & H^i(A^\bullet) \ar[r] & \mathrm{coker} \, f^{i - 1} \ar[r] & \mathrm{img} f^i \ar[r] & 0
	\end{tikzcd}
\end{document}
```

Thus, homology is a sort of invariant of the complex. Another sense in which the homology is an invariant of the complex is by taking "the [[Simplicial homology and random walks --- math-145/notes/Whitehead equivalence#_definition _ the Euler characteristic|Euler characteristic]]".

##### _proposition:_ calculating the Euler characteristic of a complex

Suppose $A^{\bullet}$ is
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r, "d_{0}"] & A^1 \ar[r, "d_{1}"] & \dots \ar[r, "d^{n - 1}"] & A^{n} \ar[r, "d^n"] & 0
	\end{tikzcd}
\end{document}
```
a complex of finite-dimensional $\mathbb{F}$-vector spaces. Then 
$$
\sum_{i = 1}^n (-1) \dim A^i = \sum_{i = 1}^n (-1)^i h^i.
$$

###### _proof sketch:_

By basic linear algebra $h^i = \dim \operatorname{img} d^i - \dim \ker d^{i - 1}$ and $A^i = \dim \ker d^i + \dim \operatorname{img} d^i$. Thus, in both sums, $\dim \operatorname{img} d^i$ and $\dim \ker d^{i}$ summed positively for even $i$ and negatively for odd $i$.

---

### Abstract nonsense properties of homology

Homology also plays fairly nicely with the structure of complexes. For one, it is functorial.

##### _proposition:_ homology is functorial

A [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ morphisms of complexes|morphism of complexes]] $\varphi : A^{\bullet} \to B^{\bullet}$ induces a morphism of (co)homology $\varphi^i_{*} : H^i(A^{\bullet}) \to H^{i}(B^{\bullet})$ (for each $i$) such that $H^i$ is a (covariant) [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|functor]] $\mathsf{Com}_{\mathscr{C}} \to \mathscr{C}$.

###### _proof sketch:_

Let $A^\bullet$ be given by $f^i : A^i \to A^{i + 1}$ and $B^\bullet$ given by $g^i : B^i \to B^{i + 1}$. Then the map $\varphi^i_{*} : a + \operatorname{img} f^{i + 1} \mapsto \varphi(a) + \operatorname{img} g^{i + 1}$ is well-defined by exactness and the commutativity of the diagram.

This functor isn't quite faithful — some distinct morphisms of complexes. However, we can characterise these morphisms

##### _definition:_ homotopic morphisms of complexes

Suppose $A^{\bullet}$ and $B^{\bullet}$ are complexes given by $f^i : A^i \to A^{i + 1}$ and $g^{i} : B^{i} \to B^{i + 1}$. 

Two morphisms of complexes $\varphi^{\bullet} : A^{\bullet} \to B^{\bullet}$ and $\psi^{\bullet} : A^{\bullet} \to B^{\bullet}$ are **homotopic** if there is a sequence of maps $\omega^i : A^i \to B^{i - 1}$ such that $\varphi^i - \psi^i = \omega^{i + 1} f^i + g^{i - 1} \omega_{i}$. This is often abbreviated to $\varphi - \psi = \omega f + g \omega$ or even $\varphi - \psi = \omega d - d \omega$ (abusing notation to write $f$ and $g$ as $d$).

##### _proposition:_ homotopic morphisms give the same map on homology

Two homotopic maps $A^{\bullet} \to B^{\bullet}$ give the same map $H^i(A^{\bullet}) \to H^i(B^{\bullet})$ on homology.

Homology also plays nicely with exactness.

##### _theorem:_ short to long exact sequence

A short exact sequence of complexes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & A^{\bullet} \ar[r] & B^{\bullet} \ar[r] & C^{\bullet} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
induces the following long exact sequence in cohomology.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& \cdots \ar[r] & H^{n - 1}(C^{\bullet}) \ar[r] & \, \\
		 H^{n}(A^{\bullet}) \ar[r] & H^{n}(B^{\bullet}) \ar[r] & H^{n}(C^{\bullet}) \ar[r] & \, \\
		  H^{n + 1}(A^{\bullet}) \ar[r] & \cdots
	\end{tikzcd}
\end{document}
```

###### _proof sketchw:_

Write $K^n = \ker d^{n}$, $I^{n} = \operatorname{img} d^{n}$, and $CK^{n} = \operatorname{coker} d^{n}$. Then, applying the [[Algebraic geometry --- rising-sea/notes/Lemmas in a general abelian category#_lemma _ the snake lemma|snake lemma]] to
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& K^{n}_{A} \ar[d] & K^{n}_{B} \ar[d] & K^n_{C} \ar[d] \\
		0 \ar[r] & A_{n} \ar[r] \ar[d] & B_{n} \ar[r] \ar[d] & C_{n} \ar[r] \ar[d] & 0 \\
		0 \ar[r] & A_{n + 1} \ar[r] \ar[d] & B_{n + 1} \ar[r] \ar[d] & C_{n + 1} \ar[r] \ar[d] & 0 \\
		& A^{n + 1} / I_{A}^{n + 1} & B^{n + 1} / I_{B}^{n + 1} & C^{n + 1} / I_{C}^{n + 1}
	\end{tikzcd}
\end{document}
```
we have the exact sequence below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		K_{A}^n \ar[r] & K_{B}^n \ar[r] & K^n_{C} \ar[r] & CK^{n + 1}_{A} \ar[r] & CK^{n + 1}_{B} \ar[r] & CK^{n + 1}_{C}
	\end{tikzcd}
\end{document}
```

Since we have $I_{n} \subseteq K_{n + 1}$, the maps $d_{n + 1}$ descend to maps $CK_{n + 1} \to I_{n + 1} \subseteq K_{n + 2}$. In fact these maps are such that the squares in the diagram below commute. That is, we can now apply the snake to the following diagram.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& K^{n + 1}_{A} / I^n_{A} \ar[d] & K^{n + 1}_{B} / I^n_{B} \ar[d] & K^{n + 1}_{C} / I^n_{C} \ar[d] \\
		0 \ar[r] & A_{n + 1} / I_{n} \ar[r] \ar[d] & B_{n + 1} / I_{n} \ar[r] \ar[d] & C_{n + 1} / I_{n} \ar[r] \ar[d] & 0 \\
		0 \ar[r] & K^{n + 2}_{A} \ar[r] \ar[d] & K^{n + 2}_{B} \ar[r] \ar[d] & K^{n + 2}_{C} \ar[r] \ar[d] & 0 \\
		& K^{n + 2}_{A} / I^{n + 1}_{A} \ar[r] & K^{n + 2}_{B} / I^{n + 1}_{B} \ar[r] & K^{n + 2}_{C} / I^{n + 1}_{C}
	\end{tikzcd}
\end{document}
```
But this gives a long exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		H^{n + 1}(A^\bullet) \ar[r] & H^{n + 1}(B^\bullet) \ar[r] & H^{n + 1}(C^\bullet) \ar[r] & \, \\
		H^{n + 2}(A^\bullet) \ar[r] & H^{n + 2}(B^\bullet) \ar[r] & H^{n + 2}(C^\bullet)
	\end{tikzcd}
\end{document}
```

---