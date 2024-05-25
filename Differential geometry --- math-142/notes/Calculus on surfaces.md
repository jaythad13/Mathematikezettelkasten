---
tags:
- diff-geo
- math-142
lecture:
- math-142-29
- math-142-30
- math-142-36
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

For a surface $M$ with the family $x_{\alpha} : D_{\alpha} \to \mathbb{R}^3$ of proper patches indexed by $\alpha \in I$, we say a function $f : M \to \mathbb{R}$ is smooth or $f \in \mathcal{C}^\infty(M)$ if each $f_{\alpha} = f \circ x_{\alpha}$ is a smooth function $f_{\alpha} \in \mathcal{C}^\infty(D_{\alpha})$.

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

Note that these definitions of smoothness seem to depend on our choice of family of coordinate maps, but we wouldn't want them to. Do they really?

##### _proposition:_ smoothness is invariant under different patches

Say $M$ is a surface with two different families of proper patches $x_{\alpha} : D_{\alpha} \to \mathbb{R}^3$ indexed by $\alpha \in I$ and $y_{\beta} : E_{\beta} \to \mathbb{R}^3$ indexed by $\beta \in J$, with
$$
x_{\alpha}^\text{img}(D_{\alpha}) \cap y^\text{img}_{\beta}(E_{\beta}) \neq \emptyset
$$
for some $\alpha \in I$ and $\beta \in J$. We claim that
1) There exists a smooth function $h$ such that $y_{\beta} = x_{\alpha} \circ h$.
2) For any well-defined $f : M \to \mathbb{R}$, $f \circ x_{\alpha}$ is smooth for all $\alpha \in I$ if and only if $f \circ y_{\beta}$ is smooth for all $\beta \in I$.

###### _proof:_

Note that what we really want is for the following diagram to commute
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		E_\beta \ar[rrd, "y_\beta"'] \ar[dd, "h"', bend right] \\
		&& x_{\alpha}(D_{\alpha}) \cap y_{\beta}(E_{\beta}) \subset M \ar[r, "f"] \ar[llu, "y_\beta^{-1}"', bend right] \ar[lld, "x_\alpha^{-1}", bend left] & \mathbb R \\
		D_\alpha \ar[rru, "x_\alpha"] \ar[uu, "h^{-1}"', bend right]
	\end{tikzcd}
\end{document}
```

Since we have $x_{\alpha}^{-1}$, the obvious choice for $h$ is $h = x_{\alpha}^{-1} \circ y_{\beta}$. Notice that $y_{\beta} = x_{\alpha} \circ h$ and thus, $(y_{\beta})_{*} = (x_{\alpha})_{*} \circ h_{*}$. By the chain rule, since $y_{\beta}$ and $x_{\alpha}$ are smooth, so is $h$, and since $(y_{\beta})_{*}$ is one to one, (by definition), so is $h_{*}$, and thus, $h$ is regular.

Thus, $f \circ x_{\alpha}$ is smooth exactly when $f \circ y_{\beta} = (f \circ h) \circ x_{\alpha}$ is smooth.

%% see lecture notes %%

Finally, there is a natural way to define when maps between surfaces are smooth.

##### _definition:_ smooth maps between surfaces

Say $M$ and $N$ are surfaces in $\mathbb{R}^3$ with families of maps $x_{k} : D_{k} \to \mathbb{R}^3$ for $k \in I$ and $y_{l} : E_{l} \to \mathbb{R}^3$ for $l \in J$ respectively. We say $F : M \to N$ is a mapping if $F_{lk} = y_{l}^{-1} \circ F \circ x_{k}$ is smooth for all $k \in I$ and $l \in J$.

To actually compute derivatives however, we need a [[Tangent spaces on surfaces|notion of directions on the surface]], which we can finally do!

Once we have this notion, we can define

##### _definition:_ the tangent map of a map between surfaces

Say $F : M \to N$ is a mapping between surfaces. Then the tangent map $F_{*} : M  \to N$ is defined by
$$
F_{*}([\mathbf{v}, p]) = (F \circ \alpha)'(t_{0})
$$
for $[\mathbf{v}, p] = \alpha'(t_{0}) \in \mathrm{T} M$.

Finally, the notion of [[Differential forms on a surface|differential forms on a surface]] gives us a natural pullback $F^* : \Omega^k(N) \to \Omega^k(M)$.

##### _definition:_ the pullback of a smooth map between surfaces

Say $F : M \to N$ is a mapping between surfaces. Then the pullback $F^* : \Omega^k(N) \to \Omega^k(M)$ is defined by
$$
F^*(\phi) = \phi \circ (\underbrace{ F_{*}, \dots, F_{*} }_{ k \text{ times} })
$$
where $0$ times means $\phi \circ F$ and $\phi \in \Omega^k(N)$.