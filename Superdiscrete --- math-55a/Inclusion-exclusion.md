---
tags:
- comb
- math-55a
lecture:
- math-55a-2
---

We know that
$$
\abs{A_1 \sqcup A_2} = \abs{A_1} + \abs{A_2}
$$
but what about
$$
\abs{A_1 \cup A_2}?
$$

Since we know we've double counted $\abs{A_1 \cap A_2}$, we can get
$$
\abs{A_1 \cup A_2} = \abs{A_1} + \abs{A_2} + \abs{A_1 \cap A_2}.
$$

What about $A_1 \cup A_2 \cup A_3$?

Looking at the Venn diagram we can use the same argument about double counting to get an answer. Because we uncount $\abs{A_1 \cap A_2 \cap A_3}$ thrice, we have to recount it. We get
$$
\abs{A_1 \cup A_2 \cup A_3} = \abs{A_1} + \abs{A_2} + \abs{A_3} - \abs{A_1 \cap A_2} - \abs{A_2 \cap A_3} - \abs{A_3 \cap A_1} + \abs{A_1 \cap A_2 \cap A_3}.
$$

This generalises!

##### _theorem:_ Principle of Inclusion-Exclusion

$$
\abs{A_1 \cup \cdots \cup A_n} = \sum_{k = 1}^n \abs{A_k} - \cdots 
$$
##### _proof sketch:_

Any element $x \in A_1, \ldots A_m$ (we can choose indexes conveniently without loss of generality) is chosen $\binom{m}{k}$ times among the $k$-intersections. Then the total number of times that $x$ is counted and uncounted is
$$
\binom{m}{1} - \binom{m}{2} + \binom{m}{3} + \cdots + (-1)^{m - 1} \binom{m}{m}
$$
We know that
$$
-\binom{m}{0} + \binom{m}{1} + \cdots (-1)^{m - 1}\binom{m}{m} = 0.
$$
Thus
$$
\binom{m}{1} - \binom{m}{2} + \binom{m}{3} + \cdots + (-1)^{m - 1} \binom{m}{m} = 1
$$
which is the number of times $x$ is counted in $A_1 \cup \cdots \cup A_n$.

##### _example:_ inclusive poker hands

How many poker hands are there that contain at least one of each suits?

There are $\binom{39}{5}$ hands that don't contain any hearts, and similarly for every suit. Then subtract all the hands with none of two suits (no hearts and no spades, for example). Then add back all the hands with none of three suits. Then subtract all these bad hands from the total number of hands.

This gives us
$$
\binom{52}{5} - \Big [ \binom{4}{1} \binom{39}{5} - \binom{4}{2} \binom{26}{5} + \binom{4}{3} \binom{13}{5} \Big ]
$$
inclusive hands.

Note that we can do this without inclusion-exclusion - choose the suit that there are two of, then choose the two cards from that suit and the one card from each of the other three suits.

##### _example:_ 

How many integer solutions are there to 
$$
x_1 + \ldots + x_6 = 21
$$
where $0 \le x_i \le 8$ for all $i \in \bb{N}_6$.

This is similar to multichoose, but we have a restriction - we have to throw out all the splits where any ninja $k$ gets more than $8$ kandies for all $k$. We can do this with inclusion exclusion!

Thus, we have
$$
\Big( \binom{6}{21} \Big) - 6 \Big ( \binom{6}{21 - 9} \Big ) + \binom{6}{2} \Big ( \binom{6}{21 - 18} \Big)
$$
solutions.

> It's not one ninja, it's ninja 1. It's not two ninjas, it's ninjas 1 and 2.

\- Prof. Benjamin

##### _example:_ derangements

If $n$ homeworks are randomly returned to $n$ students, what is the chance that nobody gets their own homework? Or, how many permutations of $\bb{N}_n$ have no fixed point.

We can use inclusion exclusion again!

Let $D_n$ be the number of ways that no one gets their own homework. There are $n!$ total permutations, subtract all the ways that one person gets their homework back, add all the double counted ways that two people get their homework back and so on.

$$
D_n = n! - n (n - 1)! + \binom{n}{2}(n - 2)! - \binom{n}{3}(n - 3)! + \cdots = \sum_{k = 0}^n \binom{n}{k}(n - k)!
(-1)^k
$$
But then we can write the sum as
$$
\sum_{k = 0}^n \frac{n!}{k! (n - k)!}(n - k)! (-1)^k = n! \sum_{k = 0}^n \frac{(-1)^k}{k!}
$$
Then the probability is
$$
\frac{D_n}{n!} = \sum_{k = 0}^n \frac{(-1)^k}{k!} \approx \frac{1}{e} \text{ for } n \ge 5.
$$
This converges very fast because the next step is only $\frac{1}{(n + 1)!}$ which is very small!

It turns out that $D_n = \frac{n!}{e}$ to the nearest integer.

Because the probabilities are almost independent, we get $\frac{D_n}{n!} \approx (1 - \frac{1}{n})^n$.
