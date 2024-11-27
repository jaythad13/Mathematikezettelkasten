---
tags:
- math-171/16x
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

$P$ is the unique Sylow $p$-subgroup of $G$ if and only if $P$ is normal in $G$.

###### _proof:_

This follows from the conjugacy condition in Sylow's theorem. If $P$ is normal in $G$, then every conjugate of $P$ is just $P$, and thus, the Sylow $p$-subgroups which are conjugates of $P$ are just $P$. Conversely, if $P$ is the unique Sylow $p$-subgroup, it cannot have any distinct conjugates as those would be subgroups groups of the same prime power order — also Sylow $p$-subgroups

### Proving Sylow's theorem

Sylow's theorem will follow from a series of lemmas.

##### _theorem:_ Sylow's theorem

Let $G$ be a finite group of order $p^a m$ where $p$ is prime. Then
1) $n_{p} \equiv 1 \pmod p$. In particular $n_{p} \neq 0$, so a Sylow $p$-subgroup exists.
2) For any Sylow $p$-subgroup, every $p$-subgroup of $G$ is contained in a conjugate of the Sylow $p$-subgroup. In particular, any two Sylow $p$-subgroups are conjugate, and thus isomorphic.
3) $n_{p}$ is the index of the normaliser of any Sylow $p$-subgroup, and thus, divides $m$. 


[^1]: McCarthy, D. Sylow's theorem is a sharp partial converse to Lagrange's theorem. _Math Z_ **113**, 383–384 (1970). https://doi.org/10.1007/BF01110508