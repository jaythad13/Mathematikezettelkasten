---
tags:
- math-157/1
- math-157/3
- prob
---

Let $\mathbb{P}, \Omega$ be a discrete probability space.

The expected value tells us something like what we expect the sample average of repeated tries of a random variable to give us. We will show later in this course that in trying lots of independent, identically distributed the sample average converges to the expected value.

##### _definition:_ expected value

The **expected value** of a [[Probability --- math-157/notes/Discrete probability#_definition _ discrete random variable|discrete random variable]] $X$ is
$$
\mathbb{E}(X) = \sum_{x \in \mathbb{R}} x \mathbb{P}(X = x)
$$
if the series converges.

---

Note that though this a sum over an uncountable set, we typically don't run into issues since $X$ is over a [[Probability --- math-157/notes/Discrete probability#_definition _ discrete measure space, discrete probability space, event, probability|discrete probability space]] $\Omega$. Thus, at most countably many $\mathbb{P}(X^\text{pre}(\alpha))$ are non-zero. If $\Omega$ is finite, $\mathbb{E}(X)$ always converges. More generally, if the $\alpha$ such that $\mathbb{P}(X^\text{pre}(\alpha)) \neq 0$ are bounded, then we also have no issues (then $\mathbb{E}(X) \leq \sup \alpha$). 

However, countable $\Omega$ need not have well-defined expectation for all random variables. Consider $\Omega = \mathbb{N}$ with $\mathbb{P}(n) = 6 / \pi^{2} n^{2}$ and $X : n \mapsto n^2$. Clearly, $\mathbb{E}(X) = \sum_{n \in \mathbb{N}} 6 / \pi^{2}$ diverges.

The classical finite example is that of a fair die.

##### _example:_ the expected value of a fair die

is $3 \frac{1}{2}$.

---

A very useful lemma about expectation is that we can reindex the sum to be over the probability space rather than $\mathbb{R}$. This will be the more useful form of expectation for us.

##### _lemma:_ expectation as a sum over probability space

Suppose $X$ is a random variable on $\mathbb{P}, \Omega$ with convergent expectation. Then
$$
\mathbb{E}(X) = \sum_{\omega \in \Omega} X(\omega) \mathbb{P}(\omega).
$$

###### _proof:_

$$
\begin{align}
\mathbb{E}(X) & = \sum_{x \in \mathbb{R}} x \mathbb{P}(X = x) \\
 & = \sum_{x \in \mathbb{R}} x \mathbb{P}(X^\text{pre}(\{ x \})) \\
 & = \sum_{x \in \mathbb{R}} \sum_{\omega \in X^\text{pre}(\{ x \})} X(\omega) \mathbb{P}(\omega) \\
 & = \sum_{\omega \in \Omega} X(\omega) \mathbb{P}(\omega).
\end{align}
$$
The first equality follows [[Probability --- math-157/notes/Discrete probability#_definition _ probability of a random variable|by definition]]. The last equality follows since the union of all $X^\text{pre}(\{ x \})$ as $x$ varies over all of $\mathbb{R}$ is exactly all of $\Omega$.

---

One reason this lemma is so nice is that proves that expectation is really nice!

##### _theorem:_ linearity of expectation

Expected value is a linear map $\mathbb{E} : V \to \mathbb{R}$ where $V \subseteq \mathbb{R}^\Omega$ is the vector space of random variables with convergent expectation.

###### _proof:_

Let $X, Y$ be random variables with convergent expectation. Let $\alpha, \beta \in \mathbb{R}$. All the work has been done by our lemma already.
$$
\begin{split}
\mathbb{E}(\alpha X + \beta Y) & = \sum_{\omega \in \Omega} (\alpha X + \beta Y)(\omega) \mathbb{P}(\omega) \\
 & = \alpha \sum_{\omega \in \Omega} X(\omega) \mathbb{P}(\omega) + \beta \sum_{\omega \in \Omega} \beta Y(\omega) \mathbb{P}(\omega) \\
 & = \alpha \mathbb{E}(X) + \beta \mathbb{E}(Y).
\end{split}
$$

---