---
tags:
- math-55a
- graph
---

We are not talking about the graph of a function!!!

##### _definition:_ graph

A graph $G$ is consists of a pair - a finite set of vertices $V$ and a set of pairs (we will say size $2$ subsets) of vertices $E$ that we think of as the edges between them.

The definition that we are thinking of is often called a simple graph - no directed edges, no self pointing edges, and no multiple edges between the same vertices.

This, is a dumb way to think of a very visual thing so we will talk about a graph as just its picture

##### _definition:_ adjacent

We say two vertices of $v_1$ and $v_2$ of $G$ are adjacent if $\set{v_1, v_2} \in E(G)$.

##### _definition:_ degree, $d(v)$

##### _proposition:_ the handshake lemma

The sum of the degrees of all of the vertices is twice the number of edges

###### _proof sketch:_

Each edge gets counted exactly twice.

##### _corollary:_ there are an even number of oddballs

There are an even number of vertices with odd degree

###### _proof sketch:_

The sum of all the degrees is even, so the sum of all odd degrees is even, so the number of them is even.

##### _definition:_ graph isomorphism

We say that two graphs $G_1$ and $G_2$ are isomorphic if there is a bijection $f : V_1 \to V_2$ with $f(v_1)$ adjacent to $f(v_2)$ if and only if $v_1$ is adjacent to $v_2$.

##### _definition:_ complete graph, $K_n$

We say a graph is complete if every pair of vertices is connected.

We call the complete graph with $n$ edges $K_n$

### Some basic graph colouring

##### _theorem:_ Ramsey's theorem for $(3, 3)$

If we colour the edges of $K_6$ red or blue, we must have a completely red or completely blue $K_3$ somewhere in the graph.

###### _proof sketch:_

After colouring the edges, look at the edges coming out from any vertex $v$. At least $3$ of them must be the same colour. (Without loss of generality) assume red.

Of the three vertices that are connected to $v$, if the edges between any of them are red, then we have a red triangle. If they are all blue, because they are connected, we have a blue triangle.

%%draw a picture%%

This is often called the $(3, 3)$ Ramsey number. We often phrase this as "among any group of $n$ people there are either $3$ friends or $3$ complete strangers".

##### _theorem:_ Ramsey's theorem for $(3, 4)$

If we colour the edges of $K_{10}$ red or blue, we must have a red $K_3$ or a blue $K_4$ somewhere in the graph.

###### _proof sketch:_

At least $4$ red or at least $6$ blue coloured edges.

If we have $4$ red, either there's a blue $K_4$ among the edges or there's a red edge that gives us a $K_3$.

If we have $6$ blue, then we have $K_6$ among the edges its connected to, inside which there's a red $K_3$ or a blue $K_3$. If red, we're done, if blue, it's connected to the vertex we're looking at to form $K_4$.

We can push this down to $K_9$ too! If any vertex has $6$ blue edges or $4$ red edges, we have what we want. If both are not true, then we have to have $5$ blue edges and $3$ red edges. Delete all of the red edges and we have the contradiction that the sum of the degrees of all the vertices of the graph is odd - a graph with $5$ blue $3$ red at each vertex cannot exist.

We cannot reduce to $K_8$ - there's a construction that shows it too. 

### Walking on graphs

##### _definition:_ walk

A walk on a graph is a sequence of adjacent vertices with repetition allowed.

##### _definition:_ path

A path on a graph is a walk with no repeated vertices.

##### _theorem:_ walks give you paths

There is a walk on a graph $G$ from $v_1$ to $v_2$ if and only if there is a path from $v_1$ to $v_2$.

###### _proof sketch:_

We use an extremal argument (consider the shortest/longest something).

Consider the shortest walk, get rid of the repetitions, and then if you don't have a path, you have a shorter walk and a contradiction.

##### _definition:_ trail

A trail on a graph is a walk with no repeated edges. (There are no repeated pairs of vertices, in any order).

##### _definition:_ a closed trail

A closed trail is a trail with the same starting and ending vertex.

##### _definition:_ cycle

A cycle is a closed trail such that removing the last vertex gives you a path.

##### _definition:_ connected

We say a graph is connected if there is a path between any two vertices on the graph.

##### _definition:_ Eulerian graphs, Eulerian circuit.

A connected graph is Eulerian if there is a closed trail that contains all of its vertices. Such a closed trail is called an Eulerian circuit.

##### _proposition:_ Eulerian graph theorem

A connected graph is Eulerian if and only if all vertices have even degree.

###### _proof sketch:_

We can do the hard direction (even $\implies$ Eulerian) by strong induction on the number of edges on the graphs.

Suppose the theorem is true for all graphs with $< e$ edges. 

Consider any graph $G$ with $e$ edges. By the finiteness of the graph we must have a cycle $C$ (just keep walking until you a hit a vertex for the second time). If $C$ is the whole graph we're done.

If not, get rid of the edges in cycle, to get the graph $G - C$. $G - C$ has even degree edges because we're only decreasing edges by $2$ if ever we decrease them.

If $G - C$ is connected, just take $C$ and compose it with the Eulerian circuit on $G - C$ that we have by the induction hypothesis.

If $G - C$ isn't connected, it has connected components. That means we can walk along $C$ and at each point on it, go through any Eulerian circuits over the connected components.

##### _corollary:_ mostly even degree is fine

If $G$ has even degree at every vertex except $v_1$ and $v_2$, there is an Eulerian trail from $v_1$ to $v_2$.