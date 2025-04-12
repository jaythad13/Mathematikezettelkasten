---
tags:
- fourier
- alg
- math-139/27
- math-139/28
---

The goal of Fourier analysis on a finite abelian group $G$ is to to decompose the data of functions $G \to \mathbb{C}$ into simpler data. For this purpose, we define the inner product space of functions $G \to \mathbb{C}$. Our goal is to get a (group-theoretically) nice [[Linear algebra done right --- ladr/notes/Orthonormal bases#_definition _ orthonormal basis|orthonormal basis]].

##### _definition:_ space of functions on a group

For a finite abelian group $G$, the vector space of functions $G \to \mathbb{C}$ is denoted $\mathbb{C}^G$. It is an inner product space with
$$
\left< f, g \right> = \frac{1}{\lvert G \rvert } \sum_{x \in G} f(x) \overline{g(x)}.
$$

### Characters and the dual group

Let $G$ be an arbitrary finite abelian group for the rest of this note.

The characters on $G$ give this orthonormal basis, and form an abelian group $\hat{G}$ themselves.

##### _definition:_ $S^1$

Let $S^1$ denote the abelian group $\{ z \in \mathbb{C}, \lvert z \rvert = 1 \}$ with complex multiplication.

##### _definition:_ character, the dual group

A character on $G$ is a [[Abstract Algebra I --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphism]] $\xi : G \to \mathbb{C}$.

Under pointwise complex multiplication the characters on $G$ form the dual group $\hat{G}$.

##### _lemma:_ characterising characters

Any homomorphism $\xi : G \to \mathbb{C}^*$ is a character.

###### _proof:_

Since $G$ is finite, $\lvert \xi \rvert$ is bounded above and below. If $\lvert \xi(x) \rvert > 1$ for any $x$, then $\xi(x^n) = \xi(x)^n$ would have unbounded magnitude above as $n \to \infty$. If $\lvert \xi(x) \rvert < 1$, then $\lvert \xi(x) \rvert^n$ would go to zero for the same reason, and thus, would not have magnitude bounded below. That is, unless $\lvert \xi \rvert = 1$ always, we have a contradiction.

##### _lemma:_ non-trivial characters sum to zero

Suppose $\xi$ is a non-trivial character in $\hat{G}$. Then
$$
\sum_{x \in G} \xi(x) = 0.
$$

###### _proof:_

We use the fact that the [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ (left) group action|group action]] on itself by left multiplication is a bijection. Given, $\xi(y) \neq 1$, this allows us to show that
$$
\xi(y) \sum_{x \in G} \xi(x) = \sum_{x \in G} \xi(x) \xi(h) = \sum_{x \in G} \xi(xy) = \sum_{g \in G} \xi(x).
$$
Thus, multiplying the sum by a non-zero complex number $\xi(y)$ returns the same sum again —
$$
(\xi(y) - 1) \sum_{x \in G} \xi(x) = 0
$$
forces the sum to be $0$ since $\xi(x) \neq 1$.

We eventually want to prove that $\hat{G}$ is an orthonormal basis for all $\mathbb{C}$-valued functions out of $G$. First, we show that distinct characters are at least [[Linear algebra done right --- ladr/notes/Orthonormal bases#_definition _ orthonormal|orthonormal]]. To do so we need the following lemma from linear algebra.

##### _lemma:_ the dual group is an orthonormal list

For any $\xi \in \hat{G}$, $\left< \xi, \xi \right> = 1$, and for any $\xi' \neq \xi$, $\left< \xi, \xi' \right> = 0$.

###### _proof:_

##### _lemma:_ simultaneous diagonalisation

Let $V$ be a finite-dimensional inner product space with a $T_{1},\dots, T_{n}$ a finite list of diagonalisable operators. If all pairs $T_{i}, T_{j}$ commute there is a single basis of eigenvectors with respect to which all of them are diagonalisable.

###### _proof:_

The base case is the spectral theorem. Suppose the lemma is true for the family $T_{1}, \dots, T_{n - 1}$ of commuting isometries. The definition of diagonalisation is that we can decompose $V$ into the direct sum of eigenspaces of $T_{n}$ —
$$
V = V_{\lambda_{1}} \oplus \dots \oplus V_{\lambda_{m}}.
$$
For any $v \in V_{\lambda_{k}}$ and any $1 \le j \leq n - 1$, we can write
$$
\begin{align}
T_{n} T_{j}v  & = T_{j} T_{n} v \\
 & = T_{j} \lambda_{k} v \\
 & = \lambda_{k} T_{j} v
\end{align}
$$
so $T_{j} v$ is also an eigenvector of $T_{n}$ with eigenvalue $V_{k}$. That is, $T_{j} v \in V_{\lambda_{k}}$.

Thus, each $V_{\lambda_{k}}$ can be decomposed into a direct sum of subspace which are each eigenspaces for all $T_{1}, \dots, T_{n - 1}$. Since the eigenspaces are contained in $V_{\lambda_{k}}$, all of these sub-eigenspaces consist of eigenvectors of $T_{n}$. Thus, the basis of eigenvectors for $T_{1}, \dots, T_{n - 1}$ consists of eigenvectors of $T_{n}$ as well.

##### _theorem:_ the dual group is an orthonormal basis

If $G$ is a finite abelian group, then $\hat{G}$ is an orthonormal basis the vector space $\mathbb{C}^G$ of all complex valued functions on $G$.

###### _proof:_

We've already shown that $\hat{G}$ is an orthonormal list in $\mathbb{C}^G$. We just need to show that it has the right length — the same as the size of $G$.

For each $x \in G$ define the linear map $T_{x} : \mathbb{C}^G \to \mathbb{C}^G$ by $(T_{x} f)y = f(x y)$. Notice that any character $\xi$ is an eigenvector of $T_{x}$ — for all $x \in G$ $(T_{x} \xi)x = \xi(xy) = \xi(x) \xi(y)$. We want to show that all of the eigenvectors of $T_{x}$ are characters.

These are linear isometries since summing $(T_{x}f_{1})(y) \overline{(T_{x} f_{2})(y)} = f_{1}(x y)  \overline{f_{2}(x y)}$ over al $x \in G$ is the same as summing $f_{1}(y) \overline{f_{2}(y)}$. Thus, the sums for $\left< T_{x} f_{1}, T_{x} f_{2} \right>$ and $\left< f_{1}, f_{2} \right>$ are the same, giving $\left< T_{x} f_{1}, T_{x} f_{2} \right> = \left< f_{1}, f_{2} \right>$. They commute since $G$ is abelian. Thus, there is a simultaneous basis of eigenvectors for all $T_{x}$.

Call the basis vectors $\zeta_{x}$ where we can index by $x \in G$ since $\mathbb{C}^G$ is clearly $\lvert G \rvert$-dimensional. Consider the normalisation $\xi_{x} = \zeta_{x} / \zeta_{x}(1)$. We claim that the basis of eigenvectors $\xi_{x}$ consists of characters, which we have already shown are orthogonal. We will show this by showing that they are homomorphisms $G \to \mathbb{C}^*$.

Let $\lambda_{x, y}$ be the eigenvalue of $\zeta_{x}$ (and thus, also $\xi_{x}$) under $T_{y}$ and define $\lambda_{x, z}$ similarly
$$
\begin{align}
\xi_{x}(yz) & = (T_{y} \xi_{x})(z) \\
 & = \lambda_{x, y} \xi_{x}(z) \\
 & = \lambda_{x, y} (T_{z} \xi_{x})(z) \\
 & = \lambda_{x, y} \lambda_{x, y} \\
 & = \xi_{x}(y) \xi_{x}(z).
\end{align}
$$
Here, the last equality comes from noticing that
$$
\xi_{x}(y) = (T_{y}\xi_{x})(1) = \lambda_{x, y} \xi_{x}(1) = \lambda_{x, y}
$$
since we normalised $\xi_{x}$ to be $1$ at the identity of $G$.

### Fourier analysis

Just as with [[Fourier Analysis --- math-139/notes/Fourier analysis on the cyclic group#_definition _ Fourier coefficient|finite Fourier analysis on cyclic groups]], the fundamental results of Fourier analysis follow immediately from [[Linear algebra done right --- ladr/notes/Orthonormal bases#Orthonormal bases|facts about orthonormal bases]]. 

##### _definition:_ Fourier coefficient

For any function $f : G \to \mathbb{C}$, and character $\xi \in \widehat{G}$, the $\xi$th Fourier coefficient of $f$ is $\hat{f}(\xi) = \left< f, \xi \right>$.

##### _theorem:_ Fourier inversion

For any function $f : G \to \mathbb{C}$, we have
$$
f = \sum_{\xi \in \hat{G}} \hat{f}(\xi) \xi.
$$

##### _theorem:_ Plancherel's theorem

For any function $f : G \to \mathbb{C}$, we have
$$
\lVert f \rVert ^{2} = \sum_{\xi \in \hat{G}} \lvert \hat{f}(\xi) \rvert^{2}.
$$