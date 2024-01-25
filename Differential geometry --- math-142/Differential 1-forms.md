---
tags:
- diff-geo
- math-142
lecture: 
- math-142-3
- math-142-4
---

Recall how in multivariable calculus we had
$$
\nabla \times (\nabla f) = 0
$$
For any smooth function $f : \mathbb{R}^2 \to \mathbb{R}$. This is just a specific case of a more general phenomenon — $d^2 = 0$.

More generally we will learn to say things like
$$
\nabla f \iff df = \frac{{\partial f}}{\partial x} dx + \frac{ \partial f }{ \partial y } dy
$$
whatever that means.

### Basic definitions

##### _definition:_ differential $1$-form, $\Omega^1(\mathbb{R}^3)$

A differential $1$-form is a function $\phi : \mathrm{T}\mathbb{R}^3 \to \mathbb{R}$ which is linear on every tangent space $\mathrm{T}_{\mathbf{p}}\mathbb{R}^3$.

$\Omega^1(\mathbb{R}^3)$ is the collection of all $1$-forms on $\mathbb{R}^3$.

##### _definition:_ algebraic properties of $1$-forms

Given $\phi, \psi \in \Omega^1(\mathbb{R}^3)$, we define $\phi + \psi \in \Omega^1(\mathbb{R}^3)$ by $[\mathbf{v}, \mathbf{p}] \mapsto \phi([\mathbf{v}, \mathbf{p}]) + \psi([\mathbf{v}, \mathbf{p}])$

Given $f \in \mathcal{C}^\infty(\mathbb{R}^3)$, we define $f \phi \in \Omega^1(\mathbb{R}^3)$ by $[\mathbf{v}, \mathbf{p}] \mapsto f(\mathbf{p}) \phi(\mathbf{p})$.

##### _proposition:_ the differential $1$-forms are a vector space

$\Omega^1(\mathbb{R}^3)$ is a $\mathcal{C}^\infty(\mathbb{R}^3)$-module (and thus, an $\mathbb{R}$-vector space).

##### _proof sketch:_

It writes itself.

Note that we can do the same thing we did with [[Vector fields#_definition _ $ mathbf{V}[f]$, derivation|derivations]] and extend the definition for tangent vectors to a definition for vector fields.

##### _definition:_ differential form evaluated on a vector field

Suppose $\mathbf{V}$ is a vector field on $\mathbb{R}^3$. Then let $\phi_{*}(\mathbf{V})$ (sometimes by abuse of notation $\phi(\mathbf{V})$) be the function given by
$$
\mathbf{p} \mapsto \phi(\mathbf{V}(\mathbf{p})).
$$

This is really an example of the push-forward — a $1$-form taking a vector field and given every point $\mathbf{p} \in \mathbb{R}^3$, it evaluates itself at $\mathbf{V}(\mathbf{p})$. That is, the following diagram commutes.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathbb R^3 \ar[r, "\mathbf V"] \ar[rr, "\phi_*(\mathbf V)"', bend right] & \mathrm T \mathbb R^3 \ar[r, "\phi"] & \mathbb R 
	\end{tikzcd}
\end{document}
```

Note that we have linearity in the vector fields as well as the forms.

##### _proposition:_ the push-forward of a $1$-form is linear two ways

For any $\phi, \psi \in \Omega^1(\mathbb{R}^3)$, $f, g \in \mathcal{C}^\infty(\mathbb{R}^3)$ and vector fields $\mathbf{V}$ and $\mathbf{W}$ on $\mathbb{R}^3$, we have 
1) $(f \phi + g \psi)_*(\mathbf{V}) = f \phi_{*}(\mathbf{V}) + g \psi_{*}(\mathbf{W})$
2) $\phi_{*}(f \mathbf{V} + g \mathbf{W}) = f \phi_{*}(\mathbf{V}) + g \phi_{*}(\mathbf{W})$

##### _proof sketch:_

1) follows literally by definition
and
2) follows from the linearity of the differential form $\phi$ on its inputs. 

### Getting back to the gradient

To get back to the gradient, we will see how thinking about the derivative makes sense.

##### _definition:_ the differential/exterior derivative of a $1$-form

For any smooth function $f : \mathbb{R}^3 \to \mathbb{R}$, define the map $df : \mathrm{T}\mathbb{R}^3 \to \mathbb{R}$ by
$$
[\mathbf{v}, \mathbf{p}] \mapsto Df \Big |_{\mathbf{p}} (\mathbf{v}).
$$

##### _proposition:_ the differential is a $1$-form

For any smooth function $f : \mathbb{R}^3 \to \mathbb{R}$, $df \in \Omega^1(\mathbb{R}^3)$

##### _proposition:_ $d$ is a linear map

The map $d : \mathcal{C}^\infty(\mathbb{R}^3) \to \Omega^1(\mathbb{R}^3)$ by $f \mapsto df$ is well defined and linear.

The big question that this raises is

Are there $1$-forms that aren't $df$ for some $f$?

##### _theorem:_ decomposing $1$-forms

Let $\phi \in \Omega(\mathbb{R}^3)$. We can find smooth functions, $f_{1}, f_{2}, f_{3} : \mathbb{R}^3 \to \mathbb{R}$ so that
$$
\phi : f_{1} \, dx_{1} + f_{2} \, dx_{2} + f_{3} \, dx_{3}.
$$
Moreover, for any $f \in \mathcal{C^\infty}(\mathbb{R}^3)$, then
$$
df = \frac{ \partial f }{ \partial x_{1} } \, dx_{1} + \frac{ \partial f }{ \partial x_{2} } \, dx_{2} + \frac{ \partial f }{ \partial x_{3} } \, dx_{3}
$$

##### _proof sketch:_

For the first part, pick any vector field and decompose it, and then choose $f_{i} = \mathbf{U}_{i}$. The second part follows.