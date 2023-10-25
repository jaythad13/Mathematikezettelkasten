---
tags:
- math-55a
- comb
---

### Basic combinatorial theorems by induction

We can use the [[Peano axioms|axiom of induction]] to prove various combinatorial theorems.

##### _example:_ the sum of the first $n$ natural numbers

We can prove that $1 + 2 + \ldots + n = \frac{n(n + 1)}{2}$ using the Gauss trick, but it's messy. Induction is more work but less messy.
We know that
$$
\sum_{k = 1}^1 k = 1 = \frac{1 (1 + 1)}{2} = 1.
$$
Suppose
$$
\sum_{k = 1}^n k = \frac{n(n + 1)}{2}
$$
for some $n \in \bb{N}$.

Then
$$
\sum_{k = 1}^{n + 1} k = \frac{n (n + 1)}{2} + n + 1 = \frac{(n(n + 1) + 2 (n + 1))}{2} = \frac{(n + 1)((n + 1) + 1)}{2}.
$$

Thus, $\sum_{k = 1}^n k = \frac{n(n + 1)}{2}$ for all $n \in \bb{N}$.

An even cleverer proof doesn't rely on words!

The sum of the first $n$ natural numbers is also the $n$th triangular number. Draw the $n$th triangular number in a triangle. Draw an additional row of $n + 1$ numbers below the triangle. 

Then each of the numbers in the original triangle determines a unique pair of the row below (by drawing lines to the bottom row). Thus, the $n$th triangular number is just $\binom{n + 1}{2}$

##### _definition:_ Fibonacci numbers

The Fibonacci numbers are the sequence defined by the [[Recurrence problems#_definition _ recurrence relation|recurrence relation]]
$$
\begin{gathered}
	F_0 = 0 \\
	F_1 = 1 \\
	F_n = F_{n - 1} + F_{n - 2}.
\end{gathered}
$$

Note that summing the Fibonacci numbers seems to give an interesting property.

##### _proposition:_ the sum of Fibonacci numbers is almost a Fibonacci number

For $n \ge 0$,
$$
\sum_{k = 0}^n F_k = F_{n + 2} - 1.
$$

##### _proof:_

By induction. %% do later %%
$$

$$

##### _theorem:_ Binet's formula

For $n \ge 0$
$$
F_n = \frac{1}{\sqrt{5}} \Big(\Big(\frac{1 + \sqrt{5}}{2}\Big)^n - \Big(\frac{1 - \sqrt{5}}{2}\Big)^n\Big).
$$
##### _proof:_

See linear algebra or generatingfunctionology for other approaches.

Note that
$$
F_0 = 0 = \frac{1}{\sqrt{5}} (\varphi^0 - \bar{\varphi}^0)
$$
and
$$
F_1 = 1 = \frac{\sqrt{5}}{\sqrt{5}} = \frac{1}{\sqrt{5}}(\varphi - \bar{\varphi}).
$$
Suppose Binet's formula holds for $n$ and $n - 1$. Then
$$
F_n = F_{n - 1} + F_{n - 2} = \frac{1}{\sqrt{5}} ( \varphi^n - \bar \varphi ^n + \varphi^{n - 1} - \bar \varphi^{n - 1}) = \frac{1}{\sqrt 5} (\varphi^{n - 1} (\varphi + 1) - \bar \varphi^{n - 1}(\bar \varphi + 1))
$$
but we know $\varphi^2 = \varphi + 1$ and $\bar \varphi^2 = \bar \varphi + 1$. Substituting gives us

$F_{n + 1}$

##### _definition:_ the golden ratio 

We write the golden ratio as
$$
\varphi = \frac{1 + \sqrt{5}}{2}.
$$
We write its conjugate as
$$
\bar{\varphi} = \frac{1 - \sqrt{5}}{2}.
$$
Induction isn't just for identities!

##### _theorem:_ you can cover almost all of a chessboard with trominoes

Given a $2^n \times 2^n$ ($n \in \bb{N}$) chessboard with one piece removed, you can cover the board using trominoes.

##### _proof sketch:_

It's possible for $n = 1$ obviously.

If it's true for $n$, break the chessboard into four quadrants. One of them has a removed piece. Cover that quadrant in trominoes.

For the rest, place a tromino such that it has one part in each of the remaining quadrants. Then cover them.

### Strong induction

Strong induction extends induction by allowing you to assume all previous cases.

##### _theorem:_ Zeckendorf's theorem

For any $n \in N$, we can write $n = \sum_{\alpha \in A} F_\alpha$ for some finite $A \subset \bb{N}$. Note that this means we can't use any number twice, including that we can't use $1$ twice.

##### _proof sketch:_

The greedy algorithm where you take the largest Fibonacci less than the number you want to sum up to works. We can prove this by strong induction.

This works for $n = 1$, obviously.

Suppose this works for all numbers less than $n + 1$. If $n + 1$ is a Fibonacci number, we are done. If it is not, it lies between two Fibonacci numbers. Choose the greatest Fibonacci number less than it, $F_j$. $n + 1 - F_j$ is the sum of distinct Fibonacci numbers. Note that we can also bound it.
$$
n + 1 - F_j < F_{j + 1} - F_j = F_{j - i} \le F_j.
$$
Thus, $n + 1 - F_j < F_j$ meaning that its expression as the sum of distinct Fibonacci numbers cannot include $F_j$. Thus
$$
n + 1 = F_j + (n + 1 - F_j)
$$
is the sum of distinct Fibonacci numbers.

%% complete the $f_n$ stuff
