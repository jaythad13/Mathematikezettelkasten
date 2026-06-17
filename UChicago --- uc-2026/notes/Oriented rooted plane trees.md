---
tags:
- uc-2026/random-graphs/1
- comb
- graph
- ewain-gwynne
---

If we want to understand [[Superdiscrete --- math-55A/notes/Special graphs#_definition _ tree|trees]], we have two tricks — we can add extra data to create finer isomorphism classes, and we can put them in bijection with objects that are simpler to understand. Here, we do both.

##### _definition:_ walk excursion

A **walk excursion** of size $2n$ is a function $f : \{ 0, \dots, 2n \} \to \mathbb{N}_{0}$ such that $f(2n) = f(0) = 0$ and $f(j) - f(j - 1) \in \{ \pm 1 \}$ for all $j$.

---

##### _definition:_ oriented rooted plane trees

An **oriented rooted plane tree** is a tree with a root vertex $e_{0}$ and a cyclic ordering for all of its branches.

---

##### _theorem:_ oriented rooted plane trees are just walk excursions

Oriented plane trees with $n$ edges are in bijection with walk excursions of size $2n$.

###### _proof sketch:_

If $v_{0}, \dots, v_{n}$ is the sequence of vertices for the unique depth first search indicated by the plane structure on the tree $T$, then send $T, \sigma$ to the distance function with $f(j) = d(v_{j}, v_{0})$. In the other direction, fold the graph. (If we didn't have the extra data of an orientation and root, this would be highly non-injective).

---

##### _theorem:_ the number of rooted plane trees

There are $\binom{2n}{n}/(n + 1)$ rooted oriented plane trees (rooted trees with a distinguished edge from the root, and a cyclic ordering of edges) with $n$ edges.

###### _proof sketch:_

It suffices to count walk excursions of length $2n$. Constructing a walk-excursion involves choosing which of the $n$ differences $f(j) - f(j - 1)$ are $1$ and setting the rest to $-1$. There are $\binom{2n}{n}$ such choices. However, an arbitrary function constructed in this way may take values in $\mathbb{Z} \setminus \mathbb{N}_{0}$.

To get rid of these, we want to find the number of functions that hit $-1$. Let $f$ be such a function and let $k$ be the minimum integer such that $f(k) = -1$. Let $\widetilde{f} : \{ 0, \dots, 2n \} \to \mathbb{Z}$ have $\widetilde{f}_{\mid [0, k]} = -2 - f_{\mid [0, k]}$ and $\widetilde{f}_{\mid [k, 2n]} = f_{\mid [k, 2n]}$. It turns out that $f \mapsto \widetilde{f}$ is a bijection between the possibly negative walk excursions that hit $-1$ and functions $f : \{ 0, 2n \} \to \mathbb{Z}$ with $f(0) = -2$, $f(2n) = 0$, and $f(j) - f(j - 1) \in \{ \pm 1 \}$. But there are obviously $\binom{2n}{n + 1}$ of these. Some binomial identities give the result.

---