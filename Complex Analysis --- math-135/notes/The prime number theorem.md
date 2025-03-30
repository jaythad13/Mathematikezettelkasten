---
tags:
- nt
- anal
- complex
- math-135/24x
---

The prime number theorem is a theorem about the asymptotics of the prime counting function $\pi$. Specifically,

##### _definition:_ the prime counting function

The prime counting function is $\pi : \mathbb{R}^+ \to \mathbb{N}$ with
$$
\pi(x) = \#\{ p \text{ prime} \mid  p \le x\}.
$$
##### _theorem:_ prime number theorem

The prime counting function satisfies
$$
\pi(x) \sim \frac{x}{\log x}.
$$
That is, $\lim_{ x \to \infty } (\pi(x) \log x) / x = 1$.

This gives us information about the distribution of primes which is useful to number theorists.

The basic idea is to use the Chebyshev function that sums the logarithms of the primes and an asymptotic lemma to estimate

##### _proposition:_ extending convergence 

If $f$ is [[Complex Analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$|holomorphic]] on the right half-plane $\{ s \in \mathbb{C} \mid \operatorname{Re} s > 0 \}$ and
$$
f(s) = \int_{1}^\infty \frac{\alpha(t)}{t^{s + 1}}\, dt
$$
and $f$ extends holomorphically to an open superset of the closed right half-plane, then the integral converges on the closed right half-plane.

##### _corollary:_ holomorphic Dirichlet series have coefficients of linear order

Suppose $\{ c_{n} \}_{n \in \mathbb{N}}$ is a sequence of non-negative real numbers such that the Dirichlet series
$$
D(s) = \sum_{n = 1}^\infty \frac{c_{n} \log n}{n^s}
$$
is holomorphic on the right half-plane $\{ s \in \mathbb{C} \mid \operatorname{Re} s > 1 \}$. If $(s - 1) D(s)$ extends holomorphically to some open superset of the right half-plane, (excluding possibly a simple pole at $s = 1$ with residue $\rho$), and if
$$
S(x) = \sum_{n \le x} c_{n} \log n =  O(x)
$$
then $S(x) = \rho x$.

###### _proof:_

We can rewrite the Dirichlet series as a Riemann-Stieltjes integral (a [[Mathematical Analysis I --- math-131/notes/Riemann integration#_definition _ Riemann integrable|Riemann integral]] with weights on the partition) and expand it by [[Mathematical Analysis I --- math-131/notes/Fundamental theorem of calculus#_corollary _ integration by parts|integration by parts]]
$$
D(s) = \int_{1}^\infty \frac{1}{t^s} \, dS(t) = \frac{S(t)}{t^s} \Big |_{1}^\infty + \int_{1}^\infty \frac{s}{t^{s + 1}} S(t) \, dt.
$$
The first term vanishes since $S(1) = 0$ and the as $t \to 1$, $S(t) < ct$ (it's order $t$) and $t^s$ is is asmyptotically greater for $\operatorname{Re} s > 1$.

For $s$ such that $\operatorname{Re} s > 0$, we then get
$$
D(s + 1) = (s + 1) \int \frac{S(t)}{t^{s + 2}} \, dt 
$$

##### _corollary:_ the logarithmic derivative of the zeta function has coefficients of finite order

The logarithmic derivative of the [[Complex Analysis --- math-135/notes/The Riemann zeta function#_definition _ the Riemann zeta function|Riemann zeta function]] is a Dirichlet series
$$
\sum_{n = 1}^\infty \frac{1}{n^s}
$$

##### _lemma:_ the non-vanishing of the zeta function on $\{ s \mid \operatorname{Re} s = 1 \}$

$\zeta(s) \neq 0$ for all $s \in \{ s \mid \operatorname{Re} s = 1 \}$.

###### _proof sketch:_

Consider $D(s) = \zeta(s)^{3} \zeta(s + it)^4 \zeta(s + 2it)$. We will use the logarithmic derivative of $D$ and the [[Complex Analysis --- math-135/notes/The argument principle and winding number#_theorem _ the argument principle|argument principle]] to calculate the order of $D$ as the [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#_proposition, definition _ principals and residues|residue]] of $D' / D$, and show that $\operatorname{ord}_{1} D \le 0$.

But then
$$
0 \ge \operatorname{ord} D_{1}(s) \ge 3 \operatorname{ord}_{1} \zeta(s) + 4 \operatorname{ord}_{1} \zeta(s + i t) + \operatorname{ord}_{1}\zeta(s + 2 i t).
$$
Since $\operatorname{ord}_{1} \zeta = -1$ and $\zeta(s + 2 i t)$ is holomorphic at $1$, we have $-3 + 4 \operatorname{ord}_{1} \zeta(s + i t) \le 0$, forcing $\operatorname{ord}_{1} \zeta(s + i t) \le 3 / 4$. Thus, it does not vanish (it does not have a pole either since it is holomorphic for $t \neq 0$).