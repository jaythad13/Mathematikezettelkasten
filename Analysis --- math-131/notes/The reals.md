---
tags:
- math-131/2
- math-131/3
- anal
---

There are a lot of constructions one can make of $\mathbb{R}$, but the essential property they all share is that $\mathbb{R}$ is the smallest ordered field with the least upper bound property. This is the essential property that allows things like the intermediate value theorem to be true.

As a result, they are all equivalent. We just define the reals to be such a field and leave the fact of its existence to the appendices of books.

##### _definition:_ least upper bound, supremum, least upper bound property

We say that $x$ is the least upper bound of some $E$, a subset of some ordered $S$, if $x \le e'$ for any upper bound $e'$ of $E$.

We say that an ordered set $S$ has the least upper bound property if any subset that is bounded above has a least upper bound.

##### _definition:_ the reals, $\mathbb{R}$

The set of all real numbers $\mathbb{R}$, is the smallest ordered [[Abstract algebra --- math-171/notes/Fields|field]] containing $\mathbb{Q}$ with the least upper bound property.

Note that hear the least upper bound property is equivalent to the "greatest lower bound property" — since $\mathbb{R}$ is an ordered field, we can look at $-A = \{ -a \mid a \in A \}$ for any $A$ bounded below. $-A$ will be bounded above, and $- \sup(-A)$ will be a lower bound for $A$, and in fact with a little work, we can show that it is the infimum. Alternatively, one could consider $\sup B$ for $B = \{ x \mid x \text{ is a lower bound of } A \}$. It almost follows as a tautology that $\inf A = \sup B$.