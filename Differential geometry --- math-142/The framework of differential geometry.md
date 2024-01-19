---
tags:
- diff-geo
- math-142
lecture: math-142-1
---

### Some motivation

Really, with this course, we're trying to motivate algebraic geometry. Algebraic geometry is half abstract algebra — groups, rings and the like and half geometry — differential geometry. This class is about the second half.

Differential geometry grew out of physics and trying to mathematically express the "structure of the universe". Specifically, people were trying to talk about electromagnetism and (Einstein's theory of) gravity, which arise from an electromagnetic field and a gravitational field respectively. What's a way to write about both using the same mathematical framework?

### Euclidean space

For this course, we will mostly be working in real [[Euclidean space]], and usually, 3-space, $\mathbb{R}^3$. Note that this explicitly includes the [[Linear algebraic considerations#_definition _ Euclidean space|usual inner product space structure]].

##### _notation:_ $\mathbf{p}$, $x$, $y$, $z$ operators

For $\mathbf{p} \in \mathbb{R}^n$, we say $\mathbf{p} = (p_{1}, \dots , p_{n})$,

For $\mathbf{p} \in \mathbb{R}^3$, we say $x(\mathbf{p}) = p_{1}$, $y(\mathbf{p}) = p_{2}$, and $z(\mathbf{p}) = p_{3}$.

We are interested in functions on Euclidean space, and particularly, $f : \mathbb{R}^3 \to \mathbb{R}$, or from some subset of $\mathbb{R}^3$. We will rigorously define [[Partials and the "total" derivative#_definition _ the $j$th partial derivative|partial derivatives]] later, but lets make some definitions right now.

##### _(unrigorous) definition:_ smooth, $\mathcal{C}^\infty$

If, for $f : \mathbb{R}^3 \to \mathbb{R}$ we can take partial derivatives of all orders, we say $f$ is a smooth or an infinitely differentiable function. We can write this as $f \in \mathcal{C}(\mathbb{R}^3)$.

Theres an obvious way to define the sum and product of functions — do it pointwise.

The sum and product of smooth functions are smooth as well, and this gives us a [[Vector spaces|vector space]] and [[Rings|ring]] structure on the functions.

##### _proposition:_ $\mathcal{C}^\infty(\mathbb{R}^3)$ is a ring and a vector space

For $f, g \in \mathcal{C}^\infty(\mathbb{R}^3)$ both $f + g \in \mathcal{C}^\infty(\mathbb{R}^3)$ and $f, g \in \mathcal{C}^\infty(\mathbb{R}^3)$. Thus, $\mathcal{C}^\infty(\mathbb{R}^3)$ is a commutative ring with identity given by the function $x \mapsto 1$ and a vector space with the regular scalar multiplication.

##### _proof sketch:_

[[Differentiability theorems#_proposition _ sums are differentiable|Sum rule]], [[Differentiability theorems#_proposition _ products are differentiable|product rule]] and an easy verification for the identity function. 

### Tangent spaces in $\mathbb{R}^3$

When we're living on a surface, we want to have a nice coordinate system wherever we are. However, a surface looks different at different points, even locally, and the surface itself is relative in space. This means that a global coordinate system — one that is the same everywhere — loses all of the geometric information about the surface, and the

##### _definition:_ tangent space at $\mathbf{p}$, $\mathrm{T}_{\mathbf{p}}\mathbb{R}^3$ , tangent vectors

Say we have $\mathbf{p} \in \mathbb{R}^3$. The tangent space at $\mathbf{p}$ is the vector space of all pairs $[\mathbf{v}, \mathbf{p}]$ where $\mathbf{v} \in \mathbb{R}^3$ and addition and scalar multiplication are defined by just performing the regular operations on the first part of the bracket. We call it $\mathrm{T}_{\mathbf{p}}\mathbb{R}^3$ and each of its elements a tangent vector at $\mathbf{p}$.

We've said its a vector space without proving it but it isn't too hard — it's just $\mathbb{R}^3$ but we shift it to rest at $\mathbf{p}$. This may seem silly now, but that's only because $\mathbf{v}$ and $\mathbf{p}$ are both in $\mathbb{R}^3$ so we can think of any $[\mathbf{v}, \mathbf{p}]$ as just $\mathbf{p} + \mathbf{v}$. Later we might have $\mathbf{v} \in \mathbb{R}^2$ or something else and then it becomes interesting.

We call $\mathbf{p}$ the point of application, and $\mathbf{v}$ the vector part.

Note that we can identify $[\mathbf{v}, \mathbf{p}]$ with a line (thought of as a function $\ell : [0, 1] \to \mathbb{R}^3$ by $t \mapsto \mathbf{p} + t \mathbf{v}$) with an initial point $\mathbf{p}$ and slope $\mathbf{v}$.

Also see that right now we haven't really said what the tangent vector is tangent to!

##### _definition:_ equality, parallel

Given tangent vectors $[\mathbf{v}, \mathbf{p}]$ and $[\mathbf{w}, \mathbf{q}]$,
- we say they are parallel if $\mathbf{v} = \mathbf{w}$
- we say they are equal if $\mathbf{v} = \mathbf{w}$ and $\mathbf{p} = \mathbf{q}$.

##### _definition:_ tangent bundle in $\mathbb{R}^3$, $\mathrm{T}\mathbb{R}^3$

The set of all $[\mathbf{v}, \mathbf{p}]$ (with neither of the parts fixed) is the tangent bundle to $\mathbb{R}^3$, $\mathrm{T}\mathbb{R}^3$.

Note that this isn't a vector space!

### Vector fields

Tangent spaces allow us to think about vector fields in a slightly funny, but useful way

##### _(re)definition:_ vector field

A vector field is a function $\mathbf{F} : \mathbb{R}^3 \to \mathrm{T}\mathbb{R}^3$ that assigns to each point $\mathbf{p} \in \mathbb{R}^3$ a tangent vector in its tangent space $\mathbf{F}(\mathbf{p}) = [\mathbf{v}, \mathbf{p}]$.

##### _examples:_ decomposing vector fields

Say $\mathbf{p}$ is a point in the sea, that we model by $\mathbb{R}^3$. The direction that the current pushes you depends on the point you are at. Thus, we can write the force field as follows, and even decompose it into component vector fields
$$
\begin{split}
\mathbf{F}(\mathbf{p}) & = [(F_{1}(\mathbf{p}), F_{2}(\mathbf{p}), F_{3}(\mathbf{p})), \mathbf{p}] \\
& = F_{1}(\mathbf{p})[\mathbf{e}_{1}, \mathbf{p}] + F_{2}(\mathbf{p})[\mathbf{e}_{2}, \mathbf{p}] + F_{3}(\mathbf{p})[\mathbf{e}_{3}, \mathbf{p}] \\
& = \mathbf{F}_{1}(\mathbf{p}) + \mathbf{F}_{2}(\mathbf{p}) + \mathbf{F}_{3}(\mathbf{p}).
\end{split}
$$
which tell us how much the vector fields are pushing us in each of the orthogonal directions (defined by the standard basis) when we are at point $\mathbf{p}$.