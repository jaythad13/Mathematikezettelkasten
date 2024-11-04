---
tags:
- math-135/14
- math-135/15
- math-135/16
- anal
---

The Paley-Wiener theorem describes an interesting connection between the support of the Fourier transform of a function and its behaviour in the complex plane in general. In particular, it shows that the support of $\hat{f}$ is bounded in $[-M , M]$ if and only if $f$ has an entire extension to $\mathbb{C}$ that grows slower than an exponential (depending on $M$). Essentially, complex differentiable functions [[Complex Analysis --- math-135/notes/What is complex analysis?|are really nice]] in yet another way, and are uniquely so — they have nicer Fourier transforms.

For some of the theorems in this note, we do not assume that $f$ is holomorphic, but we do assume that [[Complex Analysis --- math-135/notes/Fourier analysis and holomorphic functions#_theorem _ the Fourier inversion formula|the Fourier inversion formula]] holds. Proofs of necessary conditions for this result are not part of this class.

##### _theorem:_ exponential Fourier transforms have holomorphic functions

If $\hat{f}$ satisfies the decay condition $\lvert \hat{f}(\xi) \rvert \leq A e^{2 \pi a \lvert \xi \rvert}$ for some $a, A \in \mathbb{R}$, then $f$ can be extended to a holomorphic function on any horizontal strip $S_{b} = \{ z \mid \lvert \operatorname{Im} z  \rvert < b \}$ for any positive $b < a$.

###### _proof sketch:_

Define the sequence of entire functions $f_{n}$ by
$$
f_{n}(z) = \int_{-n}^n \hat{f}(\xi) e^{2 \pi i \xi z}  \, d\xi 
$$
and
$$
f(z) = \int_{-\infty}^\infty \hat{f}(\xi) e^{2 \pi i \xi z} \, d\xi \le A \int_{-\infty}^\infty e^{- 2 \pi a \lvert \xi \rvert } e^{2 \pi b \lvert \xi \rvert } \, d\xi 
$$
which must then converge for $b < a$.

Also,
$$
\lvert f(z) - f_{n}(z) \rvert \le A \int_{-\infty}^{-n} e^{-2 \pi a \lvert \xi \rvert } e^{2 \pi b \lvert \xi \rvert } \, d\xi + A \int_{n}^{\infty} e^{-2 \pi a \lvert \xi \rvert } e^{2 \pi b \lvert \xi \rvert } \, d\xi
$$
which converges to $0$ as $n \to \infty$, and thus, $f_{n} \to f$.

##### _corollary:_ exponential Fourier transforms of locally zero functions are zero

If $\hat{f}(\xi) = \mathcal{O}(e^{-2 \pi a \lvert \xi \rvert})$, $a > 0$, and $f$ vanishes on some non-empty open interval, then $f = 0$ everywhere.

###### _proof sketch:_

This is just a consequence of [[Complex Analysis --- math-135/notes/Cauchy integral formula#_theorem _ identity theorem|the identity theorem]].

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
 & \le (2M) \sup_{\xi \in [-M, M]} \lvert \hat{f}(\xi) \rvert \lvert e^{-2 \pi y \xi} \rvert \\
 & = Ae^{2 \pi M y}  \\
 & = A e^{2 \pi M \lvert z \rvert }.
\end{split}
$$

Now suppose $f$ has an entire extension $f$ with $\lvert f(z) \rvert < A e^{2 \pi M \lvert z \rvert}$. Notice that the boundedness of $\operatorname{supp} \hat{f}$ implies a stronger condition than $\lvert f(z) \rvert \le A e^{2 \pi M \lvert z \rvert}$. In particular, it gives us $\lvert f(z) \rvert \le A e^{2 \pi M \lvert \operatorname{Im} z \rvert}$. Thus, to prove the converse, we need a variant of the maximum modulus principle to tighten the bound on $f$ 

![[#_theorem _ the Phragmén-Lindelöf principle]]

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
and recall that $f$ has moderate decrease, so $f$ doesn't blow up faster than $1/(1 + i \varepsilon x)^{2} \to 1$ as $\varepsilon \to 0$. (This is rigorous with dominated convergence).

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
where the last step follows by just evaluating the integral.

This clearly goes to zero as $y \to \infty$, so we must have $\hat{f^+_{\varepsilon}}(\xi) = 0$, and thus $\hat{f}(\xi) = 0$.

We can conclude the similarly for $\xi < -M$ using
$$
f^-_{\varepsilon}(z) = \frac{f(z)}{(1 - i \varepsilon z)^{2}}.
$$

##### _theorem:_ characterising functions with no negative frequencies

Suppose $f, \hat{f}$ are continuous with moderate decrease. Then $\hat{f}(\xi) = 0$ for all $\xi < 0$ if and only if $f$ can be extended to a continuous bounded function on the closed upper half plane with $f$ holomorphic in the upper half plane.

###### _proof sketch:_

Bound $f$ using the Fourier inversion formula and the moderate decrease of $\hat{f}$. Show it is holomorphic by truncating the Fourier inversion formula and considering these truncated integrals to be a [[Complex Analysis --- math-135/notes/Cauchy integral formula#_proposition _ uniform convergence preserves holomorphicity|sequence of uniformly convergent holomorphic functions]] converging to $f$. 


##### _theorem:_ the Phragmén-Lindelöf principle

Suppose $f$ is holomorphic in the infinite sector $S$ (for example, $\{ z \mid -\pi/4 < \operatorname{arg} z < \pi / 4 \}$) and continuous on its closure. If $\lvert f(z) \rvert \le 1$ on $\partial S$ and $\lvert f(z) \rvert \le C e^{c \lvert z \rvert}$ for some $c, C \in \mathbb{R}$, then $f(z) < 1$ everywhere in $S$.

###### _proof:_

Again, we create an $\varepsilon$ of room. Specifically, we consider $f_{\varepsilon} : z \mapsto f(z) e^{-\varepsilon z^{3/2}}$. (We choose the principle branch of the square root that halves arguments in $[-\pi, \pi]$, and is thus, continuous on $S$). We will show that $\lvert f_{\varepsilon}(z) \rvert \le 1$ in $\overline{S}$ by using the maximum modulus principle, and then let $\varepsilon \to 0$ to show that $f$ must also be bounded.

First we show that $f_{\varepsilon}$ is bounded. Notice that we can bound the exponential by the real part of $\lvert z \rvert^{3/2}$. For $\operatorname{Arg} z = \theta$,
$$
\begin{split}
\lvert f_{\varepsilon}(z) \rvert & \le f(z) \lvert e^{- \varepsilon z^{3 / 2}} \rvert \\
 & \le C e^{c \lvert z \rvert } e^{-\varepsilon \lvert z \rvert^{3/2} \cos(3 \theta / 2) } \\
\end{split}
$$
But $\cos (3 \theta / 2)$ is strictly positive because of the sector we're working in (specifically, $- \pi / 2 < 3 \theta / 2 < \pi / 2$). Thus,
$$
\lvert f_{\varepsilon}(z) \rvert \le C e^{c \lvert z \rvert  - a \varepsilon \lvert z \rvert^{3/2}}
$$
where $a$ depends only on the argument of $z$. Thus, as $\lvert z \rvert \to \infty$ along a particular direction from the origin, $\lvert f_{\varepsilon} \rvert \to 0$.

Since $f_{\varepsilon} \to 0$, there is some radius $R$ outside which it is always less than $1$. Thus, we can work in the bounded sector $S_{c} = \{ z \in S \mid \lvert z \rvert < R \}$ (outside which $\lvert f_{\varepsilon} \rvert < 1$).

Let $M$ be the supremum of $f_{\varepsilon}$ on $\overline{S}$ and let $z_{n}$ be a sequence with $\lvert f_{\varepsilon}(z_{n}) \rvert \to M$. Since $f_{\varepsilon} \to 0$ as $\lvert z \rvert \to \infty$, we know that if $z_{n} \to \infty$, $M < 1$. Else, $z_{n}$ converge to some $z$ inside $S_{c}$, at which $f_{\varepsilon}$ achieves a maximum. By the [[Complex Analysis --- math-135/notes/The argument principle and winding number#_theorem _ the maximum modulus principle|maximum modulus principle]], $z$ is on the boundary $\partial S_{c} \subset \partial S$ where we already have that $\lvert f_{\varepsilon}(z) \rvert \le 1$.

##### _theorem:_ Lebesgue dominated convergence theorem

> If you have a lemon, and all your functions live inside the lemon, then it's okay to change the order of limits and integration.

\- Curtis McMullen