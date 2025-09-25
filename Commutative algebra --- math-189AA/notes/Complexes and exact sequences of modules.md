---
tags:
- math-189AA/9
- math-189AA/10
- comm-alg
---

Complexes and exact sequences of $A$-modules are exactly complexes and exact sequences in the category of $A$-modules.

![[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ complexes, exactness, short exact sequence|Complexes and exactness]]

So is homology!

![[Algebraic geometry --- rising-sea/notes/Homology of complexes#_definition _ homology, boundaries, cycles, cohomology|Homology of complexes]]

##### _example:_ the cell complex of a torus

We can draw a torus $X$ as a the [[Topology --- math-147/notes/Quotient and identification spaces#_definition _ identification space|identification space]] $\mathbb{C} / \Lambda$ for some lattice $\Lambda$. We can write this identification space as a cell complex — a disjoint union of points, lines, discs et c., modulo some attaching equivalence relations. We have one $0$-cell, two $1$-cells, and one $2$-cell.

Write the module of $0$-cells as $\mathbb{Z}$, $1$-cells as $\mathbb{Z}^{\oplus 2}$, and $2$-cells as $\mathbb{Z}$ again. Then, we have a map from $k$-cells to $(k - 1)$-cells by mapping a cell to its boundary. That is, send the $1$-cell between $0$-cells $v_{1}, v_{2}$ to the $0$-cell $v_{2} - v_{1}$. In this case, all $0$-cells on the torus have no boundary. Note that if we did this over $\mathbb{Z} / (2)$, then we wouldn't need to care about signs at all.

Taking homology gives $H_0(X) = \mathbb{Z} = H_{2}(X)$ and $H_{1}(X) = \mathbb{Z}^{\oplus 2}$ which tells us that the space has one connected component, two one-dimensional holes, and is a closed surface with one two-dimensional hole.

---

##### _example:_ the cell complex of a Klein bottle

Write the Klein bottle $X$ as a CW-complex with one $0$-cell $v$ (after identification), two $1$-cells $e_{1}$ and $e_{2}$, with $e_{2}$ twisted, and one $2$-cell $u$. The cell complex is then.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathbb{Z} \ar[r] & \mathbb{Z}^{\oplus 2} \ar[r] &  \mathbb{Z} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
Here $\partial_{2}$ given by $u \mapsto 2 e_{2}$ and $\partial_{1} = 0$. Thus, $H_{0}(X) = \mathbb{Z} / 0 \cong \mathbb{Z}$, $H_{1}(X) = \mathbb{Z}^{\oplus 2} / \mathbb{Z} \cong \mathbb{Z}$, and $H_{2}(X) = 0 / 0 = 0$. This means it is connected, with two $1$-holes, and non-oriented (respectively).

---

##### _example:_ de Rham cohomology on $\mathbb{R}^3$

For any open domain $U \subseteq \mathbb{R}^{3}$, the following is a complex. Since the arrows go in the opposite direction with the opposite indices, we call the homology cohomology.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		C^\infty(U \to \mathbb{R}) \ar[r, "\nabla"] & C^\infty(U \to \mathbb{R}^3) \ar[r, "\nabla \times"] & C^\infty(U \to \mathbb{R}^{3}) \ar[r, "\nabla \cdot"] & C(U \to \mathbb{R})
	\end{tikzcd}
\end{document}
```
If we have $U$ simply connected, then the complex is exact.

This is saying that if every loop in $U$ is contractible, then a vector field with no curl is the gradient of some potential, and a vector field with no divergence is the curl of some other vector field. If either of these fail, then we know that there's a hole in $U$.

---

##### _example:_ the natural exact sequence

For any $\varphi : M \to N$ there is a natural exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker \varphi \ar[r, hook] & M \ar[r, "\varphi"] & N \ar[r, two heads] & \mathrm{coker} \, \varphi \ar[r] & 0.
	\end{tikzcd}
\end{document}
```

---

##### _example:_ free resolution

Let $A = \mathbb{F}[x, y] / (xy)$ for some field $\mathbb{F}$, then the projective resolution of $A / (x)$ as an $A$-module is
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[rr, "\times x"] && A \ar[rr, "\times y"] \ar[rd] && A \ar[rr, "\times x"] \ar[rd] && A \ar[r, two heads] & A / (x) \\
		&&& (y) \ar[ru] && (x) \ar[ru] 
	\end{tikzcd}
\end{document}
```

---

##### _example:_ exact sequences tell you things

If
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		M \ar[r, "f"] & N \ar[r, "g"] & P \ar[r, "h"] & Q
	\end{tikzcd}
\end{document}
```
is exact, then $f$ is surjective if and only if $h$ is injective. If $f$ is surjective, then $\ker g = N$ so $\operatorname{img} g = 0$, giving $\ker h = 0$. If $h$ is injective, then $\ker h = 0$ giving $\operatorname{img} g = 0$ implying $\ker g = N$ implying $\operatorname{img} f = N$.

If
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		A \ar[r, "\alpha"] & B \ar[r, "\beta"] & C \ar[r, "\gamma"] & D \ar[r, "\delta"] & E
	\end{tikzcd}
\end{document}
```
is exact and $\alpha, \delta$ are isomorphisms, then $C = 0$. If $\alpha$ is an isomorphism, then $\beta = 0$ since it has $\ker \beta = \operatorname{img} \alpha = B$. Similarly, by exactness at $D$, $\operatorname{img} \gamma = \ker \delta = 0$ so $\gamma = 0$. Since $\ker \gamma = \operatorname{img} \beta = 0$, we have that $0$ is injective on $C$. Thus, $C = 0$.

---