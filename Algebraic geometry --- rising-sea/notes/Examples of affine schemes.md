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

### The affine line over non-algebraically closed fields

### The dual numbers

The dual numbers are the ring $\mathbb{F}[\varepsilon] / (\varepsilon^{2})$ (think of this as some adjoining some error $\varepsilon$ that we want to keep track of to the first order, but can ignore in higher orders). It has just one point $(\varepsilon)$ (by the [[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the fourth isomorphism theorem|fourth isomorphism theorem]], since $(\varepsilon)$ is the only prime ideal of $\mathbb{F}[\varepsilon]$ containing $(\varepsilon^{2})$).

It will be useful later for understanding tangents, and right now as a source of counterexamples.

##### _example:_ functions are not determined by their values

$0, \varepsilon \in \mathbb{F}[\varepsilon] / (\varepsilon^{2})$ both take value $0$ at the only point $(\varepsilon) \in \operatorname{Spec} \mathbb{F}[\varepsilon] / (\varepsilon^{2})$, yet they are not the same.

---