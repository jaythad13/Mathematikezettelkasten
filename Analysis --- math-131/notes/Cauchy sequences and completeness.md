---
tags:
- math-131/11
- math-177/3
- math-177/4
- math-177/6
- math-180/1
- anal
- metric
---

Till now, we've only been able to show that a [[Analysis --- math-131/notes/Sequences and convergence#_definition _ convergence|sequence converges]] if we have a guess for what it converges to already. Often this guess is obvious, but it would be nice to have a condition on the sequence directly that tells us whether it converges. Cauchy thought so too.

##### _definition:_ Cauchy sequence

Let $\{ x_{n} \}_{n}$ be a sequence in $X$. $\{ x_{n} \}_{n}$ is a **Cauchy sequence** if for each $\varepsilon > 0$, there exists $N$ such that $d(x_{n}, x_{m}) < \varepsilon$ for all $n, m \ge N$.

It's easy to show that all convergent sequences are Cauchy — just find $N$ such that all $x_{n}$ with $n > N$ are within $\varepsilon / 2$ of their limit and then use the [[Analysis --- math-131/notes/Metric spaces#_definition_ metric space, metric|triangle inequality]].

---

##### _lemma:_ Cauchy sequences are bounded

###### _proof:_

Let $\{ x_{n} \}_{n}$ be a Cauchy sequence. Choose $N$ such that for all $n, m \ge N$, $d(x_{m}, x_{n}) < 1$. Thus, for any $k$
$$
d(x_{k}, x_{N}) \le \max \{ 1, d(p_{1}, p_{N}, \dots, d(p_{N - 1}, p_{N})) \}.
$$

---

### Completeness

This doesn't guarantee convergence right away — points may get close to each other without getting close to any fixed point of the metric space. For example, $1, 1.4, 1.41, 1.414, 1.4142 \dots$ in the rationals (or any other sequence of non-repeating decimal expansions). Similarly, the residue sequence of $\sqrt{ 2 }$ modulo $7$ is Cauchy in $\mathbb{Q}$ with respect to the $7$-[[p-adic numbers --- math-177/notes/The p-adic numbers#_definition _ $p$-adic valuation, absolute value|absolute value]], but does not converge in $\mathbb{Q}$. However, there is an important class of metric spaces where all Cauchy sequences have to converge, and some of them are our favourites!

##### _definition:_ completeness

A metric space is **complete** if every Cauchy sequence converges.

---

##### _theorem:_ real spaces are complete

$\mathbb{R}^k$ is a complete metric space.

###### _proof:_

If $\{ x_{n} \}_{n}$ has finite range, it's easy to show that it must eventually be constant, and thus, must converge.

If $\{ x_{n} \}_{n}$ has infinite range, it is an infinite bounded set, and thus can be placed inside a closed and bounded, and [[Analysis --- math-131/notes/Compactness#_theorem _ Heine-Borel theorem|thus, compact]], set. Since it is an infinite set — [[Analysis --- math-131/notes/Compactness#_theorem _ Bolzano-Weierstrass theorem|it must have a limit point]] $x$. Thus, [[Analysis --- math-131/notes/Sequences and convergence#_proposition _ limit points induce convergent sequences|there must be a convergent subsequence]] $x_{n_{i}} \to x$. 

Given $\varepsilon > 0$, choose $I$ such that for all $i > I$, we have $d(x_{n_{i}}, x) < \varepsilon /2$ and choose $N$ such that for all $N$ such that for all $m, n > N$ we have  $d(x_{m}, x_{n}) < \varepsilon/2$. Then for $n \ge \max \{ I, N \}$
$$
d(x_{n}, x) \le d(x_{n}, x_{n_{n}}) + d(x_{n_{n}}, x) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
$$

---

This gives a further example

##### _example:_ [[Analysis --- math-131/notes/The space of continuous functions#_theorem _ $ mathcal{C}(K)$ is Analysis --- math-131/notes/Cauchy sequences and completeness _definition _ completeness complete|the space of continuous functions on a compact metric space is complete]]

----

Complete metric spaces are very nice.

##### _proposition:_ closed subsets of complete spaces are complete

Suppose $Y \subseteq X$ is a closed subset of a complete metric space. Then $Y$ is a complete metric space with the inherited metric from $X$.

---

##### _theorem:_ contraction mapping principle, or the Banach fixed point theorem

Suppose $f : X \to X$ is a **contraction** of a complete metric space. That is, there is some real $0 < \lambda < 1$ for all $x, y \in X$, we have $d(f(x), f(y)) \leq \lambda d(x, y)$. 

Then $f$ has a unique fixed point.

###### _proof:_

Choose any $x_{0} \in X$ and define $x_{i + 1} = f(x_{i})$. 

We claim $\{ x_{n} \}_{n \in \mathbb{N}}$ is Cauchy, and converges to a fixed point of $f$. Suppose $\varepsilon > 0$ and further, suppose $\lambda^N d(x_{0}, x_{1}) / (1 - \lambda) < \varepsilon$. Then, for all $m, n > N$ we have $d(x_{m}, x_{n}) < \varepsilon$. Specifically, assuming $m \leq n$, 
$$
\begin{align}
d(x_{m}, x_{n}) & < \lambda^m d(x_{0}, x_{n - m})  \\
 & \leq \lambda^m \sum_{i = 0}^{n - m - 1} d(x_{i}, x_{i + 1})  \\
 & \leq \lambda^m \sum_{i = 0}^\infty \lambda^i d(x_{0}, x_{1})  \\
 & \leq \frac{\lambda^m}{1 - \lambda} d(x_{0}, x_{1}) \\
 & < \varepsilon.
\end{align}
$$

Let $x_{n} \to x$. Since $d(x_{n}, f(x_{n})) \to 0$, we have $d(x, f(x)) = 0$.

Suppose $x, x'$ are fixed points of $f$. Then $d(x, x') \leq \lambda^n d(x, x)$ for each $n$, and so $d(x, x') = 0$. Thus, $x = x'$.

---

We can do even better than this (this doesn't have so much to do with completeness).

##### _corollary:_ fixed points of continuously varying functions vary continuously

Suppose $X$ is a complete metric space, $f : X \times Y \to X$ is continuous, and the function $f_{y} : x \mapsto f(x, y)$ is a contraction for each $y$. Then there is a continuous $g : Y \to X$ such that $f(g(y), y) = g(y)$ for each $y \in Y$.

###### _proof:_

Let $g : Y \to X$ be the function sending $y$ to the unique fixed point of the contraction $f_{y}$. Suppose $x \in X$ and consider the $\delta$-ball $B(x, \delta)$ centred at it. Its pre-image under $g$ is is all $y$ such that $f_{y}(x') = x'$ for some $x' \in B(x, \delta)$.

---

### Metric completion

In some sense $\mathbb{R}$ is the smallest complete metric space containing $\mathbb{Q}$ with its usual metric. In general, this is the notion of the completion of a metric space. We can complete any metric space by treating Cauchy sequences (appropriately identified) like points of the complete metric space.

##### _definition:_ equivalence in completion (of Cauchy sequences)

Two Cauchy sequences $\{ a_{n} \}_{n \in \mathbb{N}}$ and $\{ b_{n} \}_{n \in \mathbb{N}}$ in $X$, are **equivalent in completion** (denoted $\{ a_{n} \}_{n \in \mathbb{N}} \sim \{ b_{n} \}_{n \in \mathbb{N}}$) if and only if $d(a_{n}, b_{n}) \to 0$ (in the real numbers $\mathbb{R}$ with the Euclidean metric) as $n \to \infty$.

We claim this is an equivalence relation on the set of Cauchy sequences.

We denote the equivalence class of a Cauchy sequence $\{ a_{n} \}_{n \in \mathbb{N}}$ by $[\{ a_{n} \}_{n \in \mathbb{N}}]$.

---

##### _definition:_ completion of a metric space

The **completion** $\overline{X}$ of $X$ is the set of all Cauchy sequences in $X$ modulo equivalence in completion, endowed with the metric $\overline{d}(\{ a_{n} \}_{n \in \mathbb{N}}, \{ b_{n} \}_{n \in \mathbb{N}}) = \lim_{ n \to \infty } d(a_{n}, b_{n})$.

---

We claim this is a complete metric space, but we don't prove it here (we don't even show it is a metric space).