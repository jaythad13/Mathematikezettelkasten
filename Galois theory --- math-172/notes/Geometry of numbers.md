---
tags:
- math-172/8
- math-172/9
- alg
- alg-nt
- nt
---

Let $\mathbb{K} = \mathbb{Q}(\sqrt{ d })$ be an imaginary quadratic field. 

### Lattices

We can and should think of $\mathscr{O}_{\mathbb{K}}$ and its ideals as a $\mathbb{Z}$-module and its submodules. Since $\mathscr{O}_{\mathbb{K}}$ is an integral domain and contains $\mathbb{Z}$, and it and all of its submodules are torsion-free. That is, $\mathscr{O}_{\mathbb{K}}$ and its submodules are free $\mathbb{Z}$-modules.

This gives motivation for thinking about free $\mathbb{Z}$-modules embedded in $\mathbb{R}^{2}$ and their equal rank submodules — lattices. Here we prove some general facts.

##### _definition:_ lattice, lattice in the plane, sublattice

A **lattice** $M$ is a free $\mathbb{Z}$-module of rank $r$, with a discrete embedding $i_{M} : M \subseteq \mathbb{R}^{r}$. We say it is a lattice in the plane if $r = 2$.

A **sublattice** $N \subseteq M$ is a $\mathbb{Z}$-submodule of the same rank, with the same discrete embedding into $\mathbb{R}^r$.

We often leave the embedding implicit.

---

##### _example:_ (imaginary quadratic) number rings and their ideals are lattices and sublattices

We have already seen that $\mathscr{O}_{\mathbb{K}}$ 

---

Since $M$ is embedded in $\mathbb{R}^r$, we can use notions of volume.

##### _definition:_ fundamental domain, volume of a lattice

Let $M, i_{M}$ be a lattice of rank $r$. Let $m_{1}, \dots, m_{r}$ be a basis of the lattice and let $v_{i} = i_{M}(m_{i})$. Then the fundamental domain of the lattice

----

##### _proposition:_ volume is basis independent

---

##### _proposition:_ sublattices always have finite index

---

##### _proposition:_ computing indices of sublattices

Suppose $L \subseteq M$ is a sublattice of a lattice in the plane. Then $\# M / L = \Delta L / \Delta M$.

---

##### _proposition:_ bounding minimal length vectors

Let $M$ be a lattice. Let $v \in M$ be a non-zero vector element of minimal length $\lVert v \rVert$. Then
$$
\lVert v \rVert^{2} \leq \frac{2}{\sqrt{ 3 }} \Delta M.
$$

###### _proof:_

Choose an embedding so that $v$ is embedded as $\lVert v \rVert (1, 0)$ and choose another generator so that $w = (w_{1}, w_{2})$ such that $- \lVert v \rVert / 2 \leq w_{1} \leq \lVert v \rVert / 2$. We can obtain such a $w$ by adding or subtracting integer multiples of $v$ to a second generator.

Then 
$$
\lVert v \rVert^{2} \leq \lVert w \rVert^{2} \leq w_{1}^{2} + w_{2}^{2} \leq \lVert v \rVert^{2} / 4 + w_{2}^{2}
$$
and so $w_{2}^{2} \geq 3 \lVert v \rVert / 4$. Notice that (by definition of the area of a parallelogram) $\Delta L = \lVert v \rVert w_{2}$. But then $\Delta L = \lVert v \rVert w_{2} \geq \sqrt{ 3 } \lVert v \rVert^{2} / 2$.

---

##### _lemma:_ points in the lattice must be sufficiently far away

Let $M$ be a lattice. Let $r$ be the minimal length of the non-zero vectors. For any $m \in M$, the open disc centred at $m$ and of radius $r$ contains only one point ($m$) in $M$. Further, the open disc centred at $m / 2$ and of radius $v / 2$ contains no points from $M$ except possibly $m / 2$.

---

### Measuring the size of ideals

