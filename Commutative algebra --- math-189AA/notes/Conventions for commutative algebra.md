---
tags:
- comm-alg
- math-189AA/1
- math-189AA/2
---

Commutative algebra is the study of commutative rings. These come up naturally a lot (think $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{F}[x]$). In this category we won't just think about rings in general, but rather, [[Abstract algebra --- math-171/notes/Rings#What's a ring?|commutative, unital rings]] and we will expect their morphisms to preserve the identity — that is, we require that a ring homomorphism $f : A \to B$ must have $f(1) = 1$.

##### _homework:_ ring homomorphisms compose

If $f : A \to B$ and $g : B \to C$ are [[Abstract algebra --- math-171/notes/Ring homomorphisms#_definition _ ring homomorphisms|ring homomorphisms]], show that $g \circ f$ is a ring homomorphism.

Algebra is really the study of algebras.

##### _definition:_ algebras

An $A$-algebra is a ring $B$ and a specific choice of structure homomorphism $f : A \to B$.

Note that this allows us to define $ab = f(a) b$ for $a \in A, b \in B$.

##### _examples:_ algebras

The set of $2$-by-$2$ matrices (over $\mathbb{R}$ say) is an $\mathbb{R}$-algebra with the diagonal map
$$
\lambda \mapsto \begin{pmatrix}
\lambda & 0 \\
0 & \lambda
\end{pmatrix}.
$$

Every ring is uniquely a $\mathbb{Z}$-algebra (since $\mathbb{Z}$ is [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_example _ initial and final objects in specific categories|initial]] in the category of rings).

##### _homework:_ find two (different) definitions of [[Abstract algebra --- math-171/notes/Rings#_definition _ subring|subrings]] (in textbooks)