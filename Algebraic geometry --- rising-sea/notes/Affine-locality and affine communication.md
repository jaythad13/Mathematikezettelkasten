---
tags:
- rising-sea/5/3
- alg-geo
- comm-alg
---

Let $X$ be a scheme.

Often we have a property of schemes that is defined by requiring some property of all affine opens. However, because we don't have a definition of transition maps (as we do in the case of manifolds) we don't know how to communicate with them.

##### _lemma:_ Nike's lemma

Suppose $\operatorname{Spec} A, \operatorname{Spec} B \subseteq X$ are affine opens. Then $\operatorname{Spec} A \cap \operatorname{Spec} B$ is covered by open sets that are simultaneously distinguished in both $\operatorname{Spec} A$ and $\operatorname{Spec} B$.

---

##### _lemma:_ affine communication lemma

Let $P$ be a property of affine open subsets of a scheme $X$. Suppose, for any $\operatorname{Spec} A \subseteq X$, the following implications hold,
- If $\operatorname{Spec} A$ has property $P$, then, for any $f \in A$, $\operatorname{Spec} A_{f} \subseteq X$ has property $P$.
- If $(f_{1}, \dots, f_{n}) = A$, and each $\operatorname{Spec} A_{f_{i}} \subseteq X$ has property $P$, then $\operatorname{Spec} A$ has property $P$.
Then, if $X$ has a cover by affine opens with property $P$, every affine open of $X$ has property $P$.

---

##### _definition:_ affine-local

A property is **affine-local** if it satisfies the hypotheses of the affine communication lemma.

---

For example, reducedness is affine-local —

![[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_corollary _ affine-local characterisations of reduced schemes]]

Noetherianness of schemes is also affine local.