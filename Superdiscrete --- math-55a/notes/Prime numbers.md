---
tags:
- math-55A/3
- nt
---

##### _theorem:_ a divisor must divide something or, the important theorem

If $d \mid ab$ and $\gcd(d,a) = 1$ then $d \mid b$.

###### _proof:_

If $\gcd(d, a) = 1$, then by [[Superdiscrete --- math-55A/notes/Division and Euclid's algorithm#_theorem _ Bezout's theorem|Bezout's theorem]] we must have some integer combination $ax + dy = 1$. Thus, $abx + dby = b$, and then since $d = q ab$, for some integer $q$, we have $d(qx + by) = b$ and thus, $d \mid b$.

### Primes

##### _definition:_ prime numbers

A natural number greater than $1$ that has only two natural number divisors is a prime number.

Note that this explicitly excludes $0$ and $1$ from being primes.

##### _definition:_ composite numbers

A natural number greater than $1$ that is not prime is a composite number.

##### _proposition:_ every number has a prime factorisation

Every natural number $n$, greater than $1$ can be written as the product of finitely many primes.

###### _proof sketch:_

Use strong induction. If $n$ is a prime, we are done. If $n$ is not a prime, it is divisible by some number less than it (because if it were only divisible by itself and one, it would be a prime), and thus, is the product of two numbers less than it that both have prime factorisations.

##### _example:_ the martian numbers don't have unique factorisation

The martian numbers (we all know martians have two heads), $\bb{E} = \set{2, 4, 6, 8, \ldots}$ have every other number as a 'prime'. It fails because the division algorithm fails!

##### _theorem:_ a prime divisor divides a part of a product or, the theorem of prime importance

If $p$ is prime and $p \mid a_1 \times \cdots \times a_n$ then $p \mid a_j$ for some $j \in \bb{N}_n$
 
###### _proof sketch:_

If $p \mid a_1$, then we're done.

If $p \nmid a_1$, then $\gcd(a, p) = 1$, since $p$ only has two divisors that it could have in common with $a_1$: $p$ and $1$. Then, since [[#_theorem _ a divisor must divide something or, the important theorem|it must divide something]], $p \mid a_2 \times \cdots \times a_n$.

By induction, we can extend this to the theorem.

##### _theorem:_ unique factorisation

Every number $n \in \bb{N}_{\ge 2}$ has a unique prime factorisation
$$
n = p_1 \times \cdots \times p_j
$$

###### _proof sketch:_

We prove this by contradiction. 

Suppose $m$ is the smallest number with two different prime factorisations:
$$
p_1 \times \cdots p_j = m = q_1 \times \cdots q_k.
$$
Then $p_1$ must divide $q_1 \times \cdots \times q_k$, which means it must divide some $q_i$, which we choose without loss of generality to be $q_1$. Then $\frac{m}{p_1}$ is a number less than $m$ with two different factorisations (since $p_1$ and $q_1$ couldn't be the distinct factors in $m$). This contradicts our first assumption.

##### _proposition:_ minimum and maximum exponent prime products

Suppose for some list of primes $p_1, \ldots, p_n$ we have
$$
a = \prod_{i = 1}^n p_i^{\alpha_i}
$$
and
$$
b = \prod_{i = 1}^n p_i^{\beta_i}
$$
where $\alpha_i, \beta_i \in \bb{Z}_{\ge 0}$ (they can be zero).
Then
$$
\gcd(a, b) = \prod_{i = 1}^n p_i^{\min(\alpha_i, \beta_i)}
$$
and
$$
\operatorname{lcm}(a, b) = \prod_{i = 1}^n p_i^{\max(\alpha_i, \beta_i)}.
$$
###### _proof:_

Let $g$ be the first product and $l$ be the second.

Note that $g$ divides $a$ and $b$. If there is some $d$ that divides $a$ and $b$, then it must divide $g$, since it cannot contain any prime factor that either of $a$ or $b$ doesn't contain, and it can only contain a prime in the least exponent among $a$ and $b$. Thus, $d \le g$. Thus, $g = \gcd(a, b)$.

Note that $l$ is a multiple of both $a$ and $b$. If there is some $m$ that is a multiple of both $a$ and $b$ then it must be a multiple of $l$ since it must contain all of the prime factors of $a$ and $b$ and it must contain a prime in the greatest exponent among $a$ and $b$. Thus, $m \ge g$. Thus, $l = \operatorname{lcm}(a, b)$.

##### _corollary:_ the product of $\operatorname{lcm}$ and $\gcd$

$$
\gcd(a, b) \times \operatorname{lcm}(a, b) = ab
$$

##### _theorem:_ the infinitude of primes

There are infinitely many primes.

###### _proof sketch:_

Suppose by contradiction, $p$ is the greatest prime number. $p! + 1$ is prime or has a prime factor greater than $p$.

##### _proposition:_ there are arbitrarily long strings of composites

For any $n \in \bb{N}$ we can find $n$ consecutive composites.

###### _proof:_

$(n + 1)! + 2 \ldots (n + 1)! + (n + 1)$ are $n$ consecutive composites.

Just for fun, let's use do some rationality stuff.

##### _proposition:_ irrational exponents can be rational

There exist irrational $a, b$ such that $a^b \in \bb{Q}$.
###### _proof:_

If $\sqrt{2}^{\sqrt{2}}$ is rational, we're done.
If not, $(\sqrt{2}^{\sqrt{2}})^{\sqrt{2}}$ is $\sqrt{2}^2 = 2$ and a rational exponent of irrationals. 