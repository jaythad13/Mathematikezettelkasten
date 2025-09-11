---
tags:
- math-189AA/5
- comm-alg
---

A local ring is the [[Commutative algebra --- math-189AA/notes/Jacobson radical|nicest possible ring]] for the behaviour of units and non-units under addition.

##### _definition:_ local rings

A **local ring** is a ring with a unique [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ maximal ideal|maximal ideal]] ideal.

We sometimes specify this ideal with the ring — $A, \mathfrak{m}$ is a local ring

---

However, there's a problem — not all rings are local. Local-ity is not even preserved by polynomial extension.

##### _example:_ local-ity is not preserved

$\mathbb{C}$ is local because it is a field. $\mathbb{C}[x]$ is not local because every $(x - \lambda)$ is maximal. $\mathbb{C}[[x]]$ is local because everything not in $(x)$ is a unit.

We can make our rings local by quotienting out by the right thing.

##### _example:_ quotients can be more local

$\mathbb{F}[x]$ is generally not local (for $\mathbb{F}$ a field). However, $\mathbb{F}[x] / (x^{2})$ is local because the only ideal containing $(x^{2})$ is the maximal ideal $(x)$, and thus, $(x)$ is the only non-zero ideal in $\mathbb{F}[x] / (x^{2})$.