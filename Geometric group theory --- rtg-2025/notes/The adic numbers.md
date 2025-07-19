---
tags:
- alg-nt
- rtg-2025
- napkin
---

The $p$-adics generalise two notions that we know, each in the direction of the other.

To solve a Diophantine equation, it's often useful to consider its behaviour modulo a prime $p$ (especially to disprove the existence of integer solutions). This isn't fool-proof because the canonical surjection $\mathbb{Z} \to \mathbb{Z} / p \mathbb{Z}$ loses a lot of information (it is far from injective). We have to consider all prime powers at once, but $\mathbb{Z} / p^e \mathbb{Z}$ is not algebraically nice in general.

To approximate a sum in the Euclidean norm on $\mathbb{Q}$ (say we want to approximate $\sum_{n = 1}^N 1 / n^{2}$ within some $\varepsilon > 0$) we use the convergence of the sum in $\mathbb{R}$ (here to $\pi^{2} / 6$) and then bound the error term. However, this doesn't work when the "error" we want to discard is number-theoretic — we can't get equality modulo some $p^e$ by doing analysis on $\mathbb{R}$.

The field of $p$-adic numbers $\mathbb{Q}_{p}$ generalises $\mathbb{Z} / p^e \mathbb{Z}$ by containing the "limit" or "completion" of all of them in the $p$-adic integers $\mathbb{Z}_{p}$. However, $\mathbb{Q}_{p}$ is a field like $\mathbb{R}$. It also generalises $\mathbb{R}$ as the [[Mathematical Analysis I --- math-131/notes/Cauchy sequences#_definition _ completeness|metric completion]] of $\mathbb{Q}$ with respect to a different metric (the $p$-adic valuation). This is more like $\mathbb{Z} / p^e \mathbb{Z}$ because the metric throws away information in a modulo $p^e$ sense by making high powers of $p$ small.

With these two simultaneous generalisations we will be able to solve problems like the one below.

##### _problem:_ approximating a sum, modulo $p^3$ (USA TST 2002/2)

For prime $p$, show that the value of
$$
f_{p}(x) = \sum_{k = 1}^{p - 1} \frac{1}{(px + k)^{2}} \pmod{p^{3}}
$$
does not depend on $x$.

### $p$-adics are algebraic completions

A $p$-adic integer generalises integers. Where integers have and are determined by an eventually constant sequence of residues modulo each $p^e$, a $p$-adic integer has and is determined by a sequence of residues modulo each $p^e$ that satisfies a compatibility relation — the residues modulo high powers agree with the residues modulo low powers, in the ring modulo low powers.

##### _definition:_ the $p$-adic integers, $\mathbb{Z}_{p}$

The $p$-adic integers are the ring $\mathbb{Z}_{p}$ comprising all sequences $x = x_{1}, \dots, x_{e}, \dots$ of residues modulo $p^e$, satisfying $x_{i} \equiv x_{j} \pmod{p^i}$ for $i < j$. The ring addition and multiplication are component-wise.

Note that the additive and multiplicative identities have residue sequences $(0, 0, \dots)$ and $(1, 1, \dots )$ respectively.

In fact, this is just a categorical definition as a [[Categorical limits|limit]]. The $p$-adic numbers are the limit of the chain of maps $\mathbb{Z} / (p^j) \to \mathbb{Z} / (p^i)$ where $j > i$.

##### _proposition:_ the $p$-adic integers are an algebraic completion

$\mathbb{Z}_{p}$ and its natural maps to each $\mathbb{Z} / (p^e)$ satisfy the universal property that for any ring $A$ with maps $A \to \mathbb{Z} / (p^e)$ that commute with $\mathbb{Z} / p^j \to \mathbb{Z} / p^i$ for exponents $j > i \in \mathbb{N}$. 

That is, the following diagram of rings commutes for each $j > i$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		A \ar[rdd] \ar[rrdd, bend left] \ar[rd, dashed, "\exists !"] \\
		& \mathbb{Z}_{p} \ar[d] \ar[rd] \\
		& \mathbb{Z} / (p^i) & \mathbb{Z} / (p^j) \ar[l, two heads]
	\end{tikzcd}
\end{document}
```

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

So far, the construction we have works for non-prime base as well. Indeed, there are $n$-adic "integers" for each $n > 1$. However, they differ in their units. In particular, the $n$-adic integers are not, integral domains unless $n$ is a prime.

##### _proposition:_ $\mathbb{Z}_{p}$ is an [[Abstract Algebra I --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]]

###### _proof:_

Note that $0 \in \mathbb{Z}_{p}$ has residue sequence $(0, 0, \dots)$. If $x = (x_{i})_{i \in \mathbb{N}}, y = (y_{i})_{i \in \mathbb{N}}$ have $xy = 0$, then for each $i \in \mathbb{N}$ we have $x_{i} y_{i} \equiv 0 \pmod {p^i}$. Let $j$ be the minimal natural number such that $x_{j} \neq 0$ and similarly let $k$ be the minimal natural number such that $y_{k} \neq 0$. Since, for each $i \in \mathbb{N}$ we have $p^i \mid x_{i} y_{i}$ and we also have $p^j \mid x_{i}$ and $p^k \mid y_{i}$, we must have $j + k \geq i$. This forces $\max{j, k} \geq i / 2$. Finally, this forces $\max{j, k}$ greater than all natural numbers, and thus, one of $x$ and $y$ must have all residues equal to $0$.

In fact, we can characterise all units in $\mathbb{Z}_{p}$. Just as in $\mathbb{F}[[x]]$ where the units are those not in $(x)$, in $\mathbb{Z}_{p}$ the units are those with non-zero value modulo $p$.

##### _proposition:_ units in $\mathbb{Z}_{p}$

$x = (x_{j})_{j \in \mathbb{N}} \in \mathbb{Z}_{p}$ is a [[Abstract Algebra I --- math-171/notes/Rings#_definition _ unit|unit]] if and only if $x_{1} \not \equiv 0 \pmod p$.

###### _proof:_

If $x_{1} \equiv 0$, then the product of $x$ with any $y$ will have residue $0$ modulo $p$, and is thus, not $1$.

If $x_{1} \not \equiv 0$, then there is some $y_{1} \in \mathbb{Z} / p \mathbb{Z}$ such that $x_{1} y_{1} \equiv 1$ (since $\mathbb{Z} / p \mathbb{Z}$ [[Superdiscrete --- math-55a/notes/Modular arithmetic#_corollary _ Wilson's theorem|is a field]]). Also, each $x_{i} \equiv x_{1} \not \equiv 0$ modulo $p$, so $(x_{i}, p^i) = 1$, and $x_{i}$ has an inverse $y_{i}$ as well. These $y_{i}$ are compatible since they are all have the same 

Since $\mathbb{Z}_{p}$ is an integral domain, it has a well-defined fraction field. Just as $Q(\mathbb{Z}) = \mathbb{Q}$, we define the $p$-adic numbers as the fraction field of $\mathbb{Z}_{p}$. 

##### _definition:_ the $p$-adic numbers, $\mathbb{Q}_{p}$

The $p$-adic numbers $\mathbb{Q}_{p}$ are the [[Algebraic geometry --- rising-sea/notes/Localisation, categorically#_definition _ localisation of a ring, localisations at a prime, fraction field|fraction field]] $Q(\mathbb{Z}_{p})$ of the $p$-adic integers.

However, just as we don't typically think of [[Complex Analysis --- math-135/notes/Laurent series|Laurent series]] $\mathbb{F}((x))$ as ratios of formal power series in $\mathbb{F}[[x]]$, we don't want to do so for $\mathbb{Q}_{p}$ either. We can instead give a formal Laurent series expansion of elements of $\mathbb{Q}_{p}$.

##### _proposition:_ $\mathbb{Q}_{p}$ looks like formal Laurent series

Every non-zero element of $\mathbb{Q}_{p}$ can be uniquely written $x / p^k$ for some $x \in \mathbb{Z}_{p}$ and some integer $k \in \mathbb{Z}$.

###### _proof:_

It suffices to show $1 / y \in \mathbb{Q}_{p}$ for $y \in \mathbb{Z}_{p}$ is $x / p^k$. 

Write $y = \sum_{n \geq m} a_{n} p^n$ so that $a_{m} \not \equiv 0$. Then $y = a_{m} p^m \sum_{n = 0}^\infty a_{m + n} p^n / a_{m} = a_{m} p^m z$. Since the first term of the series $z$ is $a_{m} / a_{m} = 1$, $z$ has an inverse in $\mathbb{Z}_{p}$. Also, $a_{m}$ has an inverse in $\mathbb{Z}_{p}$ since $a_{m} \not \equiv 0$. Thus, we can write
$$
\frac{1}{y} = \frac{z^{-1} a_{m}^{-1}}{p^k}
$$
for $k = m$

### $p$-adics are analytic completions

We can also obtain the $p$-adic numbers in an analytically, by making large $p^e$ very small. 

##### _definition:_ $p$-adic valuation, absolute value

The $p$-adic valuation $\nu_{p} : \mathbb{Q}_{p}^\times \to \mathbb{Z}$ is given by the largest $\nu_{p}(x) = k$ for the unique product $x = p^k z$ with $z \in \mathbb{Z}_{p}$.

The $p$-adic absolute value is given by $\lvert x \rvert_{p} = p^{- \nu_{p}(x)}$.

While here we defined the valuation and absolute value in their full generality on $\mathbb{Q}_{p}$, they are still natural, even on $\mathbb{Q}$ — they are just the natural absolute value if you value information modulo $p^e$. Further, it is Ostrowski's theorem that the only absolute values on $\mathbb{Q}$ (up to scaling) are the trivial norm, the Euclidean norm, and the $p$-adic norms (for each prime $p$).