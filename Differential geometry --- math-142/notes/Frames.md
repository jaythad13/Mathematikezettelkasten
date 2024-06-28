---
tags: 
- diff-geo
- math-142/11
- math-142/16
---

What happens if we want to generalise the idea of the standard basis on $\mathbb{R}^3$? We get the idea of an [[Orthonormal bases#_definition _ orthonormal basis|orthonormal basis]]. But this only preserves properties with respect to the inner product. What if we want to preserve its properties with respect to the cross product as well? Then we get a frame.

### What's a frame?

##### _definition:_ frame, frame field

A frame field on $\mathbb{R}^3$ is a set of three [[The framework of differential geometry#_(re)definition _ vector field|vector fields]] $\mathbf{V}_{1}, \mathbf{V}_{2}, \mathbf{V}_{3}$ such that at every point $\mathbf{p} \in \mathbb{R}^3$ we have that $\mathbf{V}_{1}(\mathbf{p}), \mathbf{V}_{2}(\mathbf{p}), \mathbf{V}_{3}(\mathbf{p})$ is an [[Orthonormal bases#_definition _ orthonormal basis|orthonormal basis]] satisfying
$$
\begin{gathered}
\mathbf{V}_{1}(\mathbf{p}) \times \mathbf{V}_{2}(\mathbf{p}) = \mathbf{V}_{3}(\mathbf{p}) \\
\mathbf{V}_{2}(\mathbf{p}) \times \mathbf{V}_{3}(\mathbf{p}) = \mathbf{V}_{1}(\mathbf{p}) \\
\mathbf{V}_{3}(\mathbf{p}) \times \mathbf{V}_{1}(\mathbf{p}) = \mathbf{V}_{2}(\mathbf{p})
\end{gathered}
$$

At each point, $\mathbf{V}_{1}(\mathbf{p}), \mathbf{V}_{2}(\mathbf{p}), \mathbf{V}_{3}(\mathbf{p})$ form a frame. That is, a frame is a set of tangent vectors at a point $\mathbf{p}$ that form a 

Note that this motivates defining the norm of a vector field, and the dot product, cross product, and angle between two vector fields as functions that take points and spit out the respective values point-wise.

##### _example:_ the Euclidean frame field

The trivial example of a frame field just assigns the standard orthonormal basis on $\mathbb{R}^3$ to each point. That is, the Euclidean frame field is $\mathbf{U}_{1}, \mathbf{U}_{2}, \mathbf{U}_{3}$ with $\mathbf{U}_{i} = [\mathbf{e}_{i}, \mathbf{p}]$.

##### _example:_ cylindrical coordinates, spherical coordinates

The cylindrical coordinates that assign to each point $\hat{\mathbf{r}}, \hat{\boldsymbol{\theta}}, \hat{\mathbf{z}}$ and the spherical coordinates that assign $\hat{\mathbf{r}}, \hat{\boldsymbol{\theta}}, \hat{\boldsymbol{\varphi}}$ in the standard way are frame fields. This is an easy verification once you just look at their components. See the lecture notes for the details.