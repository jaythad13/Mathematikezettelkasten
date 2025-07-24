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

We've verified [[Analysis --- math-131/notes/Continuity|in analysis]] that this definition of continuity is equivalent to an $\varepsilon$-$\delta$ definition of continuity, and a sequential definition of continuity (which for metric spaces is equivalent to a limit point definition of continuity). There are more equivalent definitions.

##### _proposition:_ equivalent definitions of continuity

For a function $f : X \to Y$, the following are equivalent
1) $f$ is continuous
2) for every closed $B \subseteq Y$, the pre-image $f^\text{pre}(B)$ is closed in $X$.
3) for every limit point $p$ of $A \subseteq X$, the image $f(p)$ belongs to the closure $\overline{f^\text{img}(A)}$.
4) for every $x$ and open neighbourhood $V$ of $f(x)$, there is an open neighbourhood $U$ of $x$ such that $f^\text{img}(U) \subseteq V$.

###### _proof:_

Suppose $f$ is continuous. Let $B \subseteq Y$ be closed. Then ${Y \setminus B}$ is open and has open pre-image $U = f^\text{pre}(Y \setminus B)$. But $X \setminus f^\text{pre}(B) = U$ since the the points not in the pre-image of $B$ have to go somewhere in $Y$ and not in $B$. Thus, $f^\text{pre}(B) = X \setminus U$ [[Topology --- math-147/notes/Limit points and closed sets#_theorem _ closed sets are complements of open sets|is closed]]. This is (1) $\implies$ (2).

Suppose $f$ has closed pre-images of closed sets. Let $p$ be a limit point of $A \subseteq X$. The closed set $B = \overline{f^\text{img}(A)}$ has closed pre-image. Further, since $B$ contains the image of $A$ under $f$, its pre-image contains all of $A$. Since $f^\text{pre}(B)$ is a closed set containing $A$, [[Topology --- math-147/notes/Limit points and closed sets#_proposition _ the closure is the smallest closed set|it contains the smallest closed set, the closure]] $\overline{A}$. Then since $p \in \overline{A} \subseteq f^\text{pre}(B)$, we have $f(p) \in B$. This is (2) $\implies$ (3).

Given $x \in X$, consider any open neighbourhood $V$ of $f(x)$. Note that $Y \setminus V$ is closed and $f(x) \notin Y \setminus V = \overline{Y \setminus V}$. By properties of pre-images and images, $f^{\text{img}}(A) \subseteq Y \setminus V$ and by properties of closure (and (3)) $\overline{f^{\text{img}}(\overline{A})} \subseteq \overline{Y \setminus V}$. We have $f(x) \notin \overline{Y \setminus V}$ but if $x$ were a point of $\overline{A}$, (3) would force $f(x) \in \overline{f^{\text{img}}(\overline{A})} \subseteq \overline{Y \setminus V}$. It follows that $x$ is not a limit point nor a point of $A = f^{\text{pre}}(Y \setminus V)$. Since $x$ is not in $\overline{A}$, we must have an open neighbourhood $U$ of $x$ with $U \subseteq X \setminus A$. This neighbourhood is the desired neighbourhood since 
$$
f^{\text{img}}(U) \subseteq f^{\text{img}}(X \setminus A) \subseteq Y \setminus f^{\text{img}}(A) = Y \setminus (Y \setminus V) \subseteq V.
$$
Here we can exclude $f^{\text{img}}(U)$ from $Y \setminus V$ since $A$ is the complete pre-image of $Y \setminus V$. This is (3) $\implies$ (4).

Suppose (4). Consider an open set $V \subseteq Y$. Each $x \in f^\text{pre}(V) = U$ has open neighbourhood $U_{x} \subseteq U$ with $f^\text{img}(U_{x})$ contained in $V$ since $V$ is an open neighbourhood of $f(x)$. $U$ is then the union of all $U_{x}$. Thus, $U$ is open, giving us that $f$ is continuous.

The last definition can be made into a local definition, much like the [[Analysis --- math-131/notes/Continuity#_definition _ continuity|analysis definition of continuity]].

##### _definition:_ continuous at a point

A function $f : X \to Y$ is continuous at a point $p \in X$ if for every open neighbourhood $V$ of $f(x)$, there is an open set $U$ containing $x$ such that $f^\text{img}(U) \subseteq V$.

Note that then a function $f : X \to Y$ is continuous if and only if it is continuous at every point.

##### _example:_ some very simple continuous functions

Constant maps, inclusion maps, and restrictions of continuous maps are continuous.

### Creating continuous functions

We don't always need the complete data of a continuous function to determine a continuous function. For example, we could just use where the points of a [[Topology --- math-147/notes/Size restrictions#_definition _ dense|dense]] set go.

##### _proposition:_ (most) continuous functions are determined on dense sets

Suppose $A \subseteq X$ is [[Topology --- math-147/notes/Size restrictions#_definition _ dense|dense]] in $X$. If $Y$ is [[Topology --- math-147/notes/Separation properties#_definition _ Hausdorff spaces, $T_{2}$ spaces|Hausdorff]], and $f, g : X \to Y$ are continuous functions agreeing on $A$, then $f = g$ everywhere.

###### _proof:_

We will show that for any $p \in X$, any two open neighbourhoods $V_{f}$ of $f(p)$ and $V_{g}$ of $g(p)$ in $Y$ intersect. Since all pairs of distinct points in a Hausdorff space have disjoint open neighbourhoods, it follows that $f(p)$ and $g(p)$ are not distinct points — $f(p) = g(p)$.

Let $V_{f}$ and $V_{g}$ be open neighbourhoods of $f(p)$ and $g(p)$ respectively in $Y$. Also let $U_{f} = f^\text{pre}(V_{f})$ and $U_{g} = g^\text{pre}(V_{g})$. By the continuity of $f$ and $g$, these are both open neighbourhoods of $p$ in $X$. Their intersection $U$ is also an open neighbourhood of $p$. [[Topology --- math-147/notes/Size restrictions#_proposition _ dense sets have non-empty intersection with every open set|Since]] $A$ is dense, $U$ contains a point $a \in A$ where $f(a) = g(a)$. But then $V_{f} = f^\text{img}(U_{f})$ and $V_{g} = g^\text{img}(U_{g})$ have a non-empty intersection containing $f(a) = g(a)$. This is exactly what we needed to show.

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