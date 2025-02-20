---
tags:
- math-145/4
- math-145/5
- alg-top
---

Homology groups measure when [[Topics in Geometry and Topology --- math-145/notes/Chains revisited|cycles]] fail to be boundaries of a higher-dimensional [[Topics in Geometry and Topology --- math-145/notes/Chains revisited|chain]].

##### _definition:_ zeroth homology group

The zeroth homology group is $\mathrm{H}_{0}(U, \mathbb{F}) = \mathrm{Z}_{0}(U, \mathbb{F}) / \mathrm{B}_{0}(U, \mathbb{F})$ where $\mathrm{Z}_{0}(U, \mathbb{F}) = \mathrm{C}_{0}(U, \mathbb{F})$ is the vector space of $0$-cycles and equivalently, the space of $0$-chains.

In the case of $1$-chains, as long as $U$ is connected and [[Topics in Geometry and Topology --- math-145/notes/Chains revisited#_definition _ the mass cocycle|the mass cocycle]] is zero, we have that a $0$-cycle (which is just a $0$-chain) is indeed a boundary. Otherwise [[Topics in Geometry and Topology --- math-145/attachments/homework/hw 4/hw 4.pdf|the homework]] shows us that $\mathrm{H}_{0}$ measures the number of connected components.

Here again, the homology group measures the degree of obstruction to $1$-cycles being boundaries of $2$-chains

##### _definition:_ first homology group

The first homology group on $U$ over $\mathbb{F}$ is the [[Quotient spaces|quotient vector space]]
$$
\mathrm{H}_{1}(U, \mathbb{F}) = \mathrm{Z}_{1}(U, \mathbb{F}) / \mathrm{B}_{1}(U, \mathbb{F}).
$$

Specifically, what does the homology measure? Whatever it is, the [[Topics in Geometry and Topology --- math-145/notes/Discrete winding number#_definition _ winding number (of a $1$-cycle)|winding number]] gives a way to measure it too — specifically, if a $1$-cycle is the boundary of a $2$-chain, it has winding number $0$ about every point not in the support of the $2$-chain.

##### _proposition:_ the winding number of the boundary of a chain

Given $x$ not in the support of a $2$-chain $\sigma$, the winding number of $\partial_{1} \sigma$ about $x$ is $0$.

###### _proof sketch:_

See by the [[Topics in Geometry and Topology --- math-145/attachments/homework/hw 1/hw 1.pdf#page=2|distant cycle lemma]] that this is true for any $[\mathbf{a}, \mathbf{b}, \mathbf{c}]$. Since $w_{x} : \gamma \mapsto w(\gamma, x)$ is linear, this extends linearly to the zero function.

Most of what we care about from homology we can get from the dimensions of the homology ~~groups~~ vector spaces.

##### _definition:_ Betti numbers

The $i$th Betti number $\mathrm{b}_{i}$ is the dimension of the $i$th homology group $\mathrm{H}_{i}$.

### What does homology count?

We can check the homology of the plane to get an even better guess.

##### _proposition:_ the homology of the plane

The homology groups of $\mathbb{R}^{2}$ over $\mathbb{R}$ are $\mathrm{H}_{0}(\mathbb{R}^{2}, \mathbb{R}) \cong \mathbb{R}$ with $\mathrm{b}_{0}(\mathbb{R}^{2}, \mathbb{R}) = 1$ and $\mathrm{H}_{1}(\mathbb{R}^{2}, \mathbb{R}) \cong 0$ with $\mathrm{b}_{1}(\mathbb{R}^{2}, \mathbb{R}) = 0$.

###### _proof sketch:_

The plane is convex, and thus, clearly path-connected. That is, any point $[\mathbf{a}]$ can be written as $[\mathbf{a}] = [0] + \partial [0, \mathbf{a}]$. That is, $\mathrm{H}_{0}(\mathbb{R}^{2}, \mathbb{R})$ is at most $1$-dimensional — $\mathrm{b}_{0} \le 1$. Since there are $0$-cycles that are not boundaries, $\mathrm{H}_{0}(\mathbb{R}^{2}, \mathbb{R})$ is not $0$-dimensional. Thus, $\mathrm{H}_{0}(\mathbb{R}^{2}, \mathbb{R}) = \mathbb{R}$ is one-dimensional with $\mathrm{b}_{0} = 1$.

For each $1$-cycle $\gamma = \sum_{i = 1}^n \lambda_{i} [\mathbf{a}_{i}, \mathbf{b}_{i}]$, it isn't difficult to see that $\sigma = \sum_{i = 1}^n \lambda_{i} [0, \mathbf{a}_{i}, \mathbf{b}_{i}]$ has boundary
$$
\partial \sigma = \gamma -  \sum_{i = 1}^n [0, \mathbf{b}_{i}] - [0, \mathbf{a}_{i}] = \gamma
$$
where the sum disappears by [[Topics in Geometry and Topology --- math-145/notes/Chains revisited#_definition _ $1$-cycles|the cycle definition]].

This, along with our homework suggests that the zeroth Betti number counts connected components. For open subsets of $\mathbb{R}^{2}$ [[Complex Analysis --- math-135/notes/Analysis and (metric) topology review#_proposition _ path-connectedness and connectedness are equivalent on open sets|this is essentially true]], however, we will be more careful.

##### _definition:_ polygonally path-connected, component

We say $U \subseteq \mathbb{R}^{2}$ is polygonally path-connected if every pair of points in $U$ has a polygonal path between them. 

A polygonally path-connected component of $U \subseteq \mathbb{R}^{2}$ is a maximal polygonally path-connected subset (there may be more than one) $V \subseteq U$ 

##### _theorem:_ zeroth Betti number counts polygonally path-connected components

If $U \subseteq \mathbb{R}^{2}$ has $n$ polygonally path-connected components, then $\mathrm{b}_{0}(U, \mathbb{F}) = n$.

###### _proof sketch:_

[[Topics in Geometry and Topology --- math-145/attachments/homework/hw 4/hw 4.pdf#page=2|See the homework]].

###### _succinct proof:_

The map $m = (m_{1}, \dots, m_{n}) : \mathrm{C}_{0} \to \mathbb{F}^n$ is surjective with kernel $\mathrm{B}_{0}$ (where each $m_{i}$ is the mass function with support only in the $i$th cohommponent, or is defined as in the homework). Thus, $\mathrm{C}_{0} / \mathrm{B_{0}} \cong \mathbb{F}^n$.

We might also hope that the first Betti number counts holes in the plane. This is also true!

##### _theorem:_ first Betti number counts holes

Let $\mathbf{x}_{1}, \dots, \mathbf{x}_{m}$ be distinct points $\mathbb{R}^{2}$ and let $\Lambda$ denote the set of all of them. Then $\mathrm{b}_{1}(\mathbb{R}^{2} \setminus \Lambda, \mathbb{F}) = m$.

###### _proof sketch:_

Where we used mass cocycles for zeroth Betti numbers, we will use [[Topics in Geometry and Topology --- math-145/notes/Discrete winding number#_definition _ winding number (of a $1$-cycle)|winding numbers]] this time. Notice that the linear map $\mathrm{Z}_{1} \to \mathbb{F}$
$$
w_{k} : \gamma \mapsto w_{\mathbb{F}}(\gamma, \mathbf{x}_{k})
$$
is [[#_proposition _ the winding number of the boundary of a chain|zero on boundaries]] of $2$-chains in $\mathbb{R}^{2} \setminus \Lambda$.

Thus, $w_{k} \partial_{1} = 0$, and putting each of these maps together and quotienting by (a priori) a subset of the kernel $\mathrm{B}_{1}$, we obtain a linear map $w : \mathrm{H}_{1} = \mathrm{Z}_{1} / \mathrm{B}_{1} \to \mathbb{F}^m$ by $w = \gamma \mapsto  (w_{1} \gamma, \dots, w_{m} \gamma)$.

We want to show that $\mathrm{B}_{1}$ is all of the kernel (of the lift) and thus, that $w$ is injective. Suppose $w \gamma = 0$. Then we can freely subdivide any edge of $\gamma$ without changing winding whether it is a boundary or not since $[\mathbf{a}, \mathbf{m}, \mathbf{b}]$ with boundary $\partial [\mathbf{a}, \mathbf{m}, \mathbf{b}] = [\mathbf{a}, \mathbf{m}] + [\mathbf{m}, \mathbf{b}] - [\mathbf{a}, \mathbf{b}]$ can just be added to a $2$-chain with $[\mathbf{a}, \mathbf{b}]$ in its boundary.

By subdividing so small it doesn't matter and looking at right angled triangles, we can assume all edges of $\gamma$ to be horizontal or vertical. Further, by [[Topics in Geometry and Topology --- math-145/attachments/homework/hw 4/hw 4.pdf#page=4|the homework]] we can add $2$-chains to reorient our edges so that all horizontal edges go right and vertical edges go up. By dividing fine enough, we have that $\gamma$ consists of edges on a grid.

From here the proof that $w$ is injective is a slow process of pushing $\gamma$ to $0$. [[Topics in Geometry and Topology --- math-145/attachments/texts/MATH 145 notes.pdf#page=49|See notes]].

We can show that this is surjective by picking disjoint discs around each $\mathbf{x}_{k}$ and choosing $\gamma_{k}$ that winds around each $\mathbf{x}_{k}$ once inside the disc. For each $k$th standard basis vector $\mathbf{e}_{k}$, we have $w \gamma_{k} = \mathbf{e}_{k}$.
