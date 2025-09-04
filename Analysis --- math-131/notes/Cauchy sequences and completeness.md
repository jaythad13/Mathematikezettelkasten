---
tags:
- math-131/11
- math-177/3
- math-177/4
- anal
- metric
---

Till now, we've only been able to show that a [[Analysis --- math-131/notes/Sequences and convergence#_definition _ convergence|sequence converges]] if we have a guess for what it converges to already. Often this guess is obvious, but it would be nice to have a condition on the sequence directly that tells us whether it converges. Cauchy thought so too.

##### _definition:_ Cauchy sequence

Let $\{ x_{n} \}_{n}$ be a sequence in $X$. $\{ x_{n} \}_{n}$ is a Cauchy sequence if for each $\varepsilon > 0$, there exists $N$ such that $d(x_{n}, x_{m}) < \varepsilon$ for all $n, m \ge N$.

It's easy to show that all convergent sequences are Cauchy — just find $N$ such that all $x_{n}$ with $n > N$ are within $\varepsilon / 2$ of their limit and then use the [[Analysis --- math-131/notes/Metric spaces#_definition_ metric space, metric|triangle inequality]].

##### _lemma:_ Cauchy sequences are bounded

###### _proof:_

Let $\{ x_{n} \}_{n}$ be a Cauchy sequence. Choose $N$ such that for all $n, m \ge N$, $d(x_{m}, x_{n}) < 1$. Thus, for any $k$
$$
d(x_{k}, x_{N}) \le \max \{ 1, d(p_{1}, p_{N}, \dots, d(p_{N - 1}, p_{N})) \}.
$$

### Completeness

This doesn't guarantee convergence right away — points may get close to each other without getting close to any fixed point of the metric space. For example, $1, 1.4, 1.41, 1.414, 1.4142 \dots$ in the rationals (or any other sequence of non-repeating decimal expansions). Similarly, the residue sequence of $\sqrt{ 2 }$ modulo $7$ is Cauchy in $\mathbb{Q}$ with respect to the $7$-[[p-adic numbers --- math-177/notes/The p-adic numbers#_definition _ $p$-adic valuation, absolute value|absolute value]], but does not converge in $\mathbb{Q}$. However, there is an important class of metric spaces where all Cauchy sequences have to converge, and some of them are our favourites!

##### _definition:_ completeness

A metric space is complete if every Cauchy sequence converges.

##### _theorem:_ real spaces are complete

$\mathbb{R}^k$ is a complete metric space.

###### _proof:_

If $\{ x_{n} \}_{n}$ has finite range, it's easy to show that it must eventually be constant, and thus, must converge.

If $\{ x_{n} \}_{n}$ has infinite range, it is an infinite bounded set, and thus can be placed inside a closed and bounded, and [[Analysis --- math-131/notes/Compactness#_theorem _ Heine-Borel theorem|thus, compact]], set. Since it is an infinite set — [[Analysis --- math-131/notes/Compactness#_theorem _ Bolzano-Weierstrass theorem|it must have a limit point]] $x$. Thus, [[Analysis --- math-131/notes/Sequences and convergence#_proposition _ limit points induce convergent sequences|there must be a convergent subsequence]] $x_{n_{i}} \to x$. 

Given $\varepsilon > 0$, choose $I$ such that for all $i > I$, we have $d(x_{n_{i}}, x) < \varepsilon /2$ and choose $N$ such that for all $N$ such that for all $m, n > N$ we have  $d(x_{m}, x_{n}) < \varepsilon/2$. Then for $n \ge \max \{ I, N \}$
$$
d(x_{n}, x) \le d(x_{n}, x_{n_{n}}) + d(x_{n_{n}}, x) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
$$

### Metric completion

In some sense $\mathbb{R}$ is the smallest complete metric space containing $\mathbb{Q}$. In general, this is the notion of the completion of a metric space. We can complete any metric space by treating Cauchy sequences (appropriately identified) like points of the complete metric space.

##### _definition:_ equivalence in completion (of Cauchy sequences)

Two Cauchy sequences $\{ a_{n} \}_{n \in \mathbb{N}}$ and $\{ b_{n} \}_{n \in \mathbb{N}}$ in $X$, are **equivalent in completion** (denoted $\{ a_{n} \}_{n \in \mathbb{N}} \sim \{ b_{n} \}_{n \in \mathbb{N}}$) if and only if $d(a_{n}, b_{n}) \to 0$ (in the real numbers $\mathbb{R}$ with the Euclidean metric) as $n \to \infty$.

We claim this is an equivalence relation on the set of Cauchy sequences.

We denote the equivalence class of a Cauchy sequence $\{ a_{n} \}_{n \in \mathbb{N}}$ by $[\{ a_{n} \}_{n \in \mathbb{N}}]$.

##### _definition:_ completion of a metric space

The completion $\overline{X}$ of $X$ is the set of all Cauchy sequences in $X$ modulo equivalence in completion.

We claim this is a complete metric space, but we don't prove it here (we don't even show it is a metric space).