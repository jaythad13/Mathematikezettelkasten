---
tags:
- diff-geo
- math-142
lecture:
- math-142-29
---

Now that we have a good idea of [[Surfaces|surfaces]], we can start to calculus on them, like we would want to (perhaps, for physics, or just for math's own sake). Basically, the openness of each of the domains of the [[Surfaces#_definition _ coordinate patch|coordinate patches]] means that we can take derivatives and limits inside them, and then we will try in some sense to transfer them to the neighbourhoods of the points on the surface.

What we want to come out with is a well defined notion of when $f : M \to \mathbb{R}$ is differentiable, for some surface $M$.

### Differentiable functions

Say $M \subset \mathbb{R}^3$ is a surface, with the family $x_{\alpha} : D_{\alpha} \to \mathbb{R}^3$ of proper patches indexed by $\alpha \in I$. If we look at any $p \in M$, we have some neighbourhood $N$ contained in the image of all of the patches. We can look at $U_{\alpha} = x_{\alpha}^{\text{pre}}(N)$ for each $\alpha \in I$, which we know will be an open set by the continuity of $x_{\alpha}$.

Note that for any function $f : M \to \mathbb{R}$, we can write $f_{\alpha} = f \circ x_{\alpha}$ as a sort of "coordinate expression" of the function — where $f$ takes points in $M$ to $\mathbb{R}$, $f_{\alpha}$ takes its coordinates in $D_{\alpha}$ to $\mathbb{R}$. Then we know we can just differentiate $f_{\alpha}$ since $x^\text{pre}_{\alpha}(N)$ is open.

Basically
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		D_\alpha \ar[r, "x_\alpha"] \ar[rr, "f_\alpha", bend right] & M \ar[r, "f"] & \mathbb R
	\end{tikzcd}
\end{document}
```
where $x_{\alpha} : (u, v) \mapsto p$ and $f : p \to f(p)$.

We say $f$ is differentiable if all of the $f_{\alpha}$ are differentiable. That is,

##### _definition:_ smooth functions on a surface

For a surface $M$ with the family $x_{\alpha} : D_{\alpha} \to \mathbb{R}^3$ of proper patches indexed by $\alpha \in I$, we say a function $f : M \to \mathbb{R}$ is smooth or $f \in \mathcal{C}^\infty(M)$ if each $f_{\alpha} = x_{\alpha} \circ f$ is a smooth function $f_{\alpha} \in \mathcal{C}^\infty(D_{\alpha})$.

We can also do something similar to define a smooth functions from $\mathbb{R}^n$ into $M$!

##### _definition:_ smooth functions into a surface

For a surface $M$ with the family $x_{\alpha} : D_{\alpha} \to \mathbb{R}^3$ of proper patches indexed by $\alpha \in I$, we say a function $f : \mathbb{R}^n \to M$ is smooth if every $f_{\alpha} = x_{\alpha}^{-1} \circ f$ is smooth.

Not that $f_{\alpha}$ corresponds to the following diagram.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		f^{-1}(x_\alpha(D_\alpha)) \ar[r, "f"] \ar[rr, "f_\alpha", bend right] & x_\alpha(D_\alpha) \ar[r, "x_\alpha^{-1}"] & D_\alpha
	\end{tikzcd}
\end{document}
```
(Here we write $f^{-1}$ instead of $f^\text{pre}$ for the pre-image.)

To actually compute derivatives however, we need a [[Tangent spaces on surfaces|notion of directions on the surface]].