---
tags:
- alg
- math-171/4
- math-171/5
---

### Linear algebra recap

The theory of linear algebra holds over any field. In particular we have
- $\det$ is multiplicative — $\det(AB) = \det(A) \det(B)$
- $A$ is invertible if and only if $\det(A) \neq 0$

### Matrix groups

Just as how [[Abstract algebra --- math-171/notes/Dihedral groups and generators#The dihedral group|the dihedral group as a subset of all the permutations on vertices of a polygon]], we can think of lots of groups as encoded by the multiplication of matrices — in general function composition being associative makes such a thing natural.

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

##### _definition:_ the orthogonal group

The orthogonal group of degree $n$ over $\mathbb{F}$ is
$$
\mathrm{O}_{n}(\mathbb{F}) = \{ T \in \mathcal{L}(\mathbb{F}^n) | T T^* = T^*T = I  \}.
$$

That is, the group of isometries on $\mathbb{F}^n$. Note that $\det T = \pm 1$ for $T \in \mathrm{O}_{n}(\mathbb{F})$

##### _definition:_ the special orthogonal group

The orthogonal group of degree $n$ over $\mathbb{F}$ is
$$
\mathrm{SO}_{n}(\mathbb{F}) = \{ T \in \mathrm{O}_{n}(\mathbb{F}) | \det T = 1 \}.
$$

### The quaternions and the Hamiltonian ring

The quaternions and Hamiltonians are a sort of "higher dimensional complex numbers". The quaternions define multiplication on the "complex parts":

##### _definition:_ the quaternions

The quaternion group is
$$
Q_{8} = \{ 1, -1, i, -i, j, -j, k, -k \}
$$
where everything works as you'd expect — that is, $1$ and $-1$ behave like you'd expect, and $i, j, k$ act like $\mathbf{i}, \mathbf{j}, \mathbf{k}$ with cross multiplication in $\mathbb{R}^3$ under quaternion multiplication, except $i^2 = j^2 = k^2 = -1$. 

Note that this is very obviously non-abelian.

##### _definition:_ the Hamiltonian ring

The Hamiltonian ring is
$$
\mathbb{H} = \{ a + b i + c j + d k | a, b, c, d \in \mathbb{R} \}
$$
with addition component wise and multiplication defined by $\mathbb{R}$ commuting with elements of $Q_{8}$, the regular multiplication on $Q_{8}$ for its elements and the regular multiplication on $\mathbb{R}$ for elements of $\mathbb{R}$.

Note that we have inverses for all non-zero $z \in \mathbb{H}$ —
$$
(a + bi + cj + dk)^{-1} = \frac{a - bi - cj - dk}{a^2 + b^2 + c^2 + d^2}.
$$

We will see that the orthogonal groups and the Hamiltonians and quaternions are related.