---
tags:
- math-135/14
- math-135/15
- anal
---

The Paley-Wiener theorem describes an interesting connection between the support of the Fourier transform of a function and its behaviour in the complex plane in general. In particular, it shows that the support of $\hat{f}$ is bounded in $[-M , M]$ if and only if $f$ has an entire extension to $\mathbb{C}$ that grows slower than an exponential (depending on $M$). Essentially, complex differentiable functions [[Complex Analysis --- math-135/notes/What is complex analysis?|are really nice]] in yet another way, and are uniquely so — they have nicer Fourier transforms.

For some of the theorems in this note, we do not assume that $f$ is holomorphic, but we do assume that [[Complex Analysis --- math-135/notes/Fourier analysis and holomorphic functions#_theorem _ the Fourier inversion formula|the Fourier inversion formula]] holds. Proofs of necessary conditions for this result are not part of this class.

##### _theorem:_ sub-exponential Fourier transforms have holomorphic functions

If $\hat{f}$ satisfies the decay condition $\lvert \hat{f}(\xi) \rvert \leq A e^{2 \pi a \lvert \xi \rvert}$ for some $a, A \in \mathbb{R}$, then $f$ can be extended to a holomorphic function on any horizontal strip $S_{b} = \{ z \mid \lvert \operatorname{Im} z  \rvert < b \}$ for any positive $b < a$.

##### _corollary:_ sub-exponential Fourier transforms of locally zero functions are zero

If $\hat{f}(\xi) = \mathcal{O}(e^{-2 \pi a \lvert \xi \rvert})$, $a > 0$, and $f$ vanishes on some non-empty open interval, then $f = 0$ everywhere.

##### _theorem:_ Paley-Wiener theorem

Suppose $f : \mathbb{R} \to \mathbb{C}$ is continuous and is of moderate decrease on $\mathbb{R}$. 

Then $f$ has an entire extension $g : \mathbb{C} \to \mathbb{C}$ with $\lvert g(z) \rvert \le A e^{2 \pi M \lvert z \rvert}$ if and only if the support of the Fourier transform is bounded in some $[-M, M]$.

###### _proof:_

Suppose $\operatorname{supp}(\hat{f}) \subset [-M, M]$. Thus, $\hat{f}$ is continuous and of [[Complex Analysis --- math-135/notes/Fourier analysis and holomorphic functions#_definition _ moderate decrease|moderate decrease]] and the Fourier inversion formula holds. That is,
$$
f(x) = \int_{-M}^M \hat{f}(\xi) e^{2 \pi i x \xi} \, d\xi.
$$
Thus, we can define the entire extension
$$
g(z) = \int_{-M}^M \hat{f}(\xi) e^{2 \pi i z \xi}  \, d\xi.
$$
To see that this is entire, write it as a sequence of uniformly convergent Riemann sums and use our result on [[Complex Analysis --- math-135/notes/Cauchy integral formula#_proposition _ uniform convergence preserves holomorphicity|sequences of holomorphic functions]]. We can show that it is bounded as
$$
\begin{split}
\lvert g(z) \rvert & \le \int \lvert \hat{f}(\xi) \rvert \lvert e^{2 \pi i(x + i y)} \rvert  \, d\xi \\
 & \le 
\end{split}
$$

To prove the converse, we need a variant of the maximum modulus principle to tighten the bound on $f$ —

![[#_theorem _ the Phragmén-Lindelöf theorem]]

Using this, we can strengthen our bound to $\lvert f(z) \rvert \le A e^{2 \pi M \lvert \operatorname{Im} z \rvert}$.

Here we use the "epsilon of room" trick — we consider
$$
f_{\varepsilon}(z) = \frac{f(z)}{(1 + i \varepsilon z)^{2}}
$$
where $f_{\varepsilon} \to f$ as $\varepsilon \to 0$. We also claim that $\hat{f_{\varepsilon}} \to \hat{f}$. To see this, note that 
$$
\begin{split}
\lvert \hat{f}_{\varepsilon}(\xi) - \hat{f}(\xi) \rvert \le \left\lvert  \int_{-\infty}^{\infty} f(x) \left( \frac{1}{(1 + i \varepsilon x)^{2}} - 1 \right) e^{- 2 \pi i x \xi} \, dx   \right\rvert 
\end{split} 
$$

We show that the $\hat{f}_{\varepsilon}$ satisfy stronger bounds.
##### _theorem:_ the Phragmén-Lindelöf theorem

Suppose $f$ is holomorphic in the sector $S = \{ z \mid -\pi/4 < \operatorname{arg} z < \pi / 4 \}$ and continuous on its closure. If $\lvert f(z) \rvert \le 1$ on $\partial S$ and $\lvert f(z) \rvert \le C e^{c \lvert z \rvert}$ for some $c, C \in \mathbb{R}$, then $f(z) < 1$ everywhere in $S$.

##### _theorem:_ Lebesgue dominated convergence theorem

> If you have a lemon, and all your functions live inside the lemon, then it's okay to change the order of limits and integration.

\- Curtis McMullen
