---
tags:
- math-147/14
- math-147/15
- top
---

Let $X, Y$ be topological spaces.

Continuous functions are the right morphisms for the category of topological spaces. They preserve the topology of the domain in the codomain by keeping points close together. Often the way we define this is by saying any open sets in the codomain must come from (a possibly empty) open set in the domain.

##### _definition:_ continuity

A function $f : X \to Y$ is continuous if, for each open $V \subseteq Y$, we have $f^\text{pre}(V)$ open in $X$.

We've verified [[Mathematical Analysis I --- math-131/notes/Continuity|in analysis]] that this definition of continuity is equivalent to an $\varepsilon$-$\delta$ definition of continuity, and a sequential definition of continuity (which for metric spaces is equivalent to a limit point definition of continuity). There are more equivalent definitions.

##### _proposition:_ equivalent definitions of continuity

For a function $f : X \to Y$, the following are equivalent
1) $f$ is continuous
2) for every closed $B \subseteq Y$, the pre-image $f^\text{pre}(B)$ is closed in $X$.
3) for every limit point $p$ of $A \subseteq X$, the image $f(p)$ belongs to the closure $\overline{f^\text{img}(A)}$.
4) for every $x$ and open neighbourhood $V$ of $f(x)$, there is an open neighbourhood $U$ of $x$ such that $f^\text{img}(U) \subseteq V$.

This last definition can be made into a local definition, much like the analysis definition of continuity.

##### _definition:_ continuous at a point

A function $f : X \to Y$ is continuous at a point $p \in X$ if for every open neighbourhood $V$ of $f(x)$, there is an open set $U$ containing $x$ such that $f^\text{img}(U) \subseteq V$.

Note that then a function $f : X \to Y$ is continuous if and only if it is continuous at every point.

##### _example:_ some very simple continuous functions

Constant maps, inclusion maps, and restrictions of continuous maps are continuous.

### Creating continuous functions

We don't always need the complete data of a continuous function to determine a continuous function. For example, we could just use where the points of a dense set go.

##### _proposition:_ (most) continuous functions are determined on dense sets

Suppose $A \subseteq X$ is dense in $X$. If $Y$ is Hausdorff, and $f, g : X \to Y$ are continuous functions agreeing on $A$, then $f = g$ everywhere.

We can also compose continuous functions to get new continuous functions.

##### _proposition:_ composition of continuous functions

If $f : X \to Y$ and $g : Y \to Z$ are continuous, then their composition $g \circ f : X \to Z$ is continuous.

###### _proof sketch:_

Pull back each open set $W \subseteq Z$ twice.

##### _lemma:_ the gluing lemma

Suppose $X = A \cup B$ where $A, B$ are both closed or both open in $X$. Then if $f : A \to Y$ and $g : B \to Y$ are continuous and agree on $A \cap B$, then $h : X \to Y$ defined by $h = f$ on $A$ and $h = g$ on $B$ is a well-defined continuous function.

###### _proof sketch:_

Use the closed set definition for the closed version and the open set definition for the open version. We only sketch the open set version.

If $V \subseteq Y$ is open, then its pre-images $U_{A}$ and $U_{B}$ in $A$ and $B$ are both open. Since $A$ and $B$ are open themselves, [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|by definition of the subspace topology]], $U_{A}, U_{B}$ are open in $X$ as intersection of two open sets. Thus, $U_{A} \cup U_{B} = f^\text{pre}(V)$ is open in $X$.