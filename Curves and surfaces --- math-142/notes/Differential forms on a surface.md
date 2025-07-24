---
tags:
- diff-geo
- math-142/33
- math-142/34
- math-142/35
---

We've seen how to deal with [[Curves and surfaces --- math-142/notes/Differential forms|differential forms]] on $\mathbb{R}^3$. If you replace all of the domains $\mathbb{R}^3$ with a surface $M$, we get differential forms on a surface.

### $0$-forms and $1$-forms on a surface

To avoid repeating hypotheses all the time
##### _notation:_ $M$

For this section, let $M$ be a surface in $\mathbb{R}^3$ with a family of patches $x_{k} : D_{k} \to I$ for $k \in I$.

We already have a notion of [[Curves and surfaces --- math-142/notes/Calculus on surfaces#_definition _ smooth functions on a surface|smooth functions]] on a surface. Thus, we have $0$-forms on a surface already.

##### _definition:_ $0$-forms on a surface

A $0$-form on $M$ is a smooth function $f : M \to \mathbb{R}$.

$1$-forms allow us to take tangent vectors to the reals smoothly — we can define them in the most obvious way.

##### _definition:_ $1$-forms on a surface

A $1$-form on $M$ is a function $\phi : \mathrm{T}M \to \mathbb{R}$ that is $\mathbb{R}$-linear on each tangent space $\mathrm{T}_{p}M$ (for all $p \in M$).

We denote the collection of all $1$-forms on $M$ by $\Omega^1(M)$.

Note that most $1$-forms on $M$ can be thought of as $1$-forms on $\mathbb{R}^3$ as well.

There should then be an obvious way to go from $0$-forms to $1$-forms like the [[Curves and surfaces --- math-142/notes/The exterior derivative|exterior derivative]] was on $\mathbb{R}^3$.

##### _proposition, definition:_ the exterior derivative on $0$-forms

Say $f : M \to \mathbb{R}$ is a $0$-form and $[\mathbf{v}, p] \in \mathrm{T}_{p}M$ is given by $[\mathbf{v}, p] = \alpha'(t_{0})$. Let $p = x_{k}(u_{0}, v_{0})$ and let $a = x^{-1} \circ \alpha: \mathbb{R} \to \mathbb{R}^2$. Then the map $df : \mathrm{T}M \to \mathbb{R}$ given by
$$
df([\mathbf{v}, p]) = D(f \circ \alpha) \Big |_{t_{0}}
$$
is a $1$-form.

We say that the map $d : \Omega^0(M) \to \Omega^1(M)$ that sends a smooth $f : M \to \mathbb{R}$ to $df \in \Omega^1(M)$ is the exterior derivative.

###### _proof:_

Let $[\mathbf{v}, p] = \alpha'(t_{0}) \in \mathrm{T}_{p}M$ and $[\mathbf{w}, p] = \beta'(t_{0}) \in \mathrm{T}_{p}M$. Let $\lambda \in \mathbb{R}$.

Notice that
$$
\begin{split}
[\mathbf{v}, p] + \lambda [\mathbf{w}, p] & = \alpha'(t_{0}) + \lambda \beta'(t_{0}) \\
 & = (\alpha + \lambda \beta)'(t_{0}). 
\end{split}
$$
Let $\gamma = \alpha + \beta$.

Thus,
$$
\begin{split}
df([\mathbf{v}, p] + \lambda [\mathbf{w}, p]) & = D(f \circ \gamma) \Big|_{t_{0}} \\
 & = Df \Big |_{p} D\gamma \Big |_{t_{0}}  \\
 & = Df \Big |_{p} D \alpha \Big |_{t_{0}} + \lambda Df \Big |_{p} D \beta \Big |_{t_{0}} \\
 & = D(f \circ \alpha) \Big |_{t_{0}} + \lambda D(f \circ \beta) \Big |_{t_{0}} \\
 & = df([\mathbf{v}, p]) + \lambda \, df([\mathbf{w}, p]).
\end{split}
$$
as desired.

##### _proposition:_ the coordinate expression for $1$-forms on a surface

Fix some $p \in M$ and a patch $x$ with $x(u_{0}, v_{0}) = p$.

1) For any $\phi \in \Omega^1(M)$. Then, restricted to $\mathrm{T}_{p}M$
$$
\phi : g_{1} \, du + g_{2} \, dv
$$
	for some $g_{1}, g_{2} : D_{k} \to \mathbb{R}$.
2) Say $f : M \to \mathbb{R}$ is a $0$-form. Then, restricted to $\mathrm{T}_{p}M$,
$$
df = \frac{ \partial (f \circ x_{k}) }{ \partial u } \Big |_{(u_{0}, v_{0})} \, du + \frac{ \partial (f \circ x_{k}) }{ \partial v } \Big |_{(u_{0}, v_{0})} \, dv
$$

###### _proof:_

1) follows from writing $\phi = f_{1} \, dx_{1} + f_{2} \, dx_{2} + f_{3} \, dx_{3}$ and noticing that the coordinates $x_{1}, x_{2}, x_{3}$ can be thought of as the component functions of the patch $x$. Here we think of $u$ and $v$ as functions $M \to \mathbb{R}$.
2) follows from applying the chain rule to the formula $df = D((f \circ x) \circ(x ^{-1} \circ \alpha))$.

### $k$-forms on a surface

The natural question to ask is if we can generalise this to differential $k$-forms and their exterior derivative on a surface. Of course! We can do [[Curves and surfaces --- math-142/notes/Differential forms#Exterior algebra and differential $2$-forms|all the same algebra]] to define the wedge product of differential forms on $M$.

For completeness, we list out properties of the wedge product below.

##### _proposition:_ properties of the wedge product

For any $f, g \in \mathcal{C}^\infty(M)$ and $\phi, \psi, \theta_{1}, \dots, \theta_{n} \in \Omega^1(M)$, we have

1) linearity: $(f \, \phi + g \, \psi) \wedge \theta_{1} \wedge \cdots \wedge \theta_{n} = f(\phi \wedge \theta_{1} \wedge \cdots \wedge \theta_{n}) + g(\psi \wedge \cdots \wedge \theta_{n})$
2) commutativity with $\mathcal{C}^\infty(M)$: $\theta_{1} \wedge \cdots \wedge  f \, \theta_{i} \wedge \cdots \wedge \theta_{n} = f (\theta_{1} \wedge \cdots \wedge \theta_{n})$
3) alternating: $\phi_{\sigma(1)} \wedge \cdots \wedge \phi_{\sigma(n)} = \operatorname{sgn} \sigma (\phi_{1} \wedge \cdots \wedge \phi_{n})$.

Then, we can define $2$-forms as

##### _definition:_ $2$-forms on a surface

A $2$-form on $M$ is a linear combination of $\sum_{i} \phi_{i} \wedge \psi_{i}$ for $1$-forms $\phi_{i}, \psi_{i}$.

Notice that we don't need to define $k$-forms in general, since we can write any $2$-form as a scalar multiple of $du \wedge dv$, and thus, any further wedging with a $1$-form would cause us to repeat either $du$ or $dv$. That is, any $k$-form on $M$ with $k > 2$ is just $0$ everywhere.

Now we can define the exterior derivative in a natural way!

It turns out to be exactly the same thing as what we did on $\mathbb{R}^n$.

![[Curves and surfaces --- math-142/notes/The exterior derivative#_definition _ the exterior derivative]]

Here, however, note that this is equivalent to defining
$$
d : f \, du + g \, dv \mapsto df \wedge du + dg \wedge du.
$$
for the case of $k = 1$.

Note that all this time we've been working with $R = \mathcal{C}^\infty(M)$ as a ring and $V = \Omega^1(M)$, and then $\bigwedge^k(V)$. We don't actually need a manifold to start with — we could just pick a ring and a module and see what we get by assuming that these things are the regular functions and the differentials on some unknown space. Then the $\bigwedge^k(V)$ consist of what are called Kahler differentials, and we are doing algebraic geometry.

It turns out that, again, this definition is equivalent to things we know about! For example, the differential of a $1$-form is just the curl.

##### _proposition:_ exact $2$-forms are curls

Suppose we have $\phi = g_{1} \, du + g_{2} \, dv \in \Omega^1(M)$. Then
$$
d \phi = \left( \frac{ \partial g_{2} }{ \partial u } - \frac{ \partial g_{1} }{ \partial v }  \right) du \wedge dv. 
$$

### Evaluating forms

What does it really mean to evaluate a $1$-form or a $2$-form? Exactly what you might suspect. Let $p = x(u_{0}, v_{0}) = x_{k}(u_{0}, v_{0}) \in M$ and $[\mathbf{v}, p], [\mathbf{w}, p] \in \mathrm{T}_{p}M$ with $[\mathbf{v}, p] = a x_{u} + bx_{v}$ and $[\mathbf{w}, p] = c x_{u} + dx_{v}$.
Then for $f \in \Omega^0(M)$, $\phi = g \, du + h \, dv \in \Omega^1(M)$, and $\eta = r \, du \wedge dv \in \Omega^2(M)$, we have
$$
\begin{split}
\phi([\mathbf{v}, p]) & = a g_{k}(u_{0}, v_{0}) + b h_{k}(u_{0}, v_{0}) \\
df([\mathbf{v}, p]) & = a \frac{ \partial f_{k} }{ \partial u } \Big |_{(u_{0}, v_{0})} + b \frac{ \partial f_{k} }{ \partial v } \Big |_{(u_{0}, v_{0})} \\
\eta([\mathbf{v}, p], [\mathbf{w}, p]) & = (ad - bc) r_{k}(u_{0}, v_{0}) \\
d\phi([\mathbf{v}, p], [\mathbf{w}, p]) & = (ad - bc) \left( \frac{ \partial h_{k} }{ \partial u } \Big |_{(u_{0}, v_{0})} - \frac{ \partial g_{k} }{ \partial v } \Big |_{(u_{0}, v_{0})} \right). 
\end{split}
$$

