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