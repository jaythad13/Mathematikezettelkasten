---
tags:
- math-189AA/4
- comm-alg
---

[[Abstract algebra --- math-171/notes/Rings#_definition _ unit|Unit]]-ness does not play nicely with addition. For example, in $\mathbb{F}[x]$ or $\mathbb{Z} / (20)$, we can find examples of any choice of units and non-units adding to units and non-units. For example, $4 + 5 = 9$ is the sum of non-units that is a unit in $\mathbb{Z} / (20)$.

We want a predictable algebraic structure that describes unitness. The Jacobson radical is a solution to this problem (partially motivated by the idea of the [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_definition _ nilradical|nilradical]]). Recall that all non-units are contained in a unique maximal ideal (by Zorn's lemma containing the corresponding [[Abstract algebra --- math-171/notes/Ideals and quotients#_definition _ principal ideal|principal ideals]]). Thus, we can reframe this as a problem of how maximal ideals play with addition outside of them. We solve the problem by considering the intersection of all ideals.

##### _definition:_ Jacobson radical

The **Jacobson radical** $\mathfrak{R}_{A}$ of a ring $A$ is the intersection of all [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ maximal ideal|maximal ideals]] of $A$.

---

##### _proposition:_ characterising the Jacobson radical

$x \in \mathfrak{R}_{A}$ if and only if $1 - a x$ is a unit in $A$ for every $a \in A$.

---

Thus, in the situation that the ring has only one maximal ideal (the case of a [[Local rings|local ring]]) we have the nice picture that all the non-units are in the maximal ideal $\mathfrak{m}$ and all the units are in $A \setminus \mathfrak{m}$. This rests on the fact that $\mathfrak{m} = \mathfrak{R}$. Then any $a \in A \setminus \mathfrak{m}$ has $b \in A \setminus \mathfrak{m}$ such that $ab + \mathfrak{m} = 1 + \mathfrak{m}$ in the quotient field. Thus, $ab = 1 + x$ with $x \in \mathfrak{m}$ and is a unit. Thus, $a$ is a unit.