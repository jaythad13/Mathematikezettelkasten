---
tags:
- uc-2026/morse-theory/1
- uc-2026/morse-theory/2
- carmen-rovi
- diff-geo
- alg-top
---

Morse theory provides a "geometric" way to compute homeomorphism invariants of manifolds.

### Height functions

The first examples of Morse functions are height functions on submanifolds of $\mathbb{R}^N$.

##### _example:_ Morse theory on the sphere

Consider the unit sphere $S^{2} \subseteq \mathbb{R}^3$. We have a smooth "height function" $h : S^{2} \to \mathbb{R}$ given by $(x, y, z) \mapsto z$. We can think of this as describing the "height" of water being poured onto the surface of the sphere.

Consider the level sets (fibres) of the height function as we vary $z$. We can think of this as the shape of the intersection of the water surface with $S^2$.
$$
h^\text{pre}(z) \cong \begin{cases}
\text{Ø} & z < -1 \\
\{ * \} & z = - 1 \\
S^1 & -1< z< 1 \\
\{ * \} & z = 1 \\
\text{Ø} & z > 1
\end{cases}
$$
We can also consider the **sublevel** sets (pre-images of $(-\infty, z]$). We can think of these as the shape of the "bowl" as the water rises.
$$
h^\text{pre}((-\infty, z]) = \begin{cases}
\text{Ø} & z < -1 \\
\{ * \} & z = -1 \\
B^1 & -1 < z < 1 \\
S^2 & z \geq 1
\end{cases}
$$

We can also try the same thing on an upside down and slightly rotated (so the two legs are up in the air and not at the same height) version of Anish Kapoor's Bean (assume its hollow). Denote the bean by $X$. See the picture in the handwritten notes.

The sublevel sets are then
$$
h^\text{pre}((-\infty, z]) = \begin{cases}
\text{Ø} & z < -1 \\
\{ * \} & z = -1 \\
B^1 & -1 < z < 0 \\
S^1 \times [0, 1] / \sim & z = 0 \\
S^1 \times [0, 1] & 0 < z < 1 \\
B^1 & 1 \leq z < 2 \\
X & z \geq 2
\end{cases}
$$
where $\sim$ identifies $\{ * \} \times [0, 1/2]$ and $\{ * \} \times [1 / 2, 1]$ in the opposite direction.

---

##### _example:_ sublevel sets of the torus

Consider the torus $\mathbb{T}^2 \subseteq \mathbb{R}^3$ placed vertically as in the pictures. Then with the same height function, we have
$$
h^\text{pre}((-\infty, z]) = \begin{cases}
\text{Ø} & z < -1 \\
B^1 &  -1 < z < -1/2 \\
S^1 \times [0, 1] / \sim  & z = -1 / 2 \\
S^1 \times [0, 1] & -1 / 2 < z < 1 / 2 \\
S^1 \times [0, 1] / \sim  & z = 1 / 2 \\
B^1 & 1 / 2 < z < 1 \\
\mathbb{T}^2 & z \geq 1.
\end{cases}
$$

---

The interesting thing to note here is that the level and sublevel sets change as $z$ moves past a critical point of $h$ (where $Dh = 0$). That is, if $[z_{0}, z_{1}]$ contains no critical values, then $h^\text{pre}(z_{0}) \cong h^\text{pre}(z_{1})$ and $h^\text{pre}((-\infty, z_{0}]) \cong h^\text{pre}((-\infty, z_{1}])$. In fact, if $[z_{0}, z_{1}]$ contains no critical values, then $h^\text{pre}([z_{0}, z_{1}]) \cong h^\text{pre}(z_{0}) \times [z_{0}, z_{1}]$.

Note that the number of critical points is not an invariant of the surface — we expect the Bean $X \cong S^2$, but they have different numbers of critical poinfits. The hope however, is that we can take some sort of signed sum of the different types of critical points that is actually an invariant. Specifically, we hope (in analogy with the Euler characteristic) that
$$
\# \{ \text{minima} \} - \# \{ \text{saddle points} \} + \# \{ \text{maxima} \}
$$
is a topological invariant.

### Morse theory

Let $X$ be a smooth manifold.

The idea of Morse theory is to generalise the height functions to functions that subdivide the manifold into nice level sets. Because we have observed the behaviour change at critical points, the right idea is to consider functions with isolated (discrete) critical points.

##### _definition:_ non-degenerate, Morse type critical points

A [[UChicago --- uc-2026/notes/Manifolds background#_definition _ critical point|critical point]] of a smooth function $f : X \to \mathbb{R}$ is **non-degenerate** or of **Morse type** if its Hessian has non-zero determinant. Note that this is well-defined.

---

