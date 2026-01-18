---
tags:
- rising-sea/5/4
- comm-alg
---

Let $A$ be a ring.

Integral closure is an important concept in both algebraic geometry and algebraic number theory. In algebraic geometry, integrally closed stalks correspond to the concept of [[Algebraic geometry --- rising-sea/notes/Normal and factorial schemes#_definition _ normal schemes|normality]].

##### _definition:_ integrally closed domain

An [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]] $A$ is **integrally closed** if the following implication holds. If $p \in A[x]$ is a monic polynomial and $a \in Q(A)$ has $p(a) = 0$, then $a \in A \subseteq Q(A)$.

---

One (technical, practical) reason that we like integral closure is that it behaves well under localisation.

##### _proposition:_ localisations of integrally closed domains are integrally closed

Suppose $A$ is an integrally closed domain and $S$ is a multiplicative subset not containing $0$. Then $S^{-1} A$ is an integrally closed domain.

###### _proof:_

Suppose the monic polynomial $p(x) = x^n + (a_{n - 1} / s_{n - 1}) x^{n - 1} + \dots + a_{0} / s_{0} \in S^{-1} A[x]$ has a root $\alpha \in Q(S^{-1} A) = Q(A)$. Let $s = s_{0} s_{1} \cdots s_{n - 1}$. Since $\alpha$ is a root, we can write $s^n p(\alpha) = 0$. Moving all the $s^j$ inside the powers appropriately, we get that $s \alpha$ is a root of a monic polynomial in $A[x]$.
$$
(s \alpha)^n + (a_{n - 1} s /s_{n - 1}) (s \alpha)^{n - 1} + \dots + (a_{1} s^{n - 1} / s_{1}) (s \alpha) + a_{0} s^n/ s_{0} = 0.
$$
Thus, $s \alpha \in A$, and $\alpha \in S^{-1} A$.

---

In fact, when we are checking localisation at primes, we only need to check localisations at maximal ideals. This is both useful to us as a fact on its own and in that it gives us an excuse to introduce the ideal of denominators.

![[Commutative algebra --- math-189AA/notes/Localisation of a ring#_definition _ ideal of denominators|Localisation of a ring]]

##### _proposition:_ integral closure is (maximal) stalk-local

For an integral domain $A$, the following are equivalent.
1) $A$ is integrally closed.
2) $A_{\mathfrak{p}}$ is integrally closed for all prime ideals $\mathfrak{p} \subseteq A$.
3) $A_{\mathfrak{m}}$ is integrally closed for all maximal ideals $\mathfrak{m} \subseteq A$.

###### _proof:_

Clearly (1) implies (2) implies (3) by the previous result and the fact that all maximal ideals are prime. We are only left to show (3) implies (1). We will show the contrapositive.

Suppose $A$ is not integrally closed — there is some $\alpha \in Q(A) \setminus A$ and some monic polynomial $p \in A[x]$ such that $p(\alpha) = 0$. Consider the ideal of denominators of $\alpha$. Since $\alpha$ is not in $A$, $\mathfrak{i}_{\alpha / \cdot}$ does not contain $1$. Thus, there is a maximal ideal $\mathfrak{m}$ containing it. $A_{\mathfrak{m}}$ does not contain $\alpha$, since none of the denominators of $\alpha$ are units in $A_{\mathfrak{m}}$. Thus, $p \in A_{\mathfrak{m}}[x]$ is a monic polynomial with a zero in $Q(A_{\mathfrak{m}}) \setminus A_{\mathfrak{m}}$.

---

##### _example:_ the rational root theorem, or $\mathbb{Z}$ is integrally closed

Suppose $p(x) = \sum_{i = 0}^k a_{i} x^i \in \mathbb{Z}[x]$ and $\alpha \in \mathbb{Q} \setminus \mathbb{Z}$ is a root — $p(\alpha) = 0$. Write $\alpha = m / n$ in least terms. Then there must be some prime $p$ dividing $n$ and not dividing $m$. Write $n = p d$. Then
$$
a_{k} (m / n)^k + \dots + a_{1} (m / n) + a_{0} = 0
$$
can be rewritten as
$$
a_{k} = \frac{\sum_{i = 0}^{k - 1} a_{i} (m / n)^i}{m^k / n^k} = \frac{\sum_{i = 0}^{k - 1} a_{i} m^i n^{k - i}}{m^k}.
$$
Since the numerator is divisible by $p$ and the denominator isn't, we have $a_{k} \neq 1$, and thus, $p$ is not monic.

---

More generally, this proof works in any [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ unique factorisation domains|unique factorisation domain]] —

##### _proposition:_ UFDs are integrally closed

If $A$ is a unique factorisation domain, it is integrally closed.

---

We can also generalise the example of $\mathbb{Z}$ to the integral closure of $\mathbb{Z}$ in any algebraic extension of $\mathbb{Q}$. These are not necessarily unique factorisation domains.

##### _example:_ quadratic integer rings

Suppose $d$ is a square free integer with $d \equiv 2, 3$ modulo $4$. Then we write $A = \mathbb{Z}[\sqrt{ d }]$ for $\mathbb{Z}[x] / (x^{2} - d)$. Note that $K(\mathbb{Z}[\sqrt{ d }]) = \mathbb{Q}(\sqrt{ d }) = \mathbb{Q}[\sqrt{ d }]$. If $f(x) = x^n + a_{n - 1} x^{n - 1} + \dots + a_{0} \in A[x]$ has a root in $\mathbb{Q}(\sqrt{ d })$, then the root is some $\alpha = {a + b \sqrt{ d }}$ with $a, b \in \mathbb{Q}$. By Galois theory, whenever $\alpha$ is a root of a polynomial, $\overline{\alpha} = {a - b \sqrt{ d }}$ is a root of the same polynomial. Thus, $\alpha + \overline{\alpha} = 2a$ and $\alpha \overline{\alpha} = a^{2} - b^{2} d$ are both in $\mathbb{Z}[\sqrt{ d }]$. In fact, since they contain no $\sqrt{ d }$ term, they are in $\mathbb{Z}$.

If $a \in \mathbb{Z}$, then $b^{2} d \in \mathbb{Z}$. Since $d$ is square free, it cannot cancel out any non-trivial squared part of the denominator of $b^{2}$. Thus, there is none and $b \in \mathbb{Z}$. That is, if $a \in \mathbb{Z}$, then $b \in \mathbb{Z}$ and $\alpha \in \mathbb{Z}[\sqrt{ d }]$.

Suppose $a = n / 2$ for some odd $n$. Thus, $n^{2} / 4 - d b^{2}$ is an integer. Thus, in reduced form $d b^{2}$ has denominator $4$, and again, since $d$ is square free, we get $b = m / 2$ for some odd $m$. Further, $d$ is odd — else $d b^{2}$ would have denominator $2$. Thus, if $d \equiv 2$ we already have $\mathbb{Z}[\sqrt{ d }]$ integrally closed. Else, we can write
$$
\alpha = \frac{1 + \sqrt{ d }}{2} + \frac{n - 1}{2} + \frac{m - 1}{2} \sqrt{ d } \in \frac{1 + \sqrt{ d }}{2} + \mathbb{Z}[\sqrt{ d }].
$$
$(1 + \sqrt{ d })/2$ has trace $1$ and norm $(1 - d) / 4$. Thus, if $\alpha$ is integral over $\mathbb{Z}[\sqrt{ d }]$ with $a = n / 2$, we must have $(1 - d) / 4 \in \mathbb{Z}$ and equivalently, $d \equiv 1$. This also suffices, since $x^{2} - x + (1 - d) / 4 \in \mathbb{Z}[x] \subseteq A[x]$ has $(1 + \sqrt{ d }) / 2$ as a root. Since $\mathbb{Z}\left[ \frac{1 + \sqrt{ d }}{2} \right]$ includes $\mathbb{Z}[\sqrt{ d }]$, any root $\alpha$ must be in $\mathbb{Z}\left[ \frac{1 + \sqrt{ d }}{2} \right]$.

Else, $a \neq n / 2$ and the roots are all contained in $\mathbb{Z}[\sqrt{ d }]$.

---

##### _examples:_ integrally closed rings need not be UFDs

Since $\mathbb{Z}[\sqrt{ -5 }]$ does not have unique factorisation $2 \times 3 = (1 + \sqrt{ -5 })(1 - \sqrt{ -5 })$, this gives an example of an integrally closed domain that doesn't have unique factorisation. 

Our favourite [[Algebraic geometry --- rising-sea/notes/Examples of schemes#_example _ an integrally closed ring that is not a UFD|cone over a smooth quadric surface]] gives us another example.

They are different in that $\operatorname{Spec} \mathbb{Z}[-\sqrt{ 5 }]$ is still factorial but the cone is not.

---

There is also a very specific useful class of examples of integrally closed domains that is very similar.

##### _examples:_ adjoining square roots in UFDs

Suppose $A$ is a [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ unique factorisation domains|unique factorisation domain]] with $2$ invertible, $x \in A$, and $y^{2} - x$ is irreducible in $A[y]$. If $x \in A$ has no repeated prime factors, then $B = A[y] / (y^{2} - x)$ is integrally closed. 

If $x \in A$ has repeated prime factors, then $B$ is not integrally closed. Suppose in particular that $x = p^{2} d$ for some prime $p$. Then 

---

Finally, the following result is useful in extending proving integral closure.

##### _proposition:_ integral closure cannot come from extensions

Suppose $A$ is an $\mathbb{F}$-algebra and $\mathbb{K} / \mathbb{F}$ is field extension. If $A \otimes_{\mathbb{F}} \mathbb{K}$ is integrally clsoed, then so is $A$.

---

Note that the analogous result is not true for UFDs — we will see an $\mathbb{R}$-algebra that becomes a UFD after extension to $\mathbb{C}$.