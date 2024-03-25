---
tags:
- math-142
- diff-geo
lecture:
- math-142-23
- math-142-24
---

### The big picture — Euclidean geometry

Felix Klein roughly thought of geometry as the study of things that are invariant under a certain symmetry group. Then, Euclidean geometry should be the study of things in [[Euclidean space]] that are invariant under symmetries of the group of [[Proper Euclidean motions|proper Euclidean motions]].

Basically, if two things differ by a proper Euclidean motion, they're the same thing.

### Euclidean geometry for curves

Recall the notion of a [[Frenet-Serret frames#Vector fields on a curve|vector fields on a curve]] and their associated commutative diagram. What happens when we apply a proper Euclidean motion to it?

Say we apply an Euclidean motion $F = T \circ C$, where $T$ is a translation and $C$ is an orthogonal transformation.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& I \ar[d, "\mathbf Y"] \ar[rd, "u"] \ar[ld, "\alpha"] \\
		\mathbb R^3 \ar[r, leftarrow, "\pi"'] \ar[d, "F"] & \mathrm T \mathbb R^3 \ar[r, "\mathbf v_{\mathbf p} \mapsto \mathbf v"'] \ar[d, "F_*"] & \mathbb R^3 \ar[d, "C"] \\
		\mathbb R^3 \ar[r, leftarrow, "\pi"'] & \mathrm T \mathbb R^3 \ar[r, "\mathbf v_{\mathbf p} \mapsto \mathbf v"'] & \mathbb R^3 \\
	\end{tikzcd}
\end{document}
```

What this means is that if $\mathbf{Y}$ is a vector field on $\alpha$, then $\overline{\mathbf{Y}} = F_{*} \circ \alpha$ forms a vector field on $\overline{\alpha} = F \circ \alpha$ that is in some sense equivalent. We can make this exact by looking at what happens to [[Frenet-Serret frames]] along a strongly regular curve. We should expect them to be basically the same, so that then we can do physics on them. Specifically, we want to prove something like
##### _theorem:_ Frenet-Serret frames are invariant under orientation-preserving Euclidean motions

which we will make precise later. First, some bookkeeping.

##### _notation:_ $\overline{\alpha}$, $\overline{\mathbf{Y}}$

For any strongly regular curve $\alpha$ and a vector field $\mathbf{Y}$ on it, let $\overline{\alpha}$ denote $F \circ \alpha$ and let $\overline{\mathbf{Y}}$ denote the vector field $F_{*} \circ \mathbf{Y}$ on it.

It's obvious that we should expect Euclidean motions to preserve vector fields, and they do!

##### _proposition:_ Euclidean motions preserve vector fields over a curve

Suppose $\mathbf{X}, \mathbf{Y} : I \to \mathrm{T}\mathbb{R}^3$ are vector fields on a curve $\alpha$, and $f, g \in \mathcal{C}^\infty(I)$. 
1) Then $\mathbf{Z} = f \mathbf{X} + g \mathbf{Y}$ satisfies $\overline{\mathbf{Z}} = f \overline{\mathbf{X}} + g \overline{\mathbf{Y}}$.
2) $\overline{\mathbf{X}} \cdot \overline{\mathbf{Y}} = \mathbf{X} \cdot \mathbf{Y}$
3) $\lVert \overline{\mathbf{Y}} \rVert = \lVert \mathbf{Y} \rVert$
4) $\overline{\mathbf{X} \times \mathbf{Y}} = \operatorname{sgn} F(\overline{\mathbf{X}} \times \mathbf{Y})$
5) $\overline{\mathbf{Y}'} = \overline{\mathbf{Y}}'$

##### _proof sketch:_

The first part follows from the linearity of the vector part of $F_{*}$. The second and third parts follows from the fact that $F_{*}$ preserves dot products. The fourth part follows from the fact that $F_{*}$ [[Orientation#_proposition _ (tangent maps of) proper Euclidean motions preserve cross products upto sign|preserves cross products, upto sign]]. The last part follows from the linearity of the derivative and the linearity of the vector part of $F_{*}$.

Let's look at an example for the [[Frenet-Serret frames|Frenet-Serret frame]] of a curve.

##### _example:_ Euclidean motions on a circular helix

Consider a circular helix parameterised by $\alpha : I \to \mathbb{R}^3$ such that $\alpha(t) = (a \cos t, a \sin t, bt)$. 

If we rotate the helix $\vartheta$ counterclockwise about the $z$ axis, then we just get $\overline{\alpha}(t) = (a \cos (t + \vartheta), a \sin(t + \vartheta), b t)$. Thus, nothing changes sign. If we reflect $\alpha$ in the $xy$-plane, then we just send $z$ to $-z$, and thus, only the torsion changes sign. These are basically the only types of orthogonal transformations, and we know that translations really just affect the point part of vectors, so we don't need to care about them either.

Then, with some bookkeeping, to make sure the Frenet-Serret frame is actually well-defined, we have our theorem.

##### _proposition:_ the Frenet-Serret frame on $\overline{\alpha}$ is well-defined

For any Euclidean motion $F$, let $\overline{\alpha}$ denote $F \circ \alpha$. Then
$$
\lVert \overline{\alpha}' \rVert = \lVert \alpha' \rVert  
$$
and
$$
\lVert \overline{\alpha}' \times \overline{\alpha}'' \rVert = \lVert \alpha' \times \alpha'' \rVert.
$$

Thus, $\overline{\alpha}$ is strongly regular if and only if $\alpha$ is strongly regular.

##### _(non)proof:_

Follows from [[#_proposition _ Euclidean motions preserve vector fields over a curve|our results on vector fields on curves]].

##### _theorem:_ Frenet-Serret frames are invariant under orientation-preserving Euclidean motions

Say we have a curve $\alpha$ with Frenet-Serret apparatus $v, \kappa, \tau, \mathbf{T}, \mathbf{N}, \mathbf{B}$, and $\overline{\alpha} = F \circ \alpha$ for some Euclidean motion $F$ has Frenet-Serret apparatus $\overline{v}, \overline{\kappa}, \overline{\tau}, \overline{\mathbf{T}}, \overline{\mathbf{N}}, \overline{\mathbf{B}}$. Then
$$
\begin{aligned}
\overline{v} & = v & \overline{\kappa} & = \kappa & \overline{\tau} & = \tau \\
\overline{\mathbf{T}} & = F_{*} \circ \mathbf{T} & \overline{\mathbf{N}} & = F_{*} \circ \mathbf{N} & \mathbf{B} & = \operatorname{sgn} F (F_{*} \circ \mathbf{B})
\end{aligned}
$$

##### _proof sketch:_

Just push the definitions through $F$ [[#_proposition _ Euclidean motions preserve vector fields over a curve|our results on vector fields on curves]].