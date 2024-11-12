---
tags:
- anal
- math-135/18
---

The Hadamard factorisation theorem gives an improvement to [[Complex Analysis --- math-135/notes/Weierstrass factorisation|Weierstrass' result]] if you know something about the growth of a function.

### Order of growth

The order of growth characterises the growth of a function in terms of the polynomial

##### _definition:_ order of growth

For an entire function $f$, if there exists $\rho$ such that for all $z \in \mathbb{C}$
$$
\lvert f(z) \rvert \leq A e^{B \lvert z \rvert^\rho}
$$
(where the constants $A, B$ can depend on $\rho$) then $f$ has order of growth less than $\rho$.

The order of growth of $f$ is the infimum of all $\rho$.

### Hadamard factorisation theorem

The Hadamard factorisation theorem allows us to characterise all functions with suitable order of growth as products of 

##### _theorem:_ Hadamard factorisation theorem

If $f$ is an entire function with order of growth $\rho_{0}$ (between integers $k \le \rho_{0} < k + 1$) and the non-zero sequence $a_{n}$ contains all zeroes of $f$ (with multiplicity, and $0$ has a zero of order $m$).

Then there exists a polynomial $p$ of degree $\deg p < k$ such that
$$
f(z) = e^{p(z)} z^m \prod_{n = 1}^\infty E_{k}\left( \frac{z}{a_{n}} \right)
$$

###### _proof:_


We can bound the growth of the number of zeroes of an entire function, and further, show that not too many of them are concentrated near the origin.

##### _lemma:_ the number and distribution of zeroes of entire functions

For any entire function of order of growth less than $\rho$ and zeroes on the sequence $a_{n} \to \infty$, we have $\mathfrak n_{f}(r) \le C r \rho$ for some constant $C$. 

Further, for any $s > \rho$,
$$
\sum_{n = 1}^\infty \frac{1}{\lvert a_{n} \rvert^s}
$$
converges.

Here $\mathfrak n_{f}(r)$ is the number of zeroes of $f$ within a disc of radius $r$.

###### _proof:_

Note that the set of positive real numbers $\mathbb{R}^+$ has a Haar measure $dx / x$ — integrating $dx / x$ over $[a, b]$ or $[Ra, Rb]$ will give you $\ln (b / a)$ either way. That is, the measure is invariant under the action of scaling by positive real numbers.

Since $\mathfrak{n}_{f}$ is an increasing function, we can write
$$
\begin{split}
\mathfrak{n}_{f}(r) \ln 2 &  = \mathfrak{n}_{f}(r) \int_{r}^{2r} \frac{dx}{x} \\
 & \le \int_{r}^{2r} \mathfrak{n}_{f}(x) \, \frac{dx}{x} \\
 & = \frac{1}{2 \pi} \int_{0}^{2 \pi} \log \lvert f(R e^{i \theta}) \rvert  \, d\theta - \log \lvert f(0) \rvert   
\end{split}
$$
where the last step follows from [[Complex Analysis --- math-135/notes/Jensen's formula#_proposition _ Jensen's difference, geometrically|Jensen's formula]],

We can bound the last bit using the order of growth of $f$. We get
$$
\begin{split}
\frac{1}{2 \pi} \int_{0}^{2 \pi} \log \lvert f(R e^{i \theta}) \rvert   \, d\theta  & \le \int_{0}^{2 \pi} \log \lvert A e^{B R \rho} \rvert  \, d\theta \le C r^\rho
\end{split}
$$
and thus, dividing by $\ln 2$, we can bound $\mathfrak n_{f}(r)$ similarly.

Again, since $f$ is non-zero, there can't be infinitely many zeroes of $f$ within the compact disc $\mathbb{D}$. Thus, the series $\sum_{n \ge 1} 1 / \lvert a_{n} \rvert^s$ converges if and only if the series $\sum_{\lvert a_{n} \rvert > 1} 1 / \lvert a_{n} \rvert^s$ converges. We further divide this series into zeroes in annuli of doubling radii. That is, we write
$$
\begin{split}
\sum_{\lvert a_{n} \rvert > 1} \frac{1}{\lvert a_{n} \rvert^s} & = \sum_{j = 0}^\infty \sum_{2^j < \lvert a_{j} \rvert < 2^{j + 1}} \frac{1}{\lvert a_{j} \rvert^s }  \\
 & = \sum_{j = 0}^\infty \mathfrak n_{f}(2^{j + 1}) 2^{-j s}  \\
 & = C \sum_{j = 0}^\infty 2^{(j + 1) \rho} 2^{-j s} \\
 & = 2^\rho C \sum_{j = 0}^\infty 2^{(\rho - s)j}.
\end{split}
$$
This converges for all $s > \rho$ (as a [[Mathematical Analysis I --- math-131/notes/Series#_example _ the geometric series|geometric series]]).