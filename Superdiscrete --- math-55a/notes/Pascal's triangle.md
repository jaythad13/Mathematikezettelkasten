---
tags:
- math-55A/1
- math-55A/2
- comb
---

We can use the [[Superdiscrete --- math-55A/notes/Basic combinatorics#_definition _ $ binom{n}{k}$|binomial coefficients]] in interesting ways. Specifically, arranging the binomial coefficients in a triangle shows us some interesting properties.

##### _definition:_ Pascal's triangle

Pascal's triangle is the two dimensional sequence of $\binom{n}{k}$ arranged in a triangle as
![[Superdiscrete --- math-55A/attachments/for notes/Pascal's triangle/S0_Pascal'sTriangle.jpeg]]
and so on.

Looking at the triangle suggests several interesting identities.

Each $n$th row appears to sum to $2^n$. We can give a combinatorial proof of the proposition by asking the question: "what does each side represent?"

##### _proposition:_ binomial coefficients count subsets

$$
\sum_{k \ge 0} = 2^n
$$
###### _proof sketch:_

Each $\binom{n}{k}$ is the number of subsets with $k$ elements of a set with $n$ elements. Thus, the sum of the binomial coefficients is the total number of subsets of a set of size $n$. But since whenever we construct a subset we have $n$ binary choices - whether to include each element or not. That is, there are $2^n$ subsets of a set of size $n$.

We can also see that it looks like each part of the triangle (except the sides which are all 1) is the sum of the two elements above it. This suggests the following identity.

##### _theorem:_ Pascal's identity

For $0 \le k \le n$
$$
\binom{n}{k} = \binom{n - 1}{k - 1} + \binom{n - 1}{k}.
$$

###### _proof sketch:_

For a set of size $n$, consider splitting the set of all subsets into two: all of the subsets that contain the $n$th element, and all that don't. 

There are $\binom{n -1}{k}$ ways to choose a set of $k$ elements that doesn't contain the $n$th element. 

For the sets that do contain the $n$th element, we have to pick $k - 1$ other elements from among the other $n - 1$ elements. Thus, there are $\binom{n - 1}{k - 1}$ subsets that do contain the $n$th element.

We can see some more interesting patterns if we look at Pascal's triangle as a right triangle with rows $\binom{n}{k}$ for all $0 \le k \le n$.

![[Superdiscrete --- math-55A/attachments/for notes/Pascal's triangle/S0_Pascal'sRightTriangle.jpeg]]

##### _example:_ the hockey stick identity

For example, looking at Pascal's triangle as a right triangle suggests that adding finitely many elements down a column is the same as just looking at the element in the column to the right in the row just below - it looks like a hockey stick.

For example
$$
\binom{2}{2} + \binom{3}{2} + \binom{4}{2} + \binom{5}{2} = 1 + 3 + 6 = 10 = 20
$$
and
$$
\binom{6}{3} = 20.
$$
![[Superdiscrete --- math-55A/attachments/for notes/Pascal's triangle/S0_hockeyStick.jpeg]]

We can prove that this holds in general.

##### _proposition:_ the hockey stick identity

$$
\sum_{n = k}^N \binom{n}{k} = \binom{N + 1}{k + 1}
$$
###### _proof:_

We can have a combinatorial proof. There are $\binom{N + 1}{k + 1}$ ways to choose a team of $k + 1$ hockey players from among a pool of $N + 1$ hockey players.

But we can think of lining up all the potential players and assigning them numbers $1, \ldots, N + 1$. Then the number of squads with the largest jersey number $n + 1$ is $\binom{n}{k}$. Sum up all of these $\binom{n}{k}$ and you get all of the possible teams.

We can also look at summing along (non-principal) diagonals. Again, computing a few examples reveals a pattern. This time it's the Fibonacci numbers, and we can show that this pattern always holds.

![[Superdiscrete --- math-55A/attachments/for notes/Pascal's triangle/S0_diagonalSumsToFibonacci.jpeg]]

##### _proposition:_ the Fibonacci series in Pascal's triangle

$$
\sum_{k = 0}^{k \le n/2} \binom{n - k}{k} = f_n 
$$

###### _proof sketch:_

We have a combinatorial proof of this as well!

We know that $f_n$ is the [[Superdiscrete --- math-55A/notes/Proof by induction#_definition _ Fibonacci tiling numbers|number of tilings]] of an $n$-strip with dominoes and squares.

It's natural to want to think of $k$ as the number of dominoes since it is at least $0$ and at most $\le n/2$. If we tile an $n$-strip with $k$ dominoes, then there are $n - 2k$ remaining slots for squares, and thus, $n - 2k$ squares. This gives us $n - 2k + k = n - k$ tiles (dominoes or squares) in total. Then the number of tilings with $k$ dominoes is just given by $\binom{n - k}{k}$.

The sum of the number of tilings with $k$ dominoes for all possible $k$ is obviously the total number of tilings.

##### _proposition:_ sums of binomial coefficients with even $k$ are half the sum for all $k$

For $n \in \bb{N}$, the sum of all $\binom{n}{k}$ for even $k$ is half the sum of all $\binom{n}{k}$. That is,
$$
\sum_{k \text{ is even}}^{k \le n} \binom{n}{k} = 2^{n - 1}
$$
###### _proof:_

We have a combinatorial proof!

Consider the number of even-numbered committees that can be formed from a group of $n$ people. That is just the sum of all even $k$ binomial coefficients.

However, we can get the same thing another way - freely choose whether to include the first $n-1$ members of the group in the committee, and then choose whether to include the $n$th member based on parity. There are $2^{n - 1}$ ways to do this, and this gives us exactly the even-membered committees.