---
tags:
- math-157/1
- prob
---

The geometric and binomial distributions are two related probability functions to do with flipping coins.

### Geometric distribution

The geometric distribution (supported on $\mathbb{N}$) gives the probability that the $n$th [[Probability --- math-157/notes/Discrete probability#_example _ Bernoulli trials, or tossing a coin until it turns up heads|Bernoulli trial]] is the first success.

##### _definition:_ geometric distribution

A [[Probability --- math-157/notes/Discrete probability#_definition _ discrete random variable|random variable]] has **geometric distribution with parameter $p$** if its [[Probability --- math-157/notes/Discrete probability#_definition _ probability, probability function|probability function]] is
$$
f(n) = \begin{cases}
(1 - p)^{n - 1} p & n \in \mathbb{N} \\
0.
\end{cases}
$$

This may be abbreviated as $X \sim \operatorname{Geo}(p)$.

---

Note that this really is a probability function. [[Probability --- math-157/notes/Discrete probability#_proposition _ characterising probability functions|It suffices]] to check that $\sum_{n \in \mathbb{N}} f(n) = 1$. By geometric series we have
$$
\begin{align}
\sum_{n \in \mathbb{N}} f(n)  & = \sum_{n = 1}^\infty (1 - p)^{n - 1} p \\
 & = p \sum_{n = 0}^\infty (1 - p)^n \\
 & = p \frac{1}{1 - (1 - p)} \\
 & = 1.
\end{align}
$$

Note that using this probability function is not *always* the best way to do things. If you want to calculate $\mathbb{P}(X \geq 4)$ for $X \sim \operatorname{Geo}(p)$, then neither of summing $f(n)$ for all $n \geq 4$ or calculating $1 - \mathbb{P}(X < 4)$ by summing all $f(n)$ for $n < 4$ is particularly efficient. It is much more sensible to notice that $\mathbb{P}(X \geq 4)$ if and only if the first three tosses are tails which occurs with probability $(1 - p)^{3}$.

##### _proposition:_ expectation of a geometric random variable

Suppose $X \sim \operatorname{Geo}(p)$. Then $\mathbb{E}(X)$  

###### _proof:_

This is a straightforward calculation using the derivative trick. Let $g(x) = 1 / (1 - x)$. Note that $g$ has power series expansion $g(x) = \sum_{n = 0}^\infty x^n$ converging for $\lvert x \rvert < 1$ and that $g'(x) = 1 / (1 - x)^{2}$.
$$
\begin{align}
\mathbb{E}(X) & = \sum_{n \in \mathbb{N}} n (1 - p)^{n - 1} p \\
 & = p g'(1 - p) \\
 & = \frac{p}{(1 - (1 - p))^{2}} \\
 & = \frac{p}{p^{2}} \\
 & = \frac{1}{p}.
\end{align}
$$

---

This lines up with what we should expect!

### Binomial distribution

The binomial distribution is the probability function of a random variable counting the number of heads when a coin of probability $p$ is tossed $n$ times. 

Any particular sequence of $n$ coins with $k$ heads happens with probability $p^k(1 - p)^{n - k}$ by [[Probability --- math-157/notes/Discrete probability#_definition _ independence, dependence|independence]] of the coin tosses. There are $\binom{n}{k}$ such sequences. The product is then what the probability of $k$ heads should be.

##### _definition:_ binomial distribution

A random variable has **binomial distribution with parameters $n$ and $p$** if and only if its probability function is supported on $\{ 1, \dots, n \}$ with $f(k) = \binom{n}{k} p^k (1 - p)^{n - k}$.

---

To prove that $f$ is in fact a probability function requires a simple application of the [[Superdiscrete --- math-55A/notes/The binomial theorem#_theorem _ the binomial theorem|binomial theorem]].

##### _proposition:_ expectation of a binomial random variable

Suppose $X \sim \operatorname{Bin}(n, p)$. Then $\mathbb{E}(X) = n p$.

###### _proof:_

Notice that $X$ is the sum of the number of heads in each of $n$ independent trials of one coin toss. That is, $X = X_{1} + \dots + X_{n}$ for $X_{i} \sim \operatorname{Bin}(1, p)$. Clearly $\mathbb{E}(X_{i}) = p$. By [[Probability --- math-157/notes/Expected value#_theorem _ linearity of expectation|linearity of expectation]], $\mathbb{E}(X) = n p$.

---

This is one example of just how useful linearity of expectation is! Without this, we can still compute $\mathbb{E}(X) = np$, but the computation involves a whole chain of binomial identites and reindexing, et c.