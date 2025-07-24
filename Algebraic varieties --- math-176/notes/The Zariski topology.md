---
tags:
- math-176/30
- alg-geo
- top
---

A variety is very obviously a geometric object. If we understand it as something more than just a set of points in affine space, what is the new topology we have on it?

##### _definition:_ the Zariski topology

The Zariski topology on an [[Algebraic varieties --- math-176/notes/Non-singular projective varieties#_definition _ affine variety|affine variety]] $X$ is defined by its closed sets — $V \subset X$ is closed if $V = Z(I)$ is the [[Algebraic varieties --- math-176/notes/Non-singular projective varieties#_definition _ zero set, $Z(I)$|zero set]] of a subset of an ideal $I \subset F[x_{1}, \dots, x_{n}]$.

Of course, we should verify that this is indeed a topology — that $\emptyset, X$ are open, that arbitrary unions and finite intersections of open sets are open.