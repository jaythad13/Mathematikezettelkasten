---
tags:
- nt
- alg-nt
- PUNDiT
---

##### _example:_ sign obstruction

Consider $f(x) = x^2 + 1$. Why are there no rational $q$ such that $f(q) = 0$?
Squares of positive numbers are always greater than $0$. We call this kind of reason for non-existence of zeros a "sign obstruction"

##### _example:_ mod obstruction

What about $g(x) = x^2 - 2$? Why are there no rational roots?
Suppose there were a solution, then there would have to be an integer $a$ such that $a$ is both even and odd. We call this a "mod $2$ obstruction".

##### _example:_ a more complicated mod obstruction

Why are there no rational roots of $h$, where $h(x, y) = x^2 + y^2 - 3$?

Suppose there was a solution $(x, y) \in \bb{Q}$. Then there exist some relatively prime $u, v \in \bb{Z}$ such that $u^2 + v^2 - 3w^2 = 0$ with integer $w$. We can ensure these exist by clearing denominators.

Then neither of them can be divisible by $3$, since $u = 3k$ gives us $v^2 = 3(w^2 - 3k^2)$, contradicting their relative primeness. Thus, 

Thus, $u = 3k_1 + 1$ or $u = 3k_1 + 2$  and $v = 3k_2 + 1$ or $3k_2 + 2$ which gives us $u^2 = 3n + 1$ and $v^2  = 3m +1$. But then $u^2 + v^2 = 3(m + n) + 2$ when we know $u^2 + v^2 = 3w^2$.

We call this a "mod 3 obstruction".

This leads us to the question "What if $f(x_1, \ldots, x_n)$ has a sign obstruction and no $\mod n$  obstruction for any $n \in \bb{Z}$?"

##### _definition:_ The Hasse principle

A polynomial satisfies the Hasse principle if avoiding sign and mod obstructions means there is an integer root.

This is basically saying that if a polynomial has a zero in infinitely many contexts, then that should be because it really is zero for some thing.

##### _example:_ an unobstructed polynomial

Consider $f(x, y) = x^2 + y^2 - 2 = 0$. We have a rational solution $(\frac{1}{5}, \frac{7}{5})$! Then there's definitely no sign and mod obstructions.

But we want to go in the opposite direction. And how would we even do that?

##### _strategy:_ using the Hasse principle

1) Find a real solution. If you can't, stop.
2) Clear denominators (homogenise the polynomial). 
3) Consider the resultant $F(X_1, \ldots, X_n)$, a function of integers. Make sure the way you clear denominators so that the integers end up being relatively prime (as a group, not necessarily pairwise) so that you don't get trivial roots.
4) For each $N \in \bb{N}$, check to see whether you can find a (primitive) $\mod N$ solution.

But this is still infinitely many cases!

Okay, we can use the Chinese remainder theorem to simplify this to only having to do it for $p^k$ for all primes $p$ and all $k \in \bb{N}$. 

But this is still infinitely many cases!

But then big theorems from algebraic geometry tell us that for the "right kinds of polynomials" you avoid $\mod p$ obstructions for all sufficiently large primes $p$.

But this could still be computationally infeasibly many primes, and we could still have $p^k$ obstructions which is infinitely many cases!

But Hensel's lemma allows us to handle $p^{k + 1}$ obstructions if we know that we can handle obstructions for a given prime $p$. And we have bounds to tell us how much to check (in terms of the integer coefficients of the polynomials)!

Does this then can guarantee that the polynomial have zeroes?

Sometimes (?)

##### _theorem:_ Hasse's theorem

A polynomial $f(x_1, \ldots, x_n)$ of the form 
$$
f(x_1, \ldots, x_n) = \sum_{i, j} a_{i, j} x_i x_j
$$
has a nontrivial integer solution if and only if it has a solution over $\bb{R}$ and primitive solutions $\mod N$ for all $N \in \bb{N}$.

But this only works for lower degree things. What about higher degree things?

##### _example:_ Hasse principle fails on higher degrees

Lind and Reichardt showed that $f(x, y) = 2y^2 + (x^4 + 17)$ doesn't have integer roots. In general the Hasse principle fails for higher even degree roots.

Selmer showed that $g(x, y, z) = 3x^3 + 4y^3 + 5z^3$ doesn't have integer roots.

The Hasse principle doesn't really work most of the time. However, when it is violated, there are interesting reasons. Some of the most important concepts in algebraic geometry are to explain how it fails. 

Important question: "What is the obstruction that causes there to not be zeros?"






