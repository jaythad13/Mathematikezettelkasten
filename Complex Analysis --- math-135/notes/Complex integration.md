---
tags:
- math-135/3
- anal
- complex
---

In order to integrate functions and accumulate the change between two points, we need to integrate along a curve. Specifically, we want to make sure that we integrate only in one direction and don't go over any points twice. That's why

##### _definition:_ (oriented) curve, curve parametrisation

A parametrisation of a curve $\gamma$ is a smooth, continuously differentiable function $z_{\gamma} : [a, b] \to \mathbb{C}$ with $z_{\gamma}'(t) \neq 0$ at any point.

An (oriented) curve is an equivalence class of all parametrised curves with the same image that can be transformed into each other by a smooth bijection $s$ with $s' > 0$ always. Two curves with parametrisations that have the same image, but require a smooth bijection $s$ with $s' < 0$ always, to transform one into the other, is said to have opposite orientation to the original curve.

##### _definition:_ integral over a curve

The integral of a continuous function $f : \gamma \to \mathbb{C}$ over a curve $\gamma$ with parametrisation $z_{\gamma} : [a, b] \to \mathbb{C}$ is
$$
\int_{\gamma} f(z) \, dz = \int_{a}^b f(z_{\gamma}(t)) z'_{\gamma}(t)\, dt
$$

It's easy to show that the integral doesn't depend on the parametrisation of the curve.

##### _definition:_ length

The length of a curve $\gamma$ with parametrisation $z_{\gamma} : [a, b] \to \mathbb{C}$ is
$$
\operatorname{length}(\gamma) = \int_{a}^b \lvert z_{\gamma} \rvert  \, dt 
$$


##### _proposition:_ $ML$ bound

Given a curve $\gamma$, parameterised by $z_{\gamma} : [a, b] \to \mathbb{C}$, $M = \sup \{ f(z) \mid z \in \gamma\}$, and $L = \operatorname{length}(\gamma)$, for any continuous function $f: \gamma \to \mathbb{C}$,
$$
\left \lvert \int_{\gamma} f(z) \, dz \right \rvert \le ML.
$$

##### _theorem:_ fundamental theorem of calculus

Suppose $f$, a function on the open set $\Omega$, has a primitive $F$ that gives $F' = f$ everywhere on $\Omega$. Then, for any curve $\gamma$, with endpoints $w_{1}$ and $w_{2}$.
$$
\int_{\gamma} f(z) \, dz = F(w_{2}) - F(w_{1})
$$