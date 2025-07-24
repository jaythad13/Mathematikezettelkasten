---
tags:
- spivak/mnfld/1
- lin-alg
- self-study
---

Calculus is about local linear approximations, and for manifolds, we talk about local linear approximations to Euclidean space — the [[Prototypical vector spaces|prototypical vector space]] $\bb{R}^n$ with our usual notions of length and angle. Specifically, we mean the usual inner product structure on $\mathbb{R}^n$.

### $\mathbb{R}^n$ as an inner product space

##### _definition:_ Euclidean space

Euclidean space $\bb{R}^n$ is the set of all $n$-tuples of real numbers with the inner product given by 
$$
\langle \bvec{x}, \bvec{y} \rangle = x_1 y_1 + \cdots + x_n y_n
$$
for $\bvec{x} = (x_1, \ldots, x_n)$ and $\bvec{y} = (y_1, \ldots, y_n)$.

Usually we denote $\langle \bvec{x}, \bvec{y} \rangle$ as $\bvec{x} \cdot \bvec{y}$ for Euclidean space.

Note that this inner product induces a [[Norms|norm]] with $\norm{\bvec{x}} = \sqrt{\bvec{x} \cdot \bvec{x}} = \sqrt{x_1^2 + \cdots + x_n^2}$ and thus, a [[Analysis --- math-131/notes/Metric spaces|metric]] $d$ with $d(\bvec{x}, \bvec{y}) = \norm{\bvec{x} - \bvec{y}}$. Also note that verifying that this is indeed an inner product on a vector space gives us the following elementary results, in addition to the usual properties of an inner product.

##### _proposition:_ properties of the Euclidean norm

For $\bvec{x}, \bvec{y} \in \bb{R}^n$ and $a \in \bb{R}$ we have
1) $\norm{\bvec{x}} \ge 0$ and with equality if and only if $\bvec{x} = \bvec{0}$.
2) $\bvec{x} \cdot \bvec{y} \le \norm{\bvec{x}} \norm{\bvec{y}}$ with equality if and only if $\bvec{x}$ and $\bvec{y}$ are linearly dependent.
3) $\norm{\bvec{x} + \bvec{y}} \le \norm{\bvec{x}} + \norm{\bvec{y}}$. 
4) $\norm{a \bvec{x}} = \abs{a} \norm{\bvec{x}}$.

###### _proof:_

1) follows from positive-definiteness in the [[Inner product spaces|definition of an inner product]] and its induced norm.
2) is the [[Norms#_theorem:_ Cauchy-Schwartz inequality|Cauchy-Schwartz inequality]].
3) follows from the Cauchy-Schwartz inequality: just compare the squares of both sides.
4) follows from homogeneity and conjugate homogeneity in the definition of an inner product.

Note that we also have the [[Norms#_theorem_ the polarisation identity|polarisation identity]] (that holds generally in normed spaces and allows us to define an inner product from a norm satisfying the parallelogram law).

##### _proposition:_ the polarisation identity

For $\bvec{x}, \bvec{y} \in \bb{R}^n$
$$
\bvec{x} \cdot \bvec{y} = \frac{\norm{\bvec x + \bvec y}^2 - \norm{\bvec x - \bvec y}^2}{4}.
$$

###### _proof:_

$$
\begin{split}
	\frac{\norm{\bvec x + \bvec y}^2 - \norm{\bvec x - \bvec y}^2}{4} & = \frac{(\bvec x + \bvec y) \cdot (\bvec x + \bvec y) - (\bvec x - \bvec y) \cdot (\bvec x - \bvec y)}{4} \\
	& = \frac{\bvec x \cdot \bvec x + \bvec y \cdot \bvec y + 2 \bvec x \cdot \bvec y - (\bvec x \cdot \bvec x + \bvec y \cdot \bvec y - 2 \bvec x \cdot \bvec y)}{4} \\
	& = \frac{4}{4} \bvec x \cdot \bvec y \\
	& = \bvec x \cdot \bvec y.
\end{split}
$$

### Notational conventions

##### _notation:_ $\mathbf{x}$

A boldface lowercase letter like $\mathbf{x}$, denotes a vector $(x_{1}, \dots, x_{n}) \in \mathbb{R}$.

We denote the standard basis of $\bb{R}^n$ by $\bvec e_1, \ldots, \bvec e_n$. Specifically,

##### _notation:_ $\bvec e_1, \ldots \bvec e_n$

$\bvec e_1, \ldots \bvec e_n$ is the standard basis of $\bb{R}^n$ where $\bvec e_i = (0, \ldots, 1, \ldots 0)$ has $1$ in the $i$th place and $0$ in every other place.

For a linear transformation $T : \bb{R}^n \to \bb{R}^m$, we denote its matrix, say, $A$ as $(a_{i, j})$. Specifically,

##### _notation:_ matrix of a linear transformation, $A = (a_{i, j})$ 

For a linear transformation $T : \bb{R}^n \to \bb{R}^m$ with $T(\mathbf{e}_i) = \sum_{j = 0}^m a_{j, i} \mathbf{e}_j$, its matrix $A = (a_{i, j})$ is the $m \times n$ matrix with $a_{i, j}$ in the $i$th row and $j$th column.

Finally, sometimes we need a convenient notation for $(x_1, \ldots, x_n, y_1, \ldots, y_m)$ for $\bvec x = (x_1, \ldots, x_n) \in \bb R^n$ and $\bvec y = (y_1, \ldots, y_m) \in \bb R^m$.

##### _notation:_ $(\bvec x, \bvec y)$

For $\bvec x = (x_1 \in \bb R^n$ and $\bvec y \in \bb R^m$ we write $(\bvec x, \bvec y)$ to denote $(x_1, \ldots x_n, y_1, \ldots y_m) \in \bb R^{n + m}$.

Note that this notation basically says that we consider $\bb R^n \times \bb R^m$ to be the same as $\bb R^{n + m}$.