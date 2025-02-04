---
tags:
- math-135/21
- math-135/22
- anal
- complex
---

Often in a real analysis course, one defines the gamma function as a function of real values. Here, we will define it on the complex right half plane, where we will show it is analytic. We will extend it to a meromorphic function on the whole plane and show that its reciprocal is entire!

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

The primary reason the gamma function is of interest of course is that it obeys the functional equation $\Gamma(s + 1) = s \Gamma(s)$, and since $\Gamma(1) = 1$, we have $\Gamma(n + 1) = n!$!

##### _proposition:_ the gamma functional equation

The gamma function satisfies the functional equation
$$
\Gamma(s + 1) = s \Gamma(s).
$$
Further, $\Gamma(n + 1) = n!$.


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

### The Hadamard factorisation of $\Gamma$

We will show now that $\Gamma$ does not vanish anywhere, so $1 / \Gamma$ can be extended to an entire function. Then we will show that $1 / \Gamma$ has finite [[Complex Analysis --- math-135/notes/Hadamard factorisation#_definition _ order of growth|order of growth]], and thus, we will be able to compute its [[Complex Analysis --- math-135/notes/Hadamard factorisation#_theorem _ Hadamard factorisation theorem|Hadamard factorisation]].

It turns out that we can 

##### _proposition:_ the sine formula for $\Gamma$

The formula
$$
\Gamma(s) \, \Gamma(1 - s) = \frac{\pi}{\sin(\pi s)}
$$
holds for all $s$.

###### _proof sketch:_

Prove for $s \in (0, 1)$ using calculus and contour integration, then extend to all $s \in \mathbb{C}$ by [[Complex Analysis --- math-135/notes/Cauchy integral formula#_corollary _ unique analytic continuation|analytic continuation]].

This makes it pretty clear that $\Gamma$ should not vanish anywhere and $1 / \Gamma$ should be entire. Precisely, we can say


##### _lemma:_ $1 / \Gamma$ is entire with finite order of growth

$1 / \Gamma$ is entire with simple zeroes at $s = 0, -1, -2, \dots$ and it satisfies
$$
\left\lvert  \frac{1}{\Gamma(s)}  \right\rvert \le c_{1} e^{c_{2} \lvert s \rvert \log \lvert s \rvert } \le c_{\varepsilon} e^{c_{3} \lvert s \rvert^{1 + \varepsilon}}
$$
for any $\varepsilon > 0$. Thus, $1 / \Gamma$ has order of growth $1$.

##### _theorem:_ the Hadamard factorisation of $1 / \Gamma$

The reciprocal of the gamma function has Hadamard factorisation
$$
\frac{1}{\Gamma(s)} = e^{\gamma s} s \prod_{n = 1}^\infty \left( 1 + \frac{s}{n} \right) e^{-s/n}.
$$
where $\gamma$ is the [[Complex Analysis --- math-135/notes/Euler-Mascheroni constant|Euler-Mascheroni constant]].
###### _proof:_

By [[Complex Analysis --- math-135/notes/Hadamard factorisation#_theorem _ Hadamard factorisation theorem|Hadamard's theorem]], the order of growth of $1 / \Gamma$, and where the zeroes of $1 / \Gamma$ are, we must have
$$
\frac{1}{\Gamma(s)} = e^{As + B} s \prod_{n = 1}^\infty \left( 1 + \frac{s}{n} \right)^{-s/n}.
$$