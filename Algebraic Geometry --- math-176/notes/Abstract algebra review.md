---
tags:
- alg
- alg-geo
- math-176/12
- math-176/13
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

### Fields

We should know what a division ring is
![[Abstract Algebra I --- math-171/notes/Rings#_definition _ division ring|Rings]]
By unit, we mean that it has an inverse. We should also know what a field is
![[Abstract Algebra I --- math-171/notes/Fields#_definition _ fields|Fields]]

The characteristic a way to compare the size of a field, using the integers as our point of comparison. 

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

##### _definition:_ algebraic extensions

We say $a \in K / F$ is an algebraic number if $a$ is the root of some polynomial in $F[x]$.

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