---
tags:
- math-145/7
- math-145/8
- math-145/9
- graph
---

In analysis, [[Fourier analysis --- math-139/notes/The Dirichlet problem|the Dirichlet problem]] is to find a twice-differentiable function that is harmonic on the interior of a set and satisfies a boundary condition on the boundary of a set.

### Graphs with boundary

On graphs there isn't always a nice god-given notion of boundary, so we just choose edges ourselves and make Kronecker very unhappy.

##### _definition:_ graph with boundary

A graph with boundary is a graph with the additional data of $B(G)$, a subset of $V(G)$ called the boundary of the graph.

The interior of the graph is $I(G) = {V(G) \setminus B(G)}$.

These graphs with boundary have new "relative" notions of [[Simplicial homology and graph theory --- math-145/notes/Calculus on a graph#_definition _ zeroth Betti number on a graph|Betti number]] and [[Simplicial homology and graph theory --- math-145/notes/Calculus on a graph#_definition _ clopen|clopenness]] that treat the boundary differently.

##### _definition:_ relative Betti number

The relative Betti number is the number of components $\mathrm{b}_{0}(G, B)$ is the number of connected components of the graph that do not meet $B$.

##### _definition:_ relatively clopen

A subset $A \subseteq V(G)$ is relatively clopen if $N(A \cap I(G)) \subseteq A$.

Now we can say what the Dirichlet problem is — the Dirichlet problem on a graph with boundary $G$ and a function $g : B(G) \to \mathbb{R}$ is whether there exists a function $f \in \mathrm{C}^0(G)$ such that $f = g$ on $B(G)$ and $\Delta f = 0$ on $I(G)$.

### Solving the Dirichlet problem

##### _lemma:_ the Dirichlet maximum principle

Suppose $f$ is a solution to the Dirichlet problem on some graph with boundary $G$ with $\mathrm{b}_{0}(G, B) = 0$ and $g : B(G) \to \mathbb{R}$. Then $\max_{x \in V} f(x) = \max_{x \in B} g(x)$ and $\min_{x \in V} f(x) = \min_{x \in B} g(x)$.

###### _proof:_

Let $M = \max f$. If $x \in f^\text{pre}(M)$ is also in $B(G)$ we're done. However, if $x \in I(G)$, then the local maximum principle says $\overline{N^k}(x) \subseteq f^\text{pre}(M)$. Since the relative Betti number is zero, every connected component meets the boundary at say $y \in B(G)$. That is, $y \in \overline{N^k}(x) \subseteq f^\text{pre}(M)$ so there is a point in the boundary that achieves the maximum.

The proof is the same for the minimum.

We can also prove the Dirichlet maximum principle using the relative clopen lemma.

##### _lemma:_ the relative clopen lemma

The relative Betti number of a graph with boundary is $0$ if and only if every non-empty relatively clopen set meets $B$.

##### _theorem:_ the Dirichlet problem has a unique solution

If a finite graph with boundary $G$ has $\mathrm{b}_{0}(G, B) = 0$, then for any $g : B \to \mathbb{R}$, the Dirichlet problem has a unique solution.

###### _proof:_

We can write the Dirichlet problem a trying to find a solution to the linear problem $Df = 0 \oplus g$ for $D : \mathrm{C}^0(G) \to \mathrm{C}^0(I) \oplus \mathrm{C}^0(B)$. The dimensions are the same on both sides (the dimensions are $\# V(G)$). Thus, we only need to show $D$ is injective. But by the Dirichlet maximum principle if $g = 0$ then $f$ has maximum and minimum $0$, and thus, is $0$.

### The weighted Dirichlet problem

We can make this problem worse by adding weights. This helps solve problems like "what are the potentials at each point of this horrible electrical network?" where your weights on edges are conductances and voltage at each node is a scalar field so gradients scaled by the weights give the current across each edge.

Given $G$, a graph with boundary, $c_{E} : E(G) \to \mathbb{R}$ a strictly positive weight function on the edges, $c_{V} : V(G) \to \mathbb{R}$ the corresponding weight on vertices by
$$
c_{V}(x) = \sum_{y \in N(x)} c_{E}(xy)
$$the weighted Laplacian, $\Delta_{c} : \Omega^0(G) \to \Omega^0(G)$ given by
$$
\Delta_{c} = f(x) - \frac{\sum_{y \in N(x)} f(y) c_{E}(xy)}{c_{V}(x)}
$$
and the boundary value $g : B(G) \to \mathbb{R}$.

##### _theorem:_ the weighted Dirichlet problem has a unique solution

If a finite graph with boundary $G$ has $\mathrm{b}_{0}(G, B) = 0$, then for any $g : B(G) \to \mathbb{R}$, and any weight function $c_{V}$ the weighted Dirichlet problem has a unique solution.

###### _proof:_
can be done just as for the regular Dirichlet problem since the maximum principle still holds.

However, this lends itself to defining the same useful tools of differential operators and inner products as we did [[Topics in Geometry and Topology --- math-145/notes/Calculus on a graph#Differential operators on a graph|without weights]].

##### _definition:_ weighted gradient, weighted divergence, weighted inner products


### Energy minimisation

We can rethink the weighted Dirichlet problem as an energy (really, power) minimisation problem in the special case where the boundary is a two point set $B(G) = \{ a, b \}$ with input $a$ and output $b$. Notice that the weighted inner product of currents (vector fields) gives rise to a norm on current fields. This norm corresponds to the power of the current on each edge — $\left< \phi, \phi \right>/c$ has units of $\mathrm{A}^{2} \, \mathrm{\Omega}$.

As usual, we are still seeking a scalar field $f \in \Omega^0(G)$ so that $\Delta f = 0$ on the interior of $G$ and $f = g$ on the boundary $B(G)$. It turns out if we consider all $q \in \Omega^0(G)$ such that $q = g$ on the boundary, then the solution to the Dirichlet problem is the unique solution with $\nabla f$ having minimum power. Moreover, the power is the input power $f(a) \sum_{y \in N(a)} \nabla f(y)$.

##### _theorem:_ the solution to the Dirichlet problem minimises energy

###### _proof:_

Let $f$ be the solution and $q$ be any other function satisfying the boundary condition. We can write
$$
\begin{align}
\lVert \nabla q \rVert_{E} ^{2} & = \left< \nabla f + \nabla(q - f), \nabla f + \nabla (q - f) \right>_{E}  \\
 & = \lVert \nabla f \rVert_{E} ^{2} + \lVert \nabla (q - f) \rVert_{E} ^{2} + 2 \left< \nabla f, \nabla (q  - f) \right>_{E}.
\end{align}
$$

Using the weighted adjoint theorem we have
$$
\left< \nabla f, \nabla (q - f) \right>_{E} = \left< \Delta f, (q - f) \right>_{E} = 0
$$
since $\Delta f = 0$ on the interior and $q - f = 0$ on the boundary. Thus,
$$
\lVert \nabla q \rVert^{2}_{E} = \lVert \nabla f \rVert^{2}_{E} + \lVert \nabla(q - f) \rVert_{E}^{2} \ge \lVert \nabla f \rVert^{2}_{E}.
$$
Equality is only when $\lVert \nabla(q - f) \rVert^{2}_{E} = 0$ which forces $\nabla(q - f) = 0$.

Further
$$
\begin{align}
\lVert \nabla f \rVert^{2}_{E} & = \left< \nabla f, \nabla f \right>_{E}  \\
 & = \left< \Delta f, f \right>_{V} \\
 & = \Delta f(a) f(a) c_{V}(a) + \Delta f(b) f(b) c_{V}(b).
\end{align}
$$
Assuming without loss of generality that $f(b) = 0$ which gives the desired result.

##### _corollary:_ the effective resistance of the solution to the Dirichlet problem

##### _theorem:_ the current solution to the Dirichlet problem minimises energy