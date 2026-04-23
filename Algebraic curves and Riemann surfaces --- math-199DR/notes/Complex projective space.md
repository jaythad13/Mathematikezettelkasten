---
tags:
- math-199DR
- cx-geo
- alg-geo
---

In the study of Riemann surfaces, complex projective space plays an important role. We will define it as a complex manifold so that we can know what holomorphic maps to it are.

##### _definition:_ complex projective $n$-space

**Complex projective $n$-space** is the complex manifold $\mathbb{C} \mathbb{P}^n$ parameterising one-dimensional subspaces of $\mathbb{C}^{n + 1}$ and given by $\mathbb{C} \mathbb{P}^n = (\mathbb{C}^{n + 1} \setminus \{ 0 \}) / \mathbb{C}^\times$ with the [[Topology --- math-147/notes/Quotient and identification spaces#_definition _ quotient topology, quotient space, quotient map|quotient topology]]/

Points of $\mathbb{C} \mathbb{P}^n$ are written as $(x_{0} : x_{1} : \dots : x_{n})$ for the orbit of $(x_{0}, \dots, x_{n}) \in \mathbb{C}^{n + 1}$. 

$\mathbb{C}\mathbb{P}^n$ is covered by $n + 1$ open sets $U_{i} = \{ (x_{0} : \dots : x_{n}) \mid x_{i} \neq 0 \}$ with each $U_{i}$ homeomorphic to $\mathbb{C}^n$ by $(x_{0} : x_{1} : \dots : x_{n}) \mapsto (x_{0} / x_{i}, \dots, x_{n} / x_{i})$. They form a complex atlas.

---

Note that we can still cover $\mathbb{C} \mathbb{P}^n$ with the set of just those points with $x_{j} / x_{i} \leq 1$ in $U_{i}$. But then, $\mathbb{C} \mathbb{P}^n$ is covered by $n + 1$ compact discs, and thus, is compact itself.

$\mathbb{C} \mathbb{P}^n$ allows us to understand vanishing sets of homogeneous functions. If $f \in \mathbb{C}[x_{0}, \dots, x_{n}]$ is homogeneous, then it doesn't have well-defined values on $\mathbb{C} \mathbb{P}^n$ but whether it vanishes on $\mathbb{C} \mathbb{P}^n$ or not is well-defined.