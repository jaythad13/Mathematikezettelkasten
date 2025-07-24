---
tags:
- diff-geo
- math-142/35
- math-142/36
- math-142/37
---

### Path integrals review

Recall that a [[Curves and surfaces --- math-142/notes/Vector fields#_(temporary) definition _ curves, paths in $ mathbb{R} 3$|curve]] (or a path) is the image of a smooth function $\alpha : I \to \mathbb{R}^n$ where $I \subset \mathbb{R}^n$ is a closed interval $[a, b]$.

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

Given a function $\mathbf{F} : \mathbb{R}^3 \to \mathbb{R}^3$, the integral of $\mathbf{F}$ over a surface $M = x(D)$ is
$$
\iint_{M} \mathbf{F} \cdot d\mathbf{A} = \int \int _{D} \mathbf{F}(x(u, v)) \cdot (x_{u}(u, v) \times x_{v}(u, v)) \, du  \, dv 
$$

### Integrating forms

The natural way to define integrating a $1$-form is then to integrate it over a $1$-manifold — a curve. Similarly, the natural way to define integrating a $2$-form is to integrate it over a $2$-manifold — a surface. That is, integrating $1$-forms and $2$-forms is just redefining integrating line and surface integrals respectively.

##### _definition:_ integrating a $1$-form over a curve

For any $\phi = f_{1} \, dx_{1} + \dots + f_{n} \, dx_{n} \in \Omega^1(\mathbb{R}^n)$, and any curve $c$ parameterised by $\alpha : [a, b] \to \mathbb{R}^n$, the integral of $\phi$ over $c$ is
$$
	\int_{c} \phi = \int_{a}^b \phi(\alpha'(t)) \, dt.
$$

Note that this relates directly to the notion of the line integral of a "vector field" over a curve — for any smooth "vector field" $\mathbf{F} : \mathbb{R}^n \to \mathbb{R}^n$, with dual $\mathbf{F}^\vee = \phi$ (that is $\phi([\mathbf{v}, p]) = \mathbf{F}(p) \cdot \mathbf{v}$), we have
$$
\int_{c} \mathbf{F} \cdot d\mathbf{s} = \int_{c} \phi.
$$
Note that for $\mathbf{F}(p) = (f_{1}(p), \dots, f_{n}(p))$ we have $\phi = \mathbf{F}^\vee = f_{1} \, dx_{1} + \dots + f_{n} \, dx_{n}$. This follows just by pushing through the definitions.

##### _theorem:_ the fundamental theorem of calculus for $1$-forms

Suppose $\phi = df$ for some $f \in \mathcal{C}^\infty(\mathbb{R}^n)$. Then the integral of $\phi$ along any curve $c$ parameterised by $\alpha : [a, b] \to \mathbb{R}^n$ only depends on the endpoints $p = \alpha(a)$ and $q = \alpha(b)$. That is,
$$
\int_{c} \phi = f(q) - f(p).
$$

###### _proof:_

Note that if we have $\mathbf{F}^\vee = \phi$, then $\phi = df$ is equivalent to $\mathbf{F} = \nabla f$. Thus, this will also be a proof of the classical fundamental theorem of calculus for line integrals.

$\phi = df$ means that for $\phi = f_{1} \, dx_{1} + \dots + f_{n} \, dx_{n}$ we have $f_{k} = \frac{ \partial f }{ \partial x_{k} }$. Thus
$$
\begin{split}
\phi(\alpha'(t_{0})) & = \sum_{k = 1}^n f_{k}(\alpha(t_{0})) \frac{d \alpha_{k}}{dt} \Big |_{t_{0}} \\
 & = \sum_{k = 1}^n \frac{ \partial f }{ \partial x_{k} } \Big |_{\alpha(t_{0})} \frac{d \alpha_{k}}{dt} \Big |_{t_{0}} \\
 & = \frac{d(f \circ \alpha)}{dt} \Big |_{t_{0}}
\end{split}
$$
by the chain rule.

Thus, by the fundamental theorem of calculus,
$$
\begin{split}
\int_{c} \phi & = \int_{a}^b \frac{d(f \circ \alpha)}{dt} dt \\
 & = (f \circ \alpha) \Big |_{a}^b \\
 & = f(q) - f(p). 
\end{split}
$$

##### _definition:_ integrating a $2$-form over a surface

Say we have $M$, a surface given by a patch $x : D = [a, b] \times [c, d] \to M$, and a differential form $\eta = g_{1} \, dx_{2} \wedge dx_{3} + g_{2} \, dx_{3} \wedge dx_{1} + g_{3} \, dx_{1} \wedge dx_{2}$. Then the integral of $\eta$ over $M$
$$
\iint_{M} \eta = \int_{a}^b \int_c^d \begin{vmatrix}
(g_{1} \circ x)(u, v) & (g_{2} \circ x)(u, v) & (g_{3} \circ x)(u, v) \\
\dfrac{ \partial x_{1} }{ \partial u } \Big |_{(u, v)} & \dfrac{ \partial x_{2} }{ \partial u } \Big |_{(u, v)} & \dfrac{ \partial x_{3} }{ \partial u } \Big |_{(u, v)} \\ \\
\dfrac{ \partial x_{1} }{ \partial v } \Big |_{(u, v)} & \dfrac{ \partial x_{2} }{ \partial v } \Big |_{(u, v)} & \dfrac{ \partial x_{3} }{ \partial v } \Big |_{(u, v)}
\end{vmatrix}  \, dv   \, du 
$$

Again, note that this relates directly to the notion of the surface integral of a "vector field". Particularly, note that for the "vector field" $\mathbf{G} = (g_{1}, g_{2}, g_{3})$, we can write
$$
\begin{split}
\eta & = g_{1} \, dx_{2} \wedge dx_{3} + g_{2} \, dx_{3} \wedge dx_{1} + g_{3} \, dx_{1} \wedge dx_{2} \\
 & = r \, du \wedge dv
\end{split}
$$
where $r$ is just that determinant. Thus, we can equivalently define
$$
\iint_{M} \eta = \int_{a}^b \int_{c}^d \eta(x_{u}, x_{v})  \, dv  \, du 
$$
or
$$
\iint_{M} \eta = \iint \mathbf{G}(x(u, v)) \cdot d\mathbf{A}.
$$

### Stokes' theorem

We saw already the fundamental theorem of calculus for line integrals. Is there something analogous for surfaces? In particular, if $\eta = d \phi$ for some $1$-form $\phi$, is calculating $\iint_{M} \eta$ any easier?

##### _theorem:_ Stokes' theorem for differential forms

Suppose we have a $2$-form $\eta$ on a surface $M$. Then
$$
\iint_{M} \eta = \int_{\partial M} \phi.
$$

###### _proof:_

Recall that we can write $\phi = g \, du + h \, dv$. Thus, $\phi([\mathbf{v}, p]) = v_{1}g(p) + v_{2} h(p)$ for $[\mathbf{v}, p] = v_{1} x_{u} + v_{2} x_{v}$ and thus $g = \phi(x_{u})$ and $h = \phi(x_{v})$.

Then for $\eta = d \phi$ we have
$$
\eta(x_{u}, x_{v}) = \left( \frac{\partial h}{\partial u} \Big |_{(u, v)} - \frac{ \partial g }{ \partial v } \Big |_{(u, v)} \right)
$$

Then it follows that
$$
\begin{split}
\iint_{M} \eta & = \int_{a}^b \int_{c}^d \eta(x_{u}, x_{v})  \, dv   \, du \\
 & = \int_{c}^d \int_{a}^b \frac{ \partial h }{ \partial u } \Big |_{(u, v)} \, du    \, dv - \int_{a}^b \int_{c}^d \frac{ \partial g }{ \partial v } \Big |_{(u, v)}  \, dv   \, du \\
 & = \int_{c}^d h(b, v) - h(a, v) \, dv - \int_{a}^b g(u, d) - g(u, c)  \, du \\
 & = \int_{x^\text{img}(c_{1})} \phi + \int_{x^\text{img}(c_{2})} \phi + \int_{x^\text{img}(c_{3})} \phi + \int_{x^\text{img}(c_{4})} \phi \\
 & = \int_{\partial M} \phi. 
\end{split}
$$

##### _corollary:_ the classical Stokes' theorem

Assume $\mathbf{G} = \nabla \times \mathbf{F}$ for "vector fields" $\mathbf{F}, \mathbf{G} : \mathbb{R}^3 \to \mathbb{R}^3$. Then 
$$
\iint_{M} \mathbf{G} \cdot d\mathbf{A} = \int_{\partial M} \mathbf{F} \cdot d\mathbf{s}.
$$