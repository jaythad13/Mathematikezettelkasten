---
tags:
- rising-sea/1/5/6
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
\sum_{i = 1}^n (-1) \dim A^i = \sum_{i = 1}^n h^i.
$$
##### _proposition:_ homology is functorial

A [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ morphisms of complexes|morphism of complexes]] $A^{\bullet} \to B^{\bullet}$ induces a morphism of (co)homology $H^i(A^{\bullet}) \to H^{i}(B^{\bullet})$ (for each $i$) such that $H^i$ is a (covariant) [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|functor]] $\mathsf{Com}_{\mathscr{C}} \to \mathscr{C}$.

This functor isn't quite faithful — some distinct morphisms of complexes. However, we can characterise these morphisms

##### _definition:_ homotopic morphisms of complexes

Suppose $A^{\bullet}$ and $B^{\bullet}$ are complexes given by $f^i : A^i \to A^{i + 1}$ and $g^{i} : B^{i} \to B^{i + 1}$. 

Two morphisms of complexes $\varphi^{\bullet} : A^{\bullet} \to B^{\bullet}$ and $\psi^{\bullet} : A^{\bullet} \to B^{\bullet}$ are **homotopic** if there is a sequence of maps $\omega^i : A^i \to B^{i - 1}$ such that $\varphi^i - \psi^i = \omega^{i + 1} f^i + g^{i - 1} \omega_{i}$. This is often abbreviated to $\varphi - \psi = \omega f + g \omega$ or even $\varphi - \psi = \omega d - d \omega$ (abusing notation to write $f$ and $g$ as $d$).

##### _proposition:_ homotopic morphisms give the same map on homology

Two homotopic maps $A^{\bullet} \to B^{\bullet}$ give the same map $H^i(A^{\bullet}) \to H^i(B^{\bullet})$ on homology.

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
induces the following long exact sequence in (co)homology.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& \cdots \ar[r] & H^{i - 1}(C^{\bullet}) \ar[r] & \, \\
		 H^{i}(A^{\bullet}) \ar[r] & H^{i}(B^{\bullet}) \ar[r] & H^{i}(C^{\bullet}) \ar[r] & \, \\
		  H^{i + 1}(A^{\bullet}) \ar[r] & \cdots
	\end{tikzcd}
\end{document}
```