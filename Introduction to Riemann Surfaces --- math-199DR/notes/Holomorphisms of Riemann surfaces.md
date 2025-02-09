---
tags:
- math-199DR/6
- cx-geo
- diff-geo
---

Let $X, Y$ be Riemann surfaces with (maximal) holomorphic atlases $(\phi_{\alpha}, U_{\alpha})$ and $(\psi_{\beta}, V_{\beta})$ indexed by $\alpha \in \mathcal{I}$ and $\beta \in \mathcal{ J}$ respectively.

Now that we have the objects of our category — [[Introduction to Riemann Surfaces --- math-199DR/notes/Riemann surfaces#_definition _ (compact, connected) Riemann surface, (holomorphic) atlas, chart|Riemann surfaces]], we should try to find the right morphisms for the category. It's useful to consider what kind of properties we want the morphisms to have.

##### _desiderata:_ morphisms of Riemann surfaces

- We want the class of all Riemann surfaces to be a [[Basic category theory --- basic-cat/notes/Categories#_definition _ category|category]] — that is, each Riemann surface should have an identity morphism and the morphisms should compose associatively.
- In fact, we don't just want it to be a category — morphisms of Riemann surfaces should be functions — morphisms of the underlying sets. Categorically, we want our category to be a "concrete category".
- In fact, morphisms of Riemann surfaces, should also be [[Mathematical Analysis I --- math-131/notes/Continuity#_proposition _ $ varepsilon$-$ delta$ continuity is equivalent to topological continuity|continuous maps]] — morphisms of the underlying [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological spaces]]. Categorically, we want a "forgetful functor" to $\mathsf{\mathbb{R}^{2}Man^0}$ or $\mathsf{Top}$ (depending on whether you require a left adjoint).
- The notion of a [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ holomorphic functions|holomorphic function on a Riemann surface]] $X$ should agree with notion of a morphism of Riemann surfaces given by $X \to \mathbb{C}$.
- The notion of a [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ meromorphic|meromorphic function on a Riemann surface]] $X$ should agree with the notion of a morphism of Riemann surfaces $X \to \mathbb{C}_{\infty}$. We will see that this is really useful.
- Generally, we want morphisms $X \to Y$ to preserve the complex structures on $X$ and $Y$.
- In particular, theorems from complex analysis should have analogues for morphisms of Riemann surfaces

##### _definition:_ holomorphism

A function $\pi: X \to Y$ is holomorphic at $p \in X$ if there exist charts $(\phi, U)$ with $p \in U$ and $(\psi, V)$ with $\pi(p) \in V$ such that the composition $\psi \circ \pi \circ \phi ^{-1}$ is holomorphic at $\phi(p)$.

If $\pi$ is holomorphic at every $p \in W$ for some open $W \subseteq X$.

If $\pi$ is holomorphic on all of $X$, we say it is a holomorphism.

##### _proposition:_ Riemann surfaces form a category

$\mathsf{\mathbb{C}^1Man}$, the class of all Riemann surfaces and the holomorphisms between them, forms a category.

From this follows the natural definition of isomorphism and automorphism.

##### _proposition:_ holomorphisms are continuous

If $\pi : X \to Y$ is a holomorphism, it is a [[Mathematical Analysis I --- math-131/notes/Continuity#_proposition _ $ varepsilon$-$ delta$ continuity is equivalent to topological continuity|continuous map]] of the underlying topological spaces.

##### _definition:_ biholomorphism, isomorphism, automorphism

A biholomorphism/isomorphism of Riemann surfaces $X$ and $Y$ is a holomorphism $\pi : X \to Y$ that is a bijection with a holomorphic inverse $\pi ^{-1}$.

An isomorphism $X \to X$ is an automorphism of $X$.

##### _examples:_ dumb examples of holomorphisms

1) A [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ holomorphic functions|holomorphic function]] on $X$ is a holomorphism $X \to \mathbb{C}$.
2) The Riemann sphere $\mathbb{C}_{\infty}$ is isomorphic to the complex projective line $\mathbb{C} \mathbb{P}^1$.

### Theorems from complex analysis

We will just sketch the proofs some of the nice theorems from complex analysis that carry over.

##### _theorem:_ open mapping theorem

If $\pi : X \to Y$ is a non-constant holomorphism, $\pi$ is an open mapping.

##### _theorem:_ inverse holomorphism theorem

If $\pi : X \to Y$ is an injective holomorphism, $\pi$ has a holomorphic inverse — it is an isomorphism between $X$ and $\pi ^\text{pre}(X)$.

##### _theorem:_ identity theorem

If $\pi_{1}, \pi_{2}$ are two holomorphisms $X \to Y$, and $\pi_{1} = \pi_{2}$ on a subset $S \subseteq X$ with a limit point, then $\pi_{1} = \pi_{2}$.

##### _proposition:_ maps from compact Riemann surfaces are surjective

If $X$ is [[Mathematical Analysis I --- math-131/notes/Compactness#_definition _ compact|compact]] and $\pi : X \to Y$ is a non-constant holomorphism, then $\pi$ is surjective and $Y$ is compact.

##### _proposition:_ discreteness of pre-images

If $\pi : X \to Y$ is a non-constant holomorphism, then for each $y \in Y$, $\pi^\text{pre}(\{ y \})$ is a [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete subset]] of $X$. If $X$ and $Y$ are compact, then the pre-image is finite.

##### _proposition:_ meromorphic functions are maps to the Riemann sphere

Given a [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ meromorphic|meromorphic function]] $f : X \to \mathbb{C}$, and the stereographic projection $\phi : \mathbb{C}_{\infty} \setminus \{ \infty \} \to \mathbb{C}$, the derived map
$$
\pi(p) = \begin{cases}
\phi ^{-1}(f(p)) \in \mathbb{C} & p \text{ is not a pole} \\
\infty & p \text{ is a pole}.
\end{cases}
$$
is a holomorphism $\pi : X \to \mathbb{C}_{\infty}$.

That is, there is a bijection between meromorphic function on $X$ and holomorphisms $X \to \mathbb{C}_{\infty}$ that are not identically $\infty$.

Since $\mathbb{C}_{\infty} \cong \mathbb{C} \mathbb{P}^1$, there is a corresponding bijection to maps on $\mathbb{C}\mathbb{P}^1$ — write $f : X \to \mathbb{C}$ as the ratio $g / h$ locally, and consider $p \mapsto (g(p) : h(p))$ in projective.

##### _proposition:_ meromorphic functions on a torus $\mathbb{C} / \Lambda$ have zero total order

Any non-constant meromorphic function $f : \mathbb{C} / \Lambda \to \mathbb{C}$ has
$$
\sum_{p \in \mathbb{C} / \Lambda} \operatorname{ord}_{p} f = 0
$$


### The sheaf-theoretic view

Notice that each holomorphism $\pi : X \to Y$ induces a map going in the other direction on each open set of the [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ structure sheaf|structure sheaves]]. In particular, for each open $W \subseteq Y$ we have a $\mathbb{C}$-algebra homomorphism (a [[Abstract Algebra I --- math-171/notes/Ring homomorphisms#_definition _ ring homomorphisms|ring homomorphism]] and a [[Linear maps|linear map]])
$$
\pi^* : \mathcal{O}_{Y}(W) \to \mathcal{O}_{X}(\pi^\text{pre}(W))
$$
by $f \mapsto f \circ \pi$. This plays nicely with restriction too — it is a sheaf morphism. We will show that this completely describes holomorphisms!

##### _definition:_ sheaf morphism

A morphism of sheaves $\mathcal{F} \to \mathcal{G}$ on a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]] $X$ is the data of morphisms $\varphi_{U} = \mathcal{F}(U) \to \mathcal{G}(U)$ on each open $U \subseteq X$ that commute with restriction as follows.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(U) \ar[r, "\varphi_{U}"] \ar[d, "\mathrm{res}"] & \mathcal{G}(U) \ar[d, "\mathrm{res}"] \\
\mathcal{F}(V) \ar[r, "\varphi_{V}"] & \mathcal{G}(V)
	\end{tikzcd}
\end{document}
```

Given a continuous map $\pi : X \to Y$ and a sheaf $\mathcal{F}$ on $X$, there is a natural way to a put a sheaf on $Y$ — just give each open set on $Y$ of $\mathcal{F}$ on its pre-image under $\pi$ in $X$.

##### _definition:_ pushforward sheaf

Given a continuous map $\pi : X \to Y$ and a sheaf $\mathcal{F}$ on $X$, the pushforward sheaf on $Y$ is $\pi_{*}\mathcal{F}$ with
$$
\pi_{*} \mathcal{F}(U) = \mathcal{F}(\pi^\text{pre}(U))
$$
for each open $U \subseteq X$.

##### _definition:_ holomorphism

A continuous map $\pi : X \to Y$ is a holomorphism if the map between $f \mapsto f \circ \pi$ induces a sheaf morphism $\mathcal{O}_{Y} \to \pi_{*} \mathcal{O}_{X}$.

In fact, we don't even have to give an explicit construction for the sheaf morphism.

##### _definition:_ holomorphism

A holomorphism between $X$ and $Y$ is the data of a continuous $\pi : X \to Y$ and a morphism of sheaves of local rings $\pi^\natural : \mathcal{O}_{Y} \to \pi_{*} \mathcal{O}_{X}$ such that induced map of stalks $\pi^\sharp : \mathcal{O}_{Y, \pi(p)} \to \mathcal{O}_{X, p}$ map each [[Abstract Algebra I --- math-171/notes/Prime and maximal ideals#_definition _ maximal ideal|maximal ideal]] $\mathfrak m_{Y, \pi(p)}$ into $\mathfrak{m}_{X, p}$.