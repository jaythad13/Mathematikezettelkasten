---
tags:
- self-study
- lin-alg
- ladr/7A
---

[[Linear algebra done right --- ladr/notes/Adjoints#_remark _ thinking of operators as scalars|Previously]], we mentioned how if operators are analogous to complex scalars, then their adjoints are analogous to complex conjugates. Then the real numbers are the operators $T$ with $T = T^*$.

##### _example:_ real symmetric matrices are self-adjoint

The operator with matrix $\begin{bmatrix} 2 & c \\ 3 & 7 \end{bmatrix}$ (with respect to the standard basis) is self-adjoint if and only if $c = 3$. However, $\begin{bmatrix}  2 & c \\ 3 + i & 7 \end{bmatrix}$ is self-adjoint if and only if $c = 3 - i$.

##### _definition:_ self-adjoint operator

An operator $T \in \mathcal{L}(V)$ is self-adjoint if $T = T^*$.

Note that by definition this means that $\left< Tv, w \right> = \left< v, Tw \right>$.

### Self-adjoint operators behave like real numbers

While the first of these results is trivially true for real vector spaces, often, to think about self-adjoint operators as real numbers, we need to be working over a complex vector space.

##### _proposition:_ eigenvalues of self-adjoint operators

Every eigenvalue of a self-adjoint operator is real.

###### _proof:_

Suppose $T \in \mathcal{L}(V)$ is self-adjoint, and $v$ is an eigenvector with eigenvalue $\lambda$. Then $\left< Tv, v \right> = \lambda \left< v, v \right>$ and $\left< v, Tv  \right> = \overline{\lambda} \left< v, v \right>$. However, since $T$ is self adjoint, $\left< Tv, v \right> = \left< v, Tv \right>$, and thus $\lambda \left< v, v \right> = \overline{\lambda} \left< v, v \right>$ ultimately giving us $\lambda = \overline{\lambda}$ and $\lambda \in \mathbb{R}$.

We also have that if $\left< Tv, v \right>$ is real for all $v$, then $T$ is self-adjoint, but first we need the following lemma about operators on a complex space.

##### _lemma:_ there are no $90^\circ$ rotations in complex vector space

Suppose $V$ is a complex inner product space and $T \in \mathcal{L}(V)$. Then $\left< Tv, v \right> = 0$ for all $v \in V$ if and only if $T$ is the zero operator.

###### _proof:_

It's clear that if $T$ is the zero operator, then $Tv = 0$ is always orthogonal to $v$.

Suppose $\left< Tv, v \right> = 0$ for all $v \in V$ for some operator $T$ on $V$. For any $u, w \in V$, we can rewrite
$$
\begin{split}
\left< Tu, w \right> & = \frac{\left< T(u + w), u + w \right>  - \left< T(u - w), u - w \right> }{4} \\
 & + \frac{\left< T(u + iw), u + iw \right> - \left< T(u - iw), u - iw \right> }{4}i.
\end{split}
$$
Note that each term on the right hand side is of the form $\left< Tv, v \right>$.  Thus, $\left< Tu, w \right>$ is always $0$. But then we must have that $\left< Tu, Tu \right> = 0$ always, and thus, $T = 0$.

##### _proposition:_ $T$ is self-adjoint if and only if $\left< Tv, v \right>$ is always real

Suppose $V$ is a complex inner product space and $T \in \mathcal{L}(V)$. Then $T$ is self adjoint if and only if $\left< Tv, v \right> \in \mathbb{R}$ for every $v \in V$.

###### _proof:_

Its clear that if $T$ is self adjoint, $\left< Tv, v \right> = \left< v, Tv \right>$ and then by conjugate symmetry, it follows that $\left< Tv, v \right> = \overline{\left< Tv, v \right>} \in \mathbb{R}$.

Suppose that $\left< Tv, v \right> \in \mathbb{R}$ always. Then since $\left< T^*v, v \right> = \overline{\left< Tv, v \right>}$, we have $\left< T^*v, v \right> = \left< Tv, v \right>$, and thus, $\left< (T - T^*)v, v \right>  = 0$ always. But then by the lemma above, we must have $T - T^* = 0$ and $T$ is self-adjoint.

Finally, we can use a similar trick — to generalise the lemma. Even though real operators can have images orthogonal to their inputs, self-adjoint operators cannot.

##### _proposition:_ there are no $90^\circ$ rotation self-adjoint operators

Suppose $T$ is a self-adjoint operator on $V$. Then $\left< Tv, v \right> = 0$ for all $v \in V$ if and only if $T$ is the zero operator.

###### _proof:_

If $V$ is a complex inner product space, this follows already by [[#_lemma _ there are no $90 circ$ rotations in complex vector space|the lemma]]. Assume $V$ is a real inner product space. We can use the same trick again — for any $u, w \in V$,
$$
\begin{split}
\frac{\left< T(u + w), u + w \right> - \left< T(u - w), u - w \right> }{4} & = \frac{\left< Tu, u \right>  + \left< Tw, w \right> + \left< Tu, w \right> + \left< Tw, u \right> - \left< Tu, u \right> - \left< Tw, w \right> + \left< Tu, w \right> + \left< Tw, u \right> }{4} \\
 & = \frac{\left < Tu, w \right> + \left< Tw, u \right>}{2} \\
 & = \left< Tu, w \right>.
\end{split}
$$

Notice that this identity requires $T$ to be self-adjoint to work, and it allows us to write any $\left< Tu, w \right>$ as a linear combination of terms of the form $\left< Tv, v \right>$. Then $\left< Tu, Tu \right> = 0$ always, and thus, $T = 0$.