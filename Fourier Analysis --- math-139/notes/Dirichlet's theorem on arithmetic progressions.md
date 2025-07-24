---
tags:
- math-139/29
- math-139/30
- math-139/31
- math-139/33
- math-139/34
- fourier
- nt
- anal
---

It's been known since antiquity that there are infinitely many [[Superdiscrete --- math-55a/notes/Euclid's algorithm and primes#_definition _ prime numbers|primes]].

##### _theorem:_ the infinitude of the primes

There are infinitely many primes in $\mathbb{Z}$.

###### _proof:_

Suppose, by way of contradiction, that $p_{1}, p_{2}, \dots, p_{n}$ was a finite enumeration of all the primes. Then $p_{1} p_{2} \dots p_{n} + 1$ is a number not divisible by any of the primes in the enumeration. It is either a prime itself, or divisible by some other prime not in $p_{1}, \dots, p_{n}$.

It's clear that most of these primes (all but one of them, actually) are either $4k + 1$ or $4k + 3$ for some $k \in \mathbb{N}_{0}$. We can use a similar proof to prove that there are infinitely many primes of the form $4k + 3$.

##### _theorem:_ infinitude of primes of the form $4k + 3$

There are infinitely many primes in $\mathbb{Z}$ of the form $4k + 3$.

###### _proof:_

Suppose, by way of contradiction, that $p_{2}, \dots, p_{n}$ was an enumeration of all primes of the form $4k + 3$, excluding $p_{1} = 3$. Then consider $p = 4 p_{2} \dots p_{n} + 3$.

$p$ is not divisible by any of the $p_{i}$. This is clear for $i > 1$ since $p$ has residue $3$ modulo each of those $p_{i}$. Further, $p$ is not divisible by $3$ since that would force $4 p_{2} \dots p_{n}$ to be divisible by $3$ which it is not (since $3$ is manifestly not in its prime factorisation).

If $p_{2}, \dots, p_{n}$ were all the primes of the form $4k + 3$, $p$ would have to be the product of primes $q_{1}, \dots, q_{m}$ of the form $4k + 1$. But the product of primes of the form $q_{i} = 4k_{i} + 1$ is 
$$
q_{1} q_{2} \dots q_{n} = 4 (k_{1} k_{2} \dots k_{n} + \dots k_{1} + \dots + k_{n}) + 1
$$
of the form $4k + 1$. Thus, $p$ must be divisible by a different prime of the form $4k + 3$.

We can't do the same thing to check whether there are infinitely many primes of the form $4k + 1$. More generally when are there infinitely many primes of the form $\ell + q k$? The most elementary obstruction to having primes of the form $\ell + q k$ occur when $\gcd(\ell, q) > 1$, and thus $\gcd(\ell, q) \mid \ell + q k$ for all $k$. We might hope that this is the only obstruction — if an arithmetic sequence can contain any (odd) primes at all, it contains infinitely many. Legendre conjectured this more general statement to prove quadratic reciprocity, and Dirichlet ultimately proved it.

##### _theorem:_ Dirichlet's theorem on arithmetic progressions

If $q$ and $\ell$ are relatively prime, then the arithmetic sequence $\{ \ell + k q \mid k \in \mathbb{Z} \}$ contains infinitely many primes.

### The simplest case of Dirichlet's theorem

The idea behind Dirichlet's theorem is the same as that of, an admittedly ridiculous, analytic proof of the infinitude of primes — Euler's proof that the sum of the reciprocals of the primes diverges. Of course, this is the simplest case where $\ell = 1$, $q = 2$ (since the proof we're about to give holds even after ignoring the even prime).

##### _lemma:_ log approximation

For all $\lvert x \rvert < 1/2$,
$$
\ln(1 + x) = x + E(x)
$$
where the magnitude of the error term $E(x)$ is bounded — $\lvert E(x) \rvert \le x^{2}$.

###### _proof:_

Consider the [[Analysis --- math-131/notes/Power series#_definition _ power series|power series expansion]] of the [[Complex analysis --- math-135/notes/Cauchy integral formula#_corollary _ the derivative form (holomorphic functions are smooth and analytic)|analytic function]]
$$
\ln(1 + x) =  x - \frac{x^{2}}{2} + \frac{x^{3}}{3} - \frac{x^4}{4} + \cdots.
$$
Then the error term is bounded
$$
\lvert E(x) \rvert \leq \frac{x^{2}}{2} + \frac{x^3}{3} + \frac{x^4}{4} + \cdots = \frac{x^{2}}{2} (1 + \lvert x \rvert + \lvert x \rvert ^{2} + \cdots).
$$
For $\lvert x \rvert < 1 / 2$, the geometric sum is bounded by $2$, and thus, $\lvert E(x) \rvert \le x^{2}$.

##### _lemma:_ approximating the Riemann zeta function

[[Complex analysis --- math-135/notes/The Riemann zeta function#_definition _ the Riemann zeta function|The Riemann zeta function]] $\zeta$ is approximated
$$
\sum_{p \text{ prime}} \frac{1}{p^s} = \ln \zeta(s) + C
$$
for all real $s > 1$.

###### _proof:_

We can take logarithms on both sides of the [[Complex analysis --- math-135/notes/The Riemann zeta function#_theorem _ Euler's product formula|Euler product formula]] to get
$$
\ln \zeta(s) = - \sum_{p \text{ prime}} \ln \left( 1 - \frac{1}{p^s} \right).
$$

By our previous lemma approximating the logarithm
$$
\ln \zeta(s) \le - \sum_{p \text{ prime}} \left( - \frac{1}{p^s} + \frac{1}{p^{2s}} \right) =  \sum_{p \text{ prime}} \frac{1}{p^s}  - \sum_{p \text{ prime}} \frac{1}{p^{2s}}.
$$
Since $\sum 1 / (p^s)^{2} \le \sum 1 / (n^s)^{2} < \infty$, and the inequality in the logarithm approximation is only in the $\sum 1/p^{2s}$ term, we have the desired approximation
$$
\ln \zeta(s) = \sum_{\text{p} \text{ prime}} \frac{1}{p^s} - C.
$$

##### _theorem:_ the sum of the reciprocals of primes diverges

The sum
$$
\sum_{p \text{ prime}} \frac{1}{p}
$$
diverges.

###### _proof:_

We can write
$$
\sum_{p \text{ prime}} \frac{1}{p} \geq \liminf_{s \to 1^+} \sum_{p \text{ prime}} \frac{1}{p^s} = \liminf_{s \to 1^+} \ln \zeta(s) + C.
$$
However,
$$
\liminf_{s \to 1^+} \zeta(s) = \liminf_{s \to 1^+} \sum_{n = 1}^\infty \frac{1}{n^s} > \sum_{n = 1}^M 1 / n.
$$
for every $M$, and thus, diverges. Thus, the $\liminf$ of $\ln \zeta(s)$ diverges too, and finally, so does the sum of the reciprocals of the primes.

##### _corollary:_ the infinitude of the primes

There are infinitely many primes.

### Reducing the theorem

We want to use the same idea to prove Dirichlet's theorem in general. That is, we want to prove that there are infinitely many primes of the form $qk + \ell$ where $\gcd(q, \ell) = 1$ by proving that the sum
$$
\sum_{p \text{ prime}, p = kq + \ell} \frac{1}{p}
$$
diverges.

At this point, we introduce some notation to make our lives easier.

##### _notation:_ Weierstrass $\wp$ for primes

The set of all primes is denoted $\wp$.

##### _notation:_ modular equivalence

When $q$ is obvious, we write $p \equiv \ell$ to mean $p = \ell \pmod q$.

Our goal is now to reduce this result to something that we can say about [[Fourier analysis --- math-139/notes/Dirichlet characters and series|Dirichlet characters and series]]. Note that, we can define the characteristic function of $\ell$ modulo $q$ which gives a convenient way to express the infinite sum we want to show diverges, and simultaneously gives a way to utilise the tools of [[Fourier analysis --- math-139/notes/Finite Fourier analysis|finite Fourier analysis]] and thus, Dirichlet characters and series.

##### _definition:_ the modular characteristic function

The modular characteristic function of $\ell \in \mathbb{Z} / q \mathbb{Z}^*$ is the function
$$
\begin{align}
\delta_{\ell}  & : \mathbb{Z} / q \mathbb{Z}^* \to \mathbb{C} \\
 & : m \mapsto \begin{cases}
1 & m = \ell \\
0 &
\end{cases}
\end{align}
$$
extended to a function on $\mathbb{Z} / q \mathbb{Z}$, supported on $\mathbb{Z} / q \mathbb{Z}^*$ and extended periodically to $\mathbb{Z}$ (by the canonical surjection $\mathbb{Z} \to \mathbb{Z} / q \mathbb{Z}$).

Note that
$$
\sum_{p \in \wp, p \equiv \ell} \frac{1}{p^s} = \sum_{p \in \wp} \frac{\delta_{\ell}(p)}{p^s}
$$
for all $s > 1$ (all $s$ where the sum on the left is guaranteed to converge). Using finite Fourier analysis, we can decompose this sum. For convenience, we give it a name.

##### _definition:_ the modular characteristic series

The modular characteristic series of $\ell \in \mathbb{Z} / q \mathbb{Z}^*$ is the sum
$$
\sum_{p \in \wp} \frac{\delta_{\ell}(p)}{p^s}.
$$
Note that this is not an $L$-[[Fourier analysis --- math-139/notes/Dirichlet characters and series|series]] proper since $\delta_{\ell}$ is not a [[Fourier analysis --- math-139/notes/Finite Fourier analysis#_definition _ character, the dual group|character]] on $G$.

##### _lemma:_ Fourier decomposition of the modular characteristic series

For any $\ell \in \mathbb{Z} / q \mathbb{Z}^*$ the modular characteristic series decomposes as
$$
\sum_{p \in \wp} \frac{\delta_{\ell}(p)}{p^s} = \frac{1}{\lvert G \rvert } \sum_{\xi \in \widehat{G}} \overline{\chi_{\xi}(\ell)} \sum_{p \in \wp} \frac{\chi_{\xi}(p)}{p^s}.
$$

###### _proof:_

By [[Fourier analysis --- math-139/notes/Finite Fourier analysis#_theorem _ Fourier inversion|Fourier inversion]], we have (as functions on $\mathbb{Z} / q \mathbb{Z}^*$)
$$
\delta_{\ell} = \sum_{\xi \in \widehat{\mathbb{Z} / q \mathbb{Z}^*}} \hat{\delta}_{\ell}(\xi) \, \xi.
$$

However, because $\delta_{\ell}$ is so simple, its [[Fourier analysis --- math-139/notes/Finite Fourier analysis#_definition _ Fourier coefficient|Fourier coefficients]] $\hat{\delta}_{\ell}$ will be simple too. Explicitly,
$$
\hat{\delta}_{\ell}(\xi) = \frac{1}{\lvert G \rvert } \sum_{m \in G} \delta_{\ell}(m) \overline{\xi(m)} = \frac{\overline{\xi(\ell)}}{\lvert G \rvert }
$$
since $\delta_{\ell}$ is only nonzero when $m = \ell$. Extending this formula to all of $\mathbb{Z}$ and extending the $\xi$ to their [[Fourier analysis --- math-139/notes/Dirichlet characters and series#_definition _ Dirichlet character|Dirichlet characters]] $\chi_{\xi}$, we get
$$
\delta_{\ell}(m) = \frac{1}{\lvert G \rvert } \sum_{\xi \in \widehat{G}} \overline{\chi_{\xi}(\ell)} \chi_{\xi}(m).
$$
as functions on $\mathbb{Z}$. Plugging this into the definition of the modular characteristic series gives the desired formula.

##### _lemma:_ the trivial part of the modular characteristic series diverges as $s \to 1^+$

Let $1$ be the trivial character in $\widehat{G}$. Then 
$$
\sum_{p \in \wp} \frac{\chi_{1}(p)}{p^s} \to \infty
$$
as $s \to 1^+$.

###### _proof:_

$1(p) = 1$ for all $p \in \mathbb{Z} / q \mathbb{Z}^*$. Thus, $\chi_{1}(p) = 0$ only if $\gcd(p, q) \neq 1$. There are only finitely many such $p$ (all primes greater than $q$ are coprime with $q$). Thus,
$$
\sum_{p \in \wp} \frac{\chi_{1}(p)}{p^s} = \sum_{p \in \wp} \frac{1}{p^s} - \sum_{p \in \wp, p < q} \frac{1}{p^s}.
$$
As $s \to 1^+$ the sum on the left diverges (to $\infty$) and the sum on the right is finite, so their difference diverges (to $\infty$) as well.

##### _theorem:_ reduction of Dirichlet's theorem

If for any non-trivial [[Fourier analysis --- math-139/notes/Dirichlet characters and series#_definition _ Dirichlet character|Dirichlet character]] $\chi$ on $G$, 
$$
\sum_{p \in \wp} \frac{\chi(p)}{p^s}
$$
converges as $s \to 1^+$, then Dirichlet's theorem follows.

### The logarithm of $L$-series and further reduction

Since the $L$-series [[Fourier analysis --- math-139/notes/Dirichlet characters and series#_proposition _ niceness of $L$-series|satisfy niceness conditions]], we can define the logarithm of the $L$-series.

##### _definition:_ logarithm of the $L$-series

For $s > 1$ (where we know the $L$-series is non-vanishing) the logarithm of the $L$-series is given by
$$
\operatorname{log} L(s, \chi) = \int_{s}^\infty \frac{L'(s, \chi)}{L(s, \chi)} \, ds
$$
which converges since the integrand is $O(e^{-c s})$.

###### _proof:_

$\operatorname{Log}$ is just the [[Complex analysis --- math-135/notes/The complex logarithm#_theorem _ logarithms of functions|complex logarithm of a function]], so it follows by the same proof.

##### _proposition:_ the logarithm of the $L$-series is a genuine logarithm

For $s > 1$ we have
$$
e^{\operatorname{log} L(s, \chi)} = L(s, \chi).
$$

This now gives us addition/multiplication properties of the logarithm, and thus, allows us to prove
##### _proposition:_ the logarithmic form of the product formula

For $s > 1$, we have
$$
\operatorname{log} L(s, \chi) = \sum_{p \in \wp} \log \left( \frac{1}{1 - \chi(p) / p^s} \right).
$$
On the left the logarithm is the integral of the logarithmic derivative, and on the right, the logarithm is given by power series.

###### _proof sketch:_

Exponentiate both sides and use product properties. Show that the difference of the exponents is $2 \pi i M(s)$ where $M$ is a continuous function of integers that vanishes as $s \to \infty$, so is just $0$.

Note that for a non-trivial character, the logarithmic product formula can be approximated with bounded error by the logarithm approximation formula we showed earlier —
$$
\begin{align}
\operatorname{log} L(s, \chi) &  = \sum_{p \in \wp} \log \left( \frac{1}{1 - \chi(p) / p^s} \right)  \\
 & = \sum_{p \in \wp} \frac{\chi(p)}{p^s} + E(1 / p^s) \\
 & = \sum_{p \in \wp} \frac{\chi(p)}{p^s} + C  \\
 & = L(s, \chi) + C.
\end{align}
$$

If we can show that $L(1, \chi) \neq 0$ for all non-trivial characters, then we have that $\log L(s, \chi)$ is bounded as $s \to 1^+$ (just from its integral definition). This gives
$$
\lim_{ s \to 1^+ } \sum_{p \in \wp} \frac{\chi(p)}{p^s} < \infty.
$$

Thus, we have the reduction

##### _theorem:_ further reduction of Dirichlet's theorem

If, for each non-trivial Dirichlet character $\chi$ on $G$, its $L$-series doesn't vanish at $1$ — that is, $L(1, \chi) \neq 0$, then Dirichlet's theorem follows.

To prove that the $L$-series don't vanish for non-trivial characters, we divide into two different cases — real and complex characters.

### Complex Dirichlet characters

With some reasonable estimates we can show by contradiction that non-trivial complex Dirichlet characters $\chi$ have $L(1, \chi) \neq 0$.

First we show that the product of all $L$-series is bounded below

##### _lemma:_ the product of all Dirichlet $L$-series

For all $s > 1$,
$$
\prod_{\chi_{\xi}, \xi \in \widehat{G}} L(s, \chi_{\xi}) \geq 1.
$$
In particular, the product is real-valued.

##### _lemma:_ the $L$-series of the conjugate character

For all $s > 1$, if $L(1, \chi) = 0$, then $L(1, \overline{\chi}) = 0$.

###### _proof:_

Since the $L$-series is a series with real coefficients, we have $L(1, \bar{\chi}) = \overline{L(1, \chi)}$. The proof follows.

##### _lemma:_ upper bound on vanishing non-trivial $L$-series

If $\chi$ is non-trivial and $L(1, \chi) = 0$, then for all $s \in [1, 2]$, $\lvert L(\chi, s)  \rvert < C \lvert s - 1 \rvert$.

##### _lemma:_ upper bound on trivial $L$-series

If $\chi_{1}$ is the trivial character, then for all $s \in [1, 2]$, $\lvert L(\chi, s)  \rvert < C / \lvert s - 1 \rvert$.

##### _theorem:_ non-trivial complex $L$-series don't vanish

If $\chi$ is a non-trivial complex character, then $L(1, \chi) \neq 0$.

###### _proof:_

Suppose by way of contradiction that $L(1, \chi) = 0$. Then we also have $L(1, \overline{\chi}) = 0$. Thus, there are two terms in the product of all characters that vanish like $\lvert s - 1 \rvert$ as $s \to 1^+$.

The trivial character is the only character that grows and it only grows as $O(1 / \lvert s - 1 \rvert)$ as $s \to 1^+$. Thus, considering the three terms we know about, we get that the magnitude of the product behaves roughly like $\lvert s - 1 \rvert$ as $s \to 1^+$. Thus, the product vanishes, but we have shown this is not the case.

### Real characters and hyperbolic sums

The proof is harder because these have some real character. 

We will need the existence of the [[Complex analysis --- math-135/notes/Euler-Mascheroni constant|Euler-Mascheroni constant]] and a similar constant for the sum of square roots. Specifically, we need the following.

##### _proposition:_ Euler-Mascheroni and analogues for other $p$-series

As $N \to \infty$, we have
$$
\sum_{n = 1}^N \frac{1}{n} - \log N = O(1) + O(1 / N)
$$
and
$$
\sum_{n = 1}^N \frac{1}{\sqrt{ n }} - 2 \sqrt{ N } = O(1) + O(1 / \sqrt{N }).
$$

Our strategy will be to use this proposition to approximate $L(1, \chi)$ by the hyperbolic sum of $\chi(n) / \sqrt{ nm }$ over $(m, n) \in \mathbb{N} \times \mathbb{N}$ with $mn \le N$. Then we will show that the sum grows fast enough that $L(1, \chi) \neq 0$.

To show this, we need some more lemmas. 

##### _lemma:_ the divisor-sum of a real character is non-negative and positive for squares

For any natural number $k$, and non-trivial real Dirichlet character $\chi$ on $G$, we have
$$
\sum_{n \mid k} \chi(n) \geq \begin{cases}
0 \\
1 & k = \ell^{2} 
\end{cases}
$$
###### _proof:_

We first prove the lemma in the case that $k$ is prime power $p^\alpha$. In this case the value of the sum is completely determined by $\chi(p) \in \{ -1, 0, 1 \}$ — we have
$$
\sum_{n \mid k} \chi(n) = \chi(1) + \chi(p) + \dots + \chi(p^\alpha) 
$$
We get
$$
\sum_{n \mid k} \chi(n) = \begin{cases}
\alpha + 1 & \chi(p) = 1 \\
1 & \chi(p) = -1, \alpha \text{ even} \\
0 & \chi(p) = -1, \alpha \text{ odd} \\
1 & p \mid q \implies \chi(p) = 0
\end{cases}
$$
Notice that the reason for the reversal of the intuitive places even/odd for $\alpha$ is because we sum an additional $\chi(1) = 1$ first.

Now write $k = p_{1}^{\alpha_{1}} \cdots p_{m}^{\alpha_{m}}$. The divisors of $k$ are $n \in \{ p_{1}^{\beta_{1}} \cdots p_{m}^{\beta_{m}} \mid 0 \le \beta_{j} \le \alpha_{j}  \}$. Then, using a fundamental theorem of arithmetic trick again, we can rewrite
$$
\sum_{n \in \{ p_{1}^{\beta_{1}} \cdots p_{m}^{\beta_{m}} \}} \chi(n) = \prod_{j = 1}^m (\chi(p_{j}^0) + \chi(p_{j}) + \dots + \chi(p_{j}^{\alpha_{j}})) = \prod_{j = 1}^m \sum_{n \mid p_{j}^{\alpha_{j}}} \chi(n).
$$
The expression for the sum when $k = p^\alpha$ is now an expression for each of the multiplicands. It tells us that the product is always non-negative, and can only be $0$ if one of the $\alpha_{j}$ is odd. Thus, it can only be zero if $\alpha_{j}$ is non-square, and all squares have positive sum.

##### _lemma:_ the asymptotic cancellation lemma

For $a < b \in \mathbb{N}$ and a non-trivial real Dirichlet character $\chi$, we have
$$
\sum_{n = a}^b \frac{\chi(n)}{\sqrt{ n }} = O(1 / \sqrt{ a })
$$
and
$$
\sum_{n = a}^b \frac{\chi(n)}{n} = O(1 / a).
$$

###### _proof sketch:_

Use the [[Fourier analysis --- math-139/notes/Dirichlet characters and series#_lemma _ the cancellation lemma|cancellation lemma]]. This is actually a little subtle, but hopefully it's believable even without proof.

##### _definition:_ the hyperbolic character sum

Given a non-trivial real Dirichlet character $\chi$ on $G$, the hyperbolic character sum is
$$
S_{N} = \sum_{(m, n) \in A_{N}} \frac{\chi(n)}{\sqrt{ nm }}
$$
where $A_{N} = \{ (m, n) \in \mathbb{N} \times \mathbb{N} \mid mn \le N \}$ is the region of the natural number grid under the hyperbola $xy = N$.

##### _proposition:_ the hyperbolic sum grows logarithmically

There exists some constant positive $c$ such that $S_{N} \geq c \log N$.

###### _proof sketch:_

We can rewrite the sum over all $m, n$ with $nm \le N$ as a double sum over all $k \le N$ and all $m, n$ with $nm = k$ 
$$
\begin{align}
S_{N} & = \sum_{(m, n) \in A_{N}} \frac{\chi(n)}{\sqrt{ nm }} \\
& = \sum_{k = 1}^N \sum_{nm = k} \frac{\chi(n)}{\sqrt{ nm } }\\
& = \sum_{k = 1}^N \frac{1}{\sqrt{ k }} \sum_{n \mid k} \chi(n).
\end{align}
$$
Using our lemma about the divisor-sum of a character we can bound this sum below by at least the sum over squares. That is,
$$
\begin{align}
S_{N} & = \sum_{k = 1}^N \frac{1}{\sqrt{ k }} \sum_{n \mid k} \chi(n) \\
& \ge \sum_{k = 1, k = \ell^{2}}^N  \frac{1}{\sqrt{ k }} \\
& = \sum_{\ell = 1}^\sqrt{ N } \frac{1}{\ell}.
\end{align}
$$

Finally, due to the existence of the Euler-Mascheroni constant, this is last sum is just $\log \sqrt{ N } + O(1)$ (which of course is $c \log N + O(1)$ for $c = 1 / 2$).


##### _proposition:_ the $L$-series is well approximated by a hyperbolic sum

For positive integers $N$, we have
$$
S_{N} = 2 \sqrt{ N } L(1, \chi) + O(1).
$$

###### _proof:_

We split $S_{N}$ into a sum over three regions. That is, we split $A_{N}$ into three regions — the square $A_{N}^2 = \{ 1 \le m, n \le \sqrt{ N } \}$ and the two curvy triangles $A_{N}^1 = \{ 1 < m < \sqrt{ N }, \sqrt{ N } < n < N / m \}$ and $A_{N}^3 = \{ 1 \le n \le \sqrt{ N }, \sqrt{ N } \le m \le N / m \}$. We call the corresponding sums $S_{N}^1, S_{N}^2, S_{N}^3$ as well.

Splitting $S_{N}^1$ into a double sum, we write
$$
S_{N}^1 = \sum_{m = 1}^\sqrt{ N } \frac{1}{\sqrt{ m }} \sum_{n = \sqrt{ N }}^{N / m} \frac{\chi(n)}{\sqrt{ n }}.
$$
By asymptotic cancellation lemma, the interior sum is $O(1 / N^{1 / 4})$ which we can factor out. We then evaluate the exterior sum, and using the analogue of the Euler-Mascheroni constant for the $p$-series with $p = 1 / 2$, we get that it is $2N^{1 / 4} + O(1) + O(1 / N^{1 / 4})$. Multiplying everything together, we get
$$
S_{N}^1 = O(1 / N^{1 / 4})(2 N^{1 / 4} + O(1) + O(1 / N^{1 / 4}))
$$
which is just $S_{N}^1 = O(1)$.

Considering $S_{N}^2 + S_{N}^3$ together, we get
$$
\begin{align}
S_{N}^2 + S_{N}^3 & = \sum_{n = 1}^\sqrt{ N } \frac{\chi(n)}{\sqrt{ n }} \sum_{m = 1}^{N / n} \frac{1}{\sqrt{ m }} \\
& = \sum_{n = 1}^\sqrt{ N } \frac{\chi(n)}{\sqrt{ n }} \left (2 \sqrt{ N / n }  + c + O(\sqrt{ n / N }) \right ) \\
& = 2 \sqrt{ N } \sum_{n = 1}^{\sqrt{ N }} \frac{\chi(n)}{n } + c \sum_{1 \le n \le \sqrt{ N }} \frac{\chi(n)}{\sqrt{ n }} + O\left( \frac{1}{\sqrt{ N }} \sum_{1 \le n \le \sqrt{ N }} 1 \right).
\end{align}
$$

The last term is clearly $O(1)$. The second term is also $O(1)$ by the asymptotic cancellation lemma. Finally, as $N \to \infty$, since the tail of the $L$-series vanishes —
$$
\sum_{n = \sqrt{ N }}^\infty \frac{\chi (n)}{n} = O(1 / \sqrt{ N })
$$
by the asymptotic cancellation lemma, we have
$$
\begin{align}
S_{N} & = S_{N}^1 + S_{N}^2 + S_{N}^3  \\
& =  2 \sqrt{ N } \sum_{n = 1}^\sqrt{ N } \frac{\chi(n)}{n} + O(1) \\
 & = 2 \sqrt{ N } \left( L(1, \chi) - \sum_{n = \sqrt{ N }}^\infty \frac{\chi(n)}{n} \right) + O(1) \\
 & = 2 \sqrt{ N } (L(1, \chi) - O(1 / \sqrt{ N }) + O(1) \\
 & = 2 \sqrt{ N } L(1, \chi) + O(1).
\end{align}
$$

It follows that $L(1, \chi) \neq 0$ since that would force $S_{N} = O(1)$ which we proved is too small.