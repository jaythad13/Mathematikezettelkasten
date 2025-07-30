---
tags:
- alg
- math-139/27
---

We can in fact extend our ideas for the Fourier analysis [[Fourier analysis --- math-139/notes/Fourier analysis on the cyclic group|on the cyclic group]] to finite abelian groups in general. Recall the definition of a group and an abelian group —

![[Abstract algebra --- math-171/notes/Groups, and why you should care#_definition _ group, identity, inverse|Groups, and why you should care]]

![[Abstract algebra --- math-171/notes/Groups, and why you should care#_definition _ abelian group, commutative group|Groups, and why you should care]]

##### _example:_ the group of units in $\mathbb{Z} / n \mathbb{Z}$

Recall also that all integer residues modulo $n$ that are coprime to $n$ are invertible in $\mathbb{Z} / n \mathbb{Z}$ (by [[Superdiscrete --- math-55A/notes/Dividing integers - basic number theory#_theorem _ Bezout's theorem|Bezout's theorem]]). Thus, under multiplication modulo $n$ they form $\mathbb{Z} / n \mathbb{Z}^*$, the abelian group of [[Abstract algebra --- math-171/notes/Rings#_definition _ unit|units]] in $\mathbb{Z} / n \mathbb{Z}$.

Recall also the definition of a group homomorphism —
![[Abstract algebra --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|Group homomorphisms]]

Finally, the structure theorem allows us to decompose any finite abelian group into the direct product of concrete groups that we understand —

##### _theorem:_ structure theorem for finite abelian groups

Any finite abelian group is isomorphic to the direct product of groups $\mathbb{Z} / n \mathbb{Z}$ (with possibly different $n$)

##### _example:_ decomposition of $\mathbb{Z} / 8 \mathbb{Z}^*$

$\mathbb{Z} / 8 \mathbb{Z}^*$ consists of the units $1, 3, 5, 7$ in $8$. Since $3 \times 5 \equiv 7 \pmod 8$, $3 \times 7 \equiv 5$ and $5 \times 7 \equiv 3$, either of the maps $\mathbb{Z} / 8 \mathbb{Z}^*$ with $1 \mapsto (0, 0)$ and $7 \mapsto (1, 1)$ are group [[Abstract algebra --- math-171/notes/Group isomorphisms#_definition _ group isomorphism, isomorphic|isomorphisms]].
