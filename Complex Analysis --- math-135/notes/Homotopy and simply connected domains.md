---
tags:
- math-135/9
- anal
---

##### _definition:_ homotopy

If there exists a family of curves
$$
\{ \gamma_{s} : [a, b] \to \Omega \mid s \in [0, 1] \}
$$
such that they all have common endpoints $\alpha, \beta$, and $\gamma : [0, 1] \times [a, b] \to \mathbb{C}$ by $(s, t) \to \gamma_{s}(t)$ is continuous, then we say $\gamma_{0}$ and $\gamma_{1}$ are homotopic.

##### _theorem:_ deformation theorem

If $\gamma_{0}$ and $\gamma_{1}$ are homotopic, then they have the same integral —
$$
\int_{\gamma_{1}} f = \int_{\gamma_{2}} f.
$$

###### _proof sketch:_

Show that for $s_{1}$ close to $s_{2}$, the integrals over $\gamma_{s_{1}}$ and $\gamma_{s_{2}}$ are the same. With enough clever compactness arguments, the difference of the integrals reduces to a telescoping sum with the end terms being the difference of $f$ evaluated on the end points of each curve which is just