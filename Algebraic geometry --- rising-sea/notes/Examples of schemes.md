---
tags:
- rising-sea
- alg-geo
- comm-alg
---

Let $A$ be a ring and $\mathbb{F}$ a field. Let $X$ be a scheme.

Here we collect examples of [[Algebraic geometry --- rising-sea/notes/Schemes#_definition _ scheme, Zariski topology, isomorphism of schemes, functions|schemes]]. Many are [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition _ affine scheme|affine]].

### The complex affine line

The complex affine line is a special case of affine $n$-space over any ring. It is also a special case that behaves exactly like the general case of the affine line over any algebraically closed field $\overline{\mathbb{F}}$. Replacing $\mathbb{C}$ with $\overline{\mathbb{F}}$ will usually be fine in this example.

##### _definition:_ the complex affine line, $\mathbb{A}_{\mathbb{C}}^1$

The **complex affine line** is $\mathbb{A}^1_{\mathbb{C}} = \operatorname{Spec} \mathbb{C}[x]$.

---

##### _proposition:_ the points of the complex affine line

The points of the $\mathbb{A}_{\mathbb{C}}^1$ are exactly $(0)$ and $(x - a)$ for $a \in \mathbb{C}$.

###### _proof:_

A point of $\mathbb{A}^1_{\mathbb{C}}$ is a prime ideal of $\mathbb{C}[x]$. 

Any $\mathbb{F}[x]$ is a [[Abstract algebra --- math-171/notes/Unique factorisation#_definition _ Euclidean domain|Euclidean domain]] with polynomial long division. Thus, $\mathbb{C}[x]$ is a [[Abstract algebra --- math-171/notes/Unique factorisation#_definition _ principal ideal domain|principal ideal domain]]. Thus, any $\mathfrak{p} \subseteq \mathbb{C}[x]$ is $(p(x))$ for some $p(x) \in \mathbb{C}[x]$. 

Since $\mathbb{C}[x]$ is an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domains]], $(0)$ [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_proposition _ prime ideals have integral domains as quotients|must be prime]].

We claim that every prime ideal requires its generating polynomial $p(x)$ to be irreducible. If a polynomial $f(x)$ is not irreducible, then there are $g(x), h(x)$ of smaller degree than $f(x)$ such that $f(x) = g(x) h(x)$. Since they are of smaller degree, they are not multiples of $f(x)$, and thus, not in $(f(x))$. Thus, $(f(x))$ is not prime. By the [[Complex analysis --- math-135/notes/Cauchy integral formula#_theorem _ the fundamental theorem of algebra|fundamental theorem of algebra]] the only irreducible polynomials in $\mathbb{C}[x]$ are linear. All the linear polynomials are prime, and in fact maximal since $\mathbb{C}[x]/(x - a) \cong \mathbb{C}$.

---

The right way to imagine these points is to draw $\mathbb{C}$ as a line (it is algebraically $1$-dimensional, but this is already a little weird), with $a \in \mathbb{C}$ corresponding to $(x - a) \in \operatorname{Spec} \mathbb{C}[x]$. $(0)$ can be imagined as a "$1$-dimensional point" spread out over the whole line and "close to" every point. That is, $\mathbb{A}^1_{\mathbb{C}}$ is $\mathbb{C}$ with an extra scheme-y point.

##### _proposition:_ values of functions on $\mathbb{A}^1_{\mathbb{C}}$ are values of polynomials in $\mathbb{C}$

The value of $f \in \mathbb{C}[x]$ at $(x - a) \in \mathbb{A}_{\mathbb{C}}^1$ is $f(a)$.

###### _proof sketch:_

$\mathbb{C}[x] \to \mathbb{C}[x] / (x - a) \xrightarrow{\sim} \mathbb{C}$ is given by $f \mapsto f(a)$.

---

### The final scheme

$\operatorname{Spec} \mathbb{Z}$ will turn out to be the [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ initial, final, and zero objects|final object]] in the category of schemes, dually to how $\mathbb{Z}$ [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_example _ initial and final objects in specific categories|is the initial object in the category of rings]]. The points of $\operatorname{Spec} \mathbb{Z}$ are then just $(0)$ and $(p)$ for $p$ [[Superdiscrete --- math-55A/notes/Prime numbers#_definition _ prime numbers|prime]]. You can draw this exactly like $\overline{\mathbb{F}}[x]$ — a line with $0$-dimensional points $(p)$ on it, and a $1$-dimensional point $(0)$. 

However, its functions have a strange behaviour unlike $\mathbb{A}^1_{\overline{\mathbb{F}}}$ — they take values in different fields.

##### _example:_ values of a function on $\operatorname{Spec} \mathbb{Z}$ in different fields

$27 \in \mathbb{Z}$ is a function on $\operatorname{Spec} \mathbb{Z}$ taking value $2 \in \mathbb{Z} / (5)$ at $(5) \in \operatorname{Spec \mathbb{Z}}$ and $-1 \equiv 6 \in \mathbb{Z} / (7)$ at $(7)$.

It vanishes at $(3)$ (in fact, we want to be able to say that it has a triple zero).

---

The topology of $\operatorname{Spec} \mathbb{Z}$ is nearly the [[Topology --- math-147/notes/Topologies#_example _ the finite and countable complement topologies|cofinite topology]]. Notice that to show this we just need to show that the $V(\mathfrak{i})$ are exactly the finite sets.

For any $\mathfrak{i} = (a)$ ($\mathbb{Z}$ is principal), the chain of ideals containing $\mathfrak{i}$ is finite. The ideals containing $\mathfrak{i}$ are exactly those obtained by picking off one factor at a time from the unique factorisation of $a$. Thus, there are only finitely many primes in $V(\mathfrak{i})$. 

Conversely, each prime $\mathfrak{p} \neq (0)$ is maximal, and thus has $V(\mathfrak{p}) = \{ \mathfrak{p} \}$. This means that every finite point set not including $(0)$ is closed. However, $\{ (0) \}$ itself is not closed since $(0)$ is contained in other prime ideals (so any closed set containing $(0)$ must also contain other points).

In fact, $(0)$ is contained in *every* prime of $\mathbb{Z}$. Thus, the only closed set containing $(0)$ is the whole space $\operatorname{Spec} \mathbb{Z}$. Since open sets are just complements of closed sets, this means that any neighbourhood of any point $\mathfrak{p}$ contains $(0)$. We will later say that this means $(0)$ is the generic point of $\operatorname{Spec} \mathbb{Z}$.

### The affine line and affine space in general

In fact, we can define the affine line and affine space over any ring.

##### _definition:_ affine $n$-space

**Affine $n$-space over $A$** is the affine scheme $\operatorname{Spec} A[x_{1}, \dots, x_{n}]$.

---

We usually choose $A$ a field. The affine line over a field $\mathbb{F}$ always looks a little like $\mathbb{A}^1_{\mathbb{F}}$ or $\operatorname{Spec} \mathbb{Z}$ — there is always at least a line with infinitely many primes. 

##### _proposition:_ affine space always has infinitely many points

The set of points of $\mathbb{A}_{\mathbb{F}}^1$ is infinite.

###### _proof:_

Suppose $\mathfrak{p}_{1} = (p_{1}), \dots, \mathfrak{p}_{n} = (p_{n})$ is a finite list of primes in $\mathbb{F}[x]$, each generated by a distinct irreducible polynomial (since $\mathbb{F}[x]$ is a [[Abstract algebra --- math-171/notes/Unique factorisation#_definition _ principal ideal domain|principal ideal domain]]). Consider $f(x) = p_{1}(x) \cdots p_{n}(x) + 1$. Since it is not divisible by any of the $p_{i}$, it must be divisible by some different irreducible $p$. That is, write $f(x) = p(x) q(x)$

Since $p q \equiv 1$ in each integral domain $\mathbb{F}[x] / \mathfrak{p}_{i}$, we have $p \not\in \mathfrak{p}_{i}$ for each $i$. Since they are both irreducible, this means $(p) \neq (p_{i})$ for each $i$ and $\mathfrak{p} = (p)$ is a new prime ideal not in the finite list.

---

$\mathbb{A}^1_{\mathbb{F}}$ is also like $\operatorname{Spec} \mathbb{Z}$ in its topology. It also has a "nearly cofinite" topology for the same reason as $\operatorname{Spec} \mathbb{Z}$ — it is principal. Thus, all ideals have only finitely many primes containing them. Conversely, all primes except $(0)$ are maximal, and thus, closed. Again, $(0)$ is near every point.

For $\mathbb{C}$ (or any algebraically closed $\overline{\mathbb{F}}$) any affine $n$-space behaves similarly to the affine line, with some scheme-theoretic points (just like $(0) \in \mathbb{A}^1_{\mathbb{C}}$).

##### _example:_ points of $\mathbb{A}_{\mathbb{C}}^{2}$

The points of $\mathbb{A}^{2}_{\mathbb{C}}$ are
- $(0)$ — the "two-dimensional" generic point of the plane
- all irreducible $(f(x, y))$ — the "one-dimensional" generic points corresponding to  curves $\{ (a, b) \mid f(a, b) = 0 \} \subseteq \mathbb{C}^{2}$ in the plane
- the regular closed points $(x - a, y - b)$ corresponding to $(a, b) \in \mathbb{C}^{2}$.

We can prove that these really are all the points. Clearly if $\mathfrak{p} = (f(x, y)) \subseteq \mathbb{C}[x, y]$ is a principal prime, then $f(x, y)$ is irreducible. Suppose $\mathfrak{p} \subseteq \mathbb{C}[x, y]$ is prime, but not principal. Then for any $f(x, y) \in \mathfrak{p}$ there must be some $g(x, y)$ such that $g(x, y) \neq q(x, y) g(x, y)$. 

Since $f$ and $g$ are coprime in $\mathbb{C}[x, y]$ they are coprime in $\mathbb{C}(x)[y]$. Since $\mathbb{C}(x)[y]$ is a [[Abstract algebra --- math-171/notes/Unique factorisation#_definition _ Euclidean domain|Euclidean domain]], they have a least common factor $1$. That is,
$$
\frac{p_{1}(x)}{q_{1}(x)} f(x, y) + \frac{p_{2}(x)}{q_{2}(x)} g(x, y) = 1
$$
for some polynomials, $p_{1}, p_{2}, q_{1}, q_{2} \in \mathbb{C}[x]$. Clearing denominators, we get $h \in \mathbb{C}[x]$ as a linear combination of $f$ and $g$. By primality it follows that one of its linear factors $x - a$ is in $\mathfrak{p}$. Similarly, we can get some $y - b \in \mathfrak{p}$. Since $(x - a, y - b) \subseteq \mathfrak{p}$ and the former is maximal, we have $(x - a, y - b) = \mathfrak{p}$.

---

##### _example:_ points of $\mathbb{A}^3_{\mathbb{C}}$

The points of $\mathbb{A}^3_{\mathbb{C}}$ are  
- $(0)$ — the "three-dimensional" generic point
- all irreducible $(f(x, y, z))$ — the "two-dimensional" generic points corresponding to hypersurfaces $\{ (a, b, c) \mid f(a, b, c) = 0 \} \subseteq \mathbb{C}^{3}$
- lots of "one-dimensional" generic points corresponding to irreducible curves in $\mathbb{C}^{3}$ (for which there is no reasonable classification)
- finally, the regular points $(x - a, y - b, z - c)$ corresponding to $(a, b, c) \in \mathbb{C}^{3}$.

---

The topology of affine space is also similar to the affine. Instead of just having a nearly cofinite topology for the whole space, each of the embedded curves looks kind of like the affine line. Each curve is a closed set of its own, with a generic point and the points "on the curve". Finite unions of these curves are closed sets.

##### _example:_ the closed sets of $\mathbb{A}^{2}_{\mathbb{C}}$

The closed sets of $\mathbb{A}^{2}_{\mathbb{C}}$ are finite unions of
- the entire space, which has generic point $(0)$
- curves $V(f(x, y))$ (for irreducible $f$), containing $(f(x, y))$ and all $(x - a, y - b)$ with $f(a, b) = 0$ (or equivalently, $(f) \subseteq (x - a, y - b)$)
- closed points $(x - a, y - b)$.

Here we have generated a classification based on the irreducible closed sets of $\mathbb{A}^{2}_{\mathbb{C}}$.

---

##### _example:_ $V(xy, yz) \subseteq \mathbb{A}^3_{\mathbb{C}}$

Similarly, $V(xy, yz)$ is the locus $xy = yz = 0$. This includes the $xz$-plane — all prime ideals $(x - a, y, z - c)$, all the curves $(y, f(x, z))$ (including the $x$-axis — all prime ideals $(x - a, y, z)$ — and the $z$-axis), and the generic point of the plane $(x, z)$. This also includes the $y$-axis — all prime ideals $(x, y - b, z)$

---

However, over a field that is not algebraically closed, even the closed points (the maximal ideals) can correspond to points that are not there in $\mathbb{F}^n$.

##### _example:_ points of $\mathbb{A}^1_{\mathbb{R}}$

The points of $\mathbb{A}^1_{\mathbb{R}}$ are $(0)$ and all irreducible polynomials. Since $\mathbb{R}[x]$ is [[Abstract algebra --- math-171/notes/Unique factorisation|Euclidean]], these are all maximal. The "normal" maximal ideals, corresponding to $a \in \mathbb{R}^1$ are $(x - a) \subseteq \mathbb{R}[x]$. The other maximal ideals are $(x^{2} + bx + c)$ with $b^{2} < c$. These correspond to adjoining roots $\lambda, \overline{\lambda} \in \mathbb{C} \setminus \mathbb{R}$ to $\mathbb{R}$. 

These are all of the other maximal ideals — we can prove that there are no subfields of $\mathbb{C}$ between $\mathbb{R}$ and $\mathbb{C}$. This follows since $\mathbb{R}[\lambda] \cong \mathbb{R}[i]$.

---

This example of maximal ideals corresponding to finite extensions continues and is formalised in [[Algebraic geometry --- rising-sea/notes/Hilbert's Nullstellensatz|Hilbert's Nullstellensatz]].

##### _examples:_ affine spaces over $\mathbb{Q}$

The (closed) points of $\mathbb{A}^1_{\mathbb{Q}}$ are maximal ideals of $\mathbb{Q}$, and thus, by the [[Algebraic geometry --- rising-sea/notes/Hilbert's Nullstellensatz#_theorem _ Hilbert's (strong) Nullstellensatz or Zariski's lemma|strong Nullstellensatz]], each maximal ideal corresponds to all Galois conjugates in the corresponding residue field extension.

The (closed) points of $\mathbb{A}^2_{\mathbb{Q}}$ are similar — each maximal ideal corresponds to pairs of roots glued to their Galois conjugates. For example, $(y - x, x^{2} - 2)$ and $(y + x, x^{2} - 2)$ correspond to $(\sqrt{ 2 }, \sqrt{ 2 }) \sim (- \sqrt{ 2 }, - \sqrt{ 2 })$ and $(\sqrt{ 2 }, - \sqrt{ 2 }) \sim (- \sqrt{ 2 }, \sqrt{ 2 })$ respectively.

This description can be extended to non-closed points of $\mathbb{A}^{2}_{\mathbb{Q}}$ by $\mathbb{C}^{2} \to \mathbb{A}_{\mathbb{Q}}^{2}$ with $(z_{1}, z_{2}) \mapsto \mathfrak{p}$ where $\mathfrak{p} \subseteq \mathbb{Q}[x, y]$ is the prime of polynomials vanishing on $(z_{1}, z_{2})$. This map is in fact surjective, and thus, describes every point of $\mathbb{A}^2_{\mathbb{Q}}$ as the vanishing prime of some tuple in $\mathbb{C}^{2}$. It also generalises to arbitrary dimension.

> [!missing]
> image of $(\pi, \pi^{2})$, explanation of surjectivity, generalisation to higher dimensions

---

##### _example:_ infinite-dimensional affine space is non-Noetherian

We can get non-Noetherian $\operatorname{Spec} A$ from our favourite non-Noetherian ring — $\mathbb{F}[x_{1}, x_{2}, \dots]$. The closed subsets $V(x_{1}) \supseteq V(x_{1}, x_{2}) \supseteq \cdots$ form an infinite strictly descending chain (the codimension $1$ plane $V(x_{1})$ contains the codimension $2$ plane $V(x_{1}, x_{2})$ and so on). That is, $\mathbb{A}^\infty_{\mathbb{F}}$ is non-Noetherian.

We can also see that $\mathbb{A}_{\mathbb{F}}^\infty$ is non-Noetherian [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#_proposition _ Noetherian spaces have (quasi)compact open subsets|because]] it has an open subset that is not quasicompact. $\mathbb{A}_{\mathbb{F}}^\infty \setminus (x_{1}, x_{2}, \dots)$ is covered by all $D(x_{i})$, but no finite combination of them. For example, the point $(x_{j} - a_{j}, x_{i_{k}})_{j, k}$ is contained in our open subset, but not in the finite cover of all $D(x_{i_{k}})$.

---

### The dual numbers

The **dual numbers** are the ring $\mathbb{F}[\varepsilon] / (\varepsilon^{2})$ (think of this as some adjoining some error $\varepsilon$ that we want to keep track of to the first order, but can ignore in higher orders). It has just one point $(\varepsilon)$ (by the [[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the fourth isomorphism theorem|fourth isomorphism theorem]], since $(\varepsilon)$ is the only prime ideal of $\mathbb{F}[\varepsilon]$ containing $(\varepsilon^{2})$).

It will be useful later for understanding tangents, and right now as a source of counterexamples.

##### _example:_ functions are not determined by their values

$0, \varepsilon \in \mathbb{F}[\varepsilon] / (\varepsilon^{2})$ both take value $0$ at the only point $(\varepsilon) \in \operatorname{Spec} \mathbb{F}[\varepsilon] / (\varepsilon^{2})$, yet they are not the same.

---

To understand how they might help understand tangents, we take derivatives using the dual numbers.

##### _proposition:_ taking derivatives in the dual numbers

Suppose $f(x) \in \mathbb{F}[x]$. Then consider its image $f(x, \varepsilon) = f(x) \in \mathbb{F}[x, \varepsilon] / (\varepsilon^{2})$. Then $f(x + \varepsilon) = f(x) + \varepsilon f'(x)$.

###### _proof:_

Suppose $f(x) = a_{0} + a_{1} x + \dots + a_{n} x^n$. Then 
$$
\begin{align}
f(x + \varepsilon) & = a_{0} + a_{1}(x + \varepsilon) + \dots + a_{n} (x + \varepsilon)^n \\
 & = (a_{0} + a_{1} x + \dots + a_{n}x ^n)+ \varepsilon(a_{1} + 2 a_{2} x + \dots + n a_{n} x^{n - 1}) + \varepsilon^{2} g(x) \\
 & = f(x) + \varepsilon f'(x).
\end{align}
$$

---

### A shred of a smooth curve

All the primes in $\mathbb{F}[x]_{(x)}$ [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_proposition _ primes of the localisation are primes that don't meet $S$|are primes contained in]] $(x)$. All proper ideals contained in $(x)$ are $(f(x))$ such that $f(x) = x g(x)$ — that is non-irreducible polynomials. A non-irreducible polynomial is prime if and only if it is $0$. Thus, $\operatorname{Spec} \mathbb{F}[x]_{(x)}$ consists of two points — $(0)$ and $(x)$. We can think of this as a "shred of a smooth curve" — $(x)$ is the point on $\mathbb{A}^1_{\mathbb{F}}$ at which we are zooming in, and $(0)$ is the generic point of the curve.

This is one of the smallest examples of a "weird" topological space. It has $\{ (x) \}$ closed, but not $\{ (0) \}$ (since $(0)$ is contained in $(x)$). This two-point space is called the Sierpinski space.

Generalising, $\mathbb{F}[x, y]_{(x, y)}$ contains shreds of how all the curves in $\mathbb{A}^{2}_{\mathbb{F}}$ (and the plane itself) look "near the origin". Generalising in a different direction, the picture of $\mathbb{F}[x]_{(x)}$ as a shred of a smooth curve is how all discrete valuation rings should be thought of.

### Disjoint unions of affine schemes

We can describe finite disjoint unions of affine schemes as products of rings.

##### _proposition:_ products of rings are disjoint unions of affine schemes

If $A \cong A_{1} \times A_{2} \times \cdots A_{n}$, then there is an isomorphism of schemes
$$
\coprod_{i = 1}^n \operatorname{Spec} A_{i} \to \operatorname{Spec} A.
$$

###### _proof:_

It suffices to show that $\operatorname{Spec} A_{1} \times A_{2}$ is homeomorphic to $\operatorname{Spec} A_{1} \amalg \operatorname{Spec} A_{2}$. Note that the primes $\mathfrak{p} \in \operatorname{Spec} A$ are all either $\mathfrak{q}_{1} \times A_{2}$ or $A_{1} \times \mathfrak{q}_{2}$. Else the quotient is a product of non-zero rings which always contains non-zero zero divisors.

This coincides with the scheme morphisms dual to $A_{1} \times A_{2} \to A_{i}$ which have $A_{i} \times \mathfrak{q}_{j} \mapsto \mathfrak{q}_{j}$. Thus, each $\operatorname{Spec} A_{i} \to \operatorname{Spec} A_{1} \times A_{2}$ is continuous. By [[Topology --- math-147/notes/Continuous functions#_lemma _ the gluing lemma|gluing]], we get that $\operatorname{Spec} A_{1} \amalg \operatorname{Spec} A_{2} \to \operatorname{Spec} A_{1} \times A_{2}$ is continuous. By our characterisation of the primes of $A_{1} \times A_{2}$, we already have that it is a bijection. Thus, [[Topology --- math-147/notes/Homeomorphisms#_proposition _ homeomorphisms, closed bijections, and open bijections|it suffices]] to show that it is [[Topology --- math-147/notes/Homeomorphisms#_definition _ open map, closed map|closed]].

It suffices to show that each $V(\mathfrak{i}) \subseteq \operatorname{Spec} A_{i}$ has closed image. All primes containing $\mathfrak{i}$ get sent to primes containing $\mathfrak{i} \times A_{j}$, and all primes containing $\mathfrak{i} \times A_{j}$ correspond to primes containing $\mathfrak{i}$. Thus, $V(\mathfrak{i})$ has closed image $V(\mathfrak{i} \times A_{j})$.

Notice that on restriction to each $U_{i} = D(0, \dots, 1, \dots, 0) = \operatorname{Spec} A_{i}$, we have that $\mathscr{O}_{\operatorname{Spec} A  \mid \operatorname{Spec} A_{i}} \cong \mathscr{O}_{\operatorname{Spec} A_{i}}$. This is because $A_{(0, \dots, 1, \dots, 0)} = A_{i}$ since $(0, \dots, 1, \dots, 0)$ kills everything not in $A_{i}$. Thus, this is an isomorphism of ringed spaces, and thus, an isomorphism of schemes.

---

Notice however, that this doesn't hold for infinite disjoint unions.

##### _example:_ infinite disjoint unions are not affine — our first non-affine scheme

An infinite disjoint union of (non-empty) affine schemes is not affine. This follows since it is not [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#Quasicompactness|quasicompact]] (consider the cover of all $\operatorname{Spec} A_{i}$), but [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_corollary _ every affine scheme is quasicompact|all affine schemes are quasicompact]].

---

The correspondence between products and disconnected topological spaces allows us to see that the Chinese remainder theorem is a geometric fact.

##### _example:_ the Chinese remainder theorem on $\operatorname{Spec} \mathbb{Z} / (60)$

$\operatorname{Spec} \mathbb{Z} / (60)$ consists of three points — $(2), (3), (5)$. It has a nilpotent $2$, squaring to $0$ at $(2)$. This makes the functions on $\mathbb{Z} / (60)$ just a choice of functions on each of $\mathbb{Z} / (4)$, $\mathbb{Z} / (3)$ and $\mathbb{Z} / (5)$. Equivalently, $\mathbb{Z} / (60) \cong \mathbb{Z} / (2^{2}) \times \mathbb{Z} / (3) \times \mathbb{Z} / (5)$.

---

### Disjoint unions of schemes

Disjoint unions of schemes are exactly what you think they are.

##### _definition:_ disjoint union of schemes

The **disjoint union of schemes** $\{ X_{i} \}_{i \in \mathscr{I}}$ is the set $\coprod_{i \in \mathscr{I}} X_{i}$ with the disjoint union topology (generated by the base of open subsets of each scheme $X_{i}$) with structure sheaf given on the same base by $\mathscr{O}_{X}(U) = \mathscr{O}_{X_{i}}(U)$ for $U \subseteq X_{i}$.

---

Recall that finite disjoint unions of affine schemes [[Algebraic geometry --- rising-sea/notes/Examples of schemes#_proposition _ products of rings are disjoint unions of affine schemes|are actually affine]]. This doesn't hold for infinite disjoint unions, and thus, gives our first example of a non-affine scheme!

With the understanding of [[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_definition _ morphism of schemes|morphisms of schemes]] we can justify the use of the symbol $\coprod$ and prove that these really are coproducts of schemes.

##### _proposition:_ the disjoint union is the coproduct of schemes

###### _proof:_

Let $X_{i}$ be a collection of schemes indexed by a set $I$ (we don't need a category for coproducts). Then by construction of the disjoint union $P = \coprod_{i \in I} X_{i}$, there is a topological open embedding $X_{i} \to P$ for each $i$ and $\mathscr{O}_{P \mid X_{i}} = \mathscr{O}_{X_{i}}$ which makes this an [[Algebraic geometry --- rising-sea/notes/Morphisms of ringed spaces#_definition _ open embeddings|open embedding]] of schemes. We name these $pr_{i} : X_{i} \to P$.

Suppose $P'$ has morphisms $pr_{i}' : X_{i} \to P'$ from each $X_{i}$. Then consider $\amalg : P \to P'$ defined by $\amalg_{\mid X_{i}} = pr_{i}'$. This is well-defined since the $X_{i}$ are disjoint. Thus the morphisms glue to one $\amalg : P \to P'$ which clearly has $\amalg \circ pr_{i} = pr_{i}'$.

---

### The punctured plane

The **punctured plane** (over $\mathbb{F}$) is the [[Algebraic geometry --- rising-sea/notes/Schemes#_proposition, definition _ open subschemes, affine open subscheme|open subscheme]] $U, \mathscr{O}_{\mathbb{A}_{\mathbb{F}}^{2} \mid U}$ of $\mathbb{A}^{2}_{\mathbb{F}}$ given by $U = \mathbb{A}_{\mathbb{F}}^{2} \setminus \{ (x, y) \}$ or "$\mathbb{F}^{2} \setminus \{ (0, 0) \}$". To this end, let $A = \mathbb{F}[x, y]$ and thus, $\operatorname{Spec} A = \mathbb{A}_{\mathbb{F}}^{2}$. 

We claim that the punctured plain is in fact not affine. We first compute its global sections to check what scheme it would be if it were affine.

##### _example:_ the global sections over the punctured plane

It turns out we cannot write $U$ as a distinguished open, but we can write it as the union of distinguished opens — $U = D(x) \cup D(y)$. The functions on $U$ are functions on $D(x)$ and $D(y)$ that agree on the intersection $D(xy)$. These are functions in $A_{x}$ and $A_{y}$ that agree on $A_{xy}$, or in other words, the intersection $A_{x} \cap A_{y} \subseteq Q(A)$. But the intersection of $\{ 1, x, x^{2}, \dots \}$ and $\{ 1, y, y^{2}, \dots \}$ is just $1$, so the intersection is $A_{1} = A$. Thus, the global sections on $U$ are
$$
\mathscr{O}_{\mathbb{A}^{2}_{\mathbb{F}}}(U) = \mathbb{F}[x, y].
$$

---

Surprisingly, we found that the functions on $U$ are just $\mathbb{F}[x, y]$. In some sense this is because the point we removed is of codimension too great, and thus, there are no rational functions that only have a pole at that one point. This is a special case of the algebraic analogue of Hartog's lemma (originally from complex geometry). It says that functions extend over points of codimension at least $2$, as long as they are (what we will call) normal.

##### _example:_ the punctured plane is not affine

Since the global sections of $U$ are just $\mathbb{F}[x, y]$, if $U$ were affine, we would have $U \cong \mathbb{A}_{\mathbb{F}}^{2}$. While in the usual topology on $\mathbb{C}^{2}$ we could make some (higher) fundamental group argument about the difference between $\mathbb{C}^{2}$ and $\mathbb{C}^{2} \setminus \{ (0, 0) \}$. This would tell us that they are not homeomorphic, and thus, not isomorphic as schemes. We can't make such an argument in the Zariski topology easily (possibly because $U$ is homeomorphic to $X$). However, the structure sheaf isomorphism allows us to recover more data.

Since we have an isomorphism of structure sheaves, we have an isomorphism of stalks, and thus, if we have points where all functions in a certain ideal $\mathfrak{i} \subseteq A$ vanish on $\operatorname{\mathbb{A}}_{\mathbb{F}}^{2}$ we must have points where all functions $\mathfrak{i} \subseteq A$ vanish on $U$. But $(x, y) \subseteq A$ vanishes at $V(x, y) = \{ (x, y) \}$ on $\mathbb{A}_{\mathbb{F}}^{2}$ and there is no point where all functions in $(x, y)$ vanish on $U$. Thus, $U \cong \operatorname{Spec} A$, and thus, is not affine.

---

### The affine line and plane with doubled origin

Let $X = \operatorname{Spec} \mathbb{F}[x]$ and $Y = \operatorname{Spec} \mathbb{F}[y]$ and let $U = D(x) \subseteq X$ and $V = D(y) \subseteq Y$. Writing $U = \operatorname{Spec} \mathbb{F}[x]_{x}$ and $V = \operatorname{Spec} \mathbb{F}[y]_{y}$, let $U \cong V$ be the isomorphism of schemes given by the obvious isomorphism of rings $x \mapsto y$. Then [[Algebraic geometry --- rising-sea/notes/Schemes#_proposition _ gluing schemes|glue the schemes]] $X$ and $Y$ along this isomorphism. This gives the **affine line with doubled origin**.

Note that there is something not-separated-enough about this — it's still [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#_definition _ quasiseparated|quasiseparated]] but we will see that it is not separated.

##### _proposition:_ the affine line with doubled origin is not affine

Let $Z$ be the affine line with doubled origin. $Z \not\cong \operatorname{Spec} A$ for each $A$.

###### _proof:_

The global sections of $\mathscr{O}_{Z}$ are obtained by gluing functions on $X$ (elements of $\mathbb{F}[x]$) and functions on $Y$ (elements of $\mathbb{F}[y]$) that agree on the intersection $X \cap Y$ (that agree away from the origin). But if polynomials agree everywhere except the origin, they agree at the origin. Thus, $\mathscr{O}_{Z}(Z) = \mathbb{F}[z]$. 

If $Z$ were affine, we would have to have $Z \cong \operatorname{Spec} \mathbb{F}[z]$. But $z \in \mathscr{O}_{Z}(Z)$ vanishes at two points in $Z$ (both origins) and $z \in \mathbb{F}[z]$ only vanishes at one point. Thus, $Z$ cannot be $\operatorname{Spec} \mathbb{Z}$.

---

Note that we can define the **affine plane with doubled origin** by gluing two copies of $\mathbb{A}_{\mathbb{F}}^{2}$ along the punctured plane. Note that the intersection of the two affine copies of the plane is then the punctured plane, which is not affine.

### The projective line and projective space

Again, let $X = \operatorname{Spec} \mathbb{F}[x]$ and $Y = \operatorname{Spec} \mathbb{F}[y]$ and let $U = D(x) \subseteq X$ and $V = D(y) \subseteq Y$. But now, writing $U = \operatorname{Spec} \mathbb{F}[x]_{x}$ and $V = \operatorname{Spec} \mathbb{F}[y]_{y}$, let $U \cong V$ be the isomorphism of schemes given by the isomorphism $x \mapsto 1/y$. Gluing $X$ and $Y$ along this isomorphism gives $\mathbb{P}_{\mathbb{F}}^1$ — the affine line over $\mathbb{F}$. The same construction with an arbitrary ring $A$ instead of $\mathbb{F}$ gives $\mathbb{P}_{A}^1$.

If $\mathbb{F}$ is algebraically closed, we can think of this as gluing together non-zero traditional points $(x - a)$ and $(y - 1 / a)$ and gluing both the generic points together. This allows us to introduce homogeneous coordinates. We can write the closed points of $\mathbb{P}^1_{\mathbb{F}}$ as tuples $(a : b)$ modulo scaling by $\mathbb{F}^\times$, corresponding to $(x - a / b)$ and $(y - b / a)$ when both $a$ and $b$ are non-zero, and only the sensible one when one of them is $0$.

Usually when we've shown that schemes are not affine we've had to make some argument that the vanishing of functions is different on each, even though the topologies are possibly the same. This time, our argument won't even need the topology — it works set-theoretically.

##### _proposition:_ the projective line is not affine

$\mathbb{P}^1_{\mathbb{F}}$ is not affine.

###### _proof:_

The global sections of $\mathscr{O}_{\mathbb{P}_{\mathbb{F}}^1}$ are functions in $f(x) \in \mathbb{F}[x]$ and $g(y) \in \mathbb{F}[y]$ such that $f(x) = g(1 / x) = g(y)$ away from the origin. But it's easy to check in $\mathbb{F}[x]_{x}$ that any such polynomials are just constants — they can only have $0$th powers of $x$. Thus $\mathscr{O}_{\mathbb{P}_{\mathbb{F}}^1}(\mathbb{P}_{\mathbb{F}}^1) = \mathbb{F}$. If $\mathbb{P}_{\mathbb{F}}^1$ were affine, we would have $\mathbb{P}_{\mathbb{F}}^1 \cong \operatorname{Spec} \mathbb{F}$, and thus, just one point. But projective space isn't just one point (there are at least the two non-glued points).

---

Our computation $\mathscr{O}_{\mathbb{P}_{\mathbb{F}}^1}(\mathbb{P}_{{\mathbb{F}}}^1)$ is the algebraic analogue of the theorem that global holomorphic functions on $\mathbb{C} \mathbb{P}^1$ [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_theorem _ global holomorphic functions are constant|are constant]].

We can generalise all of this to higher dimensions.

##### _definition:_ projective $n$-space over a ring

**Projective $n$-space over $A$** is the scheme $\mathbb{P}_{\mathbb{A}}^n$ obtained by the following gluing $n + 1$ affine schemes
$$
U_{i} = \operatorname{Spec} A[x_{0 / i}, \dots, x_{n/ i}] / (x_{i / i} - 1)
$$
with $D(x_{j / i}) \subseteq U_{i}$ and $D(x_{i / j}) \subseteq U_{j}$ glued by the isomorphism
$$
\begin{align}
A[x_{0 / i}, \dots, x_{n / i}]_{x_{j / i}} / (x_{i / i} - 1) & \to A[x_{0 / j}, \dots, x_{n / j}]_{x_{i / j}} / (x_{j / j} - 1) \\
x_{k / i} & \mapsto x_{k / j} / x_{i / j}.
\end{align}
$$
Note that this implies $x_{j / i} \mapsto 1 / x_{i / j}$.

---

We do need to verify that this gluing condition is actually valid — that it satisfies the cocycle condition. This follows just by checking where the generators go on the affine triple intersection.
$$
\begin{gather}
A[x_{0 / i}, \dots, x_{n / i}]_{x_{j / i}, x_{k / i}} & \to A[x_{0 / j}, \dots, x_{n / j}]_{x_{i / j}, x_{k / j}} & \to A[x_{0 / k}, \dots, x_{n / k}]_{x_{i / k}, x_{j / k}} \\
x_{\ell / i} \mapsto & x_{\ell / j} / x_{i / j} \mapsto & \frac{x_{\ell / k} / x_{j / k}}{x_{i / k} / x_{j / k}} = x_{\ell / k} / x_{i / k}.
\end{gather}
$$

On $\mathbb{P}_{\mathbb{F}}^n$ too, the only global functions are constants.

##### _proposition:_ global functions on projective space

$\mathscr{O}_{\mathbb{P}_{\mathbb{F}}^n}(\mathbb{P}_{\mathbb{F}}^n) \cong \mathbb{F}$.

###### _proof:_

Clearly all constants in $\mathbb{F}$ are global functions — we can glue a constant function from pieces on each $U_{i}$ in the obvious way. Thus, there is an injection $\mathbb{F} \to \mathscr{O}_{\mathbb{P}_{\mathbb{F}}^n}(\mathbb{P}_{\mathbb{F}}^n)$. It is injective because we can check that different elements of $\mathbb{F}$ restrict to different functions on the affine opens.

Any function on all of $\mathbb{P}_{\mathbb{F}}^n$ must restrict to a function on $U_{0} \cup U_{1}$ which in turn are just functions on $U_{0}$ and $U_{1}$ that agree on the intersection. That is, they restrict to functions $f(x_{1 / 0}, \dots, x_{n / 0})$ on $D(x_{0 / 1}) \subseteq U_{0}$ and $g$ on $D(x_{1 / 0}) \subseteq U_{1}$ such that 
$$
f(x_{1 / 0}, x_{2 / 0} \dots, x_{n / 0}) = g\left( \frac{1}{x_{1 / 0}}, \frac{x_{2/0}}{x_{1 / 0}}, \dots, \frac{x_{n / 0}}{x_{1 / 0}} \right) = g(x_{0 / 1}, x_{2 / 1}, \dots, x_{n / 1})
$$
Again, these are exactly the constant polynomials in $\mathbb{F}[x_{1 / 0}, \dots, x_{n / 0}]_{x_{1 / 0}}$ — $f$ has no $1 / x_{1 / 0}$ terms, but if $g$ is non-constant, then it only has $1 / x_{1 / 0}$ terms. Thus, $\mathbb{F} \to \mathscr{O}_{\mathbb{P}_{\mathbb{F}}^n}(\mathbb{P}_{\mathbb{F}}^n)$ is a surjection, and an isomorphism.

---

Finally, if $\mathbb{F}$ is algebraically closed, we can once again use "homogeneous coordinates".

##### _proposition:_ homogeneous coordinates for projective space

Suppose $\mathbb{F}$ is algebraically closed. Then closed points of $\mathbb{P}_{\mathbb{F}}^n$ are in bijection with homogeneous coordinates. That is, closed points are in bijection with the set $\{ (a_{0} : \dots : a_{n}) \in \mathbb{F}^{n + 1} \ (0 : \dots : 0) \} / \mathbb{F}^\times$ of not-all-zero $(n + 1)$-tuples of $\mathbb{F}$, up to scaling by units of $\mathbb{F}$.

###### _proof sketch:_

The closed points of $\mathbb{P}_{\mathbb{F}}^n$ are exactly the closed points of its affine opens. To $(x_{1 / 0} - a_{1 / 0}, \dots, x_{n / 0} - a_{n / 0}) \in U_{0}$, we associate the homogeneous coordinate $(1 : a_{1} : \dots : a_{n})$ and similarly, on each $U_{i}$. This is clearly surjective. 

This is also injective, even after quotienting out by the action of $\mathbb{F}^\times$. Suppose $(1 : a_{1} : \dots : a_{n}) \sim (b_{0} : 1 : b_{2} : \dots : b_{n})$. That is, there is some $\lambda$ such that $\lambda b_{0} = 1$, $\lambda = a_{1}$, and $\lambda b_{i} = a_{i}$. Thus, $b_{i} = a_{i} / a_{1}$ for $i \geq 2$. We want to show that $(x_{1 / 0} - a_{1}, \dots, x_{n} - a_{n / 0}) \in U_{0}$ and $(x_{0 / 1} - b_{0 / 1}, x_{2 / 1} - b_{2 / 1} \dots, x_{n / 1} - b_{n / 1}) \in U_{1}$ are identified as the same point. Localising, we get exactly this by our theorem on [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_example _ coordinates for an affine scheme morphism|coordinates for morphisms of affine schemes]], and the definition of the isomorphism between the distinguished opens.

---

While this all gives a correct definition of projective space, it is not one that is "choice free". Projective space has many more affine opens, equally natural, that just aren't represented in this definition. A more compelling but still "wrong" definition comes from the $\operatorname{Proj}$ [[Algebraic geometry --- rising-sea/notes/Projective schemes|construction on graded rings]]. This will allow us to define not just $\mathbb{P}^n$, but also the "projective schemes" cut out in it.

### A cone over a smooth quadric surface

Let $A = \mathbb{F}[w, x, y, z] / (wz - xy)$. Then $X = \operatorname{Spec} A$ is a hypersurface in $\mathbb{A}^4_{\mathbb{F}}$ and a cone over a smooth quadric surface in $\mathbb{P}^3_{\mathbb{F}}$. It will be a source of many counterexamples for us.

##### _example:_ a function on an affine scheme with no single expression

Since the functions $z / y$ on $D(y)$ and $x / w$ on $D(w)$ agree on the intersection $D(y) \cap D(w)$, they glue together to give a section on $D(y) \cup D(w)$. However, there is no single expression $h(w, x, y, z) = f(w, x, y, z) / g(w, x, y, z)$ for the function on all of $X$.

If there were, then $g$ would have to vanish exactly on $V(y) \cap V(w)$ since $h$ is not defined exactly on the complement of $D(y) \cup D(w)$. But it turns out that $V(y) \cap V(w)$ is a line that is not cut out (even set-theoretically) by any single equation. Thus, $g$ cannot vanish exactly on $V(y) \cap V(w)$.

---

##### _example:_ an integrally closed ring that is not a UFD

$A$ is integrally closed [[Algebraic geometry --- rising-sea/notes/Normal and factorial schemes#_examples _ cones are normal|because]] $wz - xy$ is a quadratic form. However, unique factorisation clearly fails in $A$ — $wz = xy$. We do need to show that $w, z, x, y$ are irreducible. This follows because if $w = w_{0} w_{1}$ then the $w_{i}$ must be homogeneous for their product to be homogeneous. By additivity of degree, we must have $w_{0}$ of degree $0$ and $w_{1}$ of degree $1$. But then any non-zero $w_{0}$ of degree $0$ is a unit.

---