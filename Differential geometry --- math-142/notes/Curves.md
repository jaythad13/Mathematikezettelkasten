---
tags:
- diff-geo
- math-142
lecture: math-142-3
---

In physics, when a particle is moving along a curve, we want to keep track of the position and velocity of the vector. Differential geometry allows us to keep track of both simultaneously with tangent vectors.

Recall the [[Vector fields#_(temporary) definition _ curves, paths in $ mathbb{R} 3$|temporary definition of a curve]] that we gave last time. If $\alpha$ is a function that defines a curve $c$, then we say that $\alpha$ parameterises $c$. Note that we can write $\alpha$ as having component functions $\alpha_{1}, \alpha_{2}, \alpha_{3}$.

##### _definition:_ smoothness for curves

If a curve $c$ has a differentiable parameterisation $\alpha$, we say $c$ is differentiable.

If a curve $c$ has a smooth parameterisation $\alpha$, we say $c$ is smooth.

Note that checking smoothness for a parameterisation reduces to checking smoothness for its component functions.

##### _example:_ lines are smooth curves

For a line through $\mathbf{p}$ and $\mathbf{q}$, we have a smooth parameterisation
$$
\begin{gathered}
\alpha : \mathbb{R} \to \mathbb{R}^3 \\
t \mapsto \mathbf{p} + t\left( \mathbf{q} - \mathbf{p} \right)
\end{gathered}
$$

### Position and velocity

If $\alpha : I \to \mathbb{R}^3$ parameterises $c$, we can make the following definitions.

##### _definition:_ position

The position along the curve at time $t$ is $\alpha(t)$.

##### _definition:_ velocity, speed

The velocity at time $t_{0}$ is $\frac{d\alpha}{dt} \Big |_{t_{0}}$. 

The speed at time $t_{0}$ is $v(t_{0}) = \lVert \frac{d\alpha}{dt} \Big |_{t_{0}} \rVert$.

We want to omit silly parameterisations, so we make the following definition.

##### _definition:_ regularity of a curve

We say a curve $c$ is regular if it has a parameterisation such that its speed is nonzero.

To keep track of all of this at once, we use the tangent space to define tangent vectors to the curve.

##### _definition:_ tangent vector to a curve

Given a curve $c$ parameterised by $\alpha$, the tangent vector at $t_{0}$ is given by a function $\alpha' : I \to \mathrm{T}\mathbb{R}^3$ by
$$
t_{0} \mapsto \left[ \frac{d\alpha}{dt} \Big |_{t_{0}}, \alpha(t_{0}) \right].
$$

##### _proposition:_ you can use $\alpha'$ like a vector field

Given a smooth function $f : \mathbb{R}^3 \to \mathbb{R}$,
$$
\alpha'(t_{0})[f] = Df \Big |_{\alpha(t_{0})} \left( \frac{d\alpha}{dt} \Big |_{t_{0}} \right).
$$

###### _proof sketch:_

Just chase through the definitions.

### Reparameterisations

The best way to understand is physics.

##### _example:_ Minkowski's proper time

In special relativity, physics says that if we move fast, time slows down. We deal with this by reparameterising in terms of proper time

##### _definition:_ reparameterisation

Let $\alpha : I \to \mathbb{R}^3$ be a parameterisation of a curve $c$. We say that $\beta : J \to \mathbb{R}^3$ is a reparameterisation if there is a differentiable function $h : J \to I$ such that  $\beta = \alpha \circ h$ and $h'(\tau) \neq 0$.

In other words, the following diagram commutes, with all arrows being differentiable functions.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
	J \arrow[rd, "\beta"] \arrow[r, "\exists h", dashrightarrow] & I \arrow[d, "\alpha"] \\
	& \mathbb R^3
	\end{tikzcd}
\end{document}
```

This raises natural questions like
- how does the position change?
and
- how does the velocity change?
under reparameterisation.

The answers follow from the definitions and [[Differentiability theorems#_theorem _ chain rule|the chain rule]]. For $h(\tau_{0}) = t_{0}$,
- the position is $\mathbf{p} = \alpha(t_{0}) = \beta(\tau_{0})$
- and the velocity is given by $\mathbf{v} = \frac{d\beta}{d\tau} \Big |_{\tau_{0}} = \frac{d\alpha}{dt} \Big |_{t_{0}} \frac{dh}{d\tau} \Big |_{\tau_{0}}$
- thus, the tangent vector is $[\mathbf{v}, \mathbf{p}] = \frac{dh}{d\tau} \Big |_{\tau_{0}}\left[ \frac{d\alpha}{dt} \Big |_{t_{0}}, \alpha(t_{0}) \right] = \frac{dh}{d\tau} \Big |_{\tau_{0}} \alpha'(t_{0})$