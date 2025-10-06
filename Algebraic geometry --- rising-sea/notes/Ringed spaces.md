---
tags:
- rising-sea/2/2
- alg-top
- alg-geo
---

Let $X$ be a topological space.

A ringed space makes even more precise the sense in which geometry is best understood by studying the functions on the geometric space. It is a space with a distinguished sheaf of rings. The prime example of a ringed space is a manifold.

##### _example:_ smooth manifolds as (locally) ringed spaces

Let $X$ be a smooth manifold. Then it is a topological space (locally homeomorphic to $\mathbb{R}^n$) with a sheaf of smooth functions $X \to \mathbb{R}$, which we call $\mathscr{O}_{X}$. In fact, we could *define* a smooth manifold as such a ringed space. We only need require that on those $U \subseteq X$ where $U \cong \mathbb{R}^n$, we have $\mathscr{O}_{X \mid U} \cong \mathscr{O}_{\mathbb{R}^n}$. Typically manifolds are also required to be [[Topology --- math-147/notes/Separation properties#_definition _ Hausdorff spaces, $T_{2}$ spaces|Hausdorff]] and [[Topology --- math-147/notes/Size restrictions#_definition _ second countable|second-countable]] — to have "reasonable" topology. Note also that the stalks $\mathscr{O}_{X, p}$ are local with a unique maximal ideal consisting of functions vanishing at $p$.

This manifold analogy carries over to morphisms as well! The smoothness of a morphism $\pi : X \to Y$ can be checked on charts, but can also be checked sheaf-theoretically. Suppose $f \mapsto \pi \circ f$ (on each open set) gives a sheaf map $\mathscr{O}_{Y} \to \pi_{*} \mathscr{O}_{X}$. Since the charts $\psi : V \to \mathbb{R}^m$ on $Y$ are products of functions $f \in \mathscr{O}_{Y}(V)$ (by the [[Calculus --- spivak/notes/Differentiability theorems#_theorem _ the projection principle holds for differentiability|projection principle]]) we have that $\psi \circ \pi : X \to \mathbb{R}^m$ is smooth, and thus, $\psi \circ \pi \circ \varphi ^{-1} : \mathbb{R}^n \to \mathbb{R}^m$ is smooth for any chart $\varphi : U \to \mathbb{R}^n$ on $X$.

The sheaf map in turn gives a stalk map $\mathscr{O}_{Y, q} \to \pi_{*} \mathscr{O}_{X, p} = \mathscr{O}_{X, p}$ by $f_{q} \mapsto (\pi \circ f)_{p}$. $\pi \circ f$ vanishes at $p$ if $f$ vanishes at $q$, we have that the stalk map sends $\mathfrak{m}_{Y, q}$ into $\mathfrak{m}_{X, p}$. Finally, this induces a map on cotangent spaces $\mathfrak{m}_{Y, q} / \mathfrak{m}_{Y, q}^{2} \to \mathscr{m}_{X, p} / \mathfrak{m}_{X, p}^{2}$. With this sheafy picture, the cotangent map is more natural than the dual tangent map since our picture is dual to the geometry.

---

##### _definition:_ ringed spaces, structure sheaf, functions, global functions

Suppose $\mathscr{O}_{X}$ is a [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf|sheaf of rings]] on $X$. Then the pair, $X, \mathscr{O}_{X}$, sometimes abbreviated to just $X$ is a **ringed space**, with $\mathscr{O}_{X}$ the **structure sheaf** on it.

[[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ presheaves, sections, restriction maps|Sections]] of $\mathscr{O}_{X}$ are called **functions** and global sections of $\mathscr{O}_{X}$ are called global functions.

---

For convenience we notate some things for ringed spaces differently than for sheaves in general. We denote the [[Algebraic geometry --- rising-sea/notes/Sheaves#_example _ restriction presheaves and sheaves|restriction]] of $\mathscr{O}_{X}$ to an open set $U \subseteq X$ by $\mathscr{O}_{U}$ instead of $\mathscr{O}_{X \mid U}$, and we denote the [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ stalks, germs|stalks, germs]] of $\mathscr{O}_{X}$ at $p \in X$ by $\mathscr{O}_{X, p}$.

$\mathscr{O}_{X}$-modules generalise the notion of a vector bundle. In particular, if $X, \mathscr{O}_{X}$ is a smooth manifold with its sheaf of smooth functions, and $\xi : E \to X$ is a vector bundle, then the smooth sections of $\xi$ form a sheaf. On each open $U \subseteq X$, we can add sections together and scale them by smooth functions in a way compatible with restriction.

##### _definition:_ $\mathscr{O}_{X}$-modules

An **$\mathscr{O}_{X}$-module** $\mathscr{F}$ is a sheaf of [[Abstract algebra --- math-171/notes/Groups, and why you should care#_definition _ abelian group, commutative group|abelian groups]] so that for each $U \subseteq X$, $\mathscr{F}(U)$ is an $\mathscr{O}_{X}(U)$-[[Commutative algebra --- math-189AA/notes/Modules#_definition _ module|module]] so that for every pair of open subsets $V \subseteq U$ the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{O}_{X}(U) \times \mathcal{F}(U) \ar[r] \ar[d, "\mathrm{res} \times \mathrm{res}"] & \mathcal{F}(V) \ar[d, "\mathrm{res}"] \\
		\mathcal{O}_{X}(V) \times \mathcal{F}(V) \ar[r] & \mathcal{F}(U)
	\end{tikzcd}
\end{document}
```

---

Note that an $\mathscr{O}_{X}$-module is not necessarily a sheaf of $A$-modules for any $A$, since the modules could be all over different rings. 

##### _example:_ sheaves of abelian groups are $\mathscr{O}_{X}$-modules

Every sheaf of abelian groups $\mathscr{F}$ is actually a $\underline{\mathbb{Z}}$-module. It may seem silly to have $\mathscr{O}_{X} = \underline{\mathbb{Z}}$ but it means that when we prove things about $\mathscr{O}_{X}$-modules, we are proving things about sheaves of abelian groups as well. As a corollary, every $\mathscr{O}_{X}$-module is a $\underline{\mathbb{Z}}$-module.

---

##### _proposition:_ stalks of $\mathscr{O}_{X}$-modules are $\mathscr{O}_{X, p}$-modules

Suppose $X, \mathscr{O}_{X}$ is a ringed space and $\mathscr{F}$ is an $\mathscr{O}_{X}$-module. Then for each point $p \in X$, the abelian group [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ stalks, germs|stalk]] $\mathscr{F}_{p}$ is an $\mathscr{O}_{X, p}$-module.

###### _proof sketch:_

The $\mathscr{O}_{X, p}$-module structure is given by $\overline{a} \, \overline{m} = \overline{a_{\mid U \cap V} m_{\mid U \cap V}}$  for $\overline{a} \in \mathscr{O}_{X, p}$ with $a \mapsto \overline{a}$ for $a \in \mathscr{O}_{X}(U)$ and $m \mapsto \overline{m}$ for $m \in \mathscr{F}(V)$.

We only show that the structure is well-defined. The fact that it is linear et c. follows from the algebraic nature of the values of the sheaves and the fact that the restriction maps respect that algebraic nature.

Suppose $\overline{a}_{1} = \overline{a}_{2}$ and $\overline{m}_{1} = \overline{m}_{2}$ with $a_{i} \in \mathscr{O}_{X}(U_{i}), m_{i} \in \mathscr{F}(V_i)$. Then there are some open $U$ and $V$ such that $a_{1 \mid U} = a_{2 \mid U}$ and $m_{1 \mid V} = m_{2 \mid V}$. Thus, $a_{1 \mid U \cap V} m_{1 \mid U \cap V} = a_{2 \mid U \cap V} m_{2 \mid U \cap V}$.

---