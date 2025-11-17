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