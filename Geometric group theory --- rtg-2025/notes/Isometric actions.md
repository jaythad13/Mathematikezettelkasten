---
tags:
- rtg-2025
- ggt
- top
- metric
---

Let $(X, d_{X}), (Y, d_{Y})$ be metric spaces.

The [[Geometric group theory --- rtg-2025/notes/Graph actions and Cayley graphs#_definition _ Cayley graphs|Cayley graph]] of a group $G$ solves the problem of finding a space with symmetries exactly encoding $G$. However, to understand $G$ fully it's useful to consider a larger space on which it acts. A natural extension is to consider groups acting on [[Mathematical Analysis I --- math-131/notes/Metric spaces#_definition_ metric space, metric|metric spaces]]. Since the action of $G$ on its Cayley graph preserves word length (and the group of homeomorphisms) the natural extension is to require $G$ to act by isometries.

##### _definition:_ isometry

An isometry $f$ of metric spaces is a function $X \to Y$ such that
$$
d_{Y}(f(x_{1}), f(x_{2})) = d_{X}(x_{1}, x_{2})
$$
for any points $x_{1}, x_{2} \in X$.

The group of isometries $X \to X$ is denoted $\operatorname{Isom} X$.

Note that isometries are topological embeddings ([[Topology --- math-147/notes/Homeomorphisms#_definition _ homeomorphism|homeomorphisms]] onto their image).

##### _definition:_ isometric action

For a group $G$ and metric space $X$, an isometric action $G \circlearrowright X$ is a [[Abstract Algebra I --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|homomorphism]] $G \to \operatorname{Isom} X$.

Equivalently, it is a group action $G \circlearrowright X$ so that the function $x \mapsto g \cdot x$ is an isometry for each $g \in G$.

##### _examples:_ isometric group actions

- The Cayley graph of a group $G$ is a metric space with the [[Mathematical Analysis I --- math-131/notes/Metric spaces#_examples _ metric spaces|graph metric]]. Thus, $G$ itself is a metric space with the [[Geometric group theory --- rtg-2025/notes/Graph actions and Cayley graphs#_definition _ word length|word length]] metric. $G$ acts on both by left multiplication.
- $\mathbb{Z}^{2}$ acts isometrically on $\mathbb{R}^{2}$ with both, Euclidean and [[Mathematical Analysis I --- math-131/notes/Metric spaces#_example _ notions of distance|taxicab]] metrics.
- The [[Abstract Algebra I --- math-171/notes/Dihedral groups and generators#_definition _ the dihedral group|dihedral group]] $D_{2n}$ acts on $\mathbb{R}^{2}$ by rotations about $0$ and reflections about the $y$-axis.

### A deep theorem from elementary facts

Using some very elementary lemmas about (convex functions on) $\mathbb{R}^n$, we can prove a deep result about any group acting on $\mathbb{R}^n$.

##### _lemma:_ convex functions have unique minima

If $f : \mathbb{R}^n \to \mathbb{R}$ is strictly convex, and has a minimum, then the minimum is unique.

###### _proof:_

Suppose $f$ is strictly convex — for each pair $x_{1} \neq x_{2} \in \mathbb{R}^n$ and $t \in [0, 1]$, we have $f(t x_{1} + (1 - t) x_{2}) < t f(x_{1}) + (1 - t) f(x_{2})$. Clearly any minimum is unique, since two distinct minima would force $f$ to be less than minimal on the line between them.

##### _lemma:_ finite sums of convex functions are convex

The finite sum of (strictly) convex functions $f_{1}, \dots, f_{n} : \mathbb{R}^n \to \mathbb{R}$ is (strictly) convex.

###### _proof:_
follows from applying the (strict) convexity definition term-by-term.

##### _lemma:_ finite sets have a centroid

For any finite set of points $\{ x_{1}, \dots, x_{n} \} \in \mathbb{R}^n$, there is a unique point $y$ minimising
$$
\sum_{j = 1}^n \lVert y - x_{j} \rVert 
$$
called the centroid of the set.

###### _proof:_

Since the distance function $y \mapsto \lVert y - x_{j} \rVert$ is strictly convex, the sum over all $j$ is strictly convex. Thus, it has a unique minimum.

Since the set of all $x_{j}$ is finite, and thus, bounded, there is some compact set $K$ outside which the sum of distances is strictly greater than within $K$. By choosing a strictly larger compact set $K' \supseteq B(x, R) \supsetneq K$, we find a local minimum in the interior of $K'$.

##### _theorem:_ free actions on $\mathbb{R}^n$ must be torsion-free

If $G \circlearrowright \mathbb{R}^n$ is a [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ stabiliser, free|free]] isometric action, then $G$ is [[Abstract Algebra I --- math-171/attachments/homework/hw 8/hw 8.pdf#page=1|torsion-free]].

###### _proof:_

Suppose $g \in G$ is torsion, and thus, any $x \in \mathbb{R}^n$ has finite [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ orbit|orbit]] $\mathcal{O}_{G}(x) = \{ g \cdot x, \dots, g^m \cdot x \}$. Then let $y$ be the centroid of $\mathcal{O}_{G}(x)$ — the unique point minimising the sum of distances from each point in $\mathcal{O}_{G}(x)$.

Since $g \cdot \mathcal{O}_{G}(x) = \mathcal{O}_{G}(x)$, the centroid of $g \cdot \mathcal{O}_{G}(x)$ is $y$. However, since $G \circlearrowright \mathbb{R}^n$ is isometric $g \cdot \mathcal{O}_{G}(x)$ has centroid $g \cdot y$. Thus, $y = g \cdot y$. Since $G \circlearrowright \mathbb{R}^n$ is free, $g$ must be the identity.

This theorem is typical of the results of geometric group theory — we prove a purely algebraic fact about a group using facts about its action on geometric spaces. Another similar fact we will prove is 

![[Geometric group theory --- rtg-2025/notes/Actions on trees#_theorem _ free actions on trees come from free groups|Free actions on trees]]