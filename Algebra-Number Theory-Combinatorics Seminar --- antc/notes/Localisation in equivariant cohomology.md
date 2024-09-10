---
tags:
- antc
- reginald-anderson
---

Our working definition of cohomology is as follows:

##### _definition:_ cohomology

The cohomology of a cochain complex $(C; d)$ in the $i$th degree is $H^i(C; d) = \ker d^i / \operatorname{im} d^{i - 1}$.

and our working definition of cellular homology is

##### _definition:_ Euler characteristic of a CW complex

$$
\chi(X) = \sum (-1)^i \# \{ i\text{-cells} \}
$$

Basically, we glue together graphs with higher dimensional faces and edges and do $\#\text{vertices} - \# \text{edges}$ in higher dimensions.

##### _example:_  $S^2 \cong (B^2 \sqcup \{ p \}) /(S^1 \sim p)$

Note that $S^2$ is also diffeomorphic to $\mathbb{C}\mathbb{P} = \frac{\mathbb{C}^{2} \setminus \{ (0, 0) \}}{\mathbb{C}^*}$ by stereographic projection (?). That is, we could write every point on the sphere as a homogenous coordinate pair $(z_{0} : z_{1})$.

Now let's put an action of the torus $\mathbb{T} = \mathbb{C}^*$ on the sphere — $\lambda \cdot (z_{0} : z_{1}) = \lambda(\lambda z_{0} : \lambda^{2} z_{1}) = (z_{0} : \lambda z_{1})$. We don't multiply both coordinates because that would just be the trivial action. The fixed points are $n = (0 : 1)$ and $s = (1 : 0)$ for the north and south poles of the sphere. Notice that things move away from the south pole and toward the north pole — $s$ is an unstable $\mathbb{T}$-fixed point but $n$ is stable. Or to make it easiest to see
$$
\lim_{ \lambda \to \infty }(z_{0} : \lambda z_{1}) = (0 : 1).
$$

Now think about $S^1 \le \mathbb{T}$ acting on $S^2$ by rotations. The $S_{1}$ orbits are the latitudes of $S^2$. Note further that each point on an orbit has the same $\frac{\lvert z_{1} \rvert^{2}}{\lvert z_{0} \rvert^{2} + \lvert z_{1} \rvert^{2}}$.

The idea is that the action of $S^1$ on $\mathbb{C}\mathbb{P}$ gives us two $\mathbb{T}$-fixed points, and that gives us that
$$
\chi(\mathbb{C}\mathbb{P}) = \chi(S^{2}) = 2.
$$
Further, all the points that attract to $n$ give us $B^2$ and $s$ is just $p$. That is, the action of $\mathbb{T}$ gives us the CW complex decomposition.

The reason why is localisation.

### Localisation

##### _theorem(?):_ localisation

For a (compact, orientable, $\mathbb{C}$)-manifold $M$, $\chi(M)$ is the number of fixed points of a (holomorphic, other nice hypotheses) $G$ action on $M$, and the set of points that attract to each fixed point form the cells of the CW complex decomposition.

###### _proof sketch:_

Think about $V$, the manifold of $G$-fixed points, and how pushing forward cohomology from $V$ to $M$ introduces the codimension of $V$ with respect to $M$ (?). Then a bunch of integral computation with $\phi$, the Euler class of the normal bundle gives us $\chi(\mathrm{T}M)$ which turns out to be the same as $\chi(M)$.