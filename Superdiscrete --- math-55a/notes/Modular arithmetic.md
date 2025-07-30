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

If $a \equiv b \mod m$ and $b \equiv c \mod m$, then we have $a - b$ and $b - c$ divisible by $m$, which then, by [[Superdiscrete --- math-55A/notes/Division and Euclid's algorithm#_theorem _ integer combination theorem|integer combination]] gives us $a - c = (a - b) + (b - c)$ is divisible by $m$.

##### _proposition:_ congruence is preserved by addition and multiplication

If $a \equiv b \mod m$ and $c \equiv d \mod m$ then $a + c \equiv b + d \mod m$ and $ac \equiv bd \mod m$.

###### _proof:_

Addition is easy: since we have $a - b$ and $c - d$ divisible by $m$, just add them to get $(a + c) - (b + d)$ divisible by $m$.

$ac - bd = (a - b)c + (c - d)b$ which by [[Superdiscrete --- math-55A/notes/Division and Euclid's algorithm#_theorem _ integer combination theorem|the integer combination theorem]] is divisible by $m$. Thus, $ac \equiv bd \mod m$.

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

If $ax \equiv ay \mod m$ then $m|a(x - y)$. If $\gcd(a, m) = 1$, then since it [[Superdiscrete --- math-55A/notes/Prime numbers#_theorem _ a divisor must divide something or, the important theorem|must divide something]], $m|(x - y)$ and thus, $x \equiv y \mod m$.

If $ax \equiv ay \mod m$ then we also have $ax \equiv ay \mod \frac{m}{\gcd(a, m)}$. Since $a$ is co-prime to that, the previous result gives us $x \equiv y \mod \frac{m}{\gcd(a, m)}$.

##### _definition:_ multiplicative inverses $\mod m$

An integer $a$ has a multiplicative inverse $b$ $\mod m$ if there exists an integer $b$ such that $ab \equiv 1 \mod m$.

##### _theorem:_ coprime $a, m$ give us multiplicative inverses

$\gcd(a, m) = 1$ if and only if $a$ has a unique multiplicative inverse $\mod m$.

###### _proof sketch:_

Just do the algebra after [[Superdiscrete --- math-55A/notes/Division and Euclid's algorithm#_theorem _ Bezout's theorem|Bezout's theorem]]. 

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