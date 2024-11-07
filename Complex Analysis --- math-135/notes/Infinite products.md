---
tags:
- math-135/17
- anal
---

We want to show that given any countable collection of zeroes without a limit point, there is an entire function that vanishes at exactly those points — [[Complex Analysis --- math-135/notes/Weierstrass factorisation|the Weierstrass factorisation theorem]]. The obvious way to do this for a finite collection $\{ a_{1}, \dots, a_{n} \}$ is just to consider $f : z \mapsto (z - a_{1}) \dots (z - a_{n})$. To do this for an infinite collection we need a sensible notion of multiplying together infinitely many functions with the roots we want. This is where infinite products come in!

##### _definition:_ infinite products

Suppose $\{ z_{n} \} \in \mathbb{C}$.  Then the infinite product of all $z_{n}$ is
$$
\prod_{j = 1}^\infty z_{j} = \lim_{ n \to \infty } \prod_{j = 1}^n z_{j}.
$$

##### _remark:_ stricter infinite products

Note that one could have a more restrictive definition — one can require that
1) only finitely many of the $z_{n}$ are $0$
2) for any $N$ large enough that $z_{n} \neq 0$ for all $n > N$ and $\lim_{ n \to \infty } \prod_{j = N + 1}^n z_{n}$ exists and is non-zero,
then
$$
\prod_{j = 1}^\infty z_{j} = \left( \prod_{j = 1}^N z_{j} \right) \left( \lim_{ n \to \infty } \prod_{j = N + 1}^n z_{j} \right)
$$

It is easy to see this is a strictly stronger notion of convergence than the first sense. For example, $\prod_{n = 0}^\infty n$ converges in the first sense but not in the second sense because the tails don't have a limit. Also $\prod_{j = 1}^\infty \frac{1}{2^j}$ converges in the first sense but not in the second sense — the tail products always have limit $0$.

Note that if an infinite product converges, its terms must converge to $1$ —

##### _proposition:_ terms of a non-zero infinite product converge to $1$

If $\prod_{n = 1}^\infty z_{n}$ converges to a non-zero value, $\lim_{ n \to \infty } z_{n} = 1$.

###### _proof sketch:_

Consider
$$
\lim_{ n \to \infty } \frac{\prod_{j = 1}^n z_{j}}{\prod_{j = 1}^{n - 1} z_{j}}
$$


This suggests writing infinite products as
$$
\prod_{n = 1}^\infty z_{n} = \prod_{n = 1}^\infty (1 + a_{n}).
$$

We can in fact characterise convergence of the product in terms of [[Mathematical Analysis I --- math-131/notes/Series#_definition, proposition _ absolute convergence, absolute convergence implies convergence.|absolute convergence]] of the series $\sum a_{n}$.

##### _proposition:_ absolute convergence of infinite products

If $\sum \lvert a_{n} \rvert$ converges, then $\prod (1 + a_{n})$ converges.

###### _proof:_

Since $\sum \lvert a_{n} \rvert$ converges, $a_{n} \to 0$, and thus, $\lvert a_{n} \rvert < 1/2$ for sufficiently large $n$. Thus, $\lvert 1 + a_{n} \rvert \neq 0$. But then
$$
\prod_{n = 1}^N (1 + a_{n}) = e^{\sum_{n = 1}^N \operatorname{Log} (1 + a_{n})}.
$$

Using power series and some geometric series tricks, we can show $\lvert \operatorname{Log} (1 + a_{n}) \rvert \le 2 \lvert a_{n} \rvert$, so the sum converges, and so does the product

### Products of holomorphic functions

We have a strong analogue of the previous result on infinite products for functions.

##### _theorem:_ infinite products of holomorphic functions

Given an open set $\Omega$ and a sequence of holomorphic functions $f_{n} : \Omega \to \mathbb{C}$, with bounded distance from $1$ — $\lvert f_{n}(z) - 1 \rvert < M_{n}$ for all $z \in \Omega$. If $\sum M_{n}$ converges, $\prod f_{n}$ converges uniformly to a holomorphic function.

###### _proof sketch:_

We've already shown that product converges pointwise.

 > $M_{n}$ doesn't depend on $z$ so the convergence is uniform.
 
 \- Eli Stein
 
Essentially, the sum in the exponent is bounded by the sum of all $M_{n}$ uniformly.

Since the partial products are all holomorphic, the product is holomorphic since [[Complex Analysis --- math-135/notes/Cauchy integral formula#_proposition _ uniform convergence preserves holomorphicity|uniform convergence preserves holomorphicity]].

