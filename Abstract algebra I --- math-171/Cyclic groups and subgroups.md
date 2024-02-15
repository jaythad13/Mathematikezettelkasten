---
tags:
- alg
- math-171
lecture:
- math-171-9
---

Cyclic subgroups are the easiest subgroups to deal with — dealing with something like $\left< 3 \right> \le \mathbb Z$ is much easier than dealing with more elements. Here, we will see that when we are dealing with cyclic groups we never need to deal with non-cyclic subgroups. Note that this also makes [[Subgroups#_example _ the lattice of subgroups of $ mathbb{Z} / 6 mathbb{Z}$|calculating lattices of a cyclic group]] easier.

##### _theorem:_ every subgroup of a cyclic group is cyclic

Suppose $G$ is a cyclic subgroup and $H$ is cyclic


This generalises to prove a nice lemma about group orders

##### _lemma:_ the order of an element divides anything else

Let $G$ be a group and let $x \in G$ have finite order $\lvert x \rvert = n$. If $x^m = 1_{G}$, then $n \mid m$.

##### _proof sketch:_

By the division algorithm, if $n \nmid m$, we would have that the remainder $r < n$ gives us $x^r = 1_{G}$ contradicting that $n$ is the least such number.

##### _theorem:_ cyclic groups have subgroups of all divisor orders

Suppose $G$ is cyclic and finite. Then if $d \mid n$ there is a unique subgroup $\left< x^{n/d} \right>$ of order $d$.
