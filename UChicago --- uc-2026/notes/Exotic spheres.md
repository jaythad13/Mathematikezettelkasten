---
tags:
- uc-2026/exotic/1
- uc-2026/exotic/2
- uc-2026/exotic/3
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

###### _proof sketch:_

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
In particular, we get $f_{ij}$ by the inclusion of $S^3$ in the quaternionic units. We write $S^3 \times S^3 \to S^{3} \times S^3$ by $(x, y) \mapsto (x^i y x^j, x)$ where $i, j \in \mathbb{Z}$ (rather than the complex parts).

Another way to do this is by **clutching functions**. For any $\alpha : S^{3} \to \mathrm{SO}_{4}(\mathbb{R})$ gives a rank $4$ vector bundle $\mathscr{V}_{\alpha} \to S^4$ with $\mathscr{V}_{\alpha} = B^4 \times \mathbb{R}^4 \cup_{S^{3} \times \mathbb{R}^4} B^4 \times \mathbb{R}^4$ where the projection is trivial along $B^4 \times \mathbb{R}^4$ and given by $(x, v) \mapsto (x, \alpha(x) v)$ along $S^3 \times \mathbb{R}^4$. We can choose a unit sphere bundle $S(\mathscr{V}_{\alpha}) = \partial B(\mathscr{V}_{\alpha}) \subseteq \mathscr{V}_{\alpha}$, the boundary of the ball bundle inside $\mathscr{V}_{\alpha}$. The map $S^3 \to S(\mathscr{V}_{\alpha}) \to S^4$. Write $\alpha_{ij}$ for the clutching functions corresponding to $X_{ij}$ above.

Now we make a general argument about such manifolds. Suppose $X$ is a $7$-fold that is the boundary of an $8$-fold $Y$. Then define $\lambda(X) = 2 p_{1}^{2}(Y) - \operatorname{sign} Y \in \mathbb{Z} / 7$. Note, it has to be shown that this does not depend on the choice of $Y$.

Note, if $i + j = 1$, then $X_{ij} \cong_{\mathsf{Top}} S^7$. This can be seen by [[UChicago --- uc-2026/notes/Morse theory#_definition, proposition _ the Morse complex, Morse homology|Morse theory]] — it suffices to give a function with two critical points, telling us that $X_{ij}$ is glued from a $7$-cell and a $0$-cell. This function comes from the quaternionic interpretation of the gluing we gave for $S^7$. Note Morse theory cannot tell that two spaces are diffeomorphic because it does not care about how you glue the spaces together as long as its along a diffeomorphism. We're gluing together two $B^7$s along a diffeomorphism of $S^6$, but $\operatorname{Aut}_{\mathsf{Diff}} S^6$ is not connected and so we could glue along a very non-trivial diffeomorphism.

Note $\lambda(X_{ij}) = (i - j)^{2} - 1$. Thus, $S^7 \cong_{\mathsf{Diff}} X_{1, 0} \not \cong_{\mathsf{Diff}} X_{2, -1} \cong_{\mathsf{Top}} S^7$.

---

##### _lemma:_ $\lambda(X)$ does not depend on the bounding manifold

###### _proof sketch:_

Suppose $X$ is a $7$-fold and $Y, Z$ are $8$-folds with boundary $\partial Y = X = \partial Z$. Let $Z'$ be $Z$ with the opposite orientation. Then $W = Y \cup_{X} Z'$ is an oriented closed $8$-fold with $\operatorname{sign} W= \operatorname{sign} Y - \operatorname{sign} Z$ and $p_{1}^{2}(W) = p_{1}^{2}(Y) - p_{1}^{2}(Z)$. That is, $\lambda(\partial W) = \lambda(\partial Y) - \lambda(\partial Z)$.

But then, by the [[UChicago --- uc-2026/notes/Algebraic invariants for manifolds#Hirzebruch signature formula|Hirzebruch signature formula]],
$$
\operatorname{sign} W = \frac{7 p_{2}(W) - p_{1}^{2}(W)}{45} \equiv_{7} \frac{- p_{1}^{2}(W)}{45} \equiv_{7}2 p_{1}^{2}(W) \in \mathbb{Z} / 7
$$
But then this tells us that $\operatorname{sign} W - 2 p_{1}^{2}(W) = 0 \in \mathbb{Z} / 7$ and so $\lambda(\partial Y) - \lambda(\partial Z) = 0$.

---

### Kervaire invariant problem

Michael Kervaire decided to upstage Milnor by constructing a topological manifold that admits no smooth structures! He did this by plumbing.

##### _theorem:_ Kervaire's smoothless manifold

There exists a compact topological $10$-fold admitting no smooth structure.

###### _proof sketch:_

The idea of plumbing is as follows. Choose a bilinear form $\beta : M \otimes M \to \mathbb{Z}$ on a free $\mathbb{Z}$-module $M$. Choose $\beta$ to be symmetric or alternating based on whether $n$ is $0, 2 \in \mathbb{Z} / 4$. Plumbing builds a manifold $X$ with Poincaré duality [[UChicago --- uc-2026/notes/Algebraic invariants for manifolds#_definition _ intersection form on cohomology, signature of a manifold|intersection form]] given by $\beta$. For $n = 2 \in \mathbb{Z} / 4$ we choose $\beta$ to be the alternating form given by $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. If $n = 0 \in \mathbb{Z} / 4$ we choose $\beta$ given by the matrix $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.

Let $n = 2m$. Then let the plumbing manifold $P$ be the union of ball bundles in the tangent bundles of $m$-spheres with a non-trivial gluing. That is, we glue together $P^{2m} = B(\mathscr{T}_{S^m}) \cup_{B^m \times B^m} B(\mathscr{T}_{S^m})$ with the swap gluing $(x, y) \mapsto (y, x)$ over the discs $B^m \subseteq S^m$ where $B(\mathscr{T}_{S^m \mid B^m}) = B^m \times B^m$. Since $\mathscr{T}_{S^m \mid D^m}$ is trivial, this mostly looks like doing nothing, except at one point where you swap. 

You can see what this looks like for $P^{2 \times 1}$ explicitly. Drawing along the boundary you see $\partial P^{2} = S^1$. This is true in general — $\partial P^{2m} = S^{2m - 1}$. $P^{2m}$ realises $\beta$ as its intersection pairing. Looking at the two different $S^m$s in $H^m(P^{2m}, \mathbb{Z})$ gives the desired form. 

It turns out that $P^{2m}$ is **parallelisable** since $\mathscr{T}_{P^{2m}}$ is trivial. 

A **framing** of a (closed) parallelisable $n$-fold with smooth structure is a choice of $n$ global sections $v_{i} \in \Gamma(\mathscr{T}_{X})$ such that the germs of the $v_{i}$ form a basis of $\mathscr{T}_{X, x}$ at each $x \in X$. Note, if $n = 2 \in \mathbb{Z} / 4$, then reduction of the intersection form modulo $2$ gives a bilinear over $\mathbb{F}_{2}$ (note that alternating forms become symmetric modulo $2$). Further, the framing actually gives a quadratic form $q$, and there is a framing--invariant — the **Arf invariant** $\operatorname{Arf} q$ (this is an invariant of quadratic forms over $\mathbb{F}_{2}$ in general). For a parallelisable $n$-fold, we say the Arf invariant of

Close $P^{2m}$ by joining a ball to its boundary. Call this $X$ and assume, by way of contradiction, that it has a smooth structure. Then you can compute that $\operatorname{Krv} X = 1$. But Kervaire invariants are related to cobordism groups which are just maps from stable homotopy groups of spheres, which tells you that $\operatorname{Krv} X^{10} = 0$ for any smooth $4$-connected $10$-fold.

Also, note that if $\partial P^{20}$ were diffeomorphic to a sphere, we could get a smooth structure. Thus, $\partial P^{20}$ is an exotic $9$-sphere.

---