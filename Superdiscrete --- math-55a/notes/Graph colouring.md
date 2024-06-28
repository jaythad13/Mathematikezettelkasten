---
tags:
- math-55A/6
- graph
---

##### _definition:_ proper colouring

A graph is properly coloured by giving each vertex a colour, with repetitions allowed, such that no two adjacent vertices have the same colour.

##### _definition:_ $k$-colourable

A graph is $k$-colourable if it has a proper colouring using only $k$ different colours.

##### _definition:_ chromatic number, $\chi(G)$

The chromatic number $\chi(G)$ of a graph $G$ is the smallest number such that $G$ is $\chi(G)$-colourable.

##### _proposition:_ bipartite graphs haven't an odd cycle

If a graph is bipartite ($2$-colourable), it has no cycles of odd length.

###### _proof sketch:_

Try to colour the odd cycle: you'll fail. This is the contrapositive.

Surprisingly the converse is true too.

##### _proposition:_ graphs that haven't an odd cycle are $2$-colourable

If a (connected?) graph has no cycles of odd length, it is bipartite.

###### _proof sketch:_

If $G$ is a tree, do this by induction on the number of vertices—remove a leaf, $2$-colour the previous case, and then add back the leaf and since it's a leaf it can be coloured safely.

Notice that in a tree with a $2$-colouring, the length of the [[Superdiscrete --- math-55A/notes/Special graphs#_proposition _ unique paths on trees|unique path]] between two vertices of the same colour is even.

If $G$ is not a tree, remove edges from the graph (only to break cycles) until you get a tree. This is the spanning tree. $2$-colour the tree, and then add back the edges. It'll all be fine, because we had no odd cycles, and connecting two vertices of the same colour would produce an odd cycle (the unique even path plus the new edge).

### Planar graph colouring

We started caring about colouring planar graphs (graphs at all, actually) because we wanted to colour maps, and we can turn any map into a planar graph with it's dual graph.

##### _definition:_ dual graph

For a graph $G$ with vertices $V$ edges $E$ and faces $F$, its dual graph $\hat G$ has vertices $F$ and an edge for any two faces that share an edge (in fact there is an isomorphism between the edges).

##### _lemma:_ planar graphs have vertices of small degree

Every planar graph has a vertex of degree $\le 5$.

###### _proof:_

Suppose there is no such graph. Then by the handshake lemma we have $2 \abs{E} > 5n > 3n - \frac{n}{2} \ge 3n - 6$ for $n \ge 12$. (I think just do it manually in the other cases?)

##### _theorem:_ the six colour theorem

Every planar graph is $6$-colourable.

###### _proof sketch:_

We induct on $n$, the number of vertices. We have base cases $n \le 6$, obviously.

Suppose $G$ is planar. Then remove the vertex of degree $\le 5$, $6$-colour the resultant (obviously planar) graph, and then add it back.

##### _theorem:_ the five colour theorem

Every planar graph is $5$-colourable

###### _proof sketch:_

Again, induction on $n$, the number of vertices. We have base cases $n \le 5$, obviously.

Suppose $G$ is planar. Draw it in a planar way. Remove the vertex of degree $\le 5$, $5$-colour the resultant graph and then add it back. Suppose it has five neighbours $v_1, \ldots, v_5$, all of different colour (if it doesn't we're done).

Pick $v_1$ and $v_3$, and turn $v_1$ to the colour of $v_3$, and then turn its neighbours to the colour of $v_1$ if they're already $v_3$-coloured, and so on. Unless this cycles back to $v_3$, we're done.

If it cycles back to $v_3$, then it surrounds $v_2$. Since we drew the graph in a planar way, we can't cross an edge to draw a similar circling path from $v_4$ to $v_2$, so we can switch $v_2$'s colour to $v_4$'s colour, and then we have only four colours in the neighbours of the vertex.