---
tags:
- vsrp
- subhajit-goswami
- prob
---

Percolation theory is about studying properties of random graphs — subgraphs of a given graph $G$ where each edge in $G$ has a probability of being included in the subgraph. For example, we could consider the square lattice $\mathbb{Z}^{2}$ or the infinite binary tree.

##### _definition:_ (Bernoulli, bond) percolation on a graph, percolation configuration

Given a (connected) graph $G$, a (Bernoulli, bond) percolation (with parameter $p$) on $G$ is a random subgraph (or a probability distribution on all subgraphs) $H \subseteq G$ where every vertex is included in $H$ and each edge is included in $H$ with fixed probability $p \in [0, 1]$.

We say an edge in $G$ is open if it is included in $H$ and closed otherwise (imagine water flowing through pipes corresponding to the edges).

We could also do the same thing with including vertices.

We can also encode these subgraphs by random functions $\omega : E(G) \to \{ 0, 1 \}$ or $V(G) \to \{ 0, 1 \}$ respectively, called percolation configurations.

The probability measure on the space of percolation configurations can be given explicitly as a product measure (whatever that means) but it isn't strictly relevant.

Percolation theory is then about looking at how connectivity properties vary on this probability measure space.

### Connectivity questions

Recall that a connected graph $G$ is naturally a [[Mathematical Analysis I --- math-131/notes/Metric spaces#_definition_ metric space, metric|metric space]] with the shortest path distance between any two vertices. This allows us to use the notation $B(n, x)$ to represent the ball of points of distance less than $n$ from $x \in V(G)$ and $\partial B(n, x)$ to represent the balls at distance exactly $n$.

The first idea is to look at the probability that a fixed $x \in V(G)$ is connected to infinity. We approximate this by the one-arm probability. We do this because the measure space is uncountable and so we can't sum over everything directly, and instead we do this summing over the finite ball.

##### _definition:_ one-arm probability

The one arm probability is the probability 
$$
\theta(n, x, p) = \mathbb{P}(x \leftrightarrow  \partial B(n, x)).
$$

Note that this is decreasing in $n$ since connectivity to $\partial B(n + 1, x)$ implies connectivity to $\partial B(n, x)$ but not the other way round. Thus, $\theta(n, x, p)$ is a monotone sequence in $n$, bounded below by $0$. [[Mathematical Analysis I --- math-131/notes/Sequences and convergence#_proposition _ monotonic sequences blow up or converge|Thus, it converges]] as $n \to \infty$.  We call the value of the convergent sequence $\theta(\infty, x, p)$. We're interested in whether this is positive, since that tells us whether there is a positive probability of an infinite connected component.

Note that this doesn't depend on the choice of $x$ — since $G$ is connected, there is positive probability that the path between $x$ and any other vertex $y$ is completely open. Thus, we just write $\theta(p)$ for $\theta(\infty, x, p)$.

### Increasing functions

Note that we have a poset structure on our space of functions. 

##### _definition:_ percolation configuration poset

The percolation configuration poset is given by $\omega_{1} \le \omega_{2}$ if the corresponding subgraphs satisfy $H_{1} \subseteq H_{2}$. 

This gives us a notion of increasing functions — just increasing functions on the poset.

##### _example:_ infinite path indicator function
 
The infinite path indicator function $\mathbf{1}_{0 \leftrightarrow \infty}$ which returns $1$ for configurations with an infinite path and $0$ otherwise.

This is particularly interesting because it allows us to change perspective from generating new subgraphs every time, to looking at an assignment $\lambda : E(G) \to [0, 1]$ and removing an edge $e \in E(G)$ if $\lambda(e) > p$. Then we are looking at a chain in the percolation poset.

To do this formally, we use the notion of a coupling from probability, but that is just technical.

### The critical parameter

Since $\theta(p)$ is increasing in $p$, with $\theta(0) = 0$ and $\theta(1)$, we want to figure out what it's behaviour looks like. Is it positive almost everywhere, $0$ almost everywhere, or $0$ up to a point and then positive? This is encoded by the critical parameter.

##### _definition:_ critical parameter

The critical parameter of a graph is
$$
p_{c} = \sup \{ p \mid \theta(p) = 0 \}.
$$

##### _example:_ critical parameter on the line

The critical parameter on $\mathbb{Z}$ is $1$ since there is always some disconnection from infinity unless all edges are virtually guaranteed to be open.

We want to show that the behaviour is more interesting on higher-dimensional $\mathbb{Z}^d$.

##### _theorem:_ the critical parameter is non-trivial on grids (Peierls '36)

For any $\mathbb{Z}^d$, the critical parameter is in $p_{c} \in (0, 1)$.

###### _proof:_

Basically the argument works by saying that if you have exponential bounds on both, paths to infinity and closed codimension $1$ subgraphs in the dual graph, then you can bound the critical parameter from above and below.

The dual graph fact works by saying that if you have no walks to infinity, then you have a loop around the area (this is Poincaré duality on simplicial complexes).

Interestingly, if you have a group, and consider percolation on its Cayley graph, that actually tells you things about the group itself.