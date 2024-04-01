---
tags:
- math-142
- diff-geo
lecture:
- math-142-26
---

### From curves to surfaces

We [[Vector fields#Curves|defined a curve]] as the image of a smooth map from an open interval $I \subset \mathbb{R}$ to $\mathbb{R}^3$. It allowed us to specify points on the $1$-dimensional curve with just one coordinate. How can we extend this to surfaces?

A "smooth surface" should then, by extension, be something like the image of a smooth map from an open subset of $\mathbb{R}^2$ to $\mathbb{R}^3$. Getting the specifics of the map and the open subset is what we want to understand.

### Some (metric) topology

We will use the same definition of "openness" [[Metric spaces#_definition _ open set|as in Rudin]], just restricted to $\mathbb{R}^2$. That is,

##### _definition:_ open sets

A subset $D \subset \mathbb{R}^2$ is said to be an open set if for any point $p \in D$, there exists $\delta > 0$ such that the disc of radius $\delta$, centred at $p$, $B_{\delta}(p)$ is contained in $D$.

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

###### _proof:_