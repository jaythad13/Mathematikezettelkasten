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

###### _proof:_

We will give a simultaneously distinguished open neighbourhood for each point in $\operatorname{Spec} A \cap \operatorname{Spec} B$. Suppose $p \in \operatorname{Spec} A \cap \operatorname{Spec} B$. Then, since the distinguished opens form a base, we can choose some $f \in A$ such that $p \in D_{A}(f) \subseteq \operatorname{Spec} A \cap \operatorname{Spec} B$. Further, we can choose some $g \in B$ such that $p \in D_{B}(g) \subseteq D_{A}(f)$. We claim this $D_{B}(g)$ is a simultaneously distinguished open neighbourhood.

Since $D_{A}(f) \subseteq \operatorname{Spec} B$, we have a restriction map with $g \mapsto g'$ say. We claim $D_{B}(g) = D_{A_{f}}(g')$. This follows because the points where $g \in \mathscr{O}_{X}(\operatorname{Spec} B)$ doesn't vanish are all contained in $D_{A}(f) = \operatorname{Spec} A_{f}$ (since $D_{B}(g) \subseteq D_{A}(f)$), but then the points where $g$ vanishes in $D_{A}(f) = \operatorname{Spec} A_{f}$ are exactly $D_{A_{f}}(g')$. Finally, for $g' = g'' / f^m$ we have $D_{A_{f}}(g') = D_{A}(fg'')$.

---

##### _lemma, definition:_ affine communication lemma, affine-local

Let $P$ be a property of affine open subsets of a scheme $X$. Suppose that for any $\operatorname{Spec} A \subseteq X$, the following implications hold.
1) If $\operatorname{Spec} A$ has property $P$, then, for any $f \in A$, $\operatorname{Spec} A_{f} \subseteq X$ has property $P$.
2) If $(f_{1}, \dots, f_{n}) = A$, and each $\operatorname{Spec} A_{f_{i}} \subseteq X$ has property $P$, then $\operatorname{Spec} A$ has property $P$.
Then, if $X$ has a cover by affine opens with property $P$, every affine open of $X$ has property $P$.

A property is **affine-local** if it satisfies the hypotheses of the affine communication lemma.

###### _proof:_

Suppose $X = \bigcup_{i = 1}^n \operatorname{Spec} A_{i}$ with all $\operatorname{Spec} A_{i}$ having property $P$. Then cover each $\operatorname{Spec} B \cap \operatorname{Spec} A_{i}$ with affine opens simultaneously distinguished in both, and thus, having property $P$ by the first hypothesis. Thus, $\operatorname{Spec} B$ is covered with distinguished opens. each having property $P$. Reduce to finitely many distinguished opens by [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_corollary _ every affine scheme is quasicompact|quasicompactness]]. It follows that $\operatorname{Spec} B$ has property $P$ by the second hypothesis.

---

For example, reducedness and any other stalk-local property is affine-local —

![[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_corollary _ affine-local characterisations of reduced schemes]]

Noetherianness of schemes is also affine local.