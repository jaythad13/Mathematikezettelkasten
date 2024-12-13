---
tags:
- math-135/16
- anal
---

If $g$ is holomorphic in the unit disc and never vanishes, then we can consider $\log \lvert g \rvert$. In particular,
$$
\ln \lvert g \rvert = \operatorname{Re} (\log g)
$$
and thus, we can apply the [[Complex Analysis --- math-135/attachments/homework/hw 4/hw 4.pdf#page=3|mean value property]] (from [[Complex Analysis --- math-135/notes/Cauchy integral formula#_theorem _ Cauchy integral formula|the Cauchy integral formula]]) of [[Complex Analysis --- math-135/attachments/homework/hw 1/hw 1.pdf#page=8|harmonic functions]] to get
$$
\ln \lvert g(0) \rvert = \frac{1}{2 \pi} \int_{0}^{2 \pi} \ln \lvert g(e^{i \theta}) \rvert  \, d\theta.
$$

Jensen's formula tries to do this by for arbitrary functions by making them non-vanishing, using Blaschke factors.

### Blaschke factors

##### _definition:_ Blaschke factor

For any point $a \in \mathbb{D}$, the Blaschke factor at $a$ is
$$
B_{a}(z) = \frac{z - a}{1 - \overline{a}z}
$$

We proved the following important properties of Blaschke factors in an early [[Complex Analysis --- math-135/attachments/homework/hw 1/hw 1.pdf#page=4|homework]].

##### _proposition:_ properties of Blaschke factors

1) The restriction $B_{a} : \mathbb{D} \to \mathbb{D}$ is a bijection (in particular, an involution interchanging $0$ and $a$).
2) $B_{a}$ is holomorphic on $\mathbb{D}$.
3) $B_{a}(z)$ is on $\partial \mathbb{D}$ if $z$ is on $\partial \mathbb{D}$ 
4) $B_{a}$ has exactly one zero in the unit disc — a simple zero at $a$.

### Jensen's formula

##### _theorem:_ Jensen's formula

Let $f$ be holomorphic in a neighbourhood of $\overline{D}$, the closed disc of radius $r$. If $\{ a_{1}, \dots, a_{k} \}$ are all the zeroes of $f$ in $\overline{D}$, then
$$
\ln \lvert f(0) \rvert + \sum_{j = 1}^k \ln \left\lvert  \frac{r}{a_{j}}  \right\rvert = \frac{1}{2 \pi} \int_{0}^{2 \pi} \ln \lvert f(r e^{i \theta}) \rvert  \, d\theta
$$

###### _proof:_

We can create a non-vanishing holomorphic function on $\overline{D}$ by dividing out all the zeroes using Blaschke factors (scaled down by $r$ so that $\overline{D}$ looks like $\mathbb{D}$). In particular, note that
$$
\frac{f(z)}{\prod B_{a_{j}/r}(z/r)}
$$
can be extended to a non-vanishing holomorphic function on $D$, which we call $g$. We apply the mean value property to get
$$
\ln \lvert g(0) \rvert = \frac{1}{2 \pi} \int_{0}^{2 \pi} \ln \lvert g(r e^{i \theta}) \rvert  \, d\theta.
$$

Using the multiplicative property of the logarithm, we can write
$$
\ln \lvert f(0) \rvert - \sum_{j = 1}^k \ln \left\lvert  B_{a_{j} / r}(z / r)  \right\rvert = \frac{1}{2 \pi} \int_{0}^{2 \pi} \ln \lvert f(r e^{i \theta}) \rvert  - \sum_{j = 1}^k  \ln \left\lvert {B_{a_{j} / r}(e^{i \theta})}  \right\rvert  \, d\theta.
$$
Since $\lvert B_{a_{j} / r}(e^{i \theta}) \rvert = 1$ which has logarithm $0$, the sum on the right vanishes. Since $B_{a_{j} / r}(0) = a_{j} / r$, the sum on the left is just the desired sum.

Thus,
$$
\ln \lvert f(0) \rvert + \sum_{j = 1}^k \ln \left\lvert  \frac{r}{a_{j}}  \right\rvert = \frac{1}{2 \pi} \int_{0}^{2 \pi} \ln \lvert f(r e^{i \theta}) \rvert  \, d\theta.
$$

Note that this formula can be proven for discs centred at any point in $\mathbb{C}$.

##### _corollary:_ Jensen's inequality

$$
\ln \lvert f(0) \rvert \le \frac{1}{2 \pi} \int_{0}^{2 \pi} \ln \lvert f(r e^{i \theta}) \rvert  \, d\theta 
$$

###### _proof:_

Since all the roots give $\lvert a_{j} \rvert < \lvert r \rvert$, it follows that the sum of the logarithms in Jensen's formula is positive.

We can get a geometric interpretation of the logarithms as follows.

##### _definition:_ $\mathfrak{n}_{f}(r)$

If $f$ is holomorphic on $\overline{D}$, a disc of radius $R$, then $\mathfrak{n}_{f}(r)$ is the number of zeroes in $D_{r}$, the disc of radius $r < R$.

##### _proposition:_ Jensen's difference, geometrically

If $\{ a_{1}, \dots, a_{k} \}$ are all the zeroes of $f$ in $\overline{D}$, then
$$
\int_{0}^R \frac{\mathfrak{n}_{f}(r)}{r} \, dr = \sum_{j = 1}^k \log \left\lvert  \frac{R}{a_{j}}  \right\rvert 
$$

###### _proof sketch:_

Note that $\mathfrak{n}_{f}(r)$ is really just the sum of characteristic functions on $[\lvert a_{j} \rvert, \infty)$ —
$$
\mathfrak{n}_{f}(r) = \sum_{j = 1}^k \chi_{[\lvert a_{j} \rvert , \infty)}(r)
$$
Thus,
$$
\begin{split}
\int_{0}^R \frac{\mathfrak{n}_{f}(r)}{r} \, dr & = \sum_{j = 1}^k \int_{\lvert a_{j} \rvert }^R \frac{1}{r} \, dr  \\
  & = \sum_{j = 1}^k \log \left\lvert  \frac{R}{a_{j}}  \right\rvert.
\end{split}
$$
