---
tags:
- math-199DR/12
- math-199DR/13
- diff-geo
- cx-geo
---

Differential forms on a Riemann surface give us things to integrate over (over curves and regions of the Riemann surface). Eventually, this will let us get analogues of [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_theorem _ the residue formula|the residue formula]] and also a notion of [[Simplicial homology and random walks --- math-145/notes/Cochains, coboundaries, and cohomology#_definition _ cohomology|cohomology]] $\pi_{1}(X) \to \mathbb{C}$ by $\gamma \mapsto \int_{\gamma} \omega$.

### Notions from differential topology

To define differential forms in a way that is meaningful, we need some notions from differential topology which we will never need again. Therefore, we define them in an ad-hoc way — for smooth real $2$-manifolds embedded in some $\mathbb{R}^N$.

##### _definition:_ tangent space

For $X$ a smooth $2$-manifold embedded in $\mathbb{R}^N$, and a point $p \in X$, a chart $(\phi, U)$ centred at $p$, is a smooth function $\mathbb{R}^{2} \to \mathbb{R}^N$ (for the same reason [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_examples _ dumb examples of holomorphisms|charts are holomorphic]]). The tangent space at $p$ is $\mathrm{T}_{p}X = D \phi^{-1} \Big |_{0}^\text{img}(\mathbb{R}^{2})$.

##### _definition:_ derivatives

Given a smooth map of manifolds $F : X \to Y$, and charts $(\phi, U)$ and $(\psi, U)$ on $X$ and $Y$, centred at $p$ and $F(p)$ respectively, we define the derivative of $F$ at $p$ to be the derivative of the corresponding local map $\mathbb{R}^{2} \to \mathbb{R}^{2}$ — $dF_{p} = d \psi^{-1}_{0} \circ d(\psi \circ F \circ \phi ^{-1})_{0} \circ d\phi_{0}$.

##### _definition:_ $k$-form

A $k$-form on a smooth $2$-manifold $X$ is defined for non-negative integers $k \le 2$ —
- a $0$-form is a function $X \to \mathbb{C}$
- a $1$-form is a function $\omega : X \to \bigcup_{p \in X} \mathrm{T}_{p} X^\vee$ with $\omega(p) \in \mathrm{T}_{p}X^\vee$ 
- a $2$-form is a function $\omega : X \to \bigcup_{p \in X} \bigwedge^2 \mathrm{T}_{p} X$ with $\omega(p) \in \bigwedge^2 \mathrm{T}_{p} X$.

Essentially, a $k$-form $\omega$ is a function $\omega : X \to \bigcup_{p \in X} \bigwedge^k \mathrm{T}_{p}X$ with $\omega(p) \in \bigwedge^k \mathrm{T}_{p}X$ where $\bigwedge^k V$ is the $k$-[[Curves and surfaces --- math-142/notes/Differential forms#Exterior algebra and differential $2$-forms|wedge]].

We will define what it means for them to be smooth, holomorphic or anything else, case by case.

### Complex forms

##### _non-example:_ there are no non-zero holomorphic $1$-forms on $\mathbb{C}_{\infty}$

The $1$-forms must be constant for the same reason that there cannot be any [[Riemann surfaces and algebraic curves --- math-199DR/notes/Functions on Riemann surfaces#_theorem _ global holomorphic functions are constant|non-constant globally holomorphic functions on a compact Riemann surface]]. Say away from $0$, $\omega = g(w) \, dw$ and away from $\infty$ $\omega = f(z) \, dz$. Then to transform the $1$-form between the two charts with $w = 1 / z$ and thus, $w' = - 1 / z^{2}$ we have $(g \circ T)(0) = -z^{2} f(z)$ as $z \to 0$. Thus, $g(T(0)) = g()$ 

### Smooth forms

### Pulling back forms

Given a [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphism]] $\pi : X \to Y$ we might hope that we can pull back forms on $Y$ to forms on $X$ through the function. We can! 

##### _definition:_ pullback of forms

If $\pi : X \to Y$ is a holomorphism of Riemann surfaces, and $\omega$ is a $k$-form on $Y$, then
$$
\pi^*\omega_{x}(v_{1}, \dots, v_{k}) = \omega_{\pi(x)}(d \pi_{p}(v_{1}), \dots, d \pi_{p}(v_{k})).
$$

This is really nice! In fact it preserves order information!

##### _proposition:_ the order of the pullback of a form

If $\pi : X \to Y$ is a holomorphism, and $\omega$ is a holomorphic $1$-form on $Y$, then for each $p \in X$, then the order of the pullback of $\omega$ is
$$
\operatorname{ord}_{p} \pi^* \omega = \operatorname{mult}_{p}\pi (1 + \operatorname{ord}_{\pi(p)} \omega) - 1.
$$
