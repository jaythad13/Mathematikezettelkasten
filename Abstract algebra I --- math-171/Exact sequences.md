---
tags:
- math-171
- alg
- cat-th
lecture:
- math-171-6
---

Exact sequences are a category theory thing, but here we're always working in $\mathsf{Grp}$ or $\mathsf{Ring}$.

##### _definition:_ sequence

A sequence is an ordered collection of objects (here groups or rings) and arrows (here homomorphisms)

##### _definition:_ exact sequence

An sequence is exact if the kernel of each arrow (that has a preceding arrow) is the image of the arrow before.

##### _examples:_ exact sequences

1) The [[The exterior derivative|exterior derivative]] gives rise to the exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r, "d"] & \Omega^k(U) \ar[r, "d"] \ar[rr, "d^2 = 0", bend right] & \Omega^{k + 1}(U) \ar[r, "d"] & \Omega^{k + 2}(U) \ar[r, "d"] & \cdots
	\end{tikzcd}
\end{document}
``` 
on any simply connected region of a manifold, $U$.
Note that all the maps in an exact sequence need not be the same
2) The sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		(\mathbb Z, +) \ar[r, "f"] \ar[rr, "f \circ g = 0", bend right] & (\mathbb Z, +) \ar[r, "g"] & (\mathbb Z/2 \mathbb Z, +)
	\end{tikzcd}
\end{document}
```
is exact. Here $f : x \mapsto 2x$ and $g$ is the canonical map by $x \mapsto x + 2 \mathbb{Z}$

Exact sequences allow us to say things about the maps involved in them

##### _examples:_ deductions by exact sequence 

Let $0$ denote the trivial group (with only the identity).
1) If the following sequence is exact, then we must have that $\psi$ is injective.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r, "\varphi"] & A \ar[r, "\psi"] & B
	\end{tikzcd}
\end{document}
```
2) If the following sequence is exact, then we must have that $\psi$ is surjective.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		A \ar[r, "\psi"] & B \ar[r, "\theta"] & 0
	\end{tikzcd}
\end{document}
```
3) And naturally, if the following sequence is exact, then we must have that $\psi$ is an isomorphism.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r, "\varphi"] & A \ar[r, "\psi"] & B \ar[r, "\theta"] & 0
	\end{tikzcd}
\end{document}
```
##### _example:_ short exact sequence

The most common exact sequence we see is
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r, "\varphi"] & A \ar[r, "\psi"] & B \ar[r, "\kappa"] & C \ar[r, "\theta"] & 0
	\end{tikzcd}
\end{document}
```
It is called a short exact sequence and it tells us that $\varphi$ is injective, $\kappa$ is surjective, and $\ker \kappa = \operatorname{im} \varphi$.