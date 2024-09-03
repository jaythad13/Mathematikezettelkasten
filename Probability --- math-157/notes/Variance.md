---
tags:
- math-157/3
- prob
---

If the [[Probability --- math-157/notes/Expected value|expected value]] of a random variable is the most important single number describing a random variable, then variance is the second most important. Where expected value describes the central tendencies of a random variable, variance describes the spread of a distribution.

##### _definition:_ variance, standard deviation

The variance of a discrete random variable $X$, with $\mathbb{E}(X) = \mu$, is
$$
\operatorname{Var}(X) = \mathbb{E}((X - \mu)^{2})
$$

The standard deviation of $X$ is $\sigma_{X} = \sqrt{ \operatorname{Var(X)} }$

Really, it's often more useful to use the standard deviation of a random variable — by taking the square root of variance, we have a quantity that's again in the same units of $X$. However, because 

##### _theorem:_ the expected value formula for variance

For any discrete random variable $X$,
$$
\operatorname{Var}(X) = \mathbb{E}(X^{2}) - \mathbb{E}(X)^{2}.
$$
###### _proof:_

Let $\mu = \mathbb{E}(X)$. Then, we know that
$$
\begin{split}
\operatorname{Var}(X) & = \mathbb{E}((X - \mu)^{2}) \\
 & = \mathbb{E}(X^{2} - 2 \mu X + \mu^{2}) \\
 & = \mathbb{E}(X^{2}) - 2 \mathbb{E}(X)^{2} + \mathbb{E}(X)^{2} \\
 & = \mathbb{E}(X^{2}) - \mathbb{E}(X)^{2}.
\end{split}
$$
A neat corollary of this is that $\mathbb{E}(X^{2}) \geq \mathbb{E}(X)^{2}$.