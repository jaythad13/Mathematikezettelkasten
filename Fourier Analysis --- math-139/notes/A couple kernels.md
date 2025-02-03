---
tags:
- math-135/3
- anal
---

Due to properties from complex analysis, it's helpful for us to have kernels — families of functions that have higher and higher bumps at $0$, that are in some sense, in the limit, the Dirac delta function.

### The Dirichlet kernel

##### _definition:_ the Dirichlet kernel

For $N \in \mathbb{N}$, the $N$th Dirichlet kernel is the function $D_{N}$ by
$$
D_{N}(x) = \sum_{n = - N}^N e^{i n x}.
$$

##### _lemma:_ the closed form of the Dirichlet kernel

Equivalently
$$
D_{N}(x) = \frac{\sin\left( \frac{2n + 1}{2}  x\right)}{\sin(x / 2)},
$$

Note that $D_{N}$ is the continuous function with
$$
\hat{D}_{N} = \begin{cases}
1 & -N \le n \le N \\
0
\end{cases}
$$

### The Poisson kernel

##### _definition:_ the Poisson kernel

For $r \in [0, 1)$, Poisson kernel is the function $P_{r} [-\pi, \pi] \to \mathbb{C}$
$$
P_{r}(\theta) = \sum_{n = - \infty}^\infty r^{\lvert n \rvert } e^{i n \theta}.
$$

Since $\sum_{n} r^{\lvert n \rvert}$ converges as a [[Mathematical Analysis I --- math-131/notes/Series#_example _ the geometric series|geometric series]], the rest converges by [[Complex Analysis --- math-135/notes/Analysis and (metric) topology review#_theorem _ Weierstrass $M$-test|Weierstrass]] $M$-test.

##### _lemma:_ the closed form of the Poisson kernel

$$
P_{r}(\theta) = \frac{1 - r^{2}}{1 + r^{2} - 2r \cos\theta}
$$

###### _proof:_

Given $\omega = r e ^{i \theta}$, we can write
$$
\begin{align}
P_{r}(\theta) & = \sum_{n = 0}^\infty \omega^n + \sum_{n = 1}^\infty \overline{\omega}^n \\
 & = \frac{1}{1 - \omega} + \frac{\overline{\omega}}{1 - \overline{\omega}} \\
 & = \frac{1 - \omega \bar{\omega}}{(1 - \omega) (1 - \bar{\omega})} \\
 & = \frac{1 - \lvert \omega \rvert ^{2}}{\lvert 1 - \omega \rvert ^{2}} \\
 & = \frac{1 - r^{2}}{1 + r^{2} - 2 r \cos\theta}
\end{align}
$$
where the denominator in the last line follows by the law of cosines.

We sort of already proved this in [[Complex Analysis --- math-135/attachments/homework/hw 4/hw 4.pdf|complex analysis]].
