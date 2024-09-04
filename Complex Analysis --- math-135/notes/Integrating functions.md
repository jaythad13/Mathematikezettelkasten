---
tags:
- math-135/3
- anal
---

In order to integrate functions and accumulate the change between two points, we need to integrate along a curve. Specifically, we want to make sure that we integrate only in one direction and don't go over any points twice. That's why

##### _definition:_ (oriented) curve, curve parametrisation

A parametrisation of a curve $\gamma$ is a smooth, continuously diffferentiable function $z : [a, b] \to \mathbb{C}$ with $z'(t) \neq 0$ at any point.

An (oriented) curve is an equivalence class of all parametrised curves with the same image that can be transformed into each other by a smooth bijection $s$ with $s' > 0$ always.

##### _definition:_ integral over a curve

##### _definition:_ length

##### _proposition:_ $ML$ bound

##### _theorem:_ fundamental theorem of calculus

### Cauchy-Goursat

The idea of Cauchy-Goursat is to show that primitives exist in the case of triangles, and use that to build up to the case of simple shapes.

###### _proof sketch:_

Do the dyadic triangle trick to get
$$
\left\lvert   \int_{\partial \Delta_{0}} f(z) \, dz \right  \rvert \le 4^n \left \lvert \int_{\partial \Delta_{n}} f(z) \, dz  \right \rvert 
$$
Then linearise $f(z)$ in an appropriately small triangle — the first parts go to zero because they have anti-derivatives and the error part is bounded by the $ML$ bound.
