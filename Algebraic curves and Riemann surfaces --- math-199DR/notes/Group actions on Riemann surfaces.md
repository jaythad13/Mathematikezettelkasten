---
tags:
- math-199DR/9
- cx-geo
---

Given a Riemann surface $X$, what does $\operatorname{Aut} X$ look like? What are its finite subgroups? By understanding their action on the Riemann surface, we can get better answers to these questions. These in turn, allow us to [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological properties of holomorphisms#_example _ meromorphic functions on non-isomorphic elliptic curves|distinguish Riemann surfaces]].

Further, by squishing these automorphism groups to nothing by quotienting out by these actions we can get new Riemann surfaces. The reverse problem — that of which Riemann surfaces give rise to to all (compact, connected) Riemann surfaces by quotients is exactly [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Riemann surfaces#_theorem _ the uniformisation theorem|the uniformisation theorem]]!

### Reviewing group actions

Recall the definition of a group action,

![[Abstract algebra --- math-171/notes/Group actions#_definition _ (left) group action|Group actions]]

its stabiliser

![[Abstract algebra --- math-171/notes/Group actions#_definition _ stabiliser, free]]

its kernel

![[Abstract algebra --- math-171/notes/Group actions#_definition _ kernel, effective action|Group actions]]

and its orbits.

![[Abstract algebra --- math-171/notes/Group actions#_definition _ orbit|Group actions]]

### Holomorphic, effective actions on Riemann surfaces

Really we don't want to consider just any arbitrary group action on a Riemann surface — we want to consider group actions that respect the Riemann surface structure. Also, we don't want to have to deal with any redundancy in the group action — if a group action $G \circlearrowright X$ has a non-trivial kernel $K$, then the group action that we really want to consider is $(G / K) \circlearrowright X$ (which has trivial kernel).

##### _definition:_ effective, holomorphic group action

A holomorphic group action is a group action such that each function $x \mapsto g \cdot x$ is a [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphism]] $X \to X$.

A group action is [[Abstract algebra --- math-171/notes/Group actions#_definition _ kernel, effective action|effective]] if it has trivial kernel.

Finally, we don't really want to deal with infinite group actions, so we limit ourselves to the actions of finite groups — from here on, every $G \circlearrowright X$ is the holomorphic, effective action of a finite group on a Riemann surface. These have nice properties! 

##### _proposition:_ finite group actions have cyclic stabiliser

Given $G \circlearrowright X$, the stabiliser $\operatorname{stab}_{G}p$ at $p \in X$ is a finite [[Abstract algebra --- math-171/notes/Cyclic groups and subgroups|cyclic group]].

###### _proof:_

Consider, for each $g \in \operatorname{stab}_{G} p$, the holomorphism $p \mapsto g \cdot p$ on $X$, and further, given a choice of charts centred at $p \in X$ (both can be centred at $p$ since $g \cdot p = p$), the holomorphism pushed forward to a holomorphic function on $\mathbb{C}$. Call that function $f_{g}$. Notice that $f_{g}(0) = 0$, and since $g$ induces a bijection on $X$, $f_{g}$ must be injective.

Write the [[Complex analysis --- math-135/notes/Cauchy integral formula#_corollary _ the derivative form (holomorphic functions are smooth and analytic)|power series]] for $f_{g}$ —
$$
f_{g}(z) = \sum_{n = 1}^\infty a_{n} z^n
$$
and construct a [[Abstract algebra --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|homomorphism]] $\lambda : \operatorname{stab}_{G}p \to \mathbb{C}^*$ by picking out linear terms in the power series. That is
$$
\lambda(g) = f_{g}'(0) = a_{1}(f_{g}).
$$
These $\lambda(g)$ must be non-zero — by the $n$[[Complex analysis --- math-135/notes/The argument principle and winding number#_lemma _ the "$n$-to-one" lemma|-to-one lemma]] a function with order $2$ zero at $0$ cannot be injective. Further, it is indeed a homomorphism — for $g, h \in G$ we have
$$
f_{gh}(z) = \sum_{n = 1}^\infty a_{g, n} \left( \sum_{n = 1}^\infty a_{h, n} z^n \right)  = a_{g, n} a_{h, n} z + O(z^{2}).
$$

If we can just show that $\lambda$ is injective, we will have that $\operatorname{stab}_{G}p$ is a finite subgroup of $\mathbb{C}^*$, and thus, cyclic. Suppose $\lambda(g) = 1$. Then $f_{g}(z) = z + O(z^{2})$. Suppose, for all $n < m \ge 2$ we have $a_{n} = 0$. Then $f_{g}(z) = z + a_{m} z^m + O(z^{m + 1})$. Then $f_{g^k}(z) = z + k a_{m} z^{m} + O(z^{m + 1})$ (by some mildly painful induction and algebra). But since $\operatorname{stab}_{G} p$ is finite, $g^k = 1$ for some $k > 0$, and for that $k$, we must have $f_{g^k}(z) = z$. Since $k \neq 0$, we must have $a_{m} = 0$. That is, all $a_{m} = 0$ for $m \ge 2$ and $f_{g}(z) = z$. Since the action of $G$ is effective, $g$ must be the identity.

##### _lemma:_ the set of points with non-trivial stabiliser is discrete

Given $G \circlearrowright X$, the points $p \in X$ with non-trivial stabiliser form a [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete]] [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subset]] of $X$.

###### _proof sketch:_

Suppose there is a sequence of $x_{n} \in X$ converging to $x$ with $g_{n} \in G$ such that $g_{n} \cdot x_{n} = x_{n}$. Since $G$ is finite, there is some $g$ that is chosen infinitely many times. Choose the corresponding subsequence. $g \cdot x_{n_{k}} = x_{n_{k}}$. By compactness, $x_{n_{k}}$ also converges to the same thing, so $g$ [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_theorem _ identity theorem|must act by identity]]. Since $G$ acts effectively, $g$ is the identity. Thus, the stabilisers are eventually trivial, just containing $g = 1_{G}$.

### Quotient Riemann surfaces

Because we're dealing with finite group actions, collapsing all of the orbits into points just looks like folding our Riemann surface rather than anything more perverse. We should be able to make this thing into a Riemann surface!

##### _notation:_ the set of all orbits

The set of all orbits of $G \circlearrowright X$ is denoted ${G \setminus X}$.

This is a quotient, not a set minus. The slash is reversed to emphasise that $G$ acts on the left, not the right (some algebraists really care about this).

There is a natural quotient map $\pi : X \to {G \setminus X}$ that sends each $p \in X$ to its orbit. This also gives a natural topology on ${G \setminus X}$ — the coarsest topology on ${G \setminus X}$ such that $\pi$ is continuous is that where $U \subseteq {G \setminus X}$ is open if and only if $\pi^\text{pre}(U)$ is open in $X$. This is of course the [[Topology --- math-147/notes/Quotient and identification spaces#_definition _ quotient topology, quotient space, quotient map|quotient topology]] with quotient map $\pi$. It follows that $\pi$ is continuous.

We can also show that $\pi$ is an open map (since our actions are continuous).

##### _lemma:_ the quotient map is open

For $G \circlearrowright X$, the quotient map $\pi : X \to {G \setminus X}$ is open.

###### _proof:_

 We want to show $\pi^\text{img}(U)$ is open for each open $U \subseteq X$. Since ${G \setminus X}$ is given the quotient topology, this is equivalent to showing $\pi^\text{pre}(\pi^\text{img}(U))$ is open. This pre-image is in fact just the union of all $G$-translates $g \cdot U = \{ g \cdot x \mid x \in U \}$.
 
We can show that $g \cdot U = \{ g \cdot x \mid x \in U \}$ is open. Since each function $x \mapsto g \cdot x$ is an automorphism, by [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_theorem _ open mapping theorem|the open mapping theorem]], they are open functions. Thus, each $g \cdot U$ is open.

Our goal is to construct on this quotient topology a quotient Riemann surface on ${G \setminus X}$ so that the projection $\pi$ is a holomorphism. We will try to build the complex structure by considering small enough neighbourhoods around each $p \in X$ that don't "cross the folds" of the quotient map. Here, the quotient map is a local homeomorphism allowing us to pull back charts onto ${G \setminus X}$ through the inverse homeomorphism.

We can't really do this completely when $p$ has non-trivial stabiliser, but even then, our situation is better since we only have to work around the stabiliser of $p$ rather than all of $G$.

##### _proposition:_ every stabiliser fixes a neighbourhood and more

Given $G \circlearrowright X$, and a fixed $p \in X$, there is an open neighbourhood $U$ of $p$ such that
1) $U$ is invariant under the action of $\operatorname{stab}_{G}p$
2) $U$ does not intersect $g \cdot U$ for any $g \not\in \operatorname{stab}_{p} G$.
3) the natural map $\alpha : \operatorname{stab}_{G}p \setminus U \to {G \setminus X}$ is a homeomorphism onto its (open) image.
4) $p$ is the only point of $U$ that is fixed by any element of $\operatorname{stab}_{G}p$.

###### _proof:_

We can write the elements not fixing $G$ as ${G \setminus \operatorname{stab}_{p}G} = \{ g_{1}, \dots, g_{n} \}$. Since $X$ is [[Topology --- math-147/notes/Separation properties#_definition _ Hausdorff spaces, $T_{2}$ spaces|Hausdorff]] we can find disjoint open neighbourhoods $V_{i} \ni p$ and $W_{i} \ni g_{i} \cdot p$ for each $g_{i}$. Then $g_{i}^{-1} \cdot W_{i}$ must be an open neighbourhood of $p$ (by [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_theorem _ open mapping theorem|open mapping]], or just by continuity of $g_{i}$). Let
$$
U_{0} = \bigcap_{i = 1}^n V_{i} \cap g^{-1}_{i} \cdot W_{i}
$$
and then choose
$$
U = \bigcap_{g \in \operatorname{stab}_{p} G} g \cdot U_{0} = \bigcap_{g \in \operatorname{stab}_{p}G} g \cdot \left( \bigcap_{i = 1}^n V_{i} \cap g^{-1}_{i} \cdot W_{i} \right)
$$

Each open set is an open neighbourhood of $p$, so this complicated finite intersection of open neighbourhoods is really an open neighbourhood of $p$ (and thus, non-empty).

First we show $\operatorname{stab}_{p} G$-invariance. For each $q \in U \subseteq U_{0}$ and $g, h \in \operatorname{stab}_{p} G$,  $q \in g^{-1} h \cdot U_{0}$ (since $q$ is in all $\operatorname{stab}_{p} G$-translates of $U_{0}$). Thus, $g \cdot q \in h \cdot U_{0}$. Since this is true for each $h$ and fixed $g$, we have $g \cdot q \in U$. That is, $U$ is invariant under $\operatorname{stab}_{p} G$.

Another way to prove this is to note that the function $x \mapsto g \cdot x$ is a bijection, and thus, commutes with intersections. It follows that $g \cdot U$ just permutes the terms of the intersection defining it, and thus, is still just $U$.

Similarly, for $g_{j} \in {G \setminus \operatorname{stab}_{p} G}$ we can commute group action and intersection to get
$$
g_{j} \cdot U = \bigcap_{g \in \operatorname{stab}_{p} G} g \cdot \bigcap_{i = 1}^n (g_{j} \cdot V_{i}) \cap (g_{j} g^{-1}_{i} \cdot W_{i}).
$$
Thus, the intersection of $U$ with $g_{j} \cdot U$ involves the intersection $V_{i} \cap W_{i}$, which we constructed to be empty.

A natural map $\alpha : {\operatorname{stab}_{p} G \setminus U \to G \setminus X}$ is defined by sending an orbit under $\operatorname{stab}_{p} G$ to an orbit under $G$. It is injective since $g_{j} \cdot U \cap U = \text{Ø}$ prevents any distinct $x, g_{j} \cdot x$ mapping to the same orbit, and any $x, g \cdot x$ with $g \in \operatorname{stab}_{p} G$ are already the same point in $\operatorname{stab}_{p} G \setminus U$. Finally it is continuous and open by [[Topology --- math-147/notes/Quotient and identification spaces#_proposition _ the universal property of quotients|the universal property of quotients]] — the composition $U \to {\operatorname{stab}_{p} G \setminus U} \to {G \setminus X}$ is just the quotient map $\pi_{\mid U}$ which is continuous and open. Thus, it is a homeomorphism onto its image.

The last result follows by the discreteness of points with non-trivial stabiliser. Since each open subset of the $V_{i}$ or $W_{i}$ containing $p$ or $g_{i} \cdot p$ still has the Hausdorff separation property, we can make $U$ small enough that there are no other points with non-trivial stabiliser by choosing appropriate $V_{i}, W_{i}$.

We can finally put a manifold, and then a complex structure on ${G \setminus X}$ by sending the charts on $U$ through $\alpha$ — we've reduced the task to putting charts on ${\operatorname{stab}_{p} G \setminus U}$ rather than ${G \setminus U}$ directly.

##### _construction:_ the quotient Riemann surface

Given $G \circlearrowright X$ and the quotient map $\pi : X \to G \setminus X$, the quotient $G \setminus X$  is a Riemann surface with $\pi : X \to G \setminus X$ holomorphic, and satisfying the universal property of quotients — $\rho : {G \setminus X} \to Y$ is a holomorphism of Riemann surfaces if and only if $\rho \circ \pi : X \to Y$ is a holomorphism.

###### _proof:_

Let $\overline{p} \in G \setminus X$ be the orbit of a point $p \in X$. 

First we deal with the case that the stabiliser is trivial — $\operatorname{stab}_{p} G = 1$. Then by the third result of the previous proposition, there is an open neighbourhood $U \ni p$ such that $\alpha = \pi_{\mid U} : U \to G \setminus X$ is a homeomorphism onto the open $W \subseteq G \setminus X$. Since this property also holds for any open subset of $U$ containing $p$, (and charts restrict to charts) we can choose $U$ small enough to be the domain of a chart $\phi : U \to \mathbb{C}$. Then choose $\psi = \phi \circ \pi_{\mid U}^{-1} : W \to \mathbb{C}$ to be a chart on a neighbourhood $W$ of $\overline{p}$. Notice that this is chosen so that $\psi \circ \pi_{U} \circ \phi ^{-1} = \operatorname{id}_{\mathbb{C}}$, and thus (assuming that all of these charts are compatible), $\pi$ is holomorphic at $p$.

Now suppose $\operatorname{stab}_{p} G$ has size $m \geq 2$. Again $\alpha : \operatorname{stab}_{p} G \setminus U \to W \subseteq G \setminus X$ is a homeomorphism where $W$ is an open neighbourhood of $\overline{p}$. However, we can't simply apply a chart on $U$, since the map $U \to \operatorname{stab}_{p} G \setminus U$ is $m$-to-$1$ away from $p$. However, we can still find the chart $\phi : W \to \mathbb{C}$ by finding the composition $U \to {\operatorname{stab}_{p} G \setminus U} \to W \to \mathbb{C}$.

This function would have to be $\operatorname{stab}_{p}G$-invariant, and thus $m$-to-one. We claim it is the product of all $g$-translates for $g \in \operatorname{stab}_{p} G$ — for a local coordinate $z$ centred at $p$, we choose
$$
h(z) = \prod_{g \in G_{p}} f_{g}(z)
$$
where $f_{g} : U \to \mathbb{C}$ are the functions corresponding to $x \mapsto g \cdot x$ on charts.

$h$ is holomorphic and $\operatorname{stab}_{p} G$-invariant. By the [[Topology --- math-147/notes/Quotient and identification spaces#_proposition _ the universal property of quotients|universal property of quotients]], given $\overline{h} : {\operatorname{stab}_{p} G \setminus U} \to \mathbb{C}$ with $h = \alpha \circ \overline{h}$, since $h$ is continuous and open, $\overline{h}$ is continuous and open. Finally $\overline{h}$ is injective since $h(z_{1}) = h(z_{2})$ if and only if $z_{1} = g \cdot z_{2}$. This follows since each $f_{g}$ is degree $1$, their product is degree $m$, and thus, all $m$ pre-images of some $w \in \mathbb{C} \setminus \{ 0 \}$ are taken up by the size $m$ orbit of $p$. At $0$, $f_{g}(0) \sim g \cdot p$ with multiplicity $m$. Thus, $\overline{h}$ is a homeomorphism, and we can write a chart $\phi = \alpha ^{-1} \circ \overline{h} : W \to \mathbb{C}$ which is the composition of homeomorphisms.

Now we show that all the charts are compatible. We first mention that we never have to deal with two charts of the second type intersecting since points with non-trivial stabiliser are discrete, and we can shrink the charts so that they don't intersect.

Our first case is the intersection of two charts of the first type. Let $(\psi_{1}, W_{1})$ and $(\psi_{2}, W_{2})$ be two charts on ${G \setminus X}$ of the first type, defined by $\psi_{1} = \phi_{1} \circ \pi_{\mid U_{1}}^{-1}$ and $\psi_{2} = \phi_{2} \circ \pi_{\mid U_{2}}^{-1}$ where $(\phi_{i}, U_{i})$ are charts on $X$. Then 
$$
\psi_{1} \circ \psi_{2} ^{-1} = \phi_{1} \circ \pi_{\mid U_{1}}^{-1} \circ \pi_{\mid U_{2}} \circ \phi_{2}^{-1} = (\phi_{1} \phi_{2}^{-1})_{\mid U_{1} \cap U_{2}}
$$
which is holomorphic because they are charts on $X$.

We also have to consider the case of a chart $(\psi_{1}, W_{1})$ constructed around a point with trivial stabiliser intersecting with a chart $(\psi_{2}, W_{2})$ constructed around a point with non-trivial stabiliser. Consider any $\overline{p} \in W_{1} \cap W_{2}$. We can then choose $p \in U_{1} \cap U_{2}$ where $\pi(p) = \overline{p}$, and $U_{i}$ is a connected component of $\pi^\text{pre}(W_{i})$. We can always choose $U_{1}$ and $U_{2}$ so that they intersect by translating by $g \in G$. If the local coordinates on $U_{1}$ and $U_{2}$ are $w$ and $z$, then the local coordinates on $W_{1}$ and $W_{2}$ are $w$ and $h(z)$. Since $w$ and $z$ are compatible and $h$ is holomorphic, $w$ and $h(z)$ are compatible.

Thus, ${G \setminus X}$ is a Riemann surface. Notably, since $G$ is finite and $X$ is Hausdorff, $G \setminus X$ is also Hausdorff (all the orbits are finite, and thus closed). Further, since $X$ is connected, and $\pi$ is surjective, ${G \setminus X}$ [[Topology --- math-147/notes/Connectedness and path-connectedness#_proposition _ continuous functions preserve connectedness|is connected]].

It suffices to prove the universal property in the case that $Y = \mathbb{C}$. That is, $f : {G \setminus X } \to \mathbb{C}$ is holomorphic, if and only if $f \circ \pi : X \to \mathbb{C}$ is holomorphic. Clearly if $f$ is holomorphic, [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ Riemann surfaces form a (concrete) category|the composition of holomorphic functions]] $f \circ \pi$ is holomorphic.

Now suppose $f \circ \pi$ is holomorphic. Let $\overline{p} \in {G \setminus X}$, with $\pi(p) = \overline{p}$ and a chart $(\phi, U)$ around $p$. We have $f \circ \pi \circ \phi ^{-1}$ holomorphic. If $\overline{p}$ has trivial stabiliser, then we are done since there is a chart $(\psi, W)$ around it given by $\psi = \phi \circ \pi_{U}^{-1}$, so we have just shown $f \circ \psi ^{-1}$ holomorphic. Suppose $p$ has non-trivial stabiliser. The points near $p$ must have trivial stabiliser. Thus, $\overline{p}$ is contained in one of the charts on which we proved $f$ is holomorphic.

A nice result is that with a complex structure on ${G \setminus X}$, we can apply [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological properties of holomorphisms#_proposition _ local normal form|local normal form]] to make the isomorphism between $\operatorname{stab}_{p} G$ and a finite subgroup of $\mathbb{C}^*$ concrete.

##### _corollary:_ linearisation of the action

Given $G \circlearrowright X$, let $p \in X$ be a fixed point with $\lvert \operatorname{stab}_{p} G \rvert = m$ and $g \in G$ generating the stabiliser. Then there is a local coordinate centred at $p$ such that $f_{g}(z) = \lambda z$ where $\lambda$ is a primitive $m$th root of unity.

###### _proof:_

Choose local coordinate $w$ on $G \setminus X$, centred at $\overline{p}$. Then by local normal form, there is a local coordinate $z$ on $X$ with $w = z^m$ under $\pi : X \to {G \setminus X}$. Thus, the $m$ pre-images of points $w$ near $\overline{p}$ are $\lambda^j z$. Thus, the orbit of $p$ under the action consists of $z, \lambda z \dots \lambda^{m - 1} z$. Since $f_{g}(z)$ is one of these points and $g$ generates all of them, $f_{g}(z) = \lambda^k z$ where $\gcd(k, m) = 0$.

### Ramifications from Hurwitz' formula

Now we have a nice projection holomorphism $\pi : X \to G \setminus X$. It also shouldn't be surprising that $\pi$ has [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ degree of a map|degree]] $\lvert G \rvert$ but we need to prove it. From this we can understand the topology of ${G \setminus X}$ using [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological properties of holomorphisms#_theorem _ Hurwitz' formula|Hurwitz' formula]]. This in turn offers insight into the structure of $G$ and thus, $\operatorname{Aut} X$.

##### _lemma:_ the degree of a quotient holomorphism

Given $G \circlearrowright X$ and $X$ compact, the quotient map $\pi : X \to {G \setminus X}$ has degree $\lvert G \rvert$. Further, for every branch point $q \in {G \setminus X}$, there is an integer $r \geq 2$ such that $\pi^\text{pre}(\{ q \})$ consists of exactly $\lvert G \rvert / r$ points of $X$, at each of which $\pi$ has multiplicity $r$.

###### _proof:_

At all the infinitely many points $p \in X$ with trivial stabiliser, $\pi$ has multiplicity $\lvert G \rvert$. Thus, $\pi$ has degree $\lvert G \rvert$.

Suppose $q$ is a branch point with pre-images $p_{1}, \dots, p_{n}$. All the $p_{j}$ are in the same orbit, so have conjugate, and thus, equal size stabilisers. Let $r = \lvert \operatorname{stab}_{p_{j} G} \rvert$. Then $\pi$ has multiplicity $r$ at each of the points. Thus, there are $\deg \pi / r = \lvert G \rvert / r$ of the points.

Since topological invariants have sanity checks (for example, genus must be a non-negative number) we can also use [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological properties of holomorphisms#_theorem _ Hurwitz' formula|Hurwitz' formula]] to impose restrictions on what $G$ can be. This restricts $\operatorname{Aut} X$!

##### _theorem:_ Hurwitz' theorem

If $G$ is a finite subgroup of $\operatorname{Aut} X$, and $X$ has [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Topological invariants of a surface#_definition _ genus|genus]] $g_{X} \ge 2$, then
$$
\lvert G \rvert \le 84 (g_{X} - 1).
$$

###### _proof:_

Clearly $G \circlearrowright X$. Suppose $\pi : X \to {G \setminus X}$ has $n$ branch points $q_{1}, \dots, q_{n}$, with $\pi$ having multiplicity $r_{i}$ at the pre-images of $q_{i}$. By applying Hurwitz' formula to $\pi$, we get
$$
\begin{align}
2 g_{X} - 2  & = \lvert G \rvert (2 g_{G \setminus X} - 2) + \sum_{i = 1}^n \frac{\lvert G \rvert }{r_{i}} (r_{i} -  1) \\
 & = \lvert G \rvert  \left( 2g_{G \setminus X} - 2 + \sum_{i = 1}^n (1 - 1 / r_{i}) \right)
\end{align}
$$

Write $R = \sum_{i = 1}^n 1 - 1 / r_{i}$. Then combinatorics forces $R = 0$, $1 / 2 \le R \leq 2$, or $R \geq 2 \frac{1}{42}$. Substituting into Hurwitz' formula we get
$$
\lvert G \rvert = \frac{2g_{X} - 2}{2 g_{G \setminus X} - 2 + R} = \frac{g_{X} - 1}{g_{G \setminus X} - 1 + R / 2}.
$$
Suppose $g_{G \setminus X} \geq 1$. If $R = 0$, we must have $g_{G \setminus X} \ge 2$ for $\lvert G \rvert$ to be positive. It follows that
$$
\lvert G \rvert \le \frac{g_{X} - 1}{1 + R / 2} \le g_{X} - 1.
$$
Else, if $R \neq 0$, we must have at least $R \ge 1 / 2$ so we get
$$
\lvert G \rvert \le \frac{g_{X} - 1}{R / 2} \le \frac{g_{X} - 1}{1 / 4} = 4(g_{X} - 1).
$$
Finally, if $g_{G \setminus X} = 0$, then
$$
\lvert G \rvert \le \frac{g_{X} - 1}{-1 + R / 2}.
$$
Since $\lvert G \rvert > 0$ and $g_{X} \ge 2 > 0$, we must have $1 - R / 2 \geq 0$, and thus, $R \geq 2 \frac{1}{42}$. Ultimately, this gives
$$
\lvert G \rvert \le \frac{g_{X} - 1}{-1 + 1 \frac{1}{84}} = 84(g_{X} - 1).
$$


If equality is achieved (as is for the Klein quartic $x^{3} y + y^{3} z + z^{3} x = 0$), we say a group is a Hurwitz group, and the corresponding Riemann surface is a Hurwitz curve

### Infinite groups

Clearly the same constructions work for sufficiently discrete infinite groups — we've seen already that $\mathbb{Z} \times \mathbb{Z} \setminus \mathbb{C}$ is a [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Riemann surfaces#_example _ Algebraic Geometry --- math-176/notes/Elliptic curves _proposition, definition _ reducing cubics, elliptic curves elliptic curves|torus/elliptic curve]]. The exact condition we need is for the quotient to be Hausdorff and this happens when $G$ acts properly discontinuously.

##### _definition:_ properly discontinuous action

A (possibly infinite, but still holomorphic, effective) action $G \circlearrowright X$ is said to act properly discontinuously if for each pair of points $p, q \in X$, there exist open neighbourhoods $U_{p}, U_{q}$ respectively, such that only finitely many $g \in G$ have $g \cdot U_{p}$ and $U_{q}$ intersecting.