---
tags:
- math-145/13
- alg-top
---

In order to prove that [[Topics in Geometry and Topology --- math-145/notes/Simplicial homology|simplicial homology]] really is a [[Topics in Geometry and Topology --- math-145/notes/Whitehead equivalence#Whitehead invariants|Whitehead invariant]], we will need some machinery to generally analyse the objects of cohomology that we've been looking at so far.

##### _definition:_ chain complex

A chain complex $V_{}$ is a collection of vector spaces $V_{n}$ and linear maps $\partial_{n} \to V_{k + 1} \to V_{k}$
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		V_{0} & \ar[l, "\partial_{0}"] V_{1} & \ar[l, "\partial_{1}"] V_{2} & \ar[l, "\partial_{2}"] \dots
	\end{tikzcd}
\end{document}
```
such that $\partial_{k + 1} \partial_{k} = 0$ for all $n$.

There is of course, a notion of morphisms of such objects

##### _definition:_ chain map

Given chain complexes $V, W$, a chain map $T : V \to W$ between them is a collection of maps $T : V_{k} \to W_{k}$ so that the squares in the following diagram commute —
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		V_{0} \ar[d, "T_{0}"] & \ar[l, "\partial_{V, 0}"] V_{1} \ar[d, "T_{1}"] & \ar[l, "\partial_{V, 1}"] V_{2} \ar[d, "T_{2}"] & \ar[l, "\partial_{V, 2}"] \dots \\
		W_{0} & \ar[l, "\partial_{W, 0}"] W_{1} & \ar[l, "\partial_{W, 1}"] W_{2} & \ar[l, "\partial_{W, 2}"] \dots
	\end{tikzcd}
\end{document}
```

We can check that

##### _definition:_ homology of a chain complex

We can check that the maps of chain complexes in fact give rise to maps of their homology

##### _proposition:_ maps of chain complexes give maps of homology

Given a chain map $T : V \to W$, there is a linear map $\mathrm{H}_{k}T : \mathrm{H}_{k}(V) \to \mathrm{H}_{k}(W)$ by $\gamma + \operatorname{img} \partial_{V, k} \mapsto$.

We want to know when two chain maps induce the same map on homology, so that eventually we can show that we have isomorphisms of each homology. Chain homotopies give us a way to do this.

##### _definition:_ chain homotopy

Given chain maps $S, T : V \to W$, a chain homotopy $K : S \to T$ is a collection of maps $K_{k} : V_{k} \to W_{k + 1}$ such that $K_{0} \partial_{0} + K_{1} \partial_{1} = T - S$.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		V_{0} \ar[dd, "T_{0}"] \ar[rdd, "K_{0}"] & \ar[l, "\partial_{V, 0}"] V_{1} \ar[dd, "T_{1}"] \ar[rdd, "K_{1}"] & \ar[l, "\partial_{V, 1}"] V_{2} \ar[dd, "T_{2}"] & \ar[l, "\partial_{V, 2}"] \dots \\ \\
		W_{0} & \ar[l, "\partial_{W, 0}"] W_{1} & \ar[l, "\partial_{W, 1}"] W_{2} & \ar[l, "\partial_{W, 2}"] \dots
	\end{tikzcd}
\end{document}
```

##### _theorem:_ chain homotopic chain maps induce the same map on homology

Given chain homotopy $K : S \to T$ on chain maps $S, T : V \to W$, the induced maps on homology $S_{*}, T_{*}$