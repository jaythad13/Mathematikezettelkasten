---
tags:
- math-177/2
- math-177/3
- alg-nt
- metric
---

Ostrowski's theorem classifies norms on $\mathbb{Q}$ up to equivalence. It says that there are only three types — the trivial, $p$-adic, and Euclidean metrics. To state it specifically, we need to define the notion of equivalence.

##### _definition:_ equivalence of norms

Two [[Norms|norms]] on $\mathbb{Q}$ are equivalent if a sequence is [[Analysis --- math-131/notes/Cauchy sequences#_definition _ Cauchy sequence|Cauchy]] with respect to one if and only if it is Cauchy with respect to the other.

Note that this equivalence relation preserves convergence in [[Analysis --- math-131/notes/Cauchy sequences#_definition _ completeness|complete spaces]] as well. If $x_{n} \to x$ in one norm, then $\{ x_{n} \}_{n \in \mathbb{N}}$ is Cauchy in that norm, and thus, in the other, and thus, convergent in the other as well.

From the multiplicativity of the norm, some useful properties follow — $\lVert 1 \rVert = \lVert -1 \rVert = 1$ and more generally, $\lVert a^{-1} \rVert = \lVert a \rVert^{-1}$.

##### _theorem:_ Ostrowski's theorem

If $q \mapsto \lVert q \rVert$ is a norm on $\mathbb{Q}$, then it is equivalent to the trivial norm (by $0 \mapsto 0$ and $q \mapsto 1$), the $p$-[[p-adic numbers --- math-177/notes/The p-adic numbers#_definition _ $p$-adic valuation, absolute value|adic absolute value]] or the Euclidean metric.

###### _proof:_

We show that the norm is either $\lvert q \rvert^\alpha$ or $\lvert q \rvert_{p}^\alpha$ for some $\alpha > 0$ and some prime $p$. Note also that we only need to show agreement of the norms on $\mathbb{Z}$, and in fact, only on $\mathbb{N}$.

Suppose there exists some $n \in \mathbb{N}$ with $\lVert n \rVert > 1$. Let $n_{0}$ be the minimal positive integer with $\lVert n_{0} \rVert > 1$. Then choose $\alpha$ so that $\lVert n_{0} \rVert = \lvert n_{0} \rvert^\alpha$. That is, choose $\alpha = \ln \lVert n_{0} \rVert / \ln n_{0}$. Then for any $n \in \mathbb{N}$ written in base $n_{0}$ as $n = c_{0} + c_{1} n_{0} + c_{2} n_{0} + \dots + c_{k} n_{0}^k$ with $c_{i} \in [0, n_{0} - 1] \cap \mathbb{Z}$. Note that $n_{0}^k \leq n < n_{0}^{k + 1}$. Thus,
$$
\begin{align}
\lVert n \rVert & = \left\lVert c_{0} + c_{1} n_{0} + \dots + c_{k} n_{0}^k  \right\rVert    \\
 & \leq \lVert c_{0} \rVert + \lVert c_{1} \rVert \lVert n_{0} \rVert + \dots + \lVert c_{k} \rVert \lVert n_{0} \rVert^k.
\end{align}
$$
Since $c_{i} < n_{0}$, we must have $\lVert c_{i} \rVert \leq 1$. Thus,
$$
\begin{align}
\lVert n \rVert & \leq 1 + \lVert n_{0} \rVert + \dots + \lVert n_{0} \rVert ^k \\
 & = 1 + n_{0}^{\alpha} + \dots + n_{0}^{k \alpha} \\
 & = n_{0}^{k \alpha} \left( 1 + \frac{1}{n_{0}^{\alpha}} + \dots + \frac{1}{n_{0}^{k \alpha}} \right) \\
 & \leq (n_{0}^{k})^\alpha \sum_{i = 0}^{\infty} \frac{1}{(n_{0}^\alpha)^i} \\
 & = C n^\alpha.
\end{align}
$$
where the geometric series $C$ is a constant that only depends on $n_{0}$, not on $n$. Replacing $n$ with $n^N$ we get $\lVert n^N \rVert = \lVert n \rVert^N \le n^{N \alpha} C$ and thus, $\lVert n \rVert \leq n^\alpha C^{1 / N}$. Since this is true for all $N$, it must be true that $\lVert n \rVert \le n^\alpha$.
