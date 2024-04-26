---
tags:
- math-142
- diff-geo
lecture:
- math-142-35
---

### Path integrals review

Recall that a [[Vector fields#_(temporary) definition _ curves, paths in $ mathbb{R} 3$|curve]] (or a path) is the image of a smooth function $\alpha : I \to \mathbb{R}^n$ where $I \subset \mathbb{R}^n$ is a closed interval $[a, b]$.

##### _definition:_ line integral of a function

For an integrable function $f : \mathbb{R}^n \to \mathbb{R}$ and a curve $C$ parameterised by $\alpha : I \to \mathbb{R}^n$, the integral of $f$ over $C$ is
$$
\int_{C} f \, ds =\int_{a}^b f(\alpha(t)) \lVert \alpha'(t) \rVert  \, dt  
$$

##### _definition:_ line integral of a vector field

For an integrable function $\mathbf{F} : \mathbb{R}^n \to \mathbb{R}^n$ and a curve $C$ parameterised by $\alpha : I \to \mathbb{R}^n$, the integral of $\mathbf{F}$ over $C$ is
$$
\int \mathbf{F} \cdot d\mathbf{s} = \int \mathbf{F}(\alpha(t)) \cdot \alpha'(t) \, dt 
$$

Note that this hints at us defining a differential form by $\phi([\mathbf{v}, p]) = \mathbf{F}(p) \cdot[\mathbf{v}, p]$.

### Surface integrals review

For this section, fix a proper patch $x : D \to \mathbb{R}^n$ for some open $D \subset \mathbb{R}^2$. Choose some point $p = x(u, v)$. Then given $x_{u}$ and $x_{v}$, we want to look at $\lVert x_{u} \times x_{v} \rVert$ to define area, but this isn't defined unless $n = 3$. Thus, we can use Lagrange's identity to look at $\sqrt{ \lVert x_{u} \rVert^2 \lVert x_{v} \rVert^2 - (x_{u} \cdot x_{v})^2 }$.

##### _definition:_ surface integral of a function

Given an integrable function $f : \mathbb{R}^n \to \mathbb{R}$, the integral of $f$ over $M = x(D)$ is
$$
\iint_{M} f \, dA = \int \int_{D} f(x(u, v)) \sqrt{ \lVert x_{u} \rVert ^2 \lVert x_{v}^2 \rVert  - (x_{u} \cdot x_{v})} \, du \, dv 
$$

##### _definition:_ surface integral of a vector field

Given a function $\mathbf{F} : \mathbb{R}^3 \to \mathbb{R}^3$, the integral of $\mathbf{F}$ over $M = x(D)$ is
$$
\iint_{M} \mathbf{F} \cdot d\mathbf{A} = \int \int _{D} \mathbf{F}(x(u, v)) \cdot (x_{u}(u, v) \times x_{v}(u, v)) \, du  \, dv 
$$