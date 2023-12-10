---
tags:
- math-19
- calc
lecture: math-19-24
---

Recall [[Green's theorem#_theorem _ Green's theorem|Green's theorem]] for a planar vector field $\bvec F$. It tells us that we can convert the line integral along a closed curve $c$ in $\bb{R}^2$ to an area integral inside it: for $c$ oriented clockwise, and $c = \partial R$, for some region $R$, we have
$$
\oint_c \bvec{F} \cdot d\bvec{s} = \iint_D \curl \bvec{F} \, dA.
$$

We already know how [[Stokes' theorem#_theorem _ Stokes' theorem|Stokes' theorem]] allows us to generalise this to $2$-dimensional surfaces and vector fields on $\bb{R}^3$.

Gauss' divergence theorem allows us to bring a different intuition from $\bb{R}^3$ and formalise it in two and three dimensions. When we thought about flux integrals [[Stokes' theorem|last time]], we used the metaphor of fluid flow through a surface, and realised that the flux through a closed surface being positive forces us think about their being a "source" of the fluid at the point. But recall that when we learnt about [[Divergence and curl|divergence]] we used a similar metaphor and saw that [[Divergence and curl#Geometric intuitions for divergence and curl|positive divergence looks like a source]]!

Specifically, Gauss' divergence theorem formalises this by saying

##### _theorem:_ Gauss' divergence theorem

For a $\mathcal{C}^1$ vector field $\bvec{F}$ on $\bb{R}^2$, and a region $R$ with boundary, a closed curve, $\partial R$, we have
$$
\oint_{\partial R} \bvec{F} \cdot \bvec{n} \, ds = \iint_R \div \bvec{F} \, dA
$$
where $\bvec{n} \, ds$ is just the normal to the tangent to $\partial R$, oriented outwards.

For a $\mathcal{C}^1$ vector field $\bvec{F}$ on $\bb{R}^3$, and a region $W$ with boundary, a closed surface, $\partial W$, oriented outwards, we have
$$
\iint_{\partial W} \bvec{F} \cdot d\bvec{S} = \iiint_W \bvec{F} \, dV.
$$
##### _proof sketch:_

For the two-dimensional case, Gauss' divergence theorem follows directly from [[Green's theorem#_theorem _ Green's theorem|Green's theorem]]. 

For a vector field $\bvec{F}$ with $\bvec{F}(x, y) = (M(x, y), N(x, y))$, we can think of $\bvec{E} = \bvec{F} \cdot \bvec{n}$ - $\bvec E$ is $\bvec F$ rotated $90$ degrees exactly like $\partial R$ wants it to be. That is, $\bvec{E}(x, y) = (-N(x, y), M(x, y))$.

Thus,
$$
\begin{split}
\oint_{\partial R} \bvec{F} \cdot \bvec{n} \, ds & =\oint_{\partial R} \bvec{E} \cdot d\bvec{s} \\
&= \iint_R \curl \bvec E \, dA \\ 
&= \iint_R \pardx{M}{x} - \pardx{(-N)}{y} \, dA \\
&= \iint_R \pardx{M}{x} + \pardx{N}{y} \, dA \\
&= \iint_R \div \bvec{F} \, dA.
\end{split}
$$

The proof in three dimensions is more complicated, but follows from a similar idea to Stokes' theorem—divide the inside of $W$ into a bunch of cubes and note that the sum of the flux through any adjacent cubes is just the flux through their union. As these cubes get smaller and smaller, measuring the flux through a cube looks a lot like measuring the divergence at a point on the cube.

Specifically, for $\bvec{F} = (F_1, F_2, F_3)$, the flux through one of the faces can be written as
$$
(F_1(x + \Delta x, y, z) - F_1(x, y, z)) \cdot (\Delta y \Delta z, 0, 0) = \frac{F_1(x + \Delta x, y, z) - F_1(x, y, z)}{\Delta x} \Delta x \Delta y \Delta z
$$
which looks a lot like
$$
\pardx{F_1}{x} \, dV.
$$
Adding up the flux out of all of the surfaces of the box gives us something that looks like
$$
\Big ( \pardx{F_1}{x} + \pardx{F_2}{y} + \pardx{F_3}{z} \Big ) \, dV = \div \bvec{F} \, dV
$$
and in fact, turns out to be this in the limit.

##### _example:_ Gauss' theorem in action

What's the flux of $\bvec{F}(x, y, z) = (y^2, x e^z, z + \sin{x})$ through the unit $2$-sphere $\bb{S}^2$?

This would be horrific to compute as a flux integral, but Gauss' divergence theorem allows us to see that
$$
\begin{split}
	\iint_{\bb{S}^2} \bvec{F} \cdot d\bvec{S} &= \iiint_{\bb{B}^3} \div \bvec{F} \, dV \\
	& = \iiint_{\bb{B}^3} 1 \, dV \\
	& = \frac{4}{3} \pi
\end{split}
$$

We don't even need a trivial divergence for Gauss' theorem to do a lot of heavy lifting for us.

##### _example:_ Gauss' theorem in action, again

If we look at the surface $\mathcal S$ of the box $W = [0, 1] \times [0, 2] \times [0, 3]$ and the field $\bvec F(x, y, z) = (-y, x, z^2)$, calculating $\iint_{\mathcal S} \bvec{F} \cdot d\bvec{S}$ directly is horrific—it takes six different integrals. It's much easier to do the triple integral
$$
\iiint_W 2z \, dV
$$
instead.