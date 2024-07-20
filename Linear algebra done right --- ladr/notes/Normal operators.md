---
tags:
- self-study
- ladr/7A
- lin-alg
---

If an operator isn't [[Linear algebra done right --- ladr/notes/Self-adjoint operators|self-adjoint]], then the next best thing is for it to be normal. Obviously, if an operator is self-adjoint, it commutes with its adjoint. Normal operators are operators that [[Commuting operators|commute]] with their adjoint.

##### _definition:_ normal

An operator $T \in \mathcal{L}(V)$ is normal if $T T^* = T^* T$.

Every self-adjoint operator is normal, but there are other types of normal operators.

##### _example:_ non-self-adjoint normal operator

The operator $T$ on $\mathbb{F}^2$ with matrix $\begin{bmatrix} 2 & -3 \\ 3 & 2 \end{bmatrix}$ with respect to the standard basis is normal. Specifically, $T T^* = T^* T = \begin{bmatrix} 13 & 0 \\ 0 & 13 \end{bmatrix}$.

Notice here that $T(w, z) = (2w -3z, 3w + 2z)$ and $T^*(w, z) = (2w + 3z, 2w - 3z)$. Thus, there is still some symmetry in $T$ and $T^*$. We can encode this precisely as follows

##### _proposition:_ $T$ is normal if and only if $T$ and $T^*$ have the same norm everywhere

Suppose $T \in \mathcal{L}(V)$. Then $T$ is normal if and only if $\lVert Tv \rVert = \lVert T^*v \rVert$ for all $v \in V$.

###### _proof:_

$T$ being normal is equivalent to $T^*T - TT^*$ being the zero operator. Notice that $T^*T - T T^*$ is self-adjoint, so this is just the same as $(T T^* - T^* T) v$ being orthogonal to $v$ for all $v \in V$ ([[Linear algebra done right --- ladr/notes/Self-adjoint operators#_proposition _ there are no $90 circ$ rotation self-adjoint operators|we showed]] that the only such self adjoint operator is the zero operator). But then $\left< T T^* v, v \right> = \left< T^* Tv, v \right>$, and thus, by the adjoint property $\left< T^*v, T^* v \right> = \left< Tv, Tv \right>$ for all $v \in V$. That is, $\lVert Tv \rVert = \lVert T^* v \rVert$ for all $v \in V$ as desired.

### Eigenstuff and normal operators

To understand the eigenstuff of normal operators, we first need to understand their structure as linear maps. For example, the reason normal operators and their adjoints have such similar eigenstuff is that they really are as close as possible to their adjoints without necessarily being self-adjoint

##### _proposition:_ normal $T$ and $T^*$ have the same null space and range

Suppose $T \in \mathcal{L}(V)$ is normal. Then $\operatorname{null} T = \operatorname{null T^*}$ and $\operatorname{range} T = \operatorname{range} T^*$.

###### _proof:_

Since $\lVert Tv \rVert = \lVert T^* v \rVert$, $Tv = 0$ is exactly equivalent to $T^* v = 0$, for any $v \in V$. That is $\operatorname{null} T = \operatorname{null} T^*$, as desired.

[[Linear algebra done right --- ladr/notes/Adjoints#_proposition _ the null space and range of $T *$|We've seen]] that the null space and range of $T^*$ are orthogonal complements of the range and null space of $T$, respectively. Thus,
$$
\begin{split}
\operatorname{range} T & = (\operatorname{null} T*)^\perp \\
 & = (\operatorname{null} T)^\perp \\
 & = \operatorname{range} T^*.
\end{split}
$$

The obvious corollary that follows from this is that

##### _corollary:_ $V$ decomposes into the null space and range of normal $T$

Suppose $T \in \mathcal{L}(V)$ is normal. Then $V = \operatorname{null} T \oplus \operatorname{range} T$.

###### _proof:_

We showed that $\operatorname{range} T = (\operatorname{null} T)^\perp$ in the proof of the proposition. [[Linear algebra done right --- ladr/notes/Orthogonal complements and projections#_proposition _ a subspace and its orthogonal complement sum to the space|It follows]] that $V = \operatorname{null} T \oplus \operatorname{range} T$.

##### _proposition:_ normal $T$ and $T^*$ have the same eigenvectors

$T - \lambda I$ is normal for every $\lambda \in \mathbb{F}$ and $Tv = \lambda v$ if and only if $T^* v = \overline{\lambda} v$.

###### _proof:_

We can show $T - \lambda I$ is normal just by computing $(T - \lambda I)(T - \lambda I)^*$.
$$
\begin{split}
(T - \lambda I)(T - \lambda I)^* & = (T - \lambda I)(T^* - \overline{\lambda} I^*) \\
 & = T T^* - \lambda T^* - \overline{\lambda} T + \overline{\lambda} \lambda I \\
 & = T^* T - \lambda T^* - \overline{\lambda} T + \overline{\lambda} \lambda I \\
 & = T^*(T - \lambda I) - \overline{\lambda}(T - \lambda I) \\
 & = (T^* - \overline{\lambda} I^*)(T - \lambda I) \\
 & = (T - \lambda I)^* (T - \lambda I).
\end{split}
$$

Note then that $(T - \lambda I) v = 0$ is equivalent to $(T - \lambda  I)^* v = 0$ since the operator and adjoint have the same null space. That is, $Tv = \lambda v$ is equivalent to $T^* v = \overline{\lambda} v$.

##### _proposition:_ normal operators have orthogonal eigenvectors

Suppose $T \in \mathcal{L}(V)$ is normal. Then eigenvectors of $T$ corresponding to distinct eigenvalues are orthogonal.

###### _proof:_

Suppose $\alpha, \beta \in \mathbb{F}$ are distinct eigenvalues of $T$ with $Tu = \alpha u$ and $Tw = \beta w$.

We can compute
$$
\begin{split}
(\alpha - \beta) \left< u, w \right> & = \left< \alpha u, w \right>- \left< u, \overline{\beta} w \right> \\
 & = \left< Tu, w \right> - \left< u, T^* w \right>  \\
 & = 0.
\end{split}
$$
Since $\alpha - \beta \neq 0$, we must have $\left< u, w \right> = 0$.

### More on the analogy between $\mathcal{L}(V)$ and $\mathbb{C}$

Of course, the result as stated below only makes sense when $V$ is a complex vector space, but [[it can be made sense of]] on real vector spaces.

##### _proposition:_ the real and imaginary parts of normal operators commute

Suppose $V$ is a complex vector space and $T \in \mathcal{L}(V)$. Then $T$ is normal if and only if there exist commuting self-adjoint operators $A$ and $B$ such that $T = A + i B$.

###### _proposition:_

Suppose $T$ is normal. Then we can calculate its real and complex parts like we would for a complex number —  $A = (T + T^*)/2$ and $B = (T - T^*)/2 i$.

Notice that $A$ and $B$ are self adjoint, and $T = A + i B$. We can also see that
$$
AB - BA = \frac{TT^* - T^*T}{2i}
$$
and thus, that $A$ and $B$ commute.

If $T = A + i B$ for commuting self-adjoint operators, then $T^* = A - i B$. Thus,
$$
\begin{split}
T T^* & = (A + i B)(A - i B) \\
 & = A A + i B A - i A B + B B \\
 & = A A - i B A + i A B + B B \\
 & = A(A + i B) - i B(A + i B) \\
 & = (A - i B)(A + iB) \\
 & = T^* T.
\end{split}
$$
That is, $T$ is normal.
