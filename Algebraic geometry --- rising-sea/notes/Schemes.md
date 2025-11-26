---
tags:
- alg-geo
- rising-sea/4
---

### Motivation from smooth geometry

Shemes comprise a set of points, a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topology]] on them, and a structure [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf, separated presheaf|sheaf]] (of rings) defining the algebraic functions, and thus, the geometric structure of the scheme. In short, they are [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, functions, global functions|ringed spaces]] (with some additional properties). This idea generalises from smooth manifolds in the following sense.

![[Algebraic geometry --- rising-sea/notes/Ringed spaces#_example _ smooth manifolds as (local) ringed spaces|Ringed spaces]]

A scheme is similarly defined to be a topological space with a structure sheaf. Here, instead of a local "isomorphism of ringed spaces" to $\mathbb{R}^n$, we have a local isomorphism to an [[Algebraic geometry --- rising-sea/notes/Affine schemes|affine scheme]] (possibly different affines near different points). Finally, separatedness will be the analogue of "reasonable" topology, though we won't require it for a scheme to be a scheme. (Previously a non-separated scheme might be called a prescheme, like a non-Hausdorff manifold is called a premanifold) 

Sheaf morphisms will be similarly defined as a pair of $\pi : X \to Y$ and $\mathscr{O}_{Y} \to \pi_{*} \mathscr{O}_{X}$ so that the stalk map preserves the maximal ideal. Also, the cotangent space is *defined* as $\mathfrak{m}_{X, p} / \mathfrak{m}_{X, p}^{2}$ as the tangent space is *defined* as its dual.

### Schemes

A curious fact about more complicated definitions is that we will be able to (and will need to) define isomorphisms in our category of schemes before we can define morphisms.

##### _definition:_ scheme, Zariski topology, isomorphism of schemes, functions

A **scheme** is a [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, functions, global functions|ringed space]] $X, \mathscr{O}_{X}$ such that each point $p \in X$ has an open neighbourhood $U$ such that the ringed space $U, \mathscr{O}_{X \mid U}$ is (isomorphic to, as a ringed space) an [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition _ affine scheme|affine scheme]].

The topology on the scheme is called the **Zariski topology**.

An **isomorphism of schemes** is an isomorphism of ringed spaces.

Just as with ringed spaces in general, we refer to sections $f \in \mathscr{O}_{X}(U)$ as **functions** on $U$, and **global functions** when $U = X$.

---

Note that it is not part of the definition of schemes that the intersection of two affine open subsets is affine.

We can "recognise" affine schemes $X = \operatorname{Spec} A$. For example, the global sections of $\operatorname{Spec} A$ are just $A$ localised away from the unit $1$, and thus, $\mathscr{O}_{X}(X) \cong A$. We claim that this goes even further. Knowing that [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_proposition _ isomorphisms of affine schemes are isomorphisms of rings|isomorphisms of affine schemes are isomorphisms of rings]] gives us an isomorphism $\operatorname{Spec} \mathscr{O}_{X}(X) \cong \operatorname{Spec} A$.

This allows us to show in fact that distinguished opens $D(f)$ are just $\operatorname{Spec} A_{f}$, and then more generally, that any open subset of a scheme is itself a scheme.

##### _proposition, definition:_ open subschemes, affine open subscheme

For any open $U \subseteq X$, the restriction $U, \mathscr{O}_{X \mid U}$ is a scheme. 

We say it is an **open subscheme** of $X$. If it is an affine scheme, then we say it is an **affine open (subscheme)**.

###### _proof:_

Suppose $p \in U$ has affine open neighbourhood $\operatorname{Spec} A \subseteq X$. Then $U \cap \operatorname{Spec} A$ is open in $\operatorname{Spec} A$. Thus, it is covered by the base of [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_definition _ distinguished open set, doesn't vanish set|distinguished opens]]. That is, we have $p \in D(f) \subseteq \operatorname{Spec} A$. Since $D(f), \mathscr{O}_{\operatorname{Spec} A \mid D(f)}$ [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_example _ inclusions of distinguished opens as schemes|is isomorphic]] to an affine scheme $\operatorname{Spec} A_{f}$, we have found an affine open neighbourhood of $p$.

---

The most general form of this is that the affine opens are actually pretty much all the open sets we need to care about.

##### _proposition:_ affine opens form a base

The affine opens of a scheme form a base for the Zariski topology on the scheme.

###### _proof sketch:_

Every scheme $X$ has a cover by affine opens. Every open subset of $X$ is the union of its intersections with these affine opens. Each of these intersections is open in the affine open, and thus can be covered by the base of distinguished opens. Since each of the distinguished opens is an affine open, we have written the open subset as a union of affine opens.

---

### Stalks of schemes

The stalks of the structure sheaf are interesting algebraically. In fact, they are all local rings! This is nice, because it allows us to use the theory of local ringed spaces for schemes.

![[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ local ringed spaces, residue fields|Ringed spaces]]

##### _proposition:_ schemes are local-ringed

A scheme is a local-ringed space.

###### _proof:_

For any $p \in X$, choose some affine open neighbourhood $\operatorname{Spec} A \ni \mathfrak{p} = p$. Thus, the stalk at $p$ is $\mathscr{O}_{X, p} \cong \mathscr{O}_{X \mid \operatorname{Spec} A, \mathfrak{p}} = A_{\mathfrak{p}}$.

---

Values and vanishing of functions are then what they are for functions on local ringed spaces.

![[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ values of functions, vanishing|Ringed spaces]]

Note that this is actually the same as our [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition _ (global) functions on an affine scheme, value, vanishing at a point|earlier definition of the value]] of $f \in A$ at $\mathfrak{p} \in \operatorname{Spec} A$ as $f + \mathfrak{p} \in A / \mathfrak{p}$. Since [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_proposition _ localisation commutes with quotients|localisation commutes with quotients]], the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		A \ar[r] \ar[d] & A_{\mathfrak{p}} \ar[d] \\
		A / \mathfrak{p} \ar[r] & A_{\mathfrak{p}} / \mathfrak{p} A_{\mathfrak{p}} = Q(A / \mathfrak{p}) \ar[r, equals] & \kappa(\mathfrak{p})
	\end{tikzcd}
\end{document}
```
The value of $f$ as a function on the local ringed space $\operatorname{Spec} A$ is its image under $A \to A_{\mathfrak{p}} \to \kappa(\mathfrak{p})$. This is the same as its image under $A \to A / \mathfrak{p} \to \kappa(\mathfrak{p})$. Since $A / \mathfrak{p} \to Q(A / \mathfrak{p})$ is an injection, we can just think of this as the same as its image under $A \to A / \mathfrak{p}$.

##### _example:_ value of a function on an affine scheme

On $\operatorname{Spec} A = \mathbb{A}_{\mathbb{C}}^{2}$ the "rational function" $f = (x^{2} + y^{2}) / x (y^{2} - x^5)$ is a function away from the $y$-axis and the curve $y^{2} - x^5$. At $\mathfrak{p} = (x - 2, y - 4)$ we have $A / \mathfrak{p} = \mathbb{C}$ and thus, $\kappa(\mathfrak{p}) = A / \mathfrak{p} = \mathbb{C}$. In both, $A / \mathfrak{p}$ and $\kappa(\mathfrak{p})$, we have 
$$
f(\mathfrak{p}) = \frac{2^{2} + 4^{2}}{2(4^{2} - 2^5)} =  - 5 / 8.
$$

Its value at $\mathfrak{q} = (y)$, the [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition _ generic point|generic point]] of the $x$-axis is $x^{2} / (- x^6) = -1 / x^4$ in the ring $(\mathbb{C}[x, y] / (y))_{(y)} = \mathbb{C}(x)$.

This is one reason to care about fields that aren't algebraically closed — even though $\mathbb{C}$ is, residue fields (of schemes over it) like $\mathbb{C}(x)$ are not.

---

### Gluing schemes

Using [[Topology --- math-147/notes/Quotient and identification spaces#_definition _ identification space|identification spaces]] from topology, we can glue together affine schemes into a topological space locally homeomorphic to affine schemes. Then by [[Algebraic geometry --- rising-sea/notes/Gluing sheaves#_proposition, definition _ sheaves glue, cocycle condition|gluing structure sheaves]] we get a scheme.

##### _proposition:_ gluing schemes

Given a collection of schemes $\{ X_{i} \}_{i \in \mathscr{I}}$, open subschemes $X_{ij} \subseteq X_{i}$ with $X_{ii} = X_{i}$, isomorphisms $f_{ij} : X_{ij} \to X_{ji}$ with $f_{ii}$ the identity obeying the cocycle condition. Let $\sim$ denote the equivalence relation on $\bigsqcup X_{i}$ by $x_{i} \sim x_{j}$ if $f_{ij}(x_{i}) = x_{j}$. Then there is a scheme $X$ with [[Topology --- math-147/notes/Quotient and identification spaces#_definition _ quotient topology, quotient space, quotient map|the topology of]] $\bigsqcup X_{i} / \sim$ and each $X_{i}$ an open subscheme.

---

Note that the cocycle condition is necessary for $\sim$ to define an equivalence relation on the disjoint union of topological spaces.