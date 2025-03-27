---
tags:
- math-145/7
- math-145/9
- prob
---

Given an art museum that is a grid, with a guard and an exit at two different vertices, what is the probability that the thief will randomly walk to the exit before walking to the guard?

##### _definition:_ random walk on a graph with boundary

Given a [[Topics in Geometry and Topology --- math-145/notes/Calculus on a graph#_definition _ graph with boundary|graph with boundary]] $G$ with $g : B(G) \to \mathbb{R}$ a "reward" function. A random walk is a random sequence of vertices $x_{0}, x_{1}, \dots$ defined by
$$
x_{n + 1} = \begin{cases}
y \text{ with probability } \frac{1}{\lvert N(x_{n}) \rvert } & x_{n} \in I(G), y \in N(x_{n}) \\
x_{n} & x_{n} \in B(G).
\end{cases}
$$

If the random walk is eventually constant at $b \in B(G)$, we say the walk stops at $b$. We say then that the reward is $g(b)$. It's a fact that for a finite graph with [[Topics in Geometry and Topology --- math-145/notes/Calculus on a graph#_definition _ relative Betti number|relative Betti number]] $\mathrm{b}_{0}(G, B) = 0$, (that is, all connected components eventually reach the boundary) then stopping is probability $1$ (almost certain).

##### _proposition:_ stopping is almost certain

##### _theorem:_ expected value of reward solves a Dirichlet problem

If $G$ is a finite graph with boundary, connected, with $\mathrm{b}_{0}(G, B) = 0$, and a reward function $g : B(G) \to \mathbb{R}$, then any function $f$ with
$$
f(x) = \mathbb{E}(g(b) \mid x_{0} = x)
$$
where $b$ is the random variable that gives the vertex where random walk stops (so $g(b)$ is just a shorthand for reward), then $f$ solves [[Topics in Geometry and Topology --- math-145/notes/The Dirichlet problem on a graph|the Dirichlet problem on a graph]] with boundary value $g$.

###### _proof:_

$$
\begin{align}
f(x) & = \mathbb{E}(g(b) \mid x_{0} = x) \\
 & = \sum_{y \in N(x)} \mathbb{E}(g(b) \mid x_{1} = y) \mathbb{P}(x_{1} = y \mid x_{0} = x) \\
 & = \sum_{y \in N(x)} f(y) \frac{1}{\lvert N(x) \rvert }.
\end{align}
$$

But then by definition $\Delta f = 0$. Clearly $f = g$ on $B$. 

Note that if $B$ consists of "guard" vertices where the reward is $0$ and "exit" vertices where the reward is one, then $\mathbb{E}(g(b) \mid x_{0} = x)$ is just the probability of "escape" for a random walk starting at $0$.

### on infinite graphs

We can also use our tools to understand random walks on infinite graphs, as long as they are [[Topics in Geometry and Topology --- math-145/notes/Calculus on a graph#_definition _ locally finite graph|locally finite]].

##### _definition:_ random walk

Given a locally finite graph $G$ with a starting vertex $x_{0}$ and a positive weight function $c_{E} : E(G) \to [0, \infty)$, a random walk is a sequence of vertices $x_{0}, x_{1}, \dots$ such that
$$
\mathbb{P}(x_{n + 1} = y \mid x_{n} = x) = \begin{cases}
c_{E}(x, y) / c_{V}(x) & y \in N(x) \\
0  & \text{otherwise}.
\end{cases}
$$

Notice that here we don't have a stopping condition, so $x_{0}, x_{1}, \dots$ may be an infinite sequence. However, we can ask, if we will ever reach some $x_{n} = x_{0}$.

##### _definition:_ return and escape probability

The probability of return of a graph is the probability that a random walk eventually returns to its starting point
$$
p_{\text{R}} = \mathbb{P}(\exists n > 0, x_{n} = a \mid x_{0} = a).
$$

The probability of escape is the probability that the walk never returns — $p_{\text{E}} = 1 - p_{\text{R}}$.

It turns out that $p_{\text{R}}$ does not depend on the starting vertex $a$. Thus, it is only a characteristic of the graph.

##### _definition:_ recurrence and transience

For a locally finite graph if $p_{\text{R}} = 1$, $G$ is recurrent.

If $p_{\text{return}} < 1$, $G$ is transient.

It's easy to see that any finite graph is recurrent. However, this question is much more interesting for infinite graphs. For example, Polya's theorem says that $\mathbb{Z}^{2}$ is, surprisingly, recurrent.

##### _theorem:_ Polya's theorem, or, a drunk man will eventually come home but a dumb homing pigeon may never

$\mathbb{Z}$ and $\mathbb{Z}^{2}$ are recurrent graphs, but $\mathbb{Z}^d$ is transient for $d \ge 3$.

Our heuristic to understand transience and recurrence will be then to estimate the probabilities on finite subgraphs, using the solution to the [[Topics in Geometry and Topology --- math-145/notes/The Dirichlet problem on a graph#The weighted Dirichlet problem|(weighted) Dirichlet problem]] on the graph. In analogy with the applications of the Dirichlet problem, this can be seen as estimating the effective resistance between the starting vertex and infinity.

This heuristic really does work —

##### _definition:_ restricted return probability

The restricted return probability $p_{\text{R} \mid N(a)^k}$ is the probability that a walk starting at $a$ returns to $a$ before hitting $B(a)^k = N(a)^k \setminus N(a)^{k - 1}$ — the set of vertices at distance exactly $k$ from $a$.

##### _lemma:_ restricted return probabilities approach return probability

###### _proof sketch:_

Consider the set of all possible walks on $G$ starting at $a$. Let $A$ be all the walks that return to $a$. Then let $A_{k}$ be all the walks that return to $a$ before getting distance $k$ away from $a$. Then
$$
A_{1} \subseteq A_{2} \subseteq A_{3} \subseteq \dots \subseteq A
$$
and in fact
$$
A = \bigcup_{k = 1}^\infty A_{k}.
$$

Thus, we can write $A$ as the disjoint union of all $A_{k} \setminus A_{k - 1}$, and use countable additivity to get $\mu_{\mathbb{P}}(A) = \sum_{k = 1}^\infty \mu_{\mathbb{P}}(A_{k}) - \mu_{\mathbb{P}}(A_{k - 1}) = \lim_{ k \to \infty } \mu_{\mathbb{P}}(A_{k})$. But $\mu_{\mathbb{P}}(A_{k})$ is exactly $p_{\text{R} \mid N(a)^k}$.

##### _lemma:_ restricted return probabilities are given by a Dirichlet problem

Suppose $f$ solves the weighted Dirichlet problem on $N(a)^k$ for $g(a) = 1$ and $g = 0$ on $B(a)^k$. Then
$$
p_{\text{R} \mid B(a)^k} = \sum_{y \in N(a)} f(y) \cdot \mathbb{P}(x_{1} = y \mid x_{0} = a).
$$

###### _proof sketch:_

The term on the right is the first step of the random walk, the term on the left is the probability of returning given that first step.

