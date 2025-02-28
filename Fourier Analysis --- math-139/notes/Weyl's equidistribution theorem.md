---
tags:
- math-139/13
- fourier
- anal
- nt
---

We want to consider how the sequence of residues of $n \gamma$ in $\mathbb{R} / \mathbb{Z}$ (for $n \in \mathbb{N}$) is distributed in $(0, 1)$. Kronecker's theorem says it is dense, but we want something stronger. If irrational numbers have "random" decimal expansions, we want the sequence of residues of $n \gamma$ to be distributed uniformly at random in $(0, 1)$.

##### _definition:_ equidistributed sequence

A sequence $\{ \xi_{n} \}_{n \in \mathbb{N}}$ in $(0, 1)$ is equidistributed in $(0, 1)$ if for each interval $(a, b) \subseteq (0, 1)$,
$$
\lim_{ N \to \infty } \frac{\# \{ n \in \mathbb{N}_{N} \mid : \xi_{n} \in (a, b) \}}{N} = b - a.
$$

##### _theorem:_ Weyl's equidistribution theorem

If $\gamma \not\in \mathbb{Q}$, the set of decimal residues of its integer multiples is equidistributed in $(0, 1)$.

###### _proof sketch:_

We want to translate this into an equivalent Fourier analysis question. By the definition of equidistribution, it should be equivalent to ask whether, the "numerical integral" over $n \gamma$ approximates the integral over any interval $(a, b) \subseteq (0, 1)$. In order to avoid modding out by $1$ everytime, here $\chi_{(a, b)}$ refers to the characteristic function extended to a $1$-periodic function. We ask whether
$$
\lim_{ N \to \infty } \frac{1}{N} \sum_{n = 1}^\infty \chi_{(a, b)}(n \gamma) = \frac{1}{1 - 0} \int_{0}^1 \chi_{(a, b)}(x) \, dx = b - a.
$$

We first show that this holds for trigonometric polynomials and slowly approximate our way to the characteristic function. It's sufficient to show it for their "basis function" $e^{i k x}$. For $n = 0$ this is obvious since $e^{i k x}$ is constant. For $n \neq 0$ the integral is $0$ so we need to show the sum goes to zero. But we can understand it as a geometric sum —
$$
\frac{1}{N} \sum_{n = 1}^N e^{i k n \gamma} = \frac{e^{i k \gamma}}{N (1 - e^{i k \gamma})} (1 - e^{i k N \gamma})
$$

The term on the right is bounded and the fraction on the left is a constant over $N$ so goes to zero.

[[Fourier Analysis --- math-139/notes/Kernels#_corollary _ Weierstrass approximation theorem|Continuous functions are approximated by trigonometric polynomials]] and [[Fourier Analysis --- math-139/notes/Facts about integration and convergence#_lemma _ integrable functions are approximated by continuous functions|integrable functions are approximated by continuous functions]]. Using these convergences we can transfer the result to the characteristic function (specifically, bound from above and below and trap the integral and sum in between). You can't go directly because we don't have $\chi_{(a,b)}$ approximated by continuous functions in $L^\infty$. This actually works for integrable functions in general, not just the characteristic function, because we can approximate by step functions in $L^\infty$.

##### _corollary:_ Kronecker's theorem

If $\gamma \not\in \mathbb{Q}$, the set of decimal residues of its integer multiples is dense in $(0, 1)$.

In our proof of Weyl's theorem, we demonstrated a further result —

##### _theorem:_ Weyl's criterion

A sequence of real numbers $\xi_{n} \in (0, 1)$ is equidistributed if and only if for all $k \in \mathbb{Z}$,
$$
\lim_{ n \to \infty } \frac{1}{N} \sum_{n = 1}^\infty e^{2 \pi i k \xi_{n}} \to 0.
$$