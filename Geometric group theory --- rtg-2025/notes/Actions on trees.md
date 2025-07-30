---
tags:
- ggt
- alg
- graph
---

In this note, we will prove that significant group theoretic information can be obtained just from actions on trees. In particular, we obtain freeness results and decompositions of groups into [[Geometric group theory --- rtg-2025/notes/Free products and amalgamation|free products and amalgamations]].

However, for a theorem giving group theoretic information from actions on trees to be useful, we must have natural actions on trees. One example is that of [[Geometric group theory --- rtg-2025/notes/The Farey tree and congruence subgroups|the special linear group and the Farey tree]]. Our results will show that principal congruence subgroups of sufficiently high level are free. In particular,

![[Geometric group theory --- rtg-2025/notes/The Farey tree and congruence subgroups#_theorem _ free congruence subgroups|The special linear group and the Farey tree]]

and that

### Free actions on trees

If an action on a tree is free, then the group must be free. This has, as a corollary, a highly non-trivial theorem about subgroups of free groups.

##### _theorem:_ free actions on trees come from free groups

If a group $G$ [[Geometric group theory --- rtg-2025/notes/Graph actions and Cayley graphs#_definition _ graph action|acts]] [[Abstract algebra --- math-171/notes/Group actions#_definition _ stabiliser, free|freely]] on a [[Superdiscrete --- math-55A/notes/Special graphs#_definition _ tree|tree]], it is a [[Geometric group theory --- rtg-2025/notes/Free groups and presentations#_definition _ free group|free group]].

##### _theorem:_ Nielsen-Shreier theorem

Any [[Abstract algebra --- math-171/notes/Subgroups#_definition _ subgroup, $ le$|subgroup]] of a free group is a free group.

### Non-free actions on trees

We can prove weaker results even when the action of a group is not completely free. In particular, if the action is free on edges, but has some non-trivial [[Abstract algebra --- math-171/notes/Group actions#_definition _ stabiliser, free|stabiliser]] for some vertices, we an get an expression for the group as a free product.

##### _theorem:_ edge-free actions on trees come from free products

Suppose a group $G$ acts freely and transitively on the edges of a tree without inversions. Then if the two endpoints of an edge have stabilisers $H_{1}$ and $H_{2}$, $G$ is isomorphic to their [[Geometric group theory --- rtg-2025/notes/Free products and amalgamation#_definition _ free product, coproduct of groups|free product]] $H_{1} * H_{2}$.

Even when the action isn't free on edges, transitivity suffices.

##### _theorem:_ edge-transitive actions on trees come from amalgamations

Suppose a group $G$ acts transitively on the edges of a tree without inversions. Suppose the two endpoints of an edge have stabilisers $H_{1}$ and $H_{2}$ and the edge has stabiliser $K$. Then $G$ is isomorphic to their [[Geometric group theory --- rtg-2025/notes/Free products and amalgamation#_definition _ free product with amalgamation, cofibred coproduct of groups|amalgamation]] $H_{1} *_{K} H_{2}$ along the obvious inclusions induced by $K \le H_{i}$.