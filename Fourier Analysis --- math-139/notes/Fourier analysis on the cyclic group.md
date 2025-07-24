---
tags:
- fourier
- alg
- math-139/26
- math-139/27
---

We've already seen that we convert the data of continuous functions $\mathbb{R} / 2 \pi \mathbb{Z} \to \mathbb{C}$ into the data of their [[Fourier analysis --- math-139/notes/Fourier series|Fourier series]] $\mathbb{Z} \to \mathbb{C}$ and the data of [[Fourier analysis --- math-139/notes/The Fourier transform#_definition _ Schwartz class, $ mathcal{S}( mathbb{R})$|Schwartz functions]] $\mathbb{R} \to \mathbb{C}$ into the data of their [[Fourier analysis --- math-139/notes/The Fourier transform#_definition _ the Fourier transform|Fourier transforms]] $\mathbb{R} \to \mathbb{C}$. With the respective inversion formulas, these can be viewed as isomorphisms of appropriate vector spaces given by finding [[Linear algebra done right --- ladr/notes/Orthonormal bases#_definition _ orthonormal basis|orthonormal bases]]. This can be generalised to the complex valued functions on [[Fourier analysis --- math-139/notes/Finite Fourier analysis|any finite abelian group]] (and in fact, any locally compact abelian group, but we will not show that).

### Fourier analysis on the cyclic group

The first example where we can do this is the cyclic group.

##### _definition:_ the inner product space of functions on the cyclic group

The vector space of complex functions on the cyclic group is 
$$
\mathbb{C}^{\mathbb{Z} / n \mathbb{Z}} = \{ f : \mathbb{Z} / n \mathbb{Z} \to \mathbb{C} \}
$$
and is an [[Inner product spaces|inner product space]] with
$$
\left< f, g \right> = \frac{1}{n} \sum_{k \in \mathbb{Z} / n \mathbb{Z}} f(k) \overline{g(k)}. 
$$

Recall that we can also understand the cyclic group as the $N$th complex roots of unity. The canonical orthonormal basis on $\mathbb{Z} / n \mathbb{Z}$ is surprisingly nice with this context.

##### _proposition:_ an orthonormal basis on $\mathbb{C}^{\mathbb{Z} / n \mathbb{Z}}$

For $\zeta = e^{2 \pi i / N}$, the functions $e_{\ell}$ given by $e_{\ell}(k) = e^{2 \pi \ell k i / N}$ form an orthonormal basis in $V$.

###### _proof:_

It suffices to prove that this is an orthonormal list since it follows that would imply that it is an  linearly independent list of maximal length.

If $m = \ell$, then each of the $n$ terms of the sum defining the inner product $\left< e_{m}, e_{\ell} \right >$ is just $1$, and thus, $\left< e_{m}, e_{\ell} \right> = n / n = 1$. However, if $m \neq \ell$, then we have a geometric sum which vanishes —
$$
\begin{align}
\left< e_{m}, e_{\ell} \right> &  = \frac{1}{n} \sum_{k = 0}^{N - 1} (e^{2 \pi i (m - \ell)/ N})^k \\
 & = \frac{1}{n} \frac{1 - (e^{2 \pi i (m - \ell)/ N})^N}{1 - e^{2 \pi i (m - \ell) / N}} \\
 & = \frac{1}{n} \frac{1 - e^{2 \pi i (m - \ell)}}{1 - e^{2 \pi i (m - \ell)/N}} \\
 & = 0.
\end{align}
$$

The next few results follow directly as consequences of linear algebra.

##### _definition:_ Fourier coefficients

For each $\ell \in \mathbb{Z} / n \mathbb{Z}$ the $\ell$th Fourier coefficient of $f : \mathbb{Z} / n \mathbb{Z} \to \mathbb{C}$ is $\hat{f}(\ell) = \left< f, e_{\ell} \right>$.

##### _theorem:_ Fourier inversion

For any function $f : \mathbb{Z} / n \mathbb{Z} \to \mathbb{C}$ we have $f = \sum_{\ell \in \mathbb{Z} / n \mathbb{Z}} \hat{f}(\ell) e_{\ell}$.

###### _proof:_
see [[Linear algebra done right --- ladr/notes/Orthonormal bases#_proposition _ the coordinates of a vector in an orthonormal basis|notes on orthonormal bases]]

##### _theorem:_ Plancherel's theorem

For any function $f : \mathbb{Z} / n \mathbb{Z} \to \mathbb{C}$ we have
$$
\lVert f \rVert^{2} = \sum_{\ell \in \mathbb{Z} / n \mathbb{Z}} \lvert \hat{f}(\ell)  \rvert^{2}
$$

###### _proof:_
again, see [[Linear algebra done right --- ladr/notes/Orthonormal bases#_corollary _ the norm of a vector in an orthonormal basis|notes on orthonormal bases]].

### Fast Fourier transform

The theory of Fourier analysis on $\mathbb{Z} / n \mathbb{Z}$ falls out easily from linear algebra. However, so far, we've only computed Fourier transforms in the obvious way — by applying the formula. This requires $O(n^{2})$ calculations. However this is not the best we can do. In the 60s, John Tukey showed that this can actually be done in $O(n \log n)$ which is much better! This follows by splitting a function on $\mathbb{Z} / n \mathbb{Z}$ into its odd and even parts.

##### _definition:_ $\# \mathrm{FFT}(\mathbb{Z} / n \mathbb{Z})$

For any positive integer $n$, let $\# \mathrm{FFT}(\mathbb{Z} / n \mathbb{Z})$ be the minimum number of operations required to compute the Fourier transform of a function $f : \mathbb{Z} / n \mathbb{Z} \to \mathbb{C}$.

##### _lemma:_ the splitting lemma

Given any $f : \mathbb{Z} / 2 n \mathbb{Z} \to \mathbb{C}$, and consider $g_{0}, g_{1} : \mathbb{Z} / n \mathbb{Z} \to \mathbb{C}$ defined by $g_{0}(n) = f(2n)$ and $g_{1}(n) = f(2n + 1)$. Then
$$
\hat{f}(k) = \frac{\hat{g}_{0}(k) + \hat{g}_{1}(k) \omega_{2n}^k}{2}
$$
where $\omega_{2n} = e^{2 \pi i / 2n}$ is the first $2n$th root of unity.

###### _proof:_

Also, let $\omega_{n} = e^{2 \pi i / n}$.

This is essentially a consequence of the fact that $\mathbb{Z} / 2 n \mathbb{Z}$ can be split into odd and even components. We just split the sum defining $\hat{f}(k)$ into odd and even parts —
$$
\begin{align}
\hat{f}(k) & = \left< f, e_{k} \right> \\
 & = \frac{1}{2n} \sum_{\ell \in \mathbb{Z} / 2n \mathbb{Z}} f(\ell) (\omega_{2n}^{k})^{\ell} \\
 & = \frac{1}{2n} \sum_{\ell \in \mathbb{Z} / n \mathbb{Z}} f(2 \ell) (\omega_{2n}^{k})^{2 \ell} + \frac{1}{2n} \sum_{\ell \in \mathbb{Z} / n \mathbb{Z}} f(2 \ell + 1) (\omega_{2n}^k)^{2 \ell + 1}  \\
 & = \frac{1}{2 n} \sum_{\ell \in \mathbb{Z} / n \mathbb{Z}} g_{0}(\ell) (\omega_{n}^k)^{\ell} + \frac{\omega_{2n}^k}{2n} \sum_{\ell \in \mathbb{Z} / n \mathbb{Z}} g_{1}(\ell) (\omega_{n}^k)^{\ell} \\
 & = \frac{\hat{g}_{0}(k) + \hat{g}_{1}(k) \omega_{2n}^k}{2}.
\end{align}
$$

##### _lemma:_ bounding complexity by the previous

Given $\omega_{2 n} = e^{-2 \pi i / 2n}$,
$$
\# \mathrm{FFT}(\mathbb{Z} / 2n \mathbb{Z}) \le 2 \# \mathrm{FFT}(\mathbb{Z} / n \mathbb{Z}) + 8n.
$$

###### _proof:_

To calculate $\omega_{2n}, \dots, \omega_{2n}^{2n}$ takes no more than $2n$ multiplications. This also calculates all $\omega_{n}^k$. Calculating the Fourier transforms of $g_{0}$ and $g_{1}$ takes $2 \# \mathrm{F F T}(\mathbb{Z} / n \mathbb{Z})$ each. Then, for each $k \in \mathbb{Z} / 2n \mathbb{Z}$, we perform three calculations with $\hat{g}_{0}(k)$ and $\hat{g}_{1}(k)$ to get $\hat{f}(k)$. For $2n$ different $k$ this gives $6 n$ operations. Thus,
$$
\# \mathrm{FFT}(\mathbb{Z} / 2n \mathbb{Z}) \le 2n + 2 \# \mathrm{ F F T}(\mathbb{Z} / n \mathbb{Z}) + 6 n = 2 \# \mathrm{FFT}(\mathbb{Z} / n \mathbb{Z}) + 8n.
$$

##### _theorem:_ the fast Fourier transform

For any positive $n$, given the first $n$th root of unity $\omega_n = e^{- 2 \pi i / n}$, it takes at most $O(n \log n)$ operations to compute the Fourier transform.

###### _proof:_

It suffices to prove this in the case that $n = 2^j$.

By induction on the previous lemma it follows that
$$
\# \mathrm{F F T}(\mathbb{Z} / 2^j \mathbb{Z}) \le 2^{j - 1} \#\mathrm{F F T}(\mathbb{Z} / 2 \mathbb{Z}) + 8 j n \le 2^{j + 1} + j 2^{j + 3}.
$$
Rewriting with $n$ we get
$$
\# \mathrm{F F T}(\mathbb{Z} / n \mathbb{Z}) \le 2n + 8 n \log_{2} n = O(n \log n).
$$