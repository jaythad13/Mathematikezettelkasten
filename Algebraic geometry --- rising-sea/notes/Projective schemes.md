---
tags:
- rising-sea/4/5
- alg-geo
---

Basically any scheme you could care about (for non-pathological reasons) is projective or an open [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#Quasicompactness|quasicompact]] subset of a projective scheme (so quasiprojective). These are basically all the projective schemes cut out by homogeneous polynomials in [[Algebraic geometry --- rising-sea/notes/Examples of schemes#_definition _ projective $n$-space over a ring|projective space]] and their quasicompact opens.

### Real projective geometry and projective schemes informally

In smooth geometry and topology we think of $\mathbb{R} \mathbb{P}^n$ as the manifold parameterising the lines through the origin in $\mathbb{R}^{n + 1}$. If we think of $\mathbb{R}^{n + 1}$ as a ball, we can think of $\mathbb{R} \mathbb{P}^n$ as the bounding sphere with opposite points identified. Then $\mathbb{P}^{n + 1}$ is both, the ball $\mathbb{R}^{n + 1}$ and the bounding sphere $\mathbb{R} \mathbb{P}^n$.

Homogeneous equations in the $n + 1$ variables of $\mathbb{R}^{n + 1}$ cut out a closed union of lines in $\mathbb{R}^{n + 1}$ called the **affine cone** (of $V$), and a "variety" or "manifold" $V$ in $\mathbb{P}^n$. Finally the union of $V$ and its affine cone is the **projective cone** of $V$.

##### _example:_ a literal cone

$x^{2} + y^{2} = z^{2}$ cuts out a cone shape as its affine cone in $\mathbb{R}^3$, a copy of $\mathbb{R} \mathbb{P}^1 \cong S^1$ in $\mathbb{R} \mathbb{P}^2$, and their union looks like a closed compact cone in the ball.

---

### The $\operatorname{Proj}$ construction

The $\operatorname{Proj}$ construction constructs the projective scheme from any give affine cone specified by a [[Algebraic geometry --- rising-sea/notes/Graded rings#_definition _ $ mathbb{Z}$-graded rings, homogeneous elements, degree|graded ring]]. That is, $\operatorname{Proj} \mathbb{C}[x, y, z] / (x^{2} + y^{2} - z^{2})$ defines the scheme analogue of the subset of $\mathbb{C} \mathbb{P}^{2}$ cut out by $x^{2} + y^{2} = z^{2}$.