---
tags:
- math-157/3
- prob
---

The expected value tells us something like what we expect the sample average of repeated tries of a random variable to give us. We will show later in this course that in trying lots of independent, identically distributed the sample average converges to the expected value.

##### _definition:_ expected value

The expected value of a discrete random variable $X$ is
$$
\mathbb{E}(X) = \sum_{\text{all } k} k \mathbb{P}(X =k).
$$
For a function $g$, we often define
$$
\begin{split}
\mathbb{E}(g(X)) & = \sum_{\text{all } j} j \mathbb{P}(g(X) = j) \\
& = \sum_{\text{all } k} g(k) \mathbb{P}(X = k)
\end{split}
$$

The classical example is that of a fair die

##### _example:_ the expected value of a fair die

is $3 \frac{1}{2}$.

The reason expected value is so nice is linearity!

##### _definition:_ linearity of expectation

For any scalars $a, b \in \mathbb{R}$, $\mathbb{E}(aX + b) = a \mathbb{E}(X) + b$.

###### _proof:_

We can just use the little lemma encoded in our definition of $\mathbb{E}(g(X))$ —
$$
\begin{split}
\mathbb{E}(aX + b) & = \sum_{\text{all } k} (ak + b) \mathbb{P}(X = k) \\
 & = a \sum_{\text{all } k} k \mathbb{P}(X = k) + b \sum_{\text{all } k} \mathbb{P}(X = k) \\
 & = a \mathbb{E}(X) + 1b  \\
 & = a \mathbb{E}(X) + b
\end{split}
$$