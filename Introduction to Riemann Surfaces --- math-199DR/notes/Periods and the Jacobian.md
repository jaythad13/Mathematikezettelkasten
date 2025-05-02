---
tags:
- math-199DR/26
- cx-geo
- alg-geo
---

Let $X$ be a compact, connected Riemann surface.

It's a fact of topology that [[Topology --- math-147/notes/Classification of surfaces#_theorem _ triangulation of low-dimensional manifolds (Moise–Bing)|every surface is triangulable]] — that is, any algebraic curve $X$ is homeomorphic to a [[Topics in Geometry and Topology --- math-145/notes/Simplicial complexes#_definition _ simplicial complex|simplicial complex]] $X$ with all maximal [[Topics in Geometry and Topology --- math-145/notes/Simplicial complexes#_definition _ face, coface|faces]] of dimension $2$. This, allows us to use all of the theory of [[Topics in Geometry and Topology --- math-145/notes/Simplicial homology|simplicial homology]] on $X$. Since $X$ is $2$-dimensional, compact, and connected, we don't really care about anything except for the first homology which captures $1$-holes. Note that $\mathrm{H}_{1}(X)$ is the abelianisation of the fundamental group $\pi_{1}(X)$.

Typically, for a genus $g$ curve — a $g$-holed torus, the homology looks like $\mathbb{Z}^{2g}$ (recall that the torus $S^1 \times S^1$ has abelian fundamental group $\mathbb{Z} \times \mathbb{Z}$).

The primary thing we do with homology is de Rham cohomology by [[Introduction to Riemann Surfaces --- math-199DR/notes/Integrating forms|integrating over it]]. That is, since, by Stokes' theorem we don't have to care about integrating over anything that is a boundary, we have a homomorphism $\mathrm{H}_{1}(X) \to \Omega^1(X)^\vee$ by "integrating over".

##### _definition:_ periods

Given $\gamma \in \mathrm{H}^1(X)$, a period is a functional on holomorphic $1$-forms, in the image of $I : \mathrm{H}^1(X) \to \Omega^1(X)^\vee$ by
$$
I \gamma : \omega \mapsto \int_{\gamma} \omega.
$$

##### _definition:_ the Jacobian

The Jacobian of $X$ is the complex manifold $\operatorname{Jac} X = \Omega^1(X)^\vee / d$.

##### _example:_ the Jacobian of the torus

We've seen that a torus $\mathbb{C} / \Lambda$ [[Introduction to Riemann Surfaces --- math-199DR/notes/Linear equivalence of divisors#_theorem _ Abel's theorem for elliptic curves|is isomorphic to its Jacobian]].

Unfortunately, we don't in general have that Riemann surfaces are isomorphic to their Jacobians — for one, the Jacobian tends to look like a dimension $g$ complex manifold $(\mathbb{C} / \mathbb{Z}^{2})^g$ while Riemann surfaces are of course (complex) dimension $1$.

##### _definition:_ Abel-Jacobi map

Given a choice of base point $p_{0} \in X$, the Abel-Jacobi map is $A : \operatorname{Div} X \to \operatorname{Jac} X$ extended linearly from
$$
A(p) : \omega \mapsto \int_{p_{0}}^p \omega \, dx \pmod{\operatorname{img} I}.
$$

Note that the restriction to degree zero divisors is particularly nice. Since we can pair positive and negative points

Abel's theorem will be to investigate the kernel of $A_{0} : \operatorname{Div}_{0} X \to \operatorname{Jac} X$. We want to show that it is just the principle divisors $\operatorname{PDiv} X$.

Essentially, what we want to prove is that the Abel-Jacobi map gives us a way to show that the missing piece in both of the exact sequences below is the Jacobian.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathcal{O}_{X}(X)^* \ar[r] & \mathcal{M}_{X}(X)^* \ar[r, "\mathrm{div}"] & \mathrm{Div}_{0} \, X \ar[r] & ? \ar[r] & 0 \\
		0 \ar[r] & \mathrm{B}_{1}(X) \ar[r] & \mathrm{Z}_{1}(X) \ar[r] & \Omega_{1}(X)^\vee \ar[r] & ? \ar[r] & 0
	\end{tikzcd}
\end{document}
```


Assuming the statement of Abel's theorem, we get lots of useful facts

##### _proposition:_ the Abel-Jacobi map is typically injective


