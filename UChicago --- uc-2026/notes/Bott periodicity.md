---
tags:
- alg-top
- peter-may
- uc-2026/alg-top/8
---

By some standard computations in algebraic topology, it suffices to give a map $\beta : B \mathrm{U} \to \Omega \mathrm{SU}$ that induces an isomorphism on homology. Specifically, all the solid arrows below are homotopy equivalences. Thus, it suffices to give a homotopy equivalence $\Omega \mathrm{SU} \simeq \Omega B \mathrm{U}$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\Omega \mathrm{SU} \times \mathbb{Z} \ar[r] & \Omega \mathrm{U} \ar[r] & \Omega^{2} B \mathrm{U} \ar[d] \\
		\Omega B\mathrm{U} \times \mathbb{Z} \ar[rr, dashed] \ar[u, dashed] & & \Omega^{2}(B \mathrm{U} \times \mathbb{Z})
	\end{tikzcd}
\end{document}
```


The first step is to give a new model for $B \mathrm{U}$.

##### _proposition:_

Let $\mathrm{U}_{n}$ be the group of unitary transformations of $\mathbb{C}^n$. Then for
$$
\mathrm{U} / \mathrm{U} \times \mathrm{U} = \operatorname{colim}_{n \to \infty} \mathrm{U}_{2n} / \mathrm{U}_{n} \times \mathrm{U}_{n}
$$
we have $B \mathrm{U} \cong \mathrm{U} / \mathrm{U} \times \mathrm{U}$.

###### _proof:_

---

##### _proposition:_

###### _proof:_

Let $V = \mathbb{C}^\infty$ and consider the group of unitary linear maps $\mathrm{U}(V^{\oplus 2})$. There is a function $[0, \pi] \to \mathrm{U}(V^{\oplus 2})$ by $\theta \mapsto \nu_{\theta}$ where $\nu_{\theta}(z_{1} \oplus z_{2}) = e^{i \theta} z_{1} \oplus e^{-i \theta} z_{2}$. Then consider $\beta : \mathrm{U}(V^{\oplus 2}) \to \Omega \mathrm{SU}(V^{\oplus 2})$ by $T \mapsto \nu_{T}$ where $\nu_{T}(\theta) = T v_{\theta} T^{-1} \nu_{- \theta}$.

This gives the diagram below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{U}_{n + 1} / \mathrm{U}_{n} \times \mathrm{U}_{1} \ar[r, "\alpha"] \ar[d, "j"] & \Omega \mathrm{SU}_{n + 1} \ar[d, "\Omega j"] \\
		\mathrm{U}_{n + n} / \mathrm{U}_{n} \times \mathrm{U}_{n} \ar[r, "\beta"] & \Omega \mathrm{SU}_{n _{ n}}
	\end{tikzcd}
\end{document}
```
Passing to the colimit as $n \to \infty$ we have
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathbb{C} \mathbb{P}^\infty \ar[r, "\alpha"] \ar[d, "j"] & \Omega \mathrm{SU} \ar[d, "\Omega j"] \\
		B \mathrm{U} \ar[r, "\beta"] & \Omega \mathrm{SU}
	\end{tikzcd}
\end{document}
```
where $\Omega j$ is a homotopy equivalence.

---