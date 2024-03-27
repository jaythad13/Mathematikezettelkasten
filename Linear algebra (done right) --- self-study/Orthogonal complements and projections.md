---
tags:
- self-study
- lin-alg
---

Sometimes we want to decompose a vector into one part that's in some sense related to a certain subspace, which we call the orthogonal projection, and another part that's absolutely not, which is part of the orthogonal complement of that subspace.

### Orthogonal complement

##### _(motivating) example:_ planes and their normal vectors

A plane (that passes through the origin) is a two-dimensional subspace of $\mathbb{R}^3$. It corresponds exactly to the one dimensional subspace spanned by the vectors normal to it.

Orthogonal complements generalise this idea.

##### _definition:_ orthogonal complement, $U^\perp$

If $U$ is a subset of $V$, then the orthogonal complement of $U$, denoted $U^\perp$, is the set of all vectors orthogonal to every vector in $U$ —
$$
U^\perp = \{ v \in V \mid \left< v, u \right> = 0 \text{ for each } u \in U \}
$$

It turns out that this has some nice properties.

##### _proposition:_ the properties of the orthogonal complement

If $U, W$ are subsets of $V$,
1) $U^\perp$ is a subspace of $V$.
2) $\{ 0 \}^\perp = V$.
3) $V^\perp = \{ 0 \}$.
4) $U \cap U^\perp \subseteq \{ 0 \}$.
5) If $W \subseteq U$, the $U^\perp \subseteq W^\perp$.

##### _proof:_

1) First, since $\left< 0, u \right> = 0$ for any $u \in U$, (and in fact any $u \in V$), we have that $0 \in U^\perp$. Suppose $v, w \in U^\perp$ and $\lambda \in \mathbb{F}$. Then 
$$
\begin{split}
\left< \lambda v + w, u \right> & = \left< \lambda v, u \right> + \left< w, u \right> \\
& = \lambda \left< v, u \right> + \left< w, u \right> \\
& = 0 + 0 \\
& = 0
\end{split}
$$
		where the first and second steps follow by the linearity of the inner product. Thus, for any $v, w \in U^\perp$ we have $v + w \in U^\perp$ by taking $a = 1$ and for any $v \in U^\perp, a \in \mathbb{F}$, we have $av \in U^\perp$ by taking $w = 0$.
2) For any $v \in V$, we have $\left< v, 0 \right> = 0$. Thus, any $v \in V$ gives us $v \in \{ 0 \}^\perp$, and thus, $V = \{ 0 \}^\perp$.
3) If $u \in V^\perp$, since $u$ is orthogonal to every vector, it must be orthogonal to itself. That is, $\left< u, u \right> = 0$. By the [[Inner product spaces|positivity of the inner product]], we must have $u = 0$. Thus, $V^\perp \subset \{ 0 \}$. Since $\left< 0, v \right> = 0$ for all $v \in V$, we also have $\{ 0 \} \subset V$ and thus, $\{  0 \} = V$.
4) If $v \in U \cap U^\perp$, then $v$ is perpendicular to everything in $U$, including itself. That is, $\left< v, v \right> = 0$, and thus, $v = 0$. Thus, $U \cap U^\perp \subseteq \{ 0 \}$.
5) Suppose $W \subseteq U$ and $v \in U^\perp$. Then since $\left< v, u \right> = 0$ for all $u \in U$, $\left< v, w \right> = 0$ for every $w \in W$ since every $w \in W \subseteq U$. That is, if $v \in U^\perp$, then $v \in W^\perp$, or in other words, $U^\perp \subseteq W^\perp$.

We can do even nicer things if $U$ is a subspace — specifically, we can decompose the vector space into the direct sum of $U$ and $U^\perp$. Of course if $U$ is not, we can make it a subspace by just considering the span of the vectors in it.

##### _proposition:_ a subspace and its orthogonal complement sum to the space

Suppose $U$ is a finite dimensional subspace of $V$. Then $V = U \oplus U^\perp$.

##### _proof:_

Note that we already have that $U \cap U^\perp \subseteq \{ 0 \}$ by the previous result. This is obviously an equality when $U$ is a subspace since $U^\perp$ is always a subspace. Thus, we only need to show that $V = U + U^\perp$.

Let $e_{1}, \dots, e_{m}$ be an orthonormal basis of $U$. Thus, for any $v \in V$, we can "project" onto this orthonormal list [[Gram-Schmidt procedure#_theorem _ Gram-Schmidt procedure|like we did for the Gram-Schmidt procedure]]. That is, we can write
$$
v = \left< v, e_{1} \right> \, e_{1} + \dots + \left< v, e_{m} \right>\, e_{m} + (v - ( \left< v, e_{1} \right> \, e_{1} + \dots + \left< v, e_{m} \right>\, e_m)).
$$

Note that $u =  \left< v, e_{1} \right> \, e_{1} + \dots + \left< v, e_{m} \right>\, e_m$ is obviously in $U$. We will show that $v - u$ is in $U^\perp$. For any $e_{i}$, we can see that
$$
\begin{split}
\left< v - u, e_{i} \right> & =\left< v, e_{i} \right> - \left< u, e_{i} \right> \\
& =\left< v, e_{i} \right> - \left< v, e_{i} \right>  \\
& = 0.
\end{split}
$$
Then by the linearity of orthogonality $v - u$ is orthogonal to any vector in $U$, which must be a linear combination of $e_{i}$. Thus, $v - u \in U^\perp$.

This means that we have written any arbitrary $v \in V$ as a sum of $u \in U$ and $v - u \in U^\perp$, and thus, we've shown that $V = U + U^\perp$ as desired.

##### _corollary:_ dimension of the orthogonal complement

Suppose $V$ is finite dimensional and $U$ is a subspace of $V$. Then
$$
\operatorname{dim} U^\perp = \operatorname{dim} V - \operatorname{dim} U.
$$

##### _proof:_

Since $V = U \oplus U^\perp$, we have $\operatorname{dim} V = \operatorname{dim} U + \operatorname{dim} U^\perp$. Thus, $\operatorname{dim} U^\perp = \operatorname{dim} V - \operatorname{dim} U$.

##### _proposition:_ the orthogonal complement is an involution

Suppose $U$ is a finite dimensional subspace of $V$. Then $(U^\perp)^\perp = U$.

##### _proof:_

First we will show that $U \subset (U^\perp)^\perp$. Note that for any $u \in U$, $w \in U^\perp$, we must have $\left< w, u \right> = 0$, and thus $\left< u, w \right> = 0$. Thus, $u \in (U^\perp)^\perp$. That is, $U \subset (U^\perp)^\perp$.

Now we will show $(U^\perp)^\perp \subset U$. Suppose $v \in (U^\perp)^\perp$. Then, for every $w \in U^\perp$, we must have $\left< v, w \right > = 0$. Since we can uniquely decompose $v$ into $u + (v - u)$ where $u \in U$ and $v - u \in U^\perp$, we can write this as
$$
\left< u, w \right> + \left< v - u, w \right> = 0.
$$
Since $u \in (U^\perp)^\perp$, $\left< u, w \right> = 0$, and thus, we're left with
$$
\left< v - u, w \right> = 0.
$$
That is, $v - u$ is orthogonal to every $w \in U^\perp$ and thus, is orthogonal to itself. Thus, $v - u = 0$. Then $v = u \in U$, and thus $(U^\perp)^\perp \subset U$, completing the proof.

### Orthogonal projections

##### _(motivating) example:_ orthogonal projections from Gram-Schmidt

When we create an orthonormal basis from a regular basis using Gram-Schmidt, we project the next vector onto the span of the orthonormal basis we already have, and then just look at the rest.

Orthogonal projections are exactly this idea, but now that we've already done the work with inner products, we can write it more cleanly.

##### _definition:_ orthogonal projection, $P_{U}$

Suppose $U$ is a finite-dimensional subspace of $V$. The orthogonal projection of $V$ onto $U$ is the operator $P_{U} : V \to V$ defined as follows. 

For any $v \in V$, with $v = u + w$ where $u \in U$ and $w \in U^\perp$, $P_{U}v = u$.

##### _example:_ projection on to a one-dimensional subspace

Suppose $U = \operatorname{span} u$ for some $u \in V$. Then
$$
P_{U}v = \frac{\left< v, u \right> }{\lVert u \rVert ^2} u.
$$
This just follows from [[Orthogonality|the orthogonal decomposition]] we've seen already.

There's a whole bunch of nice properties about projections.

##### _proposition:_ the properties of the orthogonal projection

Suppose $U$ is a finite-dimensional subspace of $V$ and $v \in V$. Then
1) $P_{U}$ is a linear operator — $P_{U} \in \mathcal{L}(V)$
2) $P_{U} u = u$ for any $u \in U$
3) $P_{U}w = 0$ for any $w \in U^\perp$.
4) $\operatorname{range} P_{U} = U$
5) $\operatorname{null} P_{U} = U^\perp$
6) $v - P_{U}v \in U^\perp$
7) $P_{U}^2 = P_{U}$
8) $\lVert P_{U}v \rVert \le \lVert v \rVert$
9) for every orthonormal basis $e_{1}, \dots, e_{m}$ of $U$,$$
P_{U} v = \left< v, e_{1} \right> e_{1} + \dots + \left< v, e_{m} \right> e_{m}.
$$
##### _proof:_

1) Suppose $v_{1}, v_{2} \in V$ and $\lambda \in \mathbb{F}$. Then we can decompose $v_{1} = u_{1} + w_{1}$ and $v_{2} = u_{2} + w_{2}$ where $u_{1}, u_2 \in U$ and $w_{1}, w_{2} \in U^\perp$. Since $\lambda v_{1} + v_{2} = (\lambda u_{1} + u_{2}) + (\lambda w_{1} + w_{2})$ is a unique decomposition into $\lambda u_{1} + u_{2} \in U$ and $\lambda w_{1} + w_{2} \in U^\perp$, we have $$
\begin{split}
P_{U}(\lambda v_{1} + v_{2}) & = \lambda u_{1} + u_{2} \\
& = \lambda P_{U} v_{1} + P_{U} v_{2} \\
\end{split}
$$which establishes linearity, as desired.
2) For any $u \in U$, the unique decomposition into elements of $U$ and $U^\perp$ is just $u = u + 0$ where $u \in U$ and $0 \in U^\perp$. Thus, $P_{U}u = u$.
3) For any $w \in U^\perp$, the unique decomposition into elements of $U$ and $U^\perp$ is just $w = 0 + w$ where $0 \in U$ and $w \in U^\perp$. Thus, $P_{U}w = 0$.
4) We have defined $P_{U}$ so that $\operatorname{range} P_{U} \subset U$. Thus, we only need to show that every $u \in U$ is $P_{U}v$ for some $v \in V$. Since $P_{U} u = u$ for all $u \in U$, this is true.
5) We've already shown that $U^\perp \subset \operatorname{null} P_{U}$ in 3). Note that if $v \not\in U^\perp$ then $v = u + w$ with $u \in U$, $u \neq 0$, and $w \in U^\perp$. Thus $P_{U}v = 0 \neq 0$ if $v \not\in U^\perp$. Thus, $\operatorname{null} P_{U} \subset U^\perp$ giving us $\operatorname{null} P_{U} = U^\perp$.
6) If we have $v = u + w$ where $u \in U$ and $w \in U^\perp$, then $$
\begin{split}
v - P_{U}v & = v - u \\
& = u + w - u \\
& = w \in U^\perp.
\end{split}
$$
7) Since $P_{U}u = u$ for all $u \in U$ and $P_{U}v \in U$ for all $v \in V$, we have $$
\begin{split}
P_{U}^2 v & = P_{U}(P_{U}v) \\
& = P_{U}v
\end{split}
$$for any $v \in V$. Thus $P_{U}^2 = P_{U}$.
8) For $v = u + w$ with $u \in U$ and $w \in U^\perp$, note that we have $\left< u, w \right> = 0$. Thus, by Pythagoras' theorem $$
\begin{split}
\lVert P_{U}v \rVert^2 & = \lVert u \rVert^2 \\
 & \le \lVert u \rVert ^2 + \lVert w \rVert ^2 \\
 & = \lVert v \rVert ^2.
\end{split}
$$Thus, $\lVert P_{U}v \rVert \le \lVert v \rVert$.
9) This follow from the construction that we used in [[#_proof _|the proof]] that $V = U \oplus U^\perp$.