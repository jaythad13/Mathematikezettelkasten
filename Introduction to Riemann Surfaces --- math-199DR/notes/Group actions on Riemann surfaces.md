---
tags:
- math-199DR/9
- cx-geo
---

Given a Riemann surface $X$, what does $\operatorname{Aut} X$ look like? What are its finite subgroups? By understanding their action on the Riemann surface, we can get better answers to these questions. These in turn, allow us to [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_example _ meromorphic functions on non-isomorphic elliptic curves|distinguish Riemann surfaces]].

Further, by squishing these automorphism groups to nothing by quotienting out by these actions we can get new Riemann surfaces. The reverse problem — that of which Riemann surfaces give rise to to all (compact, connected) Riemann surfaces by quotients is exactly [[Introduction to Riemann Surfaces --- math-199DR/notes/Riemann surfaces#_theorem _ the uniformisation theorem|the uniformisation theorem]]!

### Reviewing group actions

Recall the definition of a group action,

![[Abstract Algebra I --- math-171/notes/Group actions#_definition _ (left) group action|Group actions]]

its stabiliser

![[Abstract Algebra I --- math-171/notes/Group actions#_definition _ stabiliser|Group actions]]

its kernel

![[Abstract Algebra I --- math-171/notes/Group actions#_definition _ kernel|Group actions]]

and its orbits.

![[Abstract Algebra I --- math-171/notes/Group actions#_definition _ orbit|Group actions]]

### Holomorphic, effective actions on Riemann surfaces

Really we don't want to consider just any arbitrary group action on a Riemann surface — we want to consider group actions that respect the Riemann surface structure. Also, we don't want to have to deal with any redundancy in the group action — if a group action $G \circlearrowright X$ has a non-trivial kernel $K$, then the group action that we really want to consider is $(G / K) \circlearrowright X$ (which has trivial kernel).

##### _definition:_ effective, holomorphic group action

A holomorphic group action is a group action such that each function $x \mapsto g \cdot x$ is a [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphism]] $X \to X$.

A group action is effective if it has trivial kernel.

Finally, we don't really want to deal with infinite group actions, so we limit ourselves to the actions of finite groups — from here on, every $G \circlearrowright X$ is the holomorphic, effective action of a finite group on a Riemann surface. These have nice properties! 

##### _proposition:_ finite group actions have cyclic stabiliser

Given $G \circlearrowright X$, the stabiliser $\operatorname{stab}_{G}p$ at $p \in X$ is a finite [[Abstract Algebra I --- math-171/notes/Cyclic groups and subgroups|cyclic group]].

###### _proof:_

Consider, for each $g \in \operatorname{stab}_{G} p$, the holomorphism $p \mapsto g \cdot p$ on $X$, and further, given a choice of charts centred at $p \in X$ (both can be centred at $p$ since $g \cdot p = p$), the holomorphism pushed forward to a holomorphic function on $\mathbb{C}$. Call that function $f_{g}$. Notice that $f_{g}(0) = 0$, and since $g$ induces a bijection on $X$, $f_{g}$ must be injective.

Write the [[Complex Analysis --- math-135/notes/Cauchy integral formula#_corollary _ the derivative form (holomorphic functions are smooth and analytic)|power series]] for $f_{g}$ —
$$
f_{g}(z) = \sum_{n = 1}^\infty a_{n} z^n
$$
and construct a [[Abstract Algebra I --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|homomorphism]] $\lambda : \operatorname{stab}_{G}p \to \mathbb{C}^*$ by picking out linear terms in the power series. That is
$$
\lambda(g) = f_{g}'(0) = a_{1}(f_{g}).
$$
These $\lambda(g)$ must be non-zero — by the $n$[[Complex Analysis --- math-135/notes/The argument principle and winding number#_lemma _ the "$n$-to-one" lemma|-to-one lemma]] a function with order $2$ zero at $0$ cannot be injective. Further, it is indeed a homomorphism — for $g, h \in G$ we have
$$
f_{gh}(z) = \sum_{n = 1}^\infty a_{g, n} \left( \sum_{n = 1}^\infty a_{h, n} z^n \right)  = a_{g, n} a_{h, n} z + O(z^{2}).
$$

If we can just show that $\lambda$ is injective, we will have that $\operatorname{stab}_{G}p$ is a finite subgroup of $\mathbb{C}^*$, and thus, cyclic. Suppose $\lambda(g) = 1$. Then $f_{g}(z) = z + O(z^{2})$. Suppose, for all $n < m \ge 2$ we have $a_{n} = 0$. Then $f_{g}(z) = z + a_{m} z^m + O(z^{m + 1})$. Then $f_{g^k}(z) = z + k a_{m} z^{m} + O(z^{m + 1})$ (by some mildly painful induction and algebra). But since $\operatorname{stab}_{G} p$ is finite, $g^k = 1$ for some $k > 0$, and for that $k$, we must have $f_{g^k}(z) = z$. Since $k \neq 0$, we must have $a_{m} = 0$. That is, all $a_{m} = 0$ for $m \ge 2$ and $f_{g}(z) = z$. Since the action of $G$ is effective, $g$ must be the identity.


##### _lemma:_ the set of points with non-trivial stabiliser is discrete

Given $G \circlearrowright X$, the points $p \in X$ with non-trivial stabiliser form a [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete]] [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subset]] of $X$.

###### _proof sketch:_

Suppose there is a sequence of $x_{n} \in X$ converging to $x$ with $g_{n} \in G$ such that $g_{n} \cdot x_{n} = x_{n}$. Since $G$ is finite, there is some $g$ that is chosen infinitely many times. Choose the corresponding subsequence. $g \cdot x_{n_{k}} = x_{n_{k}}$. By compactness, $x_{n_{k}}$ also converges to the same thing, so $g$ [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_theorem _ identity theorem|must act by identity]]. Since $G$ acts effectively, $g$ is the identity. Thus, the stabilisers are eventually trivial, just containing $g = 1_{G}$.

### Quotient Riemann surfaces

Because we're dealing with finite group actions, collapsing all of the orbits into points just looks like folding our Riemann surface rather than anything more perverse. We should be able to make this thing into a Riemann surface!

##### _notation:_ the set of all orbits

The set of all orbits of $G \circlearrowright X$ is denoted ${G \setminus X}$.

This is a quotient, not a set minus. The slash is reversed to emphasise that $G$ acts on the left, not the right (representation theorists like Prof. Goins really care about this).

There is a natural quotient map $\pi : X \to {G \setminus X}$ that sends each $p \in X$ to its orbit. This also gives a natural [[Topology --- math-147/notes/Quotient and identification spaces|quotient topology]] on ${G \setminus X}$ — the coarsest topology on ${G \setminus X}$ such that $\pi$ is continuous is that where $U \subseteq {G \setminus X}$ is open if and only if $\pi^\text{pre}(U)$ is open in $X$.

We can also show that $\pi$ is an open map (since our actions are continuous).

##### _lemma:_ the quotient map is open

For $G \circlearrowright X$, the quotient map $\pi : X \to {G \setminus X}$ is open — $\pi^\text{img}(U)$ is open for each open $U \subseteq X$.

###### _proof:_

We want to show that $g \cdot U = \{ g \cdot x \mid x \in U \}$ is open. Notice that $g^{-1} \cdot (g \cdot U) = U$ is open, and since $g^{-1}$ acts continuously, $U$'s pre-image under $g^{-1}$, that is, $g \cdot U$ must be open. Thus, $\pi^\text{img}(U)$ which is the union of all $g \cdot U$ is open.

Our goal is to use this to construct a quotient Riemann surface on ${G \setminus X}$ so that the projection $\pi$ is a holomorphism. We will try to build the complex structure by considering small enough neighbourhoods around each $p \in X$ that don't "cross the folds" of the quotient map. Here, the quotient map is a local homeomorphism allowing us to pull back charts onto ${G \setminus X}$ through the inverse homeomorphism.

We can't really do this completely when $p$ has non-trivial stabiliser, but even then, our situation is better since we only have to work around the stabiliser of $p$ rather than all of $G$.

##### _proposition:_ every stabiliser fixes a neighbourhood and more

Given $G \circlearrowright X$, and a fixed $p \in X$, there is an open neighbourhood $U$ of $p$ such that
1) $U$ is invariant under the action of $\operatorname{stab}_{G}p$
2) $U$ does not intersect $g \cdot U$ for any $g \not\in \operatorname{stab}_{p} G$.
3) The quotient map $\alpha : \operatorname{stab}_{G}p \setminus U \to {G \setminus X}$ is a homeomorphism onto its (open) image.
4) $p$ is the only point of $U$ that is fixed by any element of $\operatorname{stab}_{G}p$.

We can finally put a complex structure on ${G \setminus X}$ by sending the charts on $U$ through $\alpha$.

##### _construction:_ the quotient Riemann surface


### Ramifications from Hurwitz' formula

Now we have a nice projection holomorphism $\pi : X \to G \setminus X$. It also shouldn't be surprising that $\pi$ has [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ degree of a map|degree]] $\lvert G \rvert$ but we need to prove it. From this we can understand the topology of ${G \setminus X}$ using [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_theorem _ Hurwitz' formula|Hurwitz' formula]].

##### _lemma:_ quotient Riemann surface projection has degree $\lvert G \rvert$

Given $G \circlearrowright X$ and $X$ compact, the quotient map $\pi : X \to {G \setminus X}$ has degree $\lvert G \rvert$.

Since topological invariants have sanity checks (for example, genus must be a non-negative number) we can also use the degree of $\pi$ and Hurwitz formula to impose restrictions on what $G$ can be. This restricts $\operatorname{Aut} X$!

##### _theorem:_ Hurwitz theorem

If $G$ is a finite subgroup of $\operatorname{Aut} X$, and $X$ has [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological invariants of a surface#_definition _ genus|genus]] $g \ge 2$, then
$$
\lvert G \rvert \le 84 (g - 1).
$$

If equality is achieved (as is for the Klein quartic $x^{3} y + y^{3} z + z^{3} x = 0$), we say a group is a Hurwitz group.

### Infinite groups

Clearly the same constructions work for sufficiently discrete groups — we've seen already that $\mathbb{Z} \times \mathbb{Z} \setminus \mathbb{C}$ is a [[Introduction to Riemann Surfaces --- math-199DR/notes/Riemann surfaces#_example _ Algebraic Geometry --- math-176/notes/Elliptic curves _proposition, definition _ reducing cubics, elliptic curves elliptic curves|torus/elliptic curve]]. The exact condition we need is for the quotient to be Hausdorff and this happens when $G$ acts properly discontinuously.

##### _definition:_ properly discontinuous action

A (possibly infinite, but still holomorphic, effective) action $G \circlearrowright X$ is said to act properly discontinuously if for each pair of points $p, q \in X$, there exist open neighbourhoods $U_{p}, U_{q}$ respectively, such that only finitely many $g \in G$ have $g \cdot U_{p}$ and $U_{q}$ intersecting.