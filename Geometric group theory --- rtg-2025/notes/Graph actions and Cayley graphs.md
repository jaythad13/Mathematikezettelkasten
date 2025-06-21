---
tags:
- alg
- graph
- ggt
- rtg-2025
---

The Cayley graph of a group encodes it exactly by its symmetries. To define it and prove its properties we first need exact definitions of the type of graph we're working with.

### Graphs and automorphisms

Typically we work with [[Superdiscrete --- math-55a/notes/Basic graph theory#_definition _ graph|simple graphs]] — with at most one edge between any two vertices and no edges with both endpoints at the same vertex. We will allow these extra edges.

##### _definitions:_ (directed, multi-)graphs, endpoints

A directed multi-graph $\Gamma$ comprises a set of vertices $V(\Gamma)$, a set of edges $E(\Gamma)$, and a function $\operatorname{end} : E(\Gamma) \to V(\Gamma)^{2}$ (from the edges to ordered pairs of vertices). 

For an edge $e \in E(\Gamma)$, we say $\operatorname{end}_{\Gamma}(e)$ are the endpoints of $e$.

This can be specialised to simple graphs by requiring that the endpoint function is injective and has image within the unordered pairs of size two (under the forgetful map from ordered pairs of vertices to unordered pairs).

A graph morphism is then a pair — a function on vertices and a function on edges — that are compatible with the endpoint function.

##### _definition:_ graph morphism, graph isomorphism, graph automorphism

Given graphs $\Gamma$ and $\Gamma'$, a graph morphism $\Phi : \Gamma \to \Gamma'$ comprises a function $\Phi_{V} : V(\Gamma) \to V(\Gamma')$ and $\Phi_{E} : E(\Gamma) \to E(\Gamma')$ so that the endpoint function commutes with $f$ —
$$
\Phi_{V} \circ \operatorname{end}_{\Gamma} =  \operatorname{end}_{\Gamma'} \circ \Phi_{E}.
$$

A graph isomorphism is a graph morphism $\Phi : \Gamma \to \Gamma'$ with $\Phi_{V}$ and $\Phi_{E}$ bijections.

An automorphism of $\Gamma$ is a graph isomorphism $\Gamma \to \Gamma$.

We may require in addition that a graph morphism respect some additional structure on the graphs. For example, if we work in the category of graphs with edge-labels (a function $\ell_{\Gamma} : E(\Gamma) \to \Omega$), we require that $\Phi : \Gamma \to \Gamma'$ satisfies $\ell_{\Gamma'} \circ \Phi_{E} = \ell_{\Gamma}$.

It can be easily verified that morphisms compose, and thus, automorphisms of a graph form a group, called $\operatorname{Aut} \Gamma$.

By abuse of notation, when working concretely with edges or vertices (and there is no risk of confusion) we may drop the subscripts $V$ and $E$, writing $\Phi(v)$ or $\Phi(e)$.

##### _proposition:_ graphs form a category

The collection of graphs with graph morphisms is a [[Basic category theory --- basic-cat/notes/Categories#_definition _ category|category]].

###### _proof:_

The identity morphism $\operatorname{id}_{\Gamma}$ on a graph $\Gamma$ is given by the identity morphisms on $V(\Gamma)$ and $E(\Gamma)$.

The composition of morphisms $\Phi : \Gamma_{1} \to \Gamma_{2}$ and $\Psi : \Gamma_{2} \to \Gamma_{3}$ is given by $\Theta : \Gamma_{1} \to \Gamma_{3}$ with $\Theta_{V} = \Psi_{V} \circ \Phi_{V}$ and $\Theta_{E} = \Psi_{E} \circ \Phi_{E}$. Then
$$
\begin{align}
\Theta_{V} \circ \operatorname{end}_{\Gamma_{1}} & = \Psi_{V} \circ \Phi_{V} \circ \operatorname{end}_{\Gamma_{1}}  \\
& = \Psi_{V} \circ  \operatorname{end}_{\Gamma_{2}} \circ \Phi_{E} \\
& = \operatorname{end}_{\Gamma_{3}} \circ \Psi_{E} \circ \Phi_{E}  \\
& = \operatorname{end}_{\Gamma_{3}} \circ \Theta_{E}.
\end{align}
$$

The associativity of the composition and the fact that it respects the identity follow from the fact that graph morphisms arise from functions.

It's easy to show that if some particular "label" is preserved by the morphisms, it is preserved by their composition.

### Graph actions of a group

These automorphisms give a way to represent a [[Abstract Algebra I --- math-171/notes/Groups, and why you should care#_definition _ group, identity, inverse|group]] $G$ by the symmetries of a graph $\Gamma$. We represent $G$ by a pair [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ (left) group action|group actions]] $G \circlearrowright V(\Gamma)$ and $G \circlearrowright E(\Gamma)$ such that the functions  $v \mapsto g \cdot v$ and $e \mapsto g \cdot e$ form a graph (endo)morphism. We can show easily that this is equivalent to the data of a [[Abstract Algebra I --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|homomorphism]] $G \to \operatorname{Aut} \Gamma$.

##### _definition:_ graph action

A graph action of a group $G$ on a graph $\Gamma$ is a homomorphism $G \to \operatorname{Aut} \Gamma$, denoted $G \circlearrowright \Gamma$.

##### _examples:_ graph actions

- The symmetric group $\mathfrak{S}_{n}$ acts on the complete graph $K_{n}$.
- $\mathbb{Z} / 3 \mathbb{Z}$ acts on the trivalent graph $T_{3}$ by rotation.
- The Petersen graph can be encoded as having vertices $\binom{[5]}{2}$ with an edge between vertices exactly when two subsets share no vertices. Thus, $\mathfrak{S}_{5}$ acts on it by its action on $[5]$.
- $\mathbb{Z}$ acts on the infinite line graph, and in general $\mathbb{Z}^d$ acts on the $d$-dimensional rectangular lattice.

### Cayley graphs

Cayley graphs are defined so that their symmetries capture exactly the nature of the group — no more and no less. This isn't immediately apparent from their definition and it requires proof.

##### _definition:_ Cayley graphs

The Cayley graph of a group $G$ with presentation $\left< S \mid R \right>$ is the directed, (edge-)labeled graph $\Gamma(G, S)$ with $V(\Gamma(G, S)) = G$, and an edge $e$ with $\operatorname{end}(e) = (g, gs)$ for each $g \in G$ and $s \in S$, with a label function on edges $\ell : E(\Gamma(G, S)) \to S$ that labels an edge with endpoints $(g, gs)$ with $s$.

Note that the edges of $\Gamma(G, S)$ are determined completely by their endpoints (with choice of orientation). Thus we often denote an edge $e$ in the Cayley graph by $\operatorname{end}(e) = (v, w)$.

##### _example:_ left multiplication on the Cayley graph

Given $g \in G = \left< S \mid R \right>$ there is a corresponding automorphism $\Phi_{g} \in \operatorname{Aut} \Gamma(G, S)$ given by left multiplication by $g$. In particular, $\Phi_{g, V}(h) = gh$ for all $h \in V(\Gamma(G, S))$. The edge $(g, gs)$ is mapped to $\Phi_{g, E}(g, gs) = (gh, ghs)$.

This is obviously a graph action $G \circlearrowright \Gamma(G, S)$ (it's easily verified that $\Phi_{gh} = \Phi_{g} \circ \Phi_{h}$). We claim that it gives rise to all the automorphisms of $\Gamma(G, S)$ and thus, the induced homomorphism $G \to \operatorname{Aut} \Gamma(G, S)$ is actually an [[Abstract Algebra I --- math-171/notes/Group isomorphisms#_definition _ group isomorphism, isomorphic|isomorphism]].

To prove this we need one new idea.

##### _definition:_ word length

Let $G$ be a group with presentation $\left< S \mid R \right>$. Let $S ^{-1}$ be the set $\{ s ^{-1} \mid s \in S \}$. Then the word length of $g \in G$ (with respect to $S$) is the length of the shortest word in $S \cup S^{-1}$ equal to $G$.

Equivalently, the word length is the shortest path from $1$ to $g$ on $\Gamma(G, S)$.

Since $G \cong F_{S} / \overline{R}$ [[Geometric group theory --- rtg-2025/notes/Free groups and presentations#_definition _ group presentation, generators, relators|by definition]] and the word length of each $g \in F_{S}$ is finite, the word length of each $g \in G$ is finite.

##### _theorem:_ a group is isomorphic to the symmetries of its Cayley graph

For a group $G \cong \left< S \mid R \right>$, the map $G \to \operatorname{Aut} \Gamma(G, S)$ by $g \mapsto \Phi_{g}$ is an isomorphism.

###### _proof:_

We already have that $g \mapsto \Phi_{g}$ is injective since $\Phi_{g}(1) = \Phi_{h}(1)$ if and only if $g = h$. Thus, we only need to prove surjectivity. In particular, since edges are determined by their directed endpoints, we only need to prove surjectivity of the vertex function.

Suppose $\Phi \in \operatorname{Aut} \Gamma(G, S)$ and $\Phi(1) = g$. We claim $\Phi = \Phi_{g}$. We prove this by induction on the word length with respect to $S$. The base case (word length $0$) is just that $\Phi(1) = g = \Phi_{g}(1)$. Suppose, for all $h \in G$ of word length $n$, $\Phi(h) = gh = \Phi_{g}(h)$. Note that all $h' \in G$ of word length $n + 1$ are neighbours of some $h$ of word length $n$. That is, there is some $s \in S \cup S^{-1}$ so that $h' = hs$. Without loss of generality, assume $s \in S$. Since $\Phi$ is edge preserving, we have $\Phi(h') = \Phi(h) s$ as well. In particular, 
$$
\Phi(h') = \Phi_{g}(h)s = ghs = gh' = \Phi_{g}(h).
$$
Since all $h \in G$ have finite word length, induction gives us that all $h \in G$ have $\Phi(h) = \Phi_{g}(h)$.


##### _example:_ the Cayley graph of a [[Geometric group theory --- rtg-2025/notes/Free groups and presentations#_definition _ free group|free group]]

The Cayley graph of the free group on $2$ elements (say $a, b$) $F_{2}$ is an infinite tetravalent graph (every vertex has [[Superdiscrete --- math-55a/notes/Basic graph theory#_definition _ degree, $d(v)$|degree]] $4$). If we draw the graph with all edges at a vertex perpendicular, we label all the horizontal edges with $a$ and the vertical edges with $b$.

Because the graph is infinite, are pictures are typically bad and can be misleading. For example, the subgraphs $\Gamma_{a^{-1}}$ and $\Phi_{a}(\Gamma_{a^{-1}})$ are isomorphic even though $\Phi_{b}(\Gamma_{a^{-1}})$ appears to be thrice the size. In general, for any word $g \in F_{2}$, the associated automorphism $\Phi_{g}$ looks like sliding the centre of the graph along to $g$.