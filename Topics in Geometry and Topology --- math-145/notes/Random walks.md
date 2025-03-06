---
tags:
- math-145/7
- graph
---

Given an art museum that is a grid, with a guard and an exit at two different vertices, what is the probability that the thief will randomly walk to the exit before walking to the guard?
##### _definition:_ random walk on a graph

Given a [[Topics in Geometry and Topology --- math-145/notes/The Laplacian on a graph#_definition _ graph with boundary|graph with boundary]] $G$ with $g : B(G) \to \mathbb{R}$ a "reward" function. A random walk is a random sequence of vertices $x_{0}, x_{1}, \dots$ defined by
$$
x_{n + 1} = \begin{cases}
y \text{ with probability } \frac{1}{\lvert N(x_{n}) \rvert } & x_{n} \in I(G), y \in N(x_{n}) \\
x_{n} & x_{n} \in B(G).
\end{cases}
$$

If the random walk is eventually constant at $b \in B(G)$, we say the walk stops at $b$. We say then that the reward is $g(b)$. It's a fact that for a finite graph with [[Topics in Geometry and Topology --- math-145/notes/The Laplacian on a graph#_definition _ relative Betti number|relative Betti number]] $\mathrm{b}_{0}(G, B) = 0$, (that is, all connected components eventually reach the boundary) then stopping is probability $1$ (almost certain).

##### _proposition:_ stopping is almost certain

##### _theorem:_ expectation of reward is a Dirichlet problem

If $G$ is a finite graph with boundary, connected, with $\mathrm{b}_{0}(G, B) = 0$, and a reward function $g : B(G) \to \mathbb{R}$, then any function $f$ with
$$
f(x) = \mathbb{E}(g(b) \mid x_{0} = x)
$$
then $f$ solves [[Topics in Geometry and Topology --- math-145/notes/The Laplacian on a graph#The Dirichlet problem|the Dirichlet problem]] with boundary value $g$.

###### _proof:_

$$
\begin{align}
f(x) & = \mathbb{E}(g(b) \mid x_{0} = x) \\
 & = \sum_{y \in N(x)} \mathbb{E}(g(b) \mid x_{1} = y) \mathbb{P}(x_{1} = y \mid x_{0} = x) \\
 & = \sum_{y \in N(x)} f(y) \frac{1}{\lvert N(x) \rvert }.
\end{align}
$$

But then by definition $\Delta f = 0$. Clearly $f = g$ on $B$. 