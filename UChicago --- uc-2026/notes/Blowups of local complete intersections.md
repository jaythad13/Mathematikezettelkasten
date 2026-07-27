---
tags:
- alg-geo
- uc-2026/conics/3
- altan-erdnigor
---

Blowups allow us to ignore the "bad" locus $Z \subseteq X$ of a scheme by conisdering the (birational) blowup $\operatorname{Bl}_{Z} X \to X$. This is very powerful because you can get a birational smooth $\widetilde{X} \to X$ from a sequence of blowups (this is Hironaka's celebrated resolution of singularities).

##### _example:_ blowing up affine space

The classic example is that $\operatorname{Bl}_{p} \mathbb{A}^{2} = \{ (p, \ell) \in \mathbb{A}^{2} \times \mathbb{P}^1 \mid p \in \ell \}$ where $\mathbb{P}^1$ is thought of as the moduli space of lines through $p$. If $C \subseteq \mathbb{A}^{2}$ is a curve with some singularity at the origin, then the closure of the preimage of $C \setminus \{ 0 \}$ is less singular. We call this the proper transform. For example, $V(y^{2} - x^{3} - x^{2})$ is singular in the plane, but has regular proper transform.

This generalises exactly to $\mathbb{A}^n$. Another way we can think of this is the following. Consider [[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_example _ affine $(n + 1)$-space covers projective $n$-space|the morphism]] $\mathbb{A}^n \setminus 0 \to \mathbb{P}^{n - 1}$, take its graph $X \subseteq \mathbb{A}^n \times \mathbb{P}^{n - 1}$ and take its closure.

---

##### _example:_ blowing up the projective plane

$\operatorname{Bl}_{p} \mathbb{P}^{2}$ is defined similarly as $\{ (p, \ell) \in \mathbb{P}^{2} \times \mathbb{P}^{2} \mid p \in \ell \}$ where the second $\mathbb{P}^{2}$ is thought of as the moduli space of projective lines in $\mathbb{P}^{2}$ through $p$. We can give a more general description.

Writing $U_{1} = \mathbb{A}^{2} \subseteq \mathbb{P}^{2}$ centred at $p$ and $U_{2} = \mathbb{P}^{2} \setminus p$. Then the blowup of $\mathbb{P}^{2}$ is just gluing together the blow up we $\operatorname{Bl}_{p} \mathbb{P}^{2} = \operatorname{Bl}_{0} U_{1} \cup_{U_{1} \setminus 0} U_{2}$ 

---

##### _definition:_ blowups of local complete intersections, exceptional divisor, proper transform

Suppose $X$ is an algebraic variety and $Z \subseteq X$ is a local complete intersection. For each $z \in Z$, let $U_{z} \subseteq X$ be an open neighbourhood satisfying $Z \cap U_{z} = V(f_{1}, \dots, f_{k})$. 

Then the **blowup of $U_{z}$ at $Z$** is
$$
\operatorname{Bl}_{Z \cap U_{z}} U_{z} = \left \{ (x, y) \in U_{z} \times \mathbb{P}^{k - 1} \mid \operatorname{rank} \begin{pmatrix}
f_{1}(x) & \cdots & f_{k}(x) \\
y_{1}  & \cdots & y_{k} 
\end{pmatrix} \leq 1 \right \}
$$
and the **blowup of $X$ at $Z$** is
$$
\operatorname{Bl}_{Z} X = \left( \bigcup_{z \in Z} \operatorname{Bl}_{Z \cap U_{z}} U_{z} \right) \cup (X \setminus Z)
$$
glued along the complement of $Z$.

$\pi : \operatorname{Bl}_{Z} X \to X$ is the **blowup morphism**. We say $E_{Z} X = \pi^\text{pre}(Z) \subseteq \operatorname{Bl}_{Z} X$ is the **exceptional divisor**.

The **proper transform** of a subvariety $Y \subseteq X$ is $\overline{\pi^\text{pre}(Y \setminus Z)}$. 

---

Note, for $p \in X$ we have
$$
\pi^\text{pre}(p) = \begin{cases}
\mathbb{P}^{k - 1} = \mathbb{P}(\mathscr{T}_{X, z} / \mathscr{T}_{Z, z}) = \mathbb{P}(\mathscr{N}_{Z \subseteq X, z}) & z \in Z \\
p & z \in X \setminus Z.
\end{cases}
$$