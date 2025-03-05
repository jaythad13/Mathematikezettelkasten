---
tags:
- math-199DR/11
- diff-geo
- cx-geo
---

Differential forms on a Riemann surface give us things to integrate over (over curves and regions of the Riemann surface). Eventually, this will let us get analogues of [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#_theorem _ the residue formula|the residue formula]] and also a notion of [[Topics in Geometry and Topology --- math-145/notes/Cochains, coboundaries, and cohomology#_definition _ cohomology|cohomology]] $\pi_{1}(X) \to \mathbb{C}$ by $\gamma \mapsto \int_{\gamma} \omega$.

##### _definition:_ $k$-form

A $k$-form on a Riemann surface $X$ is defined for non-negative integers $k \le 2$ —
- a $0$-form is a function $X \to \mathbb{C}$
- a $1$-form is a function $\omega : X \to \bigcup_{p \in X} \mathrm{T}_{p} X^\vee$ with $\omega(p) \in \mathrm{T}_{p}X^\vee$ 
- a $2$-form is a function $\omega : X \to \bigcup_{p \in X} \bigwedge^k \mathrm{T}_{p} X$ with $\omega(p) \in \bigwedge^k \mathrm{T}_{p} X$.

We will define what it means for them to be smooth, holomorphic or anything else, case by case.

### Complex forms



##### _non-example:_ there are no non-zero holomorphic $1$-forms on $\mathbb{C}_{\infty}$

The $1$-forms must be constant for the same reason that there cannot be any [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_theorem _ global holomorphic functions are constant|non-constant globally holomorphic functions on a compact Riemann surface]]. Say away from $0$, $\omega = g(w) \, dw$ and away from $\infty$ $\omega = f(z) \, dz$. Then to transform the $1$-form between the two charts with $w = 1 / z$ and thus, $w' = - 1 / z^{2}$ we have $(g \circ T)(0) = -z^{2} f(z)$ as $z \to 0$. Thus, $g(T(0)) = g()$ 

### Smooth forms

### Pulling back forms

Given a [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphism]] $\pi : X \to Y$ we might hope that we can pull back forms on $Y$ to forms on $X$ through the function. We can! We just need to know what a derivative is.