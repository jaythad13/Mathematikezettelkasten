---
tags:
 - diff-geo
 - math-142/15
---

Covariant derivatives generalise the notion of a [[Curves and surfaces --- math-142/notes/Vector fields#_definition _ $ mathbf{V}[f]$, derivation|directional derivative on a vector field]]. They allow us to do to a vector field what the directional derivative on a vector field does to a function.

##### _definition:_ covariant derivative

Say $\mathbf{V}, \mathbf{W} : \mathbb{R}^3 \to \mathrm{T}\mathbb{R}^3$ are vector fields with $\mathbf{W} = w_{1} \mathbf{U}_{1} + w_{2} \mathbf{U}_{2}, w_{3} \mathbf{U}_{3}$ and $w = (w_{1}, w_{2}, w_{3})$. Then, the covariant derivative of $\mathbf{W}$ with respect to $\mathbf{V}$ is 
$$
\nabla_{\mathbf{V}} \mathbf{W}(\mathbf{p}) = Dw \Big |_{\mathbf{p}} (\mathbf{V}(\mathbf{p}))
$$

Notice that what you're doing here is basically just treating $\mathbf{W}$ like a function $\mathbb{R}^3 \to \mathbb{R}^3$.

##### _example:_ covariant derivatives

Say $\mathbf{V} : \mathbf{p} \mapsto [(y - x, 0, xy), \mathbf{p}]$ and $\mathbf{W} : \mathbf{p} \mapsto [(x^{2}, 0, yz), \mathbf{p}]$ for all $\mathbf{p} = (x, y, z) \in \mathbb{R}^3$. Then we have the Jacobian
$$
\mathcal{M}(Dw \Big |_{\mathbf{p}}) = \begin{bmatrix}
2x & 0 & 0 \\
0 & 0 & 0 \\
0 & z & y
\end{bmatrix}.
$$
Thus,
$$
\nabla_{\mathbf{V}} \mathbf{W}(\mathbf{p}) = [(2x(y - x), xy^2), \mathbf{p}].
$$

The covariant derivative has all the properties of a good derivative —

##### _proposition:_ the covariant derivative is linear

Let $\mathbf{U}, \mathbf{V}, \mathbf{W}, \mathbf{Z} : \mathbb{R}^3 \to \mathrm{T}\mathbb{R}^3$ be vector fields, $f, g$ be smooth functions in $\mathcal{C}^\infty(\mathbb{R}^3)$ and $a, b \in \mathbb{R}$.

Suppose $\mathbf{X} = f\mathbf{U} + g \mathbf{V}$ and $\mathbf{Y} = a \mathbf{W} + \mathbf{b} \mathbf{Z}$. Then we have linearity in the "first slot" over $\mathcal{C}^\infty(\mathbb{R}^3)$ —
$$
\nabla_{\mathbf{X}} \mathbf{W} = f \nabla_{\mathbf{U}} + g \nabla_{\mathbf{V}} \mathbf{W} 
$$
and linearity in the second slot over $\mathbb{R}$ —
$$
\nabla_{\mathbf{V}} \mathbf{Y} = a \nabla_{\mathbf{V}} \mathbf{W} + b \nabla_{\mathbf{V}} \mathbf{Z}.
$$

###### _proof:_

For the first part, we just chase through the equations using the fact that the derivative of a smooth function $w : \mathbb{R}^3 \to \mathbb{R}^3$ at a point is a linear map —
$$
\begin{split}
\nabla_{\mathbf{V}}\mathbf{W}(\mathbf{p}) & = Dw \Big |_{\mathbf{p}}(f(\mathbf{p}) \mathbf{U}(\mathbf{p}) + g(\mathbf{p}) \mathbf{V}(\mathbf{p})) \\
 & = f(\mathbf{p}) Dw \Big |_{\mathbf{p}} (\mathbf{U}(\mathbf{p})) + g(\mathbf{p})Dw \Big |_{\mathbf{p}} (\mathbf{V}(\mathbf{p})) \\
 & = f(\mathbf{p}) \nabla_{\mathbf{U}} \mathbf{W}(\mathbf{p}) + g(\mathbf{p}) \nabla_{\mathbf{V}} \mathbf{W}(\mathbf{p})
\end{split}
$$
The second part follows just by the linearity of the derivative — $D(aw + bz) \Big |_{\mathbf{p}} = a Dw \Big |_{\mathbf{p}} + bDz \Big |_{\mathbf{p}}$


##### _proposition:_ the Leibniz rule for covariant derivatives

Say $\mathbf{V}, \mathbf{W}, \mathbf{Z} : \mathbb{R}^3 \to \mathrm{T}\mathbb{R}^3$ are vector fields and $f \in \mathcal{C}^\infty(\mathbb{R}^3)$ is a smooth function. Then we have
$$
\nabla_{\mathbf{V}}(f\mathbf{W}) = \mathbf{V}[f] \mathbf{W} + f \nabla_{\mathbf{V}} \mathbf{W}
$$
and
$$
\mathbf{V}[\mathbf{W} \cdot \mathbf{Z}] = (\nabla_{\mathbf{V}} \mathbf{W}) \cdot \mathbf{Z} + \mathbf{W} \cdot (\nabla_{\mathbf{V}} \mathbf{Z})
$$

###### _proof:_

%% see lecture notes, then do it yourself %%