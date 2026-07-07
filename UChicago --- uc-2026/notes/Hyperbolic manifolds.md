---
tags:
- uc-2026/ggt/1
- ben-lowe
- ggt
- diff-geo
---

##### _definition:_ complete hyperbolic $3$-fold

A **complete hyperbolic $3$-fold** is a quotient Riemannian manifold $X = \Gamma \setminus \mathbb{H}^{3}$ for a discrete subgroup $\Gamma \leq \mathrm{PSL}_{2}(\mathbb{C})$ acting [[Abstract algebra --- math-171/notes/Group actions#_definition _ stabiliser, free|freely]].

---

Note that by covering space theory, we have $\pi_{1}(\Gamma \setminus \mathbb{H}^{3}) \cong \Gamma$.

##### _example:_ a simple arithmetic subgroup

Consider
$$
\Gamma = \left \{ \begin{pmatrix}
1 & a + bi \\
0 & 1
\end{pmatrix} \mid a, b \in \mathbb{Z} \right \} \cong \mathbb{Z}[i] \cong \mathbb{Z}^{\oplus 2}. 
$$
Since we're quotienting $X = \Gamma \setminus \mathbb{C} \times \mathbb{R}_{\geq 0}$, topologically $X$ is a product of tori $\mathbb{T}^{2} \times \mathbb{R}_{\geq 0}$. However, because of the metric we have, these tori should get smaller as we go up (as $z \in \mathbb{R}_{\geq 0}$ gets bigger).

---