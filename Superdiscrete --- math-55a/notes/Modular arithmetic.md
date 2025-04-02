---
tags:
- math-55A/2
- nt
- alg
---

### What is a congruence?
##### _definition:_ congruence $\mod m$

For $m > 0$ we say $a \equiv b \mod m$, pronounced $a$ is congruent to $b$ $\mod m$, if $m \mid a - b$.

##### _example:_ congruences

1) $26 \equiv 20 \mod m$
2) $26 \equiv 2 \mod m$
3) $26 \not\equiv 1 \mod m$ 
4) $26 \equiv -1 \mod m$ 

##### _proposition:_ congruence is an equivalence relation

$a \equiv a \mod m$, if $a \equiv b \mod m$, then $b \equiv a \mod m$, and if $a \equiv b \mod m$ and $b \equiv c \mod m$, then $a \equiv c \mod m$.

###### _proof:_

$a - a = 0$, which is divisible by $m$. 

If $a \equiv b \mod m$, we have $a - b$ divisible by $m$. Then $b - a$ is divisible by $m$ (multiply by the negation of the thing that divides $a - b$).

If $a \equiv b \mod m$ and $b \equiv c \mod m$, then we have $a - b$ and $b - c$ divisible by $m$, which then, by [[Superdiscrete --- math-55A/notes/Dividing integers - basic number theory#_theorem _ integer combination theorem|integer combination]] gives us $a - c = (a - b) + (b - c)$ is divisible by $m$.

##### _proposition:_ congruence is preserved by addition and multiplication

If $a \equiv b \mod m$ and $c \equiv d \mod m$ then $a + c \equiv b + d \mod m$ and $ac \equiv bd \mod m$.

###### _proof:_

Addition is easy: since we have $a - b$ and $c - d$ divisible by $m$, just add them to get $(a + c) - (b + d)$ divisible by $m$.

$ac - bd = (a - b)c + (c - d)b$ which by [[Superdiscrete --- math-55A/notes/Dividing integers - basic number theory#_theorem _ integer combination theorem|the integer combination theorem]] is divisible by $m$. Thus, $ac \equiv bd \mod m$.

##### _corollary:_ congruence is preserved by (integer) exponentiation

If $a \equiv b \mod m$, then $a^n \equiv b^n \mod m$ for any nonnegative integer $n$.

##### _corollary:_ congruence is preserved by polynomials in $\bb Z[x]$

If $a \equiv b \mod m$ then $p(a) \equiv p(b) \mod m$ for any $p \in \bb Z[x]$.

### Dividing $\mod m$

We can also subtract! But can we divide? Not always.

##### _example:_ where you can't divide

$6 \times 13 \equiv 6 \times 3 \mod 20$ but $13 \not\equiv 3 \mod 20$.

##### _proposition:_ cancellation $\mod m$

If $ax \equiv ay \mod m$, and $\gcd(a, m) = 1$ then $x \equiv y \mod m$. More generally $x \equiv y \mod \frac{m}{\gcd(a, m)}$.

###### _proof:_

If $ax \equiv ay \mod m$ then $m|a(x - y)$. If $\gcd(a, m) = 1$, then since it [[Superdiscrete --- math-55A/notes/Euclid's algorithm and primes#_theorem _ a divisor must divide something or, the important theorem|must divide something]], $m|(x - y)$ and thus, $x \equiv y \mod m$.

If $ax \equiv ay \mod m$ then we also have $ax \equiv ay \mod \frac{m}{\gcd(a, m)}$. Since $a$ is co-prime to that, the previous result gives us $x \equiv y \mod \frac{m}{\gcd(a, m)}$.

##### _definition:_ multiplicative inverses $\mod m$

An integer $a$ has a multiplicative inverse $b$ $\mod m$ if there exists an integer $b$ such that $ab \equiv 1 \mod m$.

##### _theorem:_ coprime $a, m$ give us multiplicative inverses

$\gcd(a, m) = 1$ if and only if $a$ has a unique multiplicative inverse $\mod m$.

###### _proof sketch:_

Just do the algebra after [[Superdiscrete --- math-55A/notes/Dividing integers - basic number theory#_theorem _ Bezout's theorem|Bezout's theorem]]. 

### Fermat's little theorem

We know that we have a characterisation of when we can divide $\mod m$. This gives us the following result.

##### _corollary:_ $\bb{Z}_p$ is a field, whatever that means

If $p$ is prime then $1, 2, \ldots p -1$ have inverses $\mod p$.

###### _proof:_

$1, 2, ... p - 1$ are all coprime with $p$, giving us multiplicative inverses, and thus a field.

##### _corollary:_ Wilson's theorem

$(p - 1)! \equiv -1 \mod p$ for any prime $p$ (and the other way around, though that's not so directly a corollary).

###### _proof sketch:_

For any prime greater than $7$, $p - 1$ is its own inverse and so is $1$. The others group in inverse pairs to multiply to $1$. 

If others are their own inverse, there'd be an even number of them, but in fact the others can't be their own inverse: $a^2 \equiv 1 \mod p \implies p \mid (a + 1)(a - 1)$.

The other way round is just some algebra — composite $n$ gives us some divisor of $n$ that also divides $(n - 1)!$, and thus, does not divide $(n - 1)! + 1$. Thus, $n \nmid (n - 1)! + 1$.

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