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

If $\mathfrak{i}_{\bullet} \subseteq S_{\bullet}$, we define the vanishing set of $\mathfrak{i}_{\bullet}$ the same way. Note that if $T$ generates $\mathfrak{i}_{\bullet}$, then $V(T) = V(\mathfrak{i}_{\bullet})$.

If $f$ is a homogeneous element of positive degree, we define $V(f) = V(\{ f \})$. We will later give this the structure of a closed subscheme.

The **projective distinguished open** corresponding to $f$ (homogeneous, of positive degree) is $D_{+}(f) = \operatorname{Proj} S_{\bullet} \setminus V(f)$. We will give this the structure of an (affine) open subscheme.

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

Another proof follows from the fact that this is the [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subspace topology]] induced by viewing $\operatorname{Proj} S_{\bullet}$ as a subspace of $\operatorname{Spec} S$ with its [[Algebraic geometry --- rising-sea/notes/Affine schemes#The space (the Zariski topology)|Zariski topology]].

---

... and the distinguished opens form a basis.

##### _proposition:_ the projective distinguished opens form a basis

The projective distinguished opens $D_{+}(f)$ form a [[Topology --- math-147/notes/Bases#_definition _ basis|basis]] of the Zariski topology on $\operatorname{Proj} S_{\bullet}$.

###### _proof:_

Clearly each $D_{+}(f)$ is open.

Suppose $U = \operatorname{Proj} S_{\bullet} \setminus V(\mathfrak{i}_{\bullet})$ is an open subset. We can write $U$ as a union of $D_{+}(f)$ as below.

We first look at all the (relevant) homogeneous primes that don't contain an element of $\mathfrak{i}_{\bullet}$ of positive degree.
$$
V = \bigcup_{f \in \mathfrak{i}_{+}} D_{+}(f) = \operatorname{Proj} S_{\bullet} \setminus \bigcap_{f \in \mathfrak{i}_{+}} V(f) = \operatorname{Proj} S_{\bullet} \setminus \{ \mathfrak{p}_{\bullet} \mid \mathfrak{i}_{+} \subseteq \mathfrak{p}_{\bullet}, S_{+} \not \subseteq  \mathfrak{p}_{\bullet} \}.
$$
Note that this is almost all of $U$ — this excludes all homogeneous primes that contain $\mathfrak{i}_{+}$. However we only want to exclude homogeneous primes that contain both $\mathfrak{i}_{+}$ and $\mathfrak{i}_{0}$ and thus, all of $\mathfrak{i}_{\bullet}$. Thus, it suffices to write $W = \operatorname{Proj} S_{\bullet} \setminus \{ \mathfrak{p}_{\bullet} \mid \mathfrak{i}_{0} \subseteq \mathfrak{p}_{\bullet}, S_{+} \not \subseteq \mathfrak{p}_{\bullet} \}$ as a union of projective distinguished opens. Then $U = V \cup W$ is a union of projective distinguished opens. 

For $f_{0} \in S_{0}$, we have that the set of homogeneous primes not containing $f_{0}$ is just $W_{f_{0}} = \bigcup_{\deg g \geq 1} D_{+}(f_{0} g)$ since any homogeneous prime containing $f_{0}$ must contain some pure positive degree $f_{0} g$ (as long as the ring contains elements of non-zero degree). Thus, we can write $W = \bigcup_{f_{0} \in \mathfrak{i}_{0}} W_{f_{0}}$ and we are done.

Note that it may be easier to prove this is a basis indirectly — showing that every open neighbourhood of a point has a basic open sub-neighbourhood. [[Topology --- math-147/notes/Bases#_proposition _ equivalent conditions to be a basis of a specific topology|This suffices]]!

---

We can prove analogues of the facts we know about the [[Algebraic geometry --- rising-sea/notes/Affine schemes#The space (the Zariski topology)|topology of affine schemes]].

##### _proposition:_ vanishing sets uniquely identify radical ideals

Suppose $\mathfrak{i}_{\bullet}, \mathfrak{j}_{\bullet} \subseteq S_{\bullet}$ are homogeneous ideals contained in $S_{+}$. Then $V({ \mathfrak{i}_{\bullet} }) = V(\mathfrak{j}_{\bullet})$ if and only if $\sqrt{ \mathfrak{i}_{\bullet} } = \sqrt{ \mathfrak{j}_{\bullet} }$.

###### _proof:_
follows exactly as in the [[Algebraic geometry --- rising-sea/notes/Affine schemes#_proposition _ vanishing sets uniquely identify only radical ideals|affine case]].

---

##### _corollary:_ containment of projective distinguished opens

Suppose $f, g \in S_{\bullet}$ are homogeneous and of positive degree. Then $D_{+}(f) \subseteq D_{+}(g)$ if and only if $f \in \sqrt{ (g) }$.

###### _proof:_
follows exactly as in the [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_proposition _ containment of distinguished opens|affine case]].

---

##### _proposition:_ intersections of projective distinguished opens are distinguished

Suppose $f, g \in S_{\bullet}$ are homogeneous and of positive degree. Then the intersection of their projective distinguished opens is $D_{+}(f) \cap D_{+}(g) = D_{+}(fg)$.

###### _proof:_
follows exactly as in the [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_proposition _ intersections of distinguished opens are distinguished|affine case]].

---

We can also define an ideal of vanishing functions.

##### _definition:_ projective ideal of vanishing functions

Given $Z \subseteq \operatorname{Proj} S_{\bullet}$, the **(projective) ideal of vanishing functions** on $Z$ is the set of all functions in $S_{\bullet}$ with $Z \subseteq V(f)$. It is denoted $I(Z)$ and is given by
$$
I(Z) = \bigcap_{\mathfrak{p}_{\bullet} \in Z} \mathfrak{p}_{\bullet} \subseteq S_{\bullet}.
$$

---

Note this latter definition makes clear that $I(Z)$ is an ideal and is homogeneous.

##### _proposition:_ vanishing functions on unions

For any two subsets $Z_{1}, Z_{2} \subseteq \operatorname{Proj} S_{\bullet}$, we have $I(Z_{1} \cup Z_{2}) = I(Z_{1}) \cap I(Z_{2})$.

###### _proof:_

$$
\begin{align}
I(Z_{1} \cup Z_{2}) & = \bigcap_{\mathfrak{p}_{\bullet} \in Z_{1} \cup Z_{2}} \mathfrak{p}_{\bullet} \subseteq S_{\bullet} \\ \\
& = \bigcap_{\mathfrak{p}_{\bullet} \in Z_{1}} \mathfrak{p_{\bullet}} \cap \bigcap_{\mathfrak{p}_{\bullet} \in Z_{2}} \mathfrak{p}_{\bullet} \\
& = I(Z_{1}) \cap I(Z_{2}).
\end{align}
$$

---

##### _proposition:_ Zariski closures

For any $Z \subseteq \operatorname{Proj} S_{\bullet}$, we have $V(I(Z)) = \bar{Z}$.

###### _proof:_

Suppose $\mathfrak{q}_{\bullet} \in V(I(Z))$. Then $\mathfrak{q}_{\bullet} \supseteq \bigcap_{\mathfrak{p}_{\bullet} \in Z} \mathfrak{p}_{\bullet}$. For any closed set $V(\mathfrak{i}_{\bullet}) \supseteq Z$, we have $\mathfrak{i}_{\bullet} \subseteq \mathfrak{p}_{\bullet}$ for all $\mathfrak{p}_{\bullet} \in Z$. That is,
$$
\mathfrak{i}_{\bullet} \subseteq \bigcap_{\mathfrak{p}_{\bullet} \in Z} \mathfrak{p}_{\bullet} \subseteq \mathfrak{q}_{\bullet}.
$$
and thus, $\mathfrak{q}_{\bullet} \in V(\mathfrak{i}_{\bullet})$. That is, $\mathfrak{q}_{\bullet}$ is in every closed set containing $Z$, and thus in the closure of $Z$.

Since $I(Z) \subseteq \mathfrak{p}_{\bullet}$ for each prime $\mathfrak{p}_{\bullet}$ in $Z$, we have $Z \subseteq V(I(Z))$ and thus, $\bar{Z} \subseteq V(I(Z))$ as well.

---

##### _proposition:_ the irrelevant ideal really is irrelevant

For any homogeneous ideal $\mathfrak{i}_{\bullet} \subseteq S_{\bullet}$. Then the following are equivalent
1) $V(\mathfrak{i}_{\bullet})= \text{Ø}$
2) For any homogeneous generating set $\mathfrak{i}_{\bullet} = (f_{j})_{j \in \mathscr{J}}$, we have $\bigcup_{\deg f_{j} \geq 1} D_{+}(f_{j}) = \operatorname{Proj} S_{\bullet}$
3) $S_{+} \subseteq \sqrt{ \mathfrak{i}_{\bullet} }$

###### _proof:_

Suppose $V(\mathfrak{i}_{\bullet}) = \text{Ø}$. Then every homogeneous prime must exclude some homogeneous positive degree element of $\mathfrak{i}_{\bullet}$. Thus, $\bigcup_{\deg f_{j} \geq 1} D_{+}(f_{j}) = \operatorname{Proj} S_{\bullet}$. (Some technical details about homogeneous generators in degree $0$ are missing here).

Suppose that for any homogeneous generating set $\mathfrak{i}_{\bullet} = (f_{j})_{j \in \mathscr{J}}$, we have $\bigcup_{\deg f_{j} \geq 1} D_{+}(f_{j}) = \operatorname{Proj} S_{\bullet}$. Thus, every relevant homogeneous prime excludes one of the $f_{j}$. Equivalently, all homogeneous primes containing $\mathfrak{i}_{\bullet}$ contain $S_{+}$. By our proof that [[Algebraic geometry --- rising-sea/notes/Graded rings#_corollary _ homogeneity is closed under sum, product, intersection, radical|radicals of homogeneous ideals are homogeneous]], this is the same as requiring that all primes containing $\mathfrak{i}_{\bullet}$ contain $S_{+}$ or equivalently $S_{+} \subseteq \sqrt{ \mathfrak{i}_{\bullet} }$.

Suppose $S_{+} \subseteq \sqrt{ \mathfrak{i}_{\bullet} }$. Since any homogeneous prime ideal containing $\mathfrak{i}_{\bullet}$ contains $\sqrt{ \mathfrak{i}_{\bullet} }$ this tells us that there are no relevant prime ideals containing $\mathfrak{i}_{\bullet}$. That is, $V(\mathfrak{i}_{\bullet}) = \text{Ø}$.

---

That is, any irrelevant ideal corresponds to functions in $S_{\bullet}$ that have no topologically relevant content.

### ... as a scheme

Finally, we can think of these distinguished opens as affine opens. It is tricky to show this at the level of sets.

##### _proposition:_ the affine cover of a projective scheme as sets

There is a natural bijection of sets between $D_{+}(f)$ and $\operatorname{Spec} ((S_{\bullet})_{f})_{0}$.

###### _proof:_

We show that for a $\mathbb{Z}$-graded ring $R_{\bullet}$ with a homogeneous invertible $f$ of positive degree, there is a natural bijection between the prime ideals of $R_{0}$ and the relevant homogeneous prime ideals of $R_{\bullet}$. Applying this to the case of $R_{\bullet} = (S_{\bullet})_{f}$ yields a bijection between relevant homogeneous primes not containing $f$ (that is, $D_{+}(f)$) and primes of $((S_{\bullet})_{f})_{0}$ as desired.

Let $R_{0} \to R_{\bullet}$ be the natural ring map. Contracting homogeneous primes $\mathfrak{p}_{\bullet}$ along this map gives $\mathfrak{p}_{0} \in \operatorname{Spec} R_{0}$. Conversely, consider a prime $\mathfrak{p}_{0} \subseteq R_{0}$. We claim that extending and taking radicals gives a relevant homogeneous prime ideal $\mathfrak{p}_{\bullet} = \sqrt{ \mathfrak{p}_{0} A_{\bullet} }$ that contracts to $\mathfrak{p}_{0}$. These two functions are then inverses, giving the desired bijection.

Finally, we show that $\mathfrak{p}_{\bullet}$ contracts to $\mathfrak{p}_{0}$. Suppose $g \in \mathfrak{p}_{\bullet}$ has degree $0$. Then $g^n \in \mathfrak{p}_{0} A_{\bullet}$. In fact, since $g^n$ has degree zero, we have $g^n \in \mathfrak{p}_{0}$. Since primes are radical, we have $g \in \mathfrak{p}_{0}$ as well. That is, $\mathfrak{p}_{\bullet} \cap A_{0} \subseteq \mathfrak{p}_{0}$. It's clear that the opposite inclusion holds — $\mathfrak{p}_{0} \subseteq \mathfrak{p}_{0} A_{\bullet} \cap A_{0} \subseteq \mathfrak{p}_{\bullet} \cap A_{0}$.

First we show that $\mathfrak{p}_{\bullet}$ is homogeneous and relevant. Homogeneity follows from the fact that $\mathfrak{p}_{0} A_{\bullet}$ is homogeneous (it is generated by the degree $0$ set $\mathfrak{p}_{0}$). Relevance follows since $f \not\in \mathfrak{p}_{\bullet}$. If $f \in \mathfrak{p}_{\bullet}$, then we would have $1 \in \mathfrak{p}_{\bullet}$. Since $\mathfrak{p}_{\bullet}$ contracts to $\mathfrak{p}_{0}$, this would imply $1 \in \mathfrak{p}_{0}$ which is false since $\mathfrak{p}_{0}$ is prime.

Finally, we show $\mathfrak{p}_{\bullet}$ is prime. [[Algebraic geometry --- rising-sea/notes/Graded rings#_corollary _ it suffices to check primeness at homogeneous elements|It suffices to check this at homogeneous elements]]. Suppose $gh \in \mathfrak{p}_{\bullet}$ with $g, h$ both homogeneous of degrees $d_{1}, d_{2}$ respectively. Thus, $g^n h^n \in \mathfrak{p}_{0} A_{\bullet}$ for all $n$ larger than some integer. Choose $n$ so that it is divisible by $\deg f$; then choose $m$ so that $\deg(g^n h^n / f^m) = 0$. Thus, $g^n h^n/f^m \in \mathfrak{p}_{0}$. By primeness, one of $g^n$ or $h^n / f^m$ is in $\mathfrak{p}_{0}$. Thus, $g^n$ or $h^n$ is in $\mathfrak{p}_{0} A_{\bullet}$, and finally, one of $g$ or $h$ is in $\mathfrak{p}_{\bullet} = \sqrt{ \mathfrak{p}_{0} A_{\bullet} }$.


---

##### _proposition:_ the affine cover of a projective scheme as topological spaces

The natural map $D_{+}(f) \to \operatorname{Spec}((S_{\bullet})_{f})_{0}$ is a homeomorphism (with $D_{+}(f) \subseteq \operatorname{Proj} S_{\bullet}$ given the [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subspace topology]]).

###### _proof:_

Since pre-images commute with unions, it suffices to check that every distinguished open $D(g) \subseteq \operatorname{Spec}((S_{\bullet})_{f})_{0}$ pulls back to an open set and that every projective distinguished open $D_{+}(fg)$ has open image.

$D(g)$ consists of all primes $\mathfrak{p}_{0}$ not containing $g$. The homogeneous primes $\mathfrak{p}_{\bullet} \in D_{+}(f)$ that contract to primes not containing $g$ also must not contain $g$. In fact, all $\mathfrak{p}_{\bullet} \in D_{+}(f)$ that do not contain $g$ contract to $\mathfrak{p}_{0}$ not containing $g$. These are exactly the $\mathfrak{p}_{\bullet} \in D_{+}(f) \cap D_{+}(g) = D_{+}(fg)$. Since the map is a bijection we have that $D(g)$ has pre-image $D_{+}(fg)$ and $D_{+}(fg)$ has image $D(g)$.

---

##### _proposition:_ gluing sheaves over the affine cover of a projective scheme

Given projective distinguished opens $D_{+}(f), D_{+}(g) \subseteq \operatorname{Proj} S_{\bullet}$, there is an isomorphism between the interpretations of $D_{+}(f) \cap D_{+}(g) = D_{+}(fg)$ as a subset of the affines $D_{+}(f)$, $D_{+}(g)$, and as an affine open of $\operatorname{Proj} S_{\bullet}$. 

The isomorphism is given by
$$
D_{+}(fg) = \operatorname{Spec} ((S_{\bullet})_{fg})_{0} \cong D(g^{\deg f} / f^{\deg g}) \subseteq \operatorname{Spec} ((S_{\bullet})_{f})_{0}
$$
and is the restriction of the isomorphism $D_{+}(f) \cong \operatorname{Spec} ((S_{\bullet})_{f})_{0}$.

###### _proof:_

Write $g_{f} = g^{\deg f} / f^{\deg g}$. Then we want to show that $((S_{\bullet})_{fg})_{0} \cong (((S_{\bullet})_{f})_{0})_{g / f}$. Suppose $\deg s = m \deg f + n \deg g$. Then we write
$$
\frac{s}{f^m g^n} \mapsto \frac{s g^{n (\deg f - 1) }}{f^m f^{n (\deg g)} g_{f}^n}
$$
This is a ring homomorphism since it is just scaling when the addition is in the numerator. This is clearly injective. It is also surjective — for any $t$ with $\deg t = k \deg f$  and arbitrary $\ell$ we have
$$
\begin{align}
\frac{t f^{\ell (\deg g)}}{f^k g^{\ell (\deg f)}} & \mapsto \frac{t f^{\ell (\deg g)} g^{\ell (\deg f)(\deg f - 1)}}{f^k f^{\ell (\deg f) (\deg g)} g_{f}^{\ell (\deg f)}}  \\
 & = \frac{t g^{\ell (\deg f) (\deg f - 1)}}{f^k f^{\ell (\deg g) (\deg f - 1)} g_f^{\ell (\deg f)}} \\
 & = \frac{t}{f^k g_{f}^\ell}.
\end{align}
$$

>[!missing]
> (deliberately) the cocycle condition

---

Since the affine open cover we defined is coherent scheme-theoretically on intersections, [[Algebraic geometry --- rising-sea/notes/Schemes#_proposition _ gluing schemes|it glues to form a scheme]]!

##### _definition:_ $\operatorname{Proj} S_{\bullet}$ as a scheme

$\operatorname{Proj} S_{\bullet}$ is the unique scheme with set and Zariski topology as defined above, and each $D_{+}(f)$ isomorphic to $\operatorname{Spec} ((S_{\bullet})_{f})_{0}$ with the isomorphism as given above.

---

Note that this implies the stalk of $\mathscr{O}_{\operatorname{Proj} S_{\bullet}}$ at $\mathfrak{p}_{\bullet}$ is just $(((S_{\bullet})_{f})_{0})_{\mathfrak{p}_{0}}$ for some $f \not\in \mathfrak{p}_{\bullet}$. Note that since the $D_{+}(f)$ form a basis of $\operatorname{Proj} S_{\bullet}$, we can get any germ as an honest element of $((S_{\bullet})_{f})_{0}$ by choosing the right $f$.

##### _definition:_ vanishing subschemes of projective schemes

Suppose $S_{\bullet}$ is generated in degree $1$, and $f \in S_{+}$ is homogeneous. Then the **vanishing scheme of $f$** is the set of points where $f$ vanishes — $V(f) = \{ \mathfrak{p}_{\bullet} \mid f \in \mathfrak{p}_{\bullet} \}$, given the scheme structure of $\operatorname{Proj} S_{\bullet} / (f)$.

In general, if $\mathfrak{i}_{\bullet} \subseteq S_{\bullet}$ is a homogeneous ideal, then we can define the **vanishing scheme of $\mathfrak{i}_{\bullet}$** as $V(\mathfrak{i}_{\bullet})$ given the scheme structure of $\operatorname{Proj} S_{\bullet} / \mathfrak{i}_{\bullet}$. 

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