---
tags:
- diff-geo
- math-142/22
- math-142/23
---

We've seen already that and [[Curves and surfaces --- math-142/notes/Proper Euclidean motions#_proposition _ the tangent maps of isometries behave like isometries|the tangent maps of proper Euclidean motions preserve dot products]]. What about cross products?

It's almost trivial to see that translations do. Thus, we need to investigate orthogonal transformations.

### Orthogonal transformations

##### _proposition:_ orthogonal transformations really are orthogonal

An [[Curves and surfaces --- math-142/notes/Proper Euclidean motions#_proposition, definition _ orthogonal transformations, $O_{n}$,|"orthogonal transformation"]] as we defined it is really an [[Isometries|isometry]] in the sense of linear algebra.

###### _proof:_

See [[Linear Algebra Done Right.pdf#page=273|Linear Algebra Done Right]].

##### _lemma:_ orthogonal transformations preserve cross products of basis vectors upto sign
##### _proposition:_ orthogonal transformations preserve cross products upto sign

### The consequences for proper Euclidean motions

Since the [[Curves and surfaces --- math-142/notes/Proper Euclidean motions#_proposition _ the tangent maps of isometries behave like isometries|tangent map is basically just the orthogonal part]], this leads us naturally to defining the sign of a proper Euclidean motion.

##### _definition:_ sign of a proper Euclidean motion, orientation preserving

For a proper Euclidean motion, $F$ with $F = T \circ C$ where $C$ is orthogonal and $T$ is a translation, the sign of $F$ is
$$
\operatorname{sgn} F = \det C.
$$

##### _proposition:_ (tangent maps of) proper Euclidean motions preserve cross products upto sign

For any proper Euclidean motion $F$, its tangent map $F_{*}$ preserves cross products upto sign:
$$
F_{*}([\mathbf{v}, \mathbf{p}] \times [\mathbf{w}, \mathbf{p}]) = \operatorname{sgn} (F) \, F_{*}([\mathbf{v}, \mathbf{p}]) \times F_{*}([\mathbf{w}, \mathbf{p}]).
$$

##### _corollary:_ (tangent maps of) proper Euclidean motions preserve scalar triple products up to sign

For any proper Euclidean motion $F$, its tangent map $F_{*}$ preserves scalar triple products upto sign:
$$
F_{*}([\mathbf{u}, \mathbf{p}] \cdot [\mathbf{v}, \mathbf{p}] \times [\mathbf{w}, \mathbf{p}]) = \operatorname{sgn} (F) \, F_{*}([\mathbf{u}, \mathbf{p}]) \cdot F_{*}([\mathbf{v}, \mathbf{p}]) \times F_{*}([\mathbf{w}, \mathbf{p}]).
$$

Note how we could also write this as having to "reverse the cross product" if $\operatorname{sgn} F = -1$. This motivates the following definition.

##### _definition:_ orientation preserving, orientation reversing

We say $F$ is orientation preserving if $\operatorname{sgn} F = 1$, and orientation reversing otherwise.

##### _examples:_ orientation preserving maps

1) Translations are obviously orientation preserving — their orthogonal part is the identity map.
2) Rotations about the $z$ axis have matrices of the form 
$$
\begin{bmatrix}
\cos \vartheta & - \sin \vartheta & 0 \\
\sin \vartheta & \cos\vartheta  & 0 \\
0 & 0 & 1
\end{bmatrix}
$$
	for a rotation of angle $\vartheta$. Thus, expanding along the bottom row, they have determinant $1$ and are orientation preserving.
3) In fact, rotations about any line are orientation preserving — for a line given by $\operatorname{span} \mathbf{v}$, the map 
$$
C : \mathbf{p} \mapsto \cos \vartheta \frac{\mathbf{v} \times \mathbf{p}}{\lVert \mathbf{v} \rVert ^2} \times \mathbf{v} + \sin\vartheta \frac{\mathbf{v}}{\lVert \mathbf{v} \rVert } \times \mathbf{p} + \frac{\mathbf{p} \cdot \mathbf{v}}{\lVert \mathbf{v} \rVert ^2} \mathbf{v}
$$
	is the orientation preserving rotation by angle $\vartheta$ about the line.

##### _example:_ orientation reversing maps

Any reflection through any plane is orientation reversing. That is, for the plane $\operatorname{span}(\mathbf{n})^\perp$, the map by
$$
C : \mathbf{p} \mapsto \mathbf{p} - 2 \frac{\mathbf{p} \cdot \mathbf{n}}{\lVert \mathbf{n} \rVert ^2} \, \mathbf{n}
$$
is orthogonal and orientation reversing