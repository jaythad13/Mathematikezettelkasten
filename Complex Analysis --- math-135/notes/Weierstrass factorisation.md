---
tags:
- math-135/17
- anal
---

##### _theorem:_ the Weierstrass factorisation theorem

Let $a_{n}$ be a sequence in $\mathbb{C}$ with $a_{n} \to \infty$. Then there exists an entire function with zeroes at exactly the $a_{n}$ (with multiplicity).

###### _proof:_

We use Weierstrass elementary factors to construct the function. They are defined by
$$
\begin{align}
E_{0}(z) & = 1 - z \\
E_{p}(z) & = (1 - z) e^{z + z^{2} / 2 + \dots + z^p / p}.
\end{align}
$$

The idea is that
$$
- \operatorname{Log} (1 - z) = \sum_{n = 1}^\infty \frac{z^n}{n}
$$
for $\lvert z \rvert < 1$, so $E_{p}$ has a zero at $1$ but looks a lot like the constant $1$ function. 

##### _lemma:_ bounding Weierstrass factors

If $\lvert z \rvert < 1$, $\lvert E_{p}(z) - 1 \rvert \le \lvert z \rvert^{p + 1}$.

