---
tags: 
- alg
- rep-th
- math-171/8
---

Representations are ways of embedding groups in sets we already understand. Often we do this by way of group actions.

There are two primary types of permutations of $G$ into [[Group combinatorics and symmetric groups#_definition _ the symmetric group on $ Omega$|symmetric groups]] and into [[Matrix groups and the quaternions#_definition _ the general linear group, $ mathrm{GL}_{n}( mathbb{F})$|matrix groups]].

##### _definition:_ permutation representation

Let $G$ be a group. A homomorphism $\varphi : G \to S_{X}$ is a permutation representation of $G$.

##### _definition:_ linear representation

Let $G$ be a group, and $n \in \mathbb{N}$. A homomorphism $\rho : G \to \mathrm{GL}_{n}(\mathbb{C})$ is a linear representation of $G$.

##### _example:_ permutation and linear representations of $D_{8}$

$$
\varphi : s^i r^j \mapsto ((1 \, 2)(3 \, 4))^i(1 \, 2 \, 3 \, 4)^j
$$
is a permutation representation of $D_{8}$ and
$$
\rho : s^i r^j \mapsto \begin{bmatrix}
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}^i
\begin{bmatrix}
0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}^j
$$
is a linear representation. You can see that there are elements that each "represent" $s$ and $r$ by swapping things around in similar ways.