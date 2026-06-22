---
tags:
- uc-2026/alg-top/2
- alg-top
- peter-may
---


Ordinary simplicial complexes are good enough for [[Simplicial homology and random walks --- math-145/notes/Simplicial homology#_definition _ simplicial homology, Betti number|simplicial homology]] but not much more. We make an improvement that is not good enough and we will immediately improve.

##### _definition:_ ordered simplicial complexes, morphism of ordered simplicial complexes

An **ordered simplicial complex** is a [[Simplicial homology and random walks --- math-145/notes/Simplicial complexes#_definition _ simplicial complex, simplex|simplicial complex]] with a partial order on the set of vertices that restricts to a total order on each simplex.

A **morphism of ordered simplicial complexes** is then a morphism of simplicial complexes such that function on vertex sets is a morphism of posets.

---

These are good enough for homology but don't have Cartesian products. If you were to investigate what products of ordered simplicial complexes should be, you'd be well motivated to drop the total order to a partial order and allow repetition and deletion of vertices, and then actually just drop any order. Maybe this definition would seem well-motivated then.

##### _definition:_ simplicial sets, simplex category, simplicial objects

A **simplicial set** is a collection of sets $K_{n}$ for all integers $n \geq 0$ with functions $d_{i} : K_{n} \to K_{n - 1}$ and $s_{i} : K_{n} \to K_{n + 1}$ such that
$$
d_{i} s_{j} = \begin{cases}
s_{j - 1} d_{i} & i < j \\
d & j \leq i \leq j + 1 \\
s_{j} d_{i - 1} i > j + 1
\end{cases}
$$
as well as $s_{i} s_{j} = s_{j + 1} s_{i}$ and $d_{i} d_{j} = d_{j - 1} d_{i}$ for any $i < j$.

Note that this defines an index category $\mathscr{I}$ such that a simplicial set is just the diagram of some functor $\mathscr{I} \to \mathsf{Set}$. Specifically, $\mathscr{I} = \Delta^\text{opp}$, if we write $\Delta$ for the **simplex category** — the category of finite sets where morphisms are non-decreasing functions. 

A **simplicial object** in a category $\mathscr{C}$ is the diagram of a covariant functor $\mathscr{I} \to \mathscr{C}$. 

The simplicial objects in a category form a category under natural transformations. We denote the category of simplicial objects in $\mathscr{C}$ by $\mathscr{C}^\Delta$. Note, usually this notation would mean the category of covariant $\Delta \to \mathscr{C}$, but here it means the category of contravariant $\Delta \to \mathscr{C}$.

---

This allows us to make a definition of simplicial abelian groups, for example. Clearly, the free abelian group functor $\mathsf{Set} \to \mathsf{Ab}$ gives us a functor $\mathsf{Set}^\Delta \to \mathsf{Ab}^\Delta$. Then, from each simplicial abelian group, we can construct a chain complex, and then take its homology.

##### _definition:_ simplicial set singular homology

---

If only we had a functor $\mathsf{Top} \to \mathsf{Set}^\Delta$ , we would get a homology theory on $\mathsf{Top}$.

### From spaces to simplicial sets

These simplicial sets really are concretely related to topological spaces somehow. The idea is to return to topological (geometric) simplexes.

##### _definition:_ topological simplices

The $n$th topological simplex is $\Delta_{n}^\mathsf{Top} \subseteq \mathbb{R}^n$ is convex hull  of all $n$ standard basis vectors $e_{i} \in \mathbb{R}^n$ (with the [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subspace topology]]).

---

There is a (covariant) functor $\Delta \to \mathsf{Top}$ by $\underline{n} \mapsto \Delta_{n}^\mathsf{Top}$ (a cosimplicial topological space). Thus, 

There is a way for us to convert this functor $\mathsf{Top} \to \mathsf{Set}^\Delta$ to a functor in the other direction by abstract nonsense. You just take the tensor product! of $F : \mathscr{D} \to \mathscr{C}$ and $G : \mathscr{D}^\text{opp} \to \mathscr{C}$ and get an element $G \otimes_{\mathscr{D}} F$ of $\mathscr{C}$.