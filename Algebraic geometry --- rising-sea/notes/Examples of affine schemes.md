---
tags:
- rising-sea
- alg-geo
- comm-alg
- rising-sea/3
---

Let $A$ be a ring and $\mathbb{F}$ a field.

Here we collect examples of [[Algebraic geometry --- rising-sea/notes/Affine schemes|affine schemes]].

### The complex affine line

The complex affine line is a special case of affine $n$-space over any ring. It is also a special case that behaves exactly like the general case of the affine line over any algebraically closed field $\overline{\mathbb{F}}$. Replacing $\mathbb{C}$ with $\overline{\mathbb{F}}$ will usually be fine in this example.

##### _definition:_ the complex affine line, $\mathbb{A}_{\mathbb{C}}^1$

The complex affine line is $\mathbb{A}^1_{\mathbb{C}} = \operatorname{Spec} \mathbb{C}[x]$.

---

##### _proposition:_ the points of the complex affine line

The points of the $\mathbb{A}_{\mathbb{C}}^1$ are exactly $(0)$ and $(x - a)$ for $a \in \mathbb{C}$.

###### _proof:_

A point of $\mathbb{A}^1_{\mathbb{C}}$ is a prime ideal of $\mathbb{C}[x]$. 

Any $\mathbb{F}[x]$ is a [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ Euclidean domain|Euclidean domain]] with polynomial long division. Thus, $\mathbb{C}[x]$ is a [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ principal ideal domain|principal ideal domain]]. Thus, any $\mathfrak{p} \subseteq \mathbb{C}[x]$ is $(p(x))$ for some $p(x) \in \mathbb{C}[x]$. 

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

Affine $n$-space over $A$ is the affine scheme $\operatorname{Spec} A[x_{1}, \dots, x_{n}]$.

---

We usually choose $A$ a field. The affine line over a field $\mathbb{F}$ always looks a little like $\mathbb{A}^1_{\mathbb{F}}$ or $\operatorname{Spec} \mathbb{Z}$ — there is always at least a line with infinitely many primes. 

##### _proposition:_ affine space always has infinitely many points

The set of points of $\mathbb{A}_{\mathbb{F}}^1$ is infinite.

###### _proof:_

Suppose $\mathfrak{p}_{1} = (p_{1}), \dots, \mathfrak{p}_{n} = (p_{n})$ is a finite list of primes in $\mathbb{F}[x]$, each generated by a distinct irreducible polynomial (since $\mathbb{F}[x]$ is a [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ principal ideal domain|principal ideal domain]]). Consider $f(x) = p_{1}(x) \cdots p_{n}(x) + 1$. Since it is not divisible by any of the $p_{i}$, it must be divisible by some different irreducible $p$. That is, write $f(x) = p(x) q(x)$

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

Since $f$ and $g$ are coprime in $\mathbb{C}[x, y]$ they are coprime in $\mathbb{C}(x)[y]$. Since $\mathbb{C}(x)[y]$ is a [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ Euclidean domain|Euclidean domain]], they have a least common factor $1$. That is,
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

The points of $\mathbb{A}^1_{\mathbb{R}}$ are $(0)$ and all irreducible polynomials. Since $\mathbb{R}[x]$ is [[Abstract algebra --- math-171/notes/Factorisation in special rings|Euclidean]], these are all maximal. The "normal" maximal ideals, corresponding to $a \in \mathbb{R}^1$ are $(x - a) \subseteq \mathbb{R}[x]$. The other maximal ideals are $(x^{2} + bx + c)$ with $b^{2} < c$. These correspond to adjoining roots $\lambda, \overline{\lambda} \in \mathbb{C} \setminus \mathbb{R}$ to $\mathbb{R}$. 

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

### The dual numbers

The dual numbers are the ring $\mathbb{F}[\varepsilon] / (\varepsilon^{2})$ (think of this as some adjoining some error $\varepsilon$ that we want to keep track of to the first order, but can ignore in higher orders). It has just one point $(\varepsilon)$ (by the [[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the fourth isomorphism theorem|fourth isomorphism theorem]], since $(\varepsilon)$ is the only prime ideal of $\mathbb{F}[\varepsilon]$ containing $(\varepsilon^{2})$).

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

We can describe finite disjoint unions of affine schemes as 

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

##### _non-example:_ our "first" non-affine scheme

An infinite disjoint union of (non-empty) affine schemes is not affine. This follows since it is not [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#Quasicompactness|quasicompact]] (consider the cover of all $\operatorname{Spec} A_{i}$), but [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_corollary _ every affine scheme is quasicompact|all affine schemes are quasicompact]].

---