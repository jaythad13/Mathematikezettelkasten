---
tags:
- math-142/8
- diff-geo
---

We've dealt a lot with maps $f: \mathbb{R}^3 \to \mathbb{R}$ and $F : \mathbb{R}^3 \to \mathbb{R}^3$. Let's talk about maps $F : \mathbb{R}^n \to \mathbb{R}^m$.

### Cells — curves on steroids

Recall our definitions of [[Vector fields#_(temporary) definition _ curves, paths in $ mathbb{R} 3$|curves]], [[Differential Geometry --- math-142/notes/Curves#_definition _ reparameterisation|parameterisation and reparameterisation]] and [[Differential Geometry --- math-142/notes/Curves#_definition _ tangent vector to a curve|tangent vectors]]. Also recall that we can treat a [[Differential Geometry --- math-142/notes/Curves#_proposition _ you can use $ alpha'$ like a vector field|curves as a vector field]], and from a parameterisation $\alpha$ and a smooth function $f$ we can get $\alpha[f]$. We can generalise this to get something new.

Note that by [[Differentiability theorems#_theorem _ the projection principle holds for differentiability|the projection principle]], we can say any $F : \mathbb{R}^n \to \mathbb{R}^m$ by $F(\mathbf{x}) = (f_{1}(\mathbf{x}), \dots,  f_{m}(\mathbf{x}))$ is differentiable if its component functions $f_{i}$ are $\mathcal{C}^1$. We can impose a stricter requirement

##### _definition:_ mapping

We say $F : \mathbb{R}^n \to \mathbb{R}^m$ with $F = (f_{1}, \dots, f_{m})$ is a mapping if each of its component functions $f_{i} \in \mathcal{C}^\infty(\mathbb{R}^n)$.

Just like with curves, we want to look at the images of the mapping. But how do we get any visual idea of what it is? How do we "plot out" a mapping? 

### Tangent maps

Say we have a mapping $F : \mathbb{R}^n \to \mathbb{R}^m$, with $F = (f_{1}, \dots, f_{m})$. One natural thing to think about is the image of a curve under $F$. That is, for a (parameterisation of a) curve $\alpha : I \to \mathbb{R}^n$, the composition $\beta = F \circ \alpha$ is the image of $\alpha$ under $F$. That is, the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		I \ar[d, "\alpha"] \ar[rd, "\beta"] \\
		\mathbb R^n \ar[r, "F"] & \mathbb R^m
	\end{tikzcd}
\end{document}
```

We care particularly about when $\alpha$ gives a line —
$$
\alpha(t) = \mathbf{p} + t \mathbf{v}.
$$

For this, we have $\beta(t) = F(\alpha(t))$, which by the chain rule is just approximately
$$
F(\mathbf{p}) + DF \Big |_{\mathbf{p}}(t \mathbf{v}).
$$

Note how this defines a map $F_{*} : \mathrm{T}\mathbb{R}^n \to \mathrm{T}\mathbb{R}^m$ that takes a tangent vector $[\mathbf{v}, \mathbf{p}]$ and returns $[DF \Big |_{\mathbf{p}}(\mathbf{v}), F(\mathbf{p})]$. This pushforward is what we call the tangent map.

##### _definition:_ tangent map

For a mapping $F : \mathbb{R}^n \to \mathbb{R}^m$, the tangent map $F_{*} : \mathrm{T}\mathbb{R}^n \to \mathrm{T}\mathbb{R}^m$ is given by
$$
[\mathbf{v}, \mathbf{p}] \mapsto [DF \Big |_{\mathbf{p}}(\mathbf{v}), F(\mathbf{p})].
$$

This basically says that given a map between spaces, we can push forward to a map between their tangent bundles.

It has some nice properties that just follow from [[Differentiability theorems|differentiability theorems]].

##### _proposition:_ the tangent map is linear on each tangent space

Given $[\mathbf{v}, \mathbf{p}], [\mathbf{w}, \mathbf{p}] \in \mathrm{T}_{\mathbf{p}}\mathbb{R}^n$, $a, b \in \mathbb{R}$, and a mapping $F : \mathbb{R}^n \to \mathbb{R}^m$
$$
F_{*}(a[\mathbf{v}, \mathbf{p}] + b[\mathbf{w}, \mathbf{p}]) = a F_{*}([\mathbf{v}, \mathbf{p}]) + b F_{*}([\mathbf{v}, \mathbf{p}])
$$

###### _proof sketch:_

[[The derivative#_definition _ derivative, differentiability|The derivative is a linear map]].

##### _proposition:_ the chain rule for tangent maps

Given mappings $F : \mathbb{R}^n \to \mathbb{R}^m$ and $G : \mathbb{R}^m \to \mathbb{R}^p$, we have
$$
(F \circ G)_{*} = F_{*} \circ G_{*}.
$$

###### _proof sketch:_

Follows from [[Differentiability theorems#_theorem _ chain rule|the chain rule]].

##### _proposition:_ regularity

For a point $\mathbf{p} \in \mathbb{R}^n$, and a mapping $F : \mathbb{R}^n \to \mathbb{R}^m$ the following are equivalent
- the restriction $F_{*} : \mathrm{T}_{\mathbf{p}}\mathbb{R}^n \to \mathrm{T}_{F(\mathbf{p})}\mathbb{R}^m$ is one to one
- $DF \Big |_{\mathbf{p}}$ is one to one
- there exists an open set $U \subset \mathbb{R}^n$ containing $\mathbf{p}$ such that the restriction $F_{|U}$ is a differentiable, one-to-one map.

###### _proof sketch:_

Follows from the [[Inverse and implicit functions#_theorem _ the inverse function theorem|inverse function theorem]].