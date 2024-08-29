---
tags:
- math-135/2
- anal
---

##### _definition:_ holomorphic, $\mathbb{C}$-differentiable, regular, the derivative, $f'(z_{0})$

Given some open $\Omega \subset \mathbb{C}$, a function $f : \Omega \to \mathbb{C}$ is called holomorphic, $\mathbb{C}$-differentiable, or regular at $z_{0} \in \mathbb{C}$ if
$$
\lim_{ h \to 0 } \frac{f(z_{0} + h) - f(z_{0})}{h}
$$
exists.

If $f$ is holomorphic, that limit is called $f'(z_{0})$, the derivative of $f$.

Note that this is equivalent to the idea that there exists a good linear approximation of the function at $z_{0}$ called $f'(z_{0})$. An exercise is to use this idea to prove that the sum rule, product rule, quotient rule, and chain rule hold.

$f$ is holomorphic on an open set if it's holomorphic on all of its points. $f$ is holomorphic on a closed set if it's holomorphic on an open superset.

Most of the obvious examples of differentiable functions from $\mathbb{R}$ hold —

##### _example:_ holomorphic functions

$f : z \mapsto z$ is holomorphic everywhere on $\mathbb{C}$ with $f'(z) = 1$ everywhere. $f : z \mapsto 1 / z$ is holomorphic everywhere except $0$ with $f'(z) = 1 / z^{2}$.

But it's more instructive to look at the non-examples — functions that are differentiable on $\mathbb{R}^{2}$ but not $\mathbb{C}$. 

##### _non-examples:_ holomorphic functions

$f : z \mapsto \overline{z}$ is not holomorphic even though it corresponds to $F : (x, y) \mapsto (x, -y)$ which is differentiable on $\mathbb{R}^{2}$. Take limits along the real and imaginary lines to see why.

$f : z \mapsto z \overline{z}$ is also not holomorphic — for similar reasons. The corresponding $F : (x, y) \to \lVert (x, y) \rVert$ which is very differentiable.

### Cauchy-Riemann equations

The Cauchy-Riemann equations give the conditions for a function that's differentiable on $\mathbb{R}^2$ to be differentiable on $\mathbb{C}$.

##### _theorem:_ Cauchy-Riemann equations

For a function $f$ we need $u_{x} = v_{y}$ and $u_{y} = - v_{x}$ for it to be holomorphic.

See Looman-Menchoff theorem for the (partial) converse (it's in Narasimhan and only requires that $f$ be continuous).

%%all of the crazy new differential operator nonsense%%

