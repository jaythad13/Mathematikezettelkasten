---
tags:
- math-199DR/10
- alg-top
---

### Homotopy

##### _definition:_ paths, loops

In a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]] $X$, a path is a continuous map $\gamma : [0, 1] \to X$.

A loop is a path $\gamma$ with $\gamma(0) = \gamma(1)$.

##### _definition:_ homotopic

Two paths $\gamma_{1}, \gamma_{2}$ are homotopic if there's a continuous map $[0, 1] \times [0, 1] \to X$ with $H(0, t) = \gamma_{1}(t)$ and $H(1, t) = \gamma_{2}(t)$, such that $H(s, 0)$ and $H(s, 1)$ are constant. 

This forms an equivalence relation with [[Simplicial homology and random walks --- math-145/notes/Continuous and differentiable winding number|winding number]] able to tell non-homotopic loops apart.

##### _definition:_ the fundamental group (based ay $x \in X$)

The set of loops based at $x \in X$ (with $\gamma(0) = \gamma(1) = x$) forms $\pi_{1}(X, x)$, the (first) fundamental group of $X$ (based at $x$) with $\gamma_{1} \gamma_{2} : [0, 2] \to X$  equal to $\gamma_2$ on $[0, 1]$ and $\gamma_{1}$ on $[1, 2]$. 

If $X$ is [[Complex analysis --- math-135/notes/Analysis and (metric) topology review#_definition _ path-connected|path-connected]] (which is [[Complex analysis --- math-135/notes/Analysis and (metric) topology review#_proposition _ path-connectedness and connectedness are equivalent on open sets|equivalent to connected for manifolds]]).

### Covering spaces

##### _definition:_ covering map, covering space

$f : X \to Y$ is a covering map and $X$ is a covering space for $Y$ if for every $p \in Y$, there exists some $W \subseteq Y$ containing $p$ with every $f^\text{pre}(W)$ is a disjoint union of open sets in $X$, say $U_{\alpha}$ where each $U_{\alpha}$ is homeomorphic to $W$ under the restriction $f_{|U}$.

##### _example:_ $\mathbb{C} \setminus \{ 0 \}$ covers itself non-trivially

$z \mapsto z^n$ is a covering map ${ \mathbb{C} \setminus \{ 0 \} } \to {\mathbb{C} \setminus \{ 0 \}}$.

##### _theorem:_ paths lift

For any covering map $f : X \to Y$ and loop $\gamma : [0, 1] \to Y$ based at $q = f(p)$, we can lift $\gamma$ to a unique path $\tilde{\gamma} : [0, 1] \to X$ such that the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		I \ar[r, "\tilde{\gamma}"] \ar[rd, "\gamma"] & X \ar[d, "f"] \\
		& Y
	\end{tikzcd}
\end{document}
```



Notice that this induces a group action of $\pi_{1}(Y, q)$ on a covering space $f : X \to Y$.

##### _theorem:_ the universal cover

For any real manifold $X$ (satisfying some technical condition that all [[Riemann surfaces and algebraic curves --- math-199DR/notes/Riemann surfaces#_definition _ (compact, connected) Riemann surface, (holomorphic) atlas, chart|Riemann surfaces]] satisfy), there exists a unique (up to cover isomorphism) cover $f_{0} : U_{0} \to X$ such that the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		U_{0} \ar[r, "g"] \ar[rd, "f_{0}"] & U \ar[d, "f"] \\
		& X
	\end{tikzcd}
\end{document}
```

Quotienting $U_{0}$ by $\pi_{1}(X, p)$ gives $X$ and quotienting by any subgroup gives a connected cover.

##### _example:_ the universal cover of the punctured plane

The universal cover of ${\mathbb{C} \setminus \{ 0 \}}$ is the cover $f : \mathbb{C} \to {\mathbb{C} \setminus \{ 0 \}}$ by $f(z) = e^z$.