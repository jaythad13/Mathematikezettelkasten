---
tags:
- math-135/13
- anal
---

Notice that for a holomorphic function in a disc $D_{R}(z_{0})$, [[Complex Analysis --- math-135/notes/Cauchy integral formula#_corollary _ the derivative form (holomorphic functions are smooth and analytic)|we have a power series]]
$$
f(z) = \sum_{n = 0}^\infty a_{n} (z - z_{0})^n
$$
with
$$
a_{n} = \frac{1}{2 \pi r^n} \int_{0}^{2 \pi} f(z_{0} + r e^{i \theta}) e^{- i n \theta}  \, d\theta 
$$
where $r \in (0, R)$. We get this just by parametrising the integral in the proof that [[Complex Analysis --- math-135/notes/Cauchy integral formula#_corollary _ the derivative form (holomorphic functions are smooth and analytic)|holomorphic functions are analytic]]. In some sense, by writing
$$
a_{0} = \frac{1}{2 \pi} \int_{0}^{2 \pi} f(z_{0} + r e^{i \theta}) e^{- i \theta} \, d\theta 
$$

Why care about any of that? Fourier analysis.

### A crash course in Fourier analysis

##### _definition:_ Fourier series

Let $f : [0, 1] \to \mathbb{C}$ be an integrable function. The Fourier series of $f$ is
$$
f \sim \sum_{n = -\infty}^\infty \hat{f}(x) e^{2 \pi i n x}
$$
where
$$
\hat{f}(x) = \int_{0}^1 f(x) e^{- 2 \pi i n x} \, dx 
$$
This can be phrased in the language of linear algebra. If we work in the [[Linear algebra done right --- ladr/notes/Vector spaces#_definition _ vector space|vector space]] of integrable functions on $[0, 1]$. Then we can define an [[Inner product spaces|inner product]]
$$
\left< f, g \right> = \int_{[0, 1]} f \, \overline{g}.
$$
Then the list of all $e^{2 \pi i n x}$ is an [[Linear algebra done right --- ladr/notes/Orthonormal bases#_definition _ orthonormal|orthonormal list]]. It isn't quite a basis, but we can get the coefficients of (the orthogonal projection onto the span of the list of) the function by taking inner products with the list and adding them all up. Notice that these $e^{2 \pi i n x}$ are just sines and cosines, so we're writing each function as the sum of functions of natural number frequencies.

The continuous analogue of this is to consider all frequencies, not just natural numbers 

##### _definition:_ Fourier transform

For $f : \mathbb{R} \to \mathbb{C}$, and $\xi \in \mathbb{R}$, the Fourier transform of $f$ is the function $\hat{f} : \mathbb{R} \to \mathbb{C}$ defined by
$$
\hat{f}(\xi) = \int_{\mathbb{R}} f(x) e^{- 2 \pi i x \xi} \, dx.
$$

Does this capture everything about a function? Under reasonable conditions, the Fourier transform is invertible. Essentially, the functions cannot have tails that go off slower than any Cauchy distribution.

##### _definition:_ moderate decrease

We say a function $f : \mathbb{R} \to \mathbb{C}$ is of moderate decrease if there is some $A$ such that
$$
\lvert f(x) \rvert \le \frac{A}{1 + x^{2}}
$$
for all $x \in \mathbb{R}$.

Now we can state the theorem, but we still need to translate the niceness conditions to the complex plane to prove it.

##### _proposition:_ the Fourier inversion formula

If $f, \hat{f}$ are both of moderate decrease, then
$$
f(x) = \int_{\mathbb{R}} \hat{f}(\xi) e^{2 \pi i n \xi}  \, d\zeta 
$$


###### _proof sketch:_

Contour integration something something (?)