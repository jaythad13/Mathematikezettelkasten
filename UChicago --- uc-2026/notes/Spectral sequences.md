---
tags:
- uc-2026/alg-top/5
- alg-top
- hom-alg
---

Let $A$ be a (commutative, unital) ring. Let $\mathscr{C}$ be an [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ abelian categories|abelian category]].

##### _definition:_ spectral sequences

A **homological spectral sequence** in $\mathscr{C}$ is a sequence of objects $E^r$ for all $r \geq r_{0}$ and endomorphisms $d^r : E^r \to E^r$ forming a [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_proposition _ complexes form an abelian category|complex]], such that the $(r + 1)$th complex $E_{\bullet}^{r + 1}, d^{r + 1}$ is the homology $H_{\bullet}(E^r_{\bullet})$.

A **cohomological spectral sequence** in $\mathscr{C}$ is a sequence of objects $E_{r}$ for all $r \geq r_{0}$ and endomorphisms $d_{r} : E_{r} \to E_{r}$ forming a complex, such that the $(r + 1)$th complex $E^{\bullet}_{r + 1}, d_{r + 1}$ is the cohomology $H^{\bullet}(E^r_{\bullet})$.

In practice, we often choose each $E_{r}$ to be a doubly graded $A$-module.

A homological spectral sequence is a sequence of $A$-modules $E^r_{p, q}$ (starting from $r = 0, 1, 2$ and with $p, q \in \mathbb{Z}$) with **differentials** $d^r_{p, q} : E_{p, q}^r \to E^r_{p - r, q + r - 1}$ such that the sequence of differentials forms a [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ complexes, exactness, short exact sequence|complex]] of $A$-modules, and the homology of the $(p, q)$th diagonal on the $r$th page is $\ker d^r_{p, q} / \operatorname{img} d_{p + r, q - r + 1}^r \cong E_{p, q}^{r + 1}$ — the $(p, q)$th term on the $(r + 1)$th page.

A spectral sequence in cohomology has maps $d_{r} : E_{r}^{p, q} \to E_{r}^{p + r, q - r + 1}$.

---

Sometimes spectral sequences have slightly different grading.

##### _example:_ the Bockstein spectral sequence

One example in homology (with a slightly different grading) is the Bockstein spectral sequence. It uses the fact that you can compare homology in $\mathbb{Z}$ and $\mathbb{F}_{p}$ by turning the short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathbb{Z} \ar[r, "p \times"] & \mathbb{Z} \ar[r] & \mathbb{F}_{p} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
into a long exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & H_{q}(C_{\bullet} \otimes \mathbb{Z}) \ar[r, "f_{*}"] & H_{q}(C_{\bullet} \otimes \mathbb{Z}) \ar[r, "g_{*}"] & H_{q}(C_{\bullet}, \mathbb{F}_{p})
	\end{tikzcd}
\end{document}
```


---

### The Serre spectral sequence

One of the most useful spectral sequences is the Serre spectral sequence.

##### _definition:_ (Hurewicz) fibration

A surjective continuous map $\pi : E \to B$ is a **Hurewicz fibration** if it satisfies the **homotopy lifting property** for all spaces $X$ as test spaces. That is, if the following diagram commutes without the dashed arrow, then there exists a dashed arrow such that it commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		X \ar[r, "f"] \ar[d, "\mathrm{id}_{X} \times \{ 0 \}"'] & E \ar[d, "\pi"] \\
		X \times [0, 1] \ar[r] \ar[ru, dashed] & B
	\end{tikzcd}
\end{document}
```

$\pi : E \to B$ is a **Serre fibration** if it satisfies the homotopy lifting property for all polydiscs $\mathbb{D}^n$ as test spaces.

---

##### _definition, proposition:_ Serre spectral sequence

Suppose $\pi : E \to B$ is a Hurewicz fibration. Then the **homological Serre spectral sequence** is given by
$$
E^2_{p, q} = H_{p}(B, H_{q}(\pi^\text{pre}(b), A)) \implies H_{p + q}(E, A)
$$
converging to the homology of $E$.

---

If $A$ is a field, then 
$$
E_{p, q}^{2} = H_{p}(B, A \otimes H_{q}(\pi^\text{pre}(b), A)) = H_{p}
(B, A) \otimes H_{q}(\pi^\text{pre}(b), A).
$$
By the Künneth formula, it shouldn't be surprising that this converges to the homology of $E$.