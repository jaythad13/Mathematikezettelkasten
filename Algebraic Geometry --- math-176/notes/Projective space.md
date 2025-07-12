---
tags:
- math-176/13
- math-176/14
- math-176/15
- alg-geo
---

The idea of projective space is to consider numbers in a field only upto ratio, [[Algebraic Geometry --- math-176/notes/Pythagorean triples and conic sections#_proposition _ the character of a Pythagorean triple|just like we did with Pythagorean triples]]. For this, fix a field $F$.

However, first, we have to think about affine space. This is just the $n$-dimensional vector space over that field, but we don't want to think about any dependence on $F$ — we strip away the addition and the origin and just think about $n$-tuples.

##### _definition:_ affine space

For each $n \in \mathbb{N}$, the affine $n$-space over $F$ is
$$
\mathbb{A}^n(F) = \{ (x_{1}, \dots, x_{n}) \mid x_{i} \in F \}.
$$
Note, one can think of $\mathbb{A}^n$ as a [[Algebraic geometry --- rising-sea/notes/Functors and natural transformations|functor]] that takes fields and spits out affine spaces.


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

##### _proposition:_ the sphere and the complex projective plane

There is a bijection
$$
\begin{split}
\phi & : \mathbb{P}^1(\mathbb{C}) \to S^2(\mathbb{R}) \\
 & : z \mapsto \left( \frac{\operatorname{Re} z}{\lvert z \rvert ^{2} + 1}, \frac{2 \operatorname{Im} z}{\lvert z \rvert ^{2} + 1}, \frac{\lvert z \rvert ^{2} - 1}{\lvert z \rvert ^{2} + 1} \right) 
\end{split}
$$

We can do the same kind of case analysis on $\mathbb{P}^2(F)$. If $x_{0} \neq 0$, then we just get the points in the affine plane. If $x_{0} = 0$, we get points $(x_{1} : x_{2} : 0)$ such that $x_{1} = x_{2} = 0$ should not hold. That is, we have a copy of $\mathbb{P}^1(F)$. Thus, morally,
$$
\mathbb{P}^2(F) = \mathbb{A}^2(F) \cup \mathbb{P}^1(F) = \mathbb{A}^2(F) \cup \mathbb{A}^1(F) \cup \{ \infty \}.
$$
In some sense, we have, in projective space, an affine plane, a projective line at infinity, and that line has a point at infinity.

To understand the geometry of $\mathbb{P}^2(F)$, we really need to understand lines in $\mathbb{P}^2(F)$. That is, we need to understand projective lines

### Projective lines

We already know what an affine line is —

##### _definition:_ affine line

An affine line $L$ in $\mathbb{A}^2(F)$ is a set of the form
$$
L = \{ (x, y) \mid a x + b y + c = 0 \}
$$


To get a projective line, we just substitute $x = \frac{x_{1}}{x_{0}}$ and $y = \frac{x_{2}}{x_{0}}$. That is,

##### _definition:_ projective line

A projective line $L$ in $\mathbb{P}^2(F)$ is a set
$$
L = \{ (x_{1} : x_{2} : x_{0}) \mid a x_{1} + b x_{2} + c x_{0} = 0 \}
$$

##### _example:_ projective line

The line at infinity, $\{ (x_{1} : x_{2} : x_{0}) \mid x_{0} = 0 \}$ is the projective line at infinity. It's a projective line!

Because of the points and this line at infinity, the following remarkable proposition holds for all projective lines!

##### _proposition:_ projective lines always intersect

1) Two distinct projective lines always intersect at unique projective point. 
2) Given two projective points, there is a unique line that goes through them.

###### _proof:_

For $L_{1} = \{ (x_{1} : x_{2} : x_{0}) \mid a_{1} x_{1} + b_{1} x_{2} + c_{1} x_{0} = 0 \}$ and $L_{2} = \{ (x_{1} : x_{2} : x_{0}) \mid a_{2} x_{1} + b_{2} x_{2} + x_{1} x_{0} \}$, consider
$$
P = \left( \begin{vmatrix}
b_{1} & c_{1} \\
b_{2} & c_{2}
\end{vmatrix} : \begin{vmatrix}
c_{1} & a_{1} \\
c_{2} & a_{2}
\end{vmatrix} : \begin{vmatrix}
a_{1} & b_{1} \\
a_{2} & b_{2}
\end{vmatrix}\right).
$$
Then evaluating the equations of both $L_{1}$ and $L_{2}$ look like taking determinants that have two columns that are the same, and so the determinants are $0$. $P = (0 :0 : 0)$ if and only if all the points are $(a_{1} : b_{1} : c_{1}) = \lambda (a_{2} : b_{2} : c_{2})$, and thus, the lines are the same, and not parallel.

To prove the second claim, consider $P_{1} = (a_{1} : b_{1} : c_{1})$ and $P_{2} = (a_{2} : b_{2} : c_{2})$. By duality, the line defined by $P$,
$$
L = \begin{vmatrix}
b_{1} & c_{1} \\
b_{2} & c_{2}
\end{vmatrix} x_{1} +  \begin{vmatrix}
c_{1} & a_{1} \\
c_{2} & a_{2}
\end{vmatrix} x_{2} +  \begin{vmatrix}
a_{1} & b_{1} \\
a_{2} & b_{2}
\end{vmatrix} x_{0}.
$$
contains both $P_{1}$ and $P_{2}$. Since any two lines intersect at a unique point, no other line can contain both $P_{1}$ and $P_{2}$.

This gives us an idea of what is happening, but still not a picture. Unfortunately, this is the best we can do — there are subtle issues that prevent us from having a nice story like $\mathbb{P}^1(\mathbb{R}) \cong S^1(\mathbb{R})$ and $\mathbb{P}^1(\mathbb{C}) \cong S^2(\mathbb{R})$ for $\mathbb{P}^2(F)$.

$\mathbb{P}^2(\mathbb{R}) = \mathbb{A}^2(\mathbb{R}) \cup S^1(\mathbb{R})$ is a compact non-orientable surface! It's an affine plane with a sphere somewhere at infinity, which is really hard to visualise. Reasonably, $\mathbb{P}^2(\mathbb{C}) = \mathbb{A}^4(\mathbb{R}) \cup S^2(\mathbb{R})$ is even harder to see. Note that the affine parts of $\mathbb{P}^2(\mathbb{R})$ and $\mathbb{P}^1(\mathbb{C})$ are the same, but the behaviour at infinity is different — everything in $\mathbb{P}^1(\mathbb{C})$ glues to form a sphere, while $\mathbb{P}^2(\mathbb{R})$ has to glue everything to get a sphere.

Our goal in this class is going to be to generalise a line $L$ inside $\mathbb{P}^2$ to a [[Algebraic Geometry --- math-176/notes/Non-singular projective varieties|variety]] inside $\mathbb{P}^n$.