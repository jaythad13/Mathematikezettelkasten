---
tags:
- alg-nt
- galois
- math-177/13
- math-177/14
- math-177/15
- math-177/16
- math-177/17
- math-177/18
- math-177/19
---

Extensions of the $p$-adics and number fields in general have a nice underlying algebraic structure. For any $\mathbb{K} / \mathbb{Q}_{p}$ we can define a ring of integers $\mathscr{O}_{\mathbb{K}} \subseteq \mathbb{K}$ that behaves like $\mathbb{Z}_{p} \subseteq \mathbb{Q}_{p}$.

##### _definition:_ ring of integers

If $\mathbb{K}$ is a finite extension of $\mathbb{Q}_{p}$ with extended $p$-adic absolute value, then the **ring of integers of $\mathbb{K}$** is $\mathscr{O}_{\mathbb{K}} = \{ z \in \mathbb{K} \mid \lvert z \rvert_{p} \leq 1 \}$.

---

This definition really is natural in some sense — $\mathscr{O}_{\mathbb{K}}$ can really be thought of as an analogue of $\mathbb{Z}_{p} \subseteq \mathbb{Q}_{p}$.

##### _proposition:_ the ring of integers is the integral closure

$\mathscr{O}_{\mathbb{K}}$ is the **integral closure** of $\mathbb{Z}_{p}$ — $\mathscr{O}_{\mathbb{K}}$ consists precisely of those $\alpha \in \mathbb{K}$ that are roots of monic polynomials in $\mathbb{Z}_{p}[x]$.

###### _proof:_

Suppose $\alpha$ is a root of some monic $\sum_{i = 0}^n a_{i} x^i$. Then 
$$
\lvert \alpha \rvert_{p}^n = \left\lvert  -\sum_{i = 0}^{n - 1} a_{i} \alpha^i  \right\rvert \leq \max \{ \lvert \alpha \rvert_{p}^{n - 1}, \lvert \alpha \rvert_{p}^{n - 2}, \dots, \lvert \alpha \rvert_{p}, 1 \}.
$$
Thus $\lvert \alpha \rvert_{p}^n \leq \lvert \alpha \rvert_{p}^{n - 1}$ implying $\lvert \alpha \rvert_{p} \leq 1$ and thus, $\alpha \in \mathscr{O}_{\mathbb{K}}$.

Conversely, suppose $\alpha \in \mathscr{O}_{\mathbb{K}}$. Then $\lvert \alpha \rvert_{p} \leq 1$. Consider the minimal polynomial $p_{\alpha}$ of $\alpha$ (over $\mathbb{Q}_{p}$). Working in the [[p-adic numbers --- math-177/notes/Algebraic field extensions#_definition _ splitting field|splitting field]] of $p_{\alpha}$ over $\mathbb{K}$, we get
$$
p_{\alpha}(x) = \prod_{i = 1}^n (x - \alpha_{i})
$$
By definition of the extension of the norm, we must have $\lvert \alpha_{i} \rvert_{p} = \lvert \alpha \rvert_{p}$. The coefficients of $p_{\alpha}$ are sums of products of $\alpha_{i}$, and thus, by the [[p-adic numbers --- math-177/notes/The p-adic numbers#_proposition _ the $p$-adic absolute value is an ultrametric|strong triangle inequality]], all have norm at most $1$. Thus, the coefficients are in $\mathbb{Z}_{p}$. That is, $p_{\alpha} \in \mathbb{Z}_{p}[x]$.

---

##### _proposition:_ the ring of integers is local

If $\mathbb{K}$ is a finite extension of $\mathbb{Q}_{p}$ with extended $p$-adic absolute value, then the ring of integers $\mathscr{O}_{\mathbb{K}}$ is a [[Commutative algebra --- math-189AA/notes/Local rings#_definition _ local rings|local ring]] with unique maximal ideal $\mathfrak{m}_{\mathbb{K}} = \{ z \in \mathbb{K} \mid \lvert z \rvert_{p} < 1 \}$.

---

Of course, then the natural thing to do is to define the residue field.

##### _definition:_ residue field

The **residue field** of a field extension $\mathbb{K} / \mathbb{Q}_{p}$ is $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$.

----

This field is naturally an extension of the residue field of $\mathbb{Q}_{p}$ — $\mathbb{F}_{p}$.

##### _proposition:_ the residue field is an extension of residue fields

Let $\mathbb{K}$ be a finite extension of $\mathbb{Q}_{p}$. Then $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ is an algebraic extension of $\mathbb{F}_{p}$.

###### _proof:_

Consider $\mathbb{F}_{p} \to \mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ by $a + p \mathbb{Z} \mapsto a + \mathfrak{m}_{\mathbb{K}}$ (with the embedding $\mathbb{Z} \to \mathbb{Z}_{p} \to \mathscr{O}_\mathbb{K}$). This is well-defined since two integers have the same residue modulo $p$ exactly when they differ by an element of $p \mathbb{Z}_{p}$, which is an element of $p \mathbb{Z}_{p}$ which is contained in $\mathfrak{m}_{\mathbb{K}}$. It inherits being a homomorphism from 

Conversely, if $a \mapsto 0$ then $a \in \mathfrak{m}_{\mathbb{K}}$. Since $\mathbb{Z} \cap \mathfrak{m}_{\mathbb{K}}$ is just $p \mathbb{Z} = \{ z \in \mathbb{Z} \mid \lvert z \rvert_{p} \leq 1 \}$, then $a \equiv 0$ in $\mathbb{F}_{p}$. Thus, it is also injective. 

---

This residue field extension has degree at most the degree of the total field extension.

##### _proposition:_ the degree of the residue field extension is bounded 

The degree of the residue field extension $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ is bounded by the degree of the field extension $\mathbb{K} / \mathbb{Q}_{p}$.

###### _proof:_

Suppose $\deg \mathbb{K} / \mathbb{Q}_{p} = n$. Choose $\overline{a}_{1}, \overline{a}_{2}, \dots, \overline{a}_{n + 1} \in \mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$. For the corresponding $a_{1}, \dots, a_{n + 1}$ in $\mathscr{O}_{\mathbb{K}}$, there are $c_{i} \in \mathbb{Q}_{p}$, not all zero, such that $c_{1} a_{1} + \dots + c_{n + 1} a_{n + 1} = 0$. By multiplying by an appropriate power of $p$, we can choose the $c_{i}$ so that all of them are actually in $\mathbb{Z}_{p}$ with at least one in $\mathbb{Z}_{p}^\times$. It follows that $\overline{c}_{1} \overline{a}_{1} + \dots + \overline{c}_{n + 1} \overline{a}_{n + 1} = 0$ with not all $\overline{c}_{i} \equiv 0$.

---

### Ramification

This additional information allows us to understand field extensions both globally (as $\mathbb{K} / \mathbb{Q}_{p}$) and locally (as $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ over $\mathbb{F}_{p}$).

##### _example:_ an unramified extension

Consider $\mathbb{K} = \mathbb{Q}_{5}(\sqrt{ 2 })$. This is a quadratic extension. We claim that $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ over $\mathbb{F}_{5}$  is also a degree $2$ extension. 

In particular, $\lvert a + b \sqrt{ 2 } \rvert_{5} < 1$ if and only if $5 \mid a$ and $5 \mid b$. Then $a_{1} + b_{1} \sqrt{ 2 } \equiv a_{2} +  b_{2} \sqrt{ 2 }$ if and only if $5 \mid (a_{1} + a_{2} )$ and $5 \mid (b_{1} + b_{2})$. Then we have, $\mathbb{F}_{5} \to \mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ by $a \mapsto a + 0 \sqrt{ 2 }$. Since $1, \sqrt{ 2 }$ is a maximal linearly independent set over $\mathbb{F}_{5}$, we have that $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ is degree $2$.

Such an extension (with field extension and residue field extension of same degree), is "nice" in a geometric sense. (All points have multiplicity $1$ for the [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes|morphism]] $\operatorname{Spec} \mathscr{O}_{\mathbb{K}} \to \operatorname{Spec} \mathbb{Z}_{5}$).

---

##### _example:_ a ramified extension

Consider $\mathbb{K} = \mathbb{Q}_{5}(\sqrt{ 5 })$. This is also a quadratic extension. Here $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ over $\mathbb{F}_{5}$ behaves differently.

Note that $\lvert a + b\sqrt{ 5 } \rvert_{5}  = \lvert a^{2} - 5 b^{2} \rvert ^{1/2}_{5}$ which is less than one if and only if $5\ \mid a$. In particular, $b \sqrt{ 5 } \in \mathfrak{m}_{\mathbb{K}}$, so $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}} \cong \mathbb{F}_{5}$ with $\mathbb{F}_{5} \to \mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ by $a \to a + 0 \sqrt{ 5 }$.

This is much less nice than the previous extension, in the same geometric sense. In particular, for $\operatorname{Spec} \mathscr{O}_{\mathbb{K}} \to \operatorname{Spec} \mathbb{Z}_{5}$, $5 \mathbb{Z}_{5}$ has only one pre-image where every other point has two.

---

Because of this geometric motivation, we classify these phenomena as 

##### _definition:_ unramified, ramified, totally ramified, ramification index

Suppose $\mathbb{K}$ is a finite extension of $\mathbb{Q}_{p}$.

If the degree of $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ over $\mathbb{F}_{p}$ is the same as the degree of $\mathbb{K}$ over $\mathbb{Q}_{p}$, then $\mathbb{K}$ is an **unramified** extension of $\mathbb{Q}_{p}$.

If $\mathbb{K} / \mathbb{Q}_{p}$ is not unramified, then it is a **ramified** extension of $\mathbb{Q}_{p}$.

If $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}} \cong \mathbb{F}_{p}$, then $\mathbb{K}$ is a **totally ramified** extension of $\mathbb{Q}_{p}$

---

### The uniformiser

Let $\mathbb{K} / \mathbb{Q}_{p}$ be a degree $n$ field extension, $e$ its ramification index, and $f$ the index of $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ over $\mathbb{F}_{p}$. To understand ramification, we want to understand $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$, for which we want to understand $\mathfrak{m}_{\mathbb{K}}$. Understanding $\mathfrak{m}_{\mathbb{K}}$ is understanding the uniformiser.

##### _proposition, definition:_ the maximal ideal is principal, uniformiser

$\mathfrak{m}_{\mathbb{K}} \subseteq \mathscr{O}_{\mathbb{K}}$ is principal, generated by the **uniformiser** $\pi$.

---

##### _proposition:_ the absolute value of the uniformiser

The uniformiser $\pi$ has $p$-adic absolute value $\lvert \pi \rvert_{p} = p^{-e}$.

---

##### _proposition:_ nef

$n = ef$.

---

### Characterising extensions

Using the uniformiser, and some facts about finite fields, we can now completely classify unramified and totally ramified extensions. Since we get all other extensions by joining these together, this gives us all finite extensions of given degree. We state this formally without proof at the end.

##### _theorem:_ characterising unramified field extensions of given degree

For each $n$ there exists a unique unramified extension $\mathbb{K} / \mathbb{Q}_{p}$ of degree $n$.

###### _proof:_

Given $n$ consider [[p-adic numbers --- math-177/notes/Finite fields#_corollary _ finite field extensions of given degree are unique|the unique extension]] $\mathbb{F}_{p^n} / \mathbb{F}_{p}$ of degree $n$ and let $\zeta$ be a primitive $(p^n - 1)$th root of unity so that [[p-adic numbers --- math-177/notes/Finite fields#_theorem _ characterising finite fields|it generates the field]] $\mathbb{F}_{p^n} = \mathbb{F}_{p}(\zeta)$. Let $p_{\zeta} \in \mathbb{F}_{p}[x]$ be its [[p-adic numbers --- math-177/notes/Algebraic field extensions#_proposition, definition _ the minimal polynomial|minimal polynomial]] (of degree $n$, say). We claim there exists an [[p-adic numbers --- math-177/notes/Irreducible polynomials#_definition _ irreducible polynomial|irreducible]] degree $n$ lift $f \in \mathbb{Z}_{p}[x]$ (such that $f \mapsto p_{\zeta}$ under $\mathbb{Z}_{p}[x] \to \mathbb{F}_{p}[x]$).

Suppose $\alpha$ is a root of $f$. Then $\mathbb{Q}_{p}(\alpha) / \mathbb{Q}_{p}$ has degree $n$ (adjoining a root of an irreducible polynomial gives a full-degree extension?) and $\overline{\alpha}$ is a root of $x^{p^n - 1} - 1$. Write $\mathbb{K} = \mathbb{Q}_{p}(\alpha)$. In fact, since all roots of $p_{\zeta}$ satisfy $x^{p^k - 1} - 1$.

This is unique. If $\mathbb{K} / \mathbb{Q}_{p}$ is unramified of degree $n$, then we have uniquely identified $\mathscr{O}_{\mathbb{K}} / \mathfrak{m}_{\mathbb{K}}$ as the unique degree $n$ extension $\mathbb{F}_{p^n}  / \mathbb{F}_{p}$. Write $\mathbb{F}_{p^n} = \mathbb{F}_{p}(\zeta)$ where $\zeta^{p^k - 1} - 1 = 0$. But then by [[p-adic numbers --- math-177/notes/Hensel's lemma#_theorem _ Hensel's lemma for extensions of $ mathbb{Q}_{p}$|generalised Hensel's lemma]], we obtain a unique $\alpha \in \mathscr{O}_{\mathbb{K}}$ with $z^{p^k - 1} - 1 = 0$ and $z \equiv \zeta$. Since $\mathbb{Q}_{p}(\alpha) / \mathbb{Q}_{p}$ has residue field extension $\mathbb{F}_{p^n} / \mathbb{F}_{p}$. Since $\mathbb{Q}_{p}(\alpha) / \mathbb{Q}_{p}$ has degree at least that of $\mathbb{F}_{p^n} / \mathbb{F}_{p}$, we have that $\mathbb{Q}_{p}(\alpha) = \mathbb{K}$. That is, $\mathbb{K}$ is the splitting field of $x^{p^k - 1} - 1$.

---

To classify totally ramified extensions, we notice that we can always get a totally ramified extension from a polynomial satisfying [[p-adic numbers --- math-177/notes/Irreducible polynomials#_theorem _ Eisenstein's criterion|Eisenstein's criterion]].

##### _proposition:_ Eisenstein polynomials give totally ramified field extensions

Suppose $f(x) = \sum_{i = 0}^n a_{i} x^i$ satisfies Eisenstein's criterion and $\pi$ is a root of $f$. Then $\mathbb{Q}_{p}(\pi)$ is totally ramified.

###### _proof:_

Since $f$ satisfies Eisenstein's criterion, $a_{0} \in p \mathbb{Z}_{p}$ (the unique prime ideal of $\mathbb{Z}_{p}$) but $a_{0} \not\in p^{2} \mathbb{Z}_{p}$. Thus, $\lvert \pi \rvert_{p} = \lvert a_{0} \rvert^{1 / n} = p^{-1 / n}$. Since $\pi \in \mathfrak{m}_{\mathbb{Q}_{p}(\pi)}$ and $1 / \nu_{p}(\pi) \leq e \leq n$, we have $e = n$. Thus, $\mathbb{Q}_{p}(\pi)$ is totally ramified. 

---

Surprisingly, the converse holds.

##### _theorem:_ characterising totally ramified field extensions of a given degree

If $\mathbb{K} / \mathbb{Q}_{p}$ is a totally ramified extension of $\mathbb{Q}_{p}$ of degree $n$, then $\mathbb{K} = \mathbb{Q}_{p}(\pi)$ where $\pi$ is a root of a degree $n$ Eisenstein polynomial.

###### _proof:_

Let $\pi$ be a uniformiser of $\mathfrak{m}_{\mathbb{K}}$. Thus, $\lvert \pi \rvert_{p} = p^{- 1 / n}$. Consider the corresponding minimal polynomial $p_{\pi}(x) = \sum a_{i} x^i$ (say of degree $m$). 

Since $p_{\pi}$ is monic, we have $\lvert a_{n} \rvert_{p} = 1$ as desired.

Since $\lvert \pi \rvert_{p} = \lvert a_{0} \rvert^{1 / m}$, this implies $\lvert a_{0} \rvert = p^{-m / n}$. Since $0 \leq m \leq n$ and $\lvert a_{0} \rvert = p^{k}$ for some integer, the only choice we have is $m = n$. Thus, $\lvert a_{0} \rvert_{p} = 1 / p$, also as desired.

Finally, working in the [[p-adic numbers --- math-177/notes/Algebraic field extensions#_definition _ splitting field|splitting field]] of $p_{\pi}$ we can write
$$
\sum_{i = 0}^n a_{i} x^i = \prod_{j = 1}^n (x - \alpha_{j}).
$$
Note that $\lvert \alpha_{j} \rvert_{p} = \lvert \pi \rvert_{p} = p^{-1 / n}$ for all $j$. Each $a_{j}$ is the sum of products of $(n - j)$-many $\alpha_{j}$s. This implies $\lvert a_{j} \rvert_{p} \leq p^{(n - j)/n} < 1$ and thus, gives $a_{j} \in p \mathbb{Z}_p$, as desired.

---

##### _theorem:_ characterising all finite extensions

If $\mathbb{K}$ is a finite extension of $\mathbb{Q}_{p}$, then $\mathbb{K} = \mathbb{L}(\pi)$ where $\mathbb{L} / \mathbb{Q}_{p}$ is unramified and $\mathbb{K} / \mathbb{L}$ is totally ramified. Equivalently, $\mathbb{K} / \mathbb{Q}_{p}(\pi)$ is unramified and $\mathbb{Q}_{p}(\pi) / \mathbb{Q}_{p}$ is totally ramified.

---

##### _corollary:_ extensions of every ramification index

Given a degree $n \in \mathbb{N}$, and a divisor $e \mid n$,  there exists a degree $n$ finite extension of $\mathbb{Q}_{p}$ with ramification index $e$.

###### _proof sketch:_

Put together your favourite totally ramified extension of degree $e$ and unramified extension of degree $f = n / e$.

---