---
tags:
- math-131/20
- math-131/22
- anal
---

##### _definition:_ differentiability, the derivative

Suppose $f : (a, b) \to \mathbb{R}$. We say that $f$ is differentiable at $x \in (a, b)$ if
$$
\lim_{ h \to 0 } \frac{f(x + h) - f(x)}{h}
$$
exists.

If the limit exists, it is called the derivative of $f$ at $x$ and is denoted $f'(x)$.

Note that this is equivalent to saying that there exists some [[Linear maps|linear operator]] $\mathbb{R} \to \mathbb{R}$ scaling by $f'(x)$ that gives
$$
\lim_{ h \to 0 } \frac{f(x + h) - f(x) - f'(x) h}{h} = 0.
$$

That is, the linear operator is a good local linear approximation to the function. This idea is exactly encoded in the definition of the [[Calculus --- spivak/notes/The derivative#_definition _ derivative, differentiability|derivative of a function of many variables]].

##### _definition:_ the error function

We define the error function of $f$ to be
$$
\psi_{f}(x, h) = f(x + h) - f(x) - f'(x) h.
$$

Then for $f$ to be differentiable is equivalent to $\lim_{ h \to 0 } \psi_{f}(x, h) / h = 0$.

##### _theorem:_ differentiability implies continuity

If $f : (a, b) \to \mathbb{R}$ is differentiable at $x \in (a, b)$, then $f$ is continuous at $x$.

###### _proof:_

Suppose $y \in (a, b)$. Then
$$
\begin{split}
\lim_{ y \to x } f(y) & = \lim_{ y \to x } f(x + y - x) \\
 & = \lim_{ y \to x } f(x) + f'(x) \, (y - x) + \psi(x, y - x) \\
 & = f(x) + 0 + 0.
\end{split}
$$

### Differentiability rules

Derivatives play very nicely with the things we might want to do with real numbers

##### _proposition:_ the sum rule

If $f, g : (a, b) \to \mathbb{R}$ are differentiable at $x \in (a, b)$, then $f + g : (a, b) \to \mathbb{R}$ is differentiable at $x$ with $(f + g)'(x) = f'(x) + g'(x)$.

##### _proposition:_ the product rule

If $f, g : (a, b) \to \mathbb{R}$ are differentiable at $x \in (a, b)$, then $fg : (a, b) \to \mathbb{R}$ is differentiable at $x$ with $(fg)'(x) = f'(x) g(x) + f(x) g'(x)$.

##### _proposition:_ the quotient rule

If $f , g : (a, b) \to \mathbb{R}$ are differentiable at $x \in (a, b)$ and $g(x) \neq 0$, then $f/g : (a, b) \to \mathbb{R}$ is differentiable at $x$ with
$$
\left( \frac{f}{g} \right)'(x) = \frac{f'(x) g(x) - f(x) g'(x)}{g(x)^{2}}.
$$

##### _proposition:_ the chain rule

If $f : (a, b) \to \mathbb{R}$ and $g : (c, d) \to \mathbb{R}$ are differentiable at $x$ and $f(x)$ respectively, then $h = g \circ f$ is differentiable with
$$
h'(x) = g'(f(x)) f'(x).
$$

### Higher order derivative

If $f : I \to \mathbb{R}$ is differentiable everywhere on its domain, then we have a function $f' : I \to \mathbb{R}$ that sends $x$ to $f'(x)$. What if this function is differentiable?

##### _definition:_ higher-order derivatives

If $f$ is differentiable, $f'$ is its first derivative. If $f$ has a differentiable $n$th derivative $f^{(n)}$, the $(n + 1)$th derivative of $f$ is $(f^{(n)})'$.

If $f$ has an $n$th derivative, we say it is $n$ times differentiable.