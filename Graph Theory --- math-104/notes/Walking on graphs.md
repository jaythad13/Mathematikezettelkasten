---
tags:
- math-104/2
- graph
- comb
---

We've already seen results about walking on graphs in #math-55A —

![[Superdiscrete --- math-55A/notes/Basic graph theory#Walking on graphs|Basic graph theory]]

So far we have considered shortest paths and walks to do things. What about longest paths? How can we find the longest path in a graph? When can we have two different longest walks (sharing no vertices)?

This last question leads to the notion of connectedness.

##### _definition:_ connected, disconnected, connected component

A graph is connected if for all vertices, $u$ and $v$, there is a walk between them.

If a graph is not connected, it is disconnected.

A connected component of a graph $G$ is a subgraph that is not a [[Graph Theory --- math-104/notes/Vocabulary for graph theory#_definition _ subgraph|proper subgraph]] of any connected subgraph of $G$.