---
tags:
- rising-sea/1/1
- cat-th
---

If functors are the morphisms in the category of categories, then natural transformations are the morphisms in the category of functors between two categories. They allow us to weaken the notion of isomorphism of categories (two inverse functors) to an equivalence of categories (functors with composition naturally isomorphic to the identity functors).

##### _definition:_ natural transformations, natural isomorphism, equivalence of categories

A **natural transformation** $F \to G$ of covariant functors $F, G : \mathscr{A} \to \mathscr{B}$ assigns to each object $A \in \mathscr{A}$ a morphism $m_{A} : F(A) \to G(A)$ so that for each morphism $f : A \to A'$ in $\mathscr{A}$, the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		F(A) \ar[r, "F(f)"] \ar[d, "m_{A}"] & F(A') \ar[d, "m_{A'}"] \\
		G(A) \ar[r, "G(f)"] & G(A')
	\end{tikzcd}
\end{document}
```

A natural transformation of contravariant functors $\mathscr{A} \to \mathscr{B}$ is a natural transformation of the equivalent covariant functors $\mathscr{A}^\text{opp} \to \mathscr{B}$.

A **natural isomorphism** of functors is a natural transformation where each $m_{A}$ is an isomorphism.

An **equivalence of categories** is a pair of functors $F : \mathscr{A} \to \mathscr{B}$ and $F' : \mathscr{B} \to \mathscr{A}$ such that $F \circ F'$ and $F' \circ F$ are naturally isomorphic to the identity functor on each category.

Note then that a natural transformation sends objects to morphisms and morphisms to commuting squares.

##### _example:_ the double dual gives an equivalence of categories

Given $\mathsf{finVec}_{\mathbb{F}}$, the category of finite-dimensional vector spaces over $\mathbb{F}$, the double dual functor $V \mapsto V^{\vee \vee}$ is naturally isomorphic to the identity functor with $m_{V}$ given by the isomorphism $v \mapsto v^{\vee \vee} = \varphi_{v}$ such that $\varphi_{v}(\psi) = \psi(v)$ for all $\psi \in V^{\vee}$. Recall that for $T : V \to W$, we have $T^{\vee \vee} : V^{\vee \vee} \to W^{\vee \vee}$ by $T^{\vee \vee}\varphi_{v} = \varphi_{Tv} = (Tv)^{\vee \vee}$. Thus, the following diagram commutes with the downward arrows isomorphisms.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		V \ar[r, "T"] \ar[d] & W \ar[d] \\
		V^{\vee \vee} \ar[r, "T^{\vee \vee}"] & W^{\vee \vee}
	\end{tikzcd}
\end{document}
```

##### _example:_ $\mathsf{finVec}_{\mathbb{F}}$ is equivalent to $\{ \mathbb{F}^n \mid n \in \mathbb{N} \}$,

Let $\mathscr{V}$ be the category of vector spaces $\mathbb{F}^n$ with linear maps as morphisms. The obvious inclusion functor $i : \mathscr{V} \to \mathsf{finVec}_{\mathbb{F}}$ gives an equivalence of categories. In particular, consider the following functor $F : \mathsf{finVec}_{\mathbb{F}} \to \mathscr{V}$. On objects, each $n$-dimensional vector space is sent to $\mathbb{F}^n$. For morphisms, choose a basis $v_{1}, \dots, v_{n}$ for each $n$-dimensional vector space (and in particular, the standard basis for each $\mathbb{F}^n$), and send it to the standard basis on $\mathbb{F}^n$. Then a linear map $V \to W$ corresponds to the linear map $\mathbb{F}^n \to \mathbb{F}^m$ represented by the matrix with respect to the bases of $V$ and $W$. 

It's clear that the composition $F \circ i = \operatorname{id}_{\mathscr{V}}$. Notice that the choice of bases on $V$ and $W$ are really just isomorphisms $V \to \mathbb{F}^n$ and $W \to \mathbb{F}^m$ so that the following diagram commutes. This is just the data of a natural isomorphism $i \circ F \cong \operatorname{id}_{\mathsf{finVec}_{\mathbb{F}}}$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		V \ar[r, "T"] \ar[d] & W \ar[d] \\
		\mathbb{F}^n \ar[r, "\mathcal{M}(T)"] & \mathbb{F}^m
	\end{tikzcd}
\end{document}
```

This is actually an example of a more general phenomenon that follows by essentially the same proof.

##### _proposition:_ equivalence is equivalent to fully faithful and essentially surjective

A functor $F : \mathscr{A} \to \mathscr{B}$ gives an equivalence of categories if and only if it is [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ faithful, full, fully faithful|fully faithful]] and essentially surjective (every object in $\mathscr{B}$ is isomorphic to an object of the form $F(A)$).

###### _proof sketch:_

Consider the functor $G : \mathscr{B} \to \mathscr{A}$ that sends every $B$ to $A$ for some $F(A)$ that it is isomorphic to, and send every morphism $B \to B'$ to a morphism $F(A) \to F(A')$ defined by the isomorphisms and then, by the bijection $\operatorname{Mor}(A, A') \cong \operatorname{Mor}(F(A), F(A'))$, send it to a morphism $A \to A'$. $F$ and $G$ give an equivalence of categories.
