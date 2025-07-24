---
tags:
- diff-geo
- math-142/18
- math-142/19
---

Recall how whenever we wanted to identify the cross product with wedge product, we said we'd just [[Curves and surfaces --- math-142/notes/The exterior derivative#A special case the curl|slap a Hodge star on it]]? We're going to do this again to write the [[Curves and surfaces --- math-142/notes/Connection forms#_theorem, definition _ the connection equations, the connection forms|the connection equation]] $\nabla_{\mathbf{V}} \mathbf{E}_{i} = \omega \times \mathbf{E}_{i}$ in the language of differential forms.

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

###### _proof sketch:_

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

###### _proof sketch:_

The first part follows from $\theta_{i}(\mathbf{V}) = \mathbf{V} \cdot \mathbf{E}_{i}$ and the fact that $\mathbf{E}_{1}, \mathbf{E}_{2}, \mathbf{E}_{3}$ is an orthonormal basis of vector fields.

The second part follows from the fact that $\phi$ is defined by how it acts on vector fields. If you want to be fancy, you can think of this as the double dual isomorphism reducing to the dual to double dual isomorphism. Basically, $\theta_{1}, \theta_{2}, \theta_{3}$ is a basis of the vector space of $1$-forms, and so to find the coefficients of a one form with respect to the basis, you need to "dot with $\theta_{i}$" which has the meaning, evaluate at $\mathbf{E}_{i}$ because of the natural double dual isomorphism.

### Structural equations

How are the dual $1$-forms related to the connection forms? We should expect there to be a "dual version" of the [[Curves and surfaces --- math-142/notes/Connection forms#_theorem, definition _ the connection equations, the connection forms|connection equations]].

##### _example:_ the structural equations for the cylindrical frame field

Let's use our favourite example of the cylindrical frame field, $\hat{\mathbf{r}}, \hat{\boldsymbol{\theta}}, \hat{\mathbf{z}}$, again remembering to be careful about the converse of $d^2 = 0$. We have dual forms
$$
\begin{split}
\theta_{1} & = \frac{x}{r} \, dx + \frac{y}{r} \, dy \\
\theta_{2} & = \frac{- y}{r} \, dx + \frac{x}{r} \, dy \\
\theta_{3} & = dz
\end{split}
$$
where $r$ is shorthand for $\sqrt{ x^2  + y^{2}}$.

Obviously, $d \theta_{3} = 0$ since $d^2 = 0$. We claim that $d\theta_{1} = 0$ as well and 
$$
d\theta_{2} = \frac{1}{r} \, dx \wedge dy.
$$

[[Curves and surfaces --- math-142/notes/Connection forms#_example _ connections on the cylindrical frame field|We have already computed]] that the connection forms are all $0$ except for $\omega_{12} = d\vartheta$. We claim that we also have $d \omega_{12} = 0$ and thus, $d\omega_{ij}$ is always $0$.

Then notice that
$$
\begin{split}
d\theta_{2} & = - \omega_{12} \wedge \theta_{1} + \omega_{23} \wedge \theta_{3} \\
 & = - \left( \frac{x}{r^2} \, dy - \frac{y}{r^2} \, dx \right) \wedge \left( \frac{x}{r} \, dx + \frac{y}{r} \, dy \right) \\
 & = \frac{r^2}{r^3} \, dx \wedge dy \\
 & = \frac{1}{r} \, dx \wedge dy.
\end{split}
$$

##### _theorem:_ Cartan's structural equations

For any frame field, $\mathbf{E}_{1}, \mathbf{E}_{2}, \mathbf{E}_{3}$
$$
d\theta_{i} = \sum_{j = 1}^3 \omega_{ij} \wedge \theta_{j}
$$
and
$$
d\omega_{ij} = \sum_{k = 1}^3 \omega_{ik} \wedge \omega_{kj}.
$$

###### _proof sketch:_

Lots of backbreaking determinant computation. See the lecture notes (or if you can think of a nicer way to do this).

Why would we care to do this backbreaking computation? Why did we care to do all the crazy cross products for [[Curves and surfaces --- math-142/notes/Connection forms|connection forms]], and [[Curves and surfaces --- math-142/notes/Frenet-Serret frames]] and in [[Curves and surfaces --- math-142/attachments/homework/hw 5/hw 5.pdf|the homework]]?

The idea is that as long as you know some limited information — $\mathbf{V}[f_{i}]$ for each component $f_{i}$ of a vector field $\mathbf{W}$, we can compute $\nabla_{\mathbf{V}}\mathbf{W}$, and similarly for derivatives of $1$-forms $\phi$.