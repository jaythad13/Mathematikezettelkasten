---
tags:
- alg
- alg-geo
- math-176/12
- math-176/13
- math-176/25
- math-176/26
- math-176/27
- math-176/28
---

### (Abelian) groups

We should know what a group is —

![[Abstract algebra --- math-171/notes/Groups, and why you should care#_definition _ group, identity, inverse|Groups, and why you should care]]

Note that we don't have to assume that the identity and inverses work on the left and the right — just assuming left inverses is enough to prove that the identity and inverses are unique and work on the right too.

Typically in this class we care about abelian groups

![[Abstract algebra --- math-171/notes/Groups, and why you should care#_definition _ abelian group, commutative group|Groups, and why you should care]]

### (Commutative) rings (with identity)

Obviously, we need to know what a ring is

![[Abstract algebra --- math-171/notes/Rings#_definition _ rings|Rings]]

Again, we don't actually have to assume $(R, +)$ is abelian — distributivity forces $(R, +)$ to be abelian

We will never care about rings without multiplicative identity

![[Abstract algebra --- math-171/notes/Rings#_definition _ ring with identity|Rings]]

We use almost the same definition, but we explicitly exclude the trivial ring where $0 = 1$.

And we will almost always be working with commutative rings

![[Abstract algebra --- math-171/notes/Rings#_definition _ commutative ring|Rings]]

Finally, we should know what the morphisms between rings are —

![[Abstract algebra --- math-171/notes/Ring homomorphisms#_definition _ ring homomorphisms|Ring homomorphisms]]

### Ideals

Recall that if a subring is a generalisation of a [[Abstract algebra --- math-171/notes/Subgroups#_definition _ subgroup, $ le$|subgroup]]

![[Abstract algebra --- math-171/notes/Rings#_definition _ subring|Rings]]

then an ideal is a generalisation of a [[Abstract algebra --- math-171/notes/Normal subgroups#_definition _ normal subgroups|normal subgroup]].

![[Abstract algebra --- math-171/notes/Ideals and quotients#_definition _ (left and right) ideals]]

Since we work with commutative rings, we don't have a distinction between left and right ideals — these are all just ideals.

Note that by the first isomorphism theorem, we know that ideals are exactly the subrings that are kernels of homomorphisms, and equivalently, the subrings that give quotient rings —

![[Abstract algebra --- math-171/notes/Ring homomorphisms#_proposition _ images and kernels|Ring homomorphisms]]

![[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the first isomorphism theorem|Ring isomorphism theorems]]

![[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the second isomorphism theorem|Ring isomorphism theorems]]

The second isomorphism theorem is often called the diamond isomorphism theorem for Hasse diagram reasons.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& R \\
		& A + B \ar[u, no head] \\
		A \ar[ur, no head] & & B \ar[ul, no head] \\
		& A \cap B \ar[ul, no head] \ar[ur, no head]\\
		& \{ 0 \} \ar[u, no head]
	\end{tikzcd}
\end{document}
```

![[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the third isomorphism theorem|Ring isomorphism theorems]]

![[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the fourth isomorphism theorem|Ring isomorphism theorems]]

This fourth isomorphism theorem is extremely useful when we start talking about [[Algebraic varieties --- math-176/notes/Spectra#_definition _ $ operatorname{Spec} R$ spectrum|spectra]] — the collections of all prime ideals of a ring.

### Integral domains

We should also recall the definition of integral domains (and thus, we need to recall the definition of zero divisors)

![[Abstract algebra --- math-171/notes/Rings#_definition _ zero divisor|zero divisor]]

![[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domains]]

We really like integral domains because they have nice properties like cancellation!

![[Abstract algebra --- math-171/notes/Integral domains#_proposition _ cancellation in integral domains|Integral domains]]

### Prime and maximal ideals

We use the following characterisation of prime ideals

![[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|Prime and maximal ideals]]

![[Abstract algebra --- math-171/notes/Prime and maximal ideals#_proposition _ prime ideals have integral domains as quotients|Prime and maximal ideals]]

Maximal ideals are even more special!

![[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ maximal ideal|Prime and maximal ideals]]

![[Abstract algebra --- math-171/notes/Prime and maximal ideals#_proposition _ maximal ideals have fields as quotients|Prime and maximal ideals]]

Note that as a corollary

![[Abstract algebra --- math-171/notes/Prime and maximal ideals#_corollary _ every maximal ideal is prime|Prime and maximal ideals]]


![[Abstract algebra --- math-171/notes/Prime and maximal ideals#_example _ not every prime ideal is maximal|Prime and maximal ideals]]

##### _proposition:_ the fourth isomorphism theorem preserves prime and maximal ideals

Let $I \subset R$ be an ideal. Then $P$ with $I \subset P \subset R$ is a prime ideal if and only if $P / I \subset R / I$ is a prime ideal. Also, $M$ with $I \subset M \subset R$ is a maximal ideal if and only if $M / I \subset R / I$ is a maximal ideal.

###### _proof sketch:_

Apply the third isomorphism theorem to see that $(R / I) / (J / I) \cong R / J$ and thus, $R / J$ [[Abstract algebra --- math-171/attachments/homework/hw 13/hw 13.pdf#page=5|is a field/integral domain if and only if]] $(R / I) / (J / I)$ is too.

### Fields

We should know what a division ring is

![[Abstract algebra --- math-171/notes/Rings#_definition _ division ring|Rings]]

By unit, we mean that it has an inverse —

![[Abstract algebra --- math-171/notes/Rings#_definition _ unit|Rings]]

The set of all units in a ring $R$ is often denoted $R^*$ and is a group under multiplication!

Obviously we're building up to what a field is —

![[Abstract algebra --- math-171/notes/Fields#_definition _ fields|Fields]]

The characteristic is a way to compare the size of a field, using the integers as our point of comparison. 

##### _definition:_ characteristic

Consider the ring homomorphism $\varphi : \mathbb{Z} \to F$ by
$$
\varphi : a \mapsto \underbrace{1 + \dots + 1}_{a \text{ times}}
$$
for $a > 0$.

Since $\ker \varphi$ is an ideal inside a [[Abstract algebra --- math-171/notes/Unique factorisation#_example _ the integers|Euclidean domain]], $\mathbb{Z}$, we have $\ker \varphi = m \mathbb{Z}$ for some $m$. We say the characteristic of $F$ is $\operatorname{char}(F) = m$.

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

Using the [[Complex analysis --- math-135/notes/Cauchy integral formula#_theorem _ the fundamental theorem of algebra|fundamental theorem of algebra]] and the fact that $\mathbb{C} \cong \mathbb{R}[x] / (x^{2} + 1)$, we can see that $\overline{\mathbb{R}} = \mathbb{C}$.

