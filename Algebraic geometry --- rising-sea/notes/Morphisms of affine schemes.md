---
tags:
- rising-sea/3
- alg-geo
---

Let $A, B$ be rings and $\mathbb{F}$ a field.

We don't just want to define affine schemes so that they correspond exactly to rings. We want to define them so that they correspond exactly to the category of rings. That is, morphisms of [[Algebraic geometry --- rising-sea/notes/Affine schemes|affine schemes]] $\operatorname{Spec} A \to \operatorname{Spec} B$ should correspond exactly to [[Abstract algebra --- math-171/notes/Ring homomorphisms|ring homomorphisms]] $B \to A$. The only difference is that the maps go the other way. In full this will become an equivalence of categories $\mathsf{AffSch} \cong \mathsf{Ring}^\mathrm{opp}$ (remember that for us, $\mathsf{Ring}$ is the category of [[Abstract algebra --- math-171/notes/Rings#_definition _ commutative|commutative]], [[Abstract algebra --- math-171/notes/Rings#_definition _ ring with identity, unital rings|unital]] rings with ring homomorphisms preserving identity).

We build this equivalence in three steps, just as for affine schemes and schemes in general. We show how a ring homomorphism $B \to A$ gives a map of points $\operatorname{Spec} A \to \operatorname{Spec} B$, then show it is continuous, and finally, we show that it respects the [[Algebraic geometry --- rising-sea/notes/Affine schemes#The structure sheaf|structure sheaf]] and thus, is a [[morphisms of schemes|morphism of schemes]].

For the rest of this note, let $\varphi : B \to A$ be a ring homomorphism.

### The morphism of sets

##### _proposition, definition:_ ring homomorphisms induce a set morphism of affine shemes

$\varphi : B \to A$ induces a morphism of sets $\varphi^* : \operatorname{Spec} A \to \operatorname{Spec} B$ with $\varphi^*(\mathfrak{p}) = \varphi^\text{pre}(\mathfrak{p})$. $A \mapsto \operatorname{Spec} A$ and $\varphi \mapsto \varphi^*$ then defines a [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|(contravariant) functor]] $\mathsf{Ring} \to \mathsf{Set}$.

This is the **morphism of sets of the affine scheme morphism $\varphi^*$**.  

###### _proof:_

It suffices to show that under $\varphi$, prime ideals pull back to prime ideals.

Let $\mathfrak{q} = \varphi^\mathrm{pre}(\mathfrak{p})$. It's easy to show (using the submodule criterion, say) that $\mathfrak{q}$ is an ideal of $B$. We show it is prime. Suppose $x y \in \mathfrak{q}$. Then $\varphi(x) \varphi(y) \in \mathfrak{p}$. But then $\varphi(x) \in \mathfrak{p}$ aor $\varphi(y) \in \mathfrak{p}$ by primeness. Without loss of generality, if $\varphi(x) \in \mathfrak{p}$, then $x \in \varphi^\text{pre}(\mathfrak{p}) = \mathfrak{q}$ as desired. 

---

##### _examples:_ inclusions of quotients and localisations

1) Suppose $\mathfrak{i} \subseteq A$ is an ideal. Then $\operatorname{Spec} A / \mathfrak{i} \to \operatorname{Spec} A$, dual to the canonical map $A \to A / \mathfrak{i}$ gives the inclusion $\operatorname{Spec} A / \mathfrak{i} \subseteq \operatorname{Spec} A$. It identifies primes $\mathfrak{p / i} \subseteq A / \mathfrak{i}$ with their pre-images — primes $\mathfrak{p} \subseteq A$.
2) Suppose $S \subseteq A$ is [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_definition _ multiplicative subsets|multiplicative]]. Then the dual to the $A \to S^{-1} A$ gives the inclusion $\operatorname{Spec} S^{-1} A \subseteq \operatorname{Spec} A$. A prime $\mathfrak{q} \subseteq S^{-1} A$ [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_proposition _ primes of the localisation are primes that don't meet $S$|is just]] $S^{-1} A \mathfrak{p}$ for some $\mathfrak{p} \subseteq A \setminus S$ which has pre-image $\mathfrak{p}$ since it includes $1^{-1} \mathfrak{p} \subseteq S^{-1} \mathfrak{p}$.

Note that if $\mathfrak{i}$ is composed of [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_definition _ nilpotents|nilpotents]], the primes of $A$ containing $\mathfrak{i}$ are just all primes, and so $\operatorname{Spec} A / \mathfrak{i} \to \operatorname{Spec} A$ is a bijection.

---

##### _example:_ an explicit isomorphism of localised affine schemes

Consider $\operatorname{Spec} \mathbb{C}[x, y] / (xy) \subseteq \mathbb{A}^{2}_{\mathbb{C}}$ by [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_examples _ inclusions of quotients and localisations|the inclusion dual to]] $\mathbb{C}[x, y] \to \mathbb{C}[x, y] / (xy)$. $\operatorname{Spec} \mathbb{C}[x, y] / (xy)$ is all those primes containing $(xy)$, corresponding to all the "points" where $xy$ vanishes. This is just the "union" of the $x$ and $y$-axes. 

If we localise to $\operatorname{Spec} (\mathbb{C}[x, y] / (xy))_{x}$, [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_proposition _ primes of the localisation are primes that don't meet $S$|this is]] all those primes not containing $x$ or all "points" where $x$ doesn't vanish. This gets rid of the whole $y$-axis, including the origin on the $x$-axis. We want this to look exactly like $\operatorname{Spec} \mathbb{C}[x]_{x}$. We will show that the underlying rings are isomorphic, which will later mean that the schemes themselves are isomorphic.

Consider $\mathbb{C}[x, y]_{x} \to \mathbb{C}[x]_{x}$ by $x \mapsto x$ and $y \mapsto 0$. It is surjective with kernel $(y) = (xy)_{x}$. Since [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_proposition _ localisation commutes with quotients|localisation commutes with quotients]] we have an isomorphism $(\mathbb{C}[x, y] / (xy))_{x} \cong \mathbb{C}[x]_{x}$.

---

##### _example:_ folding the complex line

Consider $\varphi : \mathbb{C}[y] \to \mathbb{C}[x]$ by $y \mapsto x^{2}$ and the corresponding $\varphi^* : \mathbb{A}_{\mathbb{C}}^1 \to \mathbb{A}_{\mathbb{C}}^1$. This should be the map double covering $\mathbb{C}$ (think a line) by $\mathbb{C}$ (think two lines, ramified at $0$). In particular, suppose $f(y) = p(y) (y - a) \in (y - a)$. Then $g = \varphi(f)$ has
$$
\begin{align}
g(x) & = \varphi(p(y)) (x^{2} - a)  \\
 & \in (x^{2} - a)  \\
 & = (x + \sqrt{ a }) (x - \sqrt{ a })  \\
 & \subseteq (x \pm \sqrt{ a }).
\end{align}
$$
Conversely, $(x \pm \sqrt{ a })$ must have prime pre-image. Since its pre-image contains the maximal ideal $(y - a)$, its pre-image is $(y - a)$.

Thus, it is exactly the primes $(x \pm \sqrt{ a })$ that have pre-image $(y - a)$ under $\varphi$. Thus, the points $(x \pm \sqrt{ a }) \in \operatorname{Spec} \mathbb{C}[x]$ are mapped to $(y - a) \in \operatorname{Spec} \mathbb{C}[y]$. Equivalently, $\pm \sqrt{ a } \mapsto a$.

---

This generalises to affine $n$-space and $m$-space over a field.

##### _example:_ coordinates for an affine scheme morphism

Consider an $\mathbb{F}$-algebra morphism $\varphi : \mathbb{F}[y_{1}, \dots, y_{n}] \to \mathbb{F}[x_{1}, \dots, x_{m}]$ by $y_{i} \mapsto f_{i}$ (where $f_{i} \in \mathbb{F}[x_{1}, \dots, x_{m}]$). Write this as $\varphi : A \to B$ for convenience. Suppose $g  = q_{1} (y_{1} - f_{1}(a_{1}, \dots, a_{n})) + \dots  + q_{n} (y_{n} - f_{n}(a_{1}, \dots, a_{n}))$ (where $q_{i} \in A$). Then
$$
\begin{align}
\varphi(g) & = \varphi(q_{1}) (f_{1} - f_{1}(a_{1}, \dots, a_{m})) + \dots + \varphi(q_{n}) (f_{n} - f_{n}(a_{1}, \dots, a_{m})) \\
 & \in (x_{1} - a_{1}, \dots, x_{n} - a_{m}).
\end{align}
$$
Here each $\varphi(q_{i})(f_{i} - f_{i}(a_{1}, \dots, a_{m})) \in (x_{1} - a_{1}, \dots, x_{n} - a_{m})$ since it is zero when all $x_{i} = a_{i}$. 

Thus, $(y_{1} - f_{1}(a_{1}, \dots, a_{m}), \dots, y_{n} - f_{n}(a_{1}, \dots, a_{m})) \subseteq \varphi^\text{pre}(x_{1} - a_{1}, \dots, x_{n} - a_{m})$. Since the former is maximal, and the latter must be prime, we have equality. That is, $(a_{1}, \dots, a_{m}) \mapsto (f_{1}(a_{1}, \dots, a_{m}), \dots, f_{n}(a_{1}, \dots, a_{m}))$.

Note this uses the multivariable factor theorem, proved by induction on the single variable factor theorem. The single variable factor theorem works in any $A[x]$ because $x - a$ is monic, and so division by it does not require division of coefficients.

---

In fact, since the "functor" $\varphi \mapsto \varphi^*$ plays nicely with quotients, this generalises further to "affine varieties" sitting in $n$-space and $m$-space. In particular, if $\varphi : B \to A$ is a morphism and $\mathfrak{i} \subseteq A$ and $\mathfrak{j} \subseteq B$ are ideals with $\varphi^\text{img}(\mathfrak{i}) = \mathfrak{j}$, then we get a well-defined $\psi : B  / \mathfrak{j} \to A / \mathfrak{i}$ with $\psi(b + \mathfrak{j}) = \varphi(b)$. This yields a corresponding well defined $\psi^* : \operatorname{Spec} A / \mathfrak{i} \to \operatorname{Spec} B / \mathfrak{j}$.

##### _example:_ a map of subvarieties of affine space

Consider the map from the parabola $\{ (x, y) \mid y = x^{2} \}$ in $\mathbb{C}^{2}$ to the curve in $\mathbb{C}^3$ given by $\{ (x, y, z) \mid y = x^{2}, z = y^{2} \}$, sending $(a, b) \in \mathbb{C}^{2}$ to the point above it — $(a, b, b^{2}) \in \mathbb{C}^3$. This can be written as $\psi^* : \operatorname{Spec} \mathbb{C}[x, y] / (y - x^{2}) \to \operatorname{Spec}\mathbb{C}[x, y, z](y - x^{2}, z - y^{2})$ dual to the quotient map $\psi : \mathbb{C}[x, y, z] / (y - x^{2}, z - y^{2}) \to \mathbb{C}[x, y] / (y - x^{2})$ coming from $\varphi : \mathbb{C}[x, y, z] \to \mathbb{C}[x, y]$ by $x \mapsto x$, $y \mapsto y$, and $z \mapsto y^{2}$. Note that $\varphi^\text{img}(y - x^{2}, z - y^{2}) \subseteq (y - x^{2})$ since $\varphi(y - x^{2}) = y - x^{2}$ and $\varphi(z - y^{2}) = 0$.

---

##### _example:_ affine space as an affine space-bundle

Consider $\pi : \mathbb{A}_{\mathbb{Z}}^n \to \operatorname{Spec} \mathbb{Z}$ induced by the unique $\mathbb{Z} \to \mathbb{Z}[x_{1}, \dots, x_{n}]$. Let $\mathfrak{p} = (p)$ for some prime $p \in \mathbb{Z}$. Then we claim that $\pi^\text{pre}(\mathfrak{p})$ looks like $\mathbb{A}^n_{\mathbb{F}_{p}}$.

$\pi ^{\text{pre}}(\mathfrak{p})$ is all primes $\mathfrak{q} \subseteq \mathbb{Z}[x_{1}, \dots, x_{n}]$ that have pre-image $\mathfrak{p}$ under $\mathbb{Z} \to \mathbb{Z}[x_{1}, \dots, x_{n}]$. These are equivalently, all primes $\mathfrak{q}$ containing $(p) \subseteq \mathbb{Z}[x_{1}, \dots, x_{n}]$. But $\mathbb{F}_{p}[x_{1}, \dots, x_{n}] \cong \mathbb{Z}[x_{1}, \dots, x_{n}] / (p)$ and so its primes are exactly all $\mathfrak{q} / (p)$ with $\mathfrak{q}$ a prime containing $(p)$.

$\pi^\text{pre}((0))$ is all primes $\mathfrak{q} \subseteq \mathbb{Z}[x_{1}, \dots, x_{n}]$ that contain no constant polynomial $a$. But these are exactly the primes of $\mathbb{Q}[x_{1}, \dots, x_{n}]$. Given a prime $\mathfrak{q}' \subseteq \mathbb{Q}[x_{1}, \dots, x_{n}]$, clearing denominators gives an equivalent ideal $\mathfrak{q}' \subseteq \mathbb{Z}[x_{1}, \dots, x_{n}]$. These primes contain no constants since constants are units in $\mathbb{Q}[x_{1}, \dots, x_{n}]$. 

In the opposite direction, any prime $\mathfrak{q} \subseteq \mathbb{Z}[x_{1}, \dots, x_{n}]$ not containing constants is a prime $\mathfrak{q} \subseteq \mathbb{Q}[x_{1}, \dots, x_{n}]$ and primeness is preserved (the irreducibles of $\mathbb{Z}[x_{1}, \dots, x_{n}]$ are just the irreducibles of $\mathbb{Q}[x_{1}, \dots, x_{n}]$ plus the primes).

---

### The morphism of spaces

The morphisms that we get from sets are also topological!

##### _proposition:_ ring homomorphisms induce a continuous map of affine shemes

Given $\varphi : B \to A$, the induced morphism of sets $\pi = \varphi^* : \operatorname{Spec} A \to \operatorname{Spec} B$ is continuous.

###### _proof:_

[[Topology --- math-147/notes/Continuous functions#_proposition _ equivalent definitions of continuity|It suffices]] to show that the pre-image of all closed sets is closed.

Consider some ideal $\mathfrak{i} \subseteq B$ and the corresponding closed subset $V(\mathfrak{i}) \subseteq \operatorname{Spec} B$. Then $\pi^{\text{pre}}(V(\mathfrak{i}))$ is exactly all primes $\mathfrak{p} \subseteq A$ with $\pi(\mathfrak{p}) = \mathfrak{q}$ and $\mathfrak{i} \subseteq \mathfrak{q}$. That is, $\mathfrak{i} \subseteq \mathfrak{p}^{\text{c}} = \mathfrak{q}$. Extending, we get $\mathfrak{i}^\text{e} \subseteq \mathfrak{p}^\text{ce} \subseteq \mathfrak{p}$. Thus, $\mathfrak{p} \in V(\mathfrak{i}^\text{e})$.  Conversely, if $\mathfrak{i}^\text{e} \subseteq \mathfrak{p}$, then contracting gives $\mathfrak{i} \subseteq \mathfrak{i}^\text{ec} \subseteq \mathfrak{p}^\text{c} = \pi(\mathfrak{p})$. That is, $\pi^\text{pre}(V(\mathfrak{i}))$ is exactly the closed set $V(\mathfrak{i}^\text{e})$.

---

This turns the $\operatorname{Spec}$ functor $\mathsf{Ring} \to \mathsf{Set}$ into a functor $\mathsf{Ring} \to \mathsf{Top}$. However, this is not a full functor — there are other continuous maps $\operatorname{Spec} A \to \operatorname{Spec} B$. 

##### _example:_ a non-algebraic continuous map of schemes

There is a continuous map $\mathbb{A}^1_{\mathbb{C}} \to \mathbb{A}^1_{\mathbb{C}}$ just by swapping $(x)$ and $(x - 1)$. This function does not come from a ring homomorphism. 

Suppose a ring homomorphism had $x \mapsto p(x)(x - 1)$. Then we would also have $x - a \mapsto p(x)(x - 1) - a$. By choosing $a = p(b)(b - 1)$, we get $\varphi(x - a) \in (x - b)$. Thus, $\varphi^\text{pre}((x)) = (x - a)$, or equivalently, $\varphi^*((x - b)) = (x - a)$. We can always choose $b \neq 0$, and thus, $\varphi^*$ cannot be the desired homeomorphism.

---

##### _examples:_ inclusions of quotients, topologically

Suppose $\mathfrak{i} \subseteq A$ is an ideal. Then $\operatorname{Spec} A / \mathfrak{i} \to \operatorname{Spec} A$ gives the inclusion (of a closed subset) $\operatorname{Spec} A / \mathfrak{i} \cong V(\mathfrak{i}) \subseteq \operatorname{Spec} A$. The points of the image are $\pi(\mathfrak{p} / \mathfrak{i})$ for primes $\mathfrak{p} / \mathfrak{i} \subseteq A / \mathfrak{i}$. These are exactly the primes $\mathfrak{p} \supseteq \mathfrak{i}$ or $\mathfrak{p} \in V(\mathfrak{i})$. Thus, the image of the map is $V(\mathfrak{i})$.

In fact, the Zariski topology on $\operatorname{Spec} A / \mathfrak{i}$, is the same as the [[Topology --- math-147/notes/Subspaces#_definition _ subspace topology|subspace topology]] on its image. In other words, we show that the map is a homeomorphism onto its image — it is a [[Topology --- math-147/notes/Homeomorphisms#_definition _ open map, closed map|closed map]]. Any closed subset $V(\mathfrak{j} / \mathfrak{i})$ is all primes $\mathfrak{p} / \mathfrak{i}$ containing $\mathfrak{j} / \mathfrak{i}$ (for $\mathfrak{j} / \mathfrak{i}$ an ideal of $A / \mathfrak{i}$). Each of these primes has pre-image $\mathfrak{p}$ containing $\mathfrak{j}$ and $\mathfrak{i}$. Thus, $\pi^\text{img}(V(\mathfrak{j} / \mathfrak{i})) \subseteq V(\mathfrak{j}) \cap V(\mathfrak{i})$. In fact, every $\mathfrak{p} \in V(\mathfrak{j}) \cap V(\mathfrak{i}) \subseteq \operatorname{Spec} A$ is $\pi(\mathfrak{p} / \mathfrak{i})$ for some $\mathfrak{p} / \mathfrak{i} \in V(\mathfrak{j} / \mathfrak{i})$, so we have equality $\pi^\text{img}(V(\mathfrak{j} / \mathfrak{i})) = V(\mathfrak{j}) \cap V(\mathfrak{i})$. This is a closed subset in the subspace topology on $V(\mathfrak{i})$.

Note that if $\mathfrak{i}$ is composed of nilpotents, not only is $\pi : \operatorname{Spec} A / \mathfrak{i} \to \operatorname{Spec} A$ bijective, but it is also a [[Topology --- math-147/notes/Homeomorphisms#_definition _ homeomorphism|homeomorphism]] (so any difference as schemes must come in the structure sheaf). Since we already know $\pi$ is continuous and bijective, [[Topology --- math-147/notes/Homeomorphisms#_proposition _ homeomorphisms, closed bijections, and open bijections|we need only]] show that the map is closed. We have already shown this!

---
##### _example:_ inclusions of localisations (away from the vanishing of a function), topologically

Suppose $f \in A$. Then $\pi : \operatorname{Spec} A_{f} \to \operatorname{Spec} A$ gives the inclusion (of an open subset) $\operatorname{Spec} A_{f} \subseteq \operatorname{Spec} A$. This is the inclusion of the [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets|distinguished open set]] $D(f) = \operatorname{Spec} A \setminus V(f)$. The points of $\operatorname{Spec} A_{f}$ are exactly $S^{-1} \mathfrak{p}$ for primes $\mathfrak{p}$ not containing $f$. Since $\pi(S^{-1} \mathfrak{p}) = \mathfrak{p}$, the image under $\pi$ is exactly all primes $\mathfrak{p} \in D(f)$.

Again, this is a homeomorphism onto its image. A closed subset $V(S^{-1} \mathfrak{i}) \subseteq \operatorname{Spec} A_{f}$ consists of all primes $S^{-1} \mathfrak{p}$ containing $S^{-1} \mathfrak{i}$. Each of these primes has $\pi(S^{-1} \mathfrak{p}) = \mathfrak{p}$ with $\mathfrak{p}$ not containing $f$ and containing $\mathfrak{i}$ (since $\mathfrak{i} \subseteq (S^{-1} \mathfrak{i})^\text{c} \subseteq \mathfrak{p} = (S^{-1} \mathfrak{p})^\text{c}$). That is, $\pi^\text{img}(V(S^{-1} \mathfrak{i})) \subseteq D(f) \cap V(\mathfrak{i})$. Conversely, every prime $\mathfrak{p}$ containing $\mathfrak{i}$ and not containing $f$ has prime extension $S^{-1} \mathfrak{p} \subseteq A_{f}$ containing the extension $S^{-1} \mathfrak{i}$. Thus, we have the equality $\pi^\text{img}(V(S^{-1} \mathfrak{i})) = D(f) \cap V(\mathfrak{i})$. These are exactly the closed subsets of $D(f)$ in the subspace topology.

Note that $\operatorname{Spec} S^{-1} A \subseteq \operatorname{Spec} A$ need not be open nor closed in general. For example, $\operatorname{Spec} \mathbb{F}[x]_{(x)} \subseteq \mathbb{A}_{\mathbb{F}}^1$  consists of only the points $(0)$ and $(x)$. This is not open ([[Topology --- math-147/notes/Limit points and closed sets#_proposition _ open set minus closed set and closed set minus open set|subtract the closed set]] $\{ (x) \}$ and $\{ (0) \}$ is not open). It is not closed either — the only closed subset containing $(0)$ is the whole space $\operatorname{Spec} \mathbb{F}[x]$ (which has infinitely many points).

---

### The morphism of affine schemes

In general we will want our morphisms of affine schemes to be exactly those maps $\operatorname{Spec} A \to \operatorname{Spec} B$ coming from ring homomorphisms $B \to A$. However, since morphisms of schemes are difficult to define and isomorphisms are easier, we first define isomorphisms of affine schemes.

##### _proposition:_ isomorphisms of affine schemes are isomorphisms of rings

The [[Algebraic geometry --- rising-sea/notes/Schemes#_definition _ scheme, Zariski topology, isomorphism of schemes|isomorphisms of schemes]] $\operatorname{Spec} A \to \operatorname{Spec} B$ are in bijection with the ring isomorphisms $B \to A$.

###### _proof:_

First suppose we have an isomorphism $\varphi : B \to A$ with inverse $\psi : A \to B$. Since $\varphi^* : \operatorname{Spec} A \to \operatorname{Spec} B$ is continuous and has inverse $\psi^* : \operatorname{Spec} B \to \operatorname{Spec} A$, it is a homeomorphism. 

---

Our classical example of the inclusion $\operatorname{Spec} A_{f} \to \operatorname{Spec} A$ is easy to characterise for schemes.

##### _example:_ inclusions of distinguished opens as schemes

Suppose $f \in A$. Then there is an isomorphism of schemes $D(f), \mathscr{O}_{\operatorname{Spec} A \mid D(f)} \cong \operatorname{Spec} A_{f}$. We already have a homeomorphism $\pi$ of topological spaces, so it suffices to check that $\pi_{*} \mathscr{O}_{\operatorname{Spec} A_{f}}(D(g)) = \mathscr{O}_{\operatorname{Spec}A \mid D(f)}(D(g))$ for $D(g) \subseteq D(f)$. 

On one hand we have $\mathscr{O}_{\operatorname{Spec} A \mid D(f)}(D(g)) = A_{g}$. $\pi^\text{pre}(D(g))$ is all primes $\mathfrak{p}_{f} \subseteq A_{f}$ such that $\mathfrak{p}$ doesn't contain $g$. These are exactly the primes $\mathfrak{p}_{f}$ themselves not containing $g$. Since $D(g) \subseteq D(f)$ we have $g^k = b f$. Thus, $(A_{f})_{g} \cong A_{g}$ by $(a / f^m) / g^n \mapsto a b^m / g^{n + km}$. That is,
$$
\pi_{*} \mathscr{O}_{\operatorname{Spec} A_{f}}(D(g)) = \mathscr{O}_{\operatorname{Spec} A_{f}}(D(g)) = (A_{f})_{g} \cong A_{g} = \mathscr{O}_{\operatorname{Spec} A \mid D(f)}(D(g)).
$$

---

Understanding closed subsets as schemes is more difficult, particularly since a given closed subset can be endowed with many scheme structures. It suffices to note briefly that $\operatorname{Spec} A / \mathfrak{i}$ endows $V(\mathfrak{i}) \subseteq \operatorname{Spec} A$ with a scheme structure, but so does any $\operatorname{Spec} A / \mathfrak{j}$ with $\sqrt{ \mathfrak{j} } = \sqrt{ \mathfrak{i} }$.

To define morphisms of affine schemes in general, we first show how a morphism of rings $B \to A$ defines a morphism of ringed spaces $\operatorname{Spec} A \to \operatorname{Spec} B$.

##### _definition:_ the induced morphism of ringed spaces of affine schemes

Suppose $\pi^\sharp : B \to A$ is a morphism of rings and let $\pi : \operatorname{Spec} A \to \operatorname{Spec} B$ be the induced morphism of topological spaces. Then $\pi$ is the **induced morphism of ringed spaces of affine schemes** with $\mathscr{O}_{\operatorname{Spec} B} \to \pi_{*} \mathscr{O}_{\operatorname{Spec} A}$ by $B_{g} \to A_{\pi^\sharp(g)}$ on each distinguished open $D(g) \subseteq B$.

---

It takes some serious work to show that this is well-defined — we need to show that $\pi^\text{pre}(D(g)) = D(\pi^\sharp(g))$, that the definition $B_{g} \to A_{\pi^\sharp(g)}$ is independent of $g$, and then that the morphisms commute with restriction so that they form a morphism of sheaves.

This notion of morphisms of ringed spaces still isn't enough — not all morphisms of ringed spaces of affine schemes come from ring homomorphisms. Essentially we could have a morphism of ringed spaces where functions vanishing at a point pull back to functions that do not vanish at the same point.

##### _example:_ a non-scheme morphism of ringed spaces of affine schemes

Consider $\operatorname{Spec} \mathbb{F}(x) \to \operatorname{Spec} \mathbb{F}[y]_{(y)}$ with $\pi : (0) \mapsto (y)$ at the level of points, $\pi^\sharp(\operatorname{Spec} \mathbb{F}[y]_{(y)}) : y \mapsto x$ and $\pi^\sharp(D(y)) : \mathbb{F}(y) \to 0$. Since $0$ is [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ initial, final, and zero objects|final]] in $\mathsf{Ring}$,
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathbb{F}[y]_{(y)} \ar[r] \ar[d] & \mathbb{F}(x) \ar[d] \\
		\mathbb{F}(y) \ar[r] & 0
	\end{tikzcd}
\end{document}
```
commutes, $\pi^\sharp$ is a morphism $\mathscr{O}_{\operatorname{Spec} \mathbb{F}[y]_{(y)}} \to \pi_{*} \mathscr{O}_{\operatorname{Spec} \mathbb{F}(x)}$, and $\pi, \pi^\sharp$ is a morphism of ringed spaces. However, $\pi^\sharp$ is not induced by a ring homomorphism. $\pi^\sharp(\operatorname{Spec} \mathbb{F}[y]_{(y)}) : \mathbb{F}[y]_{(y)} \to \mathbb{F}(x)$ induces a map of points $\operatorname{Spec} \mathbb{F}(x) \to \operatorname{Spec} \mathbb{F}[y]_{(y)}$ by $(0) \mapsto (0)$. When we send $y \mapsto x$, we don't send $(y)$ into $(0)$.

---

We will see that by requiring functions that vanish at a point to pull back to vanishing functions, we can ensure that the morphisms are exactly those induced by ring homomorphisms.

##### _proposition:_ morphisms of local ringed spaces are morphisms of affine schemes

If $\pi : \operatorname{Spec} A \to \operatorname{Spec} B$ is a morphism of local ringed spaces, then it is the morphism induced by the ring map $\pi^\sharp(\operatorname{Spec} B) : B \to A$ on global sections —
$$
\pi^\sharp(\operatorname{Spec} B) : \mathscr{O}_{\operatorname{Spec} B}(\operatorname{Spec B}) = B \to A = \mathscr{O}_{\operatorname{Spec} A}(\operatorname{Spec} A) = \pi_{*}\mathscr{O}_{\operatorname{Spec} A}(\operatorname{Spec} B).
$$

###### _proof:_

First suppose $\pi, \pi^\sharp : \operatorname{Spec} A \to \operatorname{Spec} B$ is induced by the global sections morphism $\pi^\sharp : B \to A$. Then for any $\mathfrak{p} \in \operatorname{Spec} A$ mapped to $\mathfrak{q} \in \operatorname{Spec} B$ we have $\pi^\sharp_{\mathfrak{q}} : B_{\mathfrak{q}} \to A_{\mathfrak{p}}$. This is the unique map of $B$-algebras induced by the fact that $B \setminus \mathfrak{q}$ is invertible in $A_{\mathfrak{p}}$ — note that $b \in B \setminus \mathfrak{q}$ acts by multiplication by $\pi^\sharp(b)$ and $\pi^{\sharp, \text{img}}(B \setminus \mathfrak{q}) \subseteq A \setminus \mathfrak{p}$. This map has $b / s \mapsto \pi^\sharp(b) / \pi^\sharp(s)$. Since $\pi^{\sharp, \text{img}}(\mathfrak{q}) \subseteq \mathfrak{p}$, this gives $\pi^{\sharp, \text{img}}_{\mathfrak{q}}(B_{\mathfrak{q}} \mathfrak{q}) \subseteq A_{\mathfrak{p}} \mathfrak{p}$. That is, $\pi^\sharp_{\mathfrak{q}}$ is a morphism of local rings and any "morphism of affine schemes" is a morphism of local ringed spaces.

Now suppose $\pi, \pi^\sharp : \operatorname{Spec} A \to \operatorname{Spec} B$ is a morphism of local ringed spaces. By abuse of notation, let $\pi^\sharp$ denote $\pi^\sharp(\operatorname{Spec} B) : B \to A$. We want to show that a point $p \in \operatorname{Spec} A$ with prime ideal of vanishing functions $\mathfrak{q}$ is sent to $q \in \operatorname{Spec} B$ with prime ideal of vanishing functions $\mathfrak{q} = \pi^{\sharp, \text{pre}}(\mathfrak{p}) \in \operatorname{Spec} B$. 

Suppose $p \mapsto q$ with corresponding primes of vanishing functions $\mathfrak{p}$ and $\mathfrak{q}$ respectively. Then since $\mathfrak{p} \subseteq A$ is the prime ideal of functions vanishing at the point $\mathfrak{p}$, and by the [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_proposition _ localisation is a colimit|colimit characterisation of localisation]], we get a stalk morphism equal to the morphism of localisations $\pi^\sharp_{q} = \pi^\sharp_{\mathfrak{q}} : B_{\mathfrak{q}} \to A_{\mathfrak{p}}$. It is a morphism of local rings — $\pi^{\sharp, \text{img}}_{\mathfrak{q}}(B_{\mathfrak{q}} \mathfrak{q}) \subseteq A_{\mathfrak{p}} \mathfrak{p}$ and so $B_{\mathfrak{q}} \mathfrak{q} \subseteq \pi^{\sharp, \text{pre}}_{\mathfrak{q}}(A_{\mathfrak{p}} \mathfrak{p})$. Since $B_{\mathfrak{q}} \mathfrak{q}$ is maximal, it must be the whole pre-image of the maximal ideal of $A_{\mathfrak{p}}$. Since $\pi^\sharp_{\mathfrak{q}} = \pi^\sharp$ on elements of $B$, we get that $\pi^{\sharp, \text{img}}(\mathfrak{q}) \subseteq \mathfrak{p}$ implying $\mathfrak{q} \subseteq \pi^{\sharp, \text{pre}}(\mathfrak{p})$ (this is actually a little technical, but if $s \pi^\sharp(b) \in \mathfrak{p}$, then since $s \not\in \mathfrak{p}$ we must have $\pi^\sharp(b) \in \mathfrak{p}$). Conversely, if $\pi^{\sharp}(b) \in \mathfrak{p}$, then we must have $\pi^\sharp_{\mathfrak{q}}(b) \in A_{\mathfrak{p}} \mathfrak{p}$, and thus, $b \in B_{\mathfrak{q}} \mathfrak{q}$. By a similar argument, this too forces $b \in \mathfrak{q}$. That is, $\mathfrak{q} \supseteq \pi^{\sharp, \text{pre}}(\mathfrak{p})$. This completes the double inclusion we wanted.

Now that we know that $\pi$ is induced by $\pi^\sharp$ at the level of sets, we get that $D(g) \subseteq \operatorname{Spec} B$ has pre-image $D(\pi^\sharp(g))$. By the definition of a morphism of sheaves the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{O}_{\mathrm{Spec} B}(\mathrm{Spec} B) \ar[r, "\pi^\sharp"] \ar[d, "\otimes B_{g}"] & \pi_{*}\mathcal{O}_{\mathrm{Spec} A}(\mathrm{Spec} B) \ar[d, "\otimes B_{g}"] \\
		\mathcal{O}_{\mathrm{Spec} B}(D(g)) \ar[r, "\pi^\sharp(D(g))"] & \pi_{*} \mathcal{O}_{\mathrm{Spec} A}(D(g))
	\end{tikzcd}
\end{document}
```

Since the vertical restriction maps are just localisation by the action of $g$ (that is, tensoring with $B_{g}$, to make clear that we invert $\pi^\sharp(g)$ on $A$), the map $\pi^\sharp(D(g))$ is determined by $\pi^\sharp(\operatorname{Spec} B)$ and the universal property of localisation. Thus, $\pi^\sharp$ is the sheaf map induced by $\pi^\sharp(\operatorname{Spec} B)$.

---

##### _definition:_ morphism of affine schemes

A **morphism of affine schemes** $\operatorname{Spec} A \to \operatorname{Spec} B$ is a morphism of local ringed spaces. 

Equivalently, it is a morphism of ringed spaces induced by a ring homomorphism $B \to A$.

---

##### _example:_ maps from the dual numbers

Recall that the [[Algebraic geometry --- rising-sea/notes/Examples of schemes#The dual numbers|dual numbers]] $\mathbb{C}[\varepsilon] / (\varepsilon^{2})$ look like a point with fuzz. Now consider the map $\mathbb{C}[x] \to \mathbb{C}[\varepsilon] / (\varepsilon^{2})$ by $x \mapsto a \varepsilon$ for some $a \in \mathbb{C}$. For non-zero $a$, this gives a map $\operatorname{Spec} \mathbb{C}[\varepsilon] / (\varepsilon^{2}) \to \mathbb{A}_{\mathbb{C}}^1$ that sends $(\varepsilon) \mapsto (x)$ and $(0) \mapsto (x^{2})$. That is, image of the map looks like a point with fuzz around it. The pull back of functions looks like pulling back functions to their linear parts, scaled by $a$. For $a = 0$, the $(0) \mapsto (x)$ as well, so the fuzz collapses.
 
---

##### _corollary:_ affine schemes are the opposite category of rings

The category of affine schemes $\mathsf{AffSch}$ is equivalent to the [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ opposite (or dual) categories|opposite category]] of $\mathsf{Ring}$.

---

Note that this means that there may be more than one morphism between two one-point spaces! In particular, the forgetful functor $\mathsf{AffSch} \to \mathsf{Set}$ is not faithful. This also means that injections of the underlying sets of affine schemes may not be monic as maps of affine schemes.

##### _example:_ two maps between one point spaces, or injections of sets are not monomorphisms of affine schemes

The canonical map $\operatorname{Spec} \mathbb{Q}[i] \to \operatorname{Spec} \mathbb{Q}$ is an injection of sets (sending $(0)$ to $(0)$), but both automorphisms in $\operatorname{Gal}(\mathbb{Q}[i] / \mathbb{Q})$ give automorphisms $\operatorname{Spec} \mathbb{Q}[i] \to \operatorname{Spec} \mathbb{Q}[i]$ which compose to the same map $\operatorname{Spec} \mathbb{Q}[i] \to \operatorname{Spec} \mathbb{Q}[i] \to \operatorname{Spec} \mathbb{Q}$.

---