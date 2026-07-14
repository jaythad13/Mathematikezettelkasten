---
tags:
- uc-2026/exotic/1
- alg-top
- diff-geo
- mark-behrens
---

To prove the existence of [[UChicago --- uc-2026/notes/Exotic spheres#_theorem _ exotic $7$-spheres exist (Milnor)|exotic spheres]], we need some diffeomorphism-invariant algebra that is not homeomorphism-invariant.

##### _definition:_ intersection form on cohomology

By Poincaré duality, if $\dim X \equiv 0 \pmod 4$ there is a [[Quadratic forms and K-theory --- pcmi-2021/notes/Quadratic forms#_definition _ (non-degenerate, symmetric) bilinear forms, quadratic forms, quadratic spaces, homomorphisms of quadratic spaces, quadratic linear map|quadratic form]]
$$
H^k(X, \mathbb{R}) \otimes H^k(X, \mathbb{R}) \to \mathbb{R}
$$
by $\alpha \otimes \beta \mapsto \left< \alpha \cup \beta, [M] \right>$. This is the **intersection form** on the cohomology of $X$.

---

Note, this is still homeomorphism-invariant!

##### _definition:_ characteristic classes

A **characteristic class** is a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformation]] of functors $\operatorname{Vect}^n \to H^\bullet(-, A)$.

---

There are Stieffel–Whitney classes $w_{i} : \operatorname{Vect}_{X}^n \to H^i(X, \mathbb{Z} / 2)$ on real manifoldsand Chern classes $c_{i} : \operatorname{Vect}^n_{X} \to H^{2i}(X, \mathbb{Z})$ on complex manifolds. We are interested in Pontrjagin classes.

##### _definition:_ Pontrjagin classes

The $i$th **Pontrjagin class** of a real vector bundle $\mathscr{V} \to X$ is $(-1)^i c_{2i}(\mathscr{V} \otimes_{\mathbb{R}} \mathbb{C})$. 

---