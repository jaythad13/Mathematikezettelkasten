---
tags:
- math-142
- diff-geo
lecture:
- math-142-23
- math-142-24
- math-142-25
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

###### _proof sketch:_

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

###### _(non)proof:_

Follows from [[#_proposition _ Euclidean motions preserve vector fields over a curve|our results on vector fields on curves]].

##### _theorem:_ Frenet-Serret frames are invariant under orientation-preserving Euclidean motions

Say we have a curve $\alpha$ with Frenet-Serret apparatus $v, \kappa, \tau, \mathbf{T}, \mathbf{N}, \mathbf{B}$, and $\overline{\alpha} = F \circ \alpha$ for some Euclidean motion $F$ has Frenet-Serret apparatus $\overline{v}, \overline{\kappa}, \overline{\tau}, \overline{\mathbf{T}}, \overline{\mathbf{N}}, \overline{\mathbf{B}}$. Then
$$
\begin{aligned}
\overline{v} & = v & \overline{\kappa} & = \kappa & \overline{\tau} & = \operatorname{sgn} F \, \tau \\
\overline{\mathbf{T}} & = F_{*} \circ \mathbf{T} & \overline{\mathbf{N}} & = F_{*} \circ \mathbf{N} & \mathbf{B} & = \operatorname{sgn} F (F_{*} \circ \mathbf{B})
\end{aligned}
$$

###### _proof sketch:_

Just push the definitions through $F$ [[#_proposition _ Euclidean motions preserve vector fields over a curve|our results on vector fields on curves]].

This leads us to believe that if two curves have all the same speed, curvature, and torsion, they are just the same curve, displaced by a Euclidean motion. Basically, curves are completely determined by their speed, curvature, and torsion. This is basically just the converse of the previous result.

##### _theorem, definition:_ congruence of curves

Say $\alpha, \beta : I \to \mathbb{R}^3$ are strongly regular curves. Then, the following are equivalent
1) There exists some $F \in \mathcal{E}_{3}$ such that $\beta = F \circ \alpha$.
2) $v_{\alpha} = v_{\beta}$, $\kappa_{\alpha} = \kappa_{\beta}$, and $\lvert \tau_{\alpha}  \rvert = \lvert \tau_{\beta} \rvert$.

If either holds, we say, $\alpha$ is congruent to $\beta$, denoted by $\alpha \equiv \beta$.

Congruence is an equivalence relation on (strongly regular) curves.

###### _proof:_

We've already shown 1) $\implies$ 2) in our previous result.

Suppose we have 2). That is, we have $v_{\alpha} = v_{\beta}$, $\kappa_{\alpha} = \kappa_{\beta}$, and $\lvert \tau_{\alpha}  \rvert = \lvert \tau_{\beta} \rvert$. Let $\mathbf{e}_{1}, \mathbf{e}_{2}, \mathbf{e}_{3}$ be the Frenet-Serret frame at $\mathbf{p} = \alpha(t)$ at some fixed $t_{0} \in I$. Similarly, define $\mathbf{f}_{1}, \mathbf{f}_{2}, \mathbf{f}_{3}$ and $\mathbf{q}$ for $\beta$.

Recall that at each point [[Proper Euclidean motions#_theorem _ isometries keep track of frame fields|there is a unique Euclidean motion]] $F$ that sends $\mathbf{p}$ to $\mathbf{q}$ and (whose pushforward $F_{*}$) sends each $\mathbf{e}_{i}$ to $\mathbf{f}_{i}$. Pick $F$ at $t_{0}$, and then write $\overline{\alpha} = F \circ \alpha$. We will show that $\overline{\alpha} = \beta$. We will do this by showing that it has exactly the same Frenet-Serret frame.

Consider $f : I \to \mathbb{R}^3$ by $f(t) = \overline{\mathbf{T}}(t) \cdot \mathbf{T}_{\beta}(t) + \overline{\mathbf{N}(t)} \cdot \mathbf{N}_{\beta}(t) + \overline{\mathbf{B}}(t) \cdot \mathbf{B}_{\beta}(t)$. It's clear by [[Norms#_theorem:_ Cauchy-Schwartz inequality|Cauchy-Schwartz]] that $f(t) \le 3$ with equality if and only if $\overline{\mathbf{T}}(t) = \mathbf{T}_{\beta}(t)$, $\overline{\mathbf{N}}(t) = \mathbf{N}_{\beta}(t)$, and $\overline{\mathbf{B}}(t) = \mathbf{B}_{\beta}(t)$. Thus $f(t_{0}) = 3$. We claim that $f$ is constant. We show this by computing
$$
\frac{df}{dt} = \left( \frac{d \overline{\mathbf{T}}}{dt} \cdot \mathbf{T}_{\beta} + \overline{\mathbf{T}} \cdot \frac{d \mathbf{T}_{\beta}}{dt} \right) + \left( \frac{d \overline{\mathbf{N}}}{dt} \cdot \mathbf{N}_{\beta} + \overline{\mathbf{N}} \cdot \frac{d \mathbf{N}_{\beta}}{dt} \right) + \left( \frac{d \overline{\mathbf{B}}}{dt} \cdot \mathbf{B}_{\beta} + \overline{\mathbf{B}} \cdot \frac{d \mathbf{B}_{\beta}}{dt} \right)
$$
which we can resolve using the [[Frenet-Serret frames#_proposition _ the derivatives of the Frenet-Serret frame|formulas for the derivatives of the Frenet-Serret frame]]. This gives us
$$
\frac{df}{dt} = 0.
$$

Note that in this step we are allowing ourselves to dot $\overline{\mathbf{T}}$ and $\mathbf{T}_{\beta}$ even though they might not be at the same point. We deal with this by taking the dot product of their vector parts, even if they're not at the same point.

Since $\frac{df}{dt} = 0$, $f$ must be constant, and thus, $f(t) = 3$ for all $t \in I$. Thus, $\overline{\mathbf{T}}(t) \cdot \mathbf{T}_{\beta}(t) = \lVert \overline{\mathbf{T}}(t) \rVert \lVert \mathbf{T}_{\beta}(t) \rVert$, giving us that $\overline{\mathbf{T}}(t)$ is parallel to $\mathbf{T}_{\beta}(t)$. Since they have the same length, they must be exactly the same (in their vector part). Since each of the derivatives, $\frac{d \overline{\alpha}_{i}}{dt} = \frac{d\beta_{i}}{dt}$, we have $\overline{\alpha} = \beta + \mathbf{p}$ for some constant $\mathbf{p}$. Since $\overline{\alpha}(t_{0}) = \beta(t_{0})$, $\mathbf{p} = 0$, and $\overline{\alpha} = \beta$ always. That is, $F(\alpha) = \beta$.