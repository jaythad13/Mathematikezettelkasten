---
tags:
- math-139/21
- math-139/22
- fourier
- anal
---

##### _definition:_ radial function

A function $f : \mathbb{R}^d \to \mathbb{R}$ is radial if it preserves rotations — for any rotation $R$, $f(Rx) = f(x)$ for all $x \in \mathbb{R}^d$.

Equivalently, $f$ is constant on each sphere centred at $0$ in $\mathbb{R}^d$, or $f$ is a function only of $\lVert x \rVert$.

##### _proposition:_ the Fourier transform of a radial function is radial

###### _proof:_

Suppose $f : \mathbb{R}^d \to \mathbb{R}$ is radial, and let $R$ be a rotation. Then
$$
\hat{f}(R \xi) = \widehat{(f \circ R)}(\xi) = \hat{f}(\xi).
$$