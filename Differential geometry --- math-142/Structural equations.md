---
tags:
- diff-geo
- math-142
lecture:
- math-142-18
---

Recall how whenever we wanted to identify the cross product with wedge product, we said we'd just [[The exterior derivative#A special case the curl|slap a Hodge star on it]]? We're going to do this again to write the [[Connection forms#_theorem, definition _ the connection equations, the connection forms|the connection equation]] $\nabla_{\mathbf{V}} \mathbf{E}_{i} = \omega \times \mathbf{E}_{i}$ in the language of differential forms.

### Dual $1$-forms

To do so, we need some special $1$-forms.

##### _definition:_ dual $1$-forms

Say $\mathbf{E}_{1}, \mathbf{E}_{2}, \mathbf{E}_{3}$ is a frame field. The dual $1$-forms $\theta_{1}, \theta_{2}, \theta_{3} \in \Omega^1(\mathbb{R}^3)$ are those $1$-forms defined by
$$
\theta_{i}(\mathbf{V})(\mathbf{p}) = \mathbf{V}(\mathbf{p}) \cdot \mathbf{E}_{i}(\mathbf{p})
$$
for any vector field $\mathbf{V}$.

Note that this is equivalent to
$$
\theta_{i}[\mathbf{v}, \mathbf{p}] = \mathbf{E}_{i}(\mathbf{p})^\vee
$$
for any tangent vector $[\mathbf{v}, \mathbf{p}]$.

These are special in the following ways.

##### _proposition:_ the dual $1$-forms really are [[Dual spaces|dual]]

For any frame field $\mathbf{E}_{1}, \mathbf{E}_{2}, \mathbf{E}_{3}$ and corresponding dual $1$-forms $\theta_{1}, \theta_{2}, \theta_{3}$ we have
$$
\mathbf{E}_{i} = \sum_{j = 1}^3 \theta_{i}(\mathbf{U}_{j}) \cdot \mathbf{U}_{j}
$$
and
$$
\theta_{i}(\mathbf{E}_{j}) = \delta_{ij}.
$$

##### _proof sketch:_

The first part follows from $\theta_{i}(\mathbf{U}_{j}) = \mathbf{U}_{j} \cdot \mathbf{E}_{i}$ and the fact that $\mathbf{U}_{1}, \mathbf{U}_{2}, \mathbf{U}_{3}$ is an orthonormal basis of vector fields.

The second part is similar — it follows from $\theta_{i}(\mathbf{E}_{j}) = \mathbf{E}_{j} \cdot \mathbf{E}_{i}$ and the fact that $\mathbf{E}_{1}, \mathbf{E}_{2}, \mathbf{E}_{3}$ is an orthonormal basis of vector fields.

##### _proposition:_ dual expansion

For any vector field $\mathbf{V}$ we have
$$
\mathbf{V} = \sum_{i = 1}^3 \theta_{i}(\mathbf{V}) \, \mathbf{E}_{i}
$$
and any $1$-form $\phi$ we have
$$
\phi = \sum_{i = 1}^3 \phi(\mathbf{E}_{i}) \, \theta_{i}
$$

##### _proof sketch:_

The first part follows from $\theta_{i}(\mathbf{V}) = \mathbf{V} \cdot \mathbf{E}_{i}$ and the fact that $\mathbf{E}_{1}, \mathbf{E}_{2}, \mathbf{E}_{3}$ is an orthonormal basis of vector fields.

The second part follows from the fact that $\phi$ is defined by how it acts on vector fields. If you want to be fancy, you can think of this as the double dual isomorphism reducing to the dual to double dual isomorphism. Basically, $\theta_{1}, \theta_{2}, \theta_{3}$ is a basis of the vector space of $1$-forms, and so to find the coefficients of a one form with respect to the basis, you need to "dot with $\theta_{i}$" which has the meaning, evaluate at $\mathbf{E}_{i}$ because of the natural double dual isomorphism.

### Structural equations

How are the dual $1$-forms related to the connection forms?

##### _theorem:_ Cartan's structural equations (due to Elie Cartan)

For any frame field, $\mathbf{E}_{1}, \mathbf{E}_{2}, \mathbf{E}_{3}$
$$
d\theta_{i} = \sum_{j = 1}^3 \omega_{ij} \wedge \theta_{j}
$$
and
$$
d\omega_{ij} = \sum_{k = 1}^3 \omega_{ik} \wedge \omega_{kj}.
$$

