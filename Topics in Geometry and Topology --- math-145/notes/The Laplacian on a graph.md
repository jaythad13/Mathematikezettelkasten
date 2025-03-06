---
tags:
- math-145/7
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

### Graph Laplacian

To define a Laplacian, we need a field of functions on which it acts.

##### _definition:_ scalar fields on a graph

The [[Linear algebra done right --- ladr/notes/Vector spaces#_definition _ vector space|vector space]] of scalar fields on a graph $\mathrm{C}^0(G)$. (Note that these are actually continuous functions if you give the graph the [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete topology]]).

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

If $G$ is finite and connected, then $f$ is constant.

##### _corollary:_ the Laplacian gives (co)homology

For any finite graph $G$,
$$
\dim \ker \Delta = \mathrm{b}_{0}(G).
$$

### The Dirichlet problem

In analysis, [[Fourier Analysis --- math-139/notes/The Dirichlet problem|the Dirichlet problem]] is to find a twice-differentiable function that is harmonic on the interior of a set and satisfies a boundary condition on the boundary of a set. On graphs there isn't always a nice notion of boundary, so we just make one up.

##### _definition:_ graph with boundary

A graph with boundary is a graph with the additional data of $B(G)$, a subset of $V(G)$ called the boundary of the graph.

The interior of the graph is $I(G) = {V(G) \setminus B(G)}$.

##### _definition:_ relative Betti number

The relative Betti number is the number of components $\mathrm{b}_{0}(G, B)$ is the number of connected components of the graph that do not meet $B$.

##### _definition:_ relatively clopen

A subset $A \subseteq V(G)$ is relatively clopen if $N(A \cap I(G)) \subseteq A$.

Now we can say what the Dirichlet problem is — the Dirichlet problem on a graph with boundary $G$ and a function $g : B(G) \to \mathbb{R}$ is whether there exists a function $f \in \mathrm{C}^0(G)$ such that $f = g$ on $B(G)$ and $\Delta f = 0$ on $I(G)$.

##### _lemma:_ the Dirichlet maximum principle

Suppose $f$ is a solution to the Dirichlet problem on some graph with boundary $G$ with $\mathrm{b}_{0}(G, B) = 0$ and $g : B(G) \to \mathbb{R}$. Then $\max_{x \in V} f(x) = \max_{x \in B} g(x)$ and $\min_{x \in V} f(x) = \min_{x \in B} g(x)$.

###### _proof:_

Let $M = \max f$. If $x \in f^\text{pre}(M)$ is also in $B(G)$ we're done. However, if $x \in I(G)$, then the local maximum principle says $\overline{N^k}(x) \subseteq f^\text{pre}(M)$. Since the relative Betti number is zero, every connected component meets the boundary at say $y \in B(G)$. That is, $y \in \overline{N^k}(x) \subseteq f^\text{pre}(M)$ so there is a point in the boundary that achieves the maximum.

The proof is the same for the minimum.

We can also prove the Dirichlet maximum principle using the relative clopen lemma.

##### _lemma:_ the relative clopen lemma

The relative Betti number of a graph with boundary is $0$ if and only if every non-empty relatively clopen set meets $B$.

##### _theorem:_ unique solution to the Dirichlet problem

If a finite graph with boundary $G$ has $\mathrm{b}_{0}(G, B) = 0$, then for any $g : B \to \mathbb{R}$, the Dirichlet problem has a unique solution.

###### _proof:_

We can write the Dirichlet problem a trying to find a solution to the linear problem $Df = 0 \oplus g$ for $D : \mathrm{C}^0(G) \to \mathrm{C}^0(I) \oplus \mathrm{C}^0(B)$. The dimensions are the same on both sides (the dimensions are $\# V(G)$). Thus, we only need to show $D$ is injective. But by the Dirichlet maximum principle if $g = 0$ then $f$ has maximum and minimum $0$, and thus, is $0$.