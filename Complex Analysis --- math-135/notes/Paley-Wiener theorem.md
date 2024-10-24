---
tags:
- math-135/14
- math-135/15
- anal
---

The Paley-Wiener theorem describes an interesting connection between the support of the Fourier transform of a function and its behaviour in the complex plane in general. In particular, it shows that the support of $\hat{f}$ is bounded in $[-M , M]$ if and only if $f$ has an entire extension to $\mathbb{C}$ that grows slower than an exponential (depending on $M$). Essentially, complex differentiable functions [[Complex Analysis --- math-135/notes/What is complex analysis?|are really nice]] in yet another way, and are uniquely so — they have nicer Fourier transforms.

For some of the theorems in this note, we do not assume that $f$ is holomorphic, but we do assume that [[Complex Analysis --- math-135/notes/Fourier analysis and holomorphic functions#_theorem _ the Fourier inversion formula|the Fourier inversion formula]] holds. Proofs of necessary conditions for this result are not part of this class.

##### _theorem:_ exponential Fourier transforms have holomorphic functions

If $\hat{f}$ satisfies the decay condition $\lvert \hat{f}(\xi) \rvert \leq A e^{2 \pi a \lvert \xi \rvert}$ for some $a, A \in \mathbb{R}$, then $f$ can be extended to a holomorphic function on any horizontal strip $S_{b} = \{ z \mid \lvert \operatorname{Im} z  \rvert < b \}$ for any positive $b < a$.

##### _corollary:_ exponential Fourier transforms of locally zero functions are zero

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
f(z) = \int_{-M}^M \hat{f}(\xi) e^{2 \pi i z \xi}  \, d\xi.
$$
To see that this is entire, write it as a sequence of uniformly convergent Riemann sums and use our result on [[Complex Analysis --- math-135/notes/Cauchy integral formula#_proposition _ uniform convergence preserves holomorphicity|sequences of holomorphic functions]]. We can show that it is bounded as
$$
\begin{split}
\lvert f(z) \rvert & \le \int_{-M}^M \lvert \hat{f}(\xi) \rvert \lvert e^{2 \pi i(x + i y) \xi} \rvert  \, d\xi \\
 & = \int_{-M}^M \lvert \hat{f}(\xi) \rvert \lvert e^{- 2 \pi y \xi} \rvert \lvert e^{- 2 \pi i x \xi} \rvert   \, d\xi \\
 & = \int_{-M}^M \lvert \hat{f}(\xi) \rvert e^{- 2 \pi y \xi}   \, d\xi \\
 & \le \sup_{\xi \in [-M, M]} \lvert \hat{f}(\xi) \rvert \lvert e^{-2 \pi y \xi} \rvert \\
 & = Ae^{2 \pi M y}  \\
 & = A e^{2 \pi M \lvert z \rvert }.
\end{split}
$$

Now suppose $f$ has an entire extension $f$ with $\lvert f(z) \rvert < A e^{2 \pi M \lvert z \rvert}$. Notice that the boundedness of $\operatorname{supp} \hat{f}$ implies a stronger condition than $\lvert f(z) \rvert \le A e^{2 \pi M \lvert z \rvert}$. In particular, it gives us $\lvert f(z) \rvert \le A e^{2 \pi M \lvert \operatorname{Im} z \rvert}$. Thus, to prove the converse, we need a variant of the maximum modulus principle to tighten the bound on $f$ 

![[#_theorem _ the Phragmén-Lindelöf theorem]]

Using this, we can strengthen our bound to $\lvert f(z) \rvert \le A e^{2 \pi M \lvert \operatorname{Im} z \rvert}$. Consider the function $F(z) = g(z) e^{2 \pi i M z}$. Note that $F / A \le e^{2 \pi M(z + i z)}$. If $z = x \in \mathbb{R}$, then
$$
\frac{F}{A} \le e^{2 \pi M x} \lvert e^{2 \pi M i x} \rvert = e^{2 \pi M x}.
$$
and if $z = iy$ for $y \in \mathbb{R}$, then
$$
\frac{F}{A} \le e^{- 2 \pi M y} \lvert e^{2 \pi M i y} \rvert = e^{- 2 \pi M y}
$$

Here we use the "epsilon of room" trick — we consider
$$
f^+_{\varepsilon}(z) = \frac{f(z)}{(1 + i \varepsilon z)^{2}}
$$
where $f^+_{\varepsilon} \to f$ as $\varepsilon \to 0$. Since $f^+_{\varepsilon}$ only has poles at $i / \varepsilon$, it is holomorphic and bounded in the closed lower half plane. We also claim that $\hat{f_{\varepsilon}^+} \to \hat{f}$. To see this, note that 
$$
\begin{split}
\lvert \hat{f^+_{\varepsilon}}(\xi) - \hat{f}(\xi) \rvert \le \left\lvert  \int_{-\infty}^{\infty} f(x) \left( \frac{1}{(1 + i \varepsilon x)^{2}} - 1 \right) e^{- 2 \pi i x \xi} \, dx   \right\rvert 
\end{split} 
$$
and recall that $f$ has moderate decrease, so $f$ doesn't blow up faster than $1/(1 + i \varepsilon x)^{2} \to 1$ as $\varepsilon \to 0$.

We show that the $f^+_{\varepsilon}$ satisfy stronger bounds — in particular, since $\varepsilon$ is fixed, we have
$$
f^+_{\varepsilon}(z) \le A \frac{e^{2 \pi M \lvert \operatorname{Im} z \rvert }}{1 + \lvert z \rvert ^{2}}
$$
by choosing the right $A$ so that
$$
\frac{1}{(1 + i \varepsilon z)^{2}} \le \frac{A}{1 + \lvert z \rvert^{2}}.
$$

Now suppose $\xi > M$. We can use the trick of shifting the Fourier transform integral down by $y > 0$ and combine it with our bound on $f$ in terms of $y$.
$$
\begin{split}
\hat{f^+_{\varepsilon}}(\xi) & = \int_{-\infty}^\infty f^{+}_{\varepsilon}(x) e^{2 \pi i \xi x}  \, dx \\
 & =  \int_{-\infty}^\infty f_{\varepsilon}^+(x - i y) e^{2 \pi i \xi (x - i y)} \, dx \\
 & \le \int_{-\infty}^\infty \frac{e^{2 \pi M y - 2 \pi \xi y} }{1 + x^{2}}  \, dx \\
 & = C e^{- 2 \pi y(\xi - M)}
\end{split}
$$
where the last step follows by Lebesgue dominated convergence.

This clearly goes to zero as $y \to \infty$, so we must have $\hat{f^+_{\varepsilon}}(\xi) = 0$, and thus $\hat{f}(\xi) = 0$.

We can conclude the similarly for $\xi < -M$ using
$$
f^-_{\varepsilon}(z) = \frac{f(z)}{(1 - i \varepsilon z)^{2}}.
$$

##### _theorem:_ the Phragmén-Lindelöf theorem

Suppose $f$ is holomorphic in the sector $S$ (for example, $\{ z \mid -\pi/4 < \operatorname{arg} z < \pi / 4 \}$) and continuous on its closure. If $\lvert f(z) \rvert \le 1$ on $\partial S$ and $\lvert f(z) \rvert \le C e^{c \lvert z \rvert}$ for some $c, C \in \mathbb{R}$, then $f(z) < 1$ everywhere in $S$.

##### _theorem:_ Lebesgue dominated convergence theorem

> If you have a lemon, and all your functions live inside the lemon, then it's okay to change the order of limits and integration.

\- Curtis McMullen
