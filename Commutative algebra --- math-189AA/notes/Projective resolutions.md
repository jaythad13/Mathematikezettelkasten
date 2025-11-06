---
tags:
- hom-alg
- comm-alg
- math-189AA/14
- math-189AA/19
- math-189AA/21
---

Projective resolutions help us understand non-projective modules in terms of projective modules. In particular, they help us understand how far a module is from being projective.

##### _definition:_ projective resolution, syzygies

A **projective resolution** of an $A$-module $M$ is a [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ complexes, exactness, short exact sequence|complex]] $P_{\bullet}$ with $P_{i}$ projective and $P_{i} = 0$ for $i < 0$ together with an augmentation map $\varepsilon : P_{0} \to M$ such that the augmented complex
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & P_{2} \ar[r, "d_{2}"] & P_{1} \ar[r, "d_{1}"] & P_{0} \ar[r, "\varepsilon"] & M \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is exact.

The kernels $\ker d_{n}$ are called the **syzygies** of $M$, denoted $\Omega^n M$.

---

##### _definition:_ presentation matrix

When $P_{0}, P_{1}$ are finitely generated free modules in a free resolution of an $A$-module $M$, the map $\alpha : P_{1} \to P_{0}$ can be represented as a matrix. This matrix is called the **presentation matrix** of $M$.

---

We can always construct a projective resolution inductively, using the fact that every module is a quotient of a free module.

##### _proposition:_ constructing a projective module

For any $A$-module $M$, there exists a projective resolution of $M$.

###### _proof sketch:_

Choose $P_{0}$ free, giving a short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker \varepsilon \ar[r] & P_{0} \ar[r, "\varepsilon"] & M \ar[r] & 0.
	\end{tikzcd}
\end{document}
```
Then choose $P_{i}$ surjecting onto each $\ker d_{i - 1}$ (for example, choose $P_{i}$ free) so that the following sequence is exact.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker d_{i}' \ar[r] & P_{i} \ar[r] & \ker d_{i - 1}' \ar[r] & 0
	\end{tikzcd}
\end{document}
```
Then piece them together as
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& & 0 \ar[rd] & & 0 \\
		& & & \ker \varepsilon \ar[rd] \ar[ru] \\
		\cdots \ar[rr, "d_{2}"] \ar[rd, "d_{2}'"] & & P_{1} \ar[rr, "d_{1}"] \ar[ru, "d_{1}'"] & & P_{0} \ar[rr] \ar[rd, "\varepsilon"] & & 0 \\
		& \ker d_{1}' \ar[ru] \ar[rd] & & & & M \ar[ru] \ar[rd] \\
		0 \ar[ru] & & 0 & & & & 0
	\end{tikzcd}
\end{document}
```

---

Projective resolutions play nicely with exact sequences.

##### _lemma:_ the horseshoe lemma, or the simultaneous resolution lemma

Suppose
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & M' \ar[r] & M \ar[r] & M'' \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is exact, and $P_{\bullet}'$ and $P_{\bullet}''$ are projective resolutions of $M'$ and $M''$ respectively. Then there is a projective resolution $P_{\bullet}$ of $M$ such that the projective resolutions form an exact sequence. 
That is, the diagram below commutes and has exact rows for each $i$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
			0 \ar[r] & P_{i + 1}' \ar[r] \ar[d] & P_{i + 1} \ar[r] \ar[d] & P_{i + 1}'' \ar[r] \ar[d] & 0 \\
			0 \ar[r] & P_{i}' \ar[r] & P_{i} \ar[r] & P_{i}'' \ar[r] & 0
	\end{tikzcd}
\end{document}
```

###### _proof sketch:_

We show this by induction and really only show the base case. Consider the diagram
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& P_{0}' \ar[d, "\varepsilon'"] & & P_{0}'' \ar["\varepsilon''", d] \\
		0 \ar[r] & M' \ar[r, "i"] & M \ar[r, "j"] & M'' \ar[r] & 0
	\end{tikzcd}
\end{document}
```

Choose $P_{0} = P_{0}' \oplus P_{0}''$. $P_{0}$ is projective since it is the direct sum of projectives. Choosing $\varepsilon : P_{0} \to M$ by $p' \oplus p'' \mapsto i \circ \varepsilon'(p') + j \circ \varepsilon(p'')$ ensures that the diagram 
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & P_{0}' \ar[d, "\varepsilon'"] \ar[r] & P_{0} \ar[r] \ar[d, "\varepsilon"] & P_{0}'' \ar["\varepsilon''", d] \ar[r] & 0 \\
		0 \ar[r] & M' \ar[r, "i"] & M \ar[r, "j"] & M'' \ar[r] & 0
	\end{tikzcd}
\end{document}
```
commutes. Also, by our choice of maps, the top row is exact. All we need to do is show that $\varepsilon$ is a surjection. The [[Algebraic geometry --- rising-sea/notes/Lemmas in a general abelian category#_lemma _ the snake lemma|snake lemma]] (and the surjectivity of $\varepsilon', \varepsilon''$) ensures that $\operatorname{coker} \varepsilon = 0$ and thus, $\varepsilon$ is surjective.

---

Projective resolutions don't uniquely determine modules.

##### _example:_ projective resolutions are not unique

$\mathbb{Z} / (3)$ is a projective $\mathbb{Z} / (6)$-module. Thus, we can choose the whole complex to be just  with $\varepsilon : \mathbb{Z} / (3) \to \mathbb{Z} / (3)$ just the identity. However,
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathbb{Z} / (2) \ar[r] & \mathbb{Z} / (6) \ar[r] & \mathbb{Z} / (3) \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is also a free resolution (or rather, the augmented complex of a projective resolution) of $\mathbb{Z} / (3)$.

---

The homology isn't actually how we extract information about the module we are resolving. It doesn't tell us anything particularly interesting.

##### _proposition:_ homology of a projective resolution

For $n \geq 1$, the homology is $H_{n}(P_{\bullet}) = 0$ and the zeroth homology is $H_{0}(P_{\bullet}) = M$.

###### _proof sketch:_

Follows directly from the exactness of the augmented sequence.

---

Instead, we define new invariants.

### Projective dimension

##### _definition:_ projective dimension, minimal projective resolution

An $A$-module $M$ has **finite projective dimension** if there exists a projective resolution of finite length.

Its **projective dimension** $\operatorname{proj dim} M = n$ is the least such length $n$ such that there exists $P_{\bullet}$ is a projective resolution with $P_{m} = 0$ for all $m > n$.

Such a projective resolution of minimal length is called a **minimal projective resolution**.

If there is no such finite length projective resolution, we say $\operatorname{proj dim} M = \infty$.

---

##### _example:_ projective dimension $0$

An $A$-module $M$ has projective dimension $0$ if and only if it is projective. (Exactness of the augmented sequence would require $\varepsilon : P_{0} \to M$)

---

We should probably show that this really is a well-defined invariant of a module.

##### _proposition:_ projective dimension is an isomorphism invariant

For any two isomorphic $A$-modules $M \cong N$, we have $\operatorname{proj dim} M = \operatorname{proj dim} N$.

###### _proof sketch:_

For any projective resolution $P_{\bullet}$ of $M$ we can construct a projective resolution of $N$ of the same length
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & P_{2} \ar[r] & P_{1} \ar[r] & P_{0} \ar[rd, "\varepsilon_{N}"] \ar[r, "\varepsilon_{M}"] & M \ar[d, "\sim"] \ar[r] & 0 \\
		& & & & N
	\end{tikzcd}
\end{document}
```
---

The horseshoe lemma tells us further that projective dimension behaves well in short exact sequences.

##### _proposition:_ projective dimension in short exact sequences

Suppose
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
				0 \ar[r] & M' \ar[r] & M \ar[r] & M'' \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is exact. Then $\operatorname{proj} \dim M \leq \max \{ \operatorname{proj} \dim M', \operatorname{proj} \dim M'' \}$.

---


How do we construct a minimal projective resolution? Homological algebraists have done this for us already.

##### _theorem:_ constructing minimal projective resolutions

The projective resolution obtained by choosing the minimal free module [[#_proposition _ constructing a projective module|in the construction above]] is minimal.

---

##### _example:_ constructing a minimal projective resolution

Consider $(x)$ as a $\mathbb{Q}[x, y, z]$-module. The first surjection is just $\mathbb{Q}[x, y, z] \to (x)$ by $p \mapsto px$. Since $\mathbb{Q}[x, y, z]$ is an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]], this has kernel $0$.

In general, this follows because every [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ principal ideal domain|principal ideal]] of an integral domain is isomorphic to the ring (as a module over the ring).

---

### Betti numbers

The Betti numbers of a module describe

##### _definition:_ Betti numbers

Let $M$ be a finitely generated module over a local ring $A, \mathfrak{m}$. Then if $P_{\bullet}$ is a minimal free resolution of $M$, we define the **Betti numbers** $\beta_{i}(M)$ of $M$ to be the dimensions of the free modules $P_{i}$. 

That is, if
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & A^{\oplus \beta_{2}(M)} \ar[r] & A^{\oplus \beta_{1}(M)} \ar[r] & A^{\oplus \beta_{0}(M)} \ar[r] & M
	\end{tikzcd}
\end{document}
```
is a minimal free resolution, then the $\beta_{i}(M)$ are the Betti numbers.

---