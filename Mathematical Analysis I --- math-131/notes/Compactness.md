---
tags:
- math-131/7
- anal
- top
---

In linear algebra, bases allow us to differentiate between finite and infinite-dimensional vector spaces. In analysis and topology, we can use compactness to get an idea of finite-dimensionality. 

##### _definition:_ open cover

Let $X$ be a metric space and consider $K \subset X$. We say the collection of open sets $\{ G_{\alpha} \mid \alpha \in A \}$ is an open cover of $K$ if $K \subset \bigcup_{\alpha \in A} G_{\alpha}$.

##### _example:_ open cover

$K = (0, 1)$ is covered by all intervals $\left( 0, 1 - 1 / n \right)$. We can even do without some of these — get rid of all even $n$, or the first $N$ $n$, for your favourite value of $N$. 

Notice however that we need infinitely many of these sets to cover $K$ — if we were left with finitely many of them, there would be a largest $n$ such that only $(0, 1 - 1/n)$ was covered by the open sets.

It turns out that there are sets where this is not the case — you can always reduce down to a finite subset of the covering sets.

##### _definition:_ subcover

If the collection of open sets $\{ G_{\alpha} \mid \alpha \in A \}$ is an open cover of $K$, but also the collection $\{ G_{\alpha} \mid \alpha \in B \}$ is a cover of $K$ for $B \subset A$, we say $\{ G_{\alpha} \mid \alpha \in B \}$ is a subcover of $K$.

##### _definition:_ compact

A set $K$ is compact if every open cover of $K$ has a finite subcover.

##### _theorem:_ compact sets are closed and bounded

If $K$ is compact, it is closed and bounded.

###### _proof:_

First we show $K$ is bounded. Consider the open cover of $K$ by picking $x \in K$, and considering all $B_{r}(x)$ where $r \in \mathbb{N}$. Then, the open cover of $K$ reduces to a finite subcover, which has a maximum radius $R$. Thus, $K$ is bounded — it is within distance $R$ of $x$.

Now we show that $K$ is closed. Consider any $z \in K^c$. We can pick an open cover of $K$ that is an $r$-neighbourhood of each $x \in K$ such that $z \not\in N_{r}(x)$. In particular, pick $r = \frac{d(x, z)}{3}$. By compactness, we can reduce this cover to a finite subcover — $K \subset N_{r_{1}}(x_{1}) \cup \dots \cup N_{r_{n}}(x_{n})$ and take the minimum radius $r$. Then notice that $N_{r}(z) \subset K$. Else we'd have some $y$ within distance $r$ of $z$ and distance $r$ of some $x_{i}$. Then, by the triangle inequality $d(x_{i}, z) \le 2r$, but this impossible since $r > 0$ and $d(x_{i}, z) = 3r$.

Note that the converse isn't true. Consider the infinite-dimensional sphere — this is closed and bounded, but not compact. To see this, consider an open cover of neighbourhoods at each point $(0, \dots, 1, \dots )$, such that each $(0, \dots, 1, \dots)$ is covered by only one open set.

In fact, the converse is only true in complete spaces like $\mathbb{R}^n$. We will prove the converse for $\mathbb{R}^n$.

##### _theorem:_ Heine-Borel theorem

If $K \subset \mathbb{R}^n$ is closed and bounded, it is compact.

###### _proof sketch:_

We will show $I = [a_{1},  b_{1}] \times [a_{2}, b_{2}]$ is compact. It follows from a similar proof that $I = [a_{1}, b_{1}] \times \cdots \times [a_{n}, b_{n}]$ is compact. Finally, any closed and bonded set can be placed inside some interval $I$. Any open cover of $K$, together with its open complement $K^c$, forms an open cover of $I$. This can then be reduced to a finite subcover of $I$. We can remove $K^c$ from the subcover since it clearly doesn't cover $K$, and thus, we are left with a finite subcover of the original open cover of $K$.



Suppose by way of contradiction that $I$ isn't compact with $\mathcal{O}$ an open cover that does not admit a finite subcover. Break $I$ into $2^n$ subparts. For example, in the case of $n = 2$, consider
$$
I = \left[ a_{1}, \frac{a_{1} + b_{1}}{2} \right] \times \left[ a_{2}, \frac{a_{2} + b_{2}}{2} \right] \cup \left[ \frac{a_{1} + b_{1}}{2}, b_{1} \right] \times \left[ \frac{a_{2} + b_{2}}{2}, b_{2} \right] \cup \left[ a_{1}, \frac{a_{1} + b_{1}}{2} \right] \times \left[ \frac{a_{2} + b_{2}}{2}, b_{2} \right] \cup \left[ \frac{a_{1} + b_{1}}{2}, b_{1} \right]  \times \left[ a_{2}, \frac{a_{2} + b_{2}}{2} \right].
$$
Set $I_{1}$ to be the subpart such that $I_{1}$ cannot be covered by a finite subcover of $\mathcal{O}$, and choose $I_{2}$, and so on recursively. Since the diameter of $I_{n} \to 0$, and the intersection is non-empty, then unless that point were not covered, we could squeeze a tiny $I_{n}$ into one of the open sets in the open cover.

### Compact set magic

Compact sets give you results that are best described as magic — just see them. For this section, let $X$ be a metric space with metric $d$.

##### _theorem:_ Bolzano-Weierstrass theorem

Any infinite subset of a compact set has a limit point in the compact set.

###### _proof:_

Let $K \subset X$ be compact and $V \subset K$ be infinite. By way of contradiction, suppose $V$ has no limit point in $K$. Then for each $x \in K$, there is some $r > 0$ such that $N_{r}(x) \cap V \subset \{ x \}$.

Consider all of these $N_{r}(x)$. Since they cover $K$, some finite subcollection of them — $N_{r_{1}}(x_{1}), \dots, N_{r_{n}}(x_{n})$ also covers $K$. Thus, $V \subset K \subset \{ x_{1}, \dots, x_{n} \}$, and thus, $V$ is finite. This is a contradiction.