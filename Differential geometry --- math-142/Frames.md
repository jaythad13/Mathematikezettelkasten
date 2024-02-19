---
tags: 
- math-142
- diff-geo
lecture:
- math-142-11
---

What happens if we want to generalise the idea of the standard basis on $\mathbb{R}^3$? We get the idea of an [[Orthonormal bases#_definition _ orthonormal basis|orthonormal basis]]. But this only preserves properties with respect to the inner product. What if we want to preserve its properties with respect to the cross product as well? Then we get a frame.

### What's a frame?

##### _definition:_ frame

A frame on $\mathbb{R}^3$ is a set of three [[The framework of differential geometry#_(re)definition _ vector field|vector fields]] $\mathbf{V}_{1}, \mathbf{V}_{2}, \mathbf{V}_{3}$ such that at every point $\mathbf{p} \in \mathbb{R}^3$ we have that $\mathbf{V}_{1}(\mathbf{p}), \mathbf{V}_{2}(\mathbf{p}), \mathbf{V}_{3}(\mathbf{p})$ is an [[Orthonormal bases#_definition _ orthonormal basis|orthonormal basis]] satisfying
$$
\begin{gathered}
\mathbf{V}_{1}(\mathbf{p}) \times \mathbf{V}_{2}(\mathbf{p}) = \mathbf{V}_{3}(\mathbf{p}) \\
\mathbf{V}_{2}(\mathbf{p}) \times \mathbf{V}_{3}(\mathbf{p}) = \mathbf{V}_{1}(\mathbf{p}) \\
\mathbf{V}_{3}(\mathbf{p}) \times \mathbf{V}_{1}(\mathbf{p}) = \mathbf{V}_{2}(\mathbf{p})
\end{gathered}
$$

##### _example:_ polar coordinates, spherical coordinates

The polar coordinates that assign to each point $\hat{\mathbf{r}}, \hat{\boldsymbol{\theta}}, \hat{\mathbf{z}}$ and the spherical coordinates that assign $\hat{\mathbf{r}}, \hat{\boldsymbol{\theta}}, \hat{\boldsymbol{\varphi}}$ in the standard way are frame fields. This is an easy verification once you just look at their components.

