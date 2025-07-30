---
tags:
- math-55A/2
- nt
---

Fermat's little theorem makes playing over finite fields even more powerful than we thought.

##### _theorem:_ Fermat's little theorem

If $p$ is prime, then $a^p \equiv a \mod p$.

###### _proof:_

Suppose $p \mid a$. Then $a \equiv 0 \mod p$. Then $p \mid a^p$ and thus, $a \equiv 0 \mod p$ as well. By transitivity, $a^p \equiv a \mod p$.

If the first case doesn't apply $p \nmid a$ and thus, $\gcd(a, p) = 1$. Note that $0, \ldots, p - 1$ are all distinct $\mod p$. Since we have cancellation with $a$, and $1 \ldots, p - 1$ are all different $\mod p$, $a, 2a, \ldots, (p - 1)a$ are all different $\mod p$ too (think about the contrapositive of cancellation).
Since both of them contain all of the different things $\mod m$,
$$
a(2a)\cdots(p - 1)a \equiv (p - 1)! \mod p
$$
which gives us 
$$
a^{p - 1}(p - 1)! \equiv (p - 1)! \mod p
$$
and since we can cancel $(p - 1)!$ (it is obviously coprime with $p$)
$$
a^{p - 1} \equiv 1 \mod p.
$$
This is often referred to as Fermat's little theorem, with the added hypothesis that $a \not\equiv 0 \mod p$. Multiplying by $a$ gives us
$$
a^p \equiv a \mod p
$$
which works even when $a \equiv 0 \mod p$ as we showed above.

It turns out that we can do better than Fermat's little theorem — there's a similar proposition even for composite numbers.

### Euler's theorem

##### _definition:_ Euler's totient function

Euler's totient function is $\phi : \bb{N} \to \bb{Z}_{\ge 0}$ such that $\phi(n)$ is the cardinality of the the set of numbers less than $n$ coprime to $n$

##### _proposition:_ A formula for $\phi(n)$

If $n$ has prime factorisation $\prod_{i = 1}^m p_i$
$$
\phi(n) = n \prod_{i = 1}^m (1 - \frac{1}{p_i})
$$

###### _proof sketch:_

We expect this to be true for probabilistic reasons (expect that even after I remove all the multiples of (for example) $7$, roughly $1/13$th of the rest are divisible by $13$).

This works out rigorously by [[Superdiscrete --- math-55A/notes/Inclusion-exclusion#_theorem _ Principle of Inclusion-Exclusion|inclusion-exclusion]].

Suppose $n = \prod_{i = 1}^m p_i$. Then get rid of all of the multiples of each $p_i$,
$$
n \Big (1 - \sum_{i = 1}^m \frac{1}{p_i} \Big )
$$
add back all the multiples of any pair $p_i p_j$ with $i \neq j$, and then the triples and so on to get
$$
\phi(n) = n \Big ( 1 - \sum_{i = 1}^m \frac{1}{p_i} + \sum_{i = 1}^m \sum_{j = 1}^{i - 1} \frac{1}{p_i p_j} - \cdots \Big )
$$
which then simplifies to
$$
\phi(n) = n \prod_{i = 1}^m (1 - \frac{1}{p_i})
$$


##### _theorem:_ Euler's theorem

If $\gcd(a, m) = 1$ then $a^{\phi(m)} \equiv 1 \mod m$. Note that in the special case that $m$ is prime, this is [[#_theorem _ Fermat's little theorem|Fermat's little theorem]] (the additional hypothesis version).

###### _proof:_

Similar to Fermat's little theorem proof, we will just multiply by the $\phi(m)$ numbers less than $m$ co-prime to $m$.

Specifically, let $\phi(m) = t$, and $u_1, \ldots, u_t$ are the numbers co-prime to $m$. Since they are all different $\mod m$ and we have cancellation with $a$, we know that $a u_1, \ldots, a u_t$ are all different $\mod m$, we also know that they are all of the $t$ numbers co-prime to $m$ ($\gcd(u_i, m) = 1$ and $\gcd(a, m) = 1$ gives us $\gcd(au_i, m)$ — just multiply their minimal integer combinations or do it by prime factorisation). Thus,
$$
a^n \prod_{i = 1}^n u_i = \prod_{i = 1}^n a u_i \equiv_m \prod_{i = 1}^n u_i.
$$
Since we have cancellation with $\prod_{i = 1}^n u_i$, we get
$$
a^n = 1 \mod m.
$$

### Primality testing

##### _strategy_: to check if $n$ is prime

If $2^n \not\equiv 2  \mod n$, $n$ is not prime.

Note that if $2^n \equiv 2 \mod n$, $n$ may not be prime. It probably is prime, and it behaves like a prime, but it might not be a prime

##### _example:_ an almost-prime

$2^{341} \equiv 2 \mod n$, but $341$ is not a prime.

##### _definition:_ Carmichael numbers

If $a^n \equiv a \mod n$ for all $a$ and $n$ is not prime, then we say $n$ is a Carmichael number.

##### _example:_ Carmichael numbers

$561$ gives us $a^{561} \equiv a$ for every $a$. It is a Carmichael number.

Note $341$ is not a Carmichael number. (It fails for $a = 341$).

##### _theorem:_ a complete description of Carmichael numbers

$n$ is a Carmichael number if and only if
1) $n = p_1 \times \cdot \times p_r$ where $r \ge 2$ and the primes are all distinct
2) $p_i - 1 \mid n - 1$ for all $i \in \bb{N}_r$.

It turns out Carmichael numbers are not a huge problem for probabilistic reasons.

### Computing $a^n \mod m$ for large $n$, or, how to achieve enormous powers!

But, we still have to calculate $a^n \mod n$ which seems computationally intractable for large numbers. Luckily there are some ways to make this better.

##### _method:_ use Euler's theorem

If $\gcd(a, m) = 1$ and $\phi(m)$ is known, you can exploit Euler's theorem to compute $a^n \mod m$, since $a^n \equiv a^r \mod m$ where $r$ is the remainder given by dividing $n$ by $\phi(m)$.

Unfortunately, if $\phi(m)$ is large, then it can still be difficult to calculate $a^r \mod m$. Fortunately, it's usually still doable by calculator even if it is not doable by hand.

##### _method:_ seed planting

Using the binary representation of $n$ successively square $a$, with some small adjustment.

##### _example:_ $6^{83} \mod 79$ two ways

Note that $83 = 64 + 16 + 2 + 1$.

Thus, $6^{83} = 6^{64}6^{16}6^{2}6^1$. We can write this as $((((((6^1)^2)^2 \times 6)^2)^2)^2 \times 6)^2 \times 6$. While this isn't really helpful if we're doing it generally, breaking it down like this allows us to take the remainder at each step and break our work down.

$$
\begin{split}
	((((((6^1)^2)^2 \times 6)^2)^2)^2 \times 6)^2 \times 6 & = (((((6^2)^2 \times 6)^2)^2)^2 \times 6)^2 \times 6 \\
	& = ((((36^2 \times 6)^2)^2)^2 \times 6)^2 \times 6 \\
	& = (((7776^2)^2)^2 \times 6)^2 \times 6 \\
	& \equiv_{79} (((34^2)^2)^2 \times 6)^2 \times 6 \\
	& = (((1156^2)^2 \times 6)^2 \times 6 \\
	& \equiv_{79} (((50^2)^2 \times 6)^2 \times 6 \\
	& = (((2500)^2 \times 6)^2 \times 6 \\
	& \equiv_{79} (51^2 \times 6)^2 \times 6 \\
	& = 15606^2 \times 6 \\
	& \equiv_{79} 43^2 \times 6 \\
	& = 11094 \\
	& \equiv_{79} 34.
\end{split}
$$
This takes far fewer than $83$ multiplications, but divides it up into enough steps that it is computationally feasible to mod out.

Of course, since $79$ is known prime and relatively small, we can just use Euler's theorem:
$$
\begin{split}
6^{83} & = 6^{78} \times 6^5 \\
& \equiv_{79} 1 \times 108 \times 72 \\
& \equiv_{79} 29 \times 72 \\
& = 2088 \\
& \equiv_{79} 34. 
\end{split}
$$