---
tags:
- math-199DR/19
- cx-geo
- alg-geo
---

One thing that we might be interested in as we think of Riemann surfaces, say $X$, more algebraically, is embedding them in projective space.

##### _definition:_ holomorphic maps to projective space

A holomorphic map from $X$ to projective space

##### _definition:_ meromorphic map to projective space

Given [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ meromorphic|meromorphic functions]] $f_{0}, \dots, f_{n} \in \mathcal{M}_{X}(X)$, a meromorphic map to projective space is $\varphi : X \to \mathbb{P}^n$ is given by
$$
\varphi(p) = (f_{0}(p) : \dots : f_{n}(p))
$$
at $p$ where $m_{p} = \min \{ \operatorname{ord}_{p}f_{i} \} = 0$ (points where there are no poles and at least one non-zero $f_{i}$). If $m_{p} \neq 0$, we can still normalise to get
$$
\varphi(p) = (z^{-m_{p}} f_{0}(z) : \dots : z^{-m_{p}} f_{n}(z))
$$
without changing the function in a local coordinate $z$.