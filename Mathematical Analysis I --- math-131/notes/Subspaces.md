---
tags:
- math-131/8
- anal
- top
---

If $X$ is a metric space with metric $d$, it's only natural to think that the same metric induces a metric space on any subset $Y \subset X$. That's what a subspace is —

##### _definition:_ metric subspace

Let $X$ be a metric space with metric $d$. Then any $Y \subset X$, endowed with the same metric space is called a subspace of $X$.

Note, that though the metric is the same, the structure of open sets is clearly not —

##### _example:_ open relative to a subspace

In $\mathbb{R}$, with the usual metric, $[0, 1/2)$ is not open, but in $[0, 1]$ with the same metric, $[0, 1 / 2)$ is all the points within distance $1 / 2$ of $0$, and thus, must be open.

We can get a complete characterisation of the topology of a subspace as follows

##### _theorem:_ the subspace topology

The set $U \subset Y$ is open in $Y$ if and only if $U = Y \cap V$ for some $V$ open in $X$.

###### _proof:_

If $U \subset Y$ is open in $Y$, then clearly
$$
U = \bigcup_{u \in U} \{ y \in Y \mid d(u, y) < r_{u} \} =  Y \cap \bigcup_{u \in U} \{ x \in X \mid d(u, x) < r_{u} \}
$$
where $r_{u}$ is the radius of the open ball around $u$ that we are guaranteed is contained in $U$ for any $u \in U$. Note that the rightmost union is an open set in $X$ as desired.

Suppose $V$ is open in $X$ and $U = Y \cap V$. Then for all $v \in V$, there is some $r > 0$ such that $\{ x \in X \mid d(v, x) < r \} \subset V$. Taking intersections with $Y$ on both sides, we get that for every $v \in V$,
$$
\{ y \in Y \mid d(v, y) < r \} \subset V \cap Y = U.
$$