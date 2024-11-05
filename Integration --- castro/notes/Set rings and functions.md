---
tags:
- anal
- castro
---

When constructing measures, we want to have an additive function on sets. For this, it's useful to have a notion of addition on sets. In fact, the sets form a [[Abstract Algebra I --- math-171/notes/Rings#_definition _ unit|ring]]! Sort of.

##### _definition:_ set rings, $\sigma$-rings

A family $\mathscr{R}$ of sets is a set ring if $A_{1}, A_{2} \in \mathscr{R}$ implies $A_{1} \cup A_{2}, A_{1} \setminus A_{2} \in \mathscr{R}$.

Note that since $A_{1} \cap A_{2} = A_{1} \setminus (A_{1} \setminus A_{2})$, this also gives us $A_{1} \cap A_{2} \in \mathscr{R}$.

A set ring $\mathscr{R}$ is a $\sigma$-ring if it is closed under countable unions —
$$
\bigcup_{n = 1}^\infty A_{n} \in \mathscr{R}
$$
whenever all $A_{n} \in \mathscr{R}$.

Since
$$
\bigcap_{n = 1}^\infty A_{n} = A_{1} - \bigcup_{n = 1}^\infty (A_{1} \setminus A_{n})
$$
we also have that $\mathscr{R}$ is closed under countable intersections.

Note that this is not a ring proper under the operations $\cup$ and $\cap$. Instead, the addition on this ring is given by the symmetric difference $A_{1} \oplus A_{2} = (A_{1} \cup A_{2}) \setminus (A_{1} \cap A_{2})$ and the multiplication is just the intersection.

Now we can define what it means for functions to be additive on this set ring.

##### _definition:_ set function, additivity, countable additivity

A function $\phi : \mathscr{R} \to \mathbb{R}_{\infty}$ from the set ring $\mathscr{R}$ to the extended real numbers is a set function.

A set function $\phi$ is a additive if $\phi(A_{1} \cup A_{2}) = \phi(A_{1}) + \phi(A_{2})$ for every pair of disjoint $A, B \in \mathscr{R}$. 

It's countably additive if
$$
\phi\left( \bigcup_{n = 1}^\infty A_{n} \right) = \sum_{n = 1}^\infty \phi(A_{n})
$$
when $A_{n}$ are pairwise disjoint — $A_{i} \cap A_{j} = \emptyset$ for all $i, j$. 

Note that for additivity to be sensible, $\phi^\text{img}(\mathscr{R})$ cannot contain both $- \infty$ and $\infty$. 

Also note that additivity is equivalent to $\phi$ being a [[Abstract Algebra I --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphism]] on $(\mathscr{R}, \oplus)$.

##### _proposition:_ additive set functions are homomorphisms

For any $A_{1}, A_{2} \in \mathscr{R}$,
$$
\phi(A_{1} \cup A_{2}) + \phi(A_{1} \cap A_{2}) = \phi(A_{1}) + \phi(A_{2})
$$
and
$$
\phi(A_{1} \setminus A_{2}) = \phi(A_{1}) \setminus \phi(A_{2}).
$$

Additive functions have a number of obvious properties —

##### _proposition:_ $n$ unions

If $\phi$ is additive,
$$
\phi\left( \bigcup_{i = 1}^n A_{i} \right) = \sum_{i = 1}^n \phi(A_{i}).
$$
In particular, $\phi(\emptyset) = 0$.

##### _proposition:_ order preservation

If $\phi(A) \ge 0$ for all $A \in \mathscr{A}$, and $A_{1} \subset A_{2}$, then
$$
\phi(A_{1}) \leq \phi(A_{2}).
$$