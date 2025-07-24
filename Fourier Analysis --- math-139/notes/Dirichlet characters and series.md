---
tags:
- math-139/30
- math-139/31
- math-139/32
- math-139/33
- fourier
- nt
- anal
---

Let $G = \mathbb{Z} / q \mathbb{Z}^*$ be the group of units modulo $q$. Let $\bar{\ell}$ be the residue of $\ell \in \mathbb{Z}$ modulo $q$.

Dirichlet characters and series generalise the [[Complex analysis --- math-135/notes/The Riemann zeta function#_theorem _ the Euler product formula|Euler product formula]] to account for the data of primes modulo $q$.

##### _definition:_ Dirichlet character

Let $\xi \in \widehat{G}$ be a [[Fourier analysis --- math-139/notes/Finite Fourier analysis#_definition _ character, the dual group|character]] $G \to S^1$, extended to a function $\xi^{\not *} : \mathbb{Z} / q \mathbb{Z} \to S^1$ by
$$
\xi^{\not *}(\ell) = \begin{cases}
\xi(\ell) & \ell \in G \\
0. 
\end{cases}
$$
 Then the corresponding Dirichlet character is a function $\chi_{\xi} : \mathbb{Z} \to S^1$ by
$$
\chi_{\xi}(\ell) = \xi^{\not *}(\overline{\ell}).
$$

##### _proposition:_ Dirichlet characters are multiplicative

Let $\chi$ be a Dirichlet character $\mathbb{Z} \to \mathbb{C}$. Then $\chi(mn) = \chi(m) \chi(n)$ for all $m, n \in \mathbb{Z}$.

###### _proof:_

Note that residues modulo $q$ [[Superdiscrete --- math-55a/notes/Modular arithmetic#_proposition _ congruence is preserved by addition and multiplication|are multiplicative]] — $\overline{mn} = \overline{m} \, \overline{n}$. If $\overline{m}, \overline{n} \in G$, then $\overline{m} \, \overline{n} \in G$, and thus,
$$
\begin{align}
\chi_{\xi}(mn) & = \xi^{\not *}(\overline{m} \, \overline{n})  \\
 & = \xi(\overline{m} \, \overline{n})  \\
 & = \xi(\overline{m}) \xi(\overline{n})  \\
 & = \chi_{\xi}(m) \chi_{\xi}(n).
\end{align}
$$

If $\overline{m} \not\in G$, then $\gcd(\overline{m}, q) > 1$. Since $m = kq + \overline{m}$, we have $\gcd(\overline{m}, q) \mid m$ and, also $\gcd(\overline{m}, q) \mid mn$ as well. We then have $\overline{m} \, \overline{n} \not\in G$ also. Thus,
$$
\chi_{\xi}(mn) = 0 = \chi(m) = \chi(m) \chi(n).
$$
The proof is similar if $\overline{n} \not\in G$.

### $L$-series

Dirichlet $L$-series generalise [[Complex analysis --- math-135/notes/The Riemann zeta function|the Riemann zeta function]] in a way that allows to take account of more subtle modular information.

##### _definition:_ Dirichlet $L$-series

For any Dirichlet character $\chi$ on $G$, its Dirichlet $L$-series is the function $L(-, \chi)$ given by
$$
L(s, \chi) = \sum_{n = 1}^\infty \frac{\chi(n)}{n^s}
$$
for $s > 1$.

Note that a Dirichlet $L$-series has a [[Complex analysis --- math-135/notes/Cauchy integral formula#_theorem _ identity theorem|unique]] [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ meromorphic functions|meromorphic]] continuation to the whole complex plane. This unique analytic continuation is called an $L$-function. We will only need to deal with the $L$-series for the most part.

Just as the zeta function has a product formula, so does each $L$-series. This is only possible because Dirichlet characters are mutliplicative. Also, since $L(s, \chi)$ can be complex and our primary method for proving products is by taking logarithms, we need some complex analysis in the form of the [[Complex analysis --- math-135/notes/The complex logarithm|complex logarithm]] and the power series expansion
$$
- \log(1- z) = \sum_{n = 1}^\infty \frac{z^n}{n}.
$$
Note that the [[Fourier analysis --- math-139/notes/Dirichlet's theorem on arithmetic progressions#_lemma _ log approximation|logarithm approximation lemma]] used to prove that the sum of the reciprocals of primes diverges still holds here, and for the same reason, for $\lvert z \rvert < 1/2$ we have $\lvert \log(1 - z) \rvert \le 2 \lvert z \rvert$. Finally, we will once again need the sum criterion for convergence of infinite products —
![[Complex analysis --- math-135/notes/Infinite products#_proposition _ absolute convergence of infinite products|Infinite products]]

##### _theorem:_ the product formula for $L$-series

For any Dirichlet character $\chi$ on $G$,
$$
L(s, \chi) = \prod_{p \in \wp} \frac{1}{1 - \chi(s) / p^s}.
$$

###### _proof:_

We consider the difference between the sum and the product by truncating. To show that the truncated differences vanish, we use the multiplicativity of the Dirichlet character. 

For any positive integers $M, N$,
$$
\begin{align}
\left\lvert  \sum_{n = 1}^\infty \frac{\chi(n)}{n^s} - \prod_{p \in \wp} \frac{1}{1 - \chi(p) / p^s}  \right\rvert & \le \left\lvert  \sum_{n = 1}^\infty \frac{\chi(n)}{n^s} - \sum_{n = 1}^N \frac{\chi(n)}{n^s}  \right\rvert  \\
& + \left\lvert  \sum_{n = 1}^N \frac{\chi(n)}{n^s} - \prod_{p \in \wp, p \leq N} \left( 1 + \frac{\chi(p)}{p^s} + \dots + \frac{\chi(p^M)}{p^{Ms}} \right)  \right\rvert   \\
& + \left\lvert  \prod_{p \in \wp, p \le N} \left( 1 + \frac{\chi(p)}{p^s} + \dots + \frac{\chi(p^M)}{p^{Ms}} \right) - \prod_{p \in \wp, p \leq N} \frac{1}{1 - \chi(p) / p^s} \right\rvert \\
  & + \left\lvert  \prod_{p \in \wp, p \le N} \frac{1}{1 - \chi(p) / p^s} - \prod_{p \in \wp} \frac{1}{1 - \chi(p) / p^s}  \right\rvert.
\end{align}
$$
The first and last terms vanish as $N \to \infty$ by the convergence of the product and the convergence of the sum. The third term vanishes by noting that $\chi(p^M) = \chi(p)^M$ and treating the sum inside the product as a geometric series. Finally, the second term vanishes by the same [[Superdiscrete --- math-55a/notes/Euclid's algorithm and primes#_theorem _ unique factorisation|fundamental theorem of arithmetic reason]] as in the [[Complex analysis --- math-135/notes/The Riemann zeta function#_theorem _ the Euler product formula|the Euler product formula]].

##### _corollary:_ the product formula for the trivial character

Suppose $\chi_{1}$ is the trivial character on $G$. Then if $q = p_{1}^{\alpha_{1}} \dots p_{n}^{\alpha_{n}}$ is the prime factorisation of $q$, then $L(s, \chi_{0}) = \zeta(s) (1 - 1/p_{1}^s) \dots (1 - 1/p_{n}^s)$.

We also want to be able to define the logarithm of the $L$-series, specifically, we want to define it as the integral of the logarithmic derivative of the $L$-series. To do so, we need some niceness conditions on the $L$-series so that it actually converges.

##### _lemma:_ the cancellation lemma

If $\chi$ is a non-trivial character on $G$, then $\lvert \sum_{n = 1}^k \chi(n) \rvert < q$ for any $k$.

###### _proof:_

[[Fourier analysis --- math-139/notes/Finite Fourier analysis#_lemma _ non-trivial characters sum to zero|Recall that]] $\sum_{n = 1}^q \chi(n) = 0$. Thus, for $k \equiv b \pmod q$ we can write
$$
\left\lvert  \sum_{n = 1}^k \chi(n)  \right\rvert = \left\lvert  \sum_{n = 1}^{aq} \chi(n)  \right\rvert + \left\lvert  \sum_{n = a q + 1}^b \chi(n) \right\rvert = 0 + b < q.
$$

##### _proposition:_ niceness of $L$-series

For a non-trivial character $\chi$ on $G$, the $L$-series converges for all $s > 0$, is continuously differentiable in $s$, and for some positive constants, $c, c'$ we have $L(s, \chi) = 1 + O(e^{- cs})$ and $\frac{d}{ds} L(s, \chi) = O(e^{-c's})$ as $s \to \infty$.

###### _proof:_

To prove that the $L$-series converges for all $s > 0$, we use [[Fourier analysis --- math-139/attachments/homework/hw 2/hw 2.pdf#page=9|summation by parts]] and some involved algebra to write
$$
\sum_{n = 1}^N \frac{\chi(n)}{n^s} = \sum_{k = 1}^N \frac{S_{k} - S_{k - 1}}{k^s} = \frac{S_{N}}{N^s} + \sum_{k = 1}^{N - 1} S_{k} \left( \frac{1}{k^s} - \frac{1}{(k + 1)^s} \right)
$$
where $S_{k} = \sum_{n = 1}^k \chi(n) / n^s$ are the partial sums of the $L$-series. It's a simple [[#_lemma _ bounding the sum of the Dirichlet character|lemma]] to show that $\lvert S_{k} \rvert \le q$ and we have
$$
\frac{1}{k^s} - \frac{1}{(k + 1)^s} \le \max_{x \in [k, k + 1]} \frac{dx^{}}{dx} = \frac{1}{k^{s + 1}}
$$
by the [[Analysis --- math-131/notes/Mean value theorems#_theorem _ mean value theorem|mean value theorem]]. It follows that
$$
L(s, \chi) = \left\lvert  \sum_{k = 1}^\infty S_{k} \left( \frac{1}{k^s} - \frac{1}{(k + 1)^s} \right)  \right\rvert < \sum_{k = 1}^\infty \left\lvert  \frac{qs}{k^{s + 1}} \right\rvert < \infty.
$$
Thus, the $L$-series converges absolutely and uniformly for all $s > \delta > 0$ for each $\delta > 0$. This also forces it to be continuous.

Differentiating each term, we can make a similar summation by parts argument to show that the series of derivatives of each term of the $L$-series converges absolutely and uniformly, and thus, that the $L$-series is continuously differentiable in $s$.

Finally, to prove the asymptotic bounds we can write
$$
\lvert L(s, \chi) - 1 \rvert = \left\lvert  \sum_{n = 2}^\infty \frac{\chi(n)}{n^s}  \right\rvert \le \max \lvert \chi(n) \rvert \int_{2}^\infty \frac{1}{x^s} \, dx = 2^{-s} O(1).
$$
which is of the desired form.  A similar argument gives the asymptotic bound on the derivative $\left\lvert  \frac{d}{ds} L(s, \chi)  \right\rvert$.