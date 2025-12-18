---
tags:
- math-199DR/6
- cx-geo
- diff-geo
---

Let $X, Y$ be Riemann surfaces with (maximal) holomorphic atlases $(\phi_{\alpha}, U_{\alpha})$ and $(\psi_{\beta}, V_{\beta})$ indexed by $\alpha \in \mathcal{I}$ and $\beta \in \mathcal{ J}$ respectively. Many of the results obviously only hold when $X$ and $Y$ are connected.

Now that we have the objects of our category — [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Riemann surfaces#_definition _ (compact, connected) Riemann surface, (holomorphic) atlas, chart|Riemann surfaces]], we should try to find the right morphisms for the category. It's useful to consider what kind of properties we want the morphisms to have.

##### _desiderata:_ morphisms of Riemann surfaces

- We want the class of all Riemann surfaces to be a [[Basic category theory --- basic-cat/notes/Categories#_definition _ category|category]] — that is, each Riemann surface should have an identity morphism and the morphisms should compose associatively.
- In fact, we don't just want it to be a category — morphisms of Riemann surfaces should be functions — morphisms of the underlying sets. Categorically, we want our category to be a "concrete category".
- In fact, morphisms of Riemann surfaces, should also be [[Analysis --- math-131/notes/Continuity#_proposition _ $ varepsilon$-$ delta$ continuity is equivalent to topological continuity|continuous maps]] — morphisms of the underlying [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological spaces]]. Categorically, we want a "forgetful functor" to $\mathsf{\mathbb{R}^{2}Man^0}$ or $\mathsf{Top}$ (depending on whether you require a left adjoint).
- The notion of a [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ holomorphic functions|holomorphic function on a Riemann surface]] $X$ should agree with notion of a morphism of Riemann surfaces given by $X \to \mathbb{C}$.
- The notion of a [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ meromorphic|meromorphic function on a Riemann surface]] $X$ should agree with the notion of a morphism of Riemann surfaces $X \to \mathbb{C}_{\infty}$. We will see that this is really useful.
- Generally, we want morphisms $X \to Y$ to preserve the complex structures on $X$ and $Y$.
- In particular, theorems from complex analysis should have analogues for morphisms of Riemann surfaces
- Perhaps this should mean something about the structure sheaves $\mathcal{O}_{X}$ and $\mathcal{O}_{Y}$?

##### _definition:_ holomorphism

A function $\pi: X \to Y$ is holomorphic at $p \in X$ if there exist charts $(\phi, U)$ with $p \in U$ and $(\psi, V)$ with $\pi(p) \in V$ such that the composition $\psi \circ \pi \circ \phi ^{-1}$ is [[Complex analysis --- math-135/notes/Holomorphic functions#_definition _ holomorphic, $ mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$|holomorphic]] at $\phi(p)$.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		X \ar[r, "\pi"] & Y \\
 U = \pi^{\mathrm{pre}}(V) \ar[u, hook] \ar[r, "\pi"] & V \ar[u, hook] \ar[d, "\psi"] \\
 \phi^\mathrm{img}(U) \ar[u, "\phi^{-1}"] \ar[r, "\psi \circ \pi \circ \phi ^{-1}"] & \psi^\mathrm{img}(V)
	\end{tikzcd}
\end{document}
```

If $\pi$ is holomorphic at every $p \in W$ for some open $W \subseteq X$.

If $\pi$ is holomorphic on all of $X$, we say it is a holomorphism.

##### _examples:_ dumb examples of holomorphisms

1) Every [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ holomorphic functions|holomorphic function]] on $X$ is a holomorphism $X \to \mathbb{C}$ (this is exercise II.3 A).
2) Every constant function $X \to Y$ is a holomorphism.
3) The identity function on $X$ is a holomorphism. In fact, since it is its own inverse, it's also our first example of an isomorphism.

From this follows the natural definition of isomorphism and automorphism.

##### _definition:_ biholomorphism/isomorphism, automorphism

A biholomorphism/isomorphism of Riemann surfaces $X$ and $Y$ is a holomorphism $\pi : X \to Y$ that is a bijection with a holomorphic inverse $\pi ^{-1}$.

An isomorphism $X \to X$ is an automorphism of $X$.

##### _examples:_ interesting isomorphisms

1) The Riemann sphere $\mathbb{C}_{\infty}$ has an automorphism by $1 / z$. In general $\operatorname{Aut}(\mathbb{C}_{\infty})$ is just $\operatorname{PSL}_{2}(\mathbb{C})$ (maps $z \mapsto \frac{az + b}{cz + d}$) since the numerator and denominator of an injective meromorphic function on $\mathbb{C}_{\infty}$ should have degree $1$. (This is exercises II.3 G, H) In the future we might see Hurwitz' theorem which says that $\operatorname{Aut} X$ is a finite [[Abstract algebra --- math-171/notes/Groups, and why you should care#_definition _ group, identity, inverse|group]] when it has sufficiently big genus.
2) The Riemann sphere $\mathbb{C}_{\infty}$ is isomorphic to the complex projective line $\mathbb{C} \mathbb{P}^1$ by $z \mapsto (z_{1} : z_{0})$ such that $z = z_{1} / z_{0}$ and $\infty \mapsto (1 : 0)$. (This is exercise II.3.C)

##### _proposition:_ Riemann surfaces form a (concrete) category

$\mathsf{\mathbb{C}^1Man}$, the class of all Riemann surfaces and the holomorphisms between them, forms a concrete category. That is, 
3) the identity set map $\operatorname{id}_{X}$ on each $X$ is a holomorphism
4) the composition of holomorphisms is a holomorphism
5) the composition is associative

###### _proof sketch:_

This is exercise II.3 B

The first is easy to see.

The second follows from the chain rule for holomorphic functions $\mathbb{C} \to \mathbb{C}$ (push everything onto the complex plane and work it out there). We can just add an extra column to the commutative diagram

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		X \ar[r, "\pi"] & Y \ar[r, "\rho"] & Z \\
 U = \pi^{\mathrm{pre}}(V) \ar[u, hook] \ar[r, "\pi"] & V = \pi^\mathrm{pre}(W) \ar[u, hook] \ar[d, "\psi"] \ar[r, "\rho"] & W \ar[u, hook] \ar[d, "\mu"] \\
 \phi^\mathrm{img}(U) \ar[u, "\phi^{-1}"] \ar[r, "\psi \circ \pi \circ \phi ^{-1}"] \ar[rr, bend right , "\mu \circ \rho \circ \pi \circ \phi ^{-1}"] & \psi^\mathrm{img}(V) \ar[u, "\psi ^{-1}"] \ar[r, "\mu \circ \rho \circ \psi ^{-1}"] & \mu^\mathrm{img}(W)
	\end{tikzcd}
\end{document}
```

##### _proposition:_ holomorphisms are continuous

If $\pi : X \to Y$ is a holomorphism, it is a [[Analysis --- math-131/notes/Continuity#_proposition _ $ varepsilon$-$ delta$ continuity is equivalent to topological continuity|continuous map]] of the underlying topological spaces.

###### _proof sketch:_

Do it locally. For charts $(U, \phi)$ and $(V, \psi)$, the complex function $\psi \circ \pi \circ \phi ^{-1}$ is holomorphic and thus, continuous. Compose with the homeomorphisms $\psi ^{-1}$ and $\phi$ on the left and right to get $\pi$ continuous on the corresponding open sets of the charts.

### Theorems from complex analysis

We will just sketch the proofs some of the nice theorems from complex analysis that carry over.

##### _theorem:_ open mapping theorem

If $\pi : X \to Y$ is a non-constant holomorphism, $\pi$ is an open mapping.

###### _proof:_

For charts $(U, \phi)$ and $(V, \psi)$, the complex function $\psi \circ \pi \circ \phi ^{-1}$ is holomorphic and thus, [[Complex analysis --- math-135/notes/The argument principle and winding number#_theorem _ open mapping theorem|open mapping]]. Compose with the homeomorphisms $\psi ^{-1}$ and $\phi$ on the left and right to get $\pi$ an open mapping on $U$.

##### _theorem:_ inverse holomorphism theorem

If $\pi : X \to Y$ is an injective holomorphism, $\pi$ has a holomorphic inverse — it is an isomorphism between $X$ and $\pi ^\mathrm{img}(X)$.

###### _proof sketch:_

Choose charts $(U, \phi)$ and $(V, \psi)$ on $X$ and $Y$. Pushing forward to the complex plane, $f = \psi \circ \pi \circ \phi ^{-1}$ is a bijective holomorphic function between two sets on the complex plane. By [[Complex analysis --- math-135/notes/The argument principle and winding number#_lemma _ the "$n$-to-one" lemma|the two-to-one lemma]] $f$ cannot have $f'(z) = 0$ at any $z$, and so has a holomorphic inverse by [[Calculus --- spivak/notes/Inverse and implicit functions#_theorem _ the inverse function theorem|the inverse function theorem]].

Glue the restricted inverses $\pi ^{-1}_{|V} = \phi ^{-1} \circ f^{-1} \circ \psi$ together on $\pi^\text{img}(X)$ to get $\pi ^{-1}$.

##### _theorem:_ identity theorem

If $\pi, \rho$ are two holomorphisms $X \to Y$, and $\pi = \rho$ on a subset $S \subseteq X$ with a [[Topology --- math-147/notes/Limit points and closed sets|limit point]] $s$ in $X$, then $\pi = \rho$.

###### _proof sketch:_

Pick a chart $(U, \phi)$ containing the limit point $s$ and $(V, \psi)$ containing $\pi(p)$. $\pi$ and $\rho$ are holomorphic at $s$ and so are the pushed forward maps on $\mathbb{C}$. By the [[Complex analysis --- math-135/notes/Cauchy integral formula#_corollary _ unique analytic continuation|identity theorem]], these are equal and so $\pi = \rho$ on $U$.

By the [[Complex analysis --- math-135/notes/Analysis and (metric) topology review#_proposition _ path-connectedness and connectedness are equivalent on open sets|equivalence]] of [[Analysis --- math-131/notes/Connectedness#_definition _ connectedness|connectedness]] and [[Complex analysis --- math-135/notes/Analysis and (metric) topology review#_proposition _ path-connectedness and connectedness are equivalent on open sets|path connectedness]] on open sets in $\mathbb{C}$, they are equivalent on Riemann surfaces, and thus, we can use the same trick we did in the proof of the identity theorem to move this disc to the whole connected component of $s$.

##### _proposition:_ maps from compact Riemann surfaces are surjective

If $X$ is [[Analysis --- math-131/notes/Compactness#_definition _ compact|compact]] and $\pi : X \to Y$ is a non-constant holomorphism, then $\pi$ is surjective and $Y$ is compact.

###### _proof:_

$\pi^\text{img}(X)$ is open by the open mapping theorem, but closed since $\pi^\text{img}(X)$ [[Analysis --- math-131/notes/Continuity#_theorem _ continuity preserves Mathematical Analysis I --- math-131/notes/Compactness _definition _ compact compactness|is compact]] (and since $Y$ is Hausdorff). Since $Y$ is connected, the image is the whole surface.

##### _proposition:_ discreteness of pre-images

If $\pi : X \to Y$ is a non-constant holomorphism, then for each $p \in Y$, $\pi^\text{pre}(\{ p \})$ is a [[Topology --- math-147/notes/Topologies#_example _ the discrete and indiscrete topologies|discrete subset]] of $X$. If $X$ and $Y$ are compact, then the pre-image is finite.

###### _proof:_

Choose charts $(U, \phi)$ and $(V, \psi)$ containing a point $q \in \pi^\text{pre}(\{ p \})$ and $p$ respectively. Since $f = \psi \circ \pi \circ \phi ^{-1}$ has $f(\phi(q)) = \psi(p)$. Since [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_proposition _ characterising holomorphic functions near zeroes|zeroes are discrete]] (for non-constant maps) $f - \psi(p)$ doesn't have another zero in the vicinity of $\phi(q)$. Do this for each $q$ to get that $\pi^\text{pre}(\{ p \})$ is discrete.

The second statement follows since [[Analysis --- math-131/notes/Compactness#_theorem _ Bolzano-Weierstrass theorem|discrete subsets of compact spaces are finite]].

### Meromorphic functions as maps to the Riemann sphere

Really the right way to understand meromorphic functions on $X$ is to see them as holomorphisms to the Riemann sphere in the obvious way. The intuition here is that [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_corollary _ $f$ is unbounded near poles|meromorphic functions blow up near poles]]. For an example of how this is useful, see exercise II.3 I

##### _proposition:_ meromorphic functions are maps to the Riemann sphere

Given a [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ meromorphic|meromorphic function]] $f : X \to \mathbb{C}$, and the stereographic projection $\phi_{0} : \mathbb{C}_{\infty} \setminus \{ \infty \} \to \mathbb{C}$, the derived map
$$
\pi(p) = \begin{cases}
\phi_{0}^{-1}(f(p)) \in \mathbb{C} & p \text{ is not a pole} \\
\infty & p \text{ is a pole}.
\end{cases}
$$
is a holomorphism $\pi : X \to \mathbb{C}_{\infty}$.

###### _proof sketch:_

This is exercise II.3 J

$\pi$ is clearly a holomorphism everywhere that $p$ is not a pole. It still works when $p$ is a pole because, by definition, $1 / f$ is holomorphic at $p$ and use the opposite chart $\phi_{\infty}$.

That is, there is a bijection between meromorphic function on $X$ and holomorphisms $X \to \mathbb{C}_{\infty}$ that are not identically $\infty$.

Since $\mathbb{C}_{\infty} \cong \mathbb{C} \mathbb{P}^1$, there is a corresponding bijection to maps on $\mathbb{C}\mathbb{P}^1$ — write $f : X \to \mathbb{C}$ as the ratio $g / h$ locally, and consider $p \mapsto (g(p) : h(p))$ in projective.

##### _proposition:_ meromorphic functions on a torus $\mathbb{C} / \Lambda$ have zero total order

Any non-constant meromorphic function $f : \mathbb{C} / \Lambda \to \mathbb{C}$ has
$$
\sum_{p \in \mathbb{C} / \Lambda} \operatorname{ord}_{p} f = 0.
$$

###### _proof:_

Suppose for contradiction that $f$ doesn't satisfy this. Without loss of generality (by considering $1 / f$) $f$ has more poles $p_{1}, \dots, p_{m}$ than zeroes $z_{1}, \dots, z_{n}$. The shifted $\Theta$ function construction [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_example _ meromorphic functions on the torus|earlier]] allows us to add zeroes $z_{n + 1}, \dots, z_{m}$ to the list (as long as they satisfy some quotient sum condition in $\mathbb{C} / \Lambda$) and create a meromorphic function $g$ with poles $p_{1}, \dots, p_{m}$ and zeroes $z_{1}, \dots, z_{m}$.

Consider $g / f$. It has no poles and only zeroes. Thus, $g / f$ is a holomorphic function on a compact Riemann surface. That is, $g / f$ is constant and identically zero. But $g$ is not identically zero, so this is a contradiction.

### The sheaf-theoretic view

Notice that each holomorphism $\pi : X \to Y$ induces a map going in the other direction on each open set of the [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_definition _ structure sheaf|structure sheaves]]. In particular, for each open $W \subseteq Y$ we have a $\mathbb{C}$-algebra homomorphism (a [[Abstract algebra --- math-171/notes/Ring homomorphisms#_definition _ ring homomorphisms|ring homomorphism]] and a [[Linear maps|linear map]])
$$
\pi^* : \mathcal{O}_{Y}(W) \to \mathcal{O}_{X}(\pi^\text{pre}(W))
$$
by $f \mapsto f \circ \pi$. One gets a similar map on the sheaves of meromorphic functions. This plays nicely with restriction too — it is a sheaf morphism. This completely describes holomorphisms!

##### _proposition:_ holomorphisms can be checked on sheaves

A continuous map $\pi : X \to Y$ is a holomorphism if sending $f \mapsto f \circ \pi$ pulls holomorphic functions in $\mathcal{O}_{Y}(W)$ to holomorphic functions in $\mathcal{O}_{X}(\pi^\text{pre}(W))$.

###### _proof sketch:_

Consider $p \in X$, we will show $\pi$ is holomorphic at $p$. Choose $V$ containing $\pi(p)$ to be one of the open sets in the atlas on $Y$ (so that we have the atlas $(V, \psi)$). $\psi$ [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_examples _ dumb examples of holomorphic functions|is a holomorphic function]] on $Y$, and thus, $\psi \circ \pi$ is a holomorphic function in $\mathcal{O}_{X}(\pi^\text{pre}(V))$, and thus, at $p$. By definition, this means, that for any chart $(U, \phi)$, we have $\psi \circ \pi \circ \phi ^{-1}$ holomorphic at $p$ — that is, $\pi$ is holomorphic at $p$.

We don't even have to give the explicit construction to say that $\pi$ pulls back functions. It's enough to show some "algebraic" conditions hold! 

Given a continuous map $\pi : X \to Y$ and a sheaf $\mathcal{F}$ on $X$, there is a natural way to a put a sheaf on $Y$ — just give each open set on $Y$ of $\mathcal{F}$ on its pre-image under $\pi$ in $X$.

##### _definition:_ pushforward sheaf

Given a continuous map $\pi : X \to Y$ and a sheaf $\mathcal{F}$ on $X$, the pushforward sheaf on $Y$ is $\pi_{*}\mathcal{F}$ with
$$
\pi_{*} \mathcal{F}(U) = \mathcal{F}(\pi^\text{pre}(U))
$$
for each open $U \subseteq X$.

Note that in the case of a holomorphism $\pi : X \to Y$, the pushforward of the structure sheaf, $\pi_{*}\mathcal{O}_{X}$ is a sheaf on $Y$, with each $\pi_{*}\mathcal{O}_{X}(U)$ being a ring of holomorphic functions on $\pi^\text{pre}(U)$ which is a subset of $X$. That is, the pushforward sheaf is a sheaf on the codomain ($Y$) taking values that are rings of functions on the domain ($X$).

We can express the relationship between these sheaves by a sheaf morphism.

##### _definition:_ sheaf morphism

A morphism of sheaves (of [[Abstract algebra --- math-171/notes/Rings#_definition _ commutative ring|rings]]) $\varphi : \mathcal{F} \to \mathcal{G}$ on a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]] $X$ is the data of ([[Abstract algebra --- math-171/notes/Ring homomorphisms#_definition _ ring homomorphisms|ring homo]])morphisms $\varphi_{U} = \mathcal{F}(U) \to \mathcal{G}(U)$ on each open $U \subseteq X$ that commute with restriction as follows.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(U) \ar[r, "\varphi_{U}"] \ar[d, "\mathrm{res}"] & \mathcal{G}(U) \ar[d, "\mathrm{res}"] \\
\mathcal{F}(V) \ar[r, "\varphi_{V}"] & \mathcal{G}(V)
	\end{tikzcd}
\end{document}
```

These sheaves also induce morphisms on the stalks (which in the case of Riemann surfaces, happen to be local rings with a unique maximal ideal). If we add an extra condition on what happens at the level of stalks — if we require germs disappearing at $\pi(p)$ to map to germs disappearing at $p$, we get a holomorphism.

##### _proposition:_ holomorphisms are morphisms of locally $\mathbb{C}$-algebraed spaces

A holomorphism between $X$ and $Y$ is the data of a continuous $\pi : X \to Y$ and a morphism of sheaves of $\mathbb{C}$-algebras $\pi^\natural : \mathcal{O}_{Y} \to \pi_{*} \mathcal{O}_{X}$ such that induced morphisms of stalks $\pi^\sharp : \mathcal{O}_{Y, \pi(p)} \to \mathcal{O}_{X, p}$ are morphisms of local rings — that is, they map each [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ maximal ideal|maximal ideal]] $\mathfrak m_{Y, \pi(p)}$ into $\mathfrak{m}_{X, p}$. 