---
tags:
- math-142
- diff-geo
lecture:
- math-142-26
- math-142-27
---

### From curves to surfaces

We [[Vector fields#Curves|defined a curve]] as the image of a smooth map from an open interval $I \subset \mathbb{R}$ to $\mathbb{R}^3$. It allowed us to specify points on the $1$-dimensional curve with just one coordinate. How can we extend this to surfaces?

A "smooth surface" should then, by extension, be something like the image of a smooth map from an open subset of $\mathbb{R}^2$ to $\mathbb{R}^3$. Getting the specifics of the map and the open subset is what we want to understand.

### Some (metric) topology

We will use the same definition of "openness" [[Metric spaces#_definition _ open set|as in Rudin]], just restricted to $\mathbb{R}^n$. That is,

##### _definition:_ open sets

A subset $U \subset \mathbb{R}^n$ is said to be an open set if for any point $p \in U$, there exists $\delta > 0$ such that the ball of radius $\delta$, centred at $p$, $B_{\delta}(p)$ is contained in $U$.

Here is a standard result about open sets [[Open and closed sets|from analysis]]:

![[Open and closed sets#_proposition _ (Potentially infinite) unions and finite intersections of open sets are open]]

It then becomes natural to try to extend these definitions to subsets of $\mathbb{R}^3$.

##### _definition:_ subspace neighbourhoods

For any $M \subset \mathbb{R}^3$, given $p \in M$, a neighbourhood of $p$ in $M$ is a subset $N \subset \mathbb{R}^3$ such that
$$
N = \{ q \in \mathbb{R}^3 \mid d(p, q) < \varepsilon, q \in M \}.
$$
Note that $N = B_{\varepsilon}(p) \cap M$.

##### _definition:_ subspace open sets

For some $M \subset \mathbb{R}^3$, $U \subset M$ is open in $M$ if for every $p \in U$, there exists a neighbourhood $N$ of $p$ in $M$ with $N \subset U$.

##### _proposition:_ the subspace topology is a topology

Arbitrary unions and finite intersections of open subsets in a subset $M \subset \mathbb{R}^3$ are open in $M$.

###### _proof sketch:_

Since the open sets of $M$ are exactly the intersections of open sets in $\mathbb{R}^3$ with all of $M$, we can just union and intersect them using the fact about unions and finite intersections of open sets in $\mathbb{R}^3$ and the fact that intersections (here, with $M$) distribute over unions and commute with other intersections.

Alternatively, since $M$ is definitely a metric space with the same metric, which induces the same neighbourhoods, and our proof didn't care about $\mathbb{R}^3$, it follows directly.

##### _examples:_ the trivial open sets in any $M \subset \mathbb{R}^3$

For any $M \subset \mathbb{R}^3$, both $\emptyset$ and $M$ are open in $M$ (in fact, this is true for $M \subset X$ for any metric space $X$).

### So what's a surface?

If we want a surface to be something that looks like $\mathbb{R}^2$, at least topologically, we should have a notion of what it means for a set in $\mathbb{R}^3$ to look like $\mathbb{R}^2$. Coordinate patches formalise this notion, allowing us to patch together a surface from neighbourhood that each look like $\mathbb{R}^2$, but allow their whole to be something different.

##### _definition:_ coordinate patch

A function $x : D \to \mathbb{R}^3$ for $D \subset \mathbb{R}^2$ is a coordinate patch if
- $x$ is a [[Maps on Euclidean space#_definition _ mapping|mapping]] (it is $\mathcal{C}^\infty$),
- $x$ is injective,
- $x$ is [[Maps on Euclidean space#_proposition _ regularity|regular]] — that is, $D \mathbf{x}$ has rank $2$ everywhere.

This means that the image of $D$ in $\mathbb{R}^3$ looks like $D$, but it could identify points that aren't identified in $D$. To prevent this, we define

##### _definition:_ proper patch

A coordinate patch $x : D \to \mathbb{R}^3$ is a proper patch if it has [[Continuity#_definition _ continuity at point, continuous function|continuous]] inverse $x ^{-1}$.

##### _definition:_ surface

A subset $M \subset \mathbb{R}^3$ is a surface if there is a family of maps $\{ x_{\alpha} \}$ with $x_{\alpha} : D_{\alpha} \to \mathbb{R}^3$ indexed by $\alpha \in I$ such that, for each $\alpha \in I$
- $D_{\alpha}$ is open in $\mathbb{R}^2$,
- $x_{\alpha} : D_{\alpha} \to \mathbb{R}^3$ is a proper patch,
- For each $p \in M$, there exists a neighbourhood $N$ of $p$ in $M$ such that $N \subset x_{\alpha}^\text{img}(D_{\alpha})$ for each $\alpha \in I$.

##### _example:_ the $xy$-plane is a surface

The $xy$-plane, $M = \{ (u, v, 0) \in \mathbb{R}^3 \}$ is a surface in $\mathbb{R}^3$. We can see that this is true by defining just on map $x : \mathbb{R}^2 \to M$ by $(u, v) \mapsto (u, v, 0)$.

We know that $\mathbb{R}^2$ is open in $\mathbb{R}^2$. We know that $x$ is a coordinate patch because it is clearly smooth and injective and its derivative has matrix $\begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0\end{bmatrix}$ which clearly has rank $2$.

It is proper because $x ^{-1} : (u, v, 0) \mapsto (u, v)$ is clearly continuous since for any open set around $(u_{0}, v_{0})$, the corresponding pre-image is just exactly the same set in embedded in $\mathbb{R}^3$. It must be open, since for any open neighbourhood about a point in the set in $\mathbb{R}^2$, we can draw an open ball in $\mathbb{R}^3$ such that it intersects $M$ in exactly that open neighbourhood.

##### _example:_ the sphere is a surface

The sphere $S^2 = \{ \mathbf{p} \in \mathbb{R}^3 \mid \lVert \mathbf{p} \rVert = 1\}$ is a surface in $\mathbb{R}^3$.

We can see this by looking at the coordinate patch $x : D \to \mathbb{R}^3$ by $(u, v) \mapsto(u, v, \sqrt{ 1 - u^{2} - v^{2} })$ where $D$ is the unit open disk centred at the origin.

$x$ is smooth since it is composed of smooth functions (the square root is smooth everywhere that it isn't $0$). $x$ is definitely injective since the first two coordinates force inputs to be equal if outputs are equal. $x$ is regular which you can see by computing its matrix $\begin{bmatrix} 1 & 0 \\ 0 & 1 \\ a & b\end{bmatrix}$ where it doesn't matter what $a, b$ are — the rank is $2$ regardless.

$x$ is proper basically because $\sqrt{ 1 - u^2 - v^2 }$ has continuous inverse on its restricted domain — if it keeps points close to each other, then adding in the points $(u, v, \sqrt{ 1 - u^2 - v^2 })$ can't really move them far apart.

Note that here $x$ does not have a large enough image to cover all of the sphere, however, by symmetry, we can rotate the sphere around so that it's all fine. Note however, that we will not always be so lucky as to be able to use the same formula for all the patches.

##### _definition, proposition:_ Monge patches are regular

A patch of the form $x : D \to \mathbb{R}^3$ such that $x(u, v) = (u, v, f(u, v))$ where $f$ is smooth is called a Monge patch.

Monge patches are proper patches.
