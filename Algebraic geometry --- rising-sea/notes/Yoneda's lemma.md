---
tags:
- cat-th
- rising-sea/1/2
---

Yoneda's lemma provides a way to understand [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?|universal properties]] in arbitrary categories as universal properties in the category $\mathsf{Set}$ with the notion of representable functors. Specifically, it says that you can recover an object in a category by understanding the set of maps into it. It significantly uses the idea of the functor of points.

![[Algebraic geometry --- rising-sea/notes/Functors#_example _ the functor of points and its opposite]]

##### _lemma:_ Yoneda's lemma

Suppose $A, A', B, C$ are objects in $\mathscr{C}$, and there are maps $i_{C} : \operatorname{Mor}(C, A) \to \operatorname{Mor}(C, A')$  such that the following diagram commutes for each $f :B \to C$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Mor} (C, A) \ar[r, "i_{C}"] \ar[d, "h_{A}(f)"] & \mathrm{Mor}(C, A') \ar[d, "h_{A'}(f)"] \\
		\mathrm{Mor}(B, A) \ar[r, "i_{B}"] & \mathrm{Mor}(B, A')
	\end{tikzcd}
\end{document}
```
Then each $i_{C}$ is induced by a unique morphism $g : A \to A'$  — we have $i_{C} = h^C(g)$. Further, if each $i_{C}$ is a bijection, then $g$ is an isomorphism.

###### _proof:_

Consider the case of $C = A$ and some $f : B \to A$. Then following the identity on $A$ through the commutative diagram above, we get $h_{A'}(f) \circ i_{A}(\operatorname{id}_{A}) = i_{B} \circ h_{A}(f)(\operatorname{id}_{A})$. Note that $h_{A}(f)(\operatorname{id}_{A})$ is just $f$, and thus, 
$$
i_{B}(f) = i_{A}(\operatorname{id}_{A}) \circ f
$$
But choosing $g = i_{A}(\operatorname{id}_{A}) : A \to A'$, this means that
$$
i_{B}(f) = g \circ f = h^B(g)(f)
$$
for each $f : B \to A$, as desired.

Suppose each $i_{C}$ is a bijection with inverse $i_{C}^{-1}$. Then note that with $C = A'$ the following diagram commutes for each $f' : B \to A'$
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Mor}(A', A) \ar[d, "h_{A}(f')"] & \mathrm{Mor}(A', A') \ar[d, "h_{A'}(f')"] \ar[l, "i_{A}^{-1}"] \\
		\mathrm{Mor}(B, A) & \mathrm{Mor}(B, A') \ar[l, "i_{B}^{-1}"]
	\end{tikzcd}
\end{document}
```
Now, following where $\operatorname{id}_{A'}$ goes gives $i_{B}^{-1} \circ h_{A'}(f')(\operatorname{id}_{A'}) = h_{A}(f') \circ i_{A'}^{-1}(\operatorname{id}_{A})$ and thus,
$$
i_{B}^{-1}(f') = i^{-1}_{A}(\operatorname{id}_{A'}) \circ f
$$
Choosing $g' = i_{A}^{-1}(\operatorname{id}_{A'})$, we see that each $i_{B}^{-1}$ is just $h^B(g')$. In particular, 
$$
\operatorname{id}_{A} = i_{A}^{-1}(i_{A}(\operatorname{id}_{A})) = i_{A}^{-1}(g) = g' \circ g.
$$
Similarly,
$$
\operatorname{id}_{A'} = i_{A}(i_{A}^{-1}(\operatorname{id}_{A'})) = g \circ g'.
$$
Thus, $g$ is an isomorphism with $g^{-1} = g'$.

More generally, Yoneda's lemma is typically stated in the language of natural transformations.

##### _lemma:_ Yoneda's lemma

Given a (covariant) [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|functor]] $F : \mathscr{C} \to \mathsf{Set}$ and $A \in \mathscr{C}$, there is a bijection between [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformations]] $h^A \to F$ and $F(A)$. In particular, there is a bijection between natural transformations $h^A \to h^B$ and morphisms $B \to A$.

If $F$ is contravariant, there is a bijection between natural transformations $F \to h_{A}$ and $F(A)$.

###### _proof:_

If $h^A \to F$ is a natural transformation, then the "natural" diagram commutes for each $f : B \to C$. In particular, when $B = A$ and $f : A \to C$, the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Mor}(A, A) \ar[r, "h^A(f)"] \ar[d, "m_{A}"] & \mathrm{Mor}(A, C) \ar[d, "m_{C}"] \\
		F(A) \ar[r, "F(f)"] & F(C)
	\end{tikzcd}
\end{document}
```
Following where $\operatorname{id}_{A}$ goes gives us
$$
m_{C} \circ h^A(f)(\operatorname{id}_{A}) = F(f) \circ m_{A} (\operatorname{id}_{A})
$$
which is just
$$
m_{C}(f) = F(f) \circ m_{A}(\operatorname{id}_{A})
$$
for each $C$. Thus, each $m_{C}$ is determined by a (free) choice of $m_{A}(\operatorname{id}_{A}) \in F(A)$.

If $h_{A} \to F$ is a natural transformation of contravariant functors, then again, there is a diagram that commutes for each $f : C \to A$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Mor}(A, A) \ar[r, "h_{A}(f)"] \ar[d, "m_{A}"] & \mathrm{Mor}(C, A) \ar[d, "m_{C}"] \\
		F(A) \ar[r, "F(f)"] & F(C)
	\end{tikzcd}
\end{document}
```
This again gives
$$
m_{C}(f) = F(f) \circ m_{A}(\operatorname{id}_{A})
$$
determining each $m_{C}$ by a free choice of $m_{A}(\operatorname{id}_{A})$.

This allows us to make the following definition.

##### _definition:_ representable functor

A covariant/contravariant functor $F : \mathscr{C} \to \mathsf{Set}$ is **representable** if there is a natural isomorphism $F \cong h^{A}$ or $F \cong h_{A}$ respectively.

Yoneda's lemma says that the data of a category is equivalent to the data of the corresponding category of representable functors. The fanciest form of this philosophical statement ("tell me who your friends are, and I'll tell you who you are") is the following.

##### _lemma:_ Yoneda's fanciest lemma

The contravariant functor $\mathscr{C} \to \mathsf{Set}^\mathscr{C}$ (the latter the category of functors $\mathscr{C} \to \mathsf{Set}$) by $A \mapsto h_{A}$ and $B \to A$ to the corresponding natural transformation $h_{A} \to h_{B}$ is [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ faithful, full, fully faithful|fully faithful]].