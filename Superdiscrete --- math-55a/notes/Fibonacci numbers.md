---
tags:
- math-55A/1
- math-55A/2
- comb
---

The Fibonacci numbers are the most famous sequence in math.

##### _definition:_ Fibonacci numbers

The Fibonacci numbers are the [[Superdiscrete --- math-55A/notes/Induction and recurrence#_definition _ recurrence relation, recurrent sequence, linear recurrence|recurrent sequence]] defined by
$$
\begin{gathered}
	F_0 = 0 \\
	F_1 = 1 \\
	F_n = F_{n - 1} + F_{n - 2}.
\end{gathered}
$$

The Fibonacci sequence is intimately connected to the polynomial $x^{2} - x - 1$ and its roots.

##### _definition:_ the golden ratio 

The golden ratio and its conjugate are the two roots of the polynomial $x^{2} - x - 1$. We write them as
$$
\varphi = \frac{1 + \sqrt{ 5 }}{2}
\quad \text{and} \quad
\bar{\varphi} = \frac{1 - \sqrt{ 5 }}{2}
$$
respectively.

In fact, the golden ratio gives a general formula for the $n$th Fibonacci number. This is a special case of a more general result for all linear recurrence relations that can be proved by induction. We provide a different proof by linear algebra.

##### _theorem:_ Binet's formula

For each $n \in \mathbb{N}_{0}$
$$
F_n = \frac{\varphi^n - \bar{\varphi}^n}{\sqrt{5}}
$$
###### _proof sketch:_

Notice that the [[Linear maps|linear map]] $T : \mathbb{R}^{2} \to \mathbb{R}^{2}$ by $(x, y) \to (y, x + y)$ has $T^n(0, 1) = (F_{n}, F_{n + 1})$ for all $n$. It also has [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_definition _ eigenvalue, eigenvector|eigenvalues]] $\varphi$ and $\bar{\varphi}$ and a basis of corresponding eigenvectors $(1, \varphi), (1, \bar{\varphi})$. Since they sum to $\sqrt{ 5 }(0, 1)$, by linearity we have Binet's formula
$$
(F_{n}, F_{n + 1}) = T^n(0, 1) = \frac{\varphi^n}{\sqrt{ 5 }} (1, \varphi) + \frac{\bar{\varphi}^n}{\sqrt{ 5 }} (1, \bar{\varphi})
$$

### Fibonacci tiling numbers

A new question that we can ask that at first seems unrelated to Fibonacci numbers is "how many sequences of $1$ and $2$ sum to $n$?" Note that these are just the same as the number of ways to tile a strip of length $n$ with dominoes and single square tiles (counting permutations).

##### _example:_ tiling an $n$-strip with dominoes and squares

1) There is only one way to tile a $1$-strip: with one square.
2) There are $2$ ways to tile a $2$-strip: two squares, or one domino.
3) There are three ways to tile a $3$-strip: three squares, one domino and one square, or one square and one domino.
In fact, we can show that there are always $F_{n+1}$ ways to tile an $n$-strip.

We suggestively name the number of ways to reflect this

##### _definition:_ Fibonacci tiling numbers

For $n \in \bb{N}$ the $n$th Fibonacci tiling number, $f_n$ is the number of different ways to tile an strip of length $n$ with dominoes and squares. 

By convention we have $f_0 = 1$ so we can extend the following result to $0$ if we so desire.

##### _proposition:_ Fibonacci tiling numbers are Fibonacci numbers

For each $n \in \mathbb{N}$, $f_n = F_{n + 1}$.

###### _proof:_

[[Superdiscrete --- math-55A/notes/Induction and recurrence#_definition _ recurrence relation, recurrent sequence, linear recurrence|Recall]] that if two sequences have (enough of) the same initial values and satisfy the same recurrence relation, they are the same sequence.

First, we have already verified that $f_1 = F_2$ and $f_2 = F_3$.

For any tiling of an $(n + 1)$-strip, there are only two options for the first tile we place — a domino or a square. If first tile is a domino, then there are $f_{n + 1 - 2} = f_{n - 1}$ ways to tile the remaining $n + 1 - 2 = n - 1$ squares. If the first tile is a square, then there aer $f_{n + 1 - 1} = f_n$ ways to tile the remaining $n + 1 - 1 = n$ squares. Thus, $f_{n + 1} = f_{n} + f_{n - 1}$ as desired.

Looking at more examples shows us that thinking of the Fibonacci numbers as tilings isn't just a useful geometric intuition, but can also make proving results easier. 

For example, we provide a much more informative proof of the fact that the sum of Fibonacci numbers is almost a Fibonacci number than the standard induction proof.

![[Superdiscrete --- math-55A/notes/Induction and recurrence#_proposition _ the sum of Fibonacci numbers is almost a Fibonacci number|Induction and recurrence]]

###### _proof by tiling:_

Obviously, it is sufficient to just show the analogous result for $f_n$.

When we want to throw one tiling out, it's only natural to throw out the all-squares tiling. Thus, we say that there are $f_{n + 2} - 1$ tilings of an $(n + 2)$-strip that include at least one domino.

We can also count the domino-containing tilings by looking at all the tilings such that the $k$th square is the square at which a domino starts (all the succeeding places are covered by single squares). Then that leaves us $n - k$ squares to tile as we please. We exhaust these domino-containing tilings by looking at all the $k \in [n]$. That is, the total number of domino-containing tilings is also counted by $\sum_{k = 0}^n f_k$. Thus, we have the desired result.

Tiling numbers can also prove new identities that are hard to prove by induction. The first one below is doable by induction, but its corollary is much harder.

##### _proposition:_ tilings of sums

For any $m, n \in \mathbb{N}$, $f_m f_n + f_{m - 1} f_{n - 1} = f_{m + n}$.

###### _proof:_

By definition there are $f_{m + n}$ ways to tile a $(m + n)$-strip.

We can divide these tilings into two groups. We divide them into tilings that are breakable at the $m$th tiling which don't have a domino across break and tilings that are not which do have a domino across the break. There are $f_m f_n$ breakable tilings — there are $f_m$ ways to tile one side and $f_n$ ways to tile the other. There are $f_{m - 1} f_{n - 1}$ unbreakable tilings — place a domino over the break and then there are $f_{m - 1}$ ways to tile one side of the domino and $f_{n - 1}$ ways to tile the other.

##### _corollary:_ tiling double the length

For any $n \in \bb{N}$, $f_{n - 1}^2 + f_n^2 = f_{2n}$.