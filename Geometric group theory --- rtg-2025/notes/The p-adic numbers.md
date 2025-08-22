---
tags:
- alg-nt
- metric
- rtg-2025
- napkin
---

The $p$-adics generalise two notions that we know, each in the direction of the other.

To solve a Diophantine equation, it's often useful to consider its behaviour modulo a prime $p$ (especially to disprove the existence of integer solutions). This isn't fool-proof because the canonical surjection $\mathbb{Z} \to \mathbb{Z} / p \mathbb{Z}$ loses a lot of information (it is far from injective). We have to consider all prime powers at once, but $\mathbb{Z} / p^e \mathbb{Z}$ is not algebraically nice in general.

To approximate a sum in the Euclidean norm on $\mathbb{Q}$ (say we want to approximate $\sum_{n = 1}^N 1 / n^{2}$ within some $\varepsilon > 0$) we use the convergence of the sum in $\mathbb{R}$ (here to $\pi^{2} / 6$) and then bound the error term. However, this doesn't work when the "error" we want to discard is number-theoretic — we can't get equality modulo some $p^e$ by doing analysis on $\mathbb{R}$.

The field of $p$-adic numbers $\mathbb{Q}_{p}$ generalises $\mathbb{Z} / p^e \mathbb{Z}$ by containing the "limit" or "completion" of all of them in the $p$-adic integers $\mathbb{Z}_{p}$. However, $\mathbb{Q}_{p}$ is a field like $\mathbb{R}$. It also generalises $\mathbb{R}$ as the [[Analysis --- math-131/notes/Cauchy sequences#_definition _ completeness|metric completion]] of $\mathbb{Q}$ with respect to a different metric (the $p$-adic valuation). This is more like $\mathbb{Z} / p^e \mathbb{Z}$ because the metric throws away information in a modulo $p^e$ sense by making high powers of $p$ small.

With these two simultaneous generalisations we will be able to solve problems like the one below.

##### _problem:_ approximating a sum, modulo $p^3$ (USA TST 2002/2)

For prime $p$, show that the value of
$$
f_{p}(x) = \sum_{k = 1}^{p - 1} \frac{1}{(px + k)^{2}} \pmod{p^{3}}
$$
does not depend on $x$.

### $p$-adics are algebraic completions

A $p$-adic integer generalises integers. Where integers have and are determined by an eventually constant sequence of residues modulo each $p^e$, a $p$-adic integer has and is determined by a sequence of residues modulo each $p^e$ that satisfies a compatibility relation — the residues modulo high powers agree with the residues modulo low powers, in the ring modulo low powers.

##### _definition:_ $p$-adic integers, $\mathbb{Z}_{p}$

The $p$-adic integers are the ring $\mathbb{Z}_{p}$ comprising all sequences $x = x_{1}, \dots, x_{e}, \dots$ of residues modulo $p^e$, satisfying $x_{i} \equiv x_{j} \pmod{p^i}$ for $i < j$. The ring addition and multiplication are component-wise.

Note that the additive and multiplicative identities have residue sequences $(0, 0, \dots)$ and $(1, 1, \dots )$ respectively.

In fact, this is just a categorical definition as a [[Algebraic geometry --- rising-sea/notes/Limits and colimits|limit]]. The $p$-adic numbers are the limit of the chain of maps $\mathbb{Z} / (p^j) \to \mathbb{Z} / (p^i)$ where $j > i$.

![[Algebraic geometry --- rising-sea/notes/Limits and colimits#_example _ $p$-adic numbers|Limits and colimits]]

In particular, $\mathbb{Z}$ and its commuting reduction modulo $p^e$ maps give rise to a map (an injection in fact) $\mathbb{Z} \to \mathbb{Z} _p$.

Residues modulo $p^e$ and expansions in base $p$ are two sides of the same coin. Just as eventually constant (compatible) residue sequences are generalised to arbitrary (compatible) residue sequences, we can generalise eventually $0$ base $p$ expansions to arbitrary base $p$ expansions. 

In particular, we can write every $p$-adic number as a base $p$-expansion and vice-versa. For $x \in \mathbb{Z}_{p}$ given by a sequence of residues $(x_{i})_{i \in \mathbb{N}}$ modulo $p^i$ we can write
$$
x = x_{1} p^0 + \frac{x_{2} - x_{1}}{p^1} p^1 + \dots + \frac{x_{e + 1} - x_{e}}{p^e} p^e + \dots
$$
Also, given a base expansion (with coefficients $a_{n} < p$)
$$
x = \sum_{n = 0}^\infty a_n p^n
$$
we get a (compatible) residue sequence $(x_{i})_{i \in \mathbb{N}}$ of partial sums $x_{i} = \sum_{n = 0}^i a_{n} p^n$.

So far, the construction we have works for non-prime base as well. Indeed, there are $n$-adic "integers" for each $n > 1$. However, they differ in their units. In particular, the $n$-adic integers are not, integral domains unless $n$ is a prime. Essentially this is because for $n = p_{1}^{e_{1}} \cdots p_{r}{e^r}$ we have $\mathbb{Z}_{n} \cong \mathbb{Z}_{p_{1}} \times \cdots \mathbb{Z}_{p_{r}}$ and so we have non-trivial ($x \neq 0, 1$) solutions to $x(x - 1) = 0$ by $x = (0, 1, 0, \dots, 0)$.

##### _proposition:_ $\mathbb{Z}_{p}$ is an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]]

###### _proof:_

Note that $0 \in \mathbb{Z}_{p}$ has residue sequence $(0, 0, \dots)$. If $x = (x_{i})_{i \in \mathbb{N}}, y = (y_{i})_{i \in \mathbb{N}}$ have $xy = 0$, then for each $i \in \mathbb{N}$ we have $x_{i} y_{i} \equiv 0 \pmod {p^i}$. Let $j$ be the minimal natural number such that $x_{j} \neq 0$ and similarly let $k$ be the minimal natural number such that $y_{k} \neq 0$. Since, for each $i \in \mathbb{N}$ we have $p^i \mid x_{i} y_{i}$ and we also have $p^j \mid x_{i}$ and $p^k \mid y_{i}$, we must have $j + k \geq i$. This forces $\max{j, k} \geq i / 2$. Finally, this forces $\max{j, k}$ greater than all natural numbers, and thus, one of $x$ and $y$ must have all residues equal to $0$.

In fact, we can characterise all units in $\mathbb{Z}_{p}$. Just as in $\mathbb{F}[[x]]$ where the units are those not in $(x)$, in $\mathbb{Z}_{p}$ the units are those with non-zero value modulo $p$.

##### _proposition:_ units in $\mathbb{Z}_{p}$

$x = (x_{j})_{j \in \mathbb{N}} \in \mathbb{Z}_{p}$ is a [[Abstract algebra --- math-171/notes/Rings#_definition _ unit|unit]] if and only if $x_{1} \not \equiv 0 \pmod p$.

###### _proof:_

If $x_{1} \equiv 0$, then the product of $x$ with any $y$ will have residue $0$ modulo $p$, and is thus, not $1$.

If $x_{1} \not \equiv 0$, then there is some $y_{1} \in \mathbb{Z} / p \mathbb{Z}$ such that $x_{1} y_{1} \equiv 1$ (since $\mathbb{Z} / p \mathbb{Z}$ [[Superdiscrete --- math-55A/notes/Modular arithmetic#_corollary _ Wilson's theorem|is a field]]). Also, each $x_{i} \equiv x_{1} \not \equiv 0$ modulo $p$, so $(x_{i}, p^i) = 1$, and $x_{i}$ has an inverse $y_{i}$ as well. These $y_{i}$ are compatible since they are all have the same 

Since $\mathbb{Z}_{p}$ is an integral domain, it has a well-defined fraction field. Just as $Q(\mathbb{Z}) = \mathbb{Q}$, we define the $p$-adic numbers as the fraction field of $\mathbb{Z}_{p}$. 

##### _definition:_ $p$-adic numbers, $\mathbb{Q}_{p}$

The $p$-adic numbers $\mathbb{Q}_{p}$ are the [[Algebraic geometry --- rising-sea/notes/Localisation, categorically#_definition _ localisation of a ring, localisations at a prime, fraction field|fraction field]] $Q(\mathbb{Z}_{p})$ of the $p$-adic integers.

However, just as we don't typically think of [[Complex analysis --- math-135/notes/Laurent series|Laurent series]] $\mathbb{F}((x))$ as ratios of formal power series in $\mathbb{F}[[x]]$, we don't want to do so for $\mathbb{Q}_{p}$ either. We can instead give a formal Laurent series expansion of elements of $\mathbb{Q}_{p}$.

##### _proposition:_ $\mathbb{Q}_{p}$ looks like formal Laurent series

Every non-zero element of $\mathbb{Q}_{p}$ can be uniquely written $x / p^k$ for some $x \in \mathbb{Z}_{p}^\times$ and some integer $k \in \mathbb{Z}$.

###### _proof:_

It suffices to show $1 / y \in \mathbb{Q}_{p}$ for $y \in \mathbb{Z}_{p}$ is $x / p^k$. 

Write $y = \sum_{n \geq m} a_{n} p^n$ so that $a_{m} \not \equiv 0$. Then $y = a_{m} p^m \sum_{n = 0}^\infty a_{m + n} p^n / a_{m} = a_{m} p^m z$. Since the first term of the series $z$ is $a_{m} / a_{m} = 1$, $z$ has an inverse in $\mathbb{Z}_{p}$. Also, $a_{m}$ has an inverse in $\mathbb{Z}_{p}$ since $a_{m} \not \equiv 0$. Thus, we can write
$$
\frac{1}{y} = \frac{z^{-1} a_{m}^{-1}}{p^k}
$$
for $k = m$

### $p$-adics are analytic completions

We can also obtain the $p$-adic numbers analytically, by making large $p^e$ very small. 

##### _definition:_ $p$-adic valuation, absolute value

The $p$-adic valuation $\nu_{p} : \mathbb{Q}_{p}^\times \to \mathbb{Z}$ is given by the largest $\nu_{p}(x) = k$ for the unique product $x = p^k z$ with $z \in \mathbb{Z}_{p}$.

Equivalently, for $x \in \mathbb{Z}_{p} \setminus \{ 0 \}$, $\nu_{p}(x)$ is the largest $i$ such that $x_{i} \equiv 0 \pmod{p^i}$ in the residue sequence $x = (x_{i})_{i \in \mathbb{N}}$, and can be extended to $\mathbb{Q}_{p}^\times$ as a homomorphism satisfying $\nu_{p}(xy) = \nu_{p}(x) + \nu_{p}(y)$.

The $p$-adic absolute value is given by $\lvert x \rvert_{p} = p^{- \nu_{p}(x)}$.

Note then that $x, y \in \mathbb{Q}_{p}$ are close with $\nu_{p}(x - y)$ big and $\lvert x - y \rvert_{p}$ small when $x - y$ is divisible by a large power of $p$.

While here we defined the valuation and absolute value in their full generality on $\mathbb{Q}_{p}$, they are still natural, even on $\mathbb{Q}$ — they are just the natural absolute value if you value information modulo $p^e$. Further, it is Ostrowski's theorem that the only absolute values on $\mathbb{Q}$ (up to scaling) are the trivial norm, the Euclidean norm, and the $p$-adic absolute value (for each prime $p$). It turns out then that $\mathbb{Q}_{p}$ is the [[Analysis --- math-131/notes/Cauchy sequences#_definition _ completeness|completion]] of $\mathbb{Q}$ with respect to the $p$-adic absolute value.

This absolute value has wonderful properties — not only are addition and multiplication continuous, but also it turns $\mathbb{Q}$ and $\mathbb{Q}_{p}$ into ultrametric spaces satisfying the strong triangle inequality.

##### _proposition:_ the $p$-adic absolute value is an ultrametric

For any $x, y \in \mathbb{Q}_{p}$ we have the strong triangle inequality
$$
\lvert x + y \rvert _{p} \leq \max \{ \lvert x \rvert _{p}, \lvert y \rvert _{p} \}.
$$
with equality if (but not only if) $\lvert x \rvert_{p} \neq \lvert y \rvert_{p}$.

###### _proof:_

Suppose $x, y \in \mathbb{Z}_{p}$. Then if $p^i \mid x$ and $p^j \mid y$ (assuming without loss of generality $p^i \leq p^j$) we have $p^i \mid (x + y)$. If $i$ and $j$ are maximal, then we have
$$
\lvert x + y \rvert_{p} \le \frac{1}{p^i} \le \max \{ \lvert x \rvert _{p}, \lvert y \rvert _{p} \} = \frac{1}{p^i}. 
$$

By writing $p$-adic numbers as $p^{k_{1}} x$ and $p^{k_{2}} y$ (for non-positive $k_{1} \leq k_{2}$) we can get the same result for all $p$-adic numbers. In particular, we have
$$
\begin{align}
\lvert p^{k_{1}} x + p^{k_{2}} y \rvert_{p}  & \le \lvert p^{k_{1}} \rvert {\lvert x + p^k y \rvert_{p} } \\
 &  \le \frac{1}{p^{k_{1}}} \max \left\{  \lvert x \rvert_{p}, \frac{\lvert y \rvert _{p}}{p^k}   \right\}  \\
& = \max \left\{ \frac{\lvert x \rvert _{p}}{p^{k_{1}}}, \frac{\lvert y \rvert _{p}}{p^{k_{2}}}  \right\}  \\
 & = \max \{ \lvert p^{k_{1}} x \rvert _{p}, \lvert p^{k_{2}} y \rvert_{p} \}.
\end{align}
$$
for $k = k_{2} - k_{1} \geq 0$.

There is a reverse version of the strong triangle inequality —

##### _corollary:_ the reverse strong triangle inequality

For any $x, y \in \mathbb{Q}_{p}$ with $\lvert x \rvert_{p} \neq \lvert y \rvert_{p}$, we have
$$
\lvert x - y \rvert_{p} \geq \max  \{ \lvert x \rvert_{p} , \lvert y \rvert_{p} \} .
$$

###### _proof:_

Suppose without loss of generality that $\lvert x \rvert_{p} > \lvert y \rvert_{p}$. Note that $x = (x - y) + (-y)$, so we have
$$
\lvert x \rvert _{p} \leq \max \{ \lvert x - y \rvert _{p}, \lvert y \rvert _{p} \}
$$
Since $\lvert y \rvert_{p} \not \geq \lvert x \rvert_{p}$, it must be that $\lvert x \rvert_{p} \le \lvert x - y \rvert_{p}$.

The strong triangle inequality also implies that the absolute value is not archimedean.

##### _corollary:_ $\mathbb{Q}_{p}$ is non-archimedean

There exists $x \in \mathbb{Q}_{p}^\times$ such that no integer $n \in \mathbb{Z} \subseteq \mathbb{Z}_{p}$ has $\lvert 1 / n \rvert_{p} < \lvert x \rvert_{p}$.

###### _proof:_

Notice that every integer has $p$-adic absolute value at most $1$, since they have $p$-adic valuation at least $0$. Thus, $1 / n$ has $p$-adic absolute value at least $1$. Alternatively, bound $\lvert n \rvert_{p} \leq \lvert 1 \rvert_{p} = 1$ using the strong triangle inequality. Choose $x$ to be any integer divisible by $p$ (and thus, having absolute value less than $1$). There is no $1 / n$ with absolute value less than it.

##### _theorem:_ $\mathbb{Q}_{p}$ is metrically complete

$\mathbb{Q}_{p}$ is the metric completion of $\mathbb{Q}$ with respect to the $p$-adic metric.

We could define $\mathbb{Q}_{p}$ as the completion of $\mathbb{Q}$ with this metric. Then we would define the integers as follows.

##### _proposition:_ a metric description of $\mathbb{Z}_{p}$

$\mathbb{Z}_{p}$ is exactly those $x \in \mathbb{Q}_{p}$ with $\lvert x \rvert_{p} \leq 1$.

### Solving the motivating problem

This means that we can solve the motivating problem! 

We just need two tools that follow (fairly easily) from $p$-adic analysis.

##### _proposition:_ $p$-adic geometric series

Let $x \in \mathbb{Q}_{p}$ have $\lvert x \rvert_{p} < 1$ (so $x \in \mathbb{Z}_{p}$ actually). Then
$$
\frac{1}{1 - x} = \sum_{n = 0}^\infty x^n.
$$
For example, $-1 / 2 = 1 + 3 + 3^{2} + \dots$ in $\mathbb{Z}_{3}$.

This helps prove the generalised binomial theorem.

##### _theorem:_ the generalised $p$-adic binomial theorem

For $x \in \mathbb{Q}_{p}$ with $\lvert x \rvert_{p} < 1$, for each $r \in \mathbb{Q}$ we have
$$
\sum_{n = 0}^\infty \binom{r}{n} x^n =  (1 + x)^r.
$$

![[#_problem _ approximating a sum, modulo $p 3$ (USA TST 2002/2)]]
###### _solution:_

We can use some algebraic manipulations to put $f_{p}$ into a form amenable to the generalised binomial theorem —
$$
\begin{align}
f_{p}(x) & = \sum_{k = 1}^{p - 1} \frac{1}{(px + k)^{2}}  \\
 & = \sum_{k = 1}^{p - 1} \frac{1}{k^{2}} \left( 1 + \frac{px}{k} \right)^{2} \\
 & = \sum_{k = 1}^{p - 1} \frac{1}{k^{2}} \sum_{n \geq 0} \binom{-2}{n} \left( \frac{px}{k} \right)^n \\
 & = \sum_{n \geq 0} \binom{-2}{n} \sum_{k = 1}^{p - 1} \frac{1}{k^{2}} \left( \frac{x}{k} \right)^n p^n \\
\end{align}
$$

But now we can reduce modulo $p^3$ to get
$$
f_{p}(x) \equiv \sum_{k = 1}^{p - 1} \frac{1}{k^{2}} - 2x \left( \sum_{k = 1}^{p - 1} \frac{1}{k^{3}} \right) p + 3 x^{2} \left( \sum_{k = 1}^{p - 1} \frac{1}{k^4} \right) p^{2} \pmod{p^3}.
$$
It follows from induction that the last two sums are divisible by $p$ (or in general, for top index $n$, divisible by $n + 1$) and thus, that the sum does not depend on $x$.

Note what we did here really needed $\mathbb{Q}_{p}$ as an algebraic and as an analytic structure! We used the analytic structure to get convergence of series that don't converge in $\mathbb{R}$ and to throw away all the information apart from modulo $p^{3}$. We also used the algebraic fact that $\mathbb{Z}$ and $\mathbb{Q}$ embed nicely in $\mathbb{Q}_{p}$ to mean that we could do all of the work in $\mathbb{Q}_{p}$ and actually recover values in $\mathbb{Z}$.

### The topology of the $p$-adic numbers

The topology that the $p$-adic norm induces on $\mathbb{Q}_{p}$ and $\mathbb{Z}_{p}$ is terrifying. In particular, $\mathbb{Z}_{p}$ is an open, compact subset of the non-compact set $\mathbb{Q}_{p}$, and both of them are totally disconnected. In fact, all open balls are actually clopen! This is nothing like $\mathbb{Z} \subseteq \mathbb{R}$ where $\mathbb{Z}$ is non-compact and closed and $\mathbb{R}$ has lots of connected sets.

##### _lemma:_ open balls are clopen

For any $x \in \mathbb{Q}_{p}$, the open ball of radius $r$, centred at $x$
$$
B(x, r) = \{ y \in \mathbb{Q}_{p} \mid \lvert y - x \rvert _{p} < r \}
$$
is also closed.

###### _proof:_

Note of course that by the definition of a metric topology, this ball is open. We just need to show it is closed. We will show (equivalently) that [[Topology --- math-147/notes/Limit points and closed sets#_theorem _ closed sets are complements of open sets|its complement is open]]. 

[[Topology --- math-147/notes/Topologies#_proposition, definition _ checking openness by neighbourhood, neighbourhood|It suffices]] to give a disjoint ball $B(y, \rho) \subseteq \mathbb{Q}_{p} \setminus B(x, r)$ for each point $y$ in the complement of $B(x, r)$. Consider for each $y \in \mathbb{Q}_{p} \setminus B(x,r )$ the points $z \in \mathbb{Q}_{p}$ with $\lvert z - y \rvert_{p} < \lvert x - y \rvert_{p}$. Since $\lvert z - x \rvert_{p} = \lvert (z - y) - (y - x) \rvert_{p} > \lvert x - y \rvert_{p}$, we have $\lvert z - x \rvert_{p} > \lvert x - y \rvert_{p} \geq r$. Thus, choosing any $\rho < \lvert x - y \rvert_{p}$ gives $B(y, \rho) \subseteq \mathbb{Q}_{p} \setminus B(x, r)$.

##### _proposition:_ the $p$-adics are totally disconnected

$\mathbb{Z}_{p}$ and $\mathbb{Q}_{p}$ are totally disconnected — there are no connected subsets of either that are not singletons or the empty set.

###### _proof:_

Suppose $A \subseteq \mathbb{Q}_{p}$ has cardinality $\# A \geq 2$. Let $x, y \in A$ be distinct points. [[Topology --- math-147/notes/Connectedness and path-connectedness#_proposition _ conditions equivalent to connectedness|It suffices]] to show that $A$ has a non-trivial ([[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|relatively]]) clopen subset. For any $r < \lvert x - y \rvert_{p}$, the set $A \cap B(x, r)$ is an example.

##### _proposition:_ topological properties of $\mathbb{Z}_{p}$ in $\mathbb{Q}_{p}$

$\mathbb{Z}_{p} \subseteq \mathbb{Q}_{p}$ is an open compact subset.

###### _proof:_

First we show $\mathbb{Z}_{p}$ is open. Again, it suffices to show each integer is the centre of a metric ball contained in $\mathbb{Z}_{p}$. We claim this is the metric ball of radius $1$.

Recall the characterisation of $x \in \mathbb{Z}_{p}$ as exactly those $x \in \mathbb{Q}_{p}$ with $\lvert x \rvert_{p} \leq 1$. For each $x \in \mathbb{Z}_{p}$ consider the metric ball $B(x, 1)$. If $y \in B(x, 1)$, then $\lvert y - x \rvert_{p} < 1$. Thus,
$$
\lvert y \rvert _p = \lvert (y - x) + x \rvert_{p} \leq \max \{ \lvert y - x \rvert_{p}, \lvert x \rvert_{p}  \} \leq 1
$$
and $y \in \mathbb{Z}_{p}$.

We show compactness as sequential compactness — that every infinite subset has a limit point (or every sequence has a [[Analysis --- math-131/notes/Sequences and convergence#_theorem, definition _ subsequential limits|subsequential limit]]), [[Analysis --- math-131/attachments/homework/hw 5/hw 5.pdf|implying compactness]]. 

Write $\{ x_{n} \}_{n \in \mathbb{N}}$ for some arbitrary sequence of $x_{n} \in \mathbb{Z}_{p}$. Note that for each exponent $e$, the set of possible residue classes modulo each $p^i$ for $i$ at most $e$ is finite. As a result, there is a $p$-adic integer $u$, given by residue sequence $(u_{i})_{i \in \mathbb{N}}$, with infinitely many $x_{n}$ agreeing under each $\mathbb{Z}_{p} \twoheadrightarrow{} \mathbb{Z} / p^e / \mathbb{Z}$. Choose a subsequence $\{ x_{n_{k}} \}_{k \in \mathbb{N}}$ with $x_{n_{k}}$ agreeing with $u$ under $\mathbb{Z}_{p} \twoheadrightarrow{} \mathbb{Z} / p^k \mathbb{Z}$. Thus, $\lvert x_{n_{k}} - u \rvert_{p} \leq p^{-k} \to 0$ as $k \to \infty$. That is, $x_{n_{k}} \to u$. 