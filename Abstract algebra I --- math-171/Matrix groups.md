---
tags:
- alg
- math-171
lecture: math-171-4
---

### Linear algebra recap

The theory of linear algebra holds over any field. In particular we have
- $\det$ is multiplicative — $\det(AB) = \det(A) \det(B)$
- $A$ is invertible if and only if $\det(A) \neq 0$

### Matrix groups

##### _notation:_ $\mathcal{M}_{n}(\mathbb{F})$

Given a field $\mathbb{F}$, we consider $\mathcal{M}_{n}(\mathbb{F})$ to be the $n \times n$ matrices with entries from $\mathbb{F}$.

The general linear group is the simplest matrix group

##### _definition:_ the general linear group, $\mathrm{GL}_{n}(\mathbb{F})$

The general linear group of degree $n$ over $\mathbb{F}$ is
$$
\begin{split}
\mathrm{GL}_{n}(\mathbb{F}) & = \{ A \in \mathcal{M}_{n}(\mathbb{F}) | A \text{ is invertible} \} \\
& = \{ A \in \mathcal{M}_{n}(\mathbb{F}) | \det A \neq 0 \}
\end{split}
$$
with the binary operation of matrix multiplication.

Note that the closure follows from the multiplicativity of the determinant, identity exists — just consider $I_{n}$, associativity follows from function composition associativity (think of matrices as linear maps), and inverses come from the fact that all of the matrices are invertible.

##### _example:_ $\mathrm{GL}_{2}(\mathbb{F}_{2})$

- is just the six matrices with two or fewer zeroes, with no two zeroes in the same line, and not the all ones matrix
$$
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}, 
\begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix},
\begin{bmatrix}
0 & 1 \\
1 & 1
\end{bmatrix},
\begin{bmatrix}
1 & 0 \\
1 & 1
\end{bmatrix},
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix},
\begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix}
$$
- is non-abelian since
$$
\begin{bmatrix}
0 & 1 \\
1 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 \\
1 & 1
\end{bmatrix}
= \begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
\neq
\begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix}
= \begin{bmatrix}
1 & 0 \\
1 & 1
\end{bmatrix}
\begin{bmatrix}
0 & 1 \\
1 & 1
\end{bmatrix}
$$
- and is the same as $\mathrm{SL}_{2}(\mathbb{F}_{2})$

##### _definition:_ the special linear group, $\mathrm{SL}_{n}(\mathbb{F})$

The special linear group of degree $n$ over $\mathbb{F}$ is
$$
\mathrm{SL}_{n}(\mathbb{F}) = \{ A \in \mathcal{M}_{n}(\mathbb{F}) | \det A = 1 \}.
$$
