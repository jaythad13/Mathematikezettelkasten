---
tags:
- math-145/12
- alg-top
---

Euler's formula for ([[Superdiscrete --- math-55a/notes/Special graphs#_definition _ planar graph|planar]]) graphs gives an invariant for graphs in terms of the number of vertices, edges, and faces. This is in fact a statement about the homology of the graph as a [[Topics in Geometry and Topology --- math-145/notes/Simplicial complexes#_definition _ simplicial complex|simplicial complex]]. In fact, this can be generalised to a statement about the homology of any graph!

##### _theorem:_ Euler's formula for graphs

For a graph $G$ (understood to be a simplicial complex), and a field $\mathbb{F}$
$$
\mathrm{b}_{0}(G, \mathbb{F}) - \mathrm{b}_{1}(G, \mathbb{F}) = v - e
$$
where $v = \# V(G)$ and $e = \# E(G)$.

###### _proof sketch:_

This is just an application of rank-nullity. Note that the [[simplicial chain complex]] looks like
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 & \mathbb{F}^n \ar[l, "\partial"] & \mathbb{F}^m \ar[l, "\partial"] & 0 \ar[l, "\partial"]
	\end{tikzcd}
\end{document}
```
Apply rank-nullity to the maps and to the quotients of the maps.

More generally, we find that the alternating sum of [[Topics in Geometry and Topology --- math-145/notes/Simplicial homology#_definition _ simplicial homology, Betti number|Betti numbers]] is actually the same as the alternating sum of the dimension of the $k$-[[Topics in Geometry and Topology --- math-145/notes/Simplicial homology#_definition _ chains|chains]], which is just the size of the 

##### _theorem:_ Euler's formula for simplicial complexes

For any simplicial complex $X$, the [[Topics in Geometry and Topology --- math-145/notes/Whitehead equivalence#_definition _ the Euler characteristic|Euler characteristic]] is
$$
\chi(X) = \sum_{k = 0}^n (-1)^k \dim \mathrm{C}_{k}(X, \mathbb{F}).
$$