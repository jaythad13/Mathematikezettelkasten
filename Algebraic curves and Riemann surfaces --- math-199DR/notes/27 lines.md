---
tags:
- uc-2026/enum-geo/3
- alg-geo
- cx-geo
- sidhant-raman
---

Let $X = V(f) \subseteq \mathbb{C} \mathbb{P}^3$ be a smooth cubic surface. Then no matter what $f$ is, $X$ contains $27$ lines. We use exactly the same trick as we did for the [[Algebraic curves and Riemann surfaces --- math-199DR/notes/The degree-genus formula#A proof by degenerations|the degree-genus formula]] — we show it for one and conclude that it is true for all.

The Fermat cubic has lots of symmetries

##### _lemma:_ lines on the Fermat cubic

The **Fermat cubic $V(w^{3} + x^{3} + y^{3} + z^{3}) \subseteq \mathbb{C} \mathbb{P}^{3}$** contains exactly $27$ lines.

###### _proof sketch:_

The lines are $V(w + x, y + z)$ and all scalings each variable by $\omega = e^{2 \pi i / 3}$.

---

##### _theorem:_ 27 lines on a cubic surface

Every smooth cubic surface $X \subseteq \mathbb{C} \mathbb{P}^3$ contains exactly $27$ lines.

###### _proof:_

Recall $\mathscr{H}_{3, 3}$ is the [[Algebraic curves and Riemann surfaces --- math-199DR/notes/The degree-genus formula#_definition _ the parameter space of degree $d$ hypersurfaces|parameter space]] of smooth cubic surfaces in $\mathbb{C} \mathbb{P}^{3}$. Informally, we want to show that the function $\mathscr{H}_{3, 3} \to \mathbb{Z}$ by $X \mapsto \#\{\text{lines on } X\}$ is continuous, thus, locally constant, and finally, constant.

Let $\operatorname{Gr}(1, \mathbb{C} \mathbb{P}^{3})$ denote the Grassmannian of projective lines $\mathbb{C}\mathbb{P}^1$ linearly embedded in $\mathbb{C} \mathbb{P}^3$. It is the same as $\operatorname{Gr}(2, \mathbb{C}^4)$. Consider the subset $Z \subseteq \mathscr{H}_{3, 3} \times \operatorname{Gr}(2, \mathbb{C}^4)$ consisting of $(X, \ell)$ such that $\ell \subseteq X$, with the projection $\pi : Z \to \mathscr{H}_{3, 3}$ by $(X, \ell) \mapsto X$. It suffices to understand the fibres of this map. In particular, we want to understand $\mathscr{H}_{3, 3} \to \mathbb{Z}$ by $X \mapsto \# \pi^\text{pre}(X)$.

It suffices to show that $Z \to \mathscr{H}_{3, 3}$ is a local diffeomorphism — this implies that it is a proper submersion of equidimensional submersion spaces. Then Ehresmann's theorem tells you that it is a fibre bundle with dimension $0$ fibres, or just a cover. Since $\mathscr{H}_{3, 3}$ is path-connected, the dimensions of the fibres are connected.

First we need to show that $Z$ is actually a subvariety. We find a polynomial and check that the hypotheses of the implicit function theorem are satisfied for the implicit function giving a line in a neighbourhood of a surface. This telss us exactly what we wanted to know.

---