---
tags:
- math-199DR/19
- math-199DR/23
- cx-geo
- alg-geo
---

One thing that we might be interested in as we think of Riemann surfaces, say $X$, more algebraically, is embedding them in projective space. This requires extending our definition of a [[Riemann surfaces and algebraic curves --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphism]] from just $1$-dimensional complex manifolds to $n$-manifolds.

##### _definition:_ holomorphic maps to projective space

A map $\Phi : X \to \mathbb{C} \mathbb{P}^n$ is holomorphic at $p \in X$ if there are [[Riemann surfaces and algebraic curves --- math-199DR/notes/Functions on Riemann surfaces#_definition _ holomorphic functions|holomorphic functions]] $g_{0}, g_{1}, \dots, g_{n}$ with $\Phi = (g_{0} : g_{1} : \dots : g_{n})$ in some neighbourhood of $p$.

$\Phi$ is holomorphic if it is holomorphic at every $p \in X$.

Note that this is a special case of the general definition of a morphism of complex manifolds using the standard chart on projective space. 

##### _proposition:_ non-constant holomorphic maps to projective space

Given [[Riemann surfaces and algebraic curves --- math-199DR/notes/Functions on Riemann surfaces#_definition _ meromorphic|meromorphic functions]] $f_{0}, \dots, f_{n} \in \mathcal{M}_{X}(X)$ not all identically zero, there is a holomorphic map to projective space $\Phi : X \to \mathbb{C}\mathbb{P}^n$ given by
$$
\Phi(p) = (f_{0}(p) : \dots : f_{n}(p))
$$
at $p$ where $m_{p} = \min \{ \operatorname{ord}_{p}f_{i} \} = 0$ (points where there are no poles and at least one non-zero $f_{i}$). If $m_{p} \neq 0$, $\Phi$ is defined by the normalised function
$$
\Phi(p) = (z^{-m_{p}} f_{0}(z) : \dots : z^{-m_{p}} f_{n}(z))
$$
in a local coordinate $z$.

###### _proof:_

Wherever $m_{p} = 0$, each $f_{i}$ is holomorphic (since none of them have order low enough to have a pole), and they are not all zero (since there is at least one function of order $0$).

Where $m_{p} \neq 0$, by multiplying by $z^{-m_{p}}$, we force no poles if $m_{p} < 0$ (by the [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ pole|definition of a pole]] from complex analysis) and we force no zeroes if $m_{p} > 0$ (by the [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_proposition _ characterising holomorphic functions near zeroes|characterisation of zeroes of a holomorphic function]] from complex analysis). Thus, each $f_{i}$ is holomorphic and they are not all zero.

In fact every holomorphic map $\Phi$ to projective space can be given uniquely up to scaling by a meromorphic function in this way. We just push $\Phi$ forward through the complex charts $z_{i}$ in $(z_{0} : z_{1} : \dots : z_{n})$ to get the meromorphic functions. If $(f_{0} : f_{1} : \dots : f_{n}) = (g_{0} : g_{1} : \dots : g_{n})$ we just write the scalar $\lambda$ at each point as a function of $p \in X$. Since $\lambda(p) = f_{0}(p) / g_{0}(p)$, $\lambda$ is meromorphic on $X$.

### Complete and general linear systems

Complete linear systems of divisors contain all of the [[Riemann surfaces and algebraic curves --- math-199DR/notes/The Riemann-Roch spaces of a divisor#_definition _ effective, positive divisor|effective]] divisors that are [[Riemann surfaces and algebraic curves --- math-199DR/notes/Linear equivalence of divisors#_definition _ linear equivalence|equivalent]] to a given divisor. They allow us to turn the information of how a divisor bounds poles and forces zeroes into just the bounds on poles. More importantly, we will see that they keep track of important information about projective maps.

##### _definition:_ complete linear system

The complete linear system of a divisor $D \in \operatorname{Div} X$ is the set
$$
\lvert D \rvert  = \{ E \in \operatorname{Div} X \mid E \geq 0, E \sim D \}.
$$


In fact, complete linear systems provide a connection between projective space and divisors! Specifically,

##### _proposition:_ projective space and complete linear system correspondence

There is a bijection between projectivisation of the [[Riemann surfaces and algebraic curves --- math-199DR/notes/The Riemann-Roch spaces of a divisor#_definition _ the Riemann-Roch function space of a divisor|the Riemann-Roch space of a divisor]] and its complete linear system.

###### _proof:_

Consider the map $S : \mathbb{P}\mathcal{L}(D) \to \lvert D \rvert$ by $f \mapsto \operatorname{div} f + D$ for $f \in \mathcal{L}(D)$. This is clearly invariant under scaling of $f$ (since a non-zero scalar doesn't change the zeroes or poles) and thus, well-defined. It is in fact a bijection.

It's clearly injective — $Sf = Sg$ forces $\operatorname{div} f = \operatorname{div} g$ and thus, $f = g$. If $E \in \lvert D \rvert$, then $E = \operatorname{div} f + D$. Further $E \geq 0$ gives $\operatorname{div} f + D \geq 0$, and thus, $f \in \mathcal{L}(D)$.

This corresponds to the short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathbb{C}^* \ar[r] & \mathcal{L}(K) \ar[r] & K \ar[r] & 0.
	\end{tikzcd}
\end{document}
```

A general linear system is just an image of the projectivisation of a linear subspace under the correspondence with the complete linear system.

##### _definition:_ linear system

A linear system in general is the image of $\mathbb{P}V \subseteq \mathbb{P} \mathcal{L}(D)$ (where $V$ is a [[linear subspace]] $V \subseteq \mathcal{L}(D)$) under $S$.

Linear systems of dimensions $1, 2, 3$ are called pencils, nets, and webs.

### Base points

There is exactly one kind of restriction on linear systems — base points.

##### _definition:_ base points

For a linear system $Q$ on $X$, $p \in X$ is a base point of $Q$ if every divisor $E \in Q$ has $E(p) \neq 0$.

Having a base point is equivalent to being a subspace of a smaller subspace

### Linear systems of a projective maps

The linear systems that are of greatest interest are the linear systems of a projective map.

##### _definition:_ linear system of a projective map

Given a holomorphic map $\Phi : X \to \mathbb{P} \mathbb{C}^n$ and a global meromorphic representation $\Phi = (f_{0} : f_{1} : \dots : f_{n})$, the linear system of $\Phi$ is given by the image of the projectivisation $V_{f} = \operatorname{span}(f_{0}, f_{1}, \dots, f_{n})$ in $\mathcal{L}(D)$ where $D$ is the divisor that allows exactly the poles of $f_{i}$ and no more —
$$
D(p) = - \min \{ \operatorname{ord}_{p} f_{i} \}.
$$

The linear system of $\Phi$ is denoted $\lvert \Phi \rvert$.

Note that we need to verify that this doesn't depend on the choice of meromorphic representation which is a not-too-difficult exercise in linear algebra.

Linear systems of projective maps are nice because they are base point free.

##### _proposition:_ the linear system of a projective map is base point free

For $\Phi : X \to \mathbb{P}\mathbb{C}^n$ a holomorphic map into projective space, $\lvert \Phi \rvert$ is base point free.

###### _proof:_

Clearly we can go from a projective map to a linear system. In fact, as long as the linear system doesn't have any obvious obstruction (that is, it is base point free) we have a projective map.

##### _theorem:_ the projective map of a linear system

Let $Q \subseteq \lvert D \rvert$ be a base point free linear system of projective dimension $n$ on $X$. Then there exists a holomorphic map $\Phi : X \to \mathbb{P} \mathbb{C}^n$ such that $\lvert \Phi \rvert = Q$. Further, $\Phi$ is unique upto choice of coordinates on $\mathbb{P} \mathbb{C}^n$.

###### _proof:_

Suppose $Q$ corresponds to a linear subspace $V \subseteq \mathcal{L}(D)$ such that $Q = \{ \operatorname{div} f + D \mid f \in V \}$. Picking a basis of meromorphic functions $f_{0}, f_{1}, \dots, f_{n}$ in $V$. We get $\Phi = (f_{0} : f_{1} : \dots : f_{n})$ is the desired holomorphic map with $\lvert \Phi \rvert = Q$.

Thus, we have a correspondence between base point free linear systems of dimension $n$ on $X$ and holomorphic maps to $\mathbb{P} \mathbb{C}^n$.
