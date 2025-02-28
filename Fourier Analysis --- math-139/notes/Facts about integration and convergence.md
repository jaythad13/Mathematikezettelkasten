---
tags:
- math-139/0
- anal
---

To do Fourier analysis, we will need some basic facts from analysis about [[Mathematical Analysis I --- math-131/notes/Riemann integration|Riemann integration]] and some definitions for convergence. We won't prove all of them, but they are proven in the appendix of [[Fourier Analysis --- math-139/attachments/texts/Fourier Analysis.pdf|the book]].

### Integration

##### _lemma:_ integrable functions are approximated by continuous functions

If $f : [-\pi, \pi] \to \mathbb{R}$ is integrable and bounded. Then there exists a sequence of continuous functions $f_{n}$ such that
$$
\int _{-\pi}^\pi \lvert f_{n} - f \rvert  \, dx \to 0
$$
as $n \to \infty$.

Note that since continuous functions are approximated by step functions, one could replace the continuous functions by step functions.

##### _theorem:_ Sard's theorem

A bounded function $f: [a, b] \to \mathbb{R}$ is integrable if and only if its set of discontinuities form a set of measure zero.

###### _proof:_

Replicate the proof that [[Mathematical Analysis I --- math-131/notes/Riemann integration#_theorem _ finitely discontinuous functions are integrable|functions with finitely many discontinuites are integrable]].

##### _theorem:_ Fubini's theorem

If $f$ is a (measurable) function $\mathbb{R}^2 \to \mathbb{R}$ with finite integral then
$$
\iint \lvert f(x, y) \rvert \, dx \, dy = \iint \lvert f(x, y) \rvert \, dy \, dx.
$$

Big Rudin shows how this can fail without the hypotheses of this theorem.

### Convergence

We use the notion of function convergence heavily in doing Fourier analysis.

The weakest notion is pointwise convergence — it's exactly what you think.

##### _definition:_ pointwise convergence

If the sequence of functions $f_{n} : E \to \mathbb{C}$ (for $E$ a subset of some [[Mathematical Analysis I --- math-131/notes/Metric spaces|metric space]] $X$), if $\lim_{ n \to \infty } f_{n}(x) = f(x)$ at each point $x \in E$, then $f_{n}$ converges to $f$ pointwise on $E$. We write this as $f_{n} \to f$.

Pointwise convergence doesn't preserve continuity, integrability, or limits under integration. However, we can remedy all of these by requiring every point to converge faster than a certain rate — this is the notion of uniform convergence.

##### _definition:_ uniform convergence

Given a sequence of functions $f_{n} : E \to \mathbb{C}$ we say $f_{n}$ converges uniformly to $f$ on $E$, if for each $\varepsilon > 0$, there exists an $N$ such that $\lvert f_{n}(x) - f(x) \rvert > \varepsilon$ for all $x \in E$. We write this as $f_{n} \rightrightarrows f$.

##### _proposition:_ the Cauchy criterion for uniform convergence

A sequence of functions $f_{n} : E \to \mathbb{C}$ converges uniformly to $f$ on $E$ if and only if, for each $\varepsilon > 0$, there exists $N$ such that $m, n > N$ forces $\lvert f_{n}(x) - f_{m}(x) \rvert < \varepsilon$ for all $x \in E$.

###### _proof sketch:_

Follows by the equivalence of convergence and Cauchy convergence on a [[Mathematical Analysis I --- math-131/notes/Cauchy sequences#_definition _ completeness|complete metric space]].

##### _theorem:_ uniform convergence is equivalent to pointwise + (stronger) $L^\infty$ convergence

Given a sequence of functions $f_{n} : E \to \mathbb{C}$ with $\lim_{ n \to \infty } f_{n}(x) = f(x)$ and $M_{n} = \sup_{x \in E}$, $f_{n} \rightrightarrows f$ on $E$ if and only if $\lim_{ n \to \infty } M_{n} = 0$.
###### _proof:_
[[Mathematical Analysis I --- math-131/notes/The space of continuous functions#_theorem _ $ mathcal{C}(K)$ is Mathematical Analysis I --- math-131/notes/Cauchy sequences _definition _ completeness complete|I think it's here]].

Finally, it'll be useful to know the [[Complex Analysis --- math-135/notes/Analysis and (metric) topology review#_theorem _ Weierstrass $M$-test|Weierstrass criterion]] for uniform convergence of series (the $M$-test).

##### _theorem:_ Weierstrass $M$-test

Suppose each function in the sequence of functions $(f_{n})$ is bounded on $A \subset \mathbb{C}$ by $\lvert f_{n}(a) \rvert \le M_{n}$ for all $a \in A$ and some sequence of real numbers $(M_{n})$. Then $\sum_{n \ge 0} f_{n}$ converges uniformly on $A$ if $\sum_{n \ge 0} M_{n}$ converges.

###### _proof sketch:_

Follows from the Cauchy criterion for series.

### Consequences of uniform convergence

We won't prove any of these.

##### _proposition:_ uniform limit of continuous functions is continuous

If a sequence of continuous functions $\{ f_{n} \}_{n \in \mathbb{N}}$ converges uniformly to $f$, then $f$ is continuous.

##### _proposition:_ uniform limit of integrable functions is integrable

If a sequence of Riemann integrable functions $\{ f_{n} : [a, b] \to \mathbb{C} \}_{n \in \mathbb{N}}$ converges uniformly to $f$ on $[a, b]$, then $f$ is Riemann integrable with
$$
\int_{a}^b f(x) \, dx = \lim_{ n \to \infty } \int_{a}^b f_{n}(x) \, dx.
$$

###### _proof sketch:_

Use the $L^\infty$ condition to bound the integral of $f$ from the lower and upper integrals of $f_{n}$.

The uniform limit of differentiable functions doesn't necessarily have as its derivative the limit of the derivatives. However, if the derivatives converge uniformly, then there are results to be had —

##### _proposition:_ the uniform limit of derivatives

If $\{ f_{n} : [a, b] \to \mathbb{C} \}_{n \in \mathbb{N}}$ is a sequence of [[Mathematical Analysis I --- math-131/notes/Differentiability|differentiable]] functions, the $f'_{n}$ converge uniformly on $[a, b]$, and the $f_{n}$ converge pointwise at $x_{0} \in [a, b]$, then
1) $f_{n} \rightrightarrows f$ for some differentiable $f$
2) $f'(x) = \lim_{ n \to \infty }f_{n}'(x)$ for all $x \in [a, b]$.

### Improper integrals

To understand the Fourier transform, which gives the Fourier coefficient of every real frequency for a function defined on all of $\mathbb{R}$, we need to integrate over all of $\mathbb{R}$, and we should properly define what we mean by that.

##### _definition:_ improper integral

We define the improper integral of a function $f : \mathbb{R} \to \mathbb{C}$ integrable on $\mathbb{R}$ to be
$$
\int_{-\infty}^\infty f(x) \, dx = \lim_{ N \to \infty } \int_{-N}^N f(x) \, dx
$$
if it exists.

Note that thinking of this as a sequence of integrals $I_{n} = \int_{-N}^N f(x) \, dx$, it is sufficient to show $\{ I_{n} \}_{n \in \mathbb{N}}$ is [[Mathematical Analysis I --- math-131/notes/Cauchy sequences#_theorem _ real spaces are complete|Cauchy]].

The functions of moderate decrease are a very nice class of functions!

##### _definition:_ functions of moderate decrease

A [[Mathematical Analysis I --- math-131/notes/Continuity#_definition _ continuity|continuous]] function $f : \mathbb{R} \to \mathbb{C}$ is of moderate decrease if there is a constant $A \in \mathbb{R}$ with
$$
\lvert f(x) \rvert \le \frac{A}{1 + x^{2}}
$$
for all $x \in \mathbb{R}$.

We could also replace $2$ by $1 + \varepsilon$, for some positive $\varepsilon$ but we don't need to choose $\varepsilon < 1$ for the work we're going to do.

The functions of moderate decrease have very nice properties under the improper integral. For the rest of this section, let $f, g$ be functions of moderate decrease.

##### _proposition:_ the improper integral is linear

For $a, b \in \mathbb{C}$, then
$$
\int_{-\infty}^\infty a f(x) + b g(x) \, dx = a \int_{-\infty}^\infty f(x) \, dx + b \int_{-\infty}^\infty g(x) \, dx.
$$

##### _proposition:_ the improper integral is translation invariant

For every $a \in \mathbb{R}$, then
$$
\int_{-\infty}^\infty f(x - a) \, dx = \int_{-\infty}^\infty f(x) \, dx.
$$

##### _proposition:_ the improper integral scales dilated functions

For any $\delta > 0$,
$$
\int_{-\infty}^\infty f(\delta x) \, dx = \frac{1}{\delta} \int_{-\infty}^\infty f(x) \, dx.
$$

##### _proposition:_ the improper integral is continuous

As $h \to 0$,
$$
\int_{-\infty}^\infty \lvert f(x - h) - f(x) \rvert  \, dx \to 0.
$$