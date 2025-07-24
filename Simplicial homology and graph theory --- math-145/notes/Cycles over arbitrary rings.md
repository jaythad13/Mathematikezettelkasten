---
tags:
- math-145/3
- alg-top
- top
---

So far we've defined $1$-[[Simplicial homology and graph theory --- math-145/notes/Discrete winding number#_definition _ $1$-chain, $1$-cycle|chains]] (and cycles) in the way that makes sense — there are an integer number of each line segment. Now we will do a rubbishy abstract nonsense thing and define this over any [[Abstract algebra --- math-171/notes/Rings#_definition _ commutative ring|(commutative) ring]].

##### _definition:_ $1$-chains, $1$-cycles over $A$

Given a commutative ring $A$, a $1$-chain over $A$ is an element of the free $A$-module over line segments in $\mathbb{R}^{2}$. That is, a $1$-chain $\gamma$ over $A$ is a weighted sum
$$
\gamma = \sum_{i = 1}^n \lambda_{i} \, \overline{\mathbf{a}_{i}, \mathbf{b}_{i}}.
$$

A $1$-chain $\gamma$ over $A$ is a $1$-cycle if the weighted number of times each $\mathbf{v}$ is the start of a line segment is the same as the weighted sum of the number of times $\mathbf{v}$ is then end of a line segment. That is,
$$
\sum_{i \mid \mathbf{a}_{i} = \mathbf{v}} \lambda_{i} = \sum_{i \mid \mathbf{b}_{i} = \mathbf{v}} \lambda_{i}
$$
for all $\mathbf{v} \in \mathbb{R}^{2}$.

##### _examples:_ $1$-cycles

Let $\mathbf{a}, \mathbf{b}, \mathbf{c}, \mathbf{d}$ be the corners of the square $[-1, 1] \times [-1, 1]$ going counter-clockwise from $\mathbf{a} = (1, 1)$, 
$$
\gamma = 3 \, \overline{\mathbf{a}, \mathbf{b}} + \overline{\mathbf{a}, \mathbf{d}} + 2 \, \overline{\mathbf{b}, \mathbf{d}} + 3 \, \overline{\mathbf{c}, \mathbf{b}} + \overline{\mathbf{c}, \mathbf{d}}
$$
is a $1$-cycle over $\mathbb{Z} / 2 \mathbb{Z}$ and $\mathbb{Z} / 4 \mathbb{Z}$ (or really, any ring of characteristic dividing $4$).

Any orientation (which way to direct the edge) of the [[Superdiscrete --- math-55A/notes/Basic graph theory#_definition _ complete graph, $K_n$|complete graph]] $K_{7}$ is a $1$-cycle over $\mathbb{Z} / 2 \mathbb{Z}$ since each vertex has an even degree, and thus, must have even difference between out degree and in degree.

### Winding number

Let $\gamma = \sum_{i = 1}^n \overline{\mathbf{a}_{i}, \mathbf{b}_{i}}$ be a $1$-cycle over a commutative ring $A$.

A bad definition of winding number over $A$ is just porting over the [[Simplicial homology and graph theory --- math-145/notes/Discrete winding number#_definition _ winding number (of a $1$-cycle)|original definition]] like so —
$$
w_{A}(\gamma, 0) = \frac{1}{2 \pi} \sum_{i = 1}^n \lambda_{i} \, \theta(\overline{\mathbf{a}_{i}, \mathbf{b}_{i}}, 0)
$$
This is nonsensical because what on earth is the product of $\lambda_{i} \in A$ and the angles in $\mathbb{R}$. Instead, we need to use [[Simplicial homology and graph theory --- math-145/notes/Discrete winding number#_proposition _ the ray escape formula|the equivalent ray escape formula]].

##### _definition:_ winding number

The winding number of $\gamma$ about $0$ is
$$
w_{A}(\gamma, 0) = \sum_{i = 1}^n \lambda_{i} \operatorname{X}(\overline{\mathbf{a}_{i}, \mathbf{b}_{i}}, R_{\phi})
$$
where $\operatorname{X}$ is the [[Simplicial homology and graph theory --- math-145/notes/Discrete winding number#_proposition _ the ray escape formula|crossing number]], and $R_{\phi}$ is the ray from $0$ at any angle $\phi$.

Notice that this definition is better since $\operatorname{X}$ is one of $1, 0, -1$, all of which exist in $A$. Of course, we need to show that this is well-defined. Thus, until we do, we should call this $w_{A}^\phi$ — the winding number over $A$ with respect to $\phi$.

##### _proposition:_ winding number over $A$ is well-defined

$w_{A}(\gamma, 0)$ is independent of the choice of angle $\phi$.

###### _proof sketch:_

Write the difference between $\operatorname{X}(\overline{\mathbf{a}, \mathbf{b}}, R_{\phi})$ and $\operatorname{X}(\overline{\mathbf{a}, \mathbf{b}}, R_{\psi})$ as $s(\mathbf{b}) - s(\mathbf{a})$ for a function $s : \mathbb{R}^{2} \setminus \{ 0 \} \to \mathbb{Z} \to A$ (by the [[Basic category theory --- basic-cat/notes/An introduction to universal properties#_example _ $ mathbb{Z}$ is uniquely embedded in every ring|initial property]] of $\mathbb{Z}$). Thus,
$$
w_{A}^\psi(\gamma, 0) = w_{A}^\phi(\gamma, 0) + \sum_{i = 1}^n \lambda_{i} s(\mathbf{b}_{i}) - \sum_{i = 1}^n \lambda_{i} s(\mathbf{a}_{i}).
$$
Turn the latter sum into a sum over $\mathbf{v} \in \mathbb{R}^{2} \setminus \{ 0 \}$ and cancel it out using the cycle condition.

Many of the same basic properties of winding number hold.

##### _proposition:_ winding number is additive

For any two $1$-cycles $\gamma_{1}, \gamma_{2}$ over $A$,
$$
w_{A}(\gamma_{1} + \gamma_{2}, 0) = w(\gamma_{1}, 0) + w(\gamma_{2}, 0).
$$

##### _proposition:_ winding number is locally constant

For any $1$-cycle over $A$, the function $x \mapsto w_{A}(\gamma, x)$ is constant on each of the connected regions of $\mathbb{R}^2 \setminus \operatorname{supp} \gamma$.