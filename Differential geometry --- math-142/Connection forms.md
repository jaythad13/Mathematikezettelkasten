---
tags:
- diff-geo
- math-142
lecture:
- math-142-17
- math-142-18
---

Recall that for the [[Frenet-Serret frames]], we can write the derivatives of each vector field as the a linear combination (with functions as coefficients) of the vector fields themselves —
$$
\begin{align}
\mathbf{T}' & =  & \kappa v \, \mathbf{N} \\
\mathbf{N}' & = -\kappa v \, \mathbf{T} & & &  + \tau v \, \mathbf{B} \\
\mathbf{B}' & = & -\tau v \mathbf{N}.
\end{align}
$$

Can we generalise this? Yes!

### Connection forms

In order to generalise this to [[Frames#_definition _ frame, frame field|frame fields]], we need to note that they are vector fields, and thus, there is no easy notion of $\mathbf{E}'$. Instead, we have to pick a vector field with respect to which we take the [[Covariant derivatives#_definition _ covariant derivative|covariant derivative]] — we look at the derivative of $\mathbf{E}$ as a function with just a vector part, and evaluate it along some reference field $\mathbf{V}$ at every point. Then,

##### _theorem, definition:_ the connection equations, the connection forms

For any frame field $\mathbf{E}_{1}, \mathbf{E}_{2}, \mathbf{E}_{3}$ and any vector field $\mathbf{V}$ there exist $1$-[[Differential 1-forms#_definition _ differential $1$-form, $ Omega 1( mathbb{R} 3)$|forms]] $\omega_{12}, \omega_{13}, \omega_{23}$ such that
$$
\begin{align} \\
\nabla_{\mathbf{V}} \mathbf{E}_{1} & = & \omega_{12}(\mathbf{V}) \, \mathbf{E}_{2}  & & - \omega_{31}(\mathbf{V}) \, \mathbf{E}_{3} \\
\nabla_{\mathbf{V}} \mathbf{E}_{2} & = -\omega_{12}(\mathbf{V}) \, \mathbf{E}_{1} & & & + \omega_{23}(\mathbf{V}) \,  \mathbf{E}_{3} \\
\nabla_{\mathbf{V}} \mathbf{E}_{3} & = \omega_{31}(\mathbf{V}) \, \mathbf{E}_{1} & - \omega_{23}(\mathbf{V}) \,  \mathbf{E}_{2}
\end{align}
$$
$\omega_{12}, \omega_{23}, \omega_{13}$ are called connection forms.

Note that for the vector field $\omega = \omega_{23}(\mathbf{V}) \, \mathbf{E}_{1} + \omega_{31}(\mathbf{V}) \, \mathbf{E}_{2} + \omega_{12}(\mathbf{V}) \, \mathbf{E}_{3}$, this is equivalent to
$$
\nabla_{\mathbf{V}}\mathbf{E}_{i} = \omega \times \mathbf{E}_{i} 
$$

###### _proof sketch:_

%% do rigorously later %%

Let $\omega_{ij}$ be defined by
$$
\omega_{ij}(\mathbf{V}) : \begin{cases}
\mathbb{R}^3 \to \mathbb{R} \\
\mathbf{p} \mapsto(\nabla_{\mathbf{V}} \mathbf{E}_{i}(\mathbf{p})) \cdot \mathbf{E}_{j}
\end{cases}
$$
for any vector field $\mathbf{V}$.

Then note that $\omega_{ij}$ is a $1$-form — it is linear in its inputs, and we can define it for any input tangent vector. To see linearity just evaluate $\omega_{ij}(\mathbf{W})$ for $\mathbf{W} =  f \, \mathbf{U} + g \, \mathbf{V}$ and chase through. This gives us nine $1$-forms. We will show that we only need to care about three.

Note that $\omega_{ij} = -\omega_{ji}$ — just use [[Covariant derivatives#_proposition _ the Leibniz rule for covariant derivatives|the product rule for covariant derivatives]] on $\mathbf{V}[\mathbf{E}_{i} \cdot E_{\mathbf{j}}]$. Thus, we get $\omega_{ii} = 0$.

Finally, to get the actual statement, just notice that since $\mathbf{E}_{1}, \mathbf{E}_{2}, \mathbf{E}_{3}$ is an [[Orthonormal bases|orthonormal basis]] on the space of vector fields, we can get each $\nabla_{\mathbf{V}}\mathbf{E}_{i}$ as a linear combination of the basis by dotting (the dot product is actually a smooth function that takes points $\mathbf{p}$ to coefficients in $\mathbb{R}$). That dot product is exactly the corresponding $1$-form evaluated on $\mathbf{V}$.

##### _example:_ connections on the cylindrical frame field

Recall the cylindrical frame field with vector fields $\hat{\mathbf{r}}, \hat{\boldsymbol{\theta}}, \hat{\mathbf{z}}$. We claim that the only non-zero connection form is $\omega_{12} = d\vartheta$. Here $\vartheta$ is the smooth function by $(x, y, z) \mapsto \arctan(y/x)$. 

We can see this by noticing that for a vector field $\mathbf{V} : \mathbf{p} \mapsto [(v_{1}, v_{2}, v_{3}), \mathbf{p}]$, we must have
$$
\begin{split}
\nabla_{\mathbf{V}} \hat{\mathbf{r}} & = \frac{x v_{2} - y v_{1}}{x^2 + y^2} \hat{\boldsymbol{\theta}} \\
 & = \frac{{x \, dy(\mathbf{V}) - y \, dx(\mathbf{V})}}{x^2 + y^2} \hat{\boldsymbol{\theta}}
\end{split}
$$
But $d\vartheta$ is just that differential form. We can show this by
$$
\begin{split}
d\vartheta & = \frac{ \partial \vartheta }{ \partial x } dx + \frac{ \partial \vartheta }{ \partial y } dy \\
 & = \frac{1}{1 + \left(\frac{y}{x} \right)^2} \left( -\frac{y}{x^2} \right) dx + \frac{1}{1 + \left( \frac{y}{x} \right)^2} \left( \frac{1}{x} \right) dy  \\
  & = \frac{{ - y \, dx + x \, dy }}{x^2 + y^2}
\end{split}
$$

Note that $\vartheta$ is not defined consistently everywhere (for example, it is undefined everywhere $x = 0$) and $d\vartheta$ has a hole wherever $x = y = 0$. Thus, this is not technically wrong, but on open connected sets, not containing the origin, and with the right sign orientation, this works.

### Computing connection forms

While the example of the cylindrical frame field is easy because it pops right out when you compute stuff, how would you do this in general? Unfortunately there isn't anything much better than computing
$$
\omega_{ij} = (\nabla_{\mathbf{V}} \mathbf{E}_{i}) \cdot \mathbf{E}_{j}
$$
directly every time. For $\mathbf{V} = [(v_{1}, v_{2}, v_{3}), \mathbf{p}]$, note that we can replace each instance of $v_{i}$ by $dx_{i}(\mathbf{V})$ in order to get a more general 