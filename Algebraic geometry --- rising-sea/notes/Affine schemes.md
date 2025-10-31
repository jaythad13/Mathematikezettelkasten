---
tags:
- alg-geo
- comm-alg
- rising-sea/3
---

Let $A$ be a ring.

Affine schemes are the basic "gluing blocks" of schemes in general, analogous to the role $\mathbb{R}^n$ or the open ball in $\mathbb{R}^n$ plays for manifolds. Just as $\mathbb{R}^n$ is a [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, functions, global functions|ringed space]], so is each affine scheme. However, in contrast, [[Algebraic geometry --- rising-sea/notes/Examples of affine schemes|there are lots of very different affine schemes]] (one for each ring). Each affine scheme is then determined by the combination of its set (of points) its space ([[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topology]]), and its [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, functions, global functions|structure sheaf.]]

### The set (of points)

Affine schemes are all $\operatorname{Spec} A$ for some ring $A$.

##### _definition:_ the points of the set of an affine scheme

Let $A$ be a ring. Then the **set of points of $\operatorname{Spec} A$** is the set of [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|prime ideals]] of $A$.

---

To avoid confusion between between $\mathfrak{p} \in \operatorname{Spec} A$ as a point and $\mathfrak{p} \subseteq A$ as an ideal, we may sometimes use the notation $[\mathfrak{p}]$ to indicate that we are talking about the point.

The best example of an affine scheme is the affine line over $\mathbb{C}$ — $\mathbb{A}^1_{\mathbb{C}} = \operatorname{Spec} \mathbb{C}[x]$.

![[Algebraic geometry --- rising-sea/notes/Examples of affine schemes#_proposition _ the points of the complex affine line]]

In general, we can define $\mathbb{A}^1_{A} = \operatorname{Spec} A[x_{1}, \dots, x_{n}]$ over any ring $A$ (typically $A$ is a field). When $A$ is a non-algebraically closed field, this can behave very differently. For example

### The functions (or more alliteratively, the sections)

Though we can't define the structure sheaf yet, we can see what the [[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ ringed spaces, structure sheaf, functions, global functions|global functions]] of it are. Essentially, $\mathscr{O}_{\operatorname{Spec} A}(\operatorname{Spec} A) = A$.

##### _definition:_ (global) functions on an affine scheme, value, vanishing at a point

The **(global) functions on $\operatorname{Spec} A$** are the elements $a \in A$.

The **value** of a global function $a \in A$ at a point $\mathfrak{p} \in \operatorname{Spec} A$ is $a \pmod {\mathfrak{p}}$ — the image of $a$ under $A \to A / \mathfrak{p}$.

$a$ **vanishes** at $\mathfrak{p}$ if it has value $0$ at $\mathfrak{p}$.

---

Note that $a$ vanishes at $\mathfrak{p}$ if and only if $a \in \mathfrak{p}$.

In some ways and sometimes, functions behave like we might expect them to.

![[Algebraic geometry --- rising-sea/notes/Examples of affine schemes#_proposition _ values of functions on $ mathbb{A} 1_{ mathbb{C}}$ are values of polynomials in $ mathbb{C}$|Examples of affine schemes]]

However, they don't always. In particular, functions can take values in different rings,

![[Algebraic geometry --- rising-sea/notes/Examples of affine schemes#_example _ values of a function on $ operatorname{Spec} mathbb{Z}$ in different fields]]

and are not always determined by their values at points.

![[Algebraic geometry --- rising-sea/notes/Examples of affine schemes#_example _ functions are not determined by their values|Examples of affine schemes]]

While this behaviour may seem somewhat pathological, we can characterise it completely, so it becomes a feature, not a bug. We claim that the functions that vanish at every point are exactly those that power to $0$. This is just saying that functions contained in every prime ideal are exactly the [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_definition _ nilpotents|nilpotents]].

![[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_proposition _ the nilradical is an ideal and the intersection of primes|Nilpotents and the nilradical]]

Thus, any two functions that take the same value at every point differ by a nilpotent. Passing to the quotient $A / \mathfrak{N}$ means that functions are determined by their value on $\operatorname{Spec} A / \mathfrak{N}$. This leads to the following definition.

##### _definition:_ reduced (ring)

(A ring) $A$ is **reduced** if it has no non-zero nilpotents. Equivalently its nilardical is $\mathfrak{N} = (0)$.

---

### The space (the Zariski topology)

One important notion for geometry is that the locus where a function vanishes should be closed. For the topology of affine schemes we will require this and nothing else.

##### _definition:_ vanishing set

The **vanishing set** of a subset $S \subseteq A$ is the set of points $\mathfrak{p} \in \operatorname{Spec} A$ where all functions in $S$ vanish, denoted $V(S)$. That is,
$$
V(S) = \{ \mathfrak{p} \in \operatorname{Spec} A \mid S \subseteq \mathfrak{p} \}.
$$

By abuse of notation we occasionally write $V(f_{1}, \dots, f_{n})$ for $V(\{ f_{1}, \dots, f_{n} \})$.

---

We should think of $V(f_{1}, \dots, f_{n})$ as solving for the locus $f_{1} = \cdots = f_{n} = 0$.

![[Algebraic geometry --- rising-sea/notes/Examples of affine schemes#_example _ $V(xy, yz) subseteq mathbb{A} 3_{ mathbb{C}}$|Examples of affine schemes]]

##### _definition, proposition:_ the Zariski topology (is a topology)

The **Zariski topology** on the affine scheme $\operatorname{Spec} A$ is the topology.

Specifically,
1) $V(0) = \operatorname{Spec} A$,
2) $V(1) = \text{Ø}$,
3) $\bigcap_{i \in \mathscr{I}} V(\mathfrak{i}_{i}) = V\left( \sum_{i \in \mathscr{I}} \mathfrak{i}_{i} \right)$,
4) $V(\mathfrak{i}) \cup V(\mathfrak{j}) = V(\mathfrak{i} \mathfrak{j}) = V(\mathfrak{i} \cap \mathfrak{j})$.

###### _proof:_
has been done many times in different homeworks. See [[Commutative algebra --- math-189AA/attachments/homework/hw 1/hw 1.pdf#page=9|this one]].

---

In the proof that the Zariski topology is a topology we crucially use the fact that the vanishing set only depends on the ideal generated by $S$. In the first part of the proof of this lemma we will use the fact that $V$ is inclusion-reversing. This is useful enough to deserve a proper statement.

##### _proposition:_ $V$ is inclusion-reversing

For any subsets $S_{1} \subseteq S_{2}$, we have $V(S_{2}) \subseteq V(S_{1})$.

###### _proof:_
is exactly same as the first argument of the proof below.

---

##### _proposition:_

If $S \subseteq A$ and $(S)$ is the ideal generated by $S$, then $V(S) = V((S))$.

###### _proof:_

Since $S \subseteq (S)$, at every point $\mathfrak{p} \in V((S))$ all the functions in $S$ vanish. That is, $V((S)) \subseteq V(S)$.

Suppose $\mathfrak{p} \in V(S)$. That is, $S \subseteq \mathfrak{p}$. But since $\mathfrak{p}$ is an ideal, we must also have $(S) \subseteq \mathfrak{p}$, and thus, $\mathfrak{p} \in V((S))$.

---


Note however, that we can have $V(S_{1}) = V(S_{2})$ without $S_{1} = S_{2}$. For example, $V(x^{2}) = V(x)$ in $\mathbb{A}_{\mathbb{F}}^1$. This is because vanishing set function doesn't preserve full information of ideals. Since it cares about containment in prime ideals, it only preserves the information in the radical of the ideal. Specifically,

##### _proposition:_ vanishing sets uniquely identify only radical ideals

Suppose $\mathfrak{i}, \mathfrak{j} \subseteq A$ are ideals. Then $V(\mathfrak{i}) = V(\mathfrak{j})$ if and only if $\sqrt{ \mathfrak{i} } = \sqrt{ \mathfrak{j} }$.

###### _proof:_

First we show that $V(\mathfrak{i}) = V(\sqrt{ \mathfrak{i} })$. It follows that if $\sqrt{ \mathfrak{i} } = \sqrt{ \mathfrak{j} }$, then $V(\sqrt{ \mathfrak{i} }) = V(\sqrt{ \mathfrak{j} })$. 

Suppose $\mathfrak{p} \in V(\mathfrak{i})$. Then $\mathfrak{i} \subseteq \mathfrak{p}$. Since $\sqrt{ \mathfrak{i} }$ [[Algebraic geometry --- rising-sea/notes/Radicals of ideals#_proposition _ the radical is the intersection of all primes containing the ideal|is the intersection of all primes containing]] $\mathfrak{i}$, we have $\mathfrak{\sqrt{ i }} \subseteq \mathfrak{p}$. That is, $\mathfrak{p} \in V(\sqrt{ \mathfrak{i} })$. Conversely, suppose $\mathfrak{p} \in V(\sqrt{ \mathfrak{i} })$. Then $\mathfrak{i} \subseteq \sqrt{ \mathfrak{i} } \subseteq \mathfrak{p}$, so $\mathfrak{p} \in V(\mathfrak{i})$.

Suppose $V(\mathfrak{i}) = V(\mathfrak{j})$. Then the set of primes containing $\mathfrak{i}$ is the same as the set of primes containing $\mathfrak{j}$. The intersections of all elements in these sets must be the same. That is, $\sqrt{ \mathfrak{i} } = \sqrt{ \mathfrak{j} }$.

---

This has the useful consequence that since $(\mathfrak{i} \cap \mathfrak{j})^{2} \subseteq \mathfrak{i} \mathfrak{j} \subseteq \mathfrak{i} \cap \mathfrak{j}$, we must have $V(\mathfrak{i} \mathfrak{j}) = V(\mathfrak{i} \cap \mathfrak{j})$. 

A similar fact characterises the functions that vanish on a vanishing set.

##### _proposition:_ functions vanishing on a vanishing set

If $f$ vanishes at all points of $V(\mathfrak{i})$, then $f$ is in $\sqrt{ i }$.

###### _proof sketch:_

If $f$ vanishes at all $\mathfrak{p} \in V(\mathfrak{i})$, it is contained in every prime containing $\mathfrak{i}$. It must then be contained in their intersection which is just $\sqrt{ \mathfrak{i} }$.

---

With the identification $\operatorname{Spec} A / \mathfrak{i} \cong V(\mathfrak{i})$ (as a closed subscheme), we can interpret this as follows. $\overline{f} \in A / \mathfrak{i}$ is a function that vanishes everywhere on $\operatorname{Spec} A / \mathfrak{i}$. Thus, it is nilpotent in $A / \mathfrak{i}$, or equivalently, $f \in \sqrt{ \mathfrak{i} }$.

### Topological properties of points

Let $X$ be a topological space

Since we have scheme like points of "different dimensions", these have interesting topological properties.

The most obvious are the "closed" or "classical" points which we've been talking about

##### _definition:_ closed point

A point $p \in X$ is **closed** if $\{ p \} \subseteq X$ is closed in the topology on $X$.

---

For affine schemes, these are exactly the maximal ideals. Thus, we finally have a formal way to show that the maximal ideals correspond to the traditional, classical points.

##### _proposition:_ closed points of affine schemes are maximal ideals

$\mathfrak{m} \in \operatorname{Spec} A$ is a closed point if and only if $\mathfrak{m}$ is a maximal ideal of $A$.

###### _proof:_

If $\mathfrak{m}$ is maximal, then the only prime ideal containing it is $\mathfrak{m}$ itself. Thus, $\{ \mathfrak{m} \} = V(\mathfrak{m})$ is closed.

Suppose $\mathfrak{m}$ is closed. Any closed set $V(\mathfrak{i})$ containing $\mathfrak{m}$ contains all primes containing $\mathfrak{m}$. Thus, there are no primes (apart from $\mathfrak{m}$) containing . Every ideal is contained in a unique maximal, and thus, prime ideal. Thus, there are also no distinct ideals containing $\mathfrak{m}$. That is, $\mathfrak{m}$ is maximal.

---

Often, it suffices just to think about the closed points. On finite $\mathbb{F}$-algebras, they are dense, and when they are [[#_definition _ reduced (ring)|reduced]] and over an algebraically closed field, they determine functions as well.

##### _proposition:_ closed points are dense on finite-type affine $\mathbb{F}$-schemes

Suppose $\mathbb{F}$ is a field and $A$ is a finitely generated $\mathbb{F}$-algebra. Then the closed points of $\operatorname{Spec} A$ are dense.

###### _proof:_

We hope to show that every open $U \subseteq \operatorname{Spec} A$ contains some maximal ideal $\mathfrak{m}$. We show that every [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_definition _ distinguished open set, doesn't vanish set|distinguished open]] contains some maximal ideal $\mathfrak{m}$.

Consider $D(f) = \operatorname{Spec} A \setminus V(f)$. The maximal ideals in $V(f)$ are exactly those containing $f$. Thus, we want to prove that there exist maximal ideals that do not contain $f$. Choose a maximal ideal $\mathfrak{m}_{f} \subseteq A_{f}$. This determines an ideal $\mathfrak{m} \subseteq A$ (a prime, and maximal among all ideals not containing $f$, but not necessarily a maximal ideal). Since [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_proposition _ localisation commutes with quotients|localisation commutes with quotients]] we have $A_{f} / \mathfrak{m}_{f} \cong (A / \mathfrak{m})_{f}$.

Thus, $(A / \mathfrak{m})_{f}$ is a finite field extension of $\mathbb{F}$. We claim $A / \mathfrak{m}$ is a finite $\mathbb{F}$-algebra and an integral domain. [[Algebraic geometry --- rising-sea/notes/Hilbert's Nullstellensatz#_proposition _ characterising finite $ mathbb{F}$-algebras|Thus]], it is a field. Then $\mathfrak{m}$ is a maximal ideal not containing $f$ and we are done.

This follows since a maximal, and thus prime ideal $\mathfrak{m}_{f} \subseteq A_{f}$ pulls back to a prime $\mathfrak{m} \subseteq A$. Thus, $A / \mathfrak{m}$ is an integral domain. Since $f$ is not a zero divisor in the integral domain $A / \mathfrak{m}$, [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_proposition _ injectivity of the localisation map|we have an injection]] $A / \mathfrak{m} \to (A / \mathfrak{m})_{f}$. Since this injection is $A$-linear, it is also $\mathbb{F}$-linear. Since $(A / \mathfrak{m})_{f} \cong A_{f} / \mathfrak{m}_{f}$ is finite-dimensional over $\mathbb{F}$, this gives us $A / \mathfrak{m}$ also finite-dimensional over $\mathbb{F}$.

---

Note that this doesn't hold for infinitely-generated $\mathbb{F}$-algebras. For example, consider [[Algebraic geometry --- rising-sea/notes/Examples of affine schemes#A shred of a smooth curve|the shred of a smooth curve]] $X = \operatorname{Spec} \mathbb{F}[x]_{(x)}$. Since $(x)$ is maximal, $X \setminus V(x)$ is open and doesn't contain the only maximal ideal $(x)$.

##### _proposition:_ functions on affine $\overline{\mathbb{F}}$-varieties are determined on closed points

Suppose $\overline{\mathbb{F}}$ is an algebraically closed field and $A$ is a reduced finitely generated $\overline{\mathbb{F}}$-algebra. Then functions on $\operatorname{Spec} A$ are determined by their values on the closed points of $\operatorname{Spec} A$.

###### _proof:_

Suppose $f, g$ are two distinct global functions on $\operatorname{Spec} A$. Thus, $f - g \neq 0$ and $D(f - g) \neq \text{Ø}$ ([[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_corollary _ the empty distinguished open|only nilpotents have empty distinguished open]]). This non-empty distinguished open contains a maximal ideal that  doesn't vanish at. That is, distinct global functions differ on some closed point.

We can give an alternate proof from an extrinsic perspective. Note that we can write $A = \overline{\mathbb{F}}[x_{1}, \dots, x_{n}] / \mathfrak{i}$ for some [[Algebraic geometry --- rising-sea/notes/Radicals of ideals#_definition _ radical of an ideal, radical ideal|radical]] ideal $\mathfrak{i}$. Applying the [[Algebraic geometry --- rising-sea/notes/Hilbert's Nullstellensatz#_theorem _ Hilbert's weak Nullstellensatz|weak Nullstellensatz]] gives us that the maximal ideals of $A$ are $\mathfrak{m} / \mathfrak{i}$ for $\mathfrak{m} = (x_{1} - a_{1}, \dots, x_{n} - a_{n})$.

Suppose $f, g$ are global functions on $\operatorname{Spec} A$ with $f(\mathfrak{m / i}) = g(\mathfrak{m / i})$ at every closed point $\mathfrak{m / i} \in \operatorname{Spec} A$. Equivalently, $f - g$ is contained in every maximal ideal $\mathfrak{m / i} \subseteq A$. But the maximal ideals $\mathfrak{m} \subseteq \overline{\mathbb{F}}[x_{1}, \dots, x_{n}]$ have intersection $0$. Thus, so do the $\mathfrak{m} / \mathfrak{i}$.

---

When we define varieties over $\overline{\mathbb{F}}$, this will imply that functions on varieties over algebraically closed fields are determined by their values on closed points.

This discussion of closed points extends to explain our notion of points containing each other. A point can't really contain another point, but its closure certainly can. We will see that the closure of a "curve point" in $\mathbb{A}^2_{\mathbb{C}}$ is the curve and all the closed points on it, and thus, the curve contains all the points on it.

##### _definition:_ specialisation and generisation

Suppose $x, y \in X$ such that $x \in \overline{\{ y \}}$. Then $x$ is a **specialisation** of $y$ and $y$ is a **generisation** of $x$.

---

##### _example:_ specialisation and generisation in $\mathbb{A}^2_{\mathbb{C}}$

Consider the point $(y - x^{2}) = \mathfrak{p} \in \mathbb{A}^{2}_{\mathbb{C}}$. Clearly, $(y - x^{2}) \subseteq (x - 1, y - 1)$ so its closure $V(\mathfrak{p})$ contains $(x - 1, y - 1)$. That is, $(y - x^{2})$ is a generisation of $(x - 1, y - 1)$ and conversely, $(x - 1, y - 1)$ is a specialisation of it.

---

This also allows us to make formal the notion of a generic point.

##### _definition:_ generic point

A point $p \in X$ is a **generic point** of a closed subset $K \subseteq X$ if $\overline{\{ p \}} = K$.

---

Note that generic is different from general — typically general means every point of some dense open subset.

##### _example:_ generic point of a curve in $\mathbb{A}_{\mathbb{C}}^{2}$

The point $(y - x^{2}) = \mathfrak{p} \in \mathbb{A}_{\mathbb{C}}^{2}$ is a generic point of $V(y - x^{2})$. The closure is the smallest closed set containing $(y - x^{2})$. Thus, it is $V(\mathfrak{i})$ for the maximal $\mathfrak{i}$ contained in $\mathfrak{p}$, which is of course $\mathfrak{i} = \mathfrak{p}$.

---

This generic point can be thought of as generic in that it is nowhere in particular on the parabola, as opposed to $(x - 1, y - 1)$ which is a specific point on the parabola.

It also serves as a tester for the whole closed subset. Since it is "near" exactly the points of $K$ in a sense that we will make precise below, we can check statements about points of $K$ by checking then for the generic point. (This is not always true — for example, we can only check reducedness at generic points for reasonable schemes).

##### _proposition:_ generic points are near exactly the points of their closure

Suppose $p$ is a generic point of $K \subseteq X$. Every neighbourhood of each point in $K$ contains $p$. Each point not in $K$ has a neighbourhood not containing $p$.

###### _proof:_

Suppose $q \in K \setminus \{ p \}$. Then $q$ is a [[Topology --- math-147/notes/Limit points and closed sets#_definition _ limit point|limit point]] of $p$. Thus, every neighbourhood of $q$ intersects with $\{ p \}$.

Suppose $q \not\in K$. If every neighbourhood of $q$ contained $p$, then $q$ would be a limit point of $\{ p \}$, and thus, would be contained in $K$.

---

### The structure sheaf