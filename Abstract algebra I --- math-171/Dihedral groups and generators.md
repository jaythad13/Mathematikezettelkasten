---
tags:
- alg
- math-171
lecture:
 - math-171-2
 - math-171-3
---

### Emergent structure on groups

Recall the [[Motivating groups#_definition _ group|definition of a group]] from last time. It turns out that these limited axioms determine a lot of other things about a group — the group has some "emergent structure". We leave the proofs because they're kind of trivial (except the last one).

##### _proposition:_ the identity is unique

For a group $G$, if $e$ and $f$ are identities in $G$, $e = f$.

##### _proposition:_ the inverse is unique

For a group $G$, if $b$ and $c$ are inverses of $a$, then $b = c$.

##### _proposition:_ the inverse is an involution

For a group $G$ and $a \in G$, $(a^{-1})^{-1} = a$.

##### _proposition:_ the inverse of a product

For a group $G$ and $a, b \in G$ we have $(ab)^{-1} = a^{-1} b^{-1}$

##### _proposition:_ the generalised associative law

For a group $G$ and $a_{1}, \dots, a_{n} \in G$, the product $a_{1} \cdots a_{n}$ is uniquely determined.

### The dihedral group

In the light of this structure, it's easier to see why we would care about groups. But we still haven't seen what we mean by "groups encode symmetries". The following is a very compelling example.

##### _definition:_ symmetry of a regular polygon

A symmetry of a regular $n$-gon with vertices $v_{1} \dots v_{n}$ is a rigid motion of the $n$-gon in $3$-space, such that at its conclusion, the $n$-gon can still cover itself (even if the vertices are no longer in the same place).

Note that each symmetry is sort of an "equivalence class" on the set of all ways to achieve that symmetry. For example, we don't think of the two different paths below as different (although we have broken down one of the paths into two steps that are symmetries in their own right).

![[S2_symmetryExample.jpeg]]

Note that each symmetry of a regular polygon can be thought of as a permutation of its vertices. Obviously, not all of the permutations are symmetries (for $n > 4$ we can't have $v_{1}$ and $v_{3}$ adjacent). Since there are finitely many permutations of $n$ vertices, there are fewer, and also finitely many symmetries of a square.

Also note that there is a sensible notion of composing symmetries — if you have some symmetries $g_{1}, g_{2}$, then you can create a composed symmetry $g_{1} g_{2}$ by doing $g_{2}$ and then $g_{1}$. For example, exactly what we did above in the two-step path! This is a binary operation! 

Since each of these is a permutation and we can think of the binary operation as composing them, we get associativity too! Function composition is associative! Another way to think of this is that in real life doing things is associative.

Finally, there are inverses! Just do the same thing in reverse!

##### _proposition:_ the symmetries of a polygon are a group

##### _proof:_

See above!

A natural question is, how many are there?

For small $n$ we can do this manually.

##### _example:_ counting the symmetries of a square

Note that we can send $v_{1}$ to any other vertex. Given where $v_{1}$ goes, there are only two places $v_{2}$ can go — on either side of $v_{1}$. Then the rest are determined. Thus, there are $8$ symmetries of the square.

If we think of $e$ as doing nothing, $r$ as rotating clockwise by $\frac{\pi}{2}$, and $s$ as flipping over the central line, then we have the following distinct symmetries:
$$
\{ e, r, r^2, r^3, s, sr, s r^2, s r^3 \}
$$
Specifically, we know these are all distinct because in the first four, $v_{1}$ is in all different positions and the vertices are labeled clockwise, and in the last four, $v_{1}$ is in all different positions and the vertices are labeled counterclockwise.

##### _definition:_ the dihedral group

The dihedral group of order $2n$, $D_{2n}$ is the group of symmetries of a regular $n$-gon.

##### _proposition:_ the structure of a dihedral group

1) $D_{2n} = \{ 1, r, \dots r^{n - 1}, s, s r, \dots s r^{n - 1} \}$, where $r$ is rotation by $\frac{2\pi}{n}$ and $s$ is flipping about the central axis.
2) $r^n = 1$
3) $s \neq r^j$ for any integer $j$.
4) $s r^j = r^{-j} s$ — that is, rotating clockwise and then flipping is the same as flipping and then rotating counterclockwise.

This is an example of a generator.

### Generators

Generators are like the a spanning list of a group, sort of.

##### _definition:_ generator

If $S \subset G$, for a group $G$, we say that $S$ generates $G$, and its elements are generators, if every $g \in G$ can be given by
$$
g = \prod_{s \in S} s
$$
where every $s$ can be repeated any number of times.

If $S$ is finite, we can write this as $G = \left< s_{1}, \dots s_{n} \right>$.


Note that we don't always need arbitrary products — we don't need to consider $r^m$ with $m > n$ for the dihedral group $D_{2n}$ since we have the equation $r^n = 1$. Similarly, the flip and rotate/rotate opposite and flip rule helps us minimise things.

##### _definition:_ relation

The equations that the generators of a group satisfy are called relations.

##### _definition:_ presentation

The generators of a group, with relations that generate all of the relations between them are a presentation of a group.

A natural question to ask then is how much you can tell about a group just from its presentation. It turns out to be a lot, but not everything, and there are some finicky cases. A nice case is the following

##### _example:_ a group given completely by its presentation

We've spoiled the ending already, but consider the group
$$
G = \left< a, b, c \vert abc = a^2 = b^2 = c^2 = 1  \right> 
$$
where $1$ is the identity.

Note that we can get rid of any one of the elements, say for convenience, $c$. This is because $abc = c^2$ allows us to cancel out $c$ and get $c = ab$. Then
$$
G = \left< a, b \vert (ab)^2 = a^2 = b^2 = 1 \right>.
$$
Note that $a$ and $b$ commute since cancelling $a$ in $a^2 = (ab)^2$ gives us $a = bab$ and thus, $ba = bbab = ab$. 

Then since they commute, we can write every string of $a$s and $bs$ as $a^m b^n$ for integers $m, n$ and then reduce modulo two until we get $a^m b^n$ where $m, n \in \{ 0, 1 \}$. Since all members of $G$ can be written as a string of $a$s and $b$s, we can reduce all of them to this form, and thus,
$$
G = \{ 1, a, b, ab \}.
$$