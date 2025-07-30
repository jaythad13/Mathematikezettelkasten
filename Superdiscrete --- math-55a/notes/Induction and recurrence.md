---
tags:
- math-55A/1
- comb
---

### Combinatorics by induction

We can use the [[Analysis --- math-131/notes/Before the real numbers#_definition _ the Peano axioms|axiom of induction]] to prove various combinatorial results.

##### _example:_ the sum of the first $n$ numbers, squares or cubes — triangle, pyramid (and whatever else) numbers

We can prove that $1 + 2 + \ldots + n = n(n + 1) / 2 = \binom{n}{2}$ using Gauss' trick (pair numbers $(1, n), (2, n - 1), \dots$ summing to $n + 1$ (or $n$) and counting the number of pairs). Of course, there is also a combinatorial proof. When we arrange a triangle number of asterisks as a triangle, each one of the $T_{n}$ asterisks $*$ corresponds to a choice of two of the daggers $\dagger$. Thus, $T_{n} = \binom{n}{2} = n (n + 1) / 2$.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& & & & * \\
		& & & * & & * \\
		& & * \ar[lldd, dashed, no head] \ar[rrdd, dashed, no head] & & * & & * \\
		& * & & * & & * & & * \\ \hline
		\dagger & & \dagger & & \dagger & & \dagger & & \dagger
	\end{tikzcd}
\end{document}
```
 
 However, these approaches don't generalise immediately to sums of squares or cubes. Induction is a lot more work, but generalises.

We know that
$$
\sum_{k = 1}^1 k = 1 = \frac{1 (1 + 1)}{2} = 1.
$$
Suppose
$$
\sum_{k = 1}^n k = \frac{n(n + 1)}{2}
$$
for some particular $n \in \bb{N}$. Then
$$
\sum_{k = 1}^{n + 1} k = \frac{n (n + 1)}{2} + n + 1 = \frac{(n(n + 1) + 2 (n + 1))}{2} = \frac{(n + 1)((n + 1) + 1)}{2}.
$$
Thus, by induction $\sum_{k = 1}^n k = n(n + 1)  / 2$ for all $n \in \bb{N}$.

This is also how we can prove the identities $\sum_{k = 1}^n k^{2} =n(n + 1)(2n + 1) / 6$ and $\sum_{k = 1}^n n^{2} (n + 1)^{2} / 4$.

Induction isn't just for identities either — it's useful to prove any "self-similar" family of things indexed by $\mathbb{N}$.

##### _theorem:_ you can cover almost all of a chessboard with trominoes

Given a $2^n \times 2^n$ ($n \in \bb{N}$) "chessboard" with one piece removed, you can cover the board using trominoes.

###### _proof sketch:_

It's possible for $n = 1$ since we can choose to use no trominoes.

If it's true for some $n$, break the chessboard into four quadrants. One of them has a removed piece. Cover that quadrant in trominoes. Then, place a tromino such that it has one part in each of the three remaining quadrants. Now each of them has a "removed piece". Cover them.

For example,
![[Superdiscrete --- math-55A/attachments/for notes/Proof by induction/S1_trominoCoveredChessboard.jpeg]]
is a covering of a chessboard. Different colours indicate levels of recursion. Pink is at no level of recursion, green is at one level of recursion, and orange is the base case at two levels of recursion.

##### _corollary:_ $2^{2n} - 1$ is a multiple of $3$

For any $n \in \bb{N}$, there is some $k \in \bb{Z}$  such that $2^{2n} - 1 = 3k$.

### Recurrence relations

Of course, induction is very useful to prove things about recurrent sequences. These are sequences defined inductively. Specifically,

##### _definition:_ recurrence relation, recurrent sequence, linear recurrence

A ($k$-term) recurrence relation (or recurrent sequence) is a function $\mathbb{N} \to \mathbb{C}$ (or in more generality, some arbitrary [[Abstract algebra --- math-171/notes/Rings#_definition _ rings|ring]] $A$) by $n \mapsto a_{n}$ such that $a_{n} = f(n, a_{n - 1}, \dots, a_{n - k})$ for some function $f$.

We say it is a linear recurrence if $n \mapsto f(n, b_{1}, \dots, b_{k})$ is constant in $n$ for all $(b_{1}, \dots, b_{k})$ and $f$ is a linear functional $\mathbb{C}^k \to \mathbb{C}$.

With suitably many initial terms defined (usually $k$), note that by induction, the recurrent function $f$ defines the whole recurrent sequence.

Induction is particularly useful to prove facts about one of the most famous linear recurrences — [[Superdiscrete --- math-55A/notes/Fibonacci numbers#_definition _ Fibonacci numbers|the Fibonacci numbers]].

For example, we can easily reprove Binet's formula

![[Superdiscrete --- math-55A/notes/Fibonacci numbers#_theorem _ Binet's formula|Fibonacci numbers]]

###### _proof by induction:_ 

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
\begin{align}
F_{n + 1} & = F_{n} + F_{n - 1}  \\
 & = \frac{1}{\sqrt{5}} ( \varphi^n - \bar \varphi ^n + \varphi^{n - 1} - \bar \varphi^{n - 1})  \\
 & = \frac{1}{\sqrt 5} (\varphi^{n - 1} (\varphi + 1) - \bar \varphi^{n - 1}(\bar \varphi + 1))
\end{align}
$$
but we know $\varphi^2 = \varphi + 1$ and $\bar \varphi^2 = \bar \varphi + 1$. Substituting gives us
$$
F_{n + 1} = \frac{\varphi^{n + 1} - \bar{\varphi}^{n + 1}}{\sqrt{ 5 }}
$$
and then by induction we are done.

For another example, summing the first $n$ Fibonacci numbers appears to be almost the $(n + 2)$th Fibonacci number. We can prove this by induction.

##### _proposition:_ the sum of Fibonacci numbers is almost a Fibonacci number

For $n \ge 0$,
$$
\sum_{k = 0}^n F_k = F_{n + 2} - 1.
$$

###### _proof:_

Note that 
$$
\sum_{k = 0}^1 F_k = F_0 + F_1 = 1 = 2 - 1 = F_3 - 1.
$$
That is, we have the base case.

If for some $n \in \bb{N}$, $\sum_{k = 0}^n F_k = F_{n + 2} - 1$, then 
$$
\sum_{k = 0}^{n + 1} F_k = F_{n + 1} + F_{n + 2} - 1 = F_{(n + 1) + 2} - 1.
$$
Thus, by induction, we are done.

### Strong induction

Strong induction extends induction by allowing you to assume all previous cases. It works for the same reasons as induction. Again, the Fibonacci numbers provide interesting examples.

##### _theorem:_ Zeckendorf's theorem

For any $n \in \mathbb{N}$, we can write $n = \sum_{\alpha \in A} F_\alpha$ for some finite $A \subseteq \mathbb{N}$. Further, $A$ can be chosen to contain no two consecutive $\alpha \in \mathbb{N}$.

Note that this means we can't use any number twice, including that we can't use $1$ twice.

###### _proof:_

The greedy algorithm where you take the largest Fibonacci less than the number you want to sum up to works. We can prove this by strong induction.

This works for $n = 1$, by choosing $A = \{ 1 \}$.

Suppose this works for all numbers less than $n + 1$. If $n + 1$ is a Fibonacci number, we are done. If it is not, it lies between two Fibonacci numbers. Choose the greatest Fibonacci number less than it, say $F_j$. Then $m = n + 1 - F_j$ is the sum of distinct Fibonacci numbers (with no two consecutive). Note that we can also bound it.
$$
m < F_{j + 1} - F_j = F_{j - i} \le F_j.
$$
Thus, $m < F_{j - 1} \le F_{j}$ meaning that its expression as the sum of distinct Fibonacci numbers cannot include $F_{j - 1}$ not $F_{j}$. Thus
$$
n + 1 = F_j + m
$$
is the sum of distinct Fibonacci numbers (with no two consecutive).