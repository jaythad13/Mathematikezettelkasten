---
tags:
- alg-geo
- alg-top
- rising-sea/7/2
---

Let $X, Y$ be ringed spaces.

A morphism of ringed spaces defines what we want to turn topology into geometry — in addition to a continuous map $\pi : X \to Y$, it defines a morphism $\pi^\sharp : \mathscr{O}_{Y} \to \pi_{*} \mathscr{O}_{X}$ that pulls back functions on $Y$ to functions on $X$.

##### _definition:_ morphisms of ringed spaces

A **morphism of ringed spaces** $\pi : X \to Y$ is a [[Topology --- math-147/notes/Continuous functions#_definition _ continuity|continuous map]] of topological spaces along with a [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_definition _ morphism of sheaves|morphism of sheaves]] on $Y$ $\pi^\sharp : \mathscr{O}_{Y} \to \pi_{*} \mathscr{O}_{X}$.

---

It's easy to verify that these define a category of ringed spaces.

We can restrict morphisms of ringed spaces to open subsets of the domain in an obvious way — restrict the morphism of topological spaces as a function. Then $\pi^\sharp: \mathscr{O}_{Y} \to \pi_{*} \mathscr{O}_{X}$ defines $\pi^\sharp_{\mid U} : \mathscr{O}_{Y} \to \pi_{*} \mathscr{O}_{X} \to \pi_{\mid U, *} \mathscr{O}_{X}$.

We can glue these morphisms together on open subsets.

##### _proposition:_ morphisms of ringed spaces glue

If $X = \bigcup_{i \in \mathscr{I}} U_{i}$ and there are morphisms of ringed spaces given by $\pi_{i} : U_{i} \to Y$ and $\pi_{i}^\sharp : \mathscr{O}_{Y} \to \pi_{i, *}\mathscr{O}_{X \mid U_{i}}$ agreeing on overlaps $U_{i} \cap U_{j}$, then there is a unique morphism of ringed spaces $X \to Y$ such that $\pi_{\mid U_{i}} = \pi_{i}$.

---

The most important example of morphisms of ringed spaces for us is the morphism $\operatorname{Spec} A \to \operatorname{Spec} B$ induced by a ring homomorphism $B \to A$.

![[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_definition _ the induced morphism of ringed spaces of affine schemes|Affine schemes]]


Morphisms of ringed spaces also behave nicely at points. Specifically, they induce a natural morphism of stalks.

##### _definition:_ induced stalk morphism

For a morphism of ringed spaces $\pi : X \to Y$ with $\pi(p) = q$, the **induced morphism of stalks** is the composition of the [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_proposition _ "stalkification" is functorial|stalk morphism]] ${\pi^\sharp_{p}}: \mathscr{O}_{Y, p}  \to \pi_{*} \mathscr{O}_{X, p}$ and [[Algebraic geometry --- rising-sea/notes/Pushforward sheaves#_proposition _ pushforwards induce morphisms of stalks|the natural morphism from the pushforward stalk]] $\pi_{*}\mathscr{O}_{X, p} \to \mathscr{O}_{X, p}$.

---

It's by specifying behaviour of these stalk morphisms, we can ensure that morphisms pull back vanishing functions to vanishing functions, which will also be the right notion for morphisms of schemes.

### Morphisms of local ringed spaces

Let $X$ and $Y$ be [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ local ringed spaces, residue fields|local ringed spaces]].

Morphisms of local ringed spaces are defined so that they preserve the vanishing of functions.

##### _definition:_ morphism of local ringed spaces

A **morphism of local ringed spaces** $\pi : X \to Y$ is a morphism as ringed spaces such that the induced stalk morphism $\mathscr{O}_{Y, q} \to \mathscr{O}_{X, p}$ is a **morphism of local rings** — that is, $\pi^{\sharp, \text{img}}(\mathfrak{m}_{Y, q}) \subseteq \mathfrak{m}_{X, p}$.

---

Note for example, that any isomorphism as ringed spaces of local ringed spaces is a morphism of local ringed spaces.

##### _proposition:_ function values pullback through morphisms of local ringed spaces

If $\pi : X \to Y$ is a morphism of local ringed spaces and $\pi(p) = q$, then $\pi$ induces an inclusion of [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ local ringed spaces, residue fields|residue fields]] $\kappa(q) \to \kappa(p)$ with $g_{q}(q) \mapsto \pi^\sharp(g_q)(p)$.

---

Note that this implies functions vanishing at $q$ have pullback vanishing at $p$, and functions invertible at $q$ have pullback invertible at $p$.

### Pulling back $\mathscr{O}$-modules

### Open embeddings

One useful class of examples of morphisms of ringed spaces is open embeddings.

##### _definition:_ open embeddings

An **open embedding** is a morphism of ringed spaces $\pi : U \to Y$ with $\pi^\text{img}(U) = V$ giving an isomorphism $U, \mathscr{O}_{U} \cong V, \mathscr{O}_{Y \mid V}$.

---

For one, they are monic.

##### _proposition:_ open embeddings are monomorphisms

Suppose $\pi : U \to Y$ is an open embedding. Then it is a monomorphism.

###### _proof:_

Suppose $\mu_{1}, \mu_{2} : Z \to U$ are two morphisms of ringed spaces with $\pi \circ \mu_{1} = \pi \circ \mu_{2}$ and $\mu_{1}^\sharp \circ \pi^\sharp = \mu_{2}^\sharp \circ \pi^\sharp$.

---

But most importantly, open embeddings of schemes are exactly [[Algebraic geometry --- rising-sea/notes/Schemes#_proposition, definition _ open subschemes, affine open subscheme|open subschemes]].