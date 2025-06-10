---
tags:
- lin-alg
- ladr/5A
---

### Operators and invariant subspaces

So far with [[Linear maps|linear maps]] we've been concerned with maps between arbitrary vector spaces. However, often, maps of interest are maps from a vector space to itself. These are also of independent interest because they tell us about the vector space, and have nice algebraic properties as a set (they form a [[Abstract Algebra I --- math-171/notes/Rings#_definition _ rings|ring]], and in fact, an algebra).

##### _definition:_ operator

A linear map from a vector space to itself is called an operator.

The space of operators on a vector space $V$ is denoted $\mathcal{L}(V)$.

If we have $T \in \mathcal{L}(V)$ and a direct sum decomposition $V = V_{1} \oplus \dots \oplus V_{n}$, we could understand $T$ as a whole by understanding the restrictions $T_{\mid V_{k}}$ to smaller vector spaces. However, we would need to have $\operatorname{img} T_{\mid V_{k}} \subseteq V_{k}$ — we would need the restrictions also to be operators. Thus, of interest are such [[Linear subspaces|subspaces]].

##### _definition:_ invariant subspace

Given $T \in \mathcal{L}(V)$, a linear subspace $U \subseteq V$ is invariant under $T$ if $Tu \in U$ for each $u \in U$.

##### _example:_ four fundamentally invariant subspaces

For any $T \in \mathcal{L}(V)$, the subspaces $0$, $V$, $\ker T$ and $\operatorname{img} T$ are invariant under $T$ for obvious reasons.

Thus, when $T$ is not invertible, it admits a non-trivial invariant subspace decomposition. However, it isn't immediately clear that this is always true. [[Linear algebra done right --- ladr/notes/Existence of eigenvalues and invariant subspaces|We will see later]] that for a complex vector space (more generally, a vector space over a complete field) with $\dim V > 1$, or a real vector space with $\dim V > 2$, there is a always a non-trivial decomposition.

The simplest case of invariant subspaces is obviously those of dimension $1$, which we will study most. For a $1$-dimensional invariant subspace of $T \in \mathcal{L}(V)$, there must be some non-zero $v \in V$ with $Tv \in \operatorname{span} v$, implying $Tv = \lambda v$ with $\lambda \in \mathbb{F}$.

##### _example:_ a concrete $1$-dimensional invariant subspace

Consider $T \in \mathcal{L}(\mathbb{C}^{2})$ with matrix
$$
\begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}
$$
with respect to the standard basis. Since $T(i, 1) = (-1, i) = i(i, 1)$, we have that $\operatorname{span} (i, 1)$ is invariant under $T$.

### Eigenvalues and eigenvectors

From now on let, $T$ be an operator on a vector space $V$.

##### _definition:_ eigenvalue, eigenvector

A non-zero $v \in V$ is an eigenvector if $Tv = \lambda v$ for some $\lambda \in \mathbb{C}$. 

A scalar $\lambda \in \mathbb{F}$ is an eigenvalue of $T$ if there is an eigenvector $v \in V$ with $Tv = \lambda v$.

##### _proposition:_ equivalent conditions 

Given some $\lambda \in \mathbb{F}$, the following are equivalent.
1) $\lambda$ is an eigenvalue of $T$
2) $T - \lambda I$ is not injective
3) $T - \lambda I$ is not surjective
4) $T - \lambda I$ is not invertible

###### _proof:_

(1) and (2) are equivalent because $Tv = \lambda v$ for non-zero $v \in V$ is equivalent to $(T - \lambda I) v = 0$ for non-zero $v \in V$.

(2), (3), and (4) are equivalent by the [[rank-nullity theorem]].

##### _example:_ eigenstuff is field-dependent

The existence of an eigenvector is dependent on the choice of field the vector space is considered to be over. While the [[#_example _ a concrete $1$-dimensional invariant subspace|example we considered previously]] of $T \in \mathcal{L}(\mathbb{C}^{2})$ with matrix
$$
\begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}
$$
has eigenvalues $i$ and $-i$, the same matrix over $\mathbb{R}^{2}$ has no eigenvalues since it can be understood geometrically as a $\pi / 2$ rotation about the origin

##### _proposition:_ eigenvectors from distinct eigenvalues are linearly independent

Suppose $v_{1}, \dots, v_{n}$ are eigenvectors of $T$ corresponding to distinct eigenvalues $\lambda_{1}, \dots, \lambda_{n}$. Then $v_{1}, \dots, v_{n}$ are linearly independent.

###### _proof:_

Suppose $v_{1}, \dots, v_{m}$ is a minimal list of linearly dependent eigenvectors of $T$ with distinct eigenvalues. Let $a_{1}, \dots, a_{m}$ be some coefficients (all non-zero, since $m$ is minimal) such that
$$
a_{1} v_{1} + \dots + a_{m} v_{m} = 0.
$$
Then, applying $T - \lambda_{m} I$ to both sides of the equation, we get
$$
a_{1} (\lambda_{1} - \lambda_{m}) v_{1} + \dots + a_{m - 1}(\lambda_{m - 1} - \lambda_{m}) v_{m - 1} = 0.
$$
The $a_{k} (\lambda_{k} - \lambda_{m})$ are all non-zero since $\lambda_{k} \neq \lambda_{m}$ for $k \neq m$. Thus, $v_{1}, \dots, v_{m - 1}$ is a smaller list of linearly dependent eigenvectors of $T$ with distinct eigenvalues, yielding a contradiction.

##### _corollary:_ bounding the number of distinct eigenvalues

If $V$ is finite-dimensional, then each operator on $V$ has at most $\dim V$ eigenvalues.