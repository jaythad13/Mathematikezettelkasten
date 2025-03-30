---
tags:
- math-147/15
- top
---

Let $X$ and $Y$ be topological spaces.

The topological notion of isomorphism is the same as the categorical notion of isomorphism (in the [[Basic category theory --- basic-cat/notes/Categories#_definition _ category|category]] where objects are topological spaces and the morphisms are continuous maps) —

##### _definition:_ homeomorphism

$X$ and $Y$ are homeomorphic if there is a homeomorphism between them — a [[Topology --- math-147/notes/Continuous functions#_definition _ continuity|continuous]] bijection $f : X \to Y$ with continuous inverse $f^{-1} : Y \to X$ (so that $f \circ f^{-1} = \operatorname{id}_{Y}$ and $f^{-1} \circ f = \operatorname{id}_{X}$).

In essence, a homeomorphism is a bijection of spaces that also induces a bijection of topologies. While continuous maps pull open and closed sets back to open and closed sets respectively, open and closed maps do the same in reverse.

##### _definition:_ open map, closed map

A function $f : X \to Y$ is an open map if $f^\text{img}(U)$ is open in $Y$ for every $U$ open in $X$.

A function $f : X \to Y$ is a closed map if $f^\text{img}(A)$ is closed in $Y$ for every $A$ closed in $Y$.

[[Topology --- math-147/notes/Continuous functions#_proposition _ equivalent definitions of continuity|Unlike with continuous maps]] these notions are not equivalent. However, they, and homeomorphism are equivalent when $f$ is continuous.

##### _proposition:_ homeomorphisms, closed bijections, and open bijections

If $f : X \to Y$ is continuous, the following are equivalent
1) $f$ is homeomorphism
2) $f$ is a closed bijection
3) $f$ is an open bijection

###### _proof:_

Suppose $f$ is a homeomorphism. This is equivalent to $f$ being a bijection and $f^{-1}$ being continuous. [[Topology --- math-147/notes/Continuous functions#_proposition _ equivalent definitions of continuity|This is equivalent to]] $f^{-1}$ having closed pre-images of closed sets. That is, $(f^{-1})^\text{pre}(A)$ is closed for every closed set $A \subseteq X$. It's a fact of set theory that $(f^{-1})^\text{pre}(A) = f^\text{img}(A)$ for each $A \subseteq X$ for a bijection $f$. Thus, $f^\text{img}(A)$ is closed in $Y$ for each closed $A \subseteq X$, which is exactly what it means for $f$ to be closed bijection. This is (1) $\iff$ (2).

The proof that (1) $\iff$ (3) follows similarly. Suppose $f$ is a homeomorphism. This is equivalent to $f$ being a bijection and $f^{-1}$ being continuous. [[Topology --- math-147/notes/Continuous functions#_proposition _ equivalent definitions of continuity|This is equivalent to]] $f^{-1}$ having open pre-images of open sets. That is, $(f^{-1})^\text{pre}(U)$ is closed for every open set $U \subseteq X$. It's a fact of set theory that $(f^{-1})^\text{pre}(U) = f^\text{img}(U)$ for each $U \subseteq X$ for a bijection $f$. Thus, $f^\text{img}(U)$ is closed in $Y$ for each closed $U \subseteq X$, which is exactly what it means for $f$ to be open bijection. This is (1) $\iff$ (2).

This equivalence allows us to construct homeomorphisms between spaces as long as we have 

##### _proposition:_ homeomorphisms between a compact and a Hausdorff space

If $f : X \to Y$ is a continuous bijection, $X$ is [[Topology --- math-147/notes/Compactness#_definition _ compact|compact]], and $Y$ is [[Topology --- math-147/notes/Separation properties#_definition _ Hausdorff spaces, $T_{2}$ spaces|Hausdorff]], then $f$ is a homeomorphism.

###### _proof sketch:_

Suppose $A \subseteq X$ is closed. Then $A$ [[Topology --- math-147/notes/Compactness#_proposition _ closed subspaces of compact spaces are compact|is compact]]. Then $f^\text{img}(A)$ [[Topology --- math-147/notes/Compactness#_proposition _ compactness is preserved by continuous functions|is compact]]. But then since $Y$ is Hausdorff $f^\text{img}(A)$ [[Topology --- math-147/notes/Compactness#_proposition _ compact subsets of Hausdorff spaces are closed|is closed]].

##### _example:_ proving homeomorphisms using compactness results

It is a result of analysis that the Cantor set $C$ is in fact compact. It is also a fact that [[Topology --- math-147/notes/Separation properties#_proposition _ product of Hausdorff spaces|products of Hausdorff spaces are Hausdorff]]. Thus, we only need to show that the bijection
$$
\begin{align}
f & : C \to \prod_{n = 1}^\infty \{ 0, 2 \} \\
 & : x\mapsto x_{3}
\end{align}
$$
is continuous, to show that the Cantor set is homeomorphic to the infinite product of the two point discrete set. Here, $x_{3}$ is the ternary expansion of a real number $x$.