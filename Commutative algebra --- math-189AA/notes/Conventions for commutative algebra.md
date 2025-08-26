---
tags:
- comm-alg
- math-189AA/1
---

Commutative algebra is the study of commutative rings. These come up naturally a lot (think $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{F}[x]$). In this category we won't just think about rings in general, but rather, [[Abstract algebra --- math-171/notes/Rings#What's a ring?|commutative, unital rings]] and we will expect their morphisms to preserve the identity — that is, we require that a ring homomorphism $f : A \to B$ must have $f(1) = 1$.

##### _homework:_ ring homomorphisms compose

If $f : A \to B$ and $g : B \to C$ are [[Abstract algebra --- math-171/notes/Ring homomorphisms#_definition _ ring homomorphisms|ring homomorphisms]], show that $g \circ f$ is a ring homomorphism.

Algebra is really the study of algebras.

##### _definition:_ algebras

An $A$-algebra is a ring $B$ and a choice of specific structure homomorphism $f : A \to B$.

Note that this allows us to define $ab = f(a) b$ for $a \in A, b \in B$.