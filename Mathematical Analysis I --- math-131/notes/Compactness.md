---
tags:
- math-131/7
- math-131/8
- math-131/9
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

### Characterising compact sets

What are the compact sets in any metric space? We will get a pretty good idea in general metric spaces $X$, and the best possible idea for $\mathbb{R}^n$.

##### _theorem:_ compact sets are closed and bounded

If $K$ is compact, it is closed and bounded.

###### _proof:_

First we show $K$ is bounded. Consider the open cover of $K$ by picking $x \in K$, and considering all $B_{r}(x)$ where $r \in \mathbb{N}$. Then, the open cover of $K$ reduces to a finite subcover, which has a maximum radius $R$. Thus, $K$ is bounded — it is within distance $R$ of $x$.

Now we show that $K$ is closed. Consider any $z \in K^c$. We can pick an open cover of $K$ that is an $r$-neighbourhood of each $x \in K$ such that $z \not\in N_{r}(x)$. In particular, pick $r = \frac{d(x, z)}{3}$. By compactness, we can reduce this cover to a finite subcover — $K \subset N_{r_{1}}(x_{1}) \cup \dots \cup N_{r_{n}}(x_{n})$ and take the minimum radius $r$. Then notice that $N_{r}(z) \subset K^c$. Else we'd have some $y$ within distance $r$ of $z$ and distance $r$ of some $x_{i}$. Then, by the triangle inequality $d(x_{i}, z) \le 2r$, but this impossible since $r > 0$ and $d(x_{i}, z) = 3r$.

Note that the converse isn't true. Consider the infinite-dimensional sphere — this is closed and bounded, but not compact. To see this, consider an open cover of neighbourhoods at each point $(0, \dots, 1, \dots )$, such that each $(0, \dots, 1, \dots)$ is covered by only one open set.

In fact, the converse is only true in complete spaces like $\mathbb{R}^n$. We will prove the converse for $\mathbb{R}^n$.

##### _theorem:_ Bolzano-Weierstrass theorem

Any infinite subset of a compact set has a limit point in the compact set.

###### _proof:_

Let $K \subset X$ be compact and $V \subset K$ be infinite. By way of contradiction, suppose $V$ has no limit point in $K$. Then for each $x \in K$, there is some $r > 0$ such that $N_{r}(x) \cap V \subset \{ x \}$.

Consider all of these $N_{r}(x)$. Since they cover $K$, some finite subcollection of them — $N_{r_{1}}(x_{1}), \dots, N_{r_{n}}(x_{n})$ also covers $K$. Thus, $V \subset K \subset \{ x_{1}, \dots, x_{n} \}$, and thus, $V$ is finite. This is a contradiction.

##### _theorem:_ intervals are compact

Any $n$-cell $I \subset \mathbb{R}^n$ is compact.

###### _proof sketch:_

We will show $I = [a_{1},  b_{1}] \times [a_{2}, b_{2}]$ is compact. It follows from a similar proof that $I = [a_{1}, b_{1}] \times \cdots \times [a_{n}, b_{n}]$ is compact. 

Suppose by way of contradiction that $I$ isn't compact with $\mathcal{O}$ an open cover that does not admit a finite subcover. Break $I$ into $2^n$ subparts. For example, in the case of $n = 2$, consider
$$
I = \left[ a_{1}, \frac{a_{1} + b_{1}}{2} \right] \times \left[ a_{2}, \frac{a_{2} + b_{2}}{2} \right] \cup \left[ \frac{a_{1} + b_{1}}{2}, b_{1} \right] \times \left[ \frac{a_{2} + b_{2}}{2}, b_{2} \right] \cup \left[ a_{1}, \frac{a_{1} + b_{1}}{2} \right] \times \left[ \frac{a_{2} + b_{2}}{2}, b_{2} \right] \cup \left[ \frac{a_{1} + b_{1}}{2}, b_{1} \right]  \times \left[ a_{2}, \frac{a_{2} + b_{2}}{2} \right].
$$
Set $I_{1}$ to be the subpart such that $I_{1}$ cannot be covered by a finite subcover of $\mathcal{O}$, and choose $I_{2}$, and so on recursively. Since the diameter of $I_{n} \to 0$, and the intersection is non-empty, then unless that point were not covered, we could squeeze a tiny $I_{n}$ into one of the open sets in the open cover.

In particular, we know that there is some $x \in I_{n}$ for all $I_{n}$ — nested intervals have a non-empty intersection. We also must have $x \in U$ for some $U \in \mathcal{O}$. Thus, we have some $N_{\varepsilon}(x) \subset U$. But then, for large enough $n$, we get that the diameter of $I_{n} < \frac{\varepsilon}{2}$. Thus, even if $I_{n}$ has $x$ right at its corner, $I_{n} \subset N_{\varepsilon}(x) \subset U$. Then $I_{n}$ is covered by a finite subcover of $\mathcal{O}$, which contradicts our hypothesis that each $I_{n}$ cannot be covered by a finite subcover of $\mathcal{O}$.

##### _lemma:_ closed $\cap$ compact is compact

The intersection of any compact $K$ and closed $V$ is compact.

###### _proof:_

If $\mathcal{O}$ is an open cover of $K \cap V$, then $\mathcal{O} \cup \{ V^c \}$ is an open cover of $K$. This admits a finite subcover of $K$, say $\{ U_{1}, \dots, U_{n}, V^c \}$ (with $U_{i} \in \mathcal{O}$). Now, $\{ U_{1}, \dots, U_{n} \}$ is a finite subcover of $V$ admitted by $\mathcal{O}$ since we can remove $V^c$ without changing whether this covers $V$.

##### _theorem:_ Heine-Borel theorem

For any set $E \subset \mathbb{R}^n$, the following are equivalent
1) $E$ is closed and bounded
2) $E$ is compact
3) Every infinite subset of $E$ has a limit point in $E$.

In fact, in any metric space, the statements "$E$ is compact" and "every infinite subset of $E$ has a limit point in $E$" are equivalent.

###### _proof:_

First we show 1) implies 2). Any closed and bounded set $E$ can be placed inside some interval $I$. Thus, $E = E \cap I$ and thus, since $E$ is the intersection of a closed set and a compact set, it is compact.

It follows from the [[#_theorem _ Bolzano-Weierstrass theorem|Bolzano-Weierstrass theorem]] that 2) implies 3).

Finally it's not too hard to show 3) implies 2).