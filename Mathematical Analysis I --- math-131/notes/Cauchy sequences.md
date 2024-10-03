---
tags:
- math-131/11
- anal
---

Till now, we've only been able to show that a [[Mathematical Analysis I --- math-131/notes/Sequences and convergence#_definition _ convergence|sequence converges]] if we have a guess for what it converges to already. Often this guess is obvious, but it would be nice to have a condition on the sequence directly that tells us whether it converges. Cauchy thought so too.

##### _definition:_ Cauchy sequence

Let $\{ x_{n} \}_{n}$ be a sequence in $X$. $\{ x_{n} \}_{n}$ is a Cauchy sequence if for each $\varepsilon > 0$, there exists $N$ such that $d(x_{n}, x_{m}) < \varepsilon$ for all $n, m \ge N$.

##### _lemma:_ Cauchy sequences are bounded

###### _proof:_

Let $\{ x_{n} \}_{n}$ be a Cauchy sequence. Choose $N$ such that for all $n, m \ge N$, $d(x_{m}, x_{n}) < 1$. Thus, for any $k$
$$
d(x_{k}, x_{N}) \le \max \{ 1, d(p_{1}, p_{N}, \dots, d(p_{N - 1}, p_{N})) \}.
$$

### Completeness

This doesn't guarantee convergence right away — points may get close to each other without getting close to any fixed point of the metric space. For example, $1, 1.4, 1.41, \dots$ in the rationals. However, there is an important class of metric spaces where all Cauchy sequences have to converge, and some of them are our favourites!

##### _definition:_ completeness

A metric space is complete if every Cauchy sequence converges.

##### _lemma:_ Cauchy sequences are bounded

###### _proof:_

Let $\{ x_{n} \}_{n}$ be a Cauchy sequence. Choose $N$ such that for all $n, m \ge N$, $d(x_{m}, x_{n}) < 1$. Thus, for any $k$
$$
d(x_{k}, x_{N}) \le \max \{ 1, d(p_{1}, p_{N}, \dots, d(p_{N - 1}, p_{N})) \}.
$$

##### _theorem:_ real spaces are complete

$\mathbb{R}^k$ is a complete metric space.

###### _proof:_

If $\{ x_{n} \}_{n}$ has finite range, it's easy to show that it must eventually be constant, and thus, must converge.

If $\{ x_{n} \}_{n}$ has infinite range, it is an infinite bounded set, and thus can be placed inside a closed and bounded, and [[Mathematical Analysis I --- math-131/notes/Compactness#_theorem _ Heine-Borel theorem|thus, compact]], set. Since it is an infinite set — [[Mathematical Analysis I --- math-131/notes/Compactness#_theorem _ Bolzano-Weierstrass theorem|it must have a limit point]] $x$. Thus, [[Mathematical Analysis I --- math-131/notes/Sequences and convergence#_proposition _ limit points induce convergent sequences|there must be a convergent subsequence]] $x_{n_{i}} \to x$. 

Given $\varepsilon > 0$, choose $I$ such that for all $i > I$, we have $d(x_{n_{i}}, x) < \varepsilon /2$ and choose $N$ such that for all $N$ such that for all $m, n > N$ we have  $d(x_{m}, x_{n}) < \varepsilon/2$. Then for $n \ge \max \{ I, N \}$
$$
d(x_{n}, x) \le d(x_{n}, x_{n_{n}}) + d(x_{n_{n}}, x) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
$$