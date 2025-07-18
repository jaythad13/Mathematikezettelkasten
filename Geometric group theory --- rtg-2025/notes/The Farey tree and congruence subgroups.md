---
tags:
- ggt
- alg
- graph
- nt
- rtg-2025
---

An important example of group [[Geometric group theory --- rtg-2025/notes/Actions on trees|actions on trees]] is that of $\mathrm{SL}_{2}(\mathbb{Z})$ on the Farey tree. This gives a non-trivial example where the theorem that [[Geometric group theory --- rtg-2025/notes/Actions on trees#_theorem _ free actions on trees come from free groups|only free groups act freely on trees]] is useful. $\mathrm{SL}_{2}(\mathbb{Z})$ is clearly not a free group — the $\pi / 2$ rotation matrix has order $4$. However, we will be able to prove that the groups obtained by reducing modulo $m$ are free by their induced action on a special tree.

### Congruence subgroups of $\mathrm{SL}_{2}(\mathbb{Z})$

Recall the definition of the special linear group over a ring.

![[Geometric group theory --- rtg-2025/notes/The special linear group over the integers#_definition _ special linear group, projective special linear group|The special linear group over the integers]]

##### _definition:_ principal congruence subgroup

For each integer $m > 1$, the principal congruence subgroup of level $n$ in $\mathrm{SL}_{2}(\mathbb{Z})$ is $\Gamma(n)$, the kernel of the [[Abstract Algebra I --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphism]] $\pi_{n} : \mathrm{SL}_{2}(\mathbb{Z}) \to \mathrm{SL}_{2}(\mathbb{Z} / n \mathbb{Z})$ given by
$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix} \mapsto \begin{pmatrix}
\overline{a} & \overline{b} \\
\overline{c} &  \overline{d}
\end{pmatrix}
$$
where $a \mapsto \overline{a}$ is the canonical homomorphism $\mathbb{Z} \to \mathbb{Z} / n \mathbb{Z}$.

Note then that $\Gamma(n) \trianglelefteq \mathrm{SL}_{2}(\mathbb{Z})$ and is of finite [[Abstract Algebra I --- math-171/notes/Lagrange's theorem#_definition _ index, $ lvert G H rvert$|index]] since $\mathrm{SL}_{2}(\mathbb{Z}) / \Gamma(n) \cong \mathrm{SL}_{2}(\mathbb{Z} / n \mathbb{Z})$ is finite.

Since we typically denote graphs by $\Gamma$, we will use the notations $\mathrm{SL}_{2}(\mathbb{Z})[n] = \Gamma(n)$ to avoid confusion.

We will demonstrate a non-trivial action of $\mathrm{SL}_{2}(\mathbb{Z})$ on a tree that restricts to a free action of $\mathrm{SL}_{2}(\mathbb{Z})[n]$.

### Farey things and the $\mathrm{SL}_{2}(\mathbb{Z})$ action

The Farey tree describes the inclusions of edges around faces in the Farey graph, an object from [[Geometric group theory --- rtg-2025/notes/The hyperbolic plane|hyperbolic geometry]].

##### _definition:_ the Farey graph

The Farey graph $\Gamma_{\text{F}}$ is the simple, undirected, infinite graph with vertex set
$$
\{ (v_{1} : v_{0}) \in \mathbb{Z}^{2} \mid  \gcd(\lvert v_{1} \rvert , \lvert v_{0} \rvert ) = 1  \} / \sim
$$
where $(v_{1} : v_{0}) \sim (-v_{1} : -v_{0})$. Notice that this is essentially the quotient of $\mathbb{Z}^{2}$ by the action of $\mathbb{Q}^\times$. $\Gamma_{\text{F}}$ has an edge between vertices $(u_{1} : u_{0})$ and $(v_{1} : v_{0} )$ exactly when
$$
\left\lvert \begin{pmatrix}
u_{1} & v_{1} \\
u_{0} & v_{0}
\end{pmatrix}  \right\rvert = \pm 1.
$$

Note that this edge definition respects the equivalence relation on primitive pairs in $\mathbb{Z}^{2}$.

The Farey graph then carries an $\mathrm{SL}_{2}(\mathbb{Z})$ action by matrix multiplication — for $A \in \mathrm{SL}_{2}(\mathbb{Z})$ and $(v_{1} : v_{0}) \in V(\Gamma_{\text{F}})$ we have an action by
$$
A \cdot (v_{1} : v_{0}) = A \begin{pmatrix}
v_{1} \\
v_{0}
\end{pmatrix}.
$$
This action is indeed a [[Geometric group theory --- rtg-2025/notes/Graph actions and Cayley graphs#_definition _ graph action|graph action]] respecting edges since the "determinant of vertices" is the same before and after the action. That is, for $A \in \mathrm{SL}_{2}(\mathbb{Z})$ and and $(u_{1}: u_{0}), (v_{1} : v_{0}) \in V(\Gamma_{\text{F}})$
$$
\begin{vmatrix}
A \begin{pmatrix}
u_{1} \\
u_{0}
\end{pmatrix} & A \begin{pmatrix}
v_{1} \\
v_{0}
\end{pmatrix}
\end{vmatrix} = \left\lvert A  \begin{pmatrix}
u_{1} & v_{1} \\
u_{0} & v_{0}
\end{pmatrix}  \right\rvert = \lvert A \rvert \left\lvert  \begin{pmatrix}
u_{1} & v_{1} \\
u_{0} & v_{0}
\end{pmatrix}  \right\rvert  = \left\lvert  \begin{pmatrix}
u_{1} & v_{1} \\
u_{0} & v_{0}
\end{pmatrix}  \right\rvert.
$$
Thus, $(u_{1} : u_{0})$ and $(v_{1} : v_{0})$ are adjacent exactly when $A \cdot (u_{1} : u_{0})$ and $A \cdot (v_{1} : v_{0})$ are.

The Farey graph can be constructed inductively by this action. We start from the two edges $(1 : 0)$ and $(0 : 1)$. There are exactly two vertices connected to both of these — $(1 : 1)$ and $(-1 : 1)$. Then for each of the four new edges, we can look for vertices connected to both of their endpoints. By column transformations (and using Bezout's theorem to verify the ratios are in least terms) we can obtain two new vertices adjacent to both $(u_{0} : u_{1})$ and $(v_{0} : v_{1})$. These are $(u_{0} + v_{0} : u_{1} + v_{1})$ and $(u_{0} - v_{0} : u_{1} - v_{1})$. We claim this procedure gives all edges.

Since any $(v_{1} : v_{0})$ can be sent to $(1 : 0)$ by some graph automorphism $A \in \mathrm{SL}_{2}(\mathbb{Z})$, we just need to verify that this procedure gives all edges with an endpoint at $(1 : 0)$. In particular, $(v_{1} : v_{0}) \mapsto (1 : 0)$ by the matrix
$$
\begin{pmatrix}
v_{1} & a \\
v_{0} & b
\end{pmatrix}^{-1} = 
\begin{pmatrix}
b & - u_{1} \\
- v_{0} & a
\end{pmatrix}
$$
where $a, b$ are integers such that $a v_{1} + b v_{0} = 1$, guaranteed to exist by [[Superdiscrete --- math-55a/notes/Dividing integers - basic number theory#_theorem _ Bezout's theorem|Bezout's theorem]].

If $(v_{1} : v_{0})$ is adjacent to $(1 : 0)$, then we have
$$
\left\lvert  \begin{pmatrix}
1 & v_{1} \\
0 & v_{0}
\end{pmatrix}  \right\rvert = \pm 1
$$
so $v_{0} = \pm 1$ and $v_{1}$ can then be any positive integer. We've seen that we get $(1 : 1)$ and $(1 : - 1)$ adjacent to $(1 : 0)$ from the first step of our algorithm. Since we can get $(n + 1 : \pm 1)$ as $(n - 1 + 1 : \pm 1 + 0)$, adjacent to both $(n : \pm 1)$ and $(1 : 0)$, it follows by induction that we get all vertices adjacent to $(1 : 0)$.

The Farey tree is then the incidence tree of edges and faces of the Farey graph all of which happen to be triangles (since any two vertices have a common neighbour).

##### _definition:_ the Farey tree

The Farey tree is the graph $T_{\mathrm{F}}$ with vertex set $E(\Gamma_{\text{F}}) \cup F(\Gamma_{\text{F}})$ so that an edge of the Farey graph is adjacent to exactly those faces it surrounds and vice-versa.

It is in fact the tree composed of vertices alternating between degree $2$ and degree $3$, starting at $e_{0}$, the vertex corresponding to the Farey graph edge between $(1 : 0)$ and $(0 : 1)$. $e_{0}$ bounds the two largest faces of the Farey graph and so has two neighbours. Each of these is a triangular face with three neighbours — the three bounding edges, only two of which are new. Each of the bounding edges has one new triangular face, and so on.

The Farey tree really is a tree — given any vertex $v$ of the tree, there is a unique path back to $e_{0}$.

### The action on the Farey tree

Note that the action of $\mathrm{SL}_{2}(\mathbb{Z})$ on the Farey graph gives an action on its faces as well, preserving the edges around a face. Thus, $\mathrm{SL}_{2}(\mathbb{Z}) \circlearrowright \Gamma _\text{F}$ induces an action on the Farey tree.

##### _theorem:_ free congruence subgroups

For $n \geq 3$, the principal congruence subgroup $\mathrm{SL}_{2}(\mathbb{Z})[n]$ is a free group.

###### _proof:_

To prove $\mathrm{SL}_{2}(\mathbb{Z})[n]$ is free, [[Geometric group theory --- rtg-2025/notes/Actions on trees#_theorem _ free actions on trees come from free groups|it suffices to prove that it acts freely]] on the Farey tree. We will show that in fact the [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ stabiliser, free|stabiliser]] of any vertex or edge of $T_{\text{F}}$ is only in $\mathrm{SL}_{2}(\mathbb{Z})[n]$ if it is the identity.

Since $\mathrm{SL}_{2}(\mathbb{Z}) \circlearrowright T_\text{F}$ comes from an action on $\Gamma _\text{F}$ which preserves edges and faces, the action on the Farey tree can't swap vertices corresponding to Farey graph edges with those corresponding to Farey graph faces. Since all edges of the tree are between a vertex corresponding to an edge and another corresponding to a face, this means that the edge between them is fixed if and only if both endpoints are fixed. It suffices then to show that the stabilisers of each vertex (under the $\mathrm{SL}_{2}(\mathbb{Z})$) contain no congruence elements.

By lemmata below, $\mathrm{SL}_{2}(\mathbb{Z}) \circlearrowright \Gamma _\text{F}$ is transitive on edges and on faces (separately). Thus, all vertices corresponding to edges have isomorphic stabilisers, and similarly for vertices corresponding to faces. Since $\mathrm{SL}_{2}(\mathbb{Z})[n]$ is [[Abstract Algebra I --- math-171/notes/Normal subgroups#_definition _ normal subgroups|normal]] (it is a kernel), its intersections with each conjugate stabiliser are also isomorphic. Thus, it suffices just to consider the cases of the vertex $e_{0}$ corresponding to the edge between $(1 : 0)$ and $(0 : 1)$ and the vertex $f_{0}$ corresponding to the face bounded by $(1 : 0)$, $(0 : 1)$, and $(1 : 1)$.

If $A \in \mathrm{SL}_{2}(\mathbb{Z})$ preserves $e_{0}$, then it must preserve the set $\{ (1, 0), (-1, 0), (0, 1), (0, -1) \} \subseteq \mathbb{Z}^{2}$ under matrix multiplication. Thus, the columns of $A$ must be some ordered choice of two vectors in the set. Since $\det A = 1$, not all $\binom{4}{2} 2!$ are valid. In particular, we cannot have a vector and its negative, and are forced to choose opposing or agreeing signs of the vectors so that they have positive determinant. Finally, we can choose to negate a matrix or not. We are left with $2 \binom{2}{2} 2! = 4$ matrices
$$
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}, \begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}, \begin{pmatrix}
-1 & 0 \\
0 & -1
\end{pmatrix}, \begin{pmatrix}
0 & 1 \\
-1 & 0
\end{pmatrix}
$$
which form the cyclic group of $\pi / 2$ rotations isomorphic to $\mathbb{Z} / 4 \mathbb{Z}$. For $n \geq 3$ none of the non-identity matrices are in $\mathrm{SL}_{2}(\mathbb{Z})[n]$. Note that this is sharp since for $n = 2$, we have $1 \equiv -1$ in $\mathbb{Z} / n \mathbb{Z}$ and thus, the negative of the identity is in $\mathrm{SL}_{2}(\mathbb{Z})[n]$.

If $A \in \mathrm{SL}_{2}(\mathbb{Z})$ preserves $f_{0}$, then it must preserve the set $\{ (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1) \}$. By similar arguments to the previous case, we get $\binom{3}{2} 2! = 6$ matrices
$$
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}, \begin{pmatrix}
0 & 1 \\
-1 & 1
\end{pmatrix}, \begin{pmatrix}
-1 & 1 \\
-1 & 0
\end{pmatrix}, \begin{pmatrix}
-1 & 0 \\
0 & -1
\end{pmatrix}, \begin{pmatrix}
0 & -1 \\
1 & -1
\end{pmatrix}, \begin{pmatrix}
1 & -1 \\
1 & 0
\end{pmatrix}
$$
which form a group of shears isomorphic $\mathbb{Z} / 6 \mathbb{Z}$. None of them are in $\mathrm{SL}_{2}(\mathbb{Z})[n]$. We are done!

##### _lemma:_ the Farey graph action is transitive on edges

###### _proof:_

It obviously suffices to show that there is $A \in \mathrm{SL}_{2}(\mathbb{Z})$ with $A \cdot e_{0}$ sent to the edge between arbitrary $(u_{1} : u_{0}), (v_{1} : v_{0})$. $A$ could be one of
$$
\begin{pmatrix}
u_{1} & v_{1} \\
u_{0} & v_{0}
\end{pmatrix} \quad \text{and} \quad \begin{pmatrix}
u_{1} & -v_{1} \\
u_{0} & -v_{0}
\end{pmatrix}
$$

##### _lemma:_ the Farey graph action is transitive on faces

###### _proof:_

Again, it suffices to show that there is $A \in \mathrm{SL}_{2}(\mathbb{Z})$ with $A \cdot f_{0}$ sent to an arbitrary face with vertices $(u_{1} : u_{0}), (v_{1} : v_{0}), (w_{1} : w_{0})$. Note that since $(w_{1} : w_{0})$ is adjacent to both of the other vertices, it is of one of the forms below —
$$
(u_{1} + v_{1} : u_{0} + v_{0}), \quad  (u_{1} - v_{1} : u_{0} - v_{0}).
$$
The two given choices for $A$ that send $e_{0}$ to the edge between $(u_{1} : u_{0})$ and $(v_{1} : v_{0})$ send $(1 : 1)$ to the two forms above (respectively).

### Presentations for $\mathrm{PSL}_{2}(\mathbb{Z})$ and $\mathrm{SL}_{2}(\mathbb{Z})$

The actions of $\mathrm{SL}_{2}(\mathbb{Z})$ on the Farey graph and tree actually descend to actions of the quotient $\mathrm{PSL}_{2}(\mathbb{Z})$ for obvious reasons. Since the units in $\mathbb{Z}$ are $\{ \pm 1 \}$, we have $\mathrm{PSL}_{2}(\mathbb{Z}) = \mathrm{SL}_{2}(\mathbb{Z}) / \{ \pm I \}$. However, $\{ \pm I \}$ is in the [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ kernel, effective action|kernel]] of the action $\mathrm{SL}_{2}(\mathbb{Z}) \circlearrowright \Gamma_\text{F}$ because we identify vertices $\pm (v_{1} : v_{0})$. This action is the [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ kernel, effective action|effective action]], and for that reason it is easier to give a presentation for $\mathrm{PSL}_{2}(\mathbb{Z})$ than it is for $\mathrm{SL}_{2}(\mathbb{Z})$.

##### _theorem:_ the free product presentation of $\mathrm{PSL}_{2}(\mathbb{Z})$

$$
\mathrm{PSL}_{2}(\mathbb{Z}) \cong \mathbb{Z} / 2 \mathbb{Z}  * \mathbb{Z} / 3 \mathbb{Z} \cong \left< a, b \mid a^2 = 1, b^3 = 1 \right>
$$

##### _theorem:_ the amalgamation presentation of $\mathrm{SL}_{2}(\mathbb{Z})$

$$
\mathrm{SL}_{2}(\mathbb{Z}) \cong \mathbb{Z}  / 4 \mathbb{Z} *_{\mathbb{Z} / 2 \mathbb{Z}} \mathbb{Z} / 6 \mathbb{Z} = \left< a, b \mid a^4 = 1, b^6 = 1, a^{2} b^{-3} = 1 \right> 
$$