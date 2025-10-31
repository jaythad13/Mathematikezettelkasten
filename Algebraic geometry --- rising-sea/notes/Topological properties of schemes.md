---
tags:
- rising-sea
- alg-geo
- comm-alg
- top
- rising-sea/3/6
---

Let $X$ be a topological space, and $A$ a ring.

Lots of topological notions have interesting applications to schemes (and affine schemes in particular).

### Connectedness

Connectedness of schemes is exactly connectedness as a topological space.

![[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ connectedness|Connectedness and path-connectedness]]

We can characterise the disconnected affine schemes as below.

##### _proposition:_ an algebraic characterisation of disconnected affine schemes

$\operatorname{Spec} A$ is disconnected if and only if $A$ is isomorphic to the product of non-zero rings.

###### _proof:_

Suppose $A = A_{1} \times A_{2}$ (a product of non-zero rings). Then note that $a_{1} = (1, 0)$ and $a_{2} = (0, 1)$ have $a_{1} a_{2} = 0$ and $a_{1} + a_{2} = 1$. Thus, $V((a_{1})) \cup V((a_{2})) = V(0) = \operatorname{Spec} A$ and $V((a_{1})) \cap V((a_{2})) = V(1) = \text{Ø}$. That is, $\operatorname{Spec} A$ is disconnected. 

Note that if $A_{1} = 0$, then $V(a_{2})$ would be $V(1)$ and thus, empty. Then connectedness would depend on the connectedness of $\operatorname{Spec} A_2$. Thus, we really do need a product of non-empty rings.

>[!missing]
> proof of the opposite direction

---

This hints at a more precise formulation.

![[Algebraic geometry --- rising-sea/notes/Examples of affine schemes#_proposition _ products of rings are disjoint unions of affine schemes|Examples of affine schemes]]

Note that we use the symbol $\coprod$ rather than $\bigsqcup$ because the disjoint union is the coproduct in the category of topological spaces (and soon we shall see, in the category of schemes as well).

### Irreducibility

Irreducibility is a strengthening of compactness. Irreducible topological spaces cannot be separated nicely — not even if we allow overlaps in the separation. This notion is less useful with Euclidean topologies (for example, $\mathbb{C}^{2}$ is reducible), but is useful when you have a coarser topology.

##### _definition:_ irreducibility, reducible

$X$ is **irreducible** if it is non-empty and it is not the union of two proper closed subsets.

That is, non-empty $X$ is irreducible if whenever $X = Y \cup Z$ with $Y, Z$ closed, we have $Y = X$ or $Z = X$.

$X$ is **reducible** if it is not irreducible.

---

Irreducibility can also be characterised by open sets.

##### _proposition:_ open set characterisation of irreducibility

$X$ is irreducible if and only if any two non-empty open sets of $X$ intersect.

###### _proof:_

Suppose $X$ is irreducible. Let $U, V \subseteq X$ be (non-empty) open sets. Then $X \setminus U \cap V = (X \setminus U) \cup (X \setminus V)$ is the union of two proper closed sets, and thus, is not all of $X$. That is, $U \cap V$ is non-empty.

Suppose any two non-empty open sets of $X$ intersect. Let $Y, Z \subsetneq X$ be two proper closed subsets and let $U = X \setminus Y$ and $V = X \setminus Z$. Then $Y \cup Z = X \setminus (U \cap V)$. Since $U \cap V$ is non-empty, $Y \cup Z$ cannot be the whole space.

---

This allows us to verify that irreducibility really is stronger than connectedness.

##### _proposition:_ irreducible spaces are connected

If $X$ is irreducible, then $X$ is connected.

###### _proof:_

Suppose $X = U \cup V$ is a union of open sets. Then, if they are both non-empty, they both intersect. Thus, $X$ is not the union of non-empty, disjoint, open sets.

---

Moreover, it is a strictly stronger notion — there are (affine scheme) examples of connected, reducible schemes.

##### _example:_ a connected, reducible scheme

Consider $\operatorname{Spec} \mathbb{C}[x, y] / (x^{2} - y^{2})$, [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_examples _ inclusions of quotients, topologically|which can be thought of as]] $V(x + y) \cup V(x - y) \subseteq \mathbb{A}_{\mathbb{C}}^{2}$. Clearly it is reducible — it is the union of proper subsets $V(x + y) \cup V(x - y)$. 

However, it is connected. We show that it is the union of connected sets with non-empty intersection. [[Topology --- math-147/notes/Connectedness and path-connectedness#_lemma _ unions of connected spaces with non-empty intersection|Such a topological space is connected]].

Each $V(x + y)$ and $V(x - y)$ is irreducible (each is homeomorphic to $\mathbb{A}^1_{\mathbb{C}}$ which is irreducible [[#_proposition _ an algebraic characterisation of irreducible affine schemes|by the algebraic characterisation below]]) and thus, connected. Their intersection is $V(x + y, x - y)$. Since $2x = (x + y) + (x - y)$ and similarly for $2y$, we have $(x, y) \subseteq (x + y, x - y)$. Since $(x, y)$ is maximal, we have $(x + y, x - y) = (x, y)$. Thus, their intersection is the non-empty set $V(x, y) = \{ (x, y) \}$.

---

Some other basic properties hold.

##### _proposition:_ open sets of an irreducible topological space

Any non-empty open subset of an irreducible topological space is [[Topology --- math-147/notes/Size restrictions#_definition _ dense|dense]].

###### _proof:_

Any non-empty open set of an irreducible topological space intersects every non-empty open set, and thus, every non-empty open neighbourhood. Thus, it is dense.

---

##### _proposition:_ closures of irreducible subsets are irreducible

$Z \subseteq X$ is irreducible (with the [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subspace topology]]) if and only if its closure $\overline{Z}$ is irreducible.

###### _proof:_

Suppose $Z \subseteq X$ is irreducible. Also suppose $\overline{Z} = Y_{1} \cup Y_{2}$ is the union of two (relatively) closed subsets. Since $\overline{Z}$ is closed, $Y_{1}$ and $Y_{2}$ are also closed in $X$. Thus, $Z = (Y_{1} \cap Z) \cup (Y_{2} \cap Z)$ is a union of two closed subsets. Without loss of generality, $Z = Y_{1} \cap Z$. Since $Y_{1} \supseteq Y_{1} \cap Z = Z$ is closed, [[Topology --- math-147/notes/Limit points and closed sets#_proposition _ the closure is the smallest closed set|it contains the closure]] of its subsets. That is, $Y_{1} \supseteq \overline{Z}$. Thus, $\overline{Z}$ is irreducible.

Suppose $Z \subseteq X$ and its closure $\overline{Z}$ is irreducible. Suppose $Z = (Y_{1} \cap Z) \cup (Y_{2} \cap Z)$ is the union of two (relatively) closed subsets (such that $Y_{1}, Y_{2} \subseteq X$ are closed). But then $Z = (Y_{1} \cup Y_{2}) \cap Z$, so $Y_{1} \cup Y_{2}$ is a closed subset containing $Z$. Thus it contains the closure — we have $\overline{Z} \subseteq Y_{1} \cup Y_{2}$. In fact, $\overline{Z} = (Y_{1} \cap \overline{Z}) \cup (Y_{2} \cap \overline{Z})$ is a union of closed subsets. Without loss of generality, $\overline{Z} = Y_{1} \cap \overline{Z}$. Thus,
$$
Z = \overline{Z} \cap Z = Y_{1} \cap \overline{Z} \cap Z = Y_{1} \cap Z.
$$
That is, $Z$ is irreducible, as desired.

---

We can characterise irreducible affine schemes algebraically.

##### _proposition:_ an algebraic characterisation of irreducible affine schemes

$\operatorname{Spec} A$ is irreducible if and only if $A$ contains a minimal prime ideal. Equivalently, the [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_definition _ nilradical|nilradical]] of $A$ is prime.

###### _proof:_

We briefly explain why the two conditions are equivalent. $A$ contains a minimal prime ideal if and only if the intersection of all primes is prime. The intersection of all prime ideals [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_proposition _ the nilradical is an ideal and the intersection of primes|is the nilradical]] $\mathfrak{N} \subseteq A$.

Suppose $\operatorname{Spec} A$ is irreducible. Equivalently, for any ideals $\mathfrak{i}, \mathfrak{j}$ with $V(\mathfrak{i}) \cup V(\mathfrak{j}) = \operatorname{Spec} A = V(0)$, we have $V(\mathfrak{i}) = V(0)$ or $V(\mathfrak{j}) = V(0)$. [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition, proposition _ the Zariski topology (is a topology)|Equivalently]], for any ideals with $V(\mathfrak{i} \mathfrak{j}) = V(0)$, we have $V(\mathfrak{i}) = V(0)$ or $V(\mathfrak{j}) = V(0)$. [[Algebraic geometry --- rising-sea/notes/Affine schemes#_proposition _ vanishing sets uniquely identify only radical ideals|Equivalently]], for any ideals with $\sqrt{ \mathfrak{ij} } = \mathfrak{N} = \sqrt{ (0) }$ we have $\sqrt{ \mathfrak{i} } = \mathfrak{N}$ or $\sqrt{ \mathfrak{j} } = \mathfrak{N}$.

If $\sqrt{ \mathfrak{a} } = \mathfrak{N}$, then clearly $\mathfrak{a} \subseteq \sqrt{ \mathfrak{a} } = \mathfrak{N}$. Conversely, suppose $\mathfrak{a} \subseteq \mathfrak{N}$. Then, each $a \in \sqrt{ \mathfrak{a} }$ has $a^n$ nilpotent, and thus, is itself nilpotent. That is, $\sqrt{ \mathfrak{a} } \subseteq \mathfrak{N}$. However, $(0) \subseteq \mathfrak{a}$, and so we also have $\mathfrak{N} = \sqrt{ (0) } \subseteq \sqrt{ \mathfrak{a} }$. That is, $\sqrt{ a } = \mathfrak{N}$ is equivalent to $\mathfrak{a} \subseteq \mathfrak{N}$. Thus, we can continue our chain of equivalences as follows.

Equivalently, for any ideals with $\mathfrak{i} \mathfrak{j} \subseteq \mathfrak{N}$ we have $\mathfrak{i} \subseteq \mathfrak{N}$ or $\mathfrak{j} \subseteq \mathfrak{N}$. Equivalently, $\mathfrak{N}$ is prime.

---

##### _corollary:_ integral domains have irreducible affine schemes

If $A$ is an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]], then $\operatorname{Spec} A$ is irreducible.

---

Note that this means, for example, that $\mathbb{A}^n_{\mathbb{F}}$ is always irreducible. This can also be helpful for more tricky examples.

##### _example:_ proving a ring is a domain is hard but worth it

Suppose $\mathfrak{i} = (wz - xy, wy - x^{2}, xz - y^{2}) \subseteq \mathbb{F}[w, x, y, z]$. Then we can show that $\operatorname{Spec} \mathbb{F}[w, x, y, z] / \mathfrak{i}$ is irreducible by showing that $\mathbb{F}[w, x, y, z] / \mathfrak{i}$ is an integral domain.

>[!missing]
>proof

---

We can always decompose a topological space into irreducible pieces in a relatively nice way.

##### _definition:_ irreducible component

An **irreducible component** of $X$ is a maximal irreducible subset.

---

Note that an irreducible component is always closed since the closure of an irreducible subset is irreducible.

##### _proposition:_ every topological space is the union of irreducible components

Every point $p \in X$ is contained in an irreducible component.

###### _proof:_

Consider the poset of irreducible subsets of $X$ and a maximal totally ordered subset. Suppose $\{ Z_{\alpha} \}$ describes the chain of irreducible subsets of $X$ containing some irreducible $Y$. Then we claim $Z = \bigcup_{\alpha} Z_{\alpha}$ is irreducible, and thus, is the maximal irreducible set containing $Y$.

Suppose $Z = Y_{1} \cup Y_{2}$ is the union of closed subsets. Then each $Z_{\alpha}$ is in either $Y_{1}$ or $Y_{2}$. If each $Z_{\alpha}$ is contained in both, then $Z$ is contained in both. Else, there is some $Z_{\beta}$ with $Z_{\alpha} \not \subseteq Y_{1}$ (say). All the $Z_{\alpha}$ contained in $Z_{\beta}$ have $Z_{\alpha} \subseteq Z_{\beta} \subseteq Y_{2}$. All the  containing $Z_{\beta}$ are also not contained in $Y_{1}$, and thus, are all contained in $Y_{2}$. Since the poset is totally ordered, these are all the $Z_{\alpha}$. That is all the $Z_{\alpha}$ and their union $Z$ are contained in $Y_{2}$.

Since every point $p$ is contained in the irreducible set $\{ p \}$, it is contained in the maximal irreducible component containing that set.

---

### Noetherian topological spaces

Noetherian topological spaces are spaces that break up into finitely many irreducible components in a nice way. However, we have to be a little careful because a Noetherian scheme isn't just a scheme that is topologically Noetherian — there's a [[Algebraic geometry --- rising-sea/notes/Noetherian rings and modules#_definition _ Noetherian rings|ring-theoretic notion]] of Noetherianness too.

##### _definition:_ Noetherian topological spaces

$X$ is a **Noetherian topological space** if any descending chain of closed subsets is eventually constant. 

That, is for any chain $Z_{1} \supseteq Z_{2} \supseteq \cdots$, there is some $r$ such that $Z_{r} = Z_{r + i}$ for all $i \in \mathbb{N}$.

---

##### _example:_ Zariski is Noetherian, Euclidean is not

$\mathbb{A}_{\mathbb{C}}^{2}$ is Noetherian since it is $\operatorname{Spec} A$ of a Noetherian ring (by the [[Algebraic geometry --- rising-sea/notes/Noetherian rings and modules#_theorem _ the Hilbert basis theorem|Hilbert basis theorem]]).

In contrast, the analytic space $\mathbb{C}^{2}$ that it models is not Noetherian. For example, consider the descending chain given by taking the whole space, and then cutting out one disjoint ball after another, from the origin all the way to infinity.

---

We now show that Noetherian spaces have the property we want.

##### _proposition:_ Noetherian spaces break up into finitely many irreducible components

Suppose $X$ is Noetherian. Then every non-empty closed subset $Z$ can be expressed uniquely as $Z = Z_{1} \cup \dots \cup Z_{n}$, a finite union of irreducible closed subsets, none contained in any other.

###### _proof:_

We apply what is called **Noetherian induction**.

Consider the collection of non-empty closed subsets that cannot be expressed as a finite union of irreducible closed subsets. Suppose by way of contradiction that it is not empty. Then $Y_{1}$ is one such subset. If it properly contains another one, then let $Y_{2}$ be that one. Construct a descending chain in this manner. This descending chain of closed subsets is eventually constant at and after $Y_{r}$.

$Y_{r}$ cannot be written as desired (and thus, is not itself irreducible), but all of its proper closed subsets can. Thus, write $Y_{r} = Y' \cup Y''$ for two proper closed subsets of $Y_{r}$. Using the decompositions of $Y'$ and $Y''$, we get $Y_{r}$ as the union of finitely many irreducible closed subsets. This is a contradiction to our assumption that the descending chain was non-empty.

We now have each non-empty closed set $Z = Z_{1} \cup \dots \cup Z_{n}$ as a finite union of irreducible closed subsets. If any are contained in any other, we can get rid of them, and thus obtain the desired decomposition. We are only left to show uniqueness.

Suppose $Z_{1} \cup \dots \cup Z_{m} = Y_{1} \cup \dots \cup Y_{n}$ are unions of irreducible closed subsets, none contained in any other. Then by irreducibility, we have $Z_{1} \subseteq Y_{i}$ for some $Y_{i}$. Similarly, $Y_{i} \subseteq Z_{j}$ for some $j$. We can only have $Z_{1} \subseteq Y_{i} \subseteq Z_{j}$ if $j = 1$ (otherwise we would have one closed set contained in some other). Thus, we have $Z_{1} = Y_{i}$ and similarly, each $Y_{i}$ is some $Z_{j}$ and vice versa.

---

The connected components of Noetherian topological spaces are also nicer than is generally true.

##### _proposition:_ Noetherian spaces have open connected components

If $X$ is Noetherian, then any union of connected components of $X$ is both open and closed.

###### _proof:_

Since each irreducible component is connected, there can be at most finitely many connected components. Each of them is closed. Since any union of them is finite, it is closed. 

For each connected component, its complement is a finite union of connected components, and thus, closed. Thus, it is itself open. Thus, any union of them is open.

---

Noetherian rings also satisfy another reasonableness property. Noetherian affine schemes are not just quasicompact — all of their open subsets are.

##### _proposition:_ Noetherian spaces have (quasi)compact open subsets

If $X$ is Noetherian, every open subset $U$ is [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes|quasicompact]].

###### _proof:_

Suppose $\{ U_{i} \}$ is an open cover of $U$. Consider all $K_{i} = X \setminus U_{i}$. Eventually the chain of all $\bigcap_{i = 1}^n K_{i}$ stabilises. That is, there is some finite $N$ such that $\bigcap_{i = 1}^N K_{i} = \bigcap_{i} K_{i} = \text{Ø}$. That is, $X \setminus \bigcup_{i = 1}^N U_{i}$ is empty, and $U_{1}, \dots, U_{N}$ form an open subcover.

---

### Quasicompactness

**Quasicompactness** is just topological compactness —

![[Topology --- math-147/notes/Compactness#_definition _ compact|Compactness]]

However, we don't call this compactness because it isn't quite the right notion for schemes. In fact, all affine schemes are compact.

![[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_corollary _ every affine scheme is quasicompact|The base of distinguished open sets]]

Since we don't want something like $\mathbb{A}_{\mathbb{C}}^1$ to be compact, we will use a different idea — properness. However, quasicompactness is still useful.

For this reason we recall some properties of quasicompact spaces.

![[Topology --- math-147/notes/Compactness#_proposition _ finite unions of compact sets are compact|Compactness]]

![[Topology --- math-147/notes/Compactness#_proposition _ closed subspaces of compact spaces are compact|Compactness]]