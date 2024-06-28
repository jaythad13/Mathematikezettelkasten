---
tags:
- math-55A/2
- comb
---

Most combinatorial rules come down to a rule for counting sums and a rule for counting products.

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

We are familiar with the fact that $n!$ tells us the number of permutations of $n$ things. It turns out that we can approximate $n!$ well.

##### _theorem:_ Stirling's approximation

$$
\lim_{n \to \infty} \frac{n!}{(n/e)^n \sqrt{2 \pi n}} = 1
$$
making $(n/e)^n \sqrt{2 \pi n}$ a good approximation for $n!$.

###### _proof sketch:_

Look at the logarithm of $n!$. Since this is the logarithm of a product, it is the sum of logarithms. Approximate the area covered using calculus, and then go back to the original factorial by differentiating and then exponentiating. This ends up being Stirling's approximation.

##### _definition:_ $\binom{n}{k}$

$\binom{n}{k}$ is the number of ways to choose $k$ different objects from a set of $n$ objects.

This is well and good, but what is the actual value of $\binom{n}{k}$? By its definition it must have some integer value!

##### _proposition:_ the binomial coefficient

$$
\binom{n}{k} = \frac{n!}{k! (n - k)!}
$$

###### _proof sketch:_

We can arrange (order matters) $k$ things from $n$ things in $n(n - 1) \ldots (n - (k - 1))$ ways. We can also arrange $k$ things in $\binom{n}{k} k!$ ways.

We generalise the non-factorial definition of the binomial theorem to $n \notin \bb{N}$

##### _definition:_ $\binom{x}{k}$ for $x \notin \bb{N}$

$$
\binom{n}{k} = \frac{x(x - 1) \dots (x - (k -1))}{k!}.
$$

We usually don't care to generalise to $k \notin \bb{N}$.

##### _example:_ poker hands

How many poker hands are there? 

$\binom{52}{5}$. (Each poker hand is 5 cards from a deck of 52, where order doesn't matter)

How many full houses are there? (three of one, two of another)

For the triple, we can choose from 13 different values, and for the double, we can choose from 12 different values. For each of those choices of value we have to choose suits. To the double, we have $\binom{4}{2}$ choices, and for the triple we have $\binom{4}{3}$.

Thus, there are $13 \times 12 \times \binom{4}{3} \binom{4}{2}$ full houses.

How many two pairs are there? (two of one, two of another, and one of yet another)

We need to choose 2 values from among 13, (don't do the stupid thing with $13 \times 12$) and then choose 2 from among 4 cards for each of them. Finally, we need to choose a fifth card that can be one of the remaining 48 cards, but it can't be from any of the previously chosen values, and thus, there are only 44 choices (don't do the stupid thing with 48).

Thus, there are $\binom{13}{12} \binom{4}{2}^2 \times 44$ two pairs.

Alternately, we need to choose 3 values from among 13. Then we need to choose the singleton, which we can do in 3 ways. Then we assign suits.

Thus, we get $3 \times \binom{13}{3} \binom{4}{2}^2 \times 4$ two pairs.

How many straights or straight flushes are there? (the sum of both)

There are 10 choices for the low card of the straight. (You can only wrap around up to the ace). Then assign suits.

Thus, we get $10 \times 4^5$ suits. If we want to throw out the straight flushes we can subtract the number of straight flushes, of which there are only $10 \times 4$.

How many hands have at least one ace?

All hands, take away hands with no aces.

This gives us $\binom{52}{5} - \binom{48}{5}$ hands.

We can look at all the cases for 1,2, 3, or 4 aces in your hands and sum them.

This gives us $4 \times \binom{48}{4} + \binom{4}{2} \binom{48}{3} + \binom{4}{3} \binom{48}{2} + 48$ hands.

How many hands are garbage? (no pairs, no straight, no flush)

We can count all of the pairless hands (choose 5 values, and choose suits for each of them) and remove the straights and flushes. Since the straights and flushes are pairless anyway, we can just subtract them. But since the straight flushes overlap, we have to add them back.

This gives us $\binom{13}{5} 4^5 - 10 \times 4^5 - 4 \binom{13}{5} + 10 \times 4$. Note that this factors to $(\binom{13}{5} - 10)(4^5 - 4)$! This is just all the choices of 5 values, except the 10 choices that lead to a straight times all the choices of suits, except the four choices that lead to a flush.

Wild cards fuck all of this up! They mess with the probabilities. For example, if you always use your wild card to convert a two pair to a three of a kind, it makes a three of a kind less rare than a two pair, but then if you change the value system to reflect this, you can flip your strategy back.