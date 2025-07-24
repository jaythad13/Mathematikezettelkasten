---
tags:
- math-139/9
- math-139/10
- anal
- fourier
---

The space of $L^2$ functions is the Goldilocks space for Fourier series — it works just right and the Fourier series does in fact converge to the function under its slightly weaker notion of convergence. This is because it is the [[Norms|norm]] induced by the [[Inner product spaces|natural inner product]] on functions.

Having an inner products gives us nice results from linear algebra. Notably, the Pythagorean theorem, the Cauchy-Shwarz inequality and the triangle inequality all hold for inner product spaces.

### Nice inner product spaces for analysis

The nicest inner product space to do analysis in is a Hilbert space

##### _definition:_ Hilbert space

A Hilbert space is an inner product space that is [[Analysis --- math-131/notes/Cauchy sequences#_definition _ completeness|complete]] with respect to the induced metric.

For one, the space of $\ell^{2}$ sequences is a Hilbert space! 

##### _definition:_ the inner product space of $\ell^{2}$ sequences

The sequences of $\ell^{2}$ complex numbers (sequences $A$ such that $\left< A, A \right>$ is finite) form an inner product space with
$$
\left< A, B \right> = \sum_{n \in \mathbb{Z}} a_{n} \overline{b_{n}}
$$
for sequences $A = \{ a_{n} \}_{n \in \mathbb{Z}}$ and $B = \{ b_{n} \}_{n \in \mathbb{Z}}$.

Using the finite dimensional triangle inequality, we can see that this space is indeed closed under addition. The inner product structure is obvious.

While $\ell^{2}$ is really nice, the space of Riemann (square) integrable functions fails to be quite as nice. For one it isn't a proper inner product space — $\lVert f \rVert = 0$ only implies $f = 0$ almost everywhere. However this can be remedied by quotienting out by functions differing only on sets of [[Calculus --- spivak/notes/Measure#_definition _ measure $0$|measure zero]]. What is more serious is that $\mathcal{R}$ isn't complete. For example the sequence $f_{n} : x \mapsto \log (1 / x) \chi_{[1 / n, 2 \pi]}(x)$ is [[Analysis --- math-131/notes/Cauchy sequences#_definition _ Cauchy sequence|Cauchy]] but doesn't converge in $\mathcal{R}$.

##### _proposition, definition:_ the $L^2$ inner product, $\mathcal{R}$

The square integrable functions (functions $f$ such that $\left< f, f \right>$ is finite)  on $\mathbb{R} / 2 \pi \mathbb{Z}$ (quotiented by the space of functions the space of functions that differ from $0$ only on a set of measure $0$) form an inner product space with 
$$
\left< f, g \right> = \frac{1}{2 \pi} \int_{-\pi}^\pi f(x) \overline{g}(x) \, dx. 
$$

This inner product space is often denoted $\mathcal{R}$ (if we had Lebesgue integration and identified functions with measure $0$ support, we might call it $L^2(\mathbb{R} / 2 \pi \mathbb{Z})$).

### Fourier analysis as orthogonal decomposition

In $\mathcal{R}$, it's easy to see that some basic facts are true —

##### _proposition:_ the Fourier characters are an orthonormal list in $\mathcal{R}$

The list of all Fourier characters $e_{n} : x \mapsto e^{in x}$ is an [[Linear algebra done right --- ladr/notes/Orthonormal bases#_definition _ orthonormal|orthonormal list]].

##### _proposition:_ the Fourier coefficients are coefficients in the orthonormal list

The Fourier coefficients $\hat{f}(n)$ of a function $f \in \mathcal{R}$ are just the [[Linear algebra done right --- ladr/notes/Orthonormal bases#_proposition _ the coordinates of a vector in an orthonormal basis|coefficients with respect to the orthonormal list]] of $e_{n}$. 

This allows us to show that the Fourier series is indeed the best approximation with respect to the $L^2$ norm.

##### _lemma:_ the best approximation lemma

If $f : \mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{C}$ is integrable, then over the set of trigonometric polynomials $\sum_{\lvert n \rvert < N} c_{n} e_{n}$, the Fourier series partial sums $S_{N}f$ are the best approximation in $L^2$ — that is, they have the minimum
$$
\frac{1}{2 \pi} \int_{-\pi}^\pi \lvert f(x) - S_{N}f(x) \rvert^{2}  \, dx.
$$

###### _proof sketch:_

This is just the result that [[Linear algebra done right --- ladr/notes/Applying orthogonality#_proposition _ the best subspace approximation|projection gives the best approximation in a subspace]].

### Square convergence

It follows then that the Fourier series converges to $f$ with respect to the $L^2$ norm.

##### _theorem:_ Fourier series convergence in $L^{2}$

If $f : \mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{C}$ is integrable,
$$
\lim_{ N \to \infty } \int_{-\pi}^\pi \lvert f(x) - S_{N}f(x) \rvert^{2} \, dx = 0.
$$
That is, $\lVert f - S_{N}f \rVert_{L^2} \to 0$.

###### _proof sketch:_

For a continuous function $g$, [[Fourier analysis --- math-139/notes/Kernels#_corollary _ Weierstrass approximation theorem|we know the (trigonometric) Weierstrass approximation theorem is true]]. Note that though the Cesaro means converge to the Fourier series when the Fourier series converges, we aren't guaranteed convergence of the Fourier series.

Since the trigonometric polynomials $p_{n} \rightrightarrows f$, they converge to $g$ in $L^\infty$ ([[Analysis --- math-131/notes/The space of continuous functions#_definition, proposition _ the space of continuous functions is a metric space|the supremum norm]]) and thus, they converge in $L^2$ (bound $\lvert p_{n} - g \rvert$ by $2 \pi \varepsilon$ and substitute into the integral). That is, $\lVert p_{n} - g \rVert_{L^2} \to 0$. Since $S_{n}g$ is the best $L^2$ approximation to $g$ by trigonometric polynomials, we must have $\lVert S_{n}g - g \rVert_{L^2} \leq \lVert p_{n} - g \rVert_{L^2} < \varepsilon$ at each point as $n \to \infty$.

Since [[Fourier analysis --- math-139/notes/Facts about integration and convergence#_lemma _ integrable functions are approximated by continuous functions|integrable functions are approximated by continuous functions]] in $L^1$, for $f$ integrable we can get $\lVert f - g \rVert_{L^1} < \varepsilon^{2} / 2B$ with $g$ continuous. By bounding $\lvert f - g \rvert$ by some $B$ (they are integrable), we can also get $\lVert f - g \rVert_{L^2} = \sqrt{ 2 B \lVert f - g \rVert_{L^1}^{2} }$ and thus $\lVert f - g \rVert_{L^2} < \varepsilon$.

Since $g$ is approximated by $\{ p_{n} \}_{n \in \mathbb{N}}$ with $\lVert g - p_{n} \rVert_{L^2} < \varepsilon$. By the triangle inequality we get $f$ approximated by $\{ p_{n} \}_{n \in \mathbb{N}}$ — we have $\lVert f - p_{n} \rVert_{L^{2}} < 2 \varepsilon$. Then applying the best approximation lemma again, we get $\lVert S_{n}f - f \rVert_{L^{2}} \le \lVert p_{n} - f \rVert \to 0$.

##### _corollary:_ Parseval's identity

Let $f : \mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{C}$ be integrable. Then
$$
\lVert \{ \hat{f}(n) \}_{n \in \mathbb{N}} \rVert^{2}_{\ell^{2}} = \sum_{n = - \infty}^\infty \lvert \hat{f}(n) \rvert^{2} = \frac{1}{2 \pi} \int_{-\pi}^\pi \lvert f(x) \rvert^{2}  \, dx =  \lVert f \rVert_{L^2}^2.
$$

###### _proof sketch:_

Extend the proof that $\lVert v \rVert^{2}$ is [[Linear algebra done right --- ladr/notes/Orthonormal bases#_corollary _ the norm of a vector in an orthonormal basis|the sum of the squares of its coefficients with respect to an orthonormal basis]] from the finite-dimensional case using the fact that $\lVert S_{N}f - f \rVert \to 0$.

##### _corollary:_ polarised Parseval's identity

Under the same hypotheses on $f$ and $g$
$$
\left< f, g \right>_{L^2} = \left< \{ \hat{f}(n) \}_{n \in \mathbb{N}}, \{ \hat{g}(n) \}_{n \in \mathbb{N}} \right>_{\ell^{2}}.
$$

###### _proof sketch:_

Use [[the polarisation identity]] to recover the inner product from the norm.

##### _corollary:_ Riemann-Lebesgue lemma

Under the same hypotheses $\hat{f}(n) \to 0$ as $\lvert n \rvert \to \infty$.

###### _proof sketch:_

Since the squares of their sums converge.

Note that by adding/subtracting conjugates, this also forces both integrals
$$
\int_{-\pi}^\pi f(x) \sin(n x) \, dx, \int_{-\pi}^\pi f(x) \cos(n x) \, dx \to 0 
$$
as $n \to \infty$.