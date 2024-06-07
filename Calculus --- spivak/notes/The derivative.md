---
tags:
- spivak
- anal
- calc
- self-study
---

In single-variable calculus, we defined the derivative of a function $f : \bb R \to \bb R$ at $a$ to be the number
$$
f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}.
$$
We could then think of $f'(a)$ as the slope of the line tangent to $f$ at $a$. Basically, $f'(a) \Delta x$ was a good approximation of the change $f(a + \Delta x) - f(a)$. In fact, it's also a linear approximation. We could rewrite this whole thing in this language of linear approximation.

For any linear transformation $T$ given by $T x = f'(a) x$, we say $f'(a)$ is the derivative of $f$ at $a$ if 
$$
\lim_{h \to 0} \frac{f(a + h) - f(a) - Th}{h} = 0.
$$

Basically, the derivative is a linear approximation of the change in function value (for small changes in the input value) that it converges to the actual change faster than the input value converges to the point at which we're evaluating the derivative.

> In the classical teaching of calculus, this idea is immediately obscured by the accidental fact that, one a one dimensional vector space, there is a one to one correspondence between linear forms and numbers, and therefore the derivative is defined as a number instead of a linear form.

\- Jean Dieudonné

While the first definition doesn't generalise well at all, this second one does! It's precisely how we define the derivative!

##### _definition:_ derivative, differentiability

For a function $f : A \to \bb R^m$, ($A \subset \bb R^n$) $f$ is differentiable at $\bvec a$ if there is a [[Linear maps|linear map]] $T : \bb R^n \to \bb R^m$ such that 
$$
\lim_{\bvec v \to \bvec 0} \frac{\norm{f(\bvec a + \bvec v) - f(\bvec a) - T \bvec v}}{\norm{\bvec v}} = 0.
$$

$Df \Big |_{\bvec a} = T$ is the derivative of $f$ at $\bvec a$.

Note that for this limit to exist, $\bvec a$ must be contained in some open subset of $A$.

Note that we call $Df \Big |_{\bvec a}$ _the_ derivative of $f$ at $\bvec a$. We can show that this title is deserved.

##### _proposition:_ the derivative is unique

If $f : A \to \bb R^m$ is differentiable at $\bvec a \in A$, there is a unique linear map $T : \bb R^n \to \bb R^m$ such that
$$
\lim_{\bvec v \to \bvec 0} \frac{\norm{f(\bvec a + \bvec v) - f(\bvec a) - T \bvec v}}{\norm{\bvec v}} = 0.
$$

###### _proof:_

By the definition of differentiability, this linear map already exists. Now we just have to show that any linear map satisfying the same property must be the same linear map.

Suppose $S$ is a linear map $S : \bb R^n \to \bb R^m$ satisfying the desired limit. Then note that
$$
\begin{split}
\lim_{\bvec v \to \bvec 0} \frac{\norm{T \bvec v - S \bvec v}}{\norm{\bvec v}} & = \lim_{\bvec v \to \bvec 0} \frac{\norm{(f(\bvec a + \bvec v) - f(\bvec a) - S \bvec v) - (f(\bvec a + \bvec v) - f(\bvec a) - T \bvec v)}}{\norm{\bvec v}} \\
& \le \lim_{\bvec v \to 0} \frac{\norm{f(\bvec a + \bvec v) - f(\bvec a) - S \bvec v}}{\norm{\bvec v}} + \frac{\norm{f(\bvec a + \bvec v) - f(\bvec a) - T \bvec v}}{\norm{\bvec v}} \\
& = 0.
\end{split}
$$
Thus, for any $\bvec v \in \bb R^n$ we have 
$$
\lim_{\alpha \to 0} \frac{\norm{T(\alpha \bvec v) - S(\alpha \bvec v)}}{\norm{\alpha \bvec v}} = 0. 
$$
and thus,
$$
\begin{split}
\lim_{\alpha \to 0} \frac{\norm{T(\alpha \bvec v) - S(\alpha \bvec v)}}{\norm{\alpha \bvec v}} & = \lim_{\alpha \to 0} \frac{\abs{\alpha}}{\abs{\alpha}} \frac{\norm{T \bvec v - S \bvec v}}{\norm{\bvec v}} \\
& = \frac{\norm{T \bvec v - S \bvec v}}{\norm{\bvec v}} \\
& = 0.
\end{split}
$$
Thus, $\norm{T \bvec v - S \bvec v} = 0$ and $S \bvec v = T \bvec v$ for all $\bvec v \in \bb R^n$. That is, $S = T$, and the derivative is unique.

This result will later allow us to prove a simple method to compute the derivative (we just show that that method satisfies the limit). Also note that this explains why it's important to consider the limit of $\lVert T \mathbf{v} - S \mathbf{v} \rVert/\lVert \mathbf{v} \rVert$ and not just the numerator by itself.

##### _example:_ the derivative

For $f : \bb R^2 \to \bb R$ with $f(x, y) = \sin{x}$ we have $Df \Big |_{\bvec a} = T$ where $T \bvec v = (\cos{a_1}, 0)$ for $\bvec a = \cos(a_1) v_1$ for $\bvec a = (a_1, a_2), \bvec v = (v_1, v_2)$.

We can prove this by showing that the limit definition holds.
$$
\begin{split}
\lim_{\bvec v \to \bvec 0} \frac{\norm{f(\bvec a + \bvec v) - f(\bvec a) - T \bvec v}}{\norm{\bvec v}} & = \lim_{\bvec v \to \bvec 0}\frac{\norm{\sin{(a_1 + v_1) - \sin{a_1} - v_1 \cos{a_1}}}}{\norm{\bvec v}} \\
& \le \lim_{v_1 \to 0} \frac{\abs{\sin(a_1 + v_1) - \sin{a_1} - v_1 \cos{a_1}}}{\abs{v_1}} \\
& = \lim_{v_1 \to 0}\frac{\abs{\sin{a_1} \cos{v_1} + \cos{a_1} \sin{v_1} - \sin{a_1} - v_1 \cos{a_1}}}{\abs{v_1}} \\
& \le \lim_{v_1 \to 0} \frac{\abs{\sin{a_1}(\cos{v_1} - 1)} + \abs{\cos{a_1}(\sin{v_1} - v_1)}}{\abs{v_1}} \\
& = \lim_{v_1 \to 0} \frac{\abs{\sin{a_1}} \abs{\sin{(v_1/2)}}^2}{\abs{v_1/2}} + \frac{\abs{\cos{a_1}} \abs{\sin{v_1} - v_1}}{\abs{v_1}} \\
& \le \sin{a_1} \lim_{v_1 \to 0} \sin{(v_1/2)} + \abs{\cos{a_1}} \lim_{v_1 \to 0} \frac{\abs{\sin{v_1}}}{\abs{v_1}} - \frac{\abs{v_1}}{\abs{v_1}}\\
& = 0.
\end{split}
$$


As you can see at the start of this example, writing down the derivative of a function can be tedious — you have to define a whole linear map. An easier way to do this, is to just think about its matrix with respect to some agreed upon basis.

##### _definition:_ the Jacobian matrix

For any function $f : A \to \bb R^m$, ($A \subset \bb R^n$) differentiable at $\bvec a$, the Jacobian matrix of $f$ at $\bvec a$ is the matrix (with respect to the [[Linear algebraic considerations#_notation _ $ bvec e_1, ldots bvec e_n$|standard basis]] of $\bb R^n$) of its derivative $Df \Big |_{\bvec a}$.