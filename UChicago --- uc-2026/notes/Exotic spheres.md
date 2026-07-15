---
tags:
- uc-2026/exotic/1
- alg-top
- diff-geo
- mark-behrens
---

Recall, by the [[Topology --- math-147/notes/Classification of surfaces|classification of surfaces]] that $S^{2}$ is the only simply connected, connected, compact surface. Similarly, we know a lot about simply connected, connected compact $3$-folds. Since $H_{1}(X) \cong \pi_{1}(X)^\text{ab}$ and $H^1(X) \cong \operatorname{Hom}(\pi_{1}(X), \mathbb{Z})$ (by Hurewicz) we can apply Poincaré duality to see that $H_{\bullet}(X) \cong H_{\bullet}(S^{3})$ ($0$ in degrees $1, 2$ and $\mathbb{Z}$ otherwise). The Poincaré conjecture was then, whether $X \cong_{\mathsf{Top}} S^{3}$.

In higher dimensions, $\pi_{1}(X) \cong \pi_{1}(S^n) = 0$ doesn't guarantee $H_{\bullet}(X) \cong H_{\bullet}(S^n)$. For example $S^{2} \times S^{2}$ is simply connected, but. However, if we assume $\pi_{1}(X) = 0$ and $H_{\bullet}(X) \cong H_{\bullet}(S^n)$, then we can ask if $X$ is homeomorphic to $S^n$. Note: this is a reasonable thing to conjecture. For one, such $X$ are homotopy spheres.

##### _proposition:_ simply-connected homology spheres are homotopy spheres

If $\pi_{1}(X) = 0$ and $H_{\bullet}(X) \cong H_{\bullet}(S^n)$, then $X \simeq S^n$.

###### _proof:_

Since both are simply connected and their homologies are the same, we just need to find a map between them that induces the isomorphism of homology (this is the Whitehead theorem).

There is a Hurewicz morphism $h_{n} : \pi_{n}(X) \to H_{n}(X)$ as follows. For $\gamma : S^n \to X$ we have $\gamma_{*} : H_{n}(S^n) \to H_{n}(X)$. $h_{n}([\gamma]) = \gamma_{*}(1)$ where $1 \in H_{n}(S^n) \cong \mathbb{Z}$ is the canonical generator. Let $k$ be the smallest $n$ such that $\pi_{n}(X)$ and $H_{n}(X)$ are non-trivial. It is a fact of classical algebraic topology that $h_{k}$ is an isomorphism.

Thus, for such a candidate $X$, we have $\pi_{n}(X) \cong \mathbb{Z}$. Choose $\gamma : S^n \to X$ such that $[\gamma]$ generates $\pi_{n}(X)$. We claim this is a homology isomorphism. It's easy to see that $\gamma_{*}$ preserves $H_{0}$ and $H_{n}$. The rest of the $H_{i}$ are are $0$, so $\gamma_{*}$ is a homology isomorphism.

---

Smale proved the $h$-cobordism theorem (by Morse theory) implying the Poincaré conjecture for $n \geq 5$. Freedman then used more techniques to give a classification of simply connected $4$-folds. Finally, Perelman proved the geometrisation conjecture, and thus Poincaré for $3$-folds. (We already knew this for dimensions $1$ and $2$).

Since we can't even have different topological structures on homotopy spheres, we would think that we can't have different smooth structures either. This is the smooth Poincaré conjecture (simply connected, compact, $n$-fold, homology spheres are diffeomorphic to $S^n$ with the structure given by $S^n \subseteq \mathbb{R}^{n + 1}$). This is wrong!

##### _theorem:_ exotic $7$-spheres exist (Milnor)

There exists a $7$-manifold $X$ such that $X \cong_{\mathsf{Top}} S^7$ but $X \not \cong_{\mathsf{Diff}} S^7$.

###### _proof:_

Consider some general odd-dimensional topological sphere $S^{2k + 1}$. Note that we can construct $S^{3}$ as a copy of two solid tori glued across their common torus boundary. That is,
$$
S^{3} \cong_{\mathsf{Diff}} (B^{2} \times S^1) \cup_{S^1 \times S^1} (S^1 \times B^{2}).
$$
To see this, think of $S^{3}$ as $(\mathbb{R}^{3})^+$, the [[Topology --- math-147/attachments/exam/exam.pdf#page|one-point compactification]] of $\mathbb{R}^{3}$. Remove a neighbourhood of infinity from $(\mathbb{R}^{3})^+$ — a complement of a large centred ball $B$. Also, remove a cylinder through the ball. But then what is left of the ball is a solid torus and what we removed was also a solid torus. This works in general too —
$$
S^{2k + 1} \cong_{\mathsf{Diff}} (B^{k + 1} \times S^k) \cup_{S^k \times S^k} (S^k \times B^{k + 1}).
$$
What if we didn't glue along the identity map? Gluing along some twist $f_{ij}$ we get some
$$
X_{ij} = (B^4 \times S^{3}) \cup_{S^3 \times S^3}^{f_{ij}} (S^{3} \times B^4).
$$
In particular, we get $f_{ij}$ by the inclusion of $S^3$ in the quaternions. We write $S^3 \times S^3 \to S^{3} \times S^3$ by $(x, y) \mapsto (x^i y x^j, x)$.

Another way to do this is by **clutching functions**. For any $\alpha : S^{3} \to \mathrm{SO}_{4}(\mathbb{R})$ gives a rank $4$ vector bundle $\mathscr{V}_{\alpha} \to S^4$ with $\mathscr{V}_{\alpha} = B^4 \times \mathbb{R}^4 \cup_{S^{3} \times \mathbb{R}^4} B^4 \times \mathbb{R}^4$ where the projection is trivial along $B^4 \times \mathbb{R}^4$ and given by $(x, v) \mapsto (x, \alpha(x) v)$ along $S^3 \times \mathbb{R}^4$. We can choose a unit sphere bundle $S(\mathscr{V}_{\alpha}) = \partial B(\mathscr{V}_{\alpha}) \subseteq \mathscr{V}_{\alpha}$, the boundary of the ball bundle inside $\mathscr{V}_{\alpha}$. The map $S^3 \to S(\mathscr{V}_{\alpha}) \to S^4$.

Now we make a general argument about such manifolds. Suppose $X$ is a $7$-fold that is the boundary of an $8$-fold $Y$. Then define $\lambda(X) = 2 p_{1}^{2}(Y) - \operatorname{sign} Y \in \mathbb{Z} / 7$. Note, it has to be shown that this does not depend on the choice of $Y$.

---