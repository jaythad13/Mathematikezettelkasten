---
tags:
- math-135/13
- math-135/14
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

Now we can state the theorem, but we still need to translate the niceness condition to the complex plane to prove it.

##### _definition:_ $\mathfrak{F}_{a}$

A complex function $f$ is said to be in $\mathfrak{F}_{a}$ if it is holomorphic on the horizontal strip $S = \{ z \in \mathbb{C} \mid \lvert \operatorname{Im}z \rvert < a\}$, and there is a (uniform) constant of moderate decay $A$, such that
$$
\lvert f(x + iy) \rvert \le \frac{A}{1 + x^{2}}
$$
for $x + i y \in S$.

##### _lemma:_ holomorphic functions of moderate decay have Fourier transform of rapid decay

If $f \in \mathfrak{F}_{a}$ for any $a > 0$, then
$$
\lvert \hat{f}(\xi) \rvert \le Be^{-2 \pi b \lvert \xi \rvert }
$$

##### _theorem:_ the Fourier inversion formula

If $f, \hat{f}$ are both of moderate decrease, then
$$
f(x) = \int_{\mathbb{R}} \hat{f}(\xi) e^{2 \pi i x \xi}  \, d \xi.
$$

###### _proof sketch:_



##### _theorem:_ the Poisson summation formula

If $f \in \mathfrak{F}_{a}$ for some $a > 0$, then
$$
\sum_{n \in \mathbb{Z}} f(n) = \sum_{n \in \mathbb{Z}} \hat{f}(n).
$$

###### _proof sketch:_

We can use the [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#_theorem _ the residue formula|the residue formula]] by considering the function ${1}/{e^{2 \pi i z} - 1}$ which has simple poles at the integers with residues $1/2 \pi i$. But then
$$
g(z) = \frac{f(z)}{e^{2 \pi i z} - 1}
$$
gives us
$$
\sum_{n = -N}^N f(n) = \frac{1}{2 \pi i} \int_{\gamma_{N}} g(z) \, dz
$$
for a rectangle $\gamma_{N}$ that encloses exactly the integers $\{ -N, \dots, N \}$ and has top and bottom sides along the $\operatorname{Im} z = b$ and $\operatorname{Im} z = - b$ lines respectively. Thus,
$$
\sum_{n \in \mathbb{Z}} f(n) = \lim_{ N \to \infty } \frac{1}{2 \pi i} \int_{\gamma_{N}} f(z) \, dz 
$$

By definition,
$$
\begin{split}
\sum_{n \in \mathbb{Z}} \hat{f}(n) & = \sum_{n = 0}^{\infty} \hat{f}(n + 1) + \sum_{n = 0}^\infty \hat{f}(-n) \\
 & = \sum_{n = 0}^\infty \int_{\mathbb{R}} f(x) e^{- 2 \pi i (n + 1) x} \, dx + \sum_{n = 0}^\infty \int_{\mathbb{R}} f(x) e^{2 \pi i n x} \, dx.
\end{split}
$$
Using the same trick as before we can shift the contours, getting
$$
\sum_{n \in \mathbb{Z}} \hat{f}(n) = \sum_{n = 0}^\infty \int_{\operatorname{Im} z = -b} f(z) e^{- 2 \pi i (n + 1) z} \, dz + \sum_{n = 0}^\infty \int_{\operatorname{Im} z = b} f(z) e^{2 \pi i n z} \, dz.
$$
Since we have split the $z$ with positive and negative real imaginary part cleverly enough, the exponentials $(e^{- 2 \pi i z})^n$ and $(e^{2 \pi i z})^n$ on the inside of the integrals are all of magnitude strictly less than $1$. Then, using the uniform convergence of the sum, we can interchange the order of summation and integration to get
$$
\begin{split}
\sum_{n \in \mathbb{Z}} \hat{f}(n) & = \int_{\operatorname{Im} z = -b} f(z)  \sum_{n = 0}^\infty (e^{-2 \pi i z})^n \, dz + \int_{\operatorname{Im} z = b} f(z)  \sum_{n = 0}^\infty   (e^{2 \pi i z})^n\, dz. \\
 & = \int_{\operatorname{Im} z = - b} \frac{f(z)}{1 - e^{ - 2 \pi i z}}  \, dz + \int_{\operatorname{Im} z = b} \frac{f(z)}{1 - e^{2 \pi i z}} \, dz. 
\end{split}
$$

Doing case work on the sign of of $z$, and noticing that the integral of $g$ along the vertical sides of $\gamma_{N}$ vanishes as $N \to \infty$, we can see that this is exactly the sum we want —
$$
\sum_{n \in \mathbb{Z}} \hat{f}(n) = \int_{\gamma_{N}} g(z) \, dz = \sum_{n \in \mathbb{Z}} f(n).
$$