---
tags:
- math-189AA/24
- hom-alg
- comm-alg
---

The Koszul complex is important for mysterious reasons.

##### _definition:_ the tensor product of complexes

Suppose $(C_{\bullet}, d_{i})$ and $(D_{\bullet}, \delta_{i})$ are complexes of $A$-modules. The **tensor product of complexes** is the complex $(C_{\bullet} \otimes D_{\bullet})$ with $(C_{\bullet} \otimes D_{\bullet})_{n} = \oplus_{i + j = n} C_{i} \otimes D_{j}$ with the map $\gamma_{n} : (C_{\bullet} \otimes D_{\bullet})_{n} \to (C_{\bullet} \otimes D_{\bullet})_{n - 1}$ given by $\gamma_{n}(c \otimes d) = (d_{i}(c) \otimes d) \oplus (-1)^i (c \otimes \delta_{j}(d))$ on a pure tensor $c \otimes d \in C_{i} \otimes D_{j}$.

---

##### _definition:_ Koszul complex

Let $x = x_{1}, \dots, x_{n}$ be a sequence of elements in $A$. Let $M$ be an $A$-module. Define $K(x_{i}, A)$ to be the complex
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & A \ar[r, "\times x_{i}"] & A \ar[r] & 0
	\end{tikzcd}
\end{document}
```
Then the **Koszul complex** of $A$ is
$$
K(x, A) = \bigotimes_{x_{i}} K(x_{i}, A)
$$
and the **Koszul complex of $M$** is $K(x, A) \otimes M$.

---

##### _proposition:_

When $x$ is a regular sequence, $K(x, A)$ is a free resolution of $A / (x)$.