---
tags:
- diff-geo
- math-142
lecture:
- math-142-20
---

Proper Euclidean motions are basically the nicest maps on metric spaces. We're just going to talk about $\mathbb{R}^n$, with the Euclidean inner product (the dot product).

##### _definition:_ proper Euclidean motion, $\mathcal{E}_{n}$

A well defined map $F : \mathbb{R}^n \to \mathbb{R}^n$ is said to be a proper Euclidean motion if it preserves distances. That is
$$
d(F(\mathbf{p}), F(\mathbf{q})) = d(\mathbf{p}, \mathbf{q}).
$$
The collection of all isometries is $\mathcal{E}_{n}$, the Euclidean group.

##### _proposition:_ the Euclidean group is a [[Motivating groups#_definition _ group, identity, inverse|group]]

$\mathcal{E}_{n}$ is a group under function composition. That is
1) For $F, G \in \mathcal{E}_{n}$, $F \circ G \in \mathcal{E}_{n}$.
2) Every $F \in \mathcal{E}_{n}$ is invertible with $F^{-1} \in \mathcal{E}_{n}$

##### _proof:_

We can show the first one by noting that for $H = F \circ G$
$$
\begin{split}
d(H(\mathbf{p}), H(\mathbf{q})) & = d(F(G(\mathbf{p})), F(G(\mathbf{q}))) \\
 & = d(G(\mathbf{p}), G(\mathbf{q})) \\
 &  = d(\mathbf{p}, \mathbf{q}).
\end{split}
$$

Prof. Goins leaves the second part as an exercise for me.

### Classifying Euclidean motions

We want to classify Euclidean motions. We can start by looking at the most basic examples of Euclidean motions

##### _definition, proposition:_ translations, $\mathcal{T}_{n}$, translations are a [[Subgroups#_definition _ subgroup, $ le$|subgroup]] of $\mathcal{E}_{n}$

1) For any fixed $\mathbf{a} \in \mathbb{R}^n$, the map $T : \mathbb{R}^n \to \mathbb{R}^n$ by $\mathbf{p} \mapsto \mathbf{p} + \mathbf{a}$ is a proper Euclidean motion, called a translation. The collection of all translations is $\mathcal{T}_{n}$
2) For any two translations $S, T \in \mathcal{T}_{n}$ we have $ST^{-1}$, which suffices to show that $\mathcal{T}_{n} \le \mathcal{E}_{n}$.

##### _proof:_
is too trivial to be written out.

##### _proposition, definition:_ orthogonal transformations, $O_{n}$,

The following are equivalent for any for any map $C : \mathbb{R}^n \to \mathbb{R}^n$,
1) $C$ is a Euclidean motion that fixes the origin.
2) $C$ preserves distances and lengths — $C$ is a Euclidean motion with $\lVert C(\mathbf{p}) \rVert = \lVert \mathbf{p} \rVert$
3) $C$ preserves the dot product — $C(\mathbf{p}) \cdot \mathbf{C}(\mathbf{q}) = \mathbf{p} \cdot \mathbf{q}$.

The collection of all such maps is called $O_{n}$. $O_{n} \le \mathcal{E}_{n}$.

##### _proof sketch:_

We will show 1) $\implies$ 2) $\implies$ 3) $\implies$ 1). We write out the first and sketch the rest.

Suppose $C$ is a Euclidean motion that fixes the origin. Then $C$ preserves distances, including the distance to $0$. Thus,
$$
\begin{split}
\lVert C(\mathbf{p}) \rVert & = d(C(\mathbf{p}), 0) \\
 & = d(C(\mathbf{p}), C(0)) \\
 & = d(\mathbf{p}, 0) \\
 & = \lVert \mathbf{p} \rVert  
\end{split}
$$

Suppose $C$ preserves distances and lengths. Then using the polarisation identity we can show that $C$ preserves dot products.

Finally, suppose $C$ preserves dot products. It's easy to write the distance in terms of dot products, which $C$ preserves. Thus, $C$ preserves the distance. We can also see that the origin is sent to itself since the only thing that has length zero is the origin, and $C$ preserves lengths.

##### _proposition:_ orthogonal transformations are linear maps

Say $C \in O_{n}$. Then $C(a\mathbf{p} + b\mathbf{q}) = aC\mathbf{p} + b C \mathbf{q}$ for any $\mathbf{p}, \mathbf{q} \in \mathbb{R}^n$ and any $a, b \in \mathbb{R}$.

##### _theorem:_ the classification of Euclidean motions

For any $F \in \mathcal{E}_{n}$ there exist a unique translation $T \in \mathcal{T}_{n}$ and a unique orthogonal transformation $C \in O_{n}$ such that $F = T \circ C$.

##### _proof sketch:_

Just check $C : \mathbf{p} \mapsto F(\mathbf{p}) - F(0)$ and $T : \mathbf{p} \mapsto \mathbf{p} + F(0)$.