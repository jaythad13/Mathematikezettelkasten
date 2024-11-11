---
tags:
- math-176/32
- alg-geo
---

What did we mean when we said [[Algebraic Geometry --- math-176/notes/Non-singular projective varieties#_definition _ non-singular projective variety|a variety has to be irreducible]]?

##### _proposition:_ $V$ irreducible implies $I(V)$ prime

Let $F$ be a field and denote $R = F[x_{1}, \dots, x_{n}]$, and $X = \mathbb{A}^n(F)$. The following are equivalent for a [[Algebraic Geometry --- math-176/notes/The Zariski topology#_definition _ the Zariski topology|Zariski closed]] $V \subseteq X$.
1) We cannot write $V$ as the union of closed proper subsets — $V$ cannot be written as $V_{1} \cup V_{2}$ with $V_{k} \neq V$ and $V_{k} = V \cap Z(T_{k})$ for some $T_{k} \subseteq R$.
2) $I(V)$ is a prime ideal in $R$ (and the affine coordinate ring of $V$, $\mathcal{O}(V) = R / I(V)$ is an integral domain).

###### _proof:_

Suppose $V$ cannot be written as the union of closed proper subsets. Suppose $f g \in I(V)$. We need to show that both $f, g \in I(V)$. Consider $p \in V$. Since $(fg)(p) = 0$, either $f(p) = 0$ or $g(p) = 0$.

Note that $Z(f) \cup Z(g) = Z(fg)$. So consider $V_{1} = V \cap Z(f)$ and $V_{2} = V \cap Z(g)$. Clearly $V_{1}, V_{2}$ are closed subsets that have union
$$
V \cap (Z(f) \cup Z(g) ) = V \cap Z(fg) = V.
$$
By our assumption, $V_{1}$ and $V_{2}$ cannot both be proper subsets of $V$. Without loss of generality assume $V_{1} = V$. Thus, $Z(f) = V$. That is, $f$ vanishes everywhere on $V$ and is in $I(V)$. Thus, $I(V)$ is prime.

Note that since $V$ is closed, its [[Algebraic Geometry --- math-176/notes/The Zariski topology|Zariski closure]] is just itself — $V = Z(I(V))$. Suppose there are proper closed subsets whose union is $V$. Then [[Algebraic Geometry --- math-176/notes/Hilbert's Nullstellensatz#_proposition _ $I$ and $Z$ turn unions to intersections|the unions are inverted to give]] $I(V) = I(V_{1}) \cap I(V_{2})$ for proper closed subsets of $I(V)$. But recall that the product of ideals is contained in their intersection, and so by choosing $a_{1} \in I(V_{1}) \setminus I(V)$ and $a_{2} \in I(V_{2}) \setminus I(V)$ we get $a_{1} a_{2} \in I(V_{1}) \cap I(V_{2}) = I(V)$ so $I(V)$ is not prime.

So we have that a geometric sense of irreducibility corresponds to an algebraic sense.

##### _example:_

If $V = \mathbb{A}^n(F)$, the coordinate ring is just $F[x_{1}, \dots, x_{n}]$.