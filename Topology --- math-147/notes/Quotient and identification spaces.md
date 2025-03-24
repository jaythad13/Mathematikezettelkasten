---
tags:
- math-147/16
- top
---

Let $(X, \mathcal{T})$ be a topological space. Note that $Y$ may not be a space, but just a set.

Quotient and identification spaces make formal the idea of gluing together parts of a topological spaces as math always does — with equivalence classes that identify the points we're gluing together. For example, with this view, the circle $S^1$ is the interval $[0, 1]$ with $0$ and $1$ identified, and then the cylinder $S^1 \times [0, 1]$ is the square $[0, 1] \times [0, 1]$ with one pair of sides identified. This really does change the topology of the space since there is no [[Topology --- math-147/notes/Homeomorphisms|homeomorphism]] between $[0, 1]$ and $S^1$.

### Identification spaces

Given an equivalence relation $\sim$ on a topological space, an identification space is a way to give the set of equivalence classes $X / \sim$ the structure of a topological space.

##### _definition:_ identification space 

Given an equivalence relation $\sim$ on $X$, let $X / \sim$ be the set of equivalence classes, and $\pi : X \to X / \sim$ be the obvious surjective quotient map sending $x \in X$ to its equivalence class under $\sim$.

$X / \sim$ is a topological space, called an identification space, with the topology containing exactly those subsets $U \subseteq X / \sim$ with $\pi ^\text{pre}(U)$ is open in $X$.

$\pi$ is called the identification map.

##### _example:_ the union is an identification space of the disjoint union

Given two topological spaces (perhaps sharing points when embedded in some $\mathbb{R}^n$), the disjoint union $X \sqcup Y$ has an obvious topology — open sets are unions of open sets in $X$ and $Y$, whereas the topology of the union $X \cup Y$ is harder to describe without exactly the data of where they share points. We can use the identification map $\pi : X \sqcup Y \to X \cup Y$ to make dealing with the topology on $X \sqcup Y$ easier.

##### _example:_ the Möbius strip

The Möbius strip is an identification space of $X = [0, 8] \times [0, 1]$. It's given by gluing the edges $\{ 0 \} \times [0, 1]$ and ${8} \times [0, 1]$ backwards — we write $(0, t) \sim (8, 1 - t)$ and then the Möbius band is $X / \sim$.

##### _example:_ the sphere

The sphere $S^{2}$ is an identification space of $\mathbb{D} \sqcup \mathbb{D}$ with the two boundary circles identified in the obvious way — $p_{\mathbb{D}_{1}} \sim p_{\mathbb{D}_{2}}$ for any $p \in S^1$, and then $S^{2} = \mathbb{D} \sqcup \mathbb{D} / \sim$.

Wedges and cones are two ways to create new spaces from identification spaces.

##### _definition:_ wedge sum

The wedge sum of topological spaces $X$ and $Y$ with respect to base points $x_{0}$ and $y_{0}$ is $X \vee Y = X \sqcup Y / x_{0} \sim y_{0}$.

##### _definition:_ cone

The cone over a topological space is the "cylinder over $X$" with all points at one end identified. That is, the cone over $X$ is $X \times [0, 1] / \sim$ where $(x_{1}, 0) \sim (x_{2}, 0)$ for any two points $x_{1}, x_{2} \in X$.

##### _example:_ the prototypical cone

The cone over the circle $S^1$ is just the prototypical cone — like an ice-cream cone.

### Quotient spaces

Quotient spaces are a generalisation of identification spaces that arise directly from a specific map that we treat like an identification map. In effect, they are still identification spaces if we treat sets up to isomorphism.

##### _definition:_ quotient topology, quotient space, quotient map

If $\pi : X \to Y$ is a surjection onto a set $Y$, the quotient topology on $Y$ consists of exactly those subsets $U \subseteq Y$ that have $\pi^\text{pre}(U)$ open in $X$.

$Y$ is then a quotient space, and $\pi$ is a quotient map.

In general, a continuous surjection of topological spaces $\pi : X \to Y$ is called a quotient map, and $Y$ a quotient space if $Y$ has the quotient topology with respect to $\pi$.

It does indeed need to be verified, that the quotient topology is really a topology (which also shows the same for the identification space topology). In fact, the quotient topology is just right so that the quotient map is continuous.

##### _proposition:_ quotient maps are just about continuous

If $Y$ is a set with $\pi : X \to Y$ a surjection, then the quotient topology on $Y$ is the [[Topology --- math-147/notes/Bases#_definition _ strength of a topology, coarser, finer|strongest]] topology on $Y$ that makes $\pi$ continuous.

###### _proof:_

If there were a stronger topology on $Y$ with any other open set, then that open set wouldn't have an open pre-image (because all those that do are already in the quotient topology) and thus, $\pi$ wouldn't be continuous.

##### _proposition:_ the universal property of quotients

Suppose $\pi : X \to Y$ is a quotient map. Then a map $g : Y \to Z$ is continuous if and only if $g \circ \pi : X \to Z$ is continuous.

###### _proof:_

If $g$ is continuous, since [[Topology --- math-147/notes/Continuous functions#_proposition _ composition of continuous functions|continuous functions compose]], $g \circ \pi$ is continuous.

Suppose $g \circ \pi$ is continuous. Then, for all open $V \subseteq Z$, $(g \circ \pi)^\text{pre}(V) = \pi^\text{pre}(g^\text{pre}(V))$ is open in $X$. But then by definition of a quotient space, $g^\text{pre}(V)$ is open in $Y$.