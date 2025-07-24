---
tags:
- vsrp-2025
- comb
- graph
---

The honeycomb lattice is exactly what you think it is. Unfortunately, it's more difficult than that to define.

##### _definition:_ honeycomb lattice

The honeycomb (or hexagonal) lattice $\mathbb{H}$ is the [[Superdiscrete --- math-55a/notes/Basic graph theory#_definition _ graph|graph]] embedded in $\mathbb{C}$ consisting of vertices
$$
v = 1 +  \sum_{n  = 0}^6 c_{n} \zeta^n
$$
such that $(c_{1} + c_{3} + c_{5}) - (c_{2} + c_{4} + c_{6}) \in \{ -1, 0, 1 \}$, where $\zeta = e^{i \pi / 3}$. 

Two vertices $v_{1}, v_{2} \in \mathbb{H} \subseteq \mathbb{C}$ are adjacent if $v_{2} - v_{1} = \zeta^n$.

The $1$ in the sum defining $v$ is so that $0$ becomes a lattice point rather than the centre of the lattice.

Because of reasons motivated by theoretical physics, it becomes interesting to consider the "loop configurations" on the hexagonal lattice and put a probability measure on the space of all of them.

##### _definition:_ loop configuration, weak loop configuration

A loop configuration on $\mathbb{H}$ is a subgraph $\eta \subseteq \mathbb{H}$ with each vertex having even [[Superdiscrete --- math-55a/notes/Basic graph theory#_definition _ degree, $d(v)$|degree]].

A weak loop configuration on $\mathbb{H}$ is a subgraph $\eta \subseteq \mathbb{H}$ with every vertex having even degree, except possibly two vertices of degree $1$.

Since each vertex on $\mathbb{H}$ has degree at most $3$, this forces the degrees of a vertex to be $0$ or $2$ in the general case. In the weak case, $\eta$ is the union of a loop configuration with a self-avoiding walk.

##### _definition:_ self-avoiding walk, number of self-avoiding walks

A self-avoiding walk is a [[Superdiscrete --- math-55a/notes/Basic graph theory#_definition _ walk|walk]] with no repeated vertices — what is sometimes called a [[Superdiscrete --- math-55a/notes/Basic graph theory#_definition _ path|path]].

We will denote the number of self-avoiding walks (starting from vertex $0$) by $c_{n}$. Note that $c_{n}$ doesn't depend on the choice of starting vertex.

Then to understand the limiting behaviour of probability measures on loop configurations, it becomes relevant to understand the limiting behaviour of the number of self-avoiding walks $c_{n}$ as $n \to \infty$. We will show that they have a precise asymptotic behaviour.

### Elementary bounds on self-avoiding walks and a reduction

We can put some simple bounds on self-avoiding walks to show that they grow exponentially. For example, self-avoiding walks are bounded above by walks at all, or walks at all.

##### _proposition:_ self-avoiding walks grow at most exponentially

For all $n \in \mathbb{N}$, $c_{n} \le 3 \cdot 2^{n - 1} \le 3^n$.

###### _proof:_

Each vertex of $\mathbb{H}$ has degree $3$. A walk on $\mathbb{H}$ corresponds to a choice of next vertex at each vertex. To create a walk of length $n$, there are then at most $3^n$ possible choices, so $c_{n} \le 3^n$.

We can sharpen this bound. At each vertex after the first, only two of the adjacent vertices are unexplored (the other was the previous vertex). Thus, $c_{n} \le 3 \cdot 2^{n - 1}$.

##### _proposition:_ self-avoiding walks grow at least exponentially

For all $n \in \mathbb{N}$, $\sqrt{ 2 }^n \le c_{n}$.

###### _proof:_

Self-avoiding walks are bounded below by "escaping" walks — walks that always increase their graph-theoretic distance to $0$. At each vertex there is always one edge that leads away from $0$. If there is only one such edge, the vertex it leads to has two edges leading away from zero. Thus, given a self avoiding walk of length $n$, there are always at least two ways to extend it to a self-avoiding walk of length $n + 2$.

Inducting on $c_{1} = 3 > \sqrt{ 2 }$ and $c_{2} =6 > \sqrt{ 2 }^{2}$, this gives $c_{n} \geq \sqrt{ 2 }^n$.

In fact, since self-avoiding walks are in some sense "sub-additive" we can prove that there is a specific constant $\mu$ so that $c_{n} \sim \mu^n$ as $n \to \infty$. Specifically,

##### _proposition, definition:_ existence of a connective constant, connective constant

There is a positive real $\mu$ such that
$$
\mu = \lim_{ n \to \infty } c_{n}^{1 / n}.
$$

$\mu$ is called the connective constant of $\mathbb{H}$.

###### _proof:_

Notice that for any positive integers $m, n$ we can cut a self-avoiding walk uniquely into a self-avoiding walk of length $m$ and another of length $n$. Of course, not every composition of self-avoiding walks of length $m$ and $n$ gives an self-avoiding walk of length $m + n$ (split a hexagon in two).

Thus, $c_{m + n} \le c_m c_{n}$ and for $a_{n} = \log c_{n}$, we have $a_{m + n} \le a_{m} + a_{n}$. It's a fact from analysis that a sub-additive sequence has $a_{n} / n$ converging to $\alpha = \inf_{n} a_{n}  /n$ as $n \to \infty$. In particular, sub-additivity forces $a_{n} \leq n a_{1}$, and thus, $a_{n} / n \leq a_{1}$.

Since $c_{n} > 1$ the $a_{n}$ are positive, and thus, $a_{n} / n$ are bounded below by $0$. Taking exponentials, we have that $e^{a_{n} / n}$ converges to $e^\alpha$ — that is $c_{n}^{1 / n}$ converges to $\mu = e^\alpha$. Our elementary bounds on $c_{n}$ force $\mu > \sqrt{ 2 } > 1$.

### Walks on mid-edges

It will be useful for analysis calculations to consider an equivalent type of walk — walks on mid-edges.

##### _definition:_ mid-edge, $\mathbb{H}'$

The mid-edges of $\mathbb{H}$ are the set $\mathbb{H}'$ of all $(v_{1} + v_{2}) / 2$ for adjacent vertices $v_{1}, v_{2} \in V(\mathbb{H})$. 

##### _definition:_ walk on mid-edges

Given a source mid-edge $a$, a walk on mid-edges $\gamma : a \to E \subseteq \mathbb{H}'$ is the data of $a$ a mid-edge between $v_{1}$ and $v_{2}$, $b \in E$ a mid-edge between $w_{1}$ and $w_{2}$, and a walk from one of the $v_{i}$ to $w_{j}$ on $\mathbb{H}$.

A useful tool is a generating function to keep track of all of the self-avoiding walks — the "partition function".

##### _definition:_ the partition function

The partition function for self-avoiding walks on the honeycomb lattice is
$$
Z(x) = \sum_{\gamma : 0 \to \mathbb{H}'} x^{\ell(\gamma)} = \sum_{n = 1}^\infty c_{n} x^n
$$
where $\ell(\gamma)$ is the length of $\gamma$.

This function immediately gives an analytic interpretation for the connective constant.

##### _proposition:_ analytic interpretation of the connective constant

Given the connective constant $\mu$, its reciprocal $1 / \mu$ is the radius of convergence of $Z$.

###### _proof:_

The [[Analysis --- math-131/notes/Power series#_theorem _ every power series has a radius of convergence (Abel)|definition of radius of convergence]] for a power series $\sum_{n = 1}^\infty c_{n} x^n$ gives $R = 1 / \lim_{ n \to \infty } c_{n}^{1 / n}$, so in this case $R = 1 / \mu$.

By considering a complex analytic twisting of the partition function (the [[Holomorphicity in loop models --- vsrp-2025/The parafermionic observable|parafermionic observable]]), we will be able to show that it really does have the desired radius of convergence.