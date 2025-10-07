---
tags:
- rising-sea
- alg-geo
- comm-alg
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

### The affine line and affine space in general

In fact, we can define the affine line and affine space over any ring.

##### _definition:_ affine $n$-space

Affine $n$-space over $A$ is the affine scheme $\operatorname{Spec} A[x_{1}, \dots, x_{n}]$.

---

We usually choose $A$ a field. For $\mathbb{C}$ (or any algebraically closed $\overline{\mathbb{F}}$) any affine $n$-space behaves similarly to the affine line, with some scheme-theoretic points (just like $(0) \in \mathbb{A}^1_{\mathbb{C}}$).

##### _example:_ points of $\mathbb{A}^3_{\mathbb{C}}$

The points of $\mathbb{A}^3_{\mathbb{C}}$ are  
- $(0)$ — the "three-dimensional" generic point
- all irreducible $(f(x, y, z))$, corresponding to the "two-dimensional" generic point of a hypersurface $\{ (a, b, c) \mid f(a, b, c) = 0 \} \subseteq \mathbb{C}^{3}$
- lots of "one-dimensional" generic points corresponding to irreducible curves in $\mathbb{C}^{3}$ (for which there is no reasonable classification)
- finally, the regular points $(x - a, y - b, z - c)$ corresponding to $(a, b, c) \in \mathbb{C}^{3}$.

---

However, over a field that is not algebraically closed, even the closed points (the maximal ideals) can correspond to points that are not there in $\mathbb{F}^n$.

##### _example:_ points of $\mathbb{A}^1_{\mathbb{R}}$

The points of $\mathbb{A}^1_{\mathbb{R}}$ are $(0)$ and all irreducible polynomials. Since $\mathbb{R}[x]$ is [[Abstract algebra --- math-171/notes/Factorisation in special rings|Euclidean]], these are all maximal. The "normal" maximal ideals, corresponding to $a \in \mathbb{R}^1$ are $(x - a) \subseteq \mathbb{R}[x]$. The other maximal ideals are $(x^{2} + bx + c)$ with $b^{2} < c$. These correspond to adjoining roots $\lambda, \overline{\lambda} \in \mathbb{C} \setminus \mathbb{R}$ to $\mathbb{R}$. 

These are all of the other maximal ideals — we can prove that there are no subfields of $\mathbb{C}$ between $\mathbb{R}$ and $\mathbb{C}$. This follows since $\mathbb{R}[\lambda] \cong \mathbb{R}[i]$.

---

This example of maximal ideals corresponding to finite extensions continues and is formalised in [[Algebraic geometry --- rising-sea/notes/Hilbert's Nullstellensatz|Hilbert's Nullstellensatz]]

##### _examples:_ affine spaces over $\mathbb{Q}$



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