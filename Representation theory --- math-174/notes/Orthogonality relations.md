---
tags:
- rep-th
- math-174/6
- math-174/7
---

Let $G$ be a finite group. For this note, we always work over $\mathbb{C}$.

The complex representations carry a lot of information about $G$ because $\mathbb{C}$ and $\mathbb{C}$-vector spaces have lots of additional structure. For one, we can think of $\mathbb{C}[G]$ itself as a $\mathbb{C}$-vector space with a Hermitian inner product on it (the usual one, with respect to the basis of elements of $G$). There are many ways to get elements of $\mathbb{C}[G]$ from a representation. Thinking about their orthogonality will be fruitful — for example, it will allow us to count irreducible representations of $G$.

### Matrix coefficients

Matrix coefficients are one way to get elements of $\mathbb{C}[G]$ from representations.

##### _definition:_ matrix coefficients

Suppose $\rho : G \to \mathrm{U}(V)$ is a unitary representation of $G$ with an associated $G$-invariant Hermitian inner product. The **matrix coefficients of $\rho$ for $v, w \in V$** is the element
$$
u_{v, w} = \sum_{g \in G} \left< \rho(g) w, v \right>_{V} g.
$$
---

Note, we can think of $u$ as a $\mathbb{C}[G]$-module homomorphism $V \otimes_{\mathbb{C}[G]} V \to \mathbb{C}[G]$.

They are so called because the coefficient of $g \in G$ in $u_{v_{i}, v_{j}}$ is $\left< \rho(g) v_{j}, v_{i} \right>$ which is just the $ij$th coefficient of the matrix of $\rho(g)$ with respect to the basis $v_{1}, \dots, v_{n}$.

We can prove some neat orthogonality results about matrix coefficients.

##### _theorem:_ all matrix coefficients of non-isomorphic irreps are orthogonal

Suppose $\rho : G \to \mathrm{U}(V)$ and $\sigma : G \to \mathrm{U}(W)$ are irreducible and non-isomorphic. For any $v_{1}, v_{2} \in V$ and $w_{1}, w_{2} \in W$, the corresponding matrix coefficients of $\rho$ and $\sigma$ are orthogonal in $\mathbb{C}[G]$.

###### _proof:_

For any $\mathbb{C}$-linear map $T : V \to W$ we can construct a $\mathbb{C}[G]$-linear map $T_{G} : V \to W$ by averaging
$$
T_{G} = \sum_{g \in G} \sigma(g^{-1}) T \rho(g).
$$
In particular, for any $h \in G$
$$
\begin{align}
\sigma(h) T_{G} & = \sum_{g \in G} \sigma(h g^{-1}) T \rho(g) \\
 & = \sum_{f = g h^{-1} \in G} \sigma(f^{-1}) T \rho(f) \rho(h) \\
 & = T_{G} \rho(h).
\end{align}
$$

Then
$$
\begin{align}
\left< u_{v_{1}, v_{2}}, u_{w_{1}, w_{2}} \right>_{\mathbb{C}[G]} & = \sum_{g \in G} \left< \rho(g) v_{2}, v_{1} \right>_{V} \overline{\left< \sigma(g) w_{2}, w_{1} \right>_{W} } \\
 & = \sum_{g \in G} \left< \left< \rho(g) v_{2}, v_{1} \right>_{V} w_{1}, \sigma(g) w_{2} \right>_{W} \\
\end{align}
$$
For any $v_{1} \in V, w_{1} \in W$ we have a linear map $T : V \to W$ by $v \mapsto \left< v, v_{1} \right>_{V} w_{1}$. Thus, 
$$
\begin{align}
\left< u_{v_{1}, v_{2}}, u_{w_{1}, w_{2}} \right>_{\mathbb{C}[G]} & = \sum_{g \in G} \left< T \rho(g) v_{2}, \sigma(g) w_{2} \right>_{W} \\ \\
 & = \sum_{g \in G} \left< \sigma(g^{-1}) T \rho(g) v_{2}, w_{2} \right> _{W} \\
 & = \left< T_{G} v_{2}, w_{2} \right>_{W} .
\end{align}
$$

By [[Representation theory --- math-174/notes/Irreducible modules#_lemma _ Schur's lemma|Schur's lemma]], $T_{G}$ must be zero (since $V$ and $W$ are not isomorphic $\mathbb{C}[G]$-modules). This is the desired result.

---

##### _theorem:_ matrix coefficients with respect to a basis are pairwise orthogonal

Suppose $\rho : G \to \mathrm{U}(V)$ is an irreducible unitary representation. Suppose $v_{1}, \dots, v_{n}$ is a basis of $V$. Write $u_{ij}$ for $u_{v_{i}, v_{j}}$. Then
$$
\left< u_{ij}, u_{k \ell} \right>_{\mathbb{C}[G]} = \frac{\# G}{\dim V} \delta_{ij} \delta_{k \ell}.
$$

###### _proof:_

Let $T : V \to V$ be the $\mathbb{C}$-linear map $v \mapsto \left< v, v_{1} \right>_{V} v_{3}$ as previously. $T_{G} = \sum_{g \in G} \rho(g^{-1}) T \rho(g)$ is $\mathbb{C}[G]$-linear. We claim that $T_{G}$ is an isomorphism (and thus $\lambda \operatorname{id}_{V}$) if and only if $v_{1} = v_{3}$ and $v_{2} = v_{4}$.

Then
$$
\begin{align}
\left< u_{12}, u_{34} \right>_{\mathbb{C}[G]} & = \sum_{g \in G} \left< \rho(g) v_{2}, v_{1} \right>_{V} \overline{\left< \rho(g) v_{3}, v_{4} \right>_{V} } \\
 & = \sum_{g \in G} \left< \left< \rho(g) v_{2}, v_{1} \right>_{V} v_{3}, \rho(g) v_{4} \right>_{V} \\
 & = \left< T_{G} v_{2}, v_{4} \right>_{V}.
\end{align}
$$
If $v_{1} = v_{3}$ and $v_{2} = v_{4}$ implying $T_{G}$ is an isomorphism, then this is just $\lVert v_{2} \rVert_{V}$ scaled. Else, $T_{G}$ is not an isomorphism, and thus, by Schur's lemma, is $0$.


---

##### _definition:_ dual of a finite group

The **dual of a finite group** $G$ is $\widehat{G}$ is the set of isomorphism classes of irreducible representations of $G$.


---

##### _corollary:_ bounding the number of irreducible representations of a group

$$
\# \widehat{G} \leq \sum_{\rho, V \in \widehat{G}} (\dim_{\mathbb{C}} V)^{2} \leq \#G.
$$

###### _proof:_

The first inequality is just obvious (number is less than the sum of number-many positive numbers).

The list of all matrix coefficients $u_{v, w}$ for all pairs $v, w \in V$ over all $\rho, V \in \widehat{G}$ forms an orthogonal list in $\mathbb{C}[G]$. There are $\sum_{\rho, V \in \widehat{G}} (\dim_{\mathbb{C}} V)^{2}$ of them. The $\mathbb{C}$-dimension of $\mathbb{C}[G]$ is $\#G$ and so the list is at most that long.

---

##### _example:_ irreducible representations of $\mathfrak{S}_{3}$

There are exactly three representations of the symmetric group $\mathfrak{S}_{3}$.
1) the trivial representation $D_{1} : \mathfrak{S}_{3} \to \mathrm{GL}_{1}(\mathbb{C})$ by $\sigma \mapsto 1$.
2) the sign representation $D_{2} : \mathfrak{S}_{3} \to \mathrm{GL}_{1}(\mathbb{C})$ by $\sigma \mapsto \operatorname{sgn} \sigma$.
3) $D_{3} : \mathfrak{S}_{3} \to \mathrm{GL}_{2}(\mathbb{C})$ by
$$
\begin{align}
(1 2) & \mapsto \begin{pmatrix}
-1 & 0 \\
 0 & 1
\end{pmatrix} = \\
(2\, 3) & \mapsto \begin{pmatrix}
1/2 &  \sqrt{ 3 }/2 \\
\sqrt{ 3 } /2 & -1 / 2
\end{pmatrix}
\end{align}
$$
This is actually a subrepresentation of the permutation representation $\mathfrak{S}_{3} \to \mathrm{GL}_{3}(\mathbb{C})$.

We know that these are all the representations of $G$ because the sum of the squares of their dimensions is $6$ and $\# \mathfrak{S}_{3} = 6$.

---