---
tags:
- uc-2026/alg-top/2
- peter-may
- alg-top
---

Analogously to the [[Topology --- math-147/notes/The fundamental group|fundamental group]], we can define higher homotopy groups of topological spaces.

##### _definition:_ $n$th homotopy group of a space

The **$n$th homotopy group of $X$, based at $x_{0}$** is $\pi_{n}(X, x_{0})$, the group of [[Topology --- math-147/notes/Homotopy#_definition _ homotopic, homotopy, homotopic relative to|homotopy]] equivalence classes of pointed maps $(S^n, p) \to (X, x_{0})$.

---

Here, composition of $\alpha, \beta : S^n \to X$ is given by the gluing of the corresponding maps $[0, 1]^n \to X$ along a face $[0, 1]^{n - 1}$ (to get a map $[0, 2] \times [0, 1]^{n - 1}$). Equivalently, it is the map $S^n \to S^n \vee S^n \to X$  This is analogous to the definition of [[Topology --- math-147/notes/The fundamental group#_definition _ composition of paths|composition of paths]]. Finally, just as [[Topology --- math-147/attachments/homework/hw 10/hw 10.pdf#page=3|the fundamental group is functorial]], so are the higher homotopy groups — pointed continuous maps $f : X, x_{0} \to Y, y_{0}$ induce group homomorphisms $f_{*} : \pi_{n}(X, x_{0}) \to \pi_{n}(Y, y_{0})$ for each $n$.

##### _proposition:_ higher homotopy groups are abelian

For $n \geq 2$, $\pi_{n}(X, x_{0})$ is abelian.

###### _proof sketch:_

For $n \geq 2$, the boundary of $[0, 1]^n$ is connected. For any two $\alpha, \beta : [0, 1]^n \to X$, we have $\alpha \cdot \beta : [0, 2] \times [0, 1]^{n - 1} \to X$. Consider the homotopy equivalence to $\alpha \cdot e \cdot e \cdot \beta : [0, 2]^{2} \times [0, 1]^{n - 1}$. Then slide $\alpha$ around the boundary of $\beta$ to get $\alpha \cdot e \cdot e \cdot \beta = \beta \cdot e \cdot e \cdot \alpha$.

---

### Weak homotopy equivalence

The homotopy groups allow us to introduce an even weaker notion of similarity than [[Topology --- math-147/notes/Homotopy#_definition _ homotopy equivalence|homotopy equivalence]].

##### _definition:_ weak homotopy equivalence

A based continuous map $f : (X, x_{0}) \to (Y, y_{0})$ is a **weak homotopy equivalence** if it induces an isomorphism of [[Algebraic geometry --- rising-sea/notes/Categories#_example _ every group is an entire category, groupoids, monoids, the fundamental groupoid|groupoids]] $f_{*} : \pi_{n}(X, x_{0}) \to \pi_{n}(Y, y_{0})$ for each $n$.

---

Clearly, any homotopy equivalence induces a weak homotopy equivalence. For most reasonable spaces (CW complexes), weak homotopy equivalence is the same as [[Topology --- math-147/notes/Homotopy#_definition _ homotopy equivalence|homotopy equivalence]]. However, finite spaces and [[UChicago --- uc-2026/notes/Alexandroff spaces and posets#_definition _ Alexandroff spaces, A-spaces|Alexandroff spaces]] give a plethora of counterexamples.

##### _example:_ a weak homotopy equivalence is strictly weaker

Consider some $f : X \to Y$. It is generally true that, for any open cover $X = U \cup V$, if the restrictions $f_{\mid U}, f_{\mid V}, f_{\mid U \cap V}$ are weak homotopy equivalences, then $f$ is a weak homotopy equivalence as a whole. This is an application of homotopy excision.

In fact, a stronger result is true for arbitrary open covers $\{ U_{i} \}$ of $X$. If $f : X \to Y$ restricts to a weak homotopy equivalence on each open cover, then $f$ is a homotopy equivalence in

Recall the notions of a [[Topology --- math-147/notes/Quotient and identification spaces#_definition _ cone|cone]] $CX = X \times [0, 1] / X \times \{ 1 \}$, a non-reduced suspension $SX = CX \sqcup CX / X \sim X$, and the reduced suspension.

We define some modifications of these ideas. The **non-Hausdorff cone** of a space is $\mathbf{C} X = X \sqcup \{ p \}$ topologised so that the subspace topology on $X$ is the same as the topology on $X$, and the only open containing $p$ is the whole set. The **non-Hausdorff suspension** $\mathbf{S} X$ is constructed from the non-Hausdorff cone in the same way that the suspension is constructed from the cone.

Consider $SX$ as a quotient of $X \times [-1, 1]$. Label the two pole points of $\mathbf{S}X$ as $\pm 1$. Consider the map $f : SX \to \mathbf{S} X$ by
$$
f(x, t) = \begin{cases}
x & t \in (-1, 1) \\
t. \\
\end{cases}
$$
Because of the weird topology on $\mathbf{S} X$ this is in fact continuous. By the covering result, it is a weak homotopy equivalence. It is almost never a homotopy equivalence proper.

For any $n$, we inductively get maps $S S^{n - 1}X \to S \mathbf{S}^{n - 1} X \to \mathbf{S}^n X$. Choosing $X = S^0$ we get a weak homotopy equivalence between $S^2$ and a six point space. Note, by classical homotopy theory, $S^{2}$ has infinitely many non-zero homotopy groups, and so must the six point space.

---

This is far from the only example of interesting notions coming up in the homotopy of Alexandroff spaces. One interesting area of study is the idea of intermediate notions between [[Simplicial homology and random walks --- math-145/notes/Whitehead equivalence|Whitehead (or simple) equivalences]] and homotopy equivalences. These are not natural in the category of (ordered) simplicial complexes, but can be constructed from the combinatorial structure on Alexandroff spaces. The functor from Alexandroff spaces to (ordered) simplicial complexes gives such equivalence classes for simplices. Another is that asymptotically in the cardinality of finite spaces, there are as many homotopy equivalence classes of spaces are there are homeomorphism classes.