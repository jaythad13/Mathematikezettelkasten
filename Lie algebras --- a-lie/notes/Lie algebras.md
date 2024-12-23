---
tags:
- a-lie/1
- alg
- diff-geo
- self-study
---

##### _definition:_ Lie algebra

A Lie algebra $L$ is a [[Linear algebra done right --- ladr/notes/Vector spaces|vector space]] with a Lie bracket — a bilinear map
$$
[\cdot, \cdot] : L \times L \to L
$$
that satisfies 
$$
[x, x] = 0
$$
and the Jacobi identity
$$
[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0.
$$

See that the notation $[\cdot, \cdot]$ imitates that of the [[Abstract Algebra I --- math-171/attachments/homework/hw 12/hw 12.pdf|commutator]] in group theory and ring theory.

The Jacobi identity might be best expressed as saying that the operator $[x, \cdot]$ satisfies the Leibniz rule —
$$
[x, [y, z]] = [[x, y], z] + [y, [x, z]].
$$


In fields not of [[Algebraic Geometry --- math-176/notes/Abstract algebra review#_definition _ characteristic|characteristic]] $2$, the Lie bracket is really antisymmetric

##### _proposition:_ Lie brackets are usually antisymmetric

If $V$ is a vector space over $F$ not of characteristic $2$, then a bilinear map $[\cdot, \cdot]$ on $V$ satisfies
$$
[v, v] = 0
$$
for all $v \in V$ if and only if
$$
[v, w] = -[w, v]
$$
for all $v, w \in V$.

###### _proof:_

Suppose we have $[v, v] = 0$ for all $v$. Then $[v + w, v + w] = 0$. Since
$$
\begin{align}
[v + w, v + w] & = [v, v] + [v, w] + [w, v] + [w, w] \\
 & = [v, w] + [w, v] \\
 & = 0
\end{align}
$$
we have $[v, w] = -[w, v]$.

Now suppose $[v, w] = -[w, v]$ for all $v, w$. Then clearly $[v, v] = -[v, v]$. Since $\operatorname{char} F \neq 2$, this implies $[v, v] = 0$.

Note over fields of characteristic $2$, we can have $[v, v] = 1$, and thus, $[v, v] = -[v, v]$ without $[v, v] = 0$.

##### _definition:_ abelian Lie algebra

We say a Lie algebra is abelian if the bracket is trivial (sends everything to zero).

Many matrix algebras are Lie algebras with the commutator product.

##### _example:_ $\mathfrak{gl}_{n}(F)$

The general linear Lie algebra of order $n$ over $F$ is just all $n$-by-$n$ matrices over $F$ with the usual addition and the commutator Lie bracket
$$
[A, B] = AB - BA.
$$
This is clearly, antisymmetric, and thus, alternating. Using the associativity of matrix multiplication, the Jacobi identity just falls out
$$
\begin{align}
[A, [B, C]] + [B, [C, A]] + [C, [A, B]] & = [A, BC - CB] + [B, CA - AC] + [C, AB - BA] \\
 & = ABC - ACB - BCA + CBA \\
 & + BCA - BAC - CAB + ACB \\
 & + CAB - CBA - ABC + BAC \\
 & = 0.
\end{align}
$$

##### _example:_ $\mathfrak{sl}_{2}(\mathbb{C})$

The special linear Lie algebra of order $2$ over $\mathbb{C}$ is the vector space of traceless $2$-by-$2$ matrices over $\mathbb{C}$ with the same commutator Lie bracket (in fact, it's a [[Lie algebras --- a-lie/notes/Subalgebras, ideals, and quotients#|subalgebra]] of $\mathfrak{gl}_{2}(\mathbb{C})$).

Note that $\mathfrak{sl}_{2}(\mathbb{C})$ has basis $e, f, h$ where
$$
e = \begin{pmatrix}
0 & 1 \\
0 & 0
\end{pmatrix} \quad
f = \begin{pmatrix}
0 & 0 \\
1 & 0
\end{pmatrix} \quad
h = \begin{pmatrix}
1 & 0 \\
0 & -1
\end{pmatrix}
$$
so we can verify it's a Lie algebra by just verifying that the Lie bracket keeps the products $[e, f], [f, h], [h, e]$ all in $\mathfrak{sl}_{2}(\mathbb{C})$.

### Lie groups and Lie algebras

Really, Lie algebras arise from (differential) geometric objects called Lie groups.

##### _(rough) definition:_ Lie group

A Lie group is a manifold that is also a group with a group operation that is compatible with the smooth structure.

Since algebras are "linearisations" of groups and tangent spaces are "linearisations" of manifolds, the tangent space (at the identity) of a Lie group is its corresponding Lie algebra.

##### _(rough) definition:_ Lie algebra of a Lie group

The Lie algebra corresponding to a Lie group $G$ is $\mathfrak{g} = \mathrm{T}_{e}G$, the tangent space of $G$ at the identity.

##### _example:_ $\mathfrak{sl}_{2}(\mathbb{C})$ and $\operatorname{SL}_{2}(\mathbb{C})$

$\operatorname{SL}_{2}(\mathbb{C})$ is the set of all $2$-by-$2$ matrices with determinant $1$. Since the determinant is a polynomial, we can think of this as the zero locus of a polynomial on $\mathbb{C}^4$, and thus, a manifold.

To calculate the tangent space, we want to classify the derivatives of all curves $\gamma : \mathbb{R} \to \operatorname{SL}_{2}(\mathbb{C})$ with $\gamma(0) = I$, the identity matrix. Really, by [[Calculus --- spivak/notes/Differentiability theorems#_theorem _ the projection principle holds for differentiability|the projection principle]] we can split this curve into four differentiable curves $a, b, c, d : \mathbb{R} \to \mathbb{C}$ satisfying
$$
a(t) d(t) - b(t) c(t) = 1
$$
everywhere, and
$$
\begin{pmatrix}
a(0) & b(0) \\
c(0) & d(0)
\end{pmatrix} = \begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}.
$$

Thus,
$$
a'(t) d(t) + a(t) d'(t) - b'(t) c(t) - b(t) c'(t) = 0
$$
which we can evaluate at $t = 0$ to get
$$
a'(0) + d'(0) = 0.
$$

That is,
$$
\gamma'(0) = \begin{pmatrix}
a'(0) & b'(0) \\
c'(0) & d'(0)
\end{pmatrix}
$$
is a traceless matrix. Now we have that $T_{e}\operatorname{SL}_{2}(\mathbb{C}) \subset \mathfrak{sl}_{2}(\mathbb{C})$. However, since these have the same dimension (complex dimension $3$), they have to be the same vector space.