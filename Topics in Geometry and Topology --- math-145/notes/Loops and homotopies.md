---
tags:
- math-145/2
- top
---

We want a way to extend our definition of the [[Topics in Geometry and Topology --- math-145/notes/Discrete winding numbers#_definition _ winding number (of a $1$-chain)|discrete winding number]] to loops.

##### _definition:_ loop

A loop in a region $D \subset \mathbb{R}^{2}$ is a [[Mathematical Analysis I --- math-131/notes/Continuity#_definition _ continuity|continuous]] function $f : [0, 1] \to D$ such that $f(0) = f(1)$.

##### _example:_ the circle

Any circle is a loop — for radius $R$ and centre $\mathbf{x}$, consider $f : t \mapsto \mathbf{x} + (\cos(2 \pi t), \sin(2 \pi t))$.

The first step towards a continuous winding number is an equivalence relation on the loops on a region so that two loops are equivalent if you can continuously deform one into the other. Homotopy is such a relation.

##### _definition:_ homotopy

The loops $f, g$ on a region $D \subset \mathbb{R}^{2}$ are homotopic if there exists a continuous function $H : [0, 1] \times [0, 1] \to D$ such that $H(0, t) = f(t)$, $H(1, t) = g(t)$, and for each "index" $s \in [0, 1]$, the function $t \mapsto H(s, t)$ is a loop.

Essentially $H$ is a continuous map from $[0, 1] \times S_{1}$ to $D$ so that every copy of $S_{1}$ is sent to a loop, with the bottom sent to $f$ and the top sent to $g$.

We say $f \simeq g$ to denote that they are homotopic.

##### _proposition:_ homotopy is an equivalence relation

###### _proof:_
is left to the homework

A very useful result is that continuous maps preserve homotopy.

### Some useful homotopies

There are some very useful homotopies.

##### _theorem:_ pushforward homotopy

If $p : D \to E$ is a continuous map and $f \simeq g$ in $D$, then $p \circ f \simeq p \circ g$ in $E$.

###### _proof sketch:_

If $H$ is the homotopy in $D$, then $p \circ H$ is the homotopy in $E$.

##### _proposition:_ straight line homotopy

If $f, g$ are loops on $D$, and each [[Topics in Geometry and Topology --- math-145/notes/Discrete winding numbers#_definition _ line segment, support of a line segment|line segment]] $\overline{f(t), g(t)}$ has support in $D$, then $f \simeq g$.

###### _proof:_

Consider $H(s, t) = (1 - s) f(t) + s g(t)$. This is continuous because it's the sum and scaling of continuous functions. It's in $D$ because it's just going along the lines between $f(t)$ and $g(t)$ which by hypothesis are in $D$.

##### _example:_ convex

Convex regions (the regions that contain the straight lines between any two points) have that any two loops are homotopic. A special case of this is that all loops on $\mathbb{R}^{2}$ itself are homotopic.