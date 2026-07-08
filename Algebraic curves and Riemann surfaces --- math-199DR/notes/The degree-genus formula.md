---
tags:
- uc-2026/enum-geo/2
- alg-geo
- cx-geo
- sidhant-raman
---

We have a way to relate the genus to the degree of a projective curve. 

##### _theorem:_ degree-genus formula

Let $X$ be a genus $g$ degree $d$ plane projective curve. Then
$$
g = \frac{(d - 1)(d - 2)}{2}.
$$

---

But why is the genus of each degree $d$ curve the same?

### Moduli of degree $d$ hypersurfaces

##### _definition:_ the parameter space of degree $d$ hypersurfaces

Let $V_{d, n} = \mathbb{C}[x_{0}, \dots, x_{n}]$ be the $\binom{n + d}{d}$-dimensional (by [[Superdiscrete --- math-55A/notes/Multisets#_theorem _ the multichoose theorem|stars and bars]]) vector space of degree $d$ homogeneous polynomials in $n + 1$ variables. Then the **parameter space of degree $d$ hypersurfaces** is $\mathbb{P} V_{d, n} =  \mathbb{C} \mathbb{P}^{\binom{d + n}{d} - 1}$.

---

This is a moduli space! It's structure is genuinely related to the hypersurfaces it parametrises. We use the following result without proof

##### _theorem:_ Riemann's

The locus of singular hypersurfaces $\partial \mathscr{H}_{d, n} \subseteq \mathbb{P}V_{d, n}$ is a closed (codimension $1$) subvariety, corresponding to the vanishing of the resultant.

---

##### _definition:_ the parameter space of smooth degree $d$ hypersurfaces

The **parameter space of smooth hypersurfaces** is $\mathscr{H}_{d, n} = \mathbb{P} V_{d, n} \setminus \partial \mathscr{H}_{d, n}$ . 

We define the **universal family of hypersurfaces** to be $\mathscr{U}_{d, n} = \{ (X, p) \in \mathscr{H}_{d, n} \times \mathbb{C} \mathbb{P}^n \mid p \in X \subseteq \mathbb{C} \mathbb{P}^n \}$ with its projection $\pi : \mathscr{U}_{d, n} \to \mathscr{H}_{d, n}$.

---

Note that the fibre above each $X \in \mathscr{H}_{d, n}$ is the hypersurface $X$.

##### _proposition:_ the universal family is a fibre bundle with homeomorphic fibres

The projection $\pi : \mathscr{U}_{d, n} \to \mathscr{H}_{d, n}$ is proper and a **submersion** (induces a surjection of tangent spaces at each point). Thus, by Ehresmann's theorem, it is a fibre bundle. In particular, since $\mathscr{H}_{d, n}$ is [[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ path-connected|path-connected]], it is a fibre bundle with homeomorphic fibres.

###### _proof sketch:_

Each compact subset of $\mathscr{H}_{d, n}$ is closed and has closed pre-image. But then closed subsets of a closed subset of $\mathbb{P}^N \times \mathbb{P}^n$ are compact. Thus, $\pi$ is proper.

To show $\pi$ is a submersion is just a calculation — it's clear that projections are always submersions.

---

### A proof by degenerations

We can understand smooth spaces using spaces that are as far away from smooth as possible.

![[#_theorem _ degree-genus formula]]

###### _proof:_

By the arguments given previously, it suffices to show that there is one smooth degree $d$ curve of genus $g = (d - 1)(d - 2) / 2$.

The worst degree $d$ curve is $d$ lines — the union of $d$ copies of $\mathbb{C} \mathbb{P}^1$ in $\mathbb{C} \mathbb{P}^{2}$. If these are defined by $d$ homogeneous polynomials $f_{1}, \dots, f_{d}$ then the union is just the vanishing set $V(f)$ of their product $f = f_{1} \cdots f_{d}$. 

We know that $V(f) \in \partial \mathscr{H}_{d, 2}$. Since $\partial \mathscr{H}_{d, 2}$ is closed, a generic perturbation $V(f_{\varepsilon})$ of coefficients is actually smooth. Euclidean-locally, $V(f) \cong V(zw) \cong V(z^{2} + w^{2}) \subseteq \mathbb{C}^{2}$ which is just the cone. However, the local model of the smooth perturbation $V(f_{\varepsilon})$ is a hyperbola $V(z^{2} + w^{2} - \varepsilon)$ is a hyperbola. Thus, $V(f_{\varepsilon})$ comes just from replacing each node at the intersection of two $\mathbb{C} \mathbb{P}^1$s with a tube. We show that $g_{V(f_{\varepsilon})}$ is the correct number.

Now we have a connect sum of $\mathbb{C} \mathbb{P}^1$s. There are $\binom{d}{2}$ intersections, but the chain of $d - 1$ in a row doesn't change genus. Thus, $g = \binom{d}{2} - (d - 1) = \frac{(d - 1)(d - 2)}{2}$.

---