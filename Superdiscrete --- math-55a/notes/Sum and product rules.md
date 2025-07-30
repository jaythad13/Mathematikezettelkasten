---
tags:
- math-55A/1
- comb
---

Combinatorics is the most basic (and still, sometimes the hardest) type of math. It is the math of counting things. Typically, the things we are counting are elements of some set. 

##### _definition:_ cardinality

The cardinality or count of a (finite) set $A$ is the number of elements in $A$, denoted by $\# A$.

For a finite set, we always have $A \in \mathbb{N}_{0}$.

Actually, in set theory, the cardinal numbers (including the non-negative integers $\mathbb{N}_{0}$) are defined by the equivalence classes of sets under bijection. Thus, for a finite set $A$, the information of what other sets $B$ it is in bijection with is (by definition) determined by whether $\# A = \# B$.

Most combinatorics comes down to rules for how to combine the counts that we have for various sets. We may want to characterise how we pick from 

### The product rule

If we are counting things in an "and" sense (counting all the ways to choose something from $A$ *and* something from $B$, and so on), we want to multiply the counts for each type of thing individually. For example,

##### _example:_ license plates

Suppose license plates come in two varieties:
1) 3 letters followed by 3 numbers
2) 2 letters followed by 4 numbers.

We can count the number of possible license plates by summing the number of license plates for each type, but also we could let the 3rd thing be either a number or a letter, where there are $36$ things it could be:
$$
26^3 \times 10^3 + 26^2 \times 10^4 = 36 \times 26^2 \times 10^3.
$$
If we decide that the letters and numbers must be different, we need to start from the end of the numbers since the third could be a number or a letter:
$$
26 \times 25 \times 31 \times 8 \times 9 \times 10
$$
(we deal with positions in order 6, 5, 4, 1, 2, 3 so that we only have to deal with the third position at the end).

We can formulate this rule exactly.

##### _theorem:_ the product rule

For finite sets $A$ and $B$, we have $\# A \times B = \# A \times \# B$.

Note that this generalises to the finite product of finite sets —
$$
\# \prod_{i = 1}^n A_{i} = \prod_{i = 1}^n \# A_{i}.
$$
### Permutations and binomial coefficients

The best examples of the product rule come from thinking about choosing subsets of a given size and arranging them. The first example is permutations.

##### _definition:_ permutations

A permutation of $n$ things is a bijection $\sigma : [n] \to [n]$.

Equivalently, a permutation of $n$ things is a choice of ordering for them.

We are familiar with the fact that $n! = n \times (n - 1) \times \dots \times 1$ tells us the number of permutations of $n$ things. This is a consequence of the product formula! Choosing an order for $n$ things involves choosing the first thing from all $n$, then the second from the remaining $n - 1$, and so on.

Stirling's approximation to the factorial is unrelated to the product rule but will be useful to us.

##### _theorem:_ Stirling's approximation

$$
\lim_{n \to \infty} \frac{n!}{(n/e)^n \sqrt{2 \pi n}} = 1
$$
making $(n/e)^n \sqrt{2 \pi n}$ a good approximation for $n!$.

###### _proof sketch:_

Look at the logarithm of $n!$. Since this is the logarithm of a product, it is the sum of logarithms. Approximate $\sum_{1}^N \log n$ as $\int_{1}^t \log x \, dx$ using calculus. Finally, go back to the original factorial by differentiating (with respect to $t$) and exponentiate. Proving that this approximation is good is what Stirling did.

##### _definition:_ binomial coefficients

For $n \in \mathbb{N}_{0}$ and integer $0 \le k \le n$, the $(n, k)$th binomial coefficient $\binom{n}{k}$ is the number of size-$k$ subsets from of a size-$n$ set.

Equivalently, it is the number of ways to choose $k$ distinct candies from a set of $n$ distinct candies. (Note that when you choose $k$ candies, it doesn't matter what order you choose them in).

What is the actual value of $\binom{n}{k}$? By its definition it must have some integer value, and it is given by the product rule!

##### _proposition:_ a factorial formula for the binomial coefficient

$$
\binom{n}{k} = \frac{n!}{k! (n - k)!}
$$

###### _proof:_

We can arrange (order matters) $k$ candies from $n$ candies by choosing the candies one at a time — the first, second, up to $k$ in $n(n - 1) \ldots (n - (k - 1)) = n! / (n - k)!$ ways. We can also arrange $k$ candies in $\binom{n}{k} k!$ ways by choosing the $k$ candies and then arranging them. These counts must be the same, and thus, give the desired formula.

This formula allows us to generalise the binomial coefficient to non-integer values.

##### _definition:_ non-integer binomial coefficients

For $x \in \mathbb{C}$ and $k \in \mathbb{N}_{0}$,
$$
\binom{x}{k} = \frac{x(x - 1) \dots (x - (k -1))}{k!}.
$$

We usually don't care to generalise to $k \not\in \mathbb{N}$.

##### _example:_ poker hands

How many poker hands are there? 

$\binom{52}{5}$. (Each poker hand is 5 cards from a deck of 52, where order doesn't matter)

How many full houses are there? (three of one, two of another)

For the triple, we can choose from $13$ different values, and for the double, we can choose from the remaining $12$ different values. For each of those choices of value we have to choose suits. To the double, we have $\binom{4}{2}$ choices, and for the triple we have $\binom{4}{3}$. Thus, there are $13 \times 12 \times \binom{4}{3} \binom{4}{2}$ full houses.

How many two pairs are there? (two of one, two of another, and one of yet another)

We need to choose 2 values from among 13, (don't do the stupid thing with $13 \times 12$) and then choose 2 from among 4 cards for each of them. Finally, we need to choose a fifth card that can be one of the remaining 48 cards, but it can't be from any of the previously chosen values, and thus, there are only 44 choices (don't do the stupid thing with 48). Thus, there are $\binom{13}{12} \binom{4}{2}^2 \times 44$ two pairs.

Alternately, we need to choose 3 values from among 13. Then we need to choose the singleton, which we can do in 3 ways. Then we assign suits.

Thus, we get $3 \times \binom{13}{3} \binom{4}{2}^2 \times 4$ two pairs.

### The sum rule

The product rule is lovely and simple because we aren't trying to make specific exceptions. When we try to do so, we have to split our sets into disjoint parts, add the parts we want, and subtract the parts we don't want. The sum rule (and later, [[Superdiscrete --- math-55A/notes/Inclusion-exclusion|inclusion-exclusion]]) is a way to get a handle on this. We can return to poker hands to see an example of how this is much more tricky.

##### _example:_ poker hands again

How many non-flush straights are there? (Say for simplicity we only allow wrapping around to the ace)

There are $10$ choices for the low card of the straight. Assigning (possibly different) suits to each, we get $10 \times 4^5$ straights. To count just the non-flush straights we subtract the number of straight flushes, of which there are only $10 \times 4$ (they are all assigned the same one of $4$ suits). Note that we partitioned the straights into flush and non-flush straights.

How many hands have at least one ace?

All hands, take away hands with no aces. This gives us $\binom{52}{5} - \binom{48}{5}$ hands. Alternatively, we could look at all the cases for $1$, $2$, $3$, or $4$ aces in your hands and sum them. This gives us $4 \times \binom{48}{4} + \binom{4}{2} \binom{48}{3} + \binom{4}{3} \binom{48}{2} + 48$ hands. In this second case we partitioned hands with aces into four cases of hands with $1$ through $4$ aces.

How many hands are garbage? (no pairs, no straight, no flush)

We can count all of the pairless hands (choose $5$ values, and choose suits for each of them) and remove the straights and flushes. Since the straights and flushes are pairless anyway, we can just subtract them. But since the straight flushes overlap, we have to add them back. This gives us $\binom{13}{5} 4^5 - 10 \times 4^5 - 4 \binom{13}{5} + 10 \times 4$. Note that this factors to $(\binom{13}{5} - 10)(4^5 - 4)$! This is just all the choices of $5$ values except the $10$ choices that lead to a straight, times all the choices of suits except the $4$ choices that lead to a flush.

Finally, jokers make the combinatorics of everything pretty horrible and the only saving grace is that they're rare.

The main idea here is that if your sets have no overlap (for example, they are partitioning a larger set), then you can count their union by just summing up their counts. This is the sum rule, which we state below in full generality.

##### _theorem:_ the sum rule

If $A_{1}, \dots, A_{n}$ are disjoint sets, then
$$
\bigcup_{i = 1}^n A_{i} = \sum_{i = 1}^n A_{i}.
$$

Note that as a corollary, we get the rule for excepting disjoint parts of a set.

##### _corrolary:_ the subtract rule

If $A, B$ are disjoint sets, then $\# A = \# A \cup B - \# B$.