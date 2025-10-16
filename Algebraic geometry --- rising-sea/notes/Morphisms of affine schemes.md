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

$\varphi : B \to A$ induces a morphism of sets $\varphi^* : \operatorname{Spec} A \to \operatorname{Spec} B$ with $\varphi^*(\mathfrak{p}) = \varphi^\text{pre}(\mathfrak{p})$.

This is the **morphism of sets of the affine scheme morphism $\varphi^*$**.  

###### _proof:_

It suffices to show that under $\varphi$, prime ideals pull back to prime ideals.

Let $\mathfrak{q} = \varphi^\mathrm{pre}(\mathfrak{p})$. It's easy to show (using the submodule criterion, say) that $\mathfrak{q}$ is an ideal of $B$. We show it is prime. Suppose $x y \in \mathfrak{q}$. Then $\varphi(x) \varphi(y) \in \mathfrak{p}$. But then $\varphi(x) \in \mathfrak{p}$ aor $\varphi(y) \in \mathfrak{p}$ by primeness. Without loss of generality, if $\varphi(x) \in \mathfrak{p}$, then $x \in \varphi^\text{pre}(\mathfrak{p}) = \mathfrak{q}$ as desired. 

---

##### _examples:_ inclusions of quotients and localisations

1) Suppose $\mathfrak{i} \subseteq A$ is an ideal. Then $\operatorname{Spec} A / \mathfrak{i} \to \operatorname{Spec} A$, dual to the canonical map $A \to A / \mathfrak{i}$ gives the inclusion $\operatorname{Spec} A / \mathfrak{i} \subseteq \operatorname{Spec} A$. It identifies primes $\mathfrak{p / i} \subseteq A / \mathfrak{i}$ with their pre-images — primes $\mathfrak{p} \subseteq A$. Note that if $\mathfrak{i}$ is composed of [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_definition _ nilpotents|nilpotents]], the primes of $A$ containing $\mathfrak{i}$ are just all primes, and so $\operatorname{Spec} A / \mathfrak{i} \to \operatorname{Spec} A$ is a bijection.
2) Suppose $S \subseteq A$ is [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_definition _ multiplicative subsets|multiplicative]]. Then the dual to the $A \to S^{-1} A$ gives the inclusion $\operatorname{Spec} S^{-1} A \subseteq \operatorname{Spec} A$. A prime $\mathfrak{q} \subseteq S^{-1} A$ [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_proposition _ primes of the localisation are primes that don't meet $S$|is just]] $S^{-1} A \mathfrak{p}$ for some $\mathfrak{p} \subseteq A \setminus S$ which has pre-image $\mathfrak{p}$ since it includes $1^{-1} \mathfrak{p} \subseteq S^{-1} \mathfrak{p}$.

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

Consider an $\mathbb{F}$-algebra morphism $\varphi : \mathbb{F}[y_{1}, \dots, y_{n}] \to \mathbb{F}[x_{1}, \dots, x_{m}]$ by $y_{i} \mapsto f_{i}$ (where $f_{i} \in \mathbb{F}[y_{1}, \dots, y_{n}]$). Write this as $\varphi : A \to B$ for convenience. Suppose $g  = q_{1} (y_{1} - f_{1}(a_{1}, \dots, a_{n})) + \dots  + q_{n} (y_{n} - f_{n}(a_{1}, \dots, a_{n}))$ (where $q_{i} \in A$). Then
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

### The morphism of schemes