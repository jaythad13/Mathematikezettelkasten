---
tags:
- math-55a
- comb
---

We can use the [[Basic combinatorics#_definition _ $ binom{n}{k}$|binomial coefficients]] in interesting ways. Specifically, arranging the binomial coefficients in a triangle shows us some interesting properties.

##### _definition:_ Pascal's triangle

Pascal's triangle is the two dimensional sequence of $\binom{n}{k}$ arranged in a triangle as

Looking at the triangle suggests several interesting identities.

Each $n$th row appears to sum to $2^n$. We can give a combinatorial proof of the proposition by asking the question: "what does each side represent?"

##### _proposition:_ binomial coefficients count subsets

$$
\sum_{k \ge 0} = 2^n
$$
##### _proof sketch:_

Each $\binom{n}{k}$ is the number of subsets with $k$ elements of a set with $n$ elements. Thus, the sum of the binomial coefficients is the total number of subsets of a set of size $n$. But since whenever we construct a subset we have $n$ binary choices - whether to include each element or not. That is, there are $2^n$ subsets of a set of size $n$.

We can also see that it looks like each part of the triangle (except the sides which are all 1) is the sum of the two elements above it. This suggests the following identity.

##### _theorem:_ Pascal's identity

For $0 \le k \le n$
$$
\binom{n}{k} = \binom{n - 1}{k - 1} + \binom{n - 1}{k}.
$$

##### _proof sketch:_

For a set of size $n$, consider splitting the set of all subsets into two: all of the subsets that contain the $n$th element, and all that don't. 

There are $\binom{n -1}{k}$ ways to choose a set of $k$ elements that doesn't contain the $n$th element. 

For the sets that do contain the $n$th element, we have to pick $k - 1$ other elements from among the other $n - 1$ elements. Thus, there are $\binom{n - 1}{k - 1}$ subsets that do contain the $n$th element.