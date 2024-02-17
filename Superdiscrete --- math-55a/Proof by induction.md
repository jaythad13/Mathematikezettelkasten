---
tags:
- math-55a
- comb
lecture: math-55a-1
---

### Basic combinatorics by induction

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

![[S1_triangleBijection.jpeg]]

We can see that there is a bijection between the triangular lattice of $n$ rows and pairs of points in the $n + 1$th row, given by picture above. That is, for any pair, draw a line parallel to the left side of the triangle from the left point of the pair and draw a line parallel to the right side of the triangle from the right point of the pair. They define a unique point in the triangular lattice above them.

Thus, there is a bijection between a set of cardinality $T_n$ and a set of cardinality $\binom{n + 1}{2}$. Thus,
$$
T_n = \binom{n + 1}{2}.
$$

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

Note that $\sum_{k = 0}^1 F_k = F_0 + F_1 = 1 = 2 - 1 = F_3 - 1$. That is, we have the base case.

If for some $n \in \bb{N}$, $\sum_{k = 0}^n F_k = F_{n + 2} - 1$, then $\sum_{k = 0}^{n + 1} F_k = F_{n + 1} + F_{n + 2} - 1 = F_{(n + 1) + 2} - 1$.

Thus, by induction
$$
\sum_{k = 0}^n F_k = F_{n + 2} - 1.
$$
for all $n \in \bb{N}$.
##### _theorem:_ Binet's formula

For $n \ge 0$
$$
F_n = \frac{1}{\sqrt{5}} \Big(\Big(\frac{1 + \sqrt{5}}{2}\Big)^n - \Big(\frac{1 - \sqrt{5}}{2}\Big)^n\Big).
$$
##### _proof:_

See [[Linear Algebra Done Right.pdf#page=188|Linear Algebra Done Right]] or [[generatingfunctionology.pdf#page=13|generatingfunctionology]] for other approaches.

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

Then, place a tromino such that it has one part in each of the three remaining quadrants. Now each of them has a "removed piece". Cover them.

For example,
![[S1_trominoCoveredChessboard.jpeg]]
is a covering of a chessboard. Different colours indicate levels of recursion. Pink is at no level of recursion, green is at one level of recursion, and orange is the base case at two levels of recursion.

##### _corollary:_ $2^{2n} - 1$ is a multiple of $3$

For any $n \in \bb{N}$, there is some $k \in \bb{Z}$  such that $2^{2n} - 1 = 3k$.

##### _proof:_

For any $n \in \bb{N}$ we have a tromino covering of the $2^n \times 2^n$ chessboard with one piece removed. Since there are $2^{2n}$ pieces in the chessboard, with one removed, there are $2^{2n} - 1$ pieces, which are covered by some number of trominoes, say $k$. Then, $3k = 2^{2n} - 1$.


### Strong induction

Strong induction extends induction by allowing you to assume all previous cases. It works for the same reasons as induction.

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

A new question that we can ask that at first seems unrelated to Fibonacci numbers is "How many sequences of $1$ and $2$ sum to $n$?" Note that these are just the same as the number of ways to tile a strip of length $n$ with dominoes and single square tiles (counting permutations).

##### _example:_ tiling an $n$-strip with dominoes and squares

There is only one way to tile a $1$-strip: with one square.
There are $2$ ways to tile a $2$-strip: two squares, or one domino.
There are three ways to tile a $3$-strip: three squares, one domino and one square, or one square and one domino.
In fact, we can show that there are always $F_{n+1}$ ways to tile an $n$-strip.

We suggestively name the number of ways to reflect this

##### _definition:_ Fibonacci tiling numbers

For $n \in \bb{N}$ the $n$th Fibonacci tiling number, $f_n$ is the number of different ways to tile an strip of length $n$ with dominoes and squares. 

By convention we have $f_0 = 1$ so we can extend the following result to $0$ if we so desire.

##### _proposition:_ Fibonacci tiling numbers are Fibonacci numbers

For $n \in \bb{N}$ $f_n = F_{n + 1}$.

##### _proof:_

We can show this by induction. 

First, just by our calculations, we know $f_1 = F_2$ and $f_2 = F_3$.

Suppose $f_n = F_{n + 1}$ and $f_{n - 1} = F_{n}$. For any tiling of an $(n + 1)$-strip, there are only two options for the first tile we place - a domino or a square. If first tile is a domino, then there are $f_{n + 1 - 2} = f_{n - 1}$ ways to tile the remaining $n + 1 - 2 = n - 1$ squares. If the first tile is a square, then there aer $f_{n + 1 - 1} = f_n$ ways to tile the remaining $n + 1 - 1 = n$ squares.

This means that we have a total of
$$
f_{n + 1} = f_n + f_{n - 1} = F_{n + 1} + F_{n} = F_{n + 2} = F_{n + 1 + 1}
$$
ways to tile the $(n + 1)$-strip as desired.

Then by induction, for any $n \in \bb{N}$, there are $F_{n + 1}$ ways to tile the $n$-strip. That is, $f_n = F_{n + 1}$.

Looking at more examples shows us that thinking of the Fibonacci numbers as tilings isn't just a useful geometric intuition, but can also make proving results easier.

##### _proposition:_ tilings of sums

For any $m, n \in \bb{N}$, $f_m f_n + f_{m - 1} f_{n - 1} = f_{m + n}$.

##### _proof:_

By definition there are $f_{m + n}$ ways to tile a $(m + n)$-strip.

We can divide these tilings into two groups - tilings that are breakable at the $m$th tiling - that don't have a domino across break and tilings that are not - that do have a domino across the break.

There are $f_m f_n$ breakable tilings - there are $f_m$ ways to tile one side and $f_n$ ways to tile the other. There are $f_{m - 1} f_{n - 1}$ unbreakable tilings - place a domino over the break and then there are $f_{m - 1}$ ways to tile one side of the domino and $f_{n - 1}$ ways to tile the other.

While this result is easy to prove by induction, its corollary (which can also be proved by the same thinking about breakable tilings) is not.

##### _corollary:_ tiling double the length

For any $n \in \bb{N}$, $f_{n - 1}^2 + f_n^2 = f_{2n}$.

We can also provide a much more informative proof of the fact that [[#_proposition _ the sum of Fibonacci numbers is almost a Fibonacci number|the sum of Fibonacci numbers is almost a Fibonacci number]], which we proved by induction earlier.

##### _proposition:_ the sum of Fibonacci numbers is almost a Fibonacci number

For $n \ge 0$,
$$
\sum_{k = 0}^n F_k = F_{n + 2} - 1.
$$

##### _proof:_

Obviously, it is sufficient to just show the analogous result for $f_n$.

When we want to throw one tiling out, it's only natural to throw out the all-squares tiling. Thus, we say that there are $f_{n + 2} - 1$ tilings of an $(n + 2)$-strip that include at least one domino.

We can also count the domino-containing tilings by looking at all the tilings such that the $k$th square is the square at which a domino starts (all the succeeding places are covered by single squares). Then that leaves us $n - k$ squares to tile as we please. We exhaust these domino-containing tilings by looking at all the $k \in \bb{N}_n$. That is, the total number of domino-containing tilings is
$$
\sum_{k = 0}^n f_k.
$$

This gives us exactly what we want:
$$
f_{n + 2} - 1 = \sum_{k = 0}^n f_k.
$$
