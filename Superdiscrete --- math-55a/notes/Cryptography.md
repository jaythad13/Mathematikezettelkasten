---
tags:
- math-55A
- nt
- crypt
---

There's an unbreakable code! It's white noise!

Just add some random bits to your message $\mod 2$ (flip some random bits). Tell the recipient what bits you flipped. As long as you use a different key each time, your message is indecipherable. This has the obvious problem that it isn't secure to human vulnerabilities - if the key becomes public you're done.

Public key cryptography relies on doing $M \to^k C$ with a public key $k$ such that it has hard to find $k^{-1}$ (which allows you to do $C \to^{k^{-1}} M$) without some extra information.

The one inverse that we know is hard to do is factoring a product of two large primes.

### RSA public key cryptography

A bank publishes two (say, $2000$-digit) numbers $n$ and $e$ ($e$ for encipher). It keeps $d$ (for decipher) private.

We convert our message $M$ to a number less than $n$ (say by converting each letter to two numbers, but other things could work too).

We compute $c = M^e \mod n$ and send it to the bank.

The bank computes $c^d \mod n$ which magically produces $M$ again.

How does this work?

The bank picks two primes $p$ and $q$ and sets $n = pq$.

Then it computes $\phi(n) = \phi(pq) = \phi(p) \phi(q) = (p - 1)(q - 1)$ and picks $d$ such that $\gcd(d, \phi(n)) = 1$ (we can do this by randomly picking $d$ because the probability of coprimality is $\frac{6}{\pi^2}$).

By [[Superdiscrete --- math-55A/notes/Dividing integers - basic number theory#_theorem _ Bezout's theorem|Bezout's theorem]] we have positive $e, f$ such that 
$$
de - \phi(n)f = 1
$$
(that is, $d$ and $e$ are inverses $\mod \phi(n)$).

##### _theorem:_ RSA works

For $n$, $d$ and $e$ chosen as described, for
$$
c = M^e \mod n
$$
then
$$
M = c^d \mod n.
$$
###### _proof:_

Note that it's enough to show that 
$$
c^d \mod n \equiv M \mod n
$$
because we know $0 \le M < n$.

Note again, obviously
$$
c = M^e \mod n \equiv M^e \mod n
$$
and thus,
$$
c^d \equiv M^{de} \mod n
$$
But $de - \phi(n)f = 1$. Then
$$
M^{de} = M M^{\phi(n)f} = M (M^{\phi(n)})^f \equiv M \times 1^f \equiv M \mod n
$$
as long as we can apply [[Superdiscrete --- math-55A/notes/Modular arithmetic#_theorem _ Euler's theorem|Euler's theorem]], that is as long as $\gcd(M, n) = 1$. This is very likely because we would have to have $p \mid M$ or $q \mid M$ which has the very small probability $\frac{1}{p} + \frac{1}{q}$ for large primes. 