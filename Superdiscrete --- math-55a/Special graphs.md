---
tags:
- math-55a
- graph
lecture: math-55a-6
---

### Hamiltonian graphs

Hamiltonian is like Eulerian, except for vertices, not paths.

##### _definition:_ Hamiltonian path, Hamiltonian cycle, Hamiltonian graph

Given a graph $G$, a Hamiltonian path is a [[Basic graph theory#_definition _ path|path]] is a path that visits every vertex of $G$. 

A Hamiltonian cycle is a [[Basic graph theory#_definition _ cycle|cycle]] that visits every vertex of $G$.

We say a graph $G$ is Hamiltonian if it contains a Hamiltonian cycle.

##### _note:_ checking if a graph is Hamiltonian is NP-hard!!!

Sometimes, there are efficient tests. If each vertex of a graph with $n$ vertices has degree $\ge 2$, then the graph is Hamiltonian. The converse is obviously false.

### Trees

Very useful things!

##### _definition:_ tree

A tree is a connected graph with no cycles.

##### _definition:_ forest

A forest is a graph which has connected components that are trees.

Note that if we define forests first as any graphs with no cycles, we get the definition of a tree as a connected forest.

##### _theorem:_ Cayley's theorem

For $n \ge 1$ the number of distinct labeled trees with $n$ vertices is $n^{n - 2}$.

##### _proof:_
is tricky and not given. (Take Math 104 or 106)

##### _definition:_ leaf

A vertex of a tree with degree $1$ is called a leaf.

##### _proposition:_ every tree has a leaf

For any $n \ge 2$, any tree with $n$ vertices has a leaf.

##### _proof sketch:_

We can prove this two ways—by contradiction, and by an extremal argument (also contradiction).

Consider the longest path in the graph $v_1 \, \cdots, v_m$. If $v_1$ isn't a leaf it must be connected to something other than $v_2$. But that can't be something in the longest path (that would give us a cycle), 

##### _proposition:_ we can build a graph leaf-by-leaf

If we remove a leaf $v$ from a graph $G$, the resultant graph $G - v$ is a tree.

##### _proof:_

%% do this later %%

##### _proposition:_ $\abs{E} = \abs{V} - 1$

Any tree with $n$ vertices has $n - 1$ edges.

##### _proof sketch:_

Induct on $n$ using the fact about leaves.

##### _proposition:_ unique paths on trees

For any two vertices $v_1$ and $v_2$ in a tree there is a unique path between them.

##### _proof sketch:_

Show that if there are two paths there is a cycle (from the first vertex after which they diverge to the next vertex they both contain and back).

### Planar graphs

Can you embed it in the plane? It's planar!

##### _definition:_ planar graph

A planar graph can be drawn so that no edges cross.

##### _(non)-example:_ $K_5$

$K_5$ is non-planar

##### _theorem:_ Euler's theorem

If $G$ is a connected plane graph with $n$ vertices, $e$ edges, and $f$ faces $n - e + f = 2$.

##### _proof sketch:_

If $G$ is a tree we have $n - 1$ edges and $1$ face. Thus, we have $n - (n - 1) + 1 = 2$ as desired.

If $G$ is not a tree, then the graph must have a cycle (since it is connected). If we remove an edge from a cycle, we have the same number of vertices but one fewer face. Then we have reduced this to a previously solved case by induction on the number of edges. Thus $n - k + (f - 1)  = 2$ giving us $n - (k + 1) + f = 2$ as desired.

One example application of this is that we cannot have a Venn diagram with four circles. Count the vertices (the number of intersections of the circles), the faces (the number of intersections of regions, which we want to be $2^4$) and then the number of edges (by the degree of each vertex and handshake lemma)

##### _proposition:_ a bound on the edges of planar graphs

If a planar graph has $n$ vertices and $e$ edges, $e \le 3n - 6$.

##### _proof:_ 

%% do later %%

##### _corollary:_ $K_5$ is non-planar

Note that we can achieve equality with $K_3$ and the converse is not true—$K_{3, 3}$ is a counterexample with the right bound on edges but is non-planar.

##### _proposition:_ $K_{3, 3}$ is non-planar

##### _proof:_

##### _theorem:_ Kuratowski's theorem

A graph is non-planar if and only if it contains $K_5$, $K_{3, 3}$ or a subdivision of one of them as a subgraph. (A subdivision is just adding vertices on an edge of a graph.)

##### _(non) proof:_

The forward direction is obvious

The only if direction involves topology.

### Tournaments

Tournaments encode the idea of a competition of no-draw games where every player plays every other player.

##### _definition:_ tournament

A tournament is a complete graph where every edge is directed (use ordered pairs instead of two member subsets of $V$).

##### _theorem:_ someone is always the best

Every tournament with $n$ vertices has a directed [[Special graphs#_definition _ Hamiltonian path, Hamiltonian cycle, Hamiltonian graph|Hamiltonian path]] (a Hamiltonian path along which all the arrows point the same way).

##### _proof sketch:_

By induction on the number of vertices. We have base case $2$ if we need it.

Remove vertex $v_{n + 1}$. Without loss of generality, suppose our Hamiltonian path on the remaining graph is $v_1 \, \cdots \, v_n$.

If $v_{n + 1}$ beat $v_1$ or $v_n$ beat $v_{n + 1}$, it's easy.

If not, $v_1$ beat $v_{n + 1}$ and $v_{n + 1}$ beat $v_n$. So slot $v_{n + 1}$ between the first thing it beat (say $v_j$) and $v_{j - 1}$ which beat it (and exists because $j \neq 1$).

##### _definition:_ king, king chicken

A king (or king chicken) is a vertex such that there is an outward (directed) path of length at most $2$ to any vertex.

##### _theorem:_ every tournament has a king

The player with most wins in a tournament (greatest outward degree) is a king.

##### _proof sketch:_

Any player who can't be reached in $2$ steps must beat the person with most wins and also beat all of the people they beat (otherwise there'd be a $2$ step way to get there). But then they've beat more people than the person with most wins—a contradiction, showing that this person doesn't exist.


