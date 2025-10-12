---
tags:
- alg-geo
- alg-top
- rising-sea/2/5/4
---

Let $X$ be a topological space.

Once we have the basic gluing blocks of schemes, in practice we will construct schemes by gluing these blocks together. To do so, we will need to be able to glue sheaves together.

##### _proposition, definition:_ sheaves glue, cocycle condition

Suppose $X = \bigcup_{i \in \mathscr{I}} U_{i}$ is an open cover of $X$ and there are sheaves $\mathscr{F}_{i}$ on each $U_{i}$ with isomorphisms $\varphi_{ij} : \mathscr{F}_{i \mid j} \to \mathscr{F}_{j \mid i}$ on restriction to $U_{i} \cap U_{j}$ that agree on triple overlaps so that $\varphi_{jk} \circ \varphi_{ij} = \varphi_{ik}$ on restriction to $U_{i} \cap U_{j} \cap U_{k}$ (called the **cocycle condition**).

Then there is a sheaf $\mathscr{F}$ on $X$ (unique up to unique isomorphism) with isomorphisms $\mathscr{F}_{\mid i} = \mathscr{F}_{i}$.

---

This says, in some sense that there is a sheaf of sheaves, but not quite.