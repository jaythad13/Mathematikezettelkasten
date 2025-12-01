---
tags:
- rising-sea/4/5
- alg-geo
---

Basically any scheme you could care about (for non-pathological reasons) is projective or an open [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#Quasicompactness|quasicompact]] subset of a projective scheme (so quasiprojective). These are basically all the projective schemes cut out by homogeneous polynomials in [[Algebraic geometry --- rising-sea/notes/Examples of schemes#_definition _ projective $n$-space over a ring|projective space]] and their quasicompact opens.

### Real projective geometry and projective schemes informally

In smooth geometry and topology we think of $\mathbb{R} \mathbb{P}^n$ as the manifold parameterising the lines through the origin in $\mathbb{R}^{n + 1}$. If we think of $\mathbb{R}^{n + 1}$ as a ball, we can think of $\mathbb{R} \mathbb{P}^n$ as the bounding sphere with opposite points identified. Then $\mathbb{P}^{n + 1}$ is both, the ball $\mathbb{R}^{n + 1}$ and the bounding sphere $\mathbb{R} \mathbb{P}^n$.

Homogeneous equations in the $n + 1$ variables of $\mathbb{R}^{n + 1}$ cut out a closed union of lines in $\mathbb{R}^{n + 1}$ called the **affine cone** (of $V$), and a "variety" or "manifold" $V$ in $\mathbb{P}^n$. Finally the union of $V$ and its affine cone is the **projective cone** of $V$.

##### _example:_ a literal cone

$x^{2} + y^{2} = z^{2}$ cuts out a cone shape as its affine cone in $\mathbb{R}^3$, a copy of $\mathbb{R} \mathbb{P}^1 \cong S^1$ in $\mathbb{R} \mathbb{P}^2$, and their union looks like a closed compact cone in the ball.

---

### The $\operatorname{Proj}$ construction ...

Let $S_{\bullet}$ be a graded ring.

The $\operatorname{Proj}$ construction constructs the projective scheme from any give affine cone specified by a [[Algebraic geometry --- rising-sea/notes/Graded rings#_definition _ $ mathbb{Z}$-graded rings, homogeneous elements, degree|graded ring]]. That is, $\operatorname{Proj} \mathbb{C}[x, y, z] / (x^{2} + y^{2} - z^{2})$ defines the scheme analogue of the subset of $\mathbb{C} \mathbb{P}^{2}$ cut out by $x^{2} + y^{2} = z^{2}$. Just like with $\operatorname{Spec} A$, we define $\operatorname{Proj} S_{\bullet}$ first as a set, then a topological space, and finally as a scheme.

### ... as a set

##### _definition:_ the set/points of $\operatorname{Proj} S_{\bullet}$

The points of $\operatorname{Proj} S_{\bullet}$ are the homogeneous prime ideals $\mathfrak{p}_{\bullet}$ that do not contain the [[Algebraic geometry --- rising-sea/notes/Graded rings#_definition _ irrelevant ideal|irrelevant ideal]].

---

### ... as a topological space

Just as we can define the notion of [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition _ vanishing set|vanishing loci]] of functions on an affine scheme, we can define the vanishing locus of homogeneous functions $f \in S_{\bullet}$ on the projective scheme $\operatorname{Proj} S_{\bullet}$. However, if we required these to be actual (or rather, non-actual, sheafy) functions on $\operatorname{Proj} S_{\bullet}$. For example, $\mathbb{P}_{\mathbb{F}}^2 = \operatorname{Proj} \mathbb{F}[x_{0}, x_{1}, x_{2}]$ has only constants in $\mathbb{F}$ as global functions. However, all of $\mathbb{F}[x_{0}, x_{1}, x_{2}]$ are global functions on the affine cone $\mathbb{A}_{\mathbb{F}}^{3}$. We look at the vanishing sets of these homogeneous global functions.

##### _definition:_ homogeneous vanishing sets, projective distinguished open

If $T \subseteq S_{\bullet}$ is a set of homogeneous elements of $S_{\bullet}$, the **vanishing set** of $T$ is the set of homogeneous prime ideals containing $T$ but not $S_{+}$ —
$$
V(T) = \{ \mathfrak{p}_{\bullet} \subseteq S_{\bullet} \mid T \subseteq \mathfrak{p}_{\bullet}, S_{+} \not\subseteq \mathfrak{p}_{\bullet} \}.
$$

If $\mathfrak{i}_{\bullet} \subseteq S_{\bullet}$, we define the vanishing set of $\mathfrak{i}_{\bullet}$ the same way. 

If $f$ is a homogeneous element of positive degree, we define $V(f) = V(\{ f \})$.

The **projective distinguished open** corresponding to $f$ (homogeneous, of positive degree) is $D_{+}(f) = \operatorname{Proj} S_{\bullet} \setminus V(f)$.

---

These vanishing sets define the topology on $\operatorname{Proj} S_{\bullet}$ ...

##### _definition, proposition:_ the Zariski topology on a projective scheme

The **Zariski topology on the projective scheme** $\operatorname{Proj} S_{\bullet}$ with closed sets defined to be exactly the $V(\mathfrak{i}_{\bullet})$ for homogeneous $\mathfrak{i}_{\bullet}$ is a topology.

Specifically,
1) $V(0) = \operatorname{Proj} S_{\bullet}$
2) $V(1) = \text{Ø}$
3) $\bigcap_{j \in \mathscr{J}} V(\mathfrak{i}_{\bullet, j}) = V\left( \sum_{j \in \mathscr{J}} \mathfrak{i}_{\bullet, j} \right)$
4) $V(\mathfrak{i}_{\bullet}) \cup V(\mathfrak{j}_{\bullet}) = V(\mathfrak{i}_{\bullet} \mathfrak{j}_{\bullet}) = V(\mathfrak{i}_{\bullet} \cap \mathfrak{j}_{\bullet})$

###### _proof:_
follows exactly as in the [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition, proposition _ the Zariski topology (is a topology)|affine case]] (because we only use properties of primeness, requiring homogeneity changes nothing in the proofs).

---

... and the distinguished opens form a basis.

##### _proposition:_ the projective distinguished opens form a basis

The projective distinguished opens $D_{+}(f)$ form a [[Topology --- math-147/notes/Bases#_definition _ basis|basis]] of the Zariski topology on $\operatorname{Proj} S_{\bullet}$.

---

We can prove analogues of the facts we know about the [[Algebraic geometry --- rising-sea/notes/Affine schemes#The space (the Zariski topology)|topology of affine schemes]].

##### _proposition:_ vanishing sets uniquely identify radical ideals

Suppose $\mathfrak{i}_{\bullet}, \mathfrak{j}_{\bullet} \subseteq S_{\bullet}$ are homogeneous ideals contained in $S_{+}$. Then $V({ \mathfrak{i}_{\bullet} }) = V(\mathfrak{j}_{\bullet})$ if and only if $\sqrt{ \mathfrak{i}_{\bullet} } = \sqrt{ \mathfrak{j}_{\bullet} }$.

---

##### _corollary:_ containment of projective distinguished opens

If $f, g \in S_{\bullet}$ are homogeneous and of positive degree. Then $f^n \in (g)$.

---

We can also define an ideal of vanishing functions.

##### _definition:_ the ideal of vanishing functions

---

##### _proposition:_ vanishing functions on unions

For any two subsets $Z_{1}, Z_{2} \subseteq \operatorname{Proj} S_{\bullet}$, we have $I(Z_{1} \cup Z_{2}) = I(Z_{1} \cap Z_{2})$.

##### _proposition:_ Zariski closures

For any $Z \subseteq \operatorname{Proj} S_{\bullet}$, we have $V(I(Z)) = \bar{Z}$.

---

##### _proposition:_ the irrelevant ideal really is irrelevant

For any homogeneous ideal $\mathfrak{i}_{\bullet} \subseteq S_{\bullet}$. Then the following are equivalent
1) $V(\mathfrak{i}_{\bullet})= \text{Ø}$
2) For any homogeneous generating set $\mathfrak{i}_{\bullet} = (f_{j})_{j \in \mathscr{J}}$, we have $\bigcup_{j \in \mathscr{J}} D_{+}(f_{j}) = \operatorname{Proj} S_{\bullet}$
3) $S_{+} \subseteq \sqrt{ \mathfrak{i}_{\bullet} }$

---

That is, any irrelevant ideal corresponds to functions in $S_{\bullet}$ that have no topologically relevant content.

### ... as a scheme

Finally, we can think of these distinguished opens as affine opens. It is tricky to show this at the level of sets.

##### _proposition:_ the affine cover of a projective scheme as sets

There is a natural bijection of sets between $D_{+}(f)$ and $\operatorname{Spec} ((S_{\bullet})_{f})_{0}$.

---

##### _proposition:_ the affine cover of a projective scheme as topological spaces

The natural map $D_{+}(f) \to \operatorname{Spec}((S_{\bullet})_{f})_{0}$ is a homeomorphism (with $D_{+}(f) \subseteq \operatorname{Proj} S_{\bullet}$ given the [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subspace topology]])

---

##### _proposition:_ gluing sheaves over the affine cover of a projective scheme

Given projective distinguished opens $D_{+}(f), D_{+}(g) \subseteq \operatorname{Proj} S_{\bullet}$, there is an isomorphism between the interpretations of $D_{+}(f) \cap D_{+}(g) = D_{+}(fg)$ as a subset of the affines $D_{+}(f)$, $D_{+}(g)$, and as an affine open of $\operatorname{Proj} S_{\bullet}$. 

The isomorphism is given by
$$
D_{+}(fg) = \operatorname{Spec} ((S_{\bullet})_{fg})_{0} \cong D(g^{\deg f} / f^{\deg g}) \subseteq \operatorname{Spec} ((S_{\bullet})_{f})_{0}
$$
and is the restriction of the isomorphism $D_{+}(f) \cong \operatorname{Spec} ((S_{\bullet})_{f})_{0}$.

---

Since the affine open cover we defined is coherent scheme-theoretically on intersections, [[Algebraic geometry --- rising-sea/notes/Schemes#_proposition _ gluing schemes|it glues to form a scheme]]!

##### _definition:_ $\operatorname{Proj} S_{\bullet}$ as a scheme

$\operatorname{Proj} S_{\bullet}$ is the unique scheme with set and Zariski topology as defined above, and each $D_{+}(f)$ isomorphic to $\operatorname{Spec} ((S_{\bullet})_{f})_{0}$ with the isomorphism as given above.

---

##### _proposition:_ the compatible germs of the structure sheaf of a projective scheme

---

##### _proposition, definition:_ vanishing subschemes of projective schemes

---

### Projective and quasiprojective schemes

##### _definition:_ projective $A$-schemes, quasiprojective $A$-schemes

A scheme (isomorphic to) $\operatorname{Proj} S_{\bullet}$ with $S_{\bullet}$ a finitely generated graded ring over $A$ is a **projective $A$-scheme**.

A **quasiprojective $A$-scheme** is a [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#Quasicompactness|quasicompact]] [[Algebraic geometry --- rising-sea/notes/Schemes#_proposition, definition _ open subschemes, affine open subscheme|open subscheme]] of a projective $A$-scheme.

---

Note that $\operatorname{Proj} S_{\bullet}$ is a scheme even when $S_{\bullet}$ is not finitely generated which is useful. Of course, if $S_{\bullet}$ is a Noetherian ring, [[Algebraic geometry --- rising-sea/notes/Noetherian schemes#_proposition _ Noetherian schemes are Noetherian topological spaces|then so is]] $\operatorname{Proj} S_{\bullet}$ a Noetherian scheme, and [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#_proposition _ Noetherian spaces have (quasi)compact open subsets|thus]], every open subscheme is a quasiprojective scheme.

##### _example:_ affine schemes are projective

Note that $\operatorname{Proj} A[X_{0}] \cong \operatorname{Spec} A$. This is because $S_{+} = (X_{0})$ and $\operatorname{Proj} A[X_{0}] = D_{+}(X_{0})$. The degree zero part of $A[X_{0}, X_{0}^{-1}]$ is just $A$, so $D_{+}(X_{0}) \cong \operatorname{Spec} A$.

---

##### _example:_ projective space as $\operatorname{Proj} A[x_{0}, \dots, x_{n}]$

[[Algebraic geometry --- rising-sea/notes/Examples of schemes#_definition _ projective $n$-space over a ring|Projective space over a ring]] $\mathbb{P}^n_{A}$ is the projective scheme $\operatorname{Proj} A[x_{0}, \dots, x_{n}]$. The variables $x_{0}, \dots, x_{n}$ are called **projective coordinates** on $\mathbb{P}^n_{A}$. To verify this is as simple as checking that the $D_{+}(x_{i})$ cover $\operatorname{Proj} A[x_{0}, \dots, x_{n}]$ since they are isomorphic to $\operatorname{Spec} \mathbb{F}[x_{0} / x_{i}, \dots, x_{n} / x_{i}] = \operatorname{Spec} \mathbb{F}[x_{0 / i}, \dots, x_{n / i}]$. They do in fact cover $\mathbb{P}_{A}^n$ — if a homogeneous prime ideal contains all of $x_{0}, \dots, x_{n}$ then it contains the irrelevant ideal — it is not a point.

---

Note that this means that a closed point $(a_{0} : \dots : a_{n})$ in $\mathbb{P}_{\mathbb{F}}^n$ (for algebraically closed $\mathbb{F}$) corresponds to a homogeneous prime ideal $(x - a_{0}, \dots, x - a_{n})$ in $\operatorname{Proj} \mathbb{F}[x_{0}, \dots, x_{n}]$. 

With our old definition of projective space it would have been difficult to show that the complement of a plane conic $D_{+}(x^{2} + y^{2} - z^{2}) \subseteq \mathbb{P}^2_{\mathbb{F}}$ is affine. Here it is clear that it is $\operatorname{Spec} A$ where $A$ is the degree $0$ part of $\mathbb{F}[x, y, z]_{x^{2} + y^{2} - z^{2}}$.

##### _example:_ the projectivisation of a vector space

We can construct the projectivisation of any finite-dimensional $\mathbb{F}$-vector space $V$ as a projective $\mathbb{F}$-scheme. In particular, the projectivisation of $\mathbb{F}^{n + 1}$ will be $\mathbb{P}^n_{\mathbb{F}}$. We define the projective algebra
$$
\operatorname{Sym}^{\bullet} V = \mathbb{F} \oplus V \oplus \operatorname{Sym}^{2} V \oplus \cdots = \bigoplus_{n = 0}^\infty \operatorname{Sym}^n V.
$$
Then $\mathbb{P} V = \operatorname{Proj} \operatorname{Sym}^\bullet V^\vee$. Here, for $V = \mathbb{F}^n$, we think of the degree one part of $\operatorname{Sym}^\bullet V^\vee$ as generated by functionals $x_{0}, \dots, x_{n + 1}$, and the higher degree parts as just the free powers of these.

This definition really is what we want from the projectivisation of a vector space — the closed points of $\mathbb{P}V$ are in a natural bijection with one-dimensional subspaces of $V$.

>[!missing]
>proof

The presence of the duals in the definition of $\mathbb{P} V$ is so that the points of $\mathbb{P} V$ really do classify one-dimensional subspaces of the vector space. Otherwise, $\operatorname{Proj} \operatorname{Sym}^\bullet V$ classifies one-dimensional quotients of $V$. This is the way that Grothendieck and some other people do it. This is because quotients are better behaved than subobjects for coherent sheaves.

---