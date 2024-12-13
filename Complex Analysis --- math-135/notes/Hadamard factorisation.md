---
tags:
- anal
- math-135/18
- math-135/19
- math-135/20
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

The Hadamard factorisation theorem allows us to characterise all functions with suitable order of growth as products of [[Complex Analysis --- math-135/notes/Weierstrass factorisation#_definition _ Weierstrass elementary factor|elementary factors]] of constant degree rather than increasing degree $n \to \infty$, with a polynomial factor.

To show this theorem we will need to bound the growth of the number of zeroes of an entire function, and further, show that they are sparse.

##### _lemma:_ the number and distribution of zeroes of entire functions

For any entire function of order of growth less than $\rho$ and zeroes on the sequence $a_{n} \to \infty$, we have $\mathfrak n_{f}(r) \le C r^\rho$ for some constant $C$. 

Further, for any $s > \rho$ (in particular for $s = k = \lfloor \rho \rfloor + 1$)
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
 & \le \sum_{j = 0}^\infty \mathfrak n_{f}(2^{j + 1}) 2^{-j s}  \\
 & \le C \sum_{j = 0}^\infty 2^{(j + 1) \rho} 2^{-j s} \\
 & = 2^\rho C \sum_{j = 0}^\infty 2^{(\rho - s)j}.
\end{split}
$$
This converges for all $s > \rho$ (as a [[Mathematical Analysis I --- math-131/notes/Series#_example _ the geometric series|geometric series]]).

##### _theorem:_ Hadamard factorisation theorem

If $f$ is an entire function with order of growth $\rho$ between integers $k \le \rho < k + 1$ and the non-zero sequence $a_{n}$ contains all zeroes of $f$ (with multiplicity, and $0$ has a zero of order $m$).

Then there exists a polynomial $p$ of degree at most $k$ such that
$$
f(z) = e^{p(z)} z^m \prod_{n = 1}^\infty E_{k}\left( \frac{z}{a_{n}} \right)
$$

###### _proof:_

First we show that the product
$$
z^m \prod_{n = 1}^\infty E_{k}\left( \frac{z}{a_{n}} \right)
$$
converges uniformly. 

Let $K \subset \mathbb{C}$ be compact. As in the proof of Weierstrass factorisation, we want to show that $E_{k}(z/a_{n}) - 1$ is bounded. We know that the growth of a Weierstrass elementary factor is bounded with
$$
\left\lvert  E_{k}\left( \frac{z}{a_{n}} \right) - 1 \right\rvert  \le C \left\lvert  \frac{z}{a_{n}}  \right\rvert^{k + 1} \le \frac{C \sup_{z \in K} \lvert z \rvert^{k + 1}}{a_{n}^{k + 1}}
$$

Here, since $K$ is compact, there is a maximum $\lvert z \rvert$, so we can just bound everything by the maximum $\lvert z \rvert$. But then, by our lemma, since $\rho < k$,
$$
\sum \frac{1}{\lvert a_{n} \rvert^{k + 1}}
$$
converges. Now, $E_{k}(z/a_{n}) - 1$ is bounded by an absolutely convergent series, and thus, [[Complex Analysis --- math-135/notes/Infinite products#_theorem _ infinite products of holomorphic functions|the infinite product converges]].

Since the product and $f$ have [[Complex Analysis --- math-135/notes/The complex logarithm#_corollary _ functions with identical zeroes differ by an exponential|identical zeroes]], we have
$$
f(z) = e^{p(z)} z^m \prod_{n = 1}^\infty E_{k}\left( \frac{z}{a_{n}} \right)
$$
for some entire function $p$. It remains to be shown that $p$ is a polynomial of degree less than $k$. We need another lemma to show this.

![[#_lemma _ functions with bounded real part growth are polynomials]]

Now using this lemma, it suffices to show that
$$
\left\lvert  \prod_{n = 1}^\infty E_{k}\left( \frac{z}{a_{n}} \right)  \right\rvert \ge e^{- c \lvert z \rvert^s}.
$$
on some sequence $\lvert z \rvert = r_{n} \to \infty$ with $\rho < s < k + 1$. This would give us
$$
\left\lvert  z^m \prod_{n = 1}^\infty E_{k} \left ( \frac{z}{a_{n}} \right)  \right\rvert \ge e^{- c \lvert z \rvert^s}
$$
(for $\lvert z \rvert = r_{i}$ with $r_{i} > 1$). Finally this gives us
$$
\lvert e^{\operatorname{Re} p} \rvert = \lvert e^p \rvert = \frac{f(z)}{z^m \prod_{n = 1}^\infty E_{k}(z / a_{n})} \le A e^{B \lvert z \rvert^\rho + c \lvert z \rvert^s} \le A e^{C \lvert z \rvert ^s}.
$$
Finally, this bounds
$$
\operatorname{Re} p \le A e^{C \lvert z \rvert^s}
$$
which gives us that $p$ is a polynomial of degree at most $s$ and thus, degree at most $k = \lfloor s \rfloor$.

Thus, we only need to bound the product from below. Given a particular, $z$ we can divide the $a_{n}$ into two cases — $\lvert z / a_{n} \rvert \le 1/2$ and otherwise. If $\lvert z / a_{n} \rvert \le 1 / 2$, then we can just use our [[Complex Analysis --- math-135/notes/Weierstrass factorisation#_proposition _ bounding the growth of Weierstrass factors|bound on the growth of elementary factors]], and otherwise we can bound the exponential parts of the elementary factors from below using the triangle inequality and [[Mathematical Analysis I --- math-131/notes/Series#_example _ the geometric series|geometric series]]. Thus, we are only left to show that
$$
\prod_{\lvert z / a_{n} \rvert \ge 1 / 2} \left\lvert  1 - \frac{z}{a_{n}}  \right\rvert \ge e^{-c \lvert z \rvert^s}.
$$
We show this by showing that the bound holds for all $z$ that are more than $1 / \lvert a_{n} \rvert^{k + 1}$ away from each $a_{n}$ (it is non-trivial that there is a sequence of these $z$ that goes off to infinity) and using our bound on the growth of the number of zeroes of a function, we get the bound proper.

##### _lemma:_ functions with bounded real part growth are polynomials

Let $g$ be an entire function with $u = \operatorname{Re} g$ and $r_{n} \to \infty$ a sequence of positive radii. If there exists an $s \ge 0$ such that
$$
u(z) \le C \lvert z \rvert^s
$$
for $z = r_{n}$, then $g$ is a polynomial of order at most $s$.

###### _proof:_

Recall that for a power series $g(z) = \sum a_{n} z^n$ we have
$$
a_{n} r^n = \frac{1}{2 \pi} \int g(r e^{i \theta}) e^{- i n \theta} \, d\theta.
$$

Adding $g + \overline{g}$ to get $2 u$, and noticing that the corresponding integral of $\overline{g} e^{-in \theta} = 0$ when $n > 0$ (by taking conjugates of the integral $g e^{i n \theta}$ which is $0$ for $n > 0$)
$$
a_{n} = \frac{1}{\pi r^n} \int_{0}^{2 \pi} u(r e^{i \theta}) e^{- i n \theta} \, d\theta
$$