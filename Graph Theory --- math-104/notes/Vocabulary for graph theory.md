---
tags:
- math-104/1
- graph
- comb
---

### What is a graph?

![[Superdiscrete --- math-55A/notes/Basic graph theory#_definition _ graph|Basic graph theory]]

The picture of a graph assings points to $V(G)$ and curves between the corresponding points to $E(G)$. The edges can cross each other without creating a vertex. It's usually non-unique.

We often write the fact $\{ u, v \} \in E(G)$ as $uv \in E(G)$.

There are some more obvious definitions we should make for an arbitrary (simple) graph $G$.

##### _definition:_ order, size

The size of the set of vertices $\lvert V(G) \rvert$ is the order of the graph.

The size of the set of edges $\lvert E(G) \rvert$ is the size of the graph.

##### _definition:_ adjacency, incidency

If $uv \in E(G)$ we say $u, v$ are adjacent or neighbours.

We say $v$ and $uv$ are incident.

If $e, f \in E(G)$ both have the vertex $v \in V$ in $e$ and $f$, then $e$ and $f$ are adjacent.

##### _example:_ a simple graph

The graph with $V(G) = \{ a, b, c, d, e \}$ and $E(G) = \{ ab, bc, ac, ce \}$ has order $5$ and size $4$.

##### _example:_ the null graph

is the graph with $V(G)$ empty.

### Subgraphs

A natural thing to do is to look at the substructures of a graph, much as one does with subgroups of groups for instance.

##### _definition:_ subgraph

A graph $H$ is a subgraph of $G$ if $V(H) \subseteq V(G)$ and $E(H) \subseteq E(G)$. We write this as $H \subseteq G$.

It's a proper subgraph if it's not the null graph and either of the inclusions of vertices and edges are proper.

##### _definition:_ spanning subgraphs

A spanning subgraph $H \subseteq G$ is a subgraph with vertex set $V(H) = V(G)$.

Note that right now subgraphs and spanning subgraphs don't have to be connected, so we can just pick the vertices without picking edges between them.

##### _definition:_ induced subgraphs

$H$ is an induced subgraph of $G$ if, for all $u, v \in V(H)$ every edge $uv \in E(G)$ is contained in $E(H)$.

For $X \subseteq V$, we write $G[X]$ for the corresponding induced subgraph.

### Linear algebra

In the future, we will see that linear algebra is really useful for graph theory. There are many natural definitions to make.

##### _definition:_ adjacency matrix

Tha adjacency matrix $A(G)$ of a graph $G$ has rows and columns labeled by the vertices of $G$ with the $(u, v)$th entry $1$ if $u$ and $v$ are adjacent and $0$ otherwise.

##### _example:_ the adjacency matrix of a simple graph

Note that for a simple graph, like the graph with $V(G) = \{ a, b, c, d, e \}$ and $E(G) = \{ ab, bc, ac, ce \}$ that we considered previously, the adjacency matrix is symmetric —
$$
A(G) = \begin{pmatrix}
0 & 1 & 1 & 0 & 0 \\
1 & 0 & 1 & 0 & 0 \\
1 & 1 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0
\end{pmatrix}
$$