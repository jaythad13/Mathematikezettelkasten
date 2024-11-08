---
tags:
- alg-geo
- math-176/31
---

For this note, for a field $F$, let $R = F[x_{1}, \dots, x_{n}]$ and $X = \mathbb{A}^n(F)$.

Given a subset $T \subset R$ we already know what its [[Algebraic Geometry --- math-176/notes/Non-singular projective varieties#_definition _ zero set, $Z(I)$|zero set]] is —
$$
Z(T) = \{ p \in X \mid f(p) = 0 \text{ for all } f \in T \}.
$$

The ideal of a subset goes the other way.

##### _definition, proposition:_ ideal of $V$

The ideal of a subset $V \subset X$ is
$$
I(V) = \{ f \in R \mid f(p) = 0 \text{ for all } f \in T \}
$$
and is in fact an [[Abstract Algebra I --- math-171/notes/Ideals and quotients#_definition _ ideal|ideal]].

###### _proof:_

Suppose $f, g \in I(V)$ and $r$ is any element of $R$. We need to show that $f - g \in I(V)$ and $r f \in I(V)$ — that is, they vanish on $V$.

For any point $p \in V$,
$$
(f - g)(p) = f(p) - g(p) = 0 - 0 = 0
$$
and
$$
(rf)(p) = r(p) f(p) = r(p) 0 = 0.
$$

### Properties of ideals

##### _proposition:_ $I$ and $Z$ are contravariant

Suppose $T \subseteq S$ are subsets of $R$ and $V \subseteq W$ are subsets of $X$. Then $Z$ and $I$ reverse the inclusion with $Z(T) \supseteq Z(S)$ and $I(V) \supseteq I(W)$.

###### _proof:_

##### _proposition:_ $I$ and $Z$ turn unions to intersections

Say $T_{1}, T_{2} \subseteq R$ and $V_{1}, V_{2} \subseteq X$. Then $Z(T_{1} \cup T_{2}) = Z(T_{1}) \cap Z(T_{2})$ and $I(V_{1} \cup V_{2}) = I(V_{1}) \cap I(V_{2})$.

###### _proof:_

The results follows just by definition — $p \in Z(T_{1} \cup T_{2})$ are exactly the points $p$ that vanish on both $T_{1}$ and $T_{2}$. $f$ that vanish on all points in $V_{1}$ and all points in $V_{2}$ are exactly the polynomials that are in both $I(V_{1})$ and $I(V_{2})$.

### The Nullstellensatz

It's intuitive that $I$ and $Z$ do opposite things

##### _proposition:_ $I$ and $Z$ are almost inverses

Any subset $V \subseteq X$ is contained in the zero set of its ideal — $V \subseteq Z(I(V))$.

The Nullstellensatz makes this precise.

##### _theorem:_ Hilbert's Nullstellensatz

Say $V = Z(T)$ for some $T \subseteq R$. Then $V = Z(I)$ where $I = (T)$. Further $\sqrt{ I } \subseteq I(V)$ and $I(V) \subseteq \sqrt{I }$ when $F$ is algebraically closed