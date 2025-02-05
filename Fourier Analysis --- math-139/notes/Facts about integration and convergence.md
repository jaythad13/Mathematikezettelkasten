---
tags:
- math-139/0
- anal
- fourier
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

Finally, it'll be useful to know the [[Complex Analysis --- math-135/notes/Analysis and (metric) topology review#_theorem _ Weierstrass $M$-test|Weierstrass criterion]] for uniform convergence of series (the $M$-test).

##### _theorem:_ Weierstrass $M$-test

Suppose each function in the sequence of functions $(f_{n})$ is bounded on $A \subset \mathbb{C}$ by $\lvert f_{n}(a) \rvert \le M_{n}$ for all $a \in A$ and some sequence of real numbers $(M_{n})$. Then $\sum_{n \ge 0} f_{n}$ converges uniformly on $A$ if $\sum_{n \ge 0} M_{n}$ converges.