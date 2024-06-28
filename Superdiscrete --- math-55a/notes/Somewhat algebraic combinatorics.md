---
tags: 
- alg-comb
- comb
- math-55A/2
---

### The binomial theorem

##### _theorem:_ the binomial theorem

$$
(x + y)^n = \sum_{k = 0}^n \binom{n}{k}x^k y^{n - k}
$$

We can prove this in many different ways!

###### _proof sketch 1:_

Induct. (This isn't a very good way to do it).

###### _proof sketch 2:_

For $(x + y)^n$ we expect to have $x^k y^{n - k}$ for each $0 \le k \le n$. How many ways are there to do this?

We have to choose $k$ $x$s from among $n$ $x$s and then the $n - k$ $y$s are chosen for us. That is, there are $\binom{n}{k}$ ways to do it!

###### _proof sketch 3:_

This proof is combinatorial. 

How many ways are there to distribute $n$ distinct candy bars among $x$ children and $y$ adults?

There are $(x + y)^n$ ways, because we can make $x + y$ different choices for each of the $n$ candy bars.

We could also get the number of ways by adding up the number of ways for the children to get $k$ candy bars for each $k \le n$. First we choose the $k$ candy bars that we're giving the children (and as a result, we have the $n - k$ that we're giving the adults). There are $\binom{n}{k}$ ways to do this. Then for each of the $k$ candies for the children, we have $x$ choices, and for each of the $n - k$ candies for the adults we have $y$ choices. That is, for each $k$, there are $\binom{n}{k} x^k y^{n - k}$, and then the total number of ways to distribute the candies is
$$
\sum_{k = 0}^n \binom{n}{k} x^k y^{n - k}.
$$
Since this counts the same thing as our first answer, we get
$$
(x + y)^n = \sum_{k = 0}^n \binom{n}{k} x^k y^{n - k}
$$
as desired.

### How it makes things easy

We get a new and easy proofs for old results as corollaries of the binomial theorem!

##### _corollary_: [[Superdiscrete --- math-55A/notes/Pascal's triangle#_proposition _ binomial coefficients count subsets|binomial coefficients count subsets]] 

$$
2^n = \sum_{k = 0}^n \binom{n}{k}
$$

###### _proof:_

Just substitute $1$ for both $x$ and $y$.

##### _corollary:_ sums of binomial coefficients with even $k$ [[Superdiscrete --- math-55A/notes/Pascal's triangle#_proposition _ sums of binomial coefficients with even $k$ are half the sum for all $k$|are half the total sum]]

$$
\sum_{k \text{ is even}}^{k \le n} \binom{n}{k} = \sum_{k \text{ is odd}}^{k \le n} \binom{n}{k} = 2^{n - 1}
$$

###### _proof:_

Rewrite
$$
\sum_{k \text{ is even}}^{k \le n} \binom{n}{k} - \sum_{k \text{ is odd}}^{k \le n}
$$
as 
$$
\sum_{k = 0}^n \binom{n}{k}(-1)^k = (1 - 1)^n = 0
$$
for $n$.

Then
$$
\sum_{k \text{ is even}}^{k \le n} \binom{n}{k} = \sum_{k \text{ is odd}}^{k \le n} \binom{n}{k}
$$
and since
$$
\sum_{k \text{ is even}}^{k \le n} \binom{n}{k} + \sum_{k \text{ is odd}}^{k \le n} \binom{n}{k} = \sum_{k = 0}^n \binom{n}{k} = 2^n
$$
we have
$$
\sum_{k \text{ is even}}^{k \le n} \binom{n}{k} = \sum_{k \text{ is odd}}^{k \le n} \binom{n}{k} = 2^{n - 1}
$$
as desired.

And if we aren't afraid to use a little calculus, this gets even more powerful!

##### _corollary:_ the sum of scaled binomial coefficients

For $n \in \bb N$,
$$
\sum_{k = 0}^n k \binom{n}{k} = n 2^{n - 1}.
$$

###### _proof:_

The binomial theorem tells us that $(1 + x)^n = \sum_{k = 0}^n \binom{n}{k} x^k$. Differentiating both sides gives us
$$
n(1 + x)^{n - 1} = \sum_{k = 0}^n k \binom{n}{k} x^{k - 1}
$$
which on plugging in $x = 1$, gives us the desired result.

Similar results come from looking at binomial coefficients scaled by $k^2$ and the "twice-differentiated binomial theorem" and so on.