---
tags:
- math-135/21
- anal
---

Often in a real analysis course, one defines the gamma function as a function of real values. Here, we will define it on the complex right half plane. Further, we claim it is analytic there!

##### _definition:_ the gamma function

The gamma function is $\gamma : \{ s \mid \operatorname{Re} s > 0 \} \to \mathbb{C}$
$$
\Gamma(s) = \int_{0}^\infty e^{-t} t^{s - 1} \, dt.
$$

##### _proposition:_ the gamma function is analytic

Let $S_{\delta, M}$ be the strip $\{ s \mid \delta < \operatorname{Re} s < M \}$ for some $\delta > 0$. Notice that for each $\varepsilon > 0$, we can write
$$
F_{\varepsilon} = \int_{\varepsilon}^{1/\varepsilon} e^{-t} t^{s - 1}  \, dx 
$$
As per, $F_{\varepsilon}$ [[Complex Analysis --- math-135/notes/Cauchy integral formula#_proposition _ holomorphic functions defined by integrals|is holomorphic]], and thus, by proving $F_{\varepsilon} \to F$ in the strip uniformly, we have $F$ holomorphic in the strip.

The primary reason the gamma function is of interest of course is that it obeys the functional equation $\Gamma(s + 1) = s \Gamma(s)$, and since $\Gamma(1) = 1$, we have $\Gamma(n) = n!$!

##### _proposition:_ the gamma functional equation

Most importantly, the gamma function can be extended to a [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ meromorphic functions|meromorphic function]] on $\mathbb{C}$! 

##### _theorem:_ a meromorphic continuation of the gamma function

$\Gamma$ has a meromorphic continuation to the complex plane with simple poles at non-positive integers $n$ with simple poles with residue $(-1)^n / n!$ at each $n$.

###### _proof:_

The basic idea is to use the functional equation to define $\Gamma$. In particular, define $F_{1} = \Gamma(s + 1) / s$. Now clearly $F_{1}$ is meromorphic on $\{ \operatorname{Re} s > -1 \}$ and has a simple pole at $0$ with residue $\Gamma(0 + 1) = 1$. Similarly define $F_{2}(s) = F_{1}(s + 1) / s = \Gamma(s + 1) /s(s + 1)$. 

Thus, we inductively define
$$
F_{m}(s) = \frac{F_{m - 1}(s + 1)}{s} = \frac{\Gamma(s + m)}{(s + m - 1)(s + m - 2) \dots (s)}.
$$
as a meromorphic function on $\{ \operatorname{Re} s > - m \}$ with residue
$$
\lim_{ s \to -n } (s + n) F_{m}(s) = \frac{(n + m)!}{(m - 1 - n) \cdots (m - (m - n - 1) - n) (m -(m - n + 1) - n) \cdots (-n)} \lim_{ s \to -n } \frac{s + n}{s + n}
$$