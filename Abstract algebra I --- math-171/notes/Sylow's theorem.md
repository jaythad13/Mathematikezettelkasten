---
tags:
- math-171/16x
- math-171/17x
- alg
---

Sylow's theorem is a "sharp" partial converse to [[Abstract Algebra I --- math-171/notes/Lagrange's theorem#_theorem _ Lagrange's theorem|Lagrange's theorem]]. It isn't just true that there exists some group $G$ with $d$ not a prime power dividing $\lvert G \rvert$ and no subgroup of order $d$ [[Abstract Algebra I --- math-171/notes/Lagrange's theorem#_counterexample _ the converse of Lagrange's theorem is false|as we showed]]. The stronger statement that for every non-prime power $d$, there is a group $G$ with $d \mid G$ and no subgroup of order $d$ holds.[^1]

Even more importantly, Sylow's theorem is instrumental to the classification of finite groups, and are intimately linked with proving simplicity and solvability of groups for Galois theoretic applications!

### Sylow $p$-subgroup

Sylow's theorem rests on classifying special subgroups of prime power order called Sylow $p$-subgroups in terms of their existence, their number $n_{p}$, and congruence properties of their number.

##### _definition:_ $p$-group, $p$-subgroup

A group of order $p^a$ for some prime $p$ is a $p$-group.

Subgroups of a group that are $p$-groups are $p$-subgroups.

A Sylow $p$-subgroup is a "maximal" $p$-subgroup in the following sense

##### _definition:_ Sylow $p$-subgroups, $\operatorname{Syl}_{p} G$, $n_{p}$

If $G$ is a group of order $p^a m$, with prime $p \nmid m$, then a subgroup of $G$ of order $p^a$ is a Sylow $p$-subgroup of $G$.

We write $\operatorname{Syl}_{p} G$ for the set of Sylow $p$-subgroups of $G$ and $n_{p}$ for $\lvert \operatorname{Syl}_{p} G \rvert$.

### Consequences of Sylow's theorem

Sylow's theorem has important consequences!

![[#_theorem _ Sylow's theorem]]

##### _corollary:_ unique Sylow $p$-subgroups

$P$ is the unique Sylow $p$-subgroup of $G$ if and only if $P$ is [[Abstract Algebra I --- math-171/notes/Normal subgroups#_definition _ normal subgroups|normal]] in $G$.

###### _proof:_

This follows from the conjugacy condition in Sylow's theorem. If $P$ is normal in $G$, then every conjugate of $P$ is just $P$, and thus, the Sylow $p$-subgroups, which are conjugates of $P$, are just $P$.

Conversely, if $P$ is the unique Sylow $p$-subgroup, it cannot have any distinct conjugates, so $g P g^{-1} \subset P$ always. That is, $P$ is normal.

##### _corollary:_ product of primes

If $\lvert G \rvert = pq$ is the product of two distinct primes $p < q$, then $G$ has a normal subgroup of order $q$.

###### _proof sketch:_

$n_{q} \mid p$ and thus, $n_{q} \le p < q$, and $n_{q} \equiv 1 \pmod q$, so $n_{q} = 1$ is the only possible value. Thus, the Sylow $q$-subgroup is normal.

##### _corollary:_ Sylow $p$-subgroups of abelian groups

If $G$ is an abelian group, $n_{p} = 1$ for all primes $p$ dividing $\lvert G \rvert$.

###### _proof:_

All subgroups of an abelian group are normal and thus, so is each Sylow $p$-subgroup. Thus, $n_{p} = 1$ for each $p$.

##### _corollary:_ Sylow $p$-subgroups of distinct primes have trivial intersection

If $p \neq q$ then Sylow $p$-subgroup $P$ and Sylow $q$-subgroup $Q$ have trivial intersection.

###### _proof:_

By [[Abstract Algebra I --- math-171/notes/Lagrange's theorem#_theorem _ Lagrange's theorem|Lagrange's theorem]] the order of $P \cap Q$ must divide $p$ and $q$. Since they are distinct primes, the order must be $1$.

##### _corollary:_ triple product of primes

If $\lvert G \rvert = pqr$ is the product of three distinct primes, then $G$ must have a normal Sylow subgroup.

###### _proof:_

We use the previous corollary to show that if $n_{p} = n_{q} = n_{r} = 1$ then $G$ would have more than $pqr$ elements. Suppose, without loss of generality, that $p < q < r$ and for contradiction that all $n_{p}, n_{q}, n_{r} > 1$.

$n_{r}$ must divide $pq$. Also, $n_{r} = 1 + k r$ with $k \neq 0$ (by our hypothesis). Since $1 + kr > p, q$ for positive $k$, $n_{r}$ doesn't divide $p$ nor $q$. Thus, [[Superdiscrete --- math-55A/notes/Euclid's algorithm and primes#_theorem _ a divisor must divide something or, the important theorem|it must have non-trivial common divisors with both]]. Since they are primes, this gives us $p \mid n_{r}$ and $q \mid n_{r}$, and thus, $pq \mid n_{r}$. That is, $n_{r} = pq$. Further, we have $n_{p} \geq 1 + p$ and $n_{q} \geq 1 + q$.

But now, since these Sylow subgroups only have trivial intersection, the total number of distinct elements contained in them is one more than just counting the non-identity elements naively
$$
\begin{align}
1 + n_{p} (p - 1) + n_{q} (q - 1) + n_{r} (r - 1) & = 1 + p^{2} - 1 + q^{2} - 1 + pqr - pq \\
 & = pqr + p^{2} + q^{2} - pq - 1 \\
 & > pqr + p^{2} - 1 \\
 & > pqr
\end{align}
$$
where the first inequality follows because $q > p$ and the second because all primes $p > 1$.

Since this is more elements than there are in the group, we have a contradiction.

### Proving Sylow's theorem

We have seen the action $G \circlearrowright G$ by [[Abstract Algebra I --- math-171/notes/The class equation#$G$ acting on itself by conjugation|conjugation]]. Here we will need consider the action of $G$ on a set of subsets by conjugation. In particular, if $X$ is a set of subgroups of $G$, consider the action of $G$ on $X$ by
$$
g \cdot H = g H g^{-1} = \{ g h g^{-1} \mid h \in H \}
$$
for any subgroup $H \le G$. Note here that two subgroups are conjugate — $H = g K g^{-1}$ if they're in the same orbit under this action of $G$.

Using this group action, we will show Sylow's theorem as a series of lemmas.

##### _theorem:_ Sylow's theorem

Let $G$ be a finite group of order $p^a m$ where $p$ is prime and $p$ doesn't divide $m$. Then
1) $n_{p} \equiv 1 \pmod p$. In particular $n_{p} \neq 0$, so a Sylow $p$-subgroup exists.
2) For any Sylow $p$-subgroup, every $p$-subgroup of $G$ is contained in a conjugate of the Sylow $p$-subgroup. In particular, any two Sylow $p$-subgroups are conjugate, and thus isomorphic.
3) $n_{p}$ is the index of the normaliser of any Sylow $p$-subgroup, and thus, divides $m$. 

##### _lemma:_ a Sylow $p$-subgroup exists

###### _proof:_ 

Let $X$ be the set of all subsets of size $p^n$. By Lucas' theorem in number theory
$$
\lvert X \rvert = \binom{p^n m}{p^n} \not \equiv 0 \pmod{p}.
$$

Let $G$ act on $X$ by left multiplication — $g \cdot H = gH = \{ gh \mid h \in H \}$. Consider $\mathcal{O}$, an orbit of size not divisible by $p$. Since $p \nmid \lvert X \rvert$, there must be at least one such orbit. Consider $S \in \mathcal{O}$ and its stabiliser $H = \operatorname{stab}_{G}(S)$. By the [[Abstract Algebra I --- math-171/notes/Group actions#_theorem _ the orbit-stabiliser theorem|orbit-stabiliser theorem]], $\operatorname{stab}_{G}(S)$ has order $\lvert G \rvert / \lvert \mathcal{O} \rvert$ which is still divisible by $p^n$ (since $p$ does not divide $\mathcal{O}$).

[^1]: McCarthy, D. Sylow's theorem is a sharp partial converse to Lagrange's theorem. _Math Z_ **113**, 383–384 (1970). https://doi.org/10.1007/BF01110508