---
tags:
- math-176/13
- math-176/14
- alg-geo
---

The idea of projective space is to consider numbers in a field only upto ratio, [[Algebraic Geometry --- math-176/notes/Pythagorean triples and conic sections#_proposition _ the character of a Pythagorean triple|just like we did with Pythagorean triples]]. For this, fix a field $F$.

However, first, we have to think about affine space. This is just the $n$-dimensional vector space over that field, but we don't want to think about any dependence on $F$ — we strip away the addition and the origin and just think about $n$-tuples.

##### _definition:_ affine space

For each $n \in \mathbb{N}$, the affine $n$-space over $F$ is
$$
\mathbb{A}^n(F) = \{ (x_{1}, \dots, x_{n}) \mid x_{i} \in F \}.
$$
Note, one can think of $\mathbb{A}^n$ as a [[functor]] that takes fields and spits out affine spaces.


##### _proposition:_ the projective equivalence relation on affine space

Write $G  = \mathbb{A}^{n + 1} \setminus \{ (0, \dots, 0) \}$. Then the relation $\sim$ by $(x_{1}, \dots, x_{n + 1}) \sim (y_{1}, \dots, y_{n + 1})$ if $(x_{1}, \dots x_{n + 1} ) = (\lambda y_{1}, \dots, \lambda y_{n+ 1})$ is an equivalence relation on $G$.

###### _proof sketch:_

Reflexivity is easy. For symmetry you just need to note that $\lambda \neq 0$ since neither of the points is $(0, \dots, 0)$. Transitivity is also easy (note that associativity of multiplication is important though).

##### _definition:_ projective space

For each $n \in \mathbb{N}$, the projective $n$-space over $F$ is
$$
\mathbb{P}^n(F) = \frac{\mathbb{A}^{n + 1}(F) \setminus \{ (0, \dots, 0) \}}{\sim}
$$
for the equivalence relation $\sim$ from the previous operation.

We write $(x_{1} : \dots : x_{n + 1})$ for the equivalence class of $(x_{1}, \dots, x_{n + 1})$, however, we often write $(x_{1} : \dots : x_{n} : x_{0})$ for reasons that will become obvious almost immediately

Note that by this equivalence relation, if $x_{0}$ is non-zero we can scale down by it to get
$$
(x_{1} : \dots : x_{n}  : x_{0}) = \left( \frac{x_{1}}{x_{0}} : \dots : \frac{x_{n}}{x_{0}} : x_{0} \right)
$$
Else, we can divide by one of the other coordinates. This is particularly nice in the case of the line $\mathbb{A}(F)$ because the only other coordinate is $\mathbb{P}(F) = \{ (x : 1) \mid x \in F \} \cup \{ (1 : 0) \}$. Morally, what we're trying to do is compactify $\mathbb{A}(F)$ by adding the point at infinity and making everything a circle $\mathbb{P}(F) = \mathbb{A}(F) \cup \{ \infty \}$. Let's do this in the case that it's very clear —

##### _proposition:_ the circle and the projective line

If $F$ is $\mathbb{Q}$ or $\mathbb{R}$, and we have $r \in F$ with $r > 0$. Then the circle $S^1(F) = \{ (x, y) \in \mathbb{A}(F) \mid x^{2} + y^{2} = r^{2} \}$. Then there is a bijection
$$
\begin{split}
\phi & : \mathbb{P}^1(F) \to S^1(F) \\
 & : (x_{1} : x_{0}) \mapsto \left( \frac{2 x_{1} x_{0}}{x_{1}^{2} + x_{0}^{2}} r, \frac{x_{1}^{2} - x_{0}^{2}}{x_{1}^{2} + x_{0}^{2}} r \right) 
\end{split}
$$

###### _proposition:_

Doesn't that formula look familiar? It's exactly the formula for parameterising [[Algebraic Geometry --- math-176/notes/Pythagorean triples and conic sections#_proposition _ the character of a Pythagorean triple|Pythagorean triples and conic sections]]! This follows by exactly the same argument!

What we're doing here is the inverse of stereographic projection — draw a line between the north pole and a point, and then the point that the line intersects the real line is the point that we map the point on the sphere to.

We can do the same thing for $F = \mathbb{C}$ and the $2$-sphere $S^2(\mathbb{R}) = \{ (x, y, z) \in \mathbb{A}^3(\mathbb{R}) \mid x^{2} + y^{2} + z^{2} = r^{2} \}$.

We can do the same kind of case analysis on $\mathbb{P}^2(F)$. If $x_{0} \neq 0$, then we just get the points in the affine plane. If $x_{0} = 0$, we get points $(x_{1} : x_{2} : 0)$ such that $x_{1} = x_{2} = 0$ should not hold. That is, we have a copy of $\mathbb{P}^1(F)$. Thus, morally,
$$
\mathbb{P}^2(F) = \mathbb{A}^2(F) \cup \mathbb{P}^1(F) = \mathbb{A}^2(F) \cup \mathbb{A}^1(F) \cup \{ \infty \}.
$$
In some sense, we have, in projective space, an affine plane, a projective line at infinity, and that line has a point at infinity.