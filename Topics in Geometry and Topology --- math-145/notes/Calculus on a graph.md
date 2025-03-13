---
tags:
- math-145/7
- math-145/8
- graph
---

In analysis, the Laplacian is a linear differential operator 
$$
\Delta : f \mapsto \frac{ \partial^{2} f }{ \partial x_{1}^{2} } + \dots + \frac{ \partial^{2} f }{ \partial x_{n}^{2} } 
$$
(for $f : \mathbb{R}^n \to \mathbb{R}$) that has applications to heat flow and wave propagation. It characterises the curvature of the graph of the function at a point.

We can define a similar operator for functions on a graph that has applications to random walks and electrical networks.

### Basic notions on graphs

Recall the notion of a simple graph.

![[Superdiscrete --- math-55A/notes/Basic graph theory#_definition _ graph|Basic graph theory]]

Let $G$ be such a simple graph.

We want to have a notion of neighbours of a vertex $x$.

##### _definition:_ neighbour set, neighbourhood, $k$th degree neighbours

The set of all vertices of $G$ [[Superdiscrete --- math-55A/notes/Basic graph theory#_definition _ adjacent|adjacent]] to $x$ is the neighbour set of $x$, denoted $N(x)$.

The neighbourhood of $x$ is $\overline{N}(x)$.

For any subset $A$ of the vertices, $N(A) = \bigcup_{x \in A} {N}(A)$ and similarly $\overline{N}(A) = \bigcup_{x \in A} \overline{N}(A)$.

Often it makes sense to iteratively consider $\overline{N}(\overline{N}(\dots \overline{N}(A)))$. Thus, we define $\overline{N^k}(A)$ inductively —
$$
\overline{N^k}(A) = \begin{cases}
A & k = 0 \\
\overline{N}(\overline{N^k}(A)) & k > 0.
\end{cases}
$$
We call $\overline{N^k}(A)$ the $k$th degree neighbours of $A$.

We won't just consider finite vertex sets, instead we'll allow ourselves to consider locally finite graphs —

##### _definition:_ locally finite graph

$G$ is locally finite if every neighbourhood $N(x)$ is finite.

Recall also the notion of a path on a graph —

![[Superdiscrete --- math-55A/notes/Basic graph theory#_definition _ walk|Graph colouring]]

![[Superdiscrete --- math-55A/notes/Basic graph theory#_definition _ path|Basic graph theory]]

Note that a $1$-[[Topics in Geometry and Topology --- math-145/notes/Chains revisited#_definition _ $0$, $1$, and $2$-chains|chain]] is just a collection of paths in the graph on $U \subseteq \mathbb{R}^{2}$ with all points vertices, and an edge between two vertices if the line segment between them is contained in $U$.

Notice also that $x \sim y$ if there is a path between $x$ and $y$, is an equivalence relation on the vertices of the graph.

##### _definition:_ connected component

Each equivalence class under the "path between" equivalence relation is a connected component of the graph.

##### _definition:_ zeroth Betti number on a graph

The zeroth Betti number of $G$ is the number of connected components of the graph, denoted $\mathrm{b}_{0}(G)$.

##### _definition:_ clopen

A subset $A \subseteq V(G)$ is called clopen if $\overline{N}(A) = A$, or equivalently $N(A) \subseteq A$.

##### _lemma:_ the clopen lemma

A subset $A \subseteq V(G)$ is clopen if and only if it is the union of connected components.

### The Laplacian on a graph

To define a Laplacian, we need a field of functions on which it acts.

##### _definition:_ scalar fields on a graph

The [[Linear algebra done right --- ladr/notes/Vector spaces#_definition _ vector space|vector space]] of scalar fields on a graph $\mathrm{C}^0(G)$. (Note that these are actually continuous functions if you give the graph the [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete topology]]). Suggestively, we also denote these $\Omega^0(G)$

##### _definition:_ graph Laplacian

The graph Laplacian is a linear operator $\mathrm{C}^0(G) \to \mathrm{C}^0(G)$ that gives the difference between $f(x)$ and the average of $f$ on its neighbours.
$$
(\Delta f)(x) = f(x) - \frac{\sum_{y \in N(x)} f(y)}{\lvert N(x) \rvert }
$$

The Laplacian is not just a linear operator on $\mathrm{C}^0(G)$ — it's a linear expression in $f(x), f(x_{1}), \dots, f(x_{n})$ for $N(x) = \{ x_{1}, \dots, x_{n} \}$. Since this is finite-dimensional, we can write it as the obvious matrix in these values.

Of special interest are the functions where the Laplacian is identically $0$.

##### _definition:_ harmonic function

$f \in \mathrm{C}^0(G)$ is harmonic if $\Delta f(x) = 0$ at all $x \in V(G)$.

On finite graphs, these are actually quite uninteresting. With a fairly obvious lemma, we can show that all harmonic functions are locally constant.

##### _lemma:_ local maximum principle

For a finite graph $G$ and a function $f \in \mathrm{C}^0(G)$, if $M$ is $\max_{x \in V(G)} f(x)$. If $f(x) = M$ and $\Delta f(x) \le 0$, then $f(y) = M$ for all $y \in N(x)$.

##### _theorem:_ harmonic functions on finite graphs are locally constant

If $G$ is finite and connected, then any harmonic function $f : G \to \mathbb{R}$ is constant.

##### _corollary:_ the Laplacian gives (co)homology

For any finite graph $G$,
$$
\dim \ker \Delta = \mathrm{b}_{0}(G).
$$

### Differential operators on a graph

We can write the Laplacian from analysis

To have analogous "differential" operators we need a notion of a vector field on a graph.

##### _definition:_ vector fields on a graph

A vector field on a graph is an antisymmetric function $\phi : E^\star(G) \to \mathbb{R}$ where $E^\star(G)$ is the set of ordered edges — $E^\star(G) = \{ (x, y) \in V \times V \mid \{ x, y \} \in E(G) \}$.

We denote the vector space of all vector fields on a graph by $\Omega^1(G)$.

The gradient of a scalar field is the obvious thing — it measures the change across the edge

##### _definition:_ gradient

Given a function $f \in \Omega^0(G)$, its gradient is the vector field $\nabla f$ given by
$$
\nabla f(x, y) = f(y) - f(x).
$$

The divergence of a vector field is also the obvious thing it should be — the average flow at a vertex (with the convention that outflow is positive).

##### _definition:_ divergence

Given a vector field $\phi \in \Omega^1(G)$, its gradient is the scalar field $\nabla \cdot \phi$ given by
$$
\nabla \cdot \phi(x) = \frac{\sum_{y \in N(x)} \phi(x, y)}{\lvert N(x) \rvert }.
$$

##### _proposition:_ the Laplacian is the divergence of the gradient

Given a scalar field $f \in \Omega^0(G)$,
$$
\Delta f = - \nabla \cdot \nabla f.
$$

###### _proof:_

Just compute —
$$
\begin{align}
\nabla \cdot \nabla f(x) & = \frac{\sum_{y \in N(x)} \nabla f(x, y)}{\lvert N(x) \rvert } \\
 & = \frac{- \sum_{y \in N(x)} f(x) + \sum_{y \in N(x)} f(y)}{\lvert N(x) \rvert } \\
 & = - \frac{\lvert N(x) \rvert }{\lvert N(x) \rvert } f(x) + \frac{\sum_{y \in N(x)} f(y)}{\lvert N(x) \rvert } \\
 & = - \Delta f(x).
\end{align}
$$

It turns out this is indicative of deeper structure — gradient and divergence are adjoint operators (given the correct [[Inner product spaces|inner products]] on $\Omega^0$ and $\Omega^1$).

##### _definition:_ the inner product on scalar fields

Given $f, g \in \Omega^0(G)$, their inner product is the sum of products of the function at each vertex weighted by the number of neighbours at the vertex —
$$
\left< f, g \right> _{V} = \sum_{x \in V(G)} f(x) g(x) \lvert N(x) \rvert  
$$

##### _definition:_ the inner product on vector fields

Given $\phi, \psi \in \Omega^1(G)$, their inner product is the sum of products of the fields at each edge —
$$
\left< \phi, \psi \right> _{E} = \sum_{xy \in E(G)} \phi(x, y) \psi(x, y) = \frac{1}{2} \sum_{x \in V(G)} \sum_{y \in N(x)} \phi(x, y) \psi(x, y)
$$

Notice that in the first formula, each $xy \in E(G)$ only appears once as either $(x, y)$ or $(y, x)$. It doesn't matter which since we switch the order in both antisymmetric functions simultaneously. The equivalent second formula follows from the [[Superdiscrete --- math-55A/notes/Basic graph theory#_proposition _ the handshake lemma|the handshake lemma]].

Both of these inner products do indeed satisfy the requirements to be an inner product on the respective (real) vector spaces, and induce corresponding norms $\lVert \rVert_{V}$ and $\lVert  \rVert_{E}$. Note also that they only make sense for finite graphs $G$.

By computing examples, we can conjecture a theorem —

##### _theorem:_ (negative) divergence and gradient are adjoint

The gradient linear map $f \mapsto \nabla f$ and the negative divergence $\phi \mapsto - \nabla \cdot \phi$ are [[Linear algebra done right --- ladr/notes/Adjoints#_definition _ adjoint, $T *$|adjoint linear maps]].

###### _proof:_

$$
\begin{align}
\left< f, - \nabla \cdot \phi \right>_{V} & = \sum_{x \in V} f(x) (-\nabla \cdot \phi)(x) \lvert N(x) \rvert  \\
 & = \sum_{x \in V} \left( f(x) \sum_{y \in N(x)} - \phi(x, y) \right) \\
 & = \sum_{(x, y) \in E^\star} f(x) \phi(x, y)
\end{align}
$$
$$
\begin{align}
\left< \nabla f, \phi \right>_{E} & = \sum_{xy \in E} \nabla f(x, y) \phi(x, y)  \\
 &  = \sum_{xy \in E} ((f(y) - f(x)) \phi(x, y)) \\
 & = - \frac{1}{2} \sum_{(x, y) \in E^\star} f(y) \phi(y, x) - \frac{1}{2} \sum_{(x, y) \in E^\star} f(x) \phi(x, y) \\
 & = \sum_{(x, y) \in E^\star} f(x) \phi(x, y)
\end{align}
$$

This leads to a new, much nicer proof of the harder direction of the result harmonic functions are exactly constant functions.

##### _proposition:_ harmonic functions on finite graphs are locally constant

If $G$ is finite and connected, then any harmonic function $f : G \to \mathbb{R}$ is constant.

###### _proof sketch:_

$f$ harmonic implies
$$
0 = \Delta f = \left< \Delta f, f \right>_{E} = \left< -\nabla \cdot \nabla f, f \right>  = \left< \nabla f, \nabla f \right>_{V} = \lVert \nabla f \rVert_{V}^{2}.
$$
and

The other direction is obvious just as previously.