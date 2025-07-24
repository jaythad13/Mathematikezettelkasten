---
tags: 
- diff-geo
- math-142/2
---

Recall that the idea of a [[Curves and surfaces --- math-142/notes/The framework of differential geometry#_(re)definition _ vector field|vector field]] is that we should be able to figure how things move at every point $\mathbf{p} \in \mathbb{R}^3$.

### Decomposing vector fields

Last time we showed with an example that

##### _proposition:_ you can decompose vector fields

Every vector field $\mathbf{F}$ on $\mathbb{R}^3$ is given by
$$
\mathbf{F} = F_{1} \mathbf{U}_{1} + F_{2} \mathbf{U}_{2} + F_{3} \mathbf{U}_{3}
$$
for component functions $F_{1}, F_{2}, F_{3} : \mathbb{R}^3 \to \mathbb{R}$ and $\mathbf{U}_{i}(\mathbf{p}) = [\mathbf{e}_{1}, \mathbf{p}]$.

###### _proof:_

See [[Curves and surfaces --- math-142/notes/The framework of differential geometry#_examples _ decomposing vector fields|the example]].

##### _example:_ why care about vector fields?

Say we have a cylinder
$$
M = \{ (x, y, z) \in \mathbb{R}^3 : x^2 + y^2 = r^2, \lvert z \rvert \le h \}.
$$

It's natural to convert this to cylindrical coordinates with $x = r \cos \theta$, $y = r \sin \theta$, and then have the natural "basis"
$$
\begin{gathered}
\hat{r} = (\cos \theta, \sin \theta, 0) \\
\hat{\theta} = (-\sin \theta, \cos \theta, 0) \\
\hat{z} = (0, 0, 1).
\end{gathered}
$$
The problem is that these change at every point! A natural way to then think about them is as vector fields instead:
$$
\begin{gathered}
\hat{r} : \mathbf{p} \mapsto [(\cos \theta, \sin \theta, 0), \mathbf{p}] \\
\hat{\theta} : \mathbf{p} \mapsto [(-\sin \theta, \cos \theta, 0), \mathbf{p}] \\
\hat{z} : \mathbf{p} \mapsto [(0, 0, 1), \mathbf{p}].
\end{gathered}
$$
Now they define a changing "frame" at each point.

### Directional derivatives for vector fields

The [[Curves and surfaces --- math-142/notes/The framework of differential geometry#_definition _ tangent space at $ mathbf{p}$, $ mathrm{T}_{ mathbf{p}} mathbb{R} 3$ , tangent vectors|correspondence between tangent vectors and lines]] that we noticed last time allows us to think about directional derivatives as tangent vectors too! 

Basically, $[\mathbf{v}, \mathbf{p}] \in \mathrm{T}_{\mathbf{p}}\mathbb{R}^3$ corresponds to $\ell : [0, 1] \to \mathbb{R}^3$ by $t \mapsto \mathbf{p} + t \mathbf{v}$. Pick a smooth function $f : \mathbb{R}^3 \to \mathbb{R}$ and consider the composition $f \circ \ell : \mathbb{R} \to \mathbb{R}$. Then by the [[Differentiability theorems#_theorem _ chain rule|chain rule]], we have that it is differentiable, and we have its derivative as the directional (in direction $\mathbf{v}$) derivative at $\mathbf{p}$.

Specifically,

##### _definition:_ directional derivative

For a smooth function $f$ and $\ell$, the line associated to $[\mathbf{v}, \mathbf{p}] \in \mathrm{T}_{\mathbf{p}}\mathbb{R}^3$, the directional derivative of $f$ at $\mathbf{p}$ in the direction of $\mathbf{v}$ is
$$
\begin{split}
[\mathbf{v}, \mathbf{p}][f] &= \frac{d}{dt} (f \circ \ell) \Big |_{t = 0}  \\
& = Df \Big |_{\mathbf{p}} (\mathbf{v})
\end{split}
$$

##### _proposition:_ linearity and product rules for directional derivatives

For tangent vectors $[\mathbf{v}, \mathbf{p}]$ and $[\mathbf{w}, \mathbf{p}]$, smooth functions $f, g$, and scalars, $a, b \in \mathbb{R}$ we have
1) linearity in the tangent vectors: $(a [\mathbf{v}, \mathbf{p}] + b [\mathbf{w}, \mathbf{p}])[f] = a[\mathbf{v}, \mathbf{p}][f] + b[\mathbf{w}, \mathbf{p}][f]$
2) linearity in the functions: $[\mathbf{v}, \mathbf{p}][a f + bg] = a [\mathbf{v}, \mathbf{p}][f] + b [\mathbf{v}, \mathbf{p}][g]$
3) the Leibniz rule for functions: $[\mathbf{v}, \mathbf{p}][f g] = [\mathbf{v}, \mathbf{p}][f] \, g(\mathbf{p}) + f(\mathbf{p}) [\mathbf{v}, \mathbf{p}][g]$

###### _proof sketch:_

1) Follows from the fact that $Df \Big |_{\mathbf{p}}$ is a linear map.
2) Follows from the [[Differentiability theorems#_proposition _ sums are differentiable|linearity of the derivative]].
3) Follows from the [[Differentiability theorems#_corollary _ the multivariable product rule|product rule]].

How do we think about this for vector fields?

If a vector field $\mathbf{V}$ on $\mathbb{R}^3$ is given by $\mathbf{p} \mapsto [\mathbf{v}, \mathbf{p}]$, for any smooth $f : \mathbb{R}^3 \to \mathbb{R}$ we have $\mathbf{V}(\mathbf{p})[f] = Df \Big |_{\mathbf{p}}(\mathbf{v})$. Thus, we make the following definition.

##### _definition:_ $\mathbf{V}[f]$, derivation

$\mathbf{V}[ - ]$ is the map that sends smooth $f : \mathbb{R}^3 \to \mathbb{R}$ to a smooth function $\mathbf{V}[f] : \mathbb{R}^3 \to \mathbb{R}$ that sends $\mathbf{p} \mapsto \mathbf{V}(\mathbf{p})[f]$.

It is called the derivation of $f$ by $\mathbf{V}$.

Note that the smooth function is just taking the directional derivative of the function at a point in the direction of the vector field at that point.

##### _example:_ a trivial directional derivative

For any smooth $f$
$$
\mathbf{U}_{1}[f] = \pardx{f}{x}.
$$

##### _proposition:_ linearity and product rules for derivations

For vector fields on $\mathbb{R}^3$, $\mathbf{V}, \mathbf{W}$ smooth functions $f, g$, and scalars, $a, b \in \mathbb{R}$ we have
1) linearity in the vector fields: $(a \mathbf{V} + b \mathbf{W})[f] = a \mathbf{V} [f] + b \mathbf{W} [f]$
2) linearity in the functions: $\mathbf{V} [a f + bg] = a \mathbf{V} [f] + b \mathbf{V} [g]$
3) the Leibniz rule for functions: $\mathbf{V} [f g] = \mathbf{V}[f] \, g(\mathbf{p}) + f(\mathbf{p}) \, \mathbf{V}[g]$.

###### _proof sketch:_

Follows by applying the [[#_proposition _ linearity and product rules for derivations|linearity and product rules for derivations]] pointwise.

### Curves

Given the idea of movement that vector fields represent, it's also natural to think of paths in $\mathbb{R}^3$ and how fast we're moving along them. We should probably define what we mean by path.

##### _(temporary) definition:_ curves, paths in $\mathbb{R}^3$

For an open interval $I \subset \mathbb{R}$, and a (insert adjectives like smooth, rectifiable, et c.) function $\alpha : I \to \mathbb{R}^3$, the image $\alpha^\text{img}(I)$ is a curve.

##### _example:_ lines are curves

Given $\mathbf{p}$ and a direction $\mathbf{v} \in \mathbb{R}^3$ then the function $\ell : [0, 1] \to \mathbb{R}^3$ by $t \mapsto \mathbf{p} + t \mathbf{v}$, $\ell^\text{img}([0, 1])$ is a curve.