---
tags:
- math-131/13
- anal
---

We now have enough machinery to talk about Euler's number!

##### _theorem, definition:_ Euler's number

Euler's number is
$$
e = \sum_{n = 0}^\infty \frac{1}{n!} = \lim_{ n \to \infty } \left( 1 + \frac{1}{n} \right)^n
$$

###### _proof:_

The series converges since it is a [[Analysis --- math-131/notes/Series#_proposition _ partials sums of a positive series must be bounded|bounded positive series]]. Define $e$ as the series. Now we will show that the limit converges to $e$.

Note that we can expand the $(1 + 1 / n)^n$ by the binomial theorem —
$$
\begin{split}
\left( 1 + \frac{1}{n} \right)^n & = 1 + \binom{n}{1} n + \binom{n}{2} \frac{1}{n^{2}} + \dots + \binom{n}{n} \frac{1}{n^n} \\
 & = 1 + \frac{n}{n} \frac{1}{1!} + \frac{n(n - 1)}{n^{2}} \frac{1}{2!} + \dots + \frac{n!}{n^n} \frac{1}{n!} \\
 & \le 1 + \frac{1}{1!} + \dots + \frac{1}{n!}.
\end{split}
$$

Similarly, we can bound
$$
\left( 1 + \frac{1}{n} \right)^n \ge \frac{1}{1!} + \dots + \frac{1}{m!}
$$
for any $m$, as long as $n > m$.

Thus,
$$
\limsup_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n \le e \le \liminf_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n
$$
which means the upper and lower limits must agree and
$$
\lim_{ n \to \infty } \left( 1 + \frac{1}{n} \right)^n = e.
$$

We can prove that $e$ is irrational!

##### _theorem:_ $e$ is irrational

$e \not\in \mathbb{Q}$.

###### _proof:_

Suppose by way of contradiction that $e$ is rational. Write $e = p/q$ in least terms. 

Let $s_{n}$ be the $n$th partial sum of the series $\sum_{n = 1}^\infty \frac{1}{n!}$. Note that by the speed of the convergence $s_{n} \to e$,
$$
e - s_{n} < \frac{1}{n! n}.
$$
We can see this by noticing that $e - s_{n}$ is just the tail of the sum —
$$
\begin{split}
e - s_{n} & = \frac{1}{(n + 1)!} + \frac{1}{(n + 2)!} + \cdots \\
 & = \frac{1}{n!}\left( \frac{1}{n + 1} + \frac{1}{(n + 1)(n + 2)} + \cdots \right) \\
 & < \frac{1}{n!} \left( \frac{1}{n + 1} + \frac{1}{(n + 1)^{2}} + \cdots \right) \\
 & = \frac{1}{n!} \frac{1}{n + 1} \frac{1}{1 - \frac{1}{n  + 1}} \\
 & = \frac{1}{n!n}
\end{split}
$$

Thus,
$$
0 < e - s_{q} < \frac{1}{q! q}.
$$
Then the positive $q!(e - s_{q}) < \frac{1}{q} < 1$ is an integer, which is absurd.