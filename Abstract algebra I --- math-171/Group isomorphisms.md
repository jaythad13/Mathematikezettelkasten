---
tags:
- math-171
- alg
lecture:
- math-171-6
---

An isomorphism is just a bijective [[Group homomorphisms|homomorphism]].

##### _definition:_ group isomorphism, isomorphic

We say a homomorphism $\varphi : G \to H$ is an isomorphism if it is bijective.

We say $G \cong H$, or that they are isomorphic if there exists an isomorphism between them.

Note that in order for $\varphi$ to be an isomorphism we must have $\ker \varphi = \{ 1_G \}$ and $\operatorname{Im} \varphi = H$.

### Lots of examples of isomorphisms

##### _example:_ the direct product is commutative

Let $A$ and $B$ be groups. Then $A \times B \cong B \times A$ by $(a, b) \mapsto (b, a)$.

##### _example:_ symmetric groups only care about cardinality

Let $A$ and $B$ be sets. Then $S_{A} \cong S_{B}$ if and only if $\lvert A \rvert = \lvert B \rvert$.

##### _example:_ exponentials convert addition to multiplication

$(\mathbb{R}, +) \cong (\mathbb{R}^+, \times)$ by $x \mapsto e^x$.

##### _example:_ every permutation of vertices of a triangle is a rigid symmetry

$D_{6} \cong S_{3}$ by $s^i r^j \mapsto (2 \, 3)^i (1 \, 2 \, 3)^j$

##### _example:_ the Chinese remainder theorem for $2$ and $3$

$\mathbb{Z} / 2 \mathbb{Z} \times \mathbb{Z} / 3 \mathbb{Z} \cong \mathbb{Z} / 6 \mathbb{Z}$ by $(1, 1) \mapsto 1$.

Isomorphisms tell us that two things have the exact same algebraic structure. If two things don't have the same algebraic structure then we should be able to spot the differences.

### Non-isomorphisms

##### _example:_ $(\mathbb{R}^\times, \times) \not \cong (\mathbb{C}^\times, \times)$ because of differences in the number of roots

We can show that this is true by contradiction. Say that we had an isomorphism $\varphi : \mathbb{C}^\times \to \mathbb{R}^\times$. Then for $\omega$, one of the non-unity third roots of unity, we would have
$$
\begin{split}
\varphi(\omega)^3 & = \varphi(\omega^3) \\
& = \varphi(1) \\
& = 1.
\end{split}
$$
Thus, $\varphi$ is not injective.

In general we can also use counting arguments to disprove isomorphisms

##### _example:_ $(\mathbb{R}, +) \not \cong (\mathbb{Q}, +)$ by cardinality

$\lvert \mathbb{Q} \rvert < \lvert \mathbb{R} \rvert$ so we cannot have a bijection between them.

##### _example:_ $\mathbb{Z} \not \cong \mathbb{Q}$ by cyclicity

$\mathbb{Z}$ is cyclic, but $\mathbb{Q}$ is not — you can't write every rational as a finite sum of sum fixed chosen generator.
