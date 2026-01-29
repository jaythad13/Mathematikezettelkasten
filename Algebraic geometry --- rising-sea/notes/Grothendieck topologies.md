---
tags:
- alg-geo
- cat-th
- rising-sea/6/2
---

Let $X$ be a scheme.

$X$ is covered by affine opens around every point, giving us a [[Algebraic geometry --- rising-sea/notes/Schemes#_proposition _ affine opens form a base|base of affine opens]]. However, the data of intersections of basic open sets is gnarly — we can have $\operatorname{Spec} B \subseteq \operatorname{Spec} A$ without $\operatorname{Spec} B$ necessarily distinguished in $\operatorname{Spec} A$. We want to restrict to just the data of the of the distinguished inclusions $\operatorname{Spec} A_{f} \subseteq \operatorname{Spec} A$. 

This is just one example of a Grothendieck topology, a generalised notion of topology that is just enough to define what sheaves are. We will be able to define Grothendieck topologies not only on individual schemes, but also on the whole category of schemes and general categories as well.

### The distinguished affine G-topology

##### _definition:_ the distinguished affine G-topology

The **distinguished affine G-topology** of $X$ is the data of affine opens and inclusions $\operatorname{Spec} A \subseteq X$ and only the inclusions of [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_definition _ distinguished open set, doesn't vanish set|distinguished opens]] $D(f) \subseteq \operatorname{Spec} A$.

For brevity we refer to this as the **distinguished affine base**.

---

Naturally, we want to define [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf, separated presheaf|sheaves]] on this. It turns out that doing this defines a sheaf on the normal Zariski topology of the scheme as well.

##### _proposition:_ Zariski topology is subordinate to distinguished affine topology

---

Thus, we can just define the values of sheaves on affine opens and their restrictions to distinguished subsets.

##### _example:_ the ideal sheaf of nilpotents

For any $f \in A$, there is an isomorphism of $A$-modules and $A_{f}$-modules $(\mathfrak{N}_{A})_{f} \cong \mathfrak{N}_{A_{f}}$. If $a^n = 0$ in $A$, then $a^n = 0$ in $A_{f}$ as well. That is, $a \in \mathfrak{N}_{A}$ implies $a / f \in \mathfrak{N}_{A_{f}}$. If $(a / f)^n = 0$ in $A_{f}$, then $f^m a^n = 0$ in $A$ and so $a f \in \mathfrak{N}_{A}$. We can write $a / f = af / f^{2} \in \mathfrak{N}_{A_{f}}$. 

Then, we can define the **ideal sheaf of nilpotents** by $\mathfrak{N}_{X}(\operatorname{Spec} A) = \mathfrak{N}_{A}$ on any scheme $X$. We just need to check that this is compatible under gluing. This is an application of [[Algebraic geometry --- rising-sea/notes/Affine-locality and affine communication#_lemma _ Nike's lemma|Nike's lemma]].

---

##### _example:_ the quasicoherent tensor product

Suppose $\mathscr{F}, \mathscr{G}$ are [[Algebraic geometry --- rising-sea/notes/Quasicoherent sheaves#_definition _ quasicoherent sheaves, $ mathsf{QCoh}_{X}$|quasicoherent]] sheaves. The assignment $\mathscr{F} \otimes \mathscr{G}(U) = \mathscr{F}(U) \otimes \mathscr{G}(U)$ is not a sheaf. However, applying Nike's lemma again shows that there is a unique sheaf defined by $\mathscr{F} \otimes \mathscr{G}(\operatorname{Spec} A) = \mathscr{F}(\operatorname{Spec} A) \otimes \mathscr{G}(\operatorname{Spec} A)$ and by the restrictions $\mathscr{F} \otimes \mathscr{G}(\operatorname{Spec} A) \to \mathscr{F} \otimes \mathscr{G}(D_{A}(f))$ given by localisation.

This satisfies the universal property of the tensor product, not only in $\mathsf{QCoh}_{X}$, but also in $\mathsf{Mod}_{\mathscr{O}_{X}}$. 

---