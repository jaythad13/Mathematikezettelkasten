---
tags:
- math-199DR/9
- cx-geo
---

Given a Riemann surface $X$, what does $\operatorname{Aut} X$ look like? What are its finite subgroups? For genus $0$, we know that these are [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_examples _ interesting isomorphisms|essentially the Möbius transformations]], and with Hurwitz formula, we've seen 

### Reviewing group actions

Recall the definition of a group action
![[Abstract Algebra I --- math-171/notes/Group actions#_definition _ (left) group action|Group actions]]
its stabiliser
![[Abstract Algebra I --- math-171/notes/Group actions#_definition _ stabiliser|Group actions]]
its kernel
![[Abstract Algebra I --- math-171/notes/Group actions#_definition _ kernel|Group actions]]
and its orbits
![[Abstract Algebra I --- math-171/notes/Group actions#_definition _ orbit|Group actions]]

### (Holomorphic, effective) actions on Riemann surfaces

We want to look at groups that act holomorphically and effectively

##### _definition:_ effective, holomorphic group action

A holomorphic group action is a group action such that each function $x \mapsto g \cdot x$ is a [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphism]] $X \to X$.

A group action is effective if it has trivial kernel.

##### _proposition:_ finite group actions have cyclic stabiliser

###### _proof:_

Identify $g \in G$ with the holomorphism $x \mapsto g \cdot x$ on $X$, and further, given a choice of chart $(\phi, U)$ centred at $p \in X$ (with $\phi(p) = 0$), with the holomorphism pushed forward to a holomorphic function $\phi^\text{img}(U) \to \mathbb{C}$.

Construct a homomorphism $\operatorname{stab}_{p}G \to \mathbb{C}^*$ by picking out linear terms in the power series. These must be non-zero since each $g$ of a group action induces a bijection and the [[Complex Analysis --- math-135/notes/The argument principle and winding number#_lemma _ the "$n$-to-one" lemma|the n to one lemma]] says this won't happen if we have zero derivative.

Since $G$

From here on, all groups acting on $X$ are finite.

##### _lemma:_ the set of points with non-trivial stabiliser is discrete

###### _proof sketch:_

Suppose there is a sequence of $x_{n} \in X$ converging to $x$ with $g_{n} \in G$ such that $g_{n} \cdot x_{n} = x_{n}$. Since $G$ is finite, there is some $g$ that is chosen infinitely many times. Choose the corresponding subsequence. $g \cdot x_{n_{k}} = x_{n_{k}}$. By compactness, $x_{n_{k}}$ also converges to the same thing, so $g$ [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_theorem _ identity theorem|must act by identity]]. Since $G$ acts effectively, $g$ is the identity. Thus, the stabilisers are eventually trivial, just containing $g = 1_{G}$.

##### _lemma:_ every stabiliser fixes a neighbourhood and more

For every holomorphic, effective action $G \circlearrowright X$, every $p \in X$ has a neighbourhood


This allows us to put a nice [[Introduction to Riemann Surfaces --- math-199DR/notes/Riemann surfaces#_definition _ (compact, connected) Riemann surface, (holomorphic) atlas, chart|complex structure]] on the quotient $G \setminus X$.

### $X$ and its quotient

Now we have a nice projection $\pi : X \to G \setminus X$. It shouldn't be surprising that this is holomorphic since we constructed $G \setminus X$ exactly so that it is. It also shouldn't be surprising that $\pi$ has [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ degree of a map|degree]] $\lvert G \rvert$ but we need to prove it.

This means we the genus of ${G \setminus X}$ from [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_theorem _ Hurwitz' formula|Hurwitz' formula]].

##### _theorem:_ 

If $G$ is a finite subgroup of $\operatorname{Aut} X$, and $X$ has [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological invariants of a surface#_definition _ genus|genus]] $g \ge 2$, then
$$
\lvert G \rvert \le 84 (g - 1).
$$

If equality is achieved (as is for the Klein quartic $x^{3} y + y^{3} z + z^{3} x = 0$), we say a group is a Hurwitz group.