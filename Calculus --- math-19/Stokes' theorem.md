---
tags:
- math-19
- calc
lecture: math-19-23
---

(Hopefully) we remember [[Surface/flux integrals|what surface integrals are]] and [[Computing surface integrals|how to compute them]]. 

One good metaphor for flux integrals is fluid flow. We can think of any vector field $\bvec{F}$ as the velocity field of a fluid, and the flux through a surface $\mathcal S$ is then the volume of water flowing through $\mathcal S$ in unit time. This helps us make sense of the dependence of flux on the angle between $\bvec{F}$ and $d\bvec{S}$ (which has the direction of the normal vector to $\mathcal S$).

This metaphor leads us to realise we have a closed surface (oriented with outward normal), then the flux through it can only be positive if there's a water source somewhere inside it. Similarly, the flux can only be negative if there's a sink inside the surface.

We know how to parameterise and formally solve these surface integrals, but how do we formalise our intuition about sinks inside them?

Let's look at an example.

##### _example:_ 

$\bvec{F} = (0, 0, k)$, where $k$ is constant. What is its flux through a hemisphere of radius $R$, $\mathcal S$?

We can write this as the surface integral, parameterise $\mathcal S$ in spherical coordinates and then integrate.
$$
\begin{split}
\iint_{\mathcal S} \bvec{F} \cdot d\bvec{S} & = \int_0^{\pi/2} \int_0^{2 \pi} (0, 0, k) \cdot (\sin{\phi} \cos{\theta}, \sin{\phi} \sin{\theta}, \cos{\phi}) \, R^2 \, \sin{\phi }\, d\theta \, d\phi \\
& = k R^2 \int_0^{\pi/2} \int_0^{2 \pi} \sin{\phi} \cos{\phi} \, d\theta \, d\phi \\
& = 2 k \pi R^2 \int_0^{\pi/2} \frac{\sin{2 \phi}}{2} \, d\phi \\
& = k \pi R^2 (- \frac{\cos{2 \phi}}{2}) \Big |_0^{\pi/2} \\
& = k \pi R^2.
\end{split}
$$

If we think about $\bvec{F}$ as the velocity field of a fluid, then we can see that the answer only depends on the magnitude of the velocity and the area of the opening of the hemisphere (the area of the disk of radius $R$). 

But if we think about integrating over the surface of the whole sphere it's just as clear that the flux is zero - in fact we have a bijection between points in the upper hemisphere and points in the lower hemisphere with equal magnitude fluid flow, but in opposite directions.

Stokes' theorem formalises both of these.

##### _theorem:_ Stokes' theorem

If $\mathcal S$ is a surface with boundary $\partial \mathcal S$, oriented by the right hand rule, and $\bvec{F}$ is a $\mathcal{C}^1$ vector field in $\bb{R}^3$ defined on all of $\mathcal S$, then
$$
\oint_{\partial \mathcal S} \bvec{F} \cdot d\bvec{s} = \iint_{\mathcal S} \curl \bvec{F} \cdot d\bvec{S}.
$$

Note that this generalises Green's theorem - instead of talking about two dimensional objects only in two dimensions, we can talk about two dimensional surfaces in $\bb R^3$ as well.

##### _example:_ Stokes' theorem in action

Let $\bvec{F} = (-y, 2x, z)$. What is $\oint_{c} \bvec{F} \cdot d\bvec{s}$, where $c = \partial \mathcal S$ for the unit quarter hemisphere in the first octant. 

Stokes' theorem here is lovely because the curl of the surface is very nice, and the boundary of the surface is very ugly. ($\bvec{F}$ spins around somewhat elliptically, and thus has constant curl along the $z$-axis only). Swapping an ugly boundary for a nice curl is an obvious choice!

$$
\begin{split}
	\oint_{\partial \mathcal S} \bvec{F} \cdot d\bvec{s} & = \iint_{\mathcal S} \curl \bvec{F} \cdot d\bvec{S} \\
	& = \iint_S (0, 0, 3) \cdot d\bvec{S} \\
	& = 3 \pi.
\end{split}
$$

%% add pictures