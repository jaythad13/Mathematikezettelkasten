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

Okay, but how do we choose the right frame to describe a particular problem? One example we can look at is if we have a curve that we care about.

### The natural frame for a curve

The best way to describe this is with a commutative diagram. Suppose we have a curve parameterised by $\alpha : I \to \mathbb{R}^3$. Then we can map $I$ onto the the [[Exact sequences#_example _ short exact sequence|short exact sequence]] associated with the tangent space in three ways.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& & I \ar[d, "\alpha'"] \ar[ld, "\alpha"] \ar[rd, "\frac{d \alpha}{dt}"] \\
		\{ \mathbf 0 \} \ar[r] & \mathbb R^3 \ar[r, "{\mathbf p \mapsto \mathbf 0_{\mathbf p}}"'] & \mathrm T \mathbb R^3 \ar[r, "\mathbf v_{\mathbf p} \mapsto \mathbf v"'] & \mathbb R^3 \ar[r] & \{ \mathbf 0 \}
	\end{tikzcd}
\end{document}
```

We only really care about $\alpha'$.

Recall the idea of reparameterisations. 

##### _proposition:_ you can go along any curve at unit speed

If $\alpha$ is a [[Curves#_definition _ regularity of a curve|regular curve]], there is an orientation preserving reparameterisation $\beta = \alpha \circ h$ such that $\lVert \beta'(\tau) \rVert = 1$ for all $\tau \in J$.

##### _proof:_

Consider the arc length $\tau$ given by
$$
	\tau(t) = \int_{t_{0}}^t \left \lVert \frac{d\alpha}{dt} \Big |_{u} \right \rVert \, du + \tau_{0}
$$
for some $\tau_{0} \in \mathbb{R}$.

Since $\alpha$ is regular, we have $\left \Vert \dfrac{d\tau}{dt} \right \Vert = \left \Vert \dfrac{d \alpha}{dt} \right \Vert \neq 0$, and thus, by [[Inverse and implicit functions#_theorem _ the inverse function theorem|the inverse function theorem]] we have a smooth inverse $h : J \to I$ ($J$ is some open subset of $\mathbb{R}$). Then we have
$$
\begin{split}
\frac{dh}{d\tau} & = \left ( \frac{d \tau}{d t} \right )^{-1} \\
& = \left \lVert \frac{d\alpha}{dt} \right \rVert^{-1} \\
& > 0
\end{split}
$$
and thus, $h : J \to I$ is a smooth function with $h'(\tau) > 0$ and $\beta = \alpha \circ h$ and thus, is an orientation preserving reparameterisation.

Finally we can calculate the velocity
$$
\begin{split}
\left \lVert \frac{d\beta}{dt} \right \rVert & = \left \lVert \frac{d\alpha}{dt} \frac{dh}{dt} \right \rVert \\
& = 1.
\end{split}
$$

Now we can go back to this diagram of our short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& & I \ar[d, "Y"] \ar[ld, "\alpha"] \ar[rd, "u"] \\
		\{ \mathbf 0 \} \ar[r] & \mathbb R^3 \ar[r, "{\mathbf p \mapsto \mathbf 0_{\mathbf p}}"'] & \mathrm T \mathbb R^3 \ar[r, "\mathbf v_{\mathbf p} \mapsto \mathbf v"'] & \mathbb R^3 \ar[r] & \{ \mathbf 0 \}
	\end{tikzcd}
\end{document}
```

Notice how although it's most natural to have $u = \dfrac{d\alpha}{dt}$, we don't have to, and if we use something different, then $Y$ doesn't have to be $\alpha'$ either. This leads to the definition of a vector field on a curve.

##### _definition:_ vector field on a curve

A vector field on a curve $\alpha$ is a map $Y : I \to \mathrm{T}\mathbb{R}^3$ such that the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		I \ar[d, "Y"] \ar[rd, "u"] \\
		\mathrm T \mathbb R^3 \ar[r, "\mathbf v_{\mathbf p} \mapsto \mathbf v"'] & \mathbb R^3
	\end{tikzcd}
\end{document}
```
