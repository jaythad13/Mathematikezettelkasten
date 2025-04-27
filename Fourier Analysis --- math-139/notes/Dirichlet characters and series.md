---
tags:
- math-139/30
- math-139/31
- fourier
- nt
- anal
---

Let $G = \mathbb{Z} / q \mathbb{Z}^*$ be the group of units modulo $q$. Let $\bar{\ell}$ be the residue of $\ell \in \mathbb{Z}$ modulo $q$.

Dirichlet characters and series generalise the [[Complex Analysis --- math-135/notes/The Riemann zeta function#_theorem _ the Euler product formula|Euler product formula]] to account for the data of primes modulo $q$.

##### _definition:_ Dirichlet character

Let $\xi \in \widehat{G}$ be a [[Fourier Analysis --- math-139/notes/Finite Fourier analysis#_definition _ character, the dual group|character]] $G \to S^1$, extended to a function $\xi^{\not *} : \mathbb{Z} / q \mathbb{Z} \to S^1$ by
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

Dirichlet $L$-series generalise [[Complex Analysis --- math-135/notes/The Riemann zeta function|the Riemann zeta function]] in a way that allows to take account of more subtle modular information.

##### _definition:_ Dirichlet $L$-series

For any Dirichlet character $\chi$ on $G$, its Dirichlet $L$-series is the function $L(-, \chi)$ given by
$$
L(s, \chi) = \sum_{n = 1}^\infty \frac{\chi(n)}{n^s}
$$
for $s > 1$.

Note that a Dirichlet $L$-series has a [[Complex Analysis --- math-135/notes/Cauchy integral formula#_theorem _ identity theorem|unique]] [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ meromorphic functions|meromorphic]] continuation to the whole complex plane. This unique analytic continuation is called an $L$-function. We will only need to deal with the $L$-series for the most part.

Just as the zeta function has a product formula, so does each $L$-series. This is only possible because Dirichlet characters are mutliplicative. Also, since $L(s, \chi)$ can be complex and our primary method for proving products is by taking logarithms, we need some complex analysis in the form of the [[Complex Analysis --- math-135/notes/The complex logarithm|complex logarithm]] and the power series expansion
$$
- \log(1- z) = \sum_{n = 1}^\infty \frac{z^n}{n}.
$$
Note that the [[Fourier Analysis --- math-139/notes/Dirichlet's theorem on arithmetic progressions#_lemma _ log approximation|logarithm approximation lemma]] used to prove that the sum of the reciprocals of primes diverges still holds here, and for the same reason, for $\lvert z \rvert < 1/2$ we have $\lvert \log(1 - z) \rvert \le 2 \lvert z \rvert$. Finally, we will once again need the sum criterion for convergence of infinite products —
![[Complex Analysis --- math-135/notes/Infinite products#_proposition _ absolute convergence of infinite products|Infinite products]]

##### _theorem:_ the product formula for $L$-series

For any Dirichlet character $\chi$ on $G$,
$$
L(s, \chi) = \prod_{p \in \wp} \frac{1}{1 - \chi(s) / p^s}.
$$

