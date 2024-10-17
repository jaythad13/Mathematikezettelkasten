---
tags:
- math-135/3
- math-135/4
- anal
---

### Goursat's theorem

The idea of Goursat's theorem is to show that primitives exist for [[Complex Analysis --- math-135/notes/Holomorphic functions|holomorphic function]] on triangles, and use that to build up to the case of simple shapes. From this we get Cauchy's theorem

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

Since the triangles are compact sets that get arbitrarily small, [[Complex Analysis --- math-135/notes/Analysis and (metric) topology review#_proposition _ shrinking nested compact sets|their intersection is a single point ]] $z_{0}$.

Then linearise $f(z)$ in an appropriately small triangle (where the error is less than $\varepsilon$) —
$$
f(z) = f(z_{0}) + f'(z_{0})(z - z_{0}) + \psi(z)(z - z_{0}).
$$
The integrals of the first two terms are zero because they have anti-derivatives. The integral of the "error", $\psi(z)(z - z_{0})$, is bounded by the $ML$ bound — $\lvert \psi(z) (z - z_{0})  \rvert < \varepsilon \operatorname{length}(\Delta_{n})$
$$
\begin{split}
\left \lvert  \int \psi(z) (z - z_{0}) \, dz   \right\rvert & \le  \varepsilon \operatorname{length} (\Delta_{n})^{2}/2 \\
 & \le \varepsilon \frac{\operatorname{length(\Delta_{0})^{2}}}{2\cdot4^n}.
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

Goursat's theorem is a lot of what underlies the rigidity of complex functions [[Complex Analysis --- math-135/notes/What is complex analysis?|that we talked about in the first lecture]].

##### _theorem:_ primitives in a disc

Suppose $D$ is an open disc in $\mathbb{C}$ and $f : D \to \mathbb{C}$ is holomorphic on $D$. Then $f$ has a primitive in $z$.

###### _proof sketch:_

Without loss of generality, we can assume that $D$ is centred at the origin. Consider $F(z) = \int_{\gamma_{z}} f(z) \, dz$ where $\gamma_{z}$ is the path from the origin to $z$ that goes horizontal and then vertical. We claim this is a primitive.

To show that $F' = f$, consider $F(z + h) - F(z)$ for any $h$ such that $z + h \in D$. Then by some geometry (cleverly doubling and cancelling paths) and an application of Goursat's theorem (to show that the integrals of $f$ over a rectangle and a triangle are both $0$), we get that
$$
F(z + h) - F(z) = \int_{\gamma} f(z) \, dz
$$
where $\gamma$ is the straight line from $z$ to $z + h$. Write $f(w) = f(z) + \psi(w)$ where $\psi(w) \to 0$ as $w \to z$ (we can do this because $f$ is continuous). Thus
$$
F(z + h) - F(z) = \int_{\gamma} f(z) \, dw + \int_{\gamma} \psi(w) \, dw
$$
taking limits as $h \to 0$, we can bound the second term since $\psi(w) \to 0$, and the first term is just $f(z) h$. Thus, dividing by $h$,
$$
\lim_{ h \to 0 }  \frac{F(z + h) - F(z)}{h} = f(z)
$$
as desired.

##### _corollary:_ Cauchy's theorem

If $f$ is a holomorphic in an open disc. and $\gamma$ is any closed curve in the disc, $\int_{\gamma} f(z) \, dz  = 0$. 

###### _proof sketch.:_

Apply [[Complex Analysis --- math-135/notes/Complex integration#_theorem _ fundamental theorem of calculus|the fundamental theorem of calculus]].

Most importantly, we can now get [[Complex Analysis --- math-135/notes/Cauchy integral formula|the representation theorem of complex analysis!]]