---
tags:
- alg-comb
- pundit
---

> Chromatic polynomials are easy to learn!

\- Rosa Orellana

Chromatic polynomials give us a way to deal with graphs using polynomials. They are algebraic combinatorics in that polynomials are algebraic and graphs are combinatoric. In particular, they help us think about trees.

##### _definition:_ tree

A tree is a connected graph with no cycles.

A colouring of a graph assigns a "colour" to each vertex of the graph. A proper colouring makes sure that no two adjacent vertices have the same colour.

##### _definition:_ proper colouring

A proper colouring of a graph $G$ is a function
$$
\kappa : V(G) \to \bb{N}
$$
with $\kappa(u) \neq \kappa(v)$ for ${u, v} \in E(G)$.

##### _example:_ applications of proper colourings

If you have $n$ courses, draw a graph with $n$ vertices with an edge between them if the courses have students in common. Then, the least proper colouring is the least number of time slots you need so that students can take all of the courses.

##### _notation:_ $\chi_G(k)$

$\chi_G(k)$ is the number of $k$ colour proper colourings of a graph $G$.

It turns out that $\chi_G(k)$ is always a polynomial (why?). (Note that if $G$ contains the $m$-complete graph, then $\chi_G(p) = 0$ for $p < m$, which if we believe that it is a polynomial, can be very useful)

For trees, we can easily get the polynomial: start at any node, colour it one of $k$ colours, then since all of its neighbours only have one coloured neighbour, they can all be coloured in $k - 1$ ways. Thus,

##### _theorem:_ chromatic polynomial of a tree

If $G$ is a tree with $n$ vertices $\chi_G(k) = k(k - 1)^{n-1}$

Note that there is some recursion on the chromatic polynomial
$$
\chi_G(k) = \chi_{G - e}(k) - \chi_{G/e}(k)
$$
where $G - e$ is the graph with some edge deleted, and $G/e$ is the graph with the same edge contracted.

Since $G - e$ and $G/e$ eventually reduce to trees. 

##### _example:_ the chromatic polynomial of $C_4$

Consider colouring the graph with commuting variables $x_1, x_2, \ldots$ instead of colours. We represent a colouring of the graph with $j_m$ vertices coloured with $x_m$ for each $m$ with the product of the commuting variables $x_1^{j_1}  x_2^{j_2}\cdots$.

The chromatic symmetric function is then the sum of all of the monomials we get from graph colourings. Note that we call it is symmetric because permuting the variables doesn't change the way you can "colour" with them. (The set of RGB colourings is the same as the set of BRG colourings).

##### _definition:_ chromatic symmetric function

Note that the set of all symmetric functions is a vector space. It turns out that using linear algebra you can calculate the CSF. Basically, you find a nice basis of the space of symmetric functions that corresponds to some graph theoretic thing, and then use that.


