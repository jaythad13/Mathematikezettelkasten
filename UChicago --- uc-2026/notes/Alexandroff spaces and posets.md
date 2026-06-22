---
tags:
- uc-2026/alg-top/1
- alg-top
- peter-may
---

Alexandroff spaces are a small generalisation of finite topological spaces. Often, we are interested in Alexandroff spaces satisfying the mildest possible separation property.

##### _definition:_ Alexandroff spaces, A-spaces

An **Alexandroff space** is a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]] where any (possibly infinite) intersection of open sets is open.

An **A-spaces** is a $T_{0}$ [[Topology --- math-147/notes/Separation properties#_definition _ $T_{0}$ space|space]]. We write $\mathsf{ASpc}$ for the subcategory of $\mathsf{Top}$ consisting of $A$-spaces

---

Note that if we had any more separation, Alexandroff spaces would be trivial. In Alexandroff spaces, arbitrary unions of closed sets are closed. If an Alexandroff space [[Topology --- math-147/notes/Separation properties#_definition _ $T_{1}$ space|is]] $T_{1}$, then every point is closed. Thus, in a $T_{1}$ Alexandroff space, every set is closed, and so the space is [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete]].

Alexandroff spaces each have a very interesting basis.

##### _proposition:_ the minimal basis for an Alexandroff space

Suppose $X$ is an Alexandroff space. Then the set of all $U_{x} = \bigcap_{x \in U \text{ open}} U$ forms a (minimal) [[Topology --- math-147/notes/Bases#_definition _ basis|basis]] of the topology.

###### _proof sketch:_

By definition of Alexandroff spaces, the $U_{x}$ are clearly all open. Suppose $U$ is an open set. Then clearly, we can write $U = \bigcup_{x \in U} U_{x}$ (since $U_{x}$ is an intersection of subsets including $U$, it is a subset of $U$). Also, since $U_{x}$ is the smallest open neighbourhood of $x$, it can't be recovered by unions of other $U_{y}$. Thus, this basis is minimal.

---

This basis allows us to construct a preorder on $X$ by asking whether $U_{x} \subseteq U_{y}$. If $X$ is an $A$-space, then this preorder is in fact a partial order, and gives us a natural equivalence (and in fact, a categorical isomorphism) between the category of A-spaces and the category of posets.

##### _proposition:_ the preorder on an Alexandroff space

Suppose $X$ is an Alexandroff space. The relation $x \leq y$ if $U_{x} \subseteq U_{y}$ defines a preorder on $X$. Denote the resulting preordered set by $P(X)$.

If $X$ is an A-space, then the pre-order is a partial order.

---

The proof is obvious.

##### _theorem:_ equivalence of A-spaces and posets

There is an equivalence (in fact, an isomorphism) of categories $\mathsf{ASpc} \cong \mathsf{Poset}$.

###### _proof sketch:_

The previous proposition gives us $P : \operatorname{obj} \mathsf{ASpc} \to \operatorname{obj} \mathsf{Poset}$. We show this extends to a functor. In fact, this is essentially surjective — given a poset $X$, we can form the corresponding Alexandroff space $A(X)$ by setting $U_{x} = \{ y \in X \mid y \leq x  \}$. Then $P(A(X)) = X$.

Suppose $f : X \to Y$ is a continuous map of Alexandroff spaces. Then the pre-image of each $U_{y} \subseteq Y$ is open, and thus, a union of $U_{x}$. Consider $Pf : P(X) \to P(Y)$ by $x \mapsto f(x)$ (the same map at the level of sets). Suppose $x_{1} \leq x_{2}$ and write $f(x_{i}) = y_{i}$. Thus, $x_{1} \in U_{x_{1}} \subseteq U_{x_{2}}$ Since $f$ is continuous, $U_{x_{2}} \subseteq f^\text{pre}(U_{y_{2}})$. Thus,
$$
y_{1} = f(x_{1}) \in f^\text{img}(U_{x_{2}}) \subseteq f^\text{img}(f^\text{pre}(U_{y_{2}})) \subseteq U_{y_{2}}.
$$
But then, since $U_{y_{1}}$ is the minimal open neighbourhood of $y_{1}$, we have $U_{y_{1}} \subseteq U_{y_{2}}$, and thus, $y_{1} \leq y_{2}$.

In fact, given any poset map $g : P(X) \to P(Y)$, the same map of sets $Ag : X \to Y$ is a continuous map. It suffices to check that the pre-image of each $U_{y}$ is open. Suppose $x \in Ag^\text{pre}(U_{y})$. Since $x \mapsto y$, each $x_{0} \leq y$ maps to some $y_{0} \leq y$. Thus, $U_{x} \subseteq Ag^\text{pre}(U_{y})$. That is, $Ag^\text{pre}(U_{y})$ contains an open neighbourhood of each point, and is open.

Functoriality of $P$ is obvious. Thus, $P : \mathsf{ASpc} \to \mathsf{Poset}$ is an essentially surjective, [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ faithful, full, fully faithful|fully faithful functor]], and [[Algebraic geometry --- rising-sea/notes/Natural transformations#_proposition _ equivalence is equivalent to fully faithful and essentially surjective|thus]], gives an equivalence of categories.

---