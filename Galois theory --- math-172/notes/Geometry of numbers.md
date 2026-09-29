---
tags:
- math-172/8
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

A **sublattice** $N \subseteq M$ is a $\mathbb{Z}$-submodule of the same rank, with the same discrete embedding into

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

##### _proposition:_ minimal length vectors

Let $M, i_{M}$ be a lattice. Let $m \in M$ and $v = i_{M}(m)$ be an element of minimal length $\lVert v \rVert$. Then
$$
\lVert v \rVert \leq \frac{2}{\sqrt{ 3 }} \Delta L.
$$

---