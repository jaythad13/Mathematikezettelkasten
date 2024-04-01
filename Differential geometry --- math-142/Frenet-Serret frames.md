---
tags:
- diff-geo
- math-142
lecture:
- math-142-11
- math-142-12
- math-142-13
- math-142-14
---

With Frenet-Serret frames, we are setting up the [[Frames|frame]]work for a lot of differential geometry.

The basic idea of a Frenet-Serret frame is to have the right frame for a particular problem. To do this, we need to an idea of how we can define vector fields on a curve.

### Vector fields on a curve

The best way to describe this is with a commutative diagram. Suppose we have a curve parameterised by $\alpha : I \to \mathbb{R}^3$. Then we can map $I$ onto the the [[Exact sequences#_example _ short exact sequence|short exact sequence]] associated with the tangent space in three ways.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& & I \ar[d, "\alpha'"] \ar[ld, "\alpha"] \ar[rd, "\frac{d \alpha}{dt}"] \\
		\{ \mathbf 0 \} \ar[r] & \mathbb R^3 \ar[r, "{\mathbf p \mapsto \mathbf 0_{\mathbf p}}"'] & \mathrm T \mathbb R^3 \ar[r, "\mathbf v_{\mathbf p} \mapsto \mathbf v"'] & \mathbb R^3 \ar[r] & \{ \mathbf 0 \}
	\end{tikzcd}
\end{document}
```

Note that the $\alpha$ arrow makes the diagram technically not commutative anymore.

We only really care about $\alpha'$.

Recall the idea of reparameterisations. 

##### _proposition:_ you can go along any curve at unit speed

If $\alpha$ is a [[Curves#_definition _ regularity of a curve|regular curve]], there is an orientation preserving reparameterisation $\beta = \alpha \circ h$ such that $\lVert \beta'(\tau) \rVert = 1$ for all $\tau \in J$.

###### _proof:_

Consider the arc length $\tau$ given by
$$
	\tau(t) = \int_{t_{0}}^t \left \lVert \frac{d\alpha}{dt} \Big |_{u} \right \rVert \, du + \tau_{0}
$$
for some $\tau_{0} \in \mathbb{R}$.

Since $\alpha$ is regular, we have $\left \Vert \dfrac{d\tau}{dt} \right \Vert = \left \Vert \dfrac{d \alpha}{dt} \right \Vert \neq 0$, and thus, by [[Inverse and implicit functions#_theorem _ the inverse function theorem|the inverse function theorem]] we have a smooth inverse $h : J \to I$ ($J$ is some open subset of $\mathbb{R}$). Then we have
$$
\begin{split}
\frac{dh}{d\tau} & = \left ( \frac{d \tau}{d t} \right )^{-1} \\
& = \left \lVert \frac{d\alpha}{dt} \right \rVert^{-1} \\
& > 0
\end{split}
$$
and thus, $h : J \to I$ is a smooth function with $h'(\tau) > 0$ and $\beta = \alpha \circ h$ and thus, is an orientation preserving reparameterisation.

Finally we can calculate the velocity
$$
\begin{split}
\left \lVert \frac{d\beta}{dt} \right \rVert & = \left \lVert \frac{d\alpha}{dt} \frac{dh}{dt} \right \rVert \\
& = 1.
\end{split}
$$

Now we can go back to this diagram of our short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& & I \ar[d, "Y"] \ar[ld, "\alpha"] \ar[rd, "u"] \\
		\{ \mathbf 0 \} \ar[r] & \mathbb R^3 \ar[r, "{\mathbf p \mapsto \mathbf 0_{\mathbf p}}"'] & \mathrm T \mathbb R^3 \ar[r, "\mathbf v_{\mathbf p} \mapsto \mathbf v"'] & \mathbb R^3 \ar[r] & \{ \mathbf 0 \}
	\end{tikzcd}
\end{document}
```

Notice how although it's most natural to have $u = \dfrac{d\alpha}{dt}$, we don't have to, and if we use something different, then $Y$ doesn't have to be $\alpha'$ either. This leads to the definition of a vector field on a curve.

Again, note that the $\alpha$ arrow means the diagram doesn't commute, but we're using it to see the short exact sequence.

##### _definition:_ vector field on a curve

A vector field on a curve $\alpha$ is a map $Y : I \to \mathrm{T}\mathbb{R}^3$ such that the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& I \ar[d, "Y"] \ar[rd, "u"] \ar[ld, "\alpha"] \\
		\mathbb R^3 \ar[r, leftarrow, "\pi"'] & \mathrm T \mathbb R^3 \ar[r, "\mathbf v_{\mathbf p} \mapsto \mathbf v"'] & \mathbb R^3
	\end{tikzcd}
\end{document}
```


### Frenet-Serret frame

Recall how a [[Frames#_definition _ vector field on a curve|vector field on a curve]] allows us to assign any tangent vector part to each point on the curve. To get from this to a frame, we need a made up definition.

##### _definition:_ strongly regular

We say a curve parameterised by $\alpha$ is strongly regular if $\alpha' \times \alpha'' \neq [\mathbf{0}, \mathbf{p}]$ everywhere.

Then we can define the Frenet-Serret frame for strongly regular curves.

##### _theorem:_ the Frenet-Serret frame is a frame

For any strongly regular curve parameterised by $\alpha$ the vector fields $\{ \mathbf{T}, \mathbf{N}, \mathbf{B} \}$ form a [[Frames#_definition _ frame|frame]], where
$$
\begin{gathered}
\mathbf{T} = \frac{\alpha'}{\lVert \alpha' \rVert } \\
\mathbf{N} = \frac{{(\alpha' \cdot \alpha')\alpha'' - (\alpha' \cdot \alpha'')\alpha'}}{\lVert \alpha' \rVert \lVert \alpha' \times \alpha'' \rVert } \\
\mathbf{B} = \frac{{\alpha' \times \alpha''}}{\lVert \alpha' \times \alpha'' \rVert }.
\end{gathered}
$$

Also, there exist functions $v, \kappa, \tau : I \to \mathbb{R}$ (speed, curvature, and torsion) such that
$$
\begin{gathered}
 \alpha' = v\mathbf{T} \\
\alpha'' = v' \mathbf{T} + \kappa v^2 \mathbf{N} \\
\alpha''' = (v'' - \kappa^2 v^3) \mathbf{T} + (\kappa' v^2 + 3 \kappa v v') \mathbf{N} + (\tau \kappa v^3) \mathbf{B}
\end{gathered}.
$$

###### _proof (along with some extra stuff):_

%% see the lecture notes/homework for this %%

We want to understand how this frame changes as the curve moves. We can get the following result (it follows lots of clever tricky computation). Notice that this is just expressing the derivatives as a linear combination of $\mathbf{T}, \mathbf{N}, \mathbf{B}$

##### _proposition:_ the derivatives of the Frenet-Serret frame

Let $\omega = \tau v \mathbf{T} + \kappa v \mathbf{B}$ be the Darboux vector. Then
$$
\begin{gathered}
\mathbf{T}' = \omega \times \mathbf{T} \\
\mathbf{N}' = \omega \times \mathbf{N} \\
\mathbf{B}' = \omega \times \mathbf{B}
\end{gathered}
$$

###### _proof:_

%% again, a bunch of computation, see the lecture notes %%.

### $v$, $\kappa$, $\tau$ and what they really mean

Now that we have all of the definitions and identities, done, we can play with some examples to see what they really mean, geometrically.

##### _example:_ a circle

Consider the parameterisation of a circle by $\alpha : \mathbb{R} \to \mathbb{R}^3$ such that $t \mapsto (r \cos\omega t, r \sin \omega t, 0)$.

Then we have its derivatives as follows
$$
\begin{gathered}
\frac{{d\alpha}}{dt} = (- r \omega \sin\omega t, r\omega \cos \omega t, 0) \\
\frac{{d^2 \alpha}}{dt^2} = (-r \omega^2 \cos \omega t, - r \omega^2 \sin\omega t, 0) \\
\frac{{d^3 \alpha}}{dt^3} = (rw^3 \sin\omega t, - r\omega^3 \omega t, 0).
\end{gathered}
$$

Then
$$
\begin{gathered}
\mathbf{T} = [(- \sin \omega t, \cos \omega t, 0), \mathbf{p}] \\ \\
\mathbf{N} = [(-\cos \omega t, -\sin \omega t, 0), \mathbf{p}] \\ \\
\mathbf{B} = [(0, 0, 1), \mathbf{p}]
\end{gathered}
$$
where $\mathbf{p} = \alpha(t)$.

Now we can calculate speed, curvature and torsion as well —
$$
\begin{gathered}
v = r \omega \\ \\
\kappa = \frac{1}{r} \\ \\
\tau = 0.
\end{gathered}
$$

Notice how $v = r \omega$ is exactly what we expect — angular speed times distance is just speed. 

Notice also that the curvature is inversely proportional to the radius. This means that our curvature somehow measures how tightly wound the coil is.

$\tau$ is $0$, so we can't learn anything about torsion from this example, except that it doesn't have any. If we are a little more interested we can notice that $\tau = 0$ exactly because $\alpha' \times \alpha''$ is in the orthogonal to the $xy$-plane that $\alpha'''$ lies in. This, gives us

##### _example:_ a helix

Consider the helix parameterised by $\alpha : \mathbb{R} \to \mathbb{R}^3$ with $t \mapsto (a \cos t, a \sin t, bt)$. Note that we don't need a $\omega$ parameter since we have one "by comparison" with $b$.

We have derivatives
$$
\begin{gathered}
\frac{{d\alpha}}{dt} = (-a \sin t, a \cos t, b) \\
\frac{{d^2 \alpha}}{dt^2} = (-a \cos t, - a \sin t, 0) \\
\frac{{d^3 \alpha}}{dt^3} = (a \sin t, - a \cos t, 0) \\
\end{gathered}
$$
which give us
$$
\begin{gathered}
\mathbf{T} = \left[ \left( -\frac{a}{\sqrt{ a^2 + b^2 }} \sin \omega t, \frac{a}{\sqrt{ a^2 + b^{2} }} \cos t, \frac{b}{\sqrt{ a^{2} + b^{2} }} \right), \mathbf{p} \right] \\ \\
\mathbf{N} = [(-\cos t, - \sin t, 0), \mathbf{p}] \\ \\
\mathbf{B} = \left[ \left( \frac{b}{\sqrt{ a^{2} + b^{2} }} \sin t, - \frac{b}{\sqrt{ a^{2} + b^{2} }}, \frac{a}{\sqrt{ a^{2} + b^{2} }} \right), \mathbf{p} \right]
\end{gathered}
$$
Then we have
$$
\begin{gathered}
v = \sqrt{ a^2 + b^2 } \\ \\
\kappa = \frac{a}{a^{2} + b^{2}} \\ \\
\tau = \frac{b}{a^2 + b^2}
\end{gathered}
$$

Notice that given any $\kappa_{0}, \tau_{0}$ we can find $a, b$ such that we have a helix of constant speed curvature, and torsion (with $\kappa_{0}$ and $\tau_{0}$ for the last two). Specifically, the helix by
$$
\alpha(t) = \left( \frac{\kappa_{0}}{\kappa_{0} + \tau_{0}} \cos t, \frac{\kappa_{0}}{\kappa_{0}^2 + \tau_{0}^2} \sin t, \frac{\tau_{0}}{\kappa_{0}^2 + \tau_{0}^2} t \right).
$$

Notice how as $\tau_{0} \to 0$, $\alpha$ approaches a circle of radius $r = \frac{1}{\kappa}$ in the $xy$-plane. When $\kappa_{0} \to 0$ then $\alpha$ approaches a vertical line with velocity $v = \frac{1}{\tau_{0}}$. This tells us that $\tau_{0}$ somehow measures the vertical "stretch". 

Note that actually having $\kappa_{0} = 0$ would make the curve not strongly regular, and so we can only look at the the limit as it approaches $0$.

This, and our example of the circle, motivates us to see that basically, a curve only has no torsion if it's a planar curve. That is $\tau$ is a measure of how far a curve is from being fixed in a plane.

##### _theorem:_ torsionless curves

For any strongly regular curve parameterised by $\alpha : I \to \mathbb{R}^3$, the following are equivalent
1) The torsion $\tau$ is $0$ everywhere.
2) The binormal vector $\mathbf{B}$ is constant (the vector part is constant).
3) There exists a plane $\mathcal{P} = \{ (x, y, z) \in \mathbb{R}^3 | ax + by + cz = d \}$ such that all $\alpha(t) \in \mathcal{P}$.

###### _proof:_

We will show that 1) $\implies$ 2) $\implies$ 3) $\implies$ 1).

Suppose a $\alpha$ has torsion $\tau = 0$. Then notice that $\frac{{d\mathbf{B}}}{dt} = - \tau v \mathbf{N}$, and thus, $\frac{d\mathbf{B}}{dt} = 0$ and $\mathbf{B}$ is a constant.

Suppose $\mathbf{B} = [(a, b, c), \alpha(t)]$ has constant vector part. Consider $\gamma : (a, b, c) \cdot \alpha(t)$. Then we have
$$
\begin{split}
\frac{d\gamma}{dt} & = (a, b, c) \cdot \frac{d\alpha}{dt} \\
& = v(\mathbf{B} \cdot \mathbf{T}) \\
& = 0
\end{split}
$$
where the last step holds by $\mathbf{B} \cdot \mathbf{T} = 0$ since they form a frame. Thus, $\gamma$ must be a constant, $d$. Then we have $a \alpha_{1}(t) + b\alpha_{2}(t) + c \alpha_{3}(t) = d$, or in other words $\alpha(t)$ always satisfies $ax + by + cz = d$ and is in the plane defined by it.

Finally, suppose $\alpha(t)$ is always in the plane $\mathcal{P}$. Then for
$$
\gamma(t) = \frac{a \alpha_{1}(t) + b \alpha_{2}(t) + c \alpha_{3}(t) - d}{\sqrt{ a^2 + b^2 + c^2 }}
$$
we have $\gamma = 0$, always.

Notice that we also have $\frac{d\gamma}{dt} = \frac{d^2\gamma}{dt^2} = 0$ with
$$
\begin{gathered}
\frac{d\gamma}{dt} = \mathbf{B}_{0} \cdot \alpha' \\
\frac{d\gamma}{dt} = \mathbf{B}_{0} \cdot \alpha''
\end{gathered}
$$
and thus, $\mathbf{B}_{0}$ orthogonal to $\mathbf{T}$ and $\mathbf{N}$ (just use the formulas in terms of $\alpha, \alpha', \alpha''$). This means that we must have $\mathbf{B} = \pm \mathbf{B}_{0}$ (with a consistent choice of sign everywhere), since the remaining vector in the orthonormal basis $\mathbf{T}, \mathbf{N}, \mathbf{B}$ must be along $\mathbf{B}_{0}$.

Then, since $\mathbf{B}$ is a constant, we have
$$
\begin{split}
\tau & = - \frac{1}{v}\left( \frac{d\mathbf{B}}{dt} \cdot \mathbf{N} \right) \\
 & = 0.
\end{split}
$$

Notice that if any of these hold then we can say, first of all, that $\alpha \subset \mathcal{P}$ is planar. Moreover, $\mathbf{B}$ is the normal vector to the plane (in one direction or the other), and since $\mathbf{T}, \mathbf{N}$ are orthogonal to it, they "generate the plane".

##### _corollary:_ torsionless curves of constant curvature

Suppose a strongly regular curve $\alpha$ has torsion $\tau = 0$ and constant curvature $\kappa$. Then $\alpha$ is contained in a circle of radius $r = \frac{1}{\kappa_{0}}$.

###### _proof:_

Here let, $\mathbf{T}, \mathbf{N}, \mathbf{B}$ represent just their vector parts. Consider $\alpha^* = \alpha + \frac{1}{\kappa} \mathbf{N}$. Thus,
$$
\begin{split}
(\alpha^*)' & = \alpha' + \frac{1}{\kappa} \mathbf{N}' \\
 & = v \mathbf{T} + \frac{1}{\kappa}(-\kappa v \mathbf{T} + \tau v \mathbf{B}) \\
 & = 0
\end{split}
$$

Thus, $\alpha^*$ is just a constant point. It turns out this is just the centre of the circle. Particularly, we can show that we always have
$$
\begin{split}
\lVert \alpha(t) - \alpha^*(t) \rVert & = \lVert \frac{1}{\kappa} \mathbf{N} \rVert  \\
 & = \frac{1}{\kappa}
\end{split}
$$
Thus, $\alpha$ is a constant distance from a fixed point, and lies in a plane $\mathcal{P}$. That is, $\alpha$ is a circle.

### Frame field?

Is the Frenet-Serret frame a frame field? It does assign a frame to each point $\mathbf{p} = \alpha(t)$, but $\mathbf{T}, \mathbf{N}, \mathbf{B}$ aren't vector fields — they are actually assigning frames to $t \in I$. Can we find vector fields $\mathbf{E}_{1}, \mathbf{E}_{2}, \mathbf{E}_{3}$ that give us
$$
\begin{gathered}
\mathbf{T}(t) = \mathbf{E}_{1}(\mathbf{p}) \\
\mathbf{N}(t) = \mathbf{E}_{2}(\mathbf{p}) \\
\mathbf{B}(t) = \mathbf{E}_{3}(\mathbf{p})
\end{gathered}
$$
where $\mathbf{v}$ is some function of $t$? Possibly, $\mathbf{p} = \alpha(t)$?

Yes we can! As long as our curve doesn't go in multiple different directions at the same point, we're good! This will lead us to the notion of simple closed curves (and simple open curves).

We won't do this rigorously right now, but basically, the circle gives us the cylindrical frame field, and the helix gives us the spherical frame field as their Frenet-Serret frames.