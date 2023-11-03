---
tags:
- math-55a
- comb
lecture:
- math-55a-1
- math-55a-2
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

We can see some more interesting patterns if we look at Pascal's triangle as a right triangle with rows $\binom{n}{k}$ for all $0 \le k \le n$.

##### _example:_ the hockey stick identity

%% compute an explicit example %%

##### _proposition:_ the hockey stick identity

$$
\sum_{n = k}^N \binom{n}{k} = \binom{N + 1}{k + 1}
$$
##### _proof:_

We can have a combinatorial proof. There are $\binom{N + 1}{k + 1}$ ways to choose a team of $k + 1$ players from among $N + 1$ players.

But we can think of lining up all the potential players and assigning them numbers $1, \ldots, N + 1$. Then the number of squads with the largest jersey number $n + 1$ is $\binom{n}{k}$. Sum up all of these $\binom{n}{k}$ and you get all of the possible teams.

##### _proposition:_ the Fibonacci series in Pascal's triangle

$$
\sum_{k = 0}^{k \le n/2} \binom{n - k}{k} = f_n 
$$

##### _proof sketch:_

We have a combinatorial proof of this as well!

We know that $f_n$ is the number of tilings of an $n$-strip with dominoes and squares.

It's natural to want to think of $k$ as the number of dominoes since it is at least $0$ and at most $\le n/2$. If we tile an $n$-strip with $k$ dominoes, then there are $n - 2k$ remaining slots for squares, and thus, $n - 2k$ squares. This gives us $n - 2k + k = n - k$ tiles in total. Then the number of tilings with $k$ dominoes is just given by $\binom{n - k}{k}$.

The sum of the number of tilings with $k$ dominoes for all possible $k$ is obviously the total number of tilings.

##### _proposition:_ half sums of rows of Pascal's triangle


##### _proof:_



