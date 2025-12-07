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

##### _definition:_ the category of ringed spaces

The **identity morphism** on a ringed space is $\operatorname{id}_{X} : X \to X$ as a topological space and $\operatorname{id}_{X}^\sharp = \operatorname{id}_{\mathscr{O}_{X}} : \mathscr{O}_{X} \to (\operatorname{id}_{X})_{*} \mathscr{O}_{X} = \mathscr{O}_{X}$.

The **composition of morphisms** of ringed spaces $\pi, \pi^\sharp : X, \mathscr{O}_{X} \to Y, \mathscr{O}_{Y}$ and $\rho, \rho^\sharp : Y, \mathscr{O}_{Y} \to Z, \mathscr{O}_{Z}$ is given by $\rho \circ \pi : X \to Y \to Z$ as morphism of topological spaces and on the level of sheaves by
$$
(\rho \circ \pi)^\sharp = \rho_{*} \pi^\sharp \circ \rho^\sharp : \mathscr{O}_{Z} \to \rho_{*} \mathscr{O}_{Y} \to \rho_{*}(\pi_{*} \mathscr{O}_{X}) = (\rho \circ \pi)_{*} \mathscr{O}_{X}
$$
where the last map is given by the [[Algebraic geometry --- rising-sea/notes/Pushforward sheaves#_proposition _ pushforward is functorial|functoriality of the pushforward]] by $\rho$.

---

We can restrict morphisms of ringed spaces to open subsets of the domain in an obvious way.

##### _definition:_ restrictions of morphisms of ringed spaces on the domain

The **restriction of a morphism of ringed spaces $\pi : X \to Y$ to an open subset $U \subseteq X$ of the domain** is defined by $\pi_{\mid U} : U \to Y$ and $\pi^\sharp_{\mid U} : \mathscr{O}_{Y} \to \pi_{*} \mathscr{O}_{X} \to (\pi_{\mid U})_{*} \mathscr{O}_{X \mid U}$.

Here $\pi_{*} \mathscr{O}_{X}(V) \to (\pi_{\mid U})_{*} \mathscr{O}_{X}(V)$ is given by restriction: 
$$
\mathscr{O}_{X}(\pi ^\text{pre}(V)) \to \mathscr{O}_{X}(\pi^\text{pre}(V) \cap U) = \mathscr{O}_{X \mid U}(\pi_{\mid U}^\text{pre}(V)).
$$
This commutes with restriction because restriction commutes with restriction, or in some sense, by functoriality of the pushforward applied to $\mathscr{O}_{X} \to \mathscr{O}_{X \mid U}$ (but these are not even really sheaves on the same space).

---

We can also restrict morphisms of ringed spaces on the codomain.

##### _definition:_ restrictions of morphisms of ringed spaces on the codomain

The **restriction of a morphism of ringed spaces $\pi : X \to Y$ to an open subset $\pi^\text{img}(X) \subseteq V \subseteq Y$ of the codomain** is defined by $\rho = \pi : X \to V$ with $\rho^\sharp : \mathscr{O}_{Y \mid V} \to \pi_{*} \mathscr{O}_{X}$ given by $\rho^\sharp(W) = \pi^\sharp(W)$.

---

We can glue these morphisms together on open subsets.

##### _proposition:_ morphisms of ringed spaces glue

If $X = \bigcup_{i \in \mathscr{I}} U_{i}$ and there are morphisms of ringed spaces given by $\pi_{i} : U_{i} \to Y$ and $\pi_{i}^\sharp : \mathscr{O}_{Y} \to (\pi_{i})_{*} \mathscr{O}_{X \mid U_{i}}$ agreeing on overlaps $U_{i} \cap U_{j}$, then there is a unique morphism of ringed spaces $X \to Y$ such that $\pi_{\mid U_{i}} = \pi_{i}$.

###### _proof sketch:_

By the [[Topology --- math-147/notes/Continuous functions#_lemma _ the gluing lemma|gluing lemma]] we can glue all the $\pi_{i}$ into a continuous map $\pi : X \to Y$. Note that for each $V \subseteq Y$, we have $\pi^\text{pre}(V) = \bigcup_{i \in \mathscr{I}} \pi_{i}^\text{pre}(V)$. For each $V \subseteq Y$, the maps $\pi_{i}^\sharp(V) : \mathscr{O}_{Y}(V) \to (\pi_{i})_{*} \mathscr{O}_{X \mid U_{i}}(V) = \mathscr{O}_{X}(\pi^\text{pre}(V) \cap U_{i})$ agree on intersections — the maps $\mathscr{O}_{Y}(V) \to \mathscr{O}_{X}(\pi^\text{pre}(V) \cap U_{i} \cap U_{j})$ are the same. By our union expression for $\pi^\text{pre}(V)$, this allows us to obtain a unique limit map $\mathscr{O}_{Y}(V) \to \pi_{*} \mathscr{O}_{X}(V) = \mathscr{O}_{X}(\pi^\text{pre}(V))$ commuting with restriction to each $V \cap U_{i}$. Choose $\pi^\sharp(V)$ to be this map; it commutes with restriction by the limit definition, and so defines the unique $\pi^\sharp : \mathscr{O}_{Y} \to \pi_{*} \mathscr{O}_{X}$ agreeing with the $\pi_{i}^\sharp$. Thus, $\pi, \pi^\sharp$ is the unique morphism of ringed spaces that we wanted.

---

The most important example of morphisms of ringed spaces for us is the morphism $\operatorname{Spec} A \to \operatorname{Spec} B$ induced by a ring homomorphism $B \to A$.

![[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_definition _ the induced morphism of ringed spaces of affine schemes|Affine schemes]]


Morphisms of ringed spaces also behave nicely at points. Specifically, they induce a natural morphism of stalks.

##### _definition:_ induced stalk morphism

For a morphism of ringed spaces $\pi : X \to Y$ with $\pi(p) = q$, the **induced morphism of stalks** is the composition of the [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_proposition _ "stalkification" is functorial|stalk morphism]] ${\pi^\sharp_{q}}: \mathscr{O}_{Y, q}  \to \pi_{*} \mathscr{O}_{X, p}$ and [[Algebraic geometry --- rising-sea/notes/Pushforward sheaves#_proposition _ pushforwards induce morphisms of stalks|the natural morphism from the pushforward stalk]] $\pi_{*}\mathscr{O}_{X, p} \to \mathscr{O}_{X, p}$.

By abuse of notation $\pi^\sharp_{q}$ will sometimes refer to the composition $\mathscr{O}_{Y, q} \to \pi_{*} \mathscr{O}_{X, p} \to \mathscr{O}_{X, p}$ rather than just the first map.

---

It's by specifying behaviour of these stalk morphisms, we can ensure that morphisms pull back vanishing functions to vanishing functions, which will also be the right notion for morphisms of schemes.

### Open embeddings

One useful class of examples of morphisms of ringed spaces is open embeddings.

##### _definition:_ open embeddings

An **open embedding** is a morphism of ringed spaces $\pi : X \to Y$ with $\pi^\text{img}(X) = V$ giving an isomorphism $X, \mathscr{O}_{X} \cong V, \mathscr{O}_{Y \mid V}$.

---

For one, they are monic.

##### _proposition:_ open embeddings are monomorphisms

Suppose $\pi : X \to Y$ is an open embedding. Then it is a [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ monomorphisms, epimorphisms|monomorphism]].

###### _proof:_

Suppose $\mu_{1}, \mu_{2} : Z \to X$ are two morphisms of ringed spaces with $\pi \circ \mu_{1} = \pi \circ \mu_{2}$ and $(\pi \circ \mu_{1})^\sharp = (\pi \circ \mu_{2})^\sharp$. 

Since $X \to Y$ is injective (and thus, a monomorphism in $\mathsf{Top}$) we must have $\mu_{1} = \mu_{2} = \mu$. Since the sheaf morphisms are equal we must also have $\pi_{*} \mu_{1}^\sharp \circ \pi^\sharp = \pi_{*} \mu_{2}^\sharp \circ \pi^\sharp$. Restricting to the image of the morphism, we see that $\pi^\sharp$ is an isomorphism $\mathscr{O}_{Y \mid \pi^\text{img}(X)} \to \pi_{*}\mathscr{O}_{X}$. Thus, it is [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ monomorphisms, epimorphisms|epic]], and $\pi_{*} \mu_{1}^\sharp = \pi_{*} \mu_{2}^\sharp$. 

Then, by definition, we have $\mu_{1}(\pi^\text{pre}(V)) = \mu_{2}(\pi^\text{pre}(V))$ for all open $V \subseteq Y$. Since $\pi$ is an open embedding, we can realise every open subset $U \subseteq X$ as the pre-image of $\pi^\text{img}(U)$. Thus, $\mu_{1}^\sharp(U) = \mu_{2}^\sharp(U)$ for every open set — we have $\mu_{1}^\sharp = \mu_{2}^\sharp$.

---

But most importantly, open embeddings of schemes are exactly [[Algebraic geometry --- rising-sea/notes/Schemes#_proposition, definition _ open subschemes, affine open subscheme|open subschemes]].

### Morphisms of local ringed spaces

Let $X$ and $Y$ be [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ local ringed spaces, residue fields|local ringed spaces]].

Morphisms of local ringed spaces are defined so that they preserve the vanishing of functions.

##### _definition:_ morphism of local ringed spaces

A **morphism of local ringed spaces** $\pi : X \to Y$ is a morphism as ringed spaces such that the induced stalk morphism $\mathscr{O}_{Y, q} \to \mathscr{O}_{X, p}$ is a **morphism of local rings** — that is, $\pi^{\sharp, \text{img}}_{q}(\mathfrak{m}_{Y, q}) \subseteq \mathfrak{m}_{X, p}$.

---

Note for example, that isomorphisms and open embeddings as ringed spaces of local ringed spaces are morphisms of local ringed spaces.

##### _proposition:_ function values pullback through morphisms of local ringed spaces

If $\pi : X \to Y$ is a morphism of local ringed spaces and $\pi(p) = q$, then $\pi$ induces an inclusion of [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ local ringed spaces, residue fields|residue fields]] $\kappa(q) \to \kappa(p)$ with $g_{q}(q) \mapsto \pi^\sharp_{q}(g_q)(p)$.

###### _proof:_

Since $\pi^\sharp_{q} : \mathscr{O}_{Y, q} \to \mathscr{O}_{X, p}$. is a morphism of local rings, it induces a morphism of residue fields $\kappa(q) \to \kappa(p)$ so that the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{O}_{Y, q} \ar[r] \ar[d] & \mathcal{O}_{X, p} \ar[d] \\
		\kappa(q) \ar[r] & \kappa(p)
	\end{tikzcd}
\end{document}
```

---

Note that this implies functions vanishing at $q$ have pullback vanishing at $p$, and functions invertible at $q$ have pullback invertible at $p$.

### Pulling back $\mathscr{O}$-modules