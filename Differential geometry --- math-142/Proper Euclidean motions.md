---
tags:
- diff-geo
- math-142
lecture:
- math-142-20
- math-142-21
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

Note that $\mathbb{R}^n \cong \mathcal{T}_{n}$ (as groups under addition and composition respectively, or vector spaces with scalar multiplication) by $\mathbf{a} \mapsto T$ where $T : \mathbb{R}^n \to \mathbb{R}^n$ by $\mathbf{v} \mapsto \mathbf{v} + \mathbf{a}$.

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

It's easy to see that $O_{n}$ is closed under composition and taking inverses. Thus, $O_{n}$ is a subgroup of $\mathcal{E}_{n}$.

##### _proposition:_ orthogonal transformations are linear maps

Say $C \in O_{n}$. Then $C(a\mathbf{p} + b\mathbf{q}) = aC\mathbf{p} + b C \mathbf{q}$ for any $\mathbf{p}, \mathbf{q} \in \mathbb{R}^n$ and any $a, b \in \mathbb{R}$.

##### _theorem:_ the classification of Euclidean motions

For any $F \in \mathcal{E}_{n}$ there exist a unique translation $T \in \mathcal{T}_{n}$ and a unique orthogonal transformation $C \in O_{n}$ such that $F = T \circ C$.

##### _proof sketch:_

Just check $C : \mathbf{p} \mapsto F(\mathbf{p}) - F(0)$ and $T : \mathbf{p} \mapsto \mathbf{p} + F(0)$. It's easy to see that these are unique.

Note that we have the following short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\{ 0 \} \ar[r] & \mathbb R^n \ar[r, "\varphi"] & \mathcal{E}_n \ar[r, "\psi"] & O_n \ar[r] & \{ 0 \}
	\end{tikzcd}
\end{document}
```
where $\varphi$ is the isomorphism between $\mathbb{R}^n$ and $\mathcal{T}_{n}$, and $\psi(F)$ is the function by $F(\mathbf{p}) - F(0)$ for any $F \in \mathcal{E}_{n}$. Note then that we have $O_{n} \cong \mathcal{E}_{n} / \mathcal{T}_{n}$.

### Euclidean motions on tangent spaces

Now we want to look at Euclidean motions on tangent spaces! One way to do this is to just look at the pushforward — [[Maps on Euclidean space#_definition _ tangent map|their tangent maps]]!

##### _proposition:_ the tangent maps of isometries behave like isometries

Suppose $F : \mathbb{R}^n \to \mathbb{R}^n$ is an isometry. Then $F_{*}$ just looks like a rotation about the point
$$
F_{*}([\mathbf{v}, \mathbf{p}]) = [C\mathbf{v}, F\mathbf{p}].
$$
for $F(\mathbf{p}) = \mathbf{a} + C\mathbf{p}$, and it preserves the dot product —
$$
F_{*}([\mathbf{v}, \mathbf{p}]) \cdot F_{*}([\mathbf{w}, \mathbf{p}]) = [\mathbf{v}, \mathbf{p}] \cdot [\mathbf{w}, \mathbf{p}].
$$

##### _proof sketch:_

Note that by the [[#_theorem _ the classification of Euclidean motions|the classification of Euclidean motions]], we can write $F$ as $T \circ C$ for some translation $T : \mathbf{p} \mapsto \mathbf{p} + \mathbf{a}$ and some $C \in O_{n}$. We can see by the [[Differentiability theorems#_corollary _ the multivariable sum rule|sum rule]] for differentiable maps that the partials will just work out to be the partials of $C$ (since $DT = 0$). Since $C$ is linear, we just have $DC = C$ at every point. Thus
$$
F_{*}([\mathbf{v}, \mathbf{p}]) = [C\mathbf{v}, F\mathbf{p}].
$$

It's then simple to see that
$$
\begin{split}
F_{*}([\mathbf{v}, \mathbf{p}]) \cdot F_{*}([\mathbf{w}, \mathbf{p}]) & = [C\mathbf{v}, F\mathbf{p}] \cdot [C\mathbf{w}, F\mathbf{p}] \\
& = C\mathbf{v} \cdot C\mathbf{w} \\
& = \mathbf{v} \cdot \mathbf{w} \\
 & = [\mathbf{v}, \mathbf{p}] \cdot [\mathbf{w}, \mathbf{p}].
\end{split}
$$

It's then kind of obvious to see that by mapping orthonormal basis to orthonormal basis and base point to base point, we can map between two orthonormal tangent bases. Specifically,

##### _theorem:_ isometries keep track of frame fields

For any frame field $\mathbf{E}_{1}, \mathbf{E}_{2}, \mathbf{E}_{3}$, there is a unique isometry $F : \mathbb{R}^3 \to \mathbb{R}^3$ such that
$$
F_{*}(\mathbf{E}_{k}(\mathbf{p})) = \mathbf{E}_{k}(\mathbf{q})
$$
for all $k \in \{ 1, 2, 3 \}$ where $\mathbf{q} = F(\mathbf{p})$.

##### _proof sketch:_

We want to write $F = T \circ C$. Recall that $F_{*} = [C, F]$, so we can just write $C$ as the orthogonal map that sends the orthonormal basis of the vector parts of $\mathbf{E}_{1}(\mathbf{p}), \mathbf{E}_{2}(\mathbf{p}), \mathbf{E}_{3}(\mathbf{p})$ to the orthonormal basis of the vector parts of $\mathbf{E}_{1}(\mathbf{q}), \mathbf{E}_{2}(\mathbf{q}), \mathbf{E}_{3}(\mathbf{q})$. Note that there is a neat basis change trick that you can use to compute the matrix of that in the standard orthonormal basis on $\mathbb{R}^3$.

Then compute $T$ so that $F\mathbf{p} = \mathbf{q}$ works out.