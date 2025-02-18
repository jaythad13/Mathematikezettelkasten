---
tags:
- math-199DR/7
- cx-geo
- diff-geo
---

Let $X, Y$ be [[Mathematical Analysis I --- math-131/notes/Compactness#_definition _ compact|compact]], [[Mathematical Analysis I --- math-131/notes/Connectedness#_definition _ connectedness|connected]] Riemann surfaces with (maximal) holomorphic atlases $(\phi_{\alpha}, U_{\alpha})$ and $(\psi_{\beta}, V_{\beta})$ indexed by $\alpha \in \mathcal{I}$ and $\beta \in \mathcal{ J}$ respectively.

Holomorphisms have very nice behaviour locally. Just as the nice behaviour of holomorphic functions on the plane translates to nice topological properties like [[Complex Analysis --- math-135/notes/The argument principle and winding number#_theorem _ open mapping theorem|open mapping]], [[Complex Analysis --- math-135/notes/The argument principle and winding number#_definition _ winding number|winding number]], and [[Complex Analysis --- math-135/notes/The argument principle and winding number#_lemma _ the "$n$-to-one" lemma|non-injectivity theorems]] like the $n$-to-one lemma, so does the behaviour of holomorphisms (we've seen some of this nice behaviour [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#Theorems from complex analysis|already]]). Here, we will see that holomorphisms preserve [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological invariants of a surface|topological invariants of a surface]].

### Multiplicity

The local normal form allows us to write every holomorphic map as locally a power map. Eventually we will turn this into a global property.

##### _theorem:_ local normal form

Let $\pi : X \to Y$ be a non-constant function [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphic]] near $p \in X$. Then there exists a unique positive integer $m$ such that for all charts $\psi : V \to \mathbb{C}$ centred at $\pi(p)$ (sending $\pi(p)$ to $0$) there exists a chart $\phi : U \to \mathbb{C}$ centred at $p$ such that $\psi \circ \pi \circ \phi ^{-1}(z) = z^m$.

###### _proof sketch:_

##### _definition:_ multiplicity

Given $\pi : X \to Y$ (non-constant, holomorphic near $p \in X$) the unique $m$ of the local normal form, is called the multiplicty of $\pi$ at $p$, denoted $\operatorname{mult}_{p}\pi$.

##### _example:_ charts have multiplicity $1$

Since [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_examples _ dumb examples of holomorphisms|they are holomorphisms]] to $\mathbb{C}$ and are injective, charts have multiplicity $1$ at each point. Otherwise the $n$-to-one lemma [[Complex Analysis --- math-135/notes/The argument principle and winding number#_lemma _ the "$n$-to-one" lemma|from complex analysis]] would force them 

Using local coordinates and differentiation we can we can get the 

##### _proposition:_ calculating multiplicities



The upshot of this theorem is that the points where multiplicity is greater than $0$ are discrete.

##### _definition:_ ramification point, branch point

A point $p$ in $X$ where $\pi : X \to Y$ has multiplicity greater than $1$ are ramification points of $f$.

Their images of ramification points under $\pi$ are branch points of $\pi$.

##### _example:_ ramification points of an affine plane curve

If a smooth affine plane curve is given by the points $f(x, y) = 0$ and $\pi : (x, y) \mapsto x$, the ramificiation points are where ${ \partial f } / { \partial y } = 0$.

For a circle floating somewhere in space, the two antipodal points that intersect a line parallel to the $x$-axis have many points attracted to the same image as them.

### Degree

Now we can define and prove the constancy of the degree of a map.

##### _definition:_ degree at a point

Suppose $\pi : X \to Y$ is a (non-constant) holomorphism. For each $y \in Y$, the degree of $\pi$ at $y$ is 
$$
d_{y} \pi = \sum_{p \in \pi^\text{pre}(\{ y \})} \operatorname{mult}_{p} \pi.
$$

##### _theorem:_ degree is constant

Given $\pi : X \to Y$, the function $y \mapsto d_{y} \pi$ is constant.

##### _definition:_ degree of a map

The degree of a (non-constant) holomorphism is constant.

##### _corollary:_ isomorphism is determined by degree

If (non-constant) $\pi  : X \to Y$ has $\operatorname{deg} \pi = 1$, then $\pi$ is an [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ biholomorphism/isomorphism, automorphism|isomorphism]].

###### _proof:_

If $\pi$ has degree $1$ there can't be any branch points, so it is injective. [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ maps from compact Riemann surfaces are surjective|We've shown]] that it is surjective (since $X, Y$ are compact). [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_theorem _ inverse holomorphism theorem|Injective holomorphisms]] are isomorphisms onto their image. So we're done.

### Ramifications for meromorphic functions

All of this theory has huge *ramifications* for [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ meromorphic|meromorphic functions]] $f : X \to \mathbb{C}$ since [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ meromorphic functions are maps to the Riemann sphere|they correspond to holomorphisms to the Riemann sphere]] $\pi_{f} : X \to \mathbb{C}_{\infty}$.

##### _lemma:_ multiplicities of meromorphic functions

Given $f : X \to \mathbb{C}$ meromorphic and $\pi_{f} : X \to \mathbb{C}_{\infty}$ the corresponding holomorphism,
1) at poles, $\operatorname{mult}_{p} \pi_{f} = - \operatorname{ord}_{p} f$
2) at zeroes, $\operatorname{mult}_{p} \pi_{f} = \operatorname{ord}_{p} f$
3) everywhere else $\operatorname{mult}_{p} \pi_{f} = \operatorname{ord}_{p}(f - f(p))$

###### _proof sketch:_

I trust Noah.


### Hurwitz' formula

Hurwitz' formula allows us to relate the topology of two Riemann surfaces given the topological data of a map between them.

##### _theorem:_ Hurwitz' formula

Given (a non-constant holomorphism of compact Riemann surfaces) $\pi : X \to Y$
$$
2g_{X} - 2 = \operatorname{deg} \pi (2g_{Y} - 2) + \sum_{p \in X} (\operatorname{mult}_{p} \pi - 1).
$$

###### _proof:_

Triangulate $Y$ with vertices at branch points. Pull the triangulation back under $\pi$. Everything gets multiplied by $\operatorname{deg} \pi$ except the number of vertices which we have to correct for by adding the multiplicity term.