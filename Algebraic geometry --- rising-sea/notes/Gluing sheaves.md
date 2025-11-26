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

###### _proof:_

Note that we don't assume $\{ U_{i} \}_{i \in \mathscr{I}}$ is a finite cover.

Consider the base $\{ B_{i_{n}} \subseteq U_{i} \}_{i \in \mathscr{I}}$ of open sets contained in some $U_{i}$. We have a [[Algebraic geometry --- rising-sea/notes/Sheaves on a base#_definition _ sheaves on a base, presheaves on a base|sheaf on this base]] by $\mathscr{F}_{\text{b}}(B_{i_{n}}) = \mathscr{F}_{i}(B_{i_{n}})$. We verify this is really a sheaf on a base below. Choosing $\mathscr{F} = \mathscr{F}_{\text{b}}^\text{sh}$ gives $\mathscr{F}_{\mid i}(B_{i_{n}}) = \mathscr{F}_{i}(B_{i_{n}})$ for every open subset $B_{i_{n}} \subseteq U_{i}$ and thus, $\mathscr{F}_{\mid i} = \mathscr{F}_{i}$. This choice is well-defined by the sheaf isomorphisms.

Suppose $B = \bigcup_{j \in \mathscr{J}} B_{j}$. Since $B$ is an open set in the base, it is contained in some $U_{i}$ and so are all the $B_{j}$. Then base identity and gluability are inherited from $\mathscr{F}_{i}$.

$\mathscr{F}$ is unique since any such gluing of the $\mathscr{F}_{i}$ into a sheaf must agree with $\mathscr{F}$ on the basis.

---

The cocycle condition allows us to ensure that $\mathscr{F}_{\mid U_{i}} \to \mathscr{F}_{i}$ is an isomorphism.

This says, in some sense that there is a sheaf of sheaves, but not quite.