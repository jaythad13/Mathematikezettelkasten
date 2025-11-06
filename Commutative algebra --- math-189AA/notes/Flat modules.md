---
tags:
- comm-alg
- hom-alg
- math-189AA/21
---

Let $A$ be a ring.

[[Algebraic geometry --- rising-sea/notes/Tensor products, categorically#_proposition _ tensoring is functorial and right-exact|Tensoring is not always exact]], but we would like to know when it is.

##### _definition:_ flatness

An $A$-module $M$ is flat if the functor $\mathsf{Mod}_{A} \to \mathsf{Mod}_{A}$ by $N \mapsto M \otimes_{A} N$ is [[Algebraic geometry --- rising-sea/notes/Exact functors#_definition _ right-exact, left-exact, exact|exact]].

---

##### _example:_ localisations (of the base ring) are flat

Consider $S^{-1} A$ as an $A$-module. Since [[Algebraic geometry --- rising-sea/notes/Tensor products, categorically#_proposition _ tensoring commutes with direct sums|tensoring commutes with localisation]], $S^{-1} A \otimes N \cong S^{-1} N$. Then, since [[Algebraic geometry --- rising-sea/notes/Exact functors#_example _ localisation is exact|localisation is exact]], we have that tensoring with $S^{-1} A$ preserves exact sequences. That is, $S^{-1} A$ is flat.

---
