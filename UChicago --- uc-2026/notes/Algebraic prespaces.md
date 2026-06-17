---
tags:
- uc-2026/de-rham/1
- alg-geo
- michael-barz
---

Vladimir Arnold famously complained that French students can only solve $\int dx / \sqrt{ 1 - x^{2} }$ while Russian students can also solve $\int dx / \sqrt{ x^{3} - 2 }$. We will understand what this has to do with the algebraic geometry of the substitutions $y^{2} = 1 - x^{2}$ (which completes to $\mathbb{P}^1_{\mathbb{C}}$) and $y^{2} = x^3 - 2$ (which is an elliptic curve, so a torus over $\mathbb{C}$).

One sense in which we can understand the difference is that the homogenisation of the first is easy to solve over $\mathbb{Z}$ — the Diophantine equation $a^{2} + b^{2} = c^{2}$ was already solved completely by Euclid. However, the second is very difficult — the Diophantine equation $a^{2} c = b^{3} - 2c^{3}$ was only solved by Mordell using algebraic number theory. Even though Fermat could have solved it, that's still very far removed from Euclid.

We will also see a suspicious coincidence — the dimension of algebraic varieties (say as varieties over $\mathbb{C}$) has something to do with the the point counts $N_{p^k}$ of solutions over $\mathbb{Z} / (p^k)$. This is clear for equations like $y - x^{2} = 0$ and $x + y + z = 0$ which are $1$ and $2$-dimensional and have $p$ and $p^{2}$ points over $\mathbb{F}_{p}$ because we can choose $x$ or $x$ and $y$ freely. However, this coincidence holds even over $x^{2} + y^{2} = 1$, just approximately. This is $1$-dimensional and has
$$
N_{p^k} = \begin{cases}
p^k - p^{k - 1} & p \equiv 1 \pmod 4 \\
p^k + p^{k - 1} & p \equiv 3  \pmod 4 \\
2 p^k
\end{cases}
$$
all of which are $O(p^k)$.

### Algebraic prespaces

Because schemes are hard, we won't use them. Instead we will use algebraic prespaces.

##### _definition:_ algebraic prespaces, morphisms of prespaces

An **(algebraic) prespace** is a (covariant) [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|functor]] $X : \mathsf{Ring} \to \mathsf{Set}$.

A **morphism of prespaces** is a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformation]] of functors.

We can identify schemes with corresponding prespaces. The scheme $X$ corresponds to the (contravariant) functor of $\operatorname{Spec} A$[[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_definition _ scheme-valued points of a scheme|-points]] of $X$, with $A \mapsto \operatorname{Mor}(\operatorname{Spec} A, X) = X(A)$. Note that since this is contravariant on affine schemes, it is covariant on rings.

---