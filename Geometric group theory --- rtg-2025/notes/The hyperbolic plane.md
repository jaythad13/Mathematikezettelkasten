---
tags:
- ggt
- cx-geo
- rtg-2025
- bradley-zykoski/1
---

Recall the [[Introduction to Riemann Surfaces --- math-199DR/notes/Riemann surfaces#_example _ the Riemann sphere and the complex projective line|Riemann sphere as complex projective space]] 
$$
\mathbb{C} \mathbb{P}^1 = (\mathbb{C}^{2} \setminus \{ 0 \}) / \mathbb{C}^\times
$$
where we quotient by the action of $\mathbb{C}^\times$ by scalar multiplication. Note that it is the [[Topology --- math-147/attachments/exam/exam.pdf#page=1|one point compactification]] of $\mathbb{C}$, and also homeomorphic to the $2$-sphere $S^{2}$ (by stereographic projection).

### Group actions on $\mathbb{C} \mathbb{P}^1$ and $\mathbb{H}^{2}$

Hyperbolic geometry occurs on a subset of $\mathbb{C} \mathbb{P}^1$. We will build it from the perspective of Felix Klein — by defining what group we want to [[Geometric group theory --- rtg-2025/notes/Isometric actions|act isometrically]] on it.

##### _definition:_ Möbius transformation

The group action $\mathrm{GL}_{2}(\mathbb{C}) \circlearrowright \mathbb{C}\mathbb{P}^1$ by
$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix} (z : w) = \left( {az + bw} : {cz + dw} \right)
$$
is called the action by Möbius transformations. Each function $(z : w) \mapsto A \cdot (z : w)$ is called a Möbius transformation.

Note that $\mathbb{C}^* \le \mathrm{GL}_{2}(\mathbb{C})$ is part of the [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ kernel, effective action|kernel]] of the group actions, so the action descends to an action of the projective general linear group $\mathrm{PGL}_{2}(\mathbb{C})$ (which incidentally is the same as $\mathrm{PSL}_{2}(\mathbb{C})$).

It's an interesting exercise to verify that the action of $\mathrm{PGL}_{2}(\mathbb{C})$ on $\mathbb{C} \mathbb{P}^1$ is strictly $3$-transitive — for each pair of triples $(z_{1}, z_{2}, z_{3}), (w_{1}, w_{2}, w_{3})$, there is a unique $A \in \mathrm{PGL}_{2}(\mathbb{C})$ so that $A z_{j} = w_{j}$ for each $j$.

##### _definition:_ upper half-plane, hyperbolic plane

The upper half-plane or hyperbolic plane is the subset of complex projective space
$$
\mathbb{H}^{2} = \{ (z : w) \in \mathbb{C} \mathbb{P}^1 \mid w = 1 \text{ and } \operatorname{Im} z > 0 \}.
$$

In the $S^{2}$ model of the complex projective line, this is the "strict upper hemisphere". It doesn't include its (topological) boundary, $\partial \mathbb{H}^{2} = \mathbb{R} \mathbb{P}^1$ which is the equator.

With this definition, we're naturally bound to ask under which Möbius transformations $f$, the hyperbolic plane $\mathbb{H}^{2}$ is invariant. 

##### _theorem:_ Möbius transformations acting on hyperbolic plane are $\mathrm{PSL}_{2}(\mathbb{R})$

The group of Möbius transformations under which $\mathbb{H}^{2}$ is invariant is isomorphic to $\mathrm{PSL}_{2}(\mathbb R)$

###### _proof sketch:_

Note that if $f$ is such a Möbius transformation, then by continuity $f$ must also fix the topological boundary. That is $f^\text{img}(\mathbb{R} \mathbb{P}^1) = \mathbb{R} \mathbb{P}^1$. Thus, any $A \in \mathrm{GL}_{2}(\mathbb{C})$ representing $f$ sends $\mathbb{R}^{2}$ to $\lambda \mathbb{R}^{2}$ for some $\lambda \in \mathbb{C}^\times$. Since any $(1 / \lambda) A$ also represents $f$, we can choose $\lambda = 1$ without loss of generality. Then $f$ must be 

However, invariance of $\mathbb{R} \mathbb{P}^1$ is not sufficient ($\mathbb{R} \mathbb{P}^1$ is invariant under flipping the Riemann sphere as well). Thus, among these real matrices, we also need to restrict to those with
$$
0 < \operatorname{Im} (f(z)) = \operatorname{Im} \left( \frac{az + b}{cz + d} \right).
$$
It's an easy exercise to verify that this forces the matrix to have positive determinant. Again, by scaling, without loss of generality, we can assume that the determinant is $1$ (recall that for $2$-by-$2$ matrices, $\det \lambda A = \lambda^{2} \det A$). Finally, again by scaling we identify $A$ and $-A$.

We can't prove this right now, but these are in fact all the automorphisms of $\mathbb{H}^{2}$

### The geometry of the hyperbolic plane

We can describe the geometry of this group action by its action on lines and circles.

##### _proposition:_ parameterising lines and circles in the complex plane

Suppose $S \subseteq \mathbb{C}$ is a circle or a line. Then
$$
S = \{ z \in \mathbb{C} \mid \alpha \lvert z \rvert^{2} + \beta z + \bar{\beta} \overline{z} + \gamma = 0 \}
$$
for some $\alpha, \gamma \in \mathbb{R}$ and $\beta \in \mathbb{C}$. 

Further, $S$ is a line if $\alpha = 0$ and a circle otherwise and $S$ intersects the real line $\mathbb{R} \subseteq \mathbb{C}$ orthogonally if and only if $\beta \in \mathbb{R}$.

##### _corollary:_ Möbius transforms act on circles and lines

Let $\mathcal{S}$ be the set of all lines and circles in $\mathbb{C}$. Let $\mathcal{S}_{\mathbb{R}}$ be those that intersect $\mathbb{R}$ orthogonally. Then if $A \in \mathrm{PGL}_{2}(\mathbb{C})$, $A \cdot \mathcal{S} = \mathcal{S}$. If $A \in \mathrm{PSL}_{2}(\mathbb{R})$, $A \cdot \mathcal{S}_{\mathbb{R}} = \mathcal{S}_{\mathbb{R}}$.