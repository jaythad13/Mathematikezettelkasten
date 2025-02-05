---
tags:
- math-196/4
- diff-geo
- complex
- cx-geo
---

Here let $X$ be a Riemann surface with an atlas consisting of charts $(U_{\alpha}, \phi_{\alpha})$ indexed by $\alpha \in \mathcal{I}$.

The raison d'etre for the complicate definition of a [[Introduction to Riemann Surfaces --- math-196/notes/Riemann surfaces#_definition _ (compact, connected) Riemann surface, (holomorphic) atlas|holomorphic atlas]], is that we want to define holomorphic functions on (open sets) of a Riemann surface. In particular, we push everything to the complex numbers and since all charts are holomorphically equivalent, we're okay.

##### _definition:_ holomorphic functions

Given an open set $W \subseteq X$. A function $f : W \to \mathbb{C}$ is holomorphic on all of $W$ if $f \circ \phi_{\alpha}^{-1}$ is a [[Complex Analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$|holomorphic]] function $\phi_{\alpha}^{\text{img}}(W \cap U_{\alpha}) \to \mathbb{C}$ for all $\alpha \in \mathcal{I}$.

The collection of all holomorphic functions on $W$ is denoted $\mathcal{O}_{X}(W)$.

For a point $p \in X$, we say a function $f$ (from a subset containing $p$) to $\mathbb{C}$ is holomorphic at $p$ if $f$ is holomorphic on an open set $W$ containing $p$.

The collection of all holomorphic functions at $p$ is denoted $\mathcal{O}_{p}$.

Naturally, we can also define singularities of functions — [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#Removable singularities|removable singularities]], [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#Poles|poles]], and [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#Essential singularities|essential singularities]] as well as [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#Meromorphic functions|meromorphic functions]]. 

##### _definition:_ meromorphic functions

A meromorphic function $f: W \to \mathbb{P}^1(\mathbb{C})$ is meromorphic on an open set $W \subseteq X$ if $\psi_{\infty} \circ f \circ \phi_{\alpha}^{-1} : \phi_{\alpha}^\text{img}(W \cap U_{\alpha}) \setminus f^\text{pre}(\infty) \to \mathbb{C}$ is a [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#Meromorphic functions|meromorphic function]] (where $\psi_{\infty}$ is the stereographic projection staying away from the pole called $\infty$).

The set of all meromorphic functions on $W$ is denoted $\mathcal{M}_{X}(W)$.

##### _definition:_ order

The order of a meromorphic $f : W \to \mathbb{P}^1(\mathbb{C})$ at $p$ is the order of the pole of $\psi_{\infty} \circ f \circ \phi_{\alpha}^{-1} : \phi_{\alpha}^\text{img}(W \cap U_{\alpha}) \setminus f^\text{pre}(\infty) \to \mathbb{C}$.

The interesting case of functions is those that are holomorphic or meromorphic on the whole surface. It's a theorem that if $X$ is compact and connected these are constants and their fraction field respectively. This leads us to distinguish the global sections —

##### _definition:_ global sections

$\mathcal{O}_{X}(X)$ is called the global section on $X$.

$\mathcal{M}_{X}(X)$ is the function field of $X$.


### Sheaves and stalks — an aside from algebraic geometry

Notice that each for each open $W \subseteq X$, the $\mathcal{O}_{X}(W)$ is a [[Abstract Algebra I --- math-171/notes/Rings#_definition _ commutative ring|commutative ring]] (in fact, it is a $\mathbb{C}$-algebra — its ring structure is compatible with its [[Linear algebra done right --- ladr/notes/Vector spaces|vector space]] structure over $\mathbb{C}$). Note, it's not an [[Abstract Algebra I --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]] since $W$ may not be connected and then we can have [[Abstract Algebra I --- math-171/notes/Rings#_definition _ zero divisor|zero divisors]].

Moreover, if we have open sets $V \subseteq W \subseteq X$, we have a map $\mathcal{O}_{X}(W) \to \mathcal{O}_{X}(V)$ that sends a function on $W$ to its restriction to $V$ (we want this to be an injection and [[Complex Analysis --- math-135/notes/Cauchy integral formula#_corollary _ unique analytic continuation|analytic continuation]] will do that for us soon). To be exact, this is a [[Functors|contravariant functor]] from the poset category on the topology of $X$ (with inclusions being the morphisms) to the category of [[Abstract Algebra I --- math-171/notes/Rings#_definition _ commutative ring|commutative rings]].

##### _definition:_ structure sheaf

$\mathcal{O}_{X}$ is the structure sheaf on $X$.

Evenmoreoverer, every open set $V$ containing $p$ has a map into the $\mathcal{O}_{p}$. This can be understood as the categorical colimit of all of the $\mathcal{O}_{X}(V)$. When $X$ is connected, this is a local ring (a commutative ring with unique maximal ideal) with maximal ideal $\mathfrak{m}_{p} = \{ f \in \mathcal{O}(p) \mid f(p) = 0 \}$.

##### _definition:_ stalk

$\mathcal{O}_{p}$ is the stalk of $\mathcal{O}_{X}$ at $p$.

Similarly, for each open $W \subseteq X$ the $\mathcal{M}_{X}(W)$ is actually a field (since dividing by a meromorphic function with a zero will still leave you a meromorphic function). This allows us to consider the order of a function at $p$.