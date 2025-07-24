---
tags:
- math-171/16x
- math-171/17x
- alg
---

Sylow's theorem is a "sharp" partial converse to [[Abstract algebra --- math-171/notes/Lagrange's theorem#_theorem _ Lagrange's theorem|Lagrange's theorem]]. It isn't just true that there exists some group $G$ with $d$ not a prime power dividing $\lvert G \rvert$ and no subgroup of order $d$ [[Abstract algebra --- math-171/notes/Lagrange's theorem#_counterexample _ the converse of Lagrange's theorem is false|as we showed]]. The stronger statement that for every non-prime power $d$, there is a group $G$ with $d \mid G$ and no subgroup of order $d$ holds.[^1]

Even more importantly, Sylow's theorem is instrumental to the classification of finite groups, and are intimately linked with proving simplicity and solvability of groups for Galois theoretic applications!

### Sylow $p$-subgroup

Sylow's theorem rests on classifying special subgroups of prime power order called Sylow $p$-subgroups in terms of their existence, their number $n_{p}$, and congruence properties of their number.

##### _definition:_ $p$-group, $p$-subgroup

A group of order $p^n$ for some prime $p$ is a $p$-group.

Subgroups of a group that are $p$-groups are $p$-subgroups.

A Sylow $p$-subgroup is a "maximal" $p$-subgroup in the following sense

##### _definition:_ Sylow $p$-subgroups, $\operatorname{Syl}_{p} G$, $n_{p}$

If $G$ is a group of order $p^a m$, with prime $p \nmid m$, then a subgroup of $G$ of order $p^a$ is a Sylow $p$-subgroup of $G$.

We write $\operatorname{Syl}_{p} G$ for the set of Sylow $p$-subgroups of $G$ and $n_{p}$ for $\lvert \operatorname{Syl}_{p} G \rvert$.

### Consequences of Sylow's theorem

Sylow's theorem has important consequences!

![[#_theorem _ Sylow's theorem]]

##### _corollary:_ unique Sylow $p$-subgroups

$P$ is the unique Sylow $p$-subgroup of $G$ if and only if $P$ is [[Abstract algebra --- math-171/notes/Normal subgroups#_definition _ normal subgroups|normal]] in $G$.

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

By [[Abstract algebra --- math-171/notes/Lagrange's theorem#_theorem _ Lagrange's theorem|Lagrange's theorem]] the order of $P \cap Q$ must divide $p$ and $q$. Since they are distinct primes, the order must be $1$.

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

We have seen the action $G \circlearrowright G$ (in particular, by [[Abstract algebra --- math-171/notes/The class equation#$G$ acting on itself by conjugation|conjugation]]. Here we will need consider the action of $G$ on a set of subsets. In particular, if $X$ is a set of subgroups of $G$, consider the action of $G$ on $X$ by left multiplication
$$
g \cdot H = g H
$$
and by conjugation
$$
g \cdot H = g H g^{-1} = \{ g h g^{-1} \mid h \in H \}
$$
for any subgroup $H \le G$. 

Note here that two subgroups are conjugate — $H = g K g^{-1}$ if they're in the same orbit under this action of $G$.

Using this group action, we will show Sylow's theorem as a series of lemmas.

##### _theorem:_ Sylow's theorem

Let $G$ be a finite group of order $p^n m$ where $p$ is prime and $p$ doesn't divide $m$. Then
1) $n_{p} \equiv 1 \pmod p$. In particular $n_{p} \neq 0$, so a Sylow $p$-subgroup exists.
2) For any Sylow $p$-subgroup, every $p$-subgroup of $G$ is contained in a conjugate of the Sylow $p$-subgroup. In particular, any two Sylow $p$-subgroups are conjugate, and thus isomorphic.
3) $n_{p}$ is the index of the normaliser of any Sylow $p$-subgroup, and thus, divides $m$. 

##### _lemma:_ a Sylow $p$-subgroup exists

###### _proof:_ 

Let $X$ be the set of all subsets of size $p^n$. By Lucas' theorem in number theory
$$
\lvert X \rvert = \binom{p^n m}{p^n} \not \equiv 0 \pmod{p}.
$$

Let $G$ act on $X$ by left multiplication — $g \cdot H = gH = \{ gh \mid h \in H \}$. Consider $\mathcal{O}$, an orbit of size not divisible by $p$. Since $p \nmid \lvert X \rvert$, there must be at least one such orbit. Consider $S \in \mathcal{O}$ and its stabiliser $H = \operatorname{stab}_{G}(S)$. By the [[Abstract algebra --- math-171/notes/Group actions#_theorem _ the orbit-stabiliser theorem|orbit-stabiliser theorem]], $H$ has order $\lvert G \rvert / \lvert \mathcal{O} \rvert$ which is still divisible by $p^n$ (since $p$ does not divide $\mathcal{O}$).

Now consider the action of $H$ on $S$ by left multiplication. Just by the definition of left multiplication, $\operatorname{stab}_{H}(s) = \{ 1 \}$ for any $s \in S$. Thus, (again by the orbit-stabiliser theorem) all the orbits of the action have the same size — $\lvert H \rvert / \lvert \operatorname{stab}_{H}(s) \rvert  = \lvert H \rvert$. Since the orbits partition the set, $\lvert H \rvert$ must divide $\lvert S \rvert = p^n$. But then $\lvert H \rvert = p^n$ since it divides and is divisible by it. That is, $H$ is a Sylow $p$-subgroup.

##### _lemma:_ any $p$-subgroup is contained in a conjugate

If $P$ is a Sylow $p$-subgroup and $Q$ is a $p$-subgroup, then $Q \subset g P g^{-1}$ for some $g \in G$.

###### _proof:_

Consider the action of $Q$ on all [[Abstract algebra --- math-171/notes/Fibres and quotients#_definition _ cosets|cosets]] of $P$ by left multiplication. Notice that since $\lvert Q \rvert = p^n$ and any orbit has size dividing $\lvert Q \rvert$ (by the orbit-stabiliser theorem) any orbit has size $p^a$ or $1$. The number of cosets is $m$, not divisible by $p$, so not all orbits are divisible by $p$. Thus, there is some orbit that is just one element — there is a fixed point $g P$ with $q g P = g P$. Thus, $q P = g P g^{-1}$, and thus, $Q \subset q P = g P g^{-1}$.

##### _corollary:_ any two Sylow $p$-subgroups are conjugate

###### _proof:_

Since conjugation is also an [[Abstract algebra --- math-171/notes/Group automorphisms and automorphism groups#_proposition _ inner automorphisms are actually automorphisms|(inner) automorphism]], $\lvert g P g^{-1} \rvert = \lvert P \rvert$. But then since $\lvert Q \rvert = \lvert P \rvert = p^n$, we have $\lvert Q \rvert = \lvert g P g^{-1} \rvert$ and $Q \subset g P g^{-1}$. Thus, $Q = g P g^{-1}$.

##### _lemma:_ fixed points of $P$ conjugating Sylow $p$-subgroups

The action of $P$ on the set of all Sylow $p$-subgroups by conjugation has only one fixed point.

###### _proof:_

We claim $P$ is the only fixed point of this action. Suppose $Q$ is a fixed point of the action giving $p Q p ^{-1} = Q$ for any $p \in P$. Thus, the [[Abstract algebra --- math-171/notes/Centralisers, centre, and normalisers#_definition _ normaliser, $N_{G}(A)$|normaliser]] of $Q$ contains all $p \in P$ (as well as all $q \in Q$). But these are both Sylow $p$-subgroups of $N_{G}(Q)$ (they have to be $p$-subgroups of maximal size since they are maximal in $G$). But then $P = g Q g^{-1}$ for some $g \in N_{G}(Q)$ and since $g \in N_{G}(Q)$, this just means $P = Q$.

##### _lemma:_ fixed points correspond to Sylow $p$-subgroups

$n_{p} \pmod p$ is the number of fixed points of the action of a Sylow $p$-subgroup $P$ on $\operatorname{Syl}_{p} G$ by conjugation.

###### _proof:_

The orbits of the action of $P$ on $\operatorname{Syl}_{p} G$ by conjugation are all divisible by $p$, except for the orbits corresponding to fixed points which have size $1$. Thus,
$$
\begin{align}
n_{p} & = \sum_{\text{non-trivial orbits}} \lvert \mathcal{O}_{G}(x) \rvert + \sum_{\text{trivial-orbits}} \lvert \mathcal{O}_{G}(x) \rvert \\
 & = \sum_{\text{non-trivial orbits}} p^{a_{i}} + \sum_{\text{trivial orbits}} 1 \\
 & \equiv \operatorname{fix}_{\operatorname{Syl}_{p} G} P \pmod p.
\end{align}
$$

##### _lemma:_ 

$n_{p}$ divides $m$.

###### _proof:_

Since $n_{p} \equiv 1 \pmod p$, we just need to show $n_{p}$ divides $\lvert G \rvert = p^n m$. Considering the action of $G$ on $\operatorname{Syl}_{p} G$ by conjugation, we see that there is only one orbit (of size $n_{p}$). By the orbit-stabiliser theorem, then $n_{p}$ divides $\lvert G \rvert$.

[^1]: McCarthy, D. Sylow's theorem is a sharp partial converse to Lagrange's theorem. _Math Z_ **113**, 383–384 (1970). https://doi.org/10.1007/BF01110508