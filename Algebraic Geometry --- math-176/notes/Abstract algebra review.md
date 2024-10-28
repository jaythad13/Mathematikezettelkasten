---
tags:
- alg
- alg-geo
- math-176/12
- math-176/13
- math-176/25
- math-176/26
---

### (Abelian) groups

We should know what a group is —

![[Abstract Algebra I --- math-171/notes/Groups, and why you should care#_definition _ group, identity, inverse|Groups, and why you should care]]

Note that we don't have to assume that the identity and inverses work on the left and the right — just assuming left inverses is enough to prove that the identity and inverses are unique and work on the right too.

Typically in this class we care about abelian groups

![[Abstract Algebra I --- math-171/notes/Groups, and why you should care#_definition _ abelian group, commutative group|Groups, and why you should care]]

### (Commutative) rings (with identity)

Obviously, we need to know what a ring is

![[Abstract Algebra I --- math-171/notes/Rings#_definition _ rings|Rings]]

Again, we don't actually have to assume $(R, +)$ is abelian — distributivity forces $(R, +)$ to be abelian

We will never care about rings without multiplicative identity

![[Abstract Algebra I --- math-171/notes/Rings#_definition _ ring with identity|Rings]]

We use almost the same definition, but we explicitly exclude the trivial ring where $0 = 1$.

And we will almost always be working with commutative rings

![[Abstract Algebra I --- math-171/notes/Rings#_definition _ commutative ring|Rings]]

Finally, we should know what the morphisms between rings are —

![[Abstract Algebra I --- math-171/notes/Ring homomorphisms#_definition _ ring homomorphisms|Ring homomorphisms]]

### Ideals

Recall that if a subring is a generalisation of a [[Abstract Algebra I --- math-171/notes/Subgroups#_definition _ subgroup, $ le$|subgroup]]

![[Abstract Algebra I --- math-171/notes/Rings#_definition _ subring|Rings]]

then an ideal is a generalisation of a [[Abstract Algebra I --- math-171/notes/Normal subgroups#_definition _ normal subgroups|normal subgroup]].

![[Abstract Algebra I --- math-171/notes/Ideals and quotients#_definition _ (left and right) ideals]]

Since we work with commutative rings, we don't have a distinction between left and right ideals — these are all just ideals.

Note that by the first isomorphism theorem, we know that ideals are exactly the subrings that are kernels of homomorphisms, and equivalently, the subrings that give quotient rings —

![[Abstract Algebra I --- math-171/notes/Ring homomorphisms#_proposition _ images and kernels|Ring homomorphisms]]

![[Abstract Algebra I --- math-171/notes/Ring isomorphism theorems#_theorem _ the first isomorphism theorem|Ring isomorphism theorems]]

### Integral domains

We should also recall the definition of integral domains (and thus, we need to recall the definition of zero divisors)

![[Abstract Algebra I --- math-171/notes/Rings#_definition _ zero divisor|zero divisor]]

![[Abstract Algebra I --- math-171/notes/Integral domains#_definition _ integral domain|integral domains]]

We really like integral domains because they have nice properties like cancellation!

![[Abstract Algebra I --- math-171/notes/Integral domains#_proposition _ cancellation in integral domains|Integral domains]]

We use the following characterisation of prime ideals

![[Abstract Algebra I --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|Prime and maximal ideals]]

![[Abstract Algebra I --- math-171/notes/Prime and maximal ideals#_proposition _ prime ideals have integral domains as quotients|Prime and maximal ideals]]

These prime ideals are respected by ring homomorphisms —

##### _proposition:_ the pullback on spectra

Suppose $\varphi : R \to S$ is a non-trivial homomorphism between integral domains. Denote the collection of prime ideals by
$$
\operatorname{Spec} S = \{ P \subset S \mid P \text{ is prime} \}.
$$

Then the pre-image of a prime $P \subset S$ is a prime in $R$ — $\varphi^\text{pre}(P)$ is prime in $R$ and the pullback
$$
\begin{split}
\varphi^* & : \operatorname{Spec} S \to \operatorname{Spec} R \\
 & : P \mapsto \varphi^\text{pre}(P).
\end{split}
$$
is well defined.

### Fields

We should know what a division ring is

![[Abstract Algebra I --- math-171/notes/Rings#_definition _ division ring|Rings]]

By unit, we mean that it has an inverse —

![[Abstract Algebra I --- math-171/notes/Rings#_definition _ unit|Rings]]

The set of all units in a ring $R$ is often denoted $R^*$ and is a group under multiplication!

Obviously we're building up to what a field is —

![[Abstract Algebra I --- math-171/notes/Fields#_definition _ fields|Fields]]

The characteristic is a way to compare the size of a field, using the integers as our point of comparison. 

##### _definition:_ characteristic

Consider the ring homomorphism $\varphi : \mathbb{Z} \to F$ by
$$
\varphi : a \mapsto \underbrace{1 + \dots + 1}_{a \text{ times}}
$$
for $a > 0$.

Since $\ker \varphi$ is an ideal inside a [[Abstract Algebra I --- math-171/notes/Factorisation in special rings#_example _ the integers|Euclidean domain]], $\mathbb{Z}$, we have $\ker \varphi = m \mathbb{Z}$ for some $m$. We say the characteristic of $F$ is $\operatorname{char}(F) = m$.

This $m$ is the first $m$ such that $\varphi(m) = 0$, and tells us whether the integer can "sit inside" a field, or they need to wrap around after some $m$. 

##### _example:_ characteristics of all the fields you could care about

1) Since $\mathbb{Q}$, $\mathbb{R}$, and $\mathbb{C}$ all contain the integers in an obvious way, the kernel of the homomorphism is just $\{ 0 \}$. Thus, $\operatorname{char}(\mathbb{Q}) = \operatorname{char}(\mathbb{R}) = \operatorname{char}(\mathbb{C}) = 0$.
2) $\operatorname{char}(\mathbb{Z} / p \mathbb{Z}) = p$, obviously.
3) For any finite field $\mathbb{F}_{q}$ with $q = p^e$ for prime $p$, we have $\operatorname{char}(\mathbb{F}_{q}) = p$ (this result requires some Galois theory)

Finally, we talk about algebraic closure and field extensions.

##### _definition:_ field extensions

For any field $F$, we say $K / F$ is a field extension if $K$ is a field with an injective ring homomorphism $F \xhookrightarrow{} K$.

##### _definition:_ algebraic numbers, algebraic extensions

We say $a \in K / F$ is an algebraic number if $a$ is the root of some polynomial in $F[x]$.

If all $a \in K / F$ are algebraic numbers, then $K / F$ is a an algebraic extension.

##### _proposition:_ towers of algebraic extensions

$L / F$ is an algebraic extension if and only if $K / F$ is an algebraic extension whenever $F \xhookrightarrow{\varphi} K \xhookrightarrow{\psi} L$ (with $\varphi, \psi$ injective homomorphisms).

##### _definition:_ algebraic closure

The algebraic closure of a field $F$ is the smallest algebraic extension of $F$ such that
$$
F \xhookrightarrow{} K \xhookrightarrow{} \overline{F}
$$
for any algebraic extension $K / F$.

##### _example:_ algebraic extensions for Pell's equation

Consider $\mathbb{Q}$. For any non-square $d \in \mathbb{Q}$, the field
$$
\mathbb{Q}(d) = \{ x + y \sqrt{ d } \mid x, y \in \mathbb{Q} \} \cong \mathbb{Q}[x] / (x^{2} - d)
$$
is an algebraic extension.

We can see that $\mathbb{Q}(d)$ is a field since $(x^{2} - d)$ will be a maximal ideal in $\mathbb{Q}[x]$.

##### _example:_ algebraic closures

Note that $\overline{\mathbb{Q}}$ is not $\mathbb{C}$. In fact, $\mathbb{C}$ is not even an algebraic extension of $\mathbb{Q}$ since $\mathbb{R} / \mathbb{Q}$ is not algebraic, breaking the tower of extensions ($\pi, e$, for example are not algebraic numbers).

Using the [[Complex Analysis --- math-135/notes/Cauchy integral formula#_theorem _ the fundamental theorem of algebra|fundamental theorem of algebra]] and the fact that $\mathbb{C} \cong \mathbb{R}[x] / (x^{2} + 1)$, we can see that $\overline{\mathbb{R}} = \mathbb{C}$.

### Polynomial rings

We can define polynomials for rings too, and these polynomials form rings themselves!

##### _definition:_ polynomial, degree, $R[x]$

Given a ring $R$, a polynomial $p$ is a formal sum
$$
a_{n} x^n + \dots + a_{1} x + a_{0}
$$
with $a_{n} \in R$. 

If $n$ is the largest integer with $a_{n} \neq 0$, we say say the degree of $p$ is $\operatorname{deg}(p) = n$. If all coefficients $a_{n}$ are $0$, we say $\operatorname{deg}(p) = -\infty$.

##### _proposition:_ polynomial rings are rings

$R[x]$ is a ring under the obvious multiplication and addition.

##### _proposition:_ polynomials over integral domains are really nice

If $R$ is an integral domain, then $R[x]$ is an integral domain with the same units as $R$ and $\operatorname{deg}(pq) = \operatorname{deg} p + \operatorname{deg} q$ for any $p, q \in R[x]$.

###### _proof:_

Suppose $R$ is an integral domain. Consider any non-zero polynomials $p = \sum a_{j} x^j$ and $q = \sum b_{j} x^j$ of degrees $m$ and $n$ in $R[x]$. Their product has a leading term $a_{m} b_{n} x^{m + n}$ and since $R$ is an integral domain, $a_{m} b_{n} \neq 0$. Thus, $\operatorname{deg}(pq) = p + q > -\infty$ giving $pq \neq 0$. 

The units of $R[x]$ are just the polynomials constant on a unit. This is just isomorphic to the units of $R$.

##### _corollary:_ multivariate polynomial rings

If $R$ is an integral domain, then $R[x_{1}, \dots, x_{n}, x_{n + 1}] = R[x_{1}, \dots, x_{n}][x_{n + 1}]$, defined inductively, is an integral domain.