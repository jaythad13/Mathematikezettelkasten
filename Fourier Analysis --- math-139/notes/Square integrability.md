---
tags:
- math-139/9
- anal
- fourier
---

Square integrability (the condition that $\int \lvert f \rvert^{2} < \infty$) is the Goldilocks of conditions for Fourier series — it works just right. This is because it is the [[Norms|norm]] induced by the [[Inner product spaces|natural inner product]] on functions.

Having an inner products gives us nice results from linear algebra. Notably, the Pythagorean theorem, the Cauchy-Shwarz inequality and the triangle inequality all hold for inner product spaces.

### Nice inner product spaces for analysis

The nicest inner product space to do analysis in is a Hilbert space

##### _definition:_ Hilbert space

A Hilbert space is an inner product space that is [[Mathematical Analysis I --- math-131/notes/Cauchy sequences#_definition _ completeness|complete]] with respect to the induced metric.

For one, the space of $\ell^{2}$ sequences is a Hilbert space! 

##### _definition:_ the inner product space of $\ell^{2}$ sequences

The sequences of $\ell^{2}$ complex numbers (sequences $A$ such that $\left< A, A \right>$ is finite) form an inner product space with
$$
\left< A, B \right> = \sum_{n \in \mathbb{Z}} a_{n} \overline{b_{n}}
$$
for sequences $A = \{ a_{n} \}_{n \in \mathbb{Z}}$ and $B = \{ b_{n} \}_{n \in \mathbb{Z}}$.

Using the finite dimensional triangle inequality, we can see that this space is indeed closed under addition. The inner product structure is obvious.

While $\ell^{2}$ is really nice, the space of Riemann (square) integrable functions fails to be quite as nice. For one it isn't a proper inner product space — $\lVert f \rVert = 0$ only implies $f = 0$ almost everywhere. However this can be remedied by quotienting out by functions differing only on sets of [[Calculus --- spivak/notes/Measure#_definition _ measure $0$|measure zero]]. What is more serious is that $\mathcal{R}$ isn't complete. For example the sequence $f_{n} : x \mapsto \log (1 / x) \chi_{[1 / n, 2 \pi]}(x)$ is [[Mathematical Analysis I --- math-131/notes/Cauchy sequences#_definition _ Cauchy sequence|Cauchy]] but doesn't converge in $\mathcal{R}$.

##### _proposition, definition:_ the $L^2$ inner product, $\mathcal{R}$

The square integrable functions (functions $f$ such that $\left< f, f \right>$ is finite)  on $\mathbb{R} / 2 \pi \mathbb{Z}$ (quotiented by the space of functions the space of functions that differ from $0$ only on a set of measure $0$) form an inner product space with 
$$
\left< f, g \right> = \frac{1}{2 \pi} \int_{-\pi}^\pi f(x) \overline{g}(x) \, dx. 
$$

This inner product space is often denoted $\mathcal{R}$ (if we had Lebesgue integration we might call it $L^2$)

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