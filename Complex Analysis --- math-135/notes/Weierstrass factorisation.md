---
tags:
- math-135/17
- math-135/18
- anal
- complex
---

If we wanted to create a function with zeroes exactly on a finite set, we consider $f(z) = (z - a_{1}) \dots (z - a_{n})$. If we want $f$ to have zeroes exactly on an infinite sequence, even with a [[Complex analysis --- math-135/notes/Infinite products#_definition _ infinite products|sensible notion of infinite products]] we can't just write $f(z) = \prod (z - a_{n})$ over all $n$ since this might not converge. The Weierstrass elementary functions $E_{p}$ are functions that we can just multiply together like that.

##### _definition:_ Weierstrass elementary factor

The Weierstrass elementary factor of degree $p$ is $E_{p} : \mathbb{C} \to \mathbb{C}$ by
$$
E_{p}(z) = (1 - z) e^{z + z^{2} /2 + \dots + z^p /p}
$$


Note that $E_{p}$ is an entire function with one zero of order $1$ at $1$. The idea is that
$$
- \operatorname{Log} (1 - z) = \sum_{n = 1}^\infty \frac{z^n}{n}
$$
for $\lvert z \rvert < 1$, so $E_{p} = (1 - z) e^{\sum z^n / n}$ looks a lot like a "constant" function $(1 - z) / (1 - z)$.

First we show that we can bound the growth of a Weierstrass elementary factor —

##### _proposition:_ bounding the growth of Weierstrass factors

If $\lvert z \rvert < 1$, the distance of the Weierstrass elementary factor from $1$ grows slower than $\lvert z \rvert^{p + 1}$. That is,
$$
\lvert 1 - E_{p}(z) \rvert \le \lvert z \rvert^{p + 1}.
$$

###### _proof:_

If $p = 0$, this is trivial — $\lvert 1 - (1 - z) \rvert = \lvert z \rvert \le \lvert z \rvert^{0 + 1}$.

We will bound the rest by considering the power series expansion of $E_{p}$. We claim

![[#_lemma _ the power series expansion of $E_{p}$]]

Then we can write
$$
\begin{split}
\lvert 1 - E_{p}(z) \rvert  & \le \left\lvert  \sum_{n = p + 1}^\infty a_{n} z^n  \right\rvert  \\
 & = \lvert z \rvert^{p + 1} \left\lvert  \sum_{n > p + 1} a_{n} z^{n - (p + 1)}  \right\rvert  \\
 & \le \lvert z \rvert^{p + 1}.
\end{split}
$$

##### _theorem:_ the Weierstrass factorisation theorem

Let $a_{n}$ be a sequence in $\mathbb{C}$ with $a_{n} \to \infty$. Then there exists an entire function with zeroes at exactly the $a_{n}$ (with multiplicity).

###### _proof:_

We claim the function $f : \mathbb{C} \to \mathbb{C}$ with
$$
f(z) = z^m \prod_{n = 1}^\infty E_{n}\left( \frac{z}{a_{n}} \right)
$$
is the exactly that function.

First we show that $f$ is holomorphic and satisfies the conditions on an arbitrary disc of radius $R$.

Since $a_{n} \to \infty$, there can only be finitely many $a_{n} \in D_{2R}(0)$. Thus, the finite product of holomorphic functions
$$
f(z) = z^m \prod_{\lvert a_{n}  \rvert < 2 R} E\left( \frac{z}{a_{n}} \right)
$$
converges.

For $\lvert a_{n} \rvert > 2 R$ and $z \in D_{R}(0)$ we have $\lvert z / a_{n} \rvert < 1 / 2$. We can bound the growth of Weierstrass factors —

Thus,
$$
\left\lvert  1 - E_{n}\left( \frac{z}{a_{n}} \right)  \right\rvert < \left\lvert  \frac{z}{a_{n}}  \right\rvert^{n + 1}  \le \left( \frac{1}{2} \right)^n.
$$

Since the functions have distance from $1$ uniformly bounded by an absolutely convergent series, their infinite product [[Complex analysis --- math-135/notes/Infinite products#_theorem _ infinite products of holomorphic functions|converges to a holomorphic function]].

##### _lemma:_ the power series expansion of $E_{p}$

The power series expansion of $E_{p}$ around $0$ by
$$
E_{p}(z) = 1 + \sum_{n = 1}^\infty a_{n} z^n
$$
has
1) $a_{n} = 0$ for $0 < n \le p$
2) $\sum_{n = 1}^\infty \lvert a_{n} \rvert = 1$.

###### _proof:_

Note that we could write $a_{0} = 1$ in the power series expansion since $E_{p}(0) = 1$.

Notice that the first derivative of $E_{p}$ is given by
$$
E_{p}'(z) = ((1 - z)(1 + z + \dots + z^{p - 1}) - 1) e^{z + z^{2} / 2 + \dots + z^p/ p} = - z^p e^{z + z^{2} / 2 + \dots + z^p / p}.
$$
Since this has a zero of order $p$ at $0$, we can see that it, and its first $p - 1$ derivatives have zeroes at $0$. That is, $a_{1}, \dots, a_{p} = 0$.

Further, since this is the negation of the composition and product of a group of functions whose Taylor series are real and non-negative, the remaining $a_{n}$ (for $n > p$) are all non-positive. We can use this to show that the sum of the coefficients converges absolutely to $1$.

We know $E_{p}(1) = 0$. But
$$
E_{p}(1) = 1 + \sum_{n = 1} a_{n}
$$
Thus,
$$
\sum_{n = 1}^\infty \lvert a_{n} \rvert = \sum_{n = 1}^\infty (-a_{n}) = 1.
$$