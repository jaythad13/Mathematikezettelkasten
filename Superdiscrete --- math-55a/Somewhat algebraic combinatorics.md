---
tags: 
- alg-comb
- comb
lecture: math-55a-2
---

### The binomial theorem

##### _theorem:_ the binomial theorem

$$
(x + y)^n = \sum_{k = 0}^n \binom{n}{k}x^k y^{n - k}
$$

We can prove this in many different ways!
##### _proof sketch 1:_

Induct

##### _proof sketch 2:_

For $(x + y)^n$ we expect to have $x^k y^{n - k}$ for each $0 \le k \le n$. How many ways are there to do this?

We have to choose $k$ $x$s from among $n$ $x$s and then the $n - k$ $y$s are chosen for us. That is, there are $\binom{n}{k}$ ways to do it!

##### _proof sketch 3:_

##### _corollary_: %% give name %%

$$
2^n = \sum_{k = 0}^n \binom{n}{k}
$$

##### _proof:_

Just substitute $1$ for both $x$ and $y$.

##### _corollary:_

$$
\sum_{k \text{ is even}}^{k \le n} \binom{n}{k} = \sum_{k \text{ is odd}}^{k \le n} \binom{n}{k} = 2^{n - 1}
$$

##### _proof:_

Rewrite this as 
$$
\sum_{k = 0}^n \binom{n}{k}(-1)^k = (1 - 1)^n = 0
$$
for $n$
