---
tags:
- alg
- math-171/3
- math-171/4
---

Finite groups are really combinatorial objects! Last time we used combinatorial arguments about generators to learn a little about 

##### _example:_ how to use order arguments about group presentations

Say we have $X_{2n} = \left< x, y \vert x^n = y^2 = 1, xy = yx^2 \right>$. What can we say about this group just from this presentation? Can we estimate its order? Find its elements?

Consider the second relation. Since we have $xy = yx^2$, if there's an $x$ that is followed by $y$s, we can always shift the $x$ to the end, increasing powers along the way (note that by induction $x^n y = y x^{2n}$). Thus, we can always write an element as $y^i x^j$. Formally we can do this by induction on $i + j$.

Since $y^2 = 1$ and $x^n = 1$, we can have at most $2n$ distinct $y^i x^j$. Thus, $\lvert X_{2n} \rvert \le 2n$.

Finally, note that we can get $x = x^4$.
$$
\begin{split}
xy = yx^2 & \implies xy^2 = y x^2 y \\
& \implies xy^2 = y^2 x^4 \\
& \implies x = x^4
\end{split}
$$
Then naturally $\lvert x \rvert \le 3$, and $\lvert X_{2n} \rvert \le 6$ (because all of the elements are $y^i x^j$).

### Group tables

Another sort of combinatorial way to think about groups is a group table. The easiest way to understand is to see an example.

##### _example:_ a nice group table

Recall $G = \left< a, b, c \vert abc = a^2 = b^2 = c^2 = 1  \right>$ from [[Dihedral groups and generators#_example _ a group given completely by its presentation|last time]]. Remembering that this really is just $\{ 1, a, b, ab \}$ and abelian we can write

| - | $1$ | $a$ | $b$ | $ab$ |
| ---- | ---- | ---- | ---- | ---- |
| $1$ | $1$ | $a$ | $b$ | $ab$ |
| $a$ | $a$ | $1$ | $ab$ | $b$ |
| $b$ | $b$ | $ab$ | $1$ | $a$ |
| $ab$ | $ab$ | $b$ | $a$ | $1$ |
Note that we only write $ab$, not $ba$, since $ab = ba$ and we chose to write $ab$ in our set representation of the group.

### Symmetric groups

Recall that we can think of each symmetry in $D_{2n}$ [[Dihedral groups and generators#The dihedral group|as just a permutation]] of $n$ vertices, but not all permutations were a symmetry. If we think about all of the symmetries, without any restrictions to "rigid motions" do they form a group? Yes!

##### _proposition:_ the set of bijections on a set is a group

Given a set $\Omega$, the set of bijections on it $S_{\Omega}$ is a group under function composition.

###### _proof:_

The identity function $\operatorname{id}_{\Omega} : x \mapsto x$ for all $x \in \Omega$ gives us $\operatorname{id}_{\Omega} \circ f = f$ and $f \circ \operatorname{id}_{\Omega} = f$ for any other function $f \in S_{\Omega}$.

Function composition is associative

Since all of the functions are bijections, they all have two sided inverses — $f \circ f^{-1} = f^{-1} \circ f = \operatorname{id}_{\Omega}$.

##### _definition:_ the symmetric group on $\Omega$

Let $\Omega$ be a non-empty set, and let $S_{\Omega}$ be the set of bijections on $\Omega$. $S_{\Omega}$ is the symmetric group on $\Omega$.

##### _abuse of notation:_ $S_{n}$

We write $S_{n}$ for $S_{\mathbb{N}_{n}}$.

##### _example:_ cycle notation

We use cycle notation to denote permutations. For example, the permutation $\sigma$ on $\mathbb{N}_{5}$ notated $(1 \, 3)(2 \, 5 \, 4)$ is given by
$$
\begin{gathered}
1 \mapsto 3 \\
2 \mapsto 5 \\
3 \mapsto 1 \\
4 \mapsto 2 \\
5 \mapsto 4.
\end{gathered}
$$

But why care? Cayley's theorem

##### _theorem:_ Cayley's theorem

Every group $G$ is isomorphic to a subgroup of a symmetric group $S_{G}$ (think of $S_{G}$ as the symmetric group on the underlying set of $G$).

##### _example:_ some permutations in $S_{3}$

$\sigma = (1 \, 2)$, $\tau = (1 \, 3 \, 2)$ have inverses $\sigma^{-1} = (1 \, 2)$ and $\tau^{-1} = (3 \, 1 \, 2)$.

Note that we can write $\tau = (1 \, 3) (2 \, 3) = (1 \, 2) (1 \, 3)$.

Can we write other permutations as a composition of transpositions ($2$-cycles) like this? We can!

##### _proposition:_ every permutation is the composition of transpositions

In general $(a_{1} \, a_{2} \, \dots a_{k}) = (a_{1} \, a_{k}) \dots (a_{1} \, a_{2})$. 

###### _proof sketch:_

Note that on the left side $a_{j} \mapsto a_{j + 1}$ except for $a_{k}$ which maps to $a_{1}$.

On the right side we can show this by induction on $k$. If $k$ is $2$, then $(a_{1}, a_{2})$ is the desired transposition. 

Suppose it's true for $k$. Notice that
$$
(a_{1}  \, a_{2} \, a_{3} \, \dots a_{k + 1}) = (a_{1} \, a_{3} \, \dots a_{k + 1})(a_{1} \, a_{2})
$$
and then it follows from the induction hypothesis that
$$
(a_{1} \, a_{3} \, \dots a_{k + 1})(a_{1} \, a_{2}) = (a_{1} \, a_{k + 1})(a_{1} \, a_{k}) \dots (a_{1} \, a_{3})(a_{1} \, a_{2}).
$$

##### _example:_ some more permutation compositions

and also a proof that $S_{3}$ is not abelian.

$\sigma \circ \tau = (1 \, 3)$ and $\tau \circ \sigma = (2 \, 3)$.

##### _example:_ the order of a composition of disjoint cycles

It's generally true that the order of a composition of disjoint cycles is just the least common multiple of the lengths of its cycles.

### Some basic properties of $S_{n}$

We state some basic facts about $S_{n}$ without proof (for now).

##### _proposition:_ $S_{n}$ is the number of ways to rearrange $n$ things

$\lvert S_{n} \rvert = n!$

##### _proposition:_ $S_{n}$ is non-abelian for all $n \ge 3$

##### _proposition:_ disjoint cycles commute

##### _proposition:_ the order of a permutation

The order of a permutation is the least common multiple of the lengths of the disjoint cycles in its cycle decompositions.

##### _proposition:_ $S_{n}$ is generated by all the obvious transpositions

$S_{n} = \left< (1 \, 2), (2 \, 3), \dots, ((n - 1) \, n) \right>$