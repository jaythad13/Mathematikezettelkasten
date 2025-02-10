---
tags:
- math-147/5
- top
---

Let $(X, \mathcal{T})$ be a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]].

While sequences in general topological spaces don't have many of the nice properties [[Mathematical Analysis I --- math-131/notes/Sequences and convergence|they have in metric spaces]], they can be defined in the same way, and have a well-defined notion of convergence.

##### _definition:_ sequence

A sequence in $X$ is a function $\mathbb{N} \to X$ often written with $n \mapsto x_{n}$. The whole sequence is often referred to by the image of $\mathbb{N}$ — $\{ x_{n} \}_{n \in \mathbb{N}}$.

##### _definition:_ convergence

A point $x \in X$ is the limit of the sequence $\{ x_{n} \}_{n \in \mathbb{N}}$ written $x_{n} \to x$ if, for every open neighbourhood $U$ of $x$, there is some $N \in \mathbb{N}$ such that for all $n > N$, $x_{n} \in U$.

##### _theorem:_ the limit of a sequence is a limit point of the sequence

If the sequence $\{ x_{n} \}_{n \in \mathbb{N}}$ converges to $x$, then $x$ is in the [[Topology --- math-147/notes/Limit points and closed sets#_definition _ closure, closed|closure]] of the set $\{ x_{n} \}$.

###### _proof:_

If $x \in \{ x_{n} \}$, then $x$ is in the closure anyway. Suppose $x \not\in \{ x_{n} \}$. Then, the condition that $x_{n} \to x$ implies [[Topology --- math-147/notes/Limit points and closed sets#_proposition _ limit points not in the set|the condition]] for $x$ to be a limit point of $\{ x_{n} \}$ (that every neighbourhood of $x$ contains points of $x_{n}$)

Note then that if $\{ x_{n} \} \subseteq A$ and $x_{n} \to x$, then $x \in \overline{A}$.

The converse is not true in general — essentially, a topology doesn't have to keep containing subsets of open sets as many topologies do.

##### _example:_ a limit point that is not a limit of a sequence



However it is true in metric spaces.

##### _theorem:_ a limit point is the limit of a sequence in metric spaces

In the [[Mathematical Analysis I --- math-131/notes/Open and closed sets#_examples _ open sets|induced topology]] on a [[Mathematical Analysis I --- math-131/notes/Metric spaces#_definition_ metric space, metric|metric space]], if $x$ is a limit point of $A \subseteq X$, there is a sequence of points in $A$ that converges to $x$.

###### _proof sketch:_

Choose smaller and smaller open balls centred at $x$ and intersecting with $A$; choose points in each of them.

##### _example:_ sequences in the cofinite and cocountable topologies

The sequences converging in the [[Topology --- math-147/notes/Topologies#_example _ the finite and countable complement topologies|cofinite topology]] on a set $X$ are exactly the eventually constant sequences and the sequences with infinite image. If a sequence is eventually constant, it obviously converges to the value it is constant at. Since each neighbourhood of $x \in X$ can only exclude finitely many points of an infinite sequence, for all $n$ greater than some $N$, all $x_{n}$ must be in that neighbourhood. Finally, any sequence that is finite and not eventually constant, cannot converge to any $x$ — consider the open neighbourhood of $x$ excluding all points of the sequence except possibly $x$.

The sequences converging in the [[Topology --- math-147/notes/Topologies#_example _ the finite and countable complement topologies|cocountable topology]] on a set $X$ are exactly the — exactly the eventually constant sequences. For the same reason as with the cofinite topologies, if a countable sequence is not eventually constant, there is a neighbourhood of every $x \in X$ that breaks the condition for $x$ to be the limit of the sequence. Since sequences are at most countable, the convergent sequences are only the eventually constant sequences.