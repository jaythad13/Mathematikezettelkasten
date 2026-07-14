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

---

