---
tags:
- uc-2026
- cat-th
- alicia-lima
---

An $\infty$-category (or more specifically, a quasi-category) is a certain particularly nice type of simplicial set. They allow us to use simplicial methods without having to do explicit combinatorics.

##### _definition:_ $\infty$-category

An **$\infty$-category** is a [[UChicago --- uc-2026/notes/Simplicial sets#_definition _ simplicial sets, simplex category, simplicial objects|simplicial set]] $X$ such that each inner horn has a **filler** — for each $0 < k < n$, each diagram of the form below commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\Lambda_{k}^n \ar[d, hook] \ar[r] & X \\
		\Delta^n \ar[ru, dashed, "\exists"]
	\end{tikzcd}
\end{document}
```

That is, each inner horn $\Delta^n_{k} \to X$ extends to an $n$-simplex $\Delta^n \to X$.

---