---
tags:
- rising-sea/1/5/6
- hom-alg
---

Let $\mathscr{C}$ be an abelian category and let all objects be objects of the abelian category.

### Complexes and exactness

Complexes are useful because algebraic topology.

##### _definition:_ complexes, exactness, short exact sequence

A sequence of morphisms
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & A \ar[r, "f"] & B \ar[r, "g"] & C \ar[r] & \cdots
	\end{tikzcd}
\end{document}
```
is a **complex** at $B$ if $g \circ f = 0$.

It is **exact** at $B$ if $\ker g = \operatorname{img} f$.

A sequence is a **complex** or is **exact** if it is exact at each term (except possibly the first and last terms).

A **short exact sequence** is an exact sequence of the form
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & A \ar[r] & B \ar[r] & C \ar[r] & 0.
	\end{tikzcd}
\end{document}
```

##### _example:_ what exactness means

1) Exactness implies being a complex — in the example in the definition, the defining property of $\ker g$ is that $\ker g \to B \to C$ is just $0$. Since $f : A \to B$ [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ images|factors through]] $A \to \operatorname{img} f$, we have $A \to B \to C$ is just $A \to \operatorname{img} f \to B \to C$ is just $A \to \ker g \to B \to C$ is just $0$.
2) $0 \to A \to 0$ is exact if and only if $A = 0$.
3) $0 \to A \to B$ is exact if and only if $A \to B$ is a monomorphism.
4) $0 \to A \to B \to 0$ is exact if and only if $A \to B$ is an isomorphism.
5) $0 \to A \to B \to C$ is exact if and only if $A \to B$ is the kernel of $B \to C$.

##### _proposition:_ factoring long exact sequences

Note that a (long) exact sequence $A^\bullet$ given by $f^i : A^i \to A^{i + 1}$ is uniquely determined by a collection of short exact sequences
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker f^i \ar[r] & A^i \ar[r] & \ker \, f^{i + 1} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
and is said to be "factored into" them.

A similar fact holds if the sequence is only assumed to be a complex with the use of [[Algebraic geometry --- rising-sea/notes/Homology of complexes|homology]].

### The (abelian) category of complexes

We can define morphisms of complexes, and even add and subtract them. In fact, they form an abelian category.

##### _definition:_ morphisms of complexes

A **morphism of complexes** $\varphi : A^{\bullet}$ and $B^{\bullet}$ (defined by $f^i : A^i \to A^{i + 1}$ and $g^i : B^i \to B^{i + 1}$) is a collection of morphisms $\varphi^i$ so that the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & A^{i - 1} \ar[r, "f^{i - 1}"] \ar[d, "\varphi^{i - 1}"] & A^i \ar[r, "f^i"] \ar[d, "\varphi^i"] & A_{i + 1} \ar[r, "f^{i + 1}"] \ar[d, "\varphi^{i + 1}"] & \cdots \\
		\cdots \ar[r] & B^{i - 1} \ar[r, "h^{i - 1}"] & B^i \ar[r, "g^i"] & B_{i + 1} \ar[r, "g^{i + 1}"] & \cdots
	\end{tikzcd}
\end{document}
```

##### _proposition:_ complexes form an abelian category

$\mathsf{Com}_{\mathscr{C}}$, the category of complexes over an abelian category $\mathscr{C}$ is an abelian category.

Note that essentially the same argument proves that the functor category $\mathscr{C}^{\mathscr{I}}$ is an abelian category for $\mathscr{I}$ small and $\mathscr{C}$ abelian.