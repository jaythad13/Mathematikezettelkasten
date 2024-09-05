---
tags:
- math-135/3
- anal
---

The idea of Goursat's theorem is to show that primitives exist for holomorphic functions on triangles, and use that to build up to the case of simple shapes.

##### _theorem:_ Goursat's theorem

For a triangle $\Delta_{0}$ contained in a region $\Omega \subset \mathbb{C}$, any function $f$, holomorphic on $\Omega$,
$$
\int_{\partial \Delta_{0}} f(z) \, dz = 0.
$$
###### _proof sketch:_

Do the dyadic triangle trick to get smaller and smaller triangles $\Delta_{n}$ where
$$
\left\lvert   \int_{\partial \Delta_{0}} f(z) \, dz \right  \rvert \le 4^n \left \lvert \int_{\partial \Delta_{n}} f(z) \, dz  \right \rvert 
$$

Since the triangles are compact sets that get arbitrarily small, [[Complex Analysis --- math-135/notes/(Metric) topology review#_proposition _ shrinking nested compact sets|their intersection is a single point ]] $z_{0}$.

Then linearise $f(z)$ in an appropriately small triangle (where the error is less than $\varepsilon$) —
$$
f(z) = f(z_{0}) + f'(z_{0})(z - z_{0}) + \psi(z)(z - z_{0}).
$$
The integrals of the first two terms are zero because they have anti-derivatives. The integral of the "error", $\psi(z)(z - z_{0})$, is bounded by the $ML$ bound — $\lvert \psi(z) (z - z_{0})  \rvert < \varepsilon \operatorname{length}(\Delta_{n})$
$$
\begin{split}
\left \lvert  \int \psi(z) (z - z_{0}) \, dz   \right\rvert & \le  \varepsilon \operatorname{length} (\Delta_{n})^{2} \\
 & \le \varepsilon \frac{\operatorname{length(\Delta_{0})^{2}}}{4^n}.
\end{split}
$$

Thus,
$$
\begin{split}
\left\lvert   \int_{\partial \Delta_{0}} f(z) \, dz \right  \rvert & \le 4^n \left \lvert \int_{\partial \Delta_{n}} f(z) \, dz  \right \rvert  \\
 & \le \varepsilon \operatorname{length}(\Delta_{0})^{2}
\end{split}
$$
and thus, must go to zero.

### Consequences