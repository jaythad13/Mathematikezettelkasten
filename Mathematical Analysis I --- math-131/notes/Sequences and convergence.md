---
tags:
- math-131/10
- math-131/11
- math-131/12
- anal
---

Here we deal with the intuitive notion of convergence by making it rigorous for metric spaces, As usual, $X$ is a metric space with metric $d$.

##### _definition:_ sequence

A sequence is a function $\{ x_{n} \}_{n} : \mathbb{N} \to X$ with $n \mapsto x_{n}$.

##### _definition:_ convergence

Suppose $\{ x_{n} \}_{n}$ is a sequence in $X$. We say that $\{ x_{n} \}_{n}$ converges to $x \in X$, or $x_{n} \to x$ or $\lim_{ n \to \infty } x_{n} = x$ if, for each $\varepsilon > 0$ there exists some $N \in \mathbb{N}$ such that $d(x_{n}, x) < \varepsilon$ for all $n \ge N$.

Equivalently, $\{ x_{n} \}_{n}$ converges to $x$ if every neighbourhood $N_{r}(x)$ contains all but finitely many $x_{n}$.

##### _example:_ using the Archimedean property

The sequence $\{ 1/n \}_{n}$ converges in $\mathbb{R}$ to $0$ by the [[Mathematical Analysis I --- math-131/attachments/homework/hw 1/hw 1.pdf#page=4|Archimedean property]].

In the real numbers we can make sense of a sequence "diverging" as well — a sequence can blow up to infinity or negative infinity.

##### _definition:_ divergence to infinity

Suppose $\{ x_{n} \}_{n}$ is a sequence in $X$. If, for all $M \in \mathbb{R}$, there exists $N$ such that for all $n > N$, $x_{n} > M$, then $\{ x_{n} \}_{n}$ diverges to $\infty$. 

If, for all $M \in \mathbb{R}$, there exists $N$ such that for all $n > N$, $x_{n} < M$, then $\{ x_{n} \}_{n}$ diverges to $-\infty$.

### Basic facts about convergent sequences

##### _proposition:_ convergent sequences are bounded

If a sequence converges, it must be bounded.

###### _proof sketch:_

For all the infinitely many $x_{n}$ with $n \ge N$ we can bound the sequence to within distance $\varepsilon$ of what it converges to, and for the rest of the finitely many $x_{n}$, they are bounded by the maximum of their distances from $x$.

However, the converse isn't true.

##### _example:_ non-convergent bounded sequence

$\{ (-1)^n \}_{n}$ is a bounded sequence that doesn't converge.

##### _proposition:_ limit points induce convergent sequences

If $x$ is a [[Mathematical Analysis I --- math-131/notes/Metric spaces#_definition _ limit point|limit point]] of $E \subset X$, then there is a sequence $\{ x_{n} \}_{n}$ in $E$ converging to $x$.

###### _proof sketch:_

Choose $x_{n}$ to be some point of $E$ such that $x_{n} \in N_{1 / n}(x)$.

##### _proposition:_ the convergence of operations on the complex numbers

If $a_{n} \to A$ and $b_{n} \to B$, then $a_{n} + b_{n} \to A + B$ and $a_{n} b_{n} \to AB$. If $b_{n} \neq 0$ for all $n$ and $B \neq 0$, then $a_{n} / b_{n} \to A / B$.

###### _proof sketch:_

For $\varepsilon > 0$, choose $N_{a}, N_{b}$ such that $\lvert A - a_{n} \rvert < \frac{\varepsilon}{2}$ and $\lvert B - b_{n} \rvert < \frac{\varepsilon}{2}$ for all $n$. Thus, by the triangle inequality $\lvert A + B - (a_{n} + b_{n}) \rvert < \varepsilon$. Thus $a_{n} + b_{n} \to A + B$.

Notice that $AB - a_{n} b_{n} = - (A - a_{n})(B - b_{n}) - A(B - b_{n}) - B(A - a_{n})$. Thus by choosing sufficiently large $n$, we get
$$
\lvert AB - a_{n} b_{n} \rvert < \lvert A - a_{n} \rvert \lvert B - b_{n} \rvert + \lvert A \rvert  \lvert B - b_{n} \rvert + \lvert B \rvert  \lvert A - a_{n} \rvert < \varepsilon
$$
for any $\varepsilon$ we choose. Thus $a_{n} b_{n} \to AB$.

First we show $\frac{1}{b_{n}} \to \frac{1}{B}$ under our hypotheses. Let $b_{n}$ be bounded with $m < \lvert b_{n} \rvert < M$ which we know is true since it converges. Further, since all $b_{n} \neq 0$, we know $m > 0$. Thus,
$$
\left\lvert  \frac{1}{B} - \frac{1}{b_{n}}  \right\rvert = \frac{\lvert b_{n} - B \rvert }{b_{n} B} < \frac{\lvert b_{n} - B \rvert  m}{B}
$$
which we can make as small as we want by choosing $n$ sufficiently large. Then, it follows by the proof of convergence of products that $a_{n} / b_{n} \to A / B$.

##### _proposition:_ component-wise convergence — the projection principle

Let $y_{n} = (y_{n_{1}}, \dots, y_{n_{k}}) \in \mathbb{R}^k$. $y_{n} \to y = (y_{1}, \dots, y_{k})$ if and only if $y_{n_{i}} \to y_{i}$ for each $i \in \{ 1, \dots, k \}$.

###### _proof:_

Suppose $y_{n} \to y$. If $n > N$ gives $\lVert y - y_{n} \rVert < \varepsilon$, then since $\lVert y - y_{n} \rVert^{2} < \varepsilon^{2}$, each $(y_{i} - y_{n_{i}})^{2} < \varepsilon^{2}$, and thus, $\lvert y_{i} - y_{n_{i}} \rvert < \varepsilon$ for all $n > N$.

Suppose $y_{n_{i}} \to y_{i}$ for all $i \in \{ 1, \dots, k \}$. Then choose $N$ such that $n > N$ gives us $\lvert y_{n_{i}} - y_{i} \rvert < \frac{\varepsilon}{\sqrt{ k }}$. Thus the sum of their squares $\lVert y - y_{n} \rVert^{2}$ is less than $\varepsilon^{2}$. Thus, $\lVert y - y_{n} \rVert < \varepsilon$.

##### _example:_ projection principle breaks in infinite dimensions

Consider $y_{n} = (0, \dots, 0, 1, 0, \dots) \in \mathbb{R}^\infty$. Though each $y_{n_{i}}$ converges to $0$, $\lVert y_{n} \rVert = 1$ always, and thus, $y_{n_{i}}$ does not converge.

##### _definition:_ monotonic

If $\{ x_{n} \}_{n} \in X$ has $x_{n} \leq x_{n + 1}$ for all $n \in \mathbb{N}$, it is monotonically increasing.

If it has $x_{n} \geq x_{n + 1}$ for all $n \in \mathbb{N}$, it is monotonically decreasing.

##### _proposition:_ monotonic sequences blow up or converge

A monotonically increasing sequence converges or diverges to $\infty$. A monotonically decreasing sequences converges or diverges to $- \infty$.

###### _proof:_

Suppose $\{ x_{n} \}_{n}$ is monotonically increasing. If $\{ x_{n} \}_{n}$ is unbounded, we must have some $x_{N} > M$ for every $M \in \mathbb{R}$. But since the sequence is monotonically increasing, we must also have $x_{n} > x_{N} > M$ for all $n > N$.

If $\{ x_{n} \}_{n}$ is bounded, the sequence must have a supremum (by the [[Mathematical Analysis I --- math-131/notes/The reals#_definition _ least upper bound, supremum, least upper bound property|least upper bound property]]). Call this supremum $L$. Since $L$ is the least upper bound, $L - \varepsilon$ cannot bound $\{ x_{n} \}_{n}$. Thus, there must be some $x_{N} > L - \varepsilon$ and since $L$ is an upper bound, $L - \varepsilon < x_{N} < L$. Then by monotonicity, $L - \varepsilon < x_{n} < L$ for all $n \ge N$. Thus, $\{ x_{n} \}_{n}$ converges to $L$.

The proof is similar for monotonically decreasing sequences.

### Subsequences

A subsequence is what you think it is — take infinitely many terms of a sequence, but not necessarily all.

##### _definition:_ subsequence

If $\{ x_{n} \}_{n}$ is a sequence $n \mapsto x_{n}$, then a subsequence of $\{ x_{n} \}_{n}$ is $\{ x_{n} \}_{n}$ with domain restricted to an infinite subset $I \subset \mathbb{N}$ together with an order preserving bijection $\mathbb{N} \to I$ with $i \to n_{i}$. We write the subsequence as $\{ x_{n_{i}} \}_{n_{i}}$ by $i \mapsto x_{n_{i}}$.

If a sequence converges, subsequences aren't too interesting.

##### _proposition:_ subsequences converge to the same limit

A sequence $\{ x_{n} \}_{n}$ if and only if every subsequence $\{ x_{n_{i}} \}_{n_{i}}$.

###### _proof sketch:_

Notice that $1 \le n_{1} < n_{2} < \dots$, and thus, $n_{i} \ge i$ for all $i$. Since for all $i > N$ we have $d(x_{i}, x) < \varepsilon$ and thus $d(x_{n_{i}}, x) < \varepsilon$ for all $i > N$.

If all subsequences converge, since $\{ x_{n} \}_{n}$ converge, since $\{ x_{n} \}_{n}$ is a subsequence of itself, it must converge too. Thus all of the subsequences converge to $\lim_{ n \to \infty } x_{n}$.

##### _theorem, definition:_ subsequential limits

Given a sequence $\{ x_{n} \}_{n} \in X$, let the set of subsequential limits be
$$
E^* = \{ x \in X \mid x = \lim_{ n \to \infty } x_{n}  \}.
$$

$E^*$ is closed.

###### _proof sketch:_

Choose some $x_{n_{1}}$ at positive distance $\delta$ from a limit point $y$. We can always find $x \in E^*$ within distance $2^{ i} \delta$ of $y$ for any $i$. For any $x$, we can always find some $x_{n_{i}}$ within distance $2^{- i} \delta$ of $x$. Thus, by the triangle inequality, we can find $x_{n_{i}}$ within distance $2^{1 - i} \delta$ of $x$. That is, $x_{n_{i}} \to x$.

Even if we can't get convergence for a sequence, if it is bounded we can get a handle on its behaviour — we can look at what range it is ultimately bounded in.

##### _definition:_ $\limsup$ and $\liminf$

Let $E^*$ be the set of subsequential limits of $\{ x_{n} \}_{n}$. If $E^*$ is appropriately bounded, we define
$$
\limsup x_{n} = \sup E^*
$$
and
$$
\liminf x_{n} = \inf E^*.
$$

### Some special sequences

Here are some real examples of how these sequences are used —

##### _proposition:_ sequences of powers and roots

Let $p > 0$ be a fixed real number. Then
1) $\lim_{ n \to \infty } \frac{1}{n^p} = 0$.
2) $\lim_{ n \to \infty } p^{1/n} = 1$.
3) $\lim_{ n \to \infty } n^{1/n} = 1$.
4) For $\alpha \in \mathbb{R}$, $\lim_{ n \to \infty } \frac{n^\alpha}{(1 + p)^n}$.
5) If $\lvert x \rvert < 1$, $\lim_{ n \to \infty } x^n = 0$

###### _proof sketch:_

1) Just choose $N > (1 / \varepsilon)^{1/p}$. Thus, for all $n > N$, we have $n^p > 1 / \varepsilon$ and thus, $\lvert 1 / n^p - 0 \rvert < \varepsilon$.
2) First, assume $p > 1$. Then $p^{1/n} > 1$ for all $n$. Write $p^{1/n} = 1 +x_{n}$ and note that $x_{n} > 0$ always. Then $p = (1 + x_{n})^n$, which we can expand using the binomial theorem to get $p = 1 + n x_{n} + \dots + x_{n}^n$. Since all of the terms are positive, we have $n x_{n} < p$ and thus, $x_{n} < p/n$. Then $x_{n} \to 0$ and thus, $p^{1/n} \to 1$. Now if $p < 1$, then $(1 / p)^{1/n} \to 1$ and thus, $p^{1/n} \to 1$.
3) We can use the same trick again — we know that $n^{1/n} \ge 1$, and thus $x_{n} \ge 0$ for $n^{1/n} = 1 + x_{n}$. Using the binomial theorem we see that $\binom{n}{2} x_{n}^2 < n$. Thus, $x_{n} < \frac{2}{\sqrt{n - 1 }}$ and thus, $x_{n} \to 0$.
4) A bunch of bounds, see the book
5) Write $x = \frac{1}{1 + p}$ for some $p > 0$.