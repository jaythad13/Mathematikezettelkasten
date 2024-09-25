---
tags:
- math-176/13
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

Write $G  = \mathbb{A}^{n + 1} \setminus \{ (0, \dots, 0) \}$. Then the relation $\sim$ by $(x_{1}, \dots, x_{n + 1}) \sim (y_{1}, \dots, y_{n + 1})$ if $(x_{1}, \dots x_{ + 1} ) = (\lambda y_{1}, \dots, \lambda y_{n+ 1})$ is an equivalence relation on $G$.

###### _proof sketch:_

Reflexivity is easy. For symmetry you just need to note that $\lambda \neq 0$ since neither of the points is $(0, \dots, 0)$. Transitivity is also easy (note that associativity of multiplication is important though).

##### _definition:_ projective space

For each $n \in \mathbb{N}$, the projective $n$-space over $F$ is
$$
\mathbb{P}^n(F) = \frac{\mathbb{A}^{n + 1}(F) \setminus \{ (0, \dots, 0) \}}{\sim}
$$
for the equivalence relation $\sim$ from the previous operation.

We write $(x_{1} : \dots : x_{n + 1})$ for the equivalence class of $(x_{1}, \dots, x_{n + 1})$.