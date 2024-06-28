---
tags:
- spivak/mnfld/2
- anal
- calc
- self-study
---

### Partials

Partials allow us to think about changes in just one of the "variables" of a multivariable function to $\bb R$, and the resultant changes in its value. It's kind of obvious why we might want to do this — they define a sort of tangent to a curve in the graph of the function.

##### _definition:_ the $j$th partial derivative

If $f : A \to \bb R$ ($A \subset \bb R^n$) and $\bvec a \in A$, if the limit
$$
\lim_{h \to 0} \frac{f(a_1, \ldots, a_j + h, \ldots, a_n) - f(\bvec a)}{h}
$$
exists, it is denoted $D_j f \Big |_{\bvec  a}$, or classically, $\pardx{f}{\bvec e_j}(\bvec a)$. It is called the $j$th partial derivative of $f$ at $\bvec a$.

The function $D_j f \Big |_{\bvec x} : B \to \bb R$ (where $B \subset A$ such that the $j$th partial exists at each $\bvec b \in B$) is called the $j$th partial derivative of $f$.

Note that this is just the derivative of $g : \bb R \to \bb R$ at $a_j$ where $g(x) = f(a_1, \ldots, a_{j - 1}, x, a_{j + 1}, \ldots, a_n)$, and by what we know from single variable calculus, $D_j f \Big |_{\bvec a}$ is the tangent line to the curve formed by intersecting $x_j = a_j$ with the graph of $f$. This also means that we can reduce the computation of partials to a problem from single variable calculus — just differentiate with respect to $x_j$, and treat all of the other $x_i$ like constants (or even explicitly substitute in $a_i$ beforehand).

##### _example:_ partial derivatives

Suppose $f : \bb R^2 \to \bb R$ is given by $f(\bvec x) = \sin(x_1 x_2^2)$. It's partial derivatives are
$$
D_1 f \Big |_{\bvec x} = x_2^2 \cos(x_2^2 x_1)
$$
and
$$
D_2 f \Big |_{\bvec x} 2 x_1 x_2 \cos(x_1 x_2^2).
$$

##### _definition:_ higher order partials

The $i, j$th second partial of $f : A \to \bb R$ is ($A \subset \bb R^n$) is $D_j (D_i f) \Big |_{\bvec x}$, which we often denote $D_{i, j} f \Big |_{\bvec x}$.

Similarly, the $k$th order partial of multi-index $I$ ($I$ is a multi-index of $k$-numbers from $\bb N_n$) is 
$$
D_I f \Big |_{\bvec x} = D_{i_1, \ldots, i_k} f \Big |_{\bvec x} = D_{i_k}(D_{i_{k - 1}} ( \cdots D_{i_1}) \cdots ) f \Big |_{\bvec x}.
$$

Note that the second order partial has some slightly confusing reversal of the indices, but this doesn't quite matter because later we will see that most of the time (whenever they are both continuous) $D_{i, j} \Big |_{\bvec x} = D_{j, i} \Big |_{\bvec x}$.

##### _definition:_ $\mathcal C^n$

A function $f : A \to \bb R$ ($A \subset \bb R^n$) is $\mathcal C^n$ on some open $U \subset A$ if all of its $n$th partials exist and are continuous on $U$. 

Sometimes, $\mathcal C_1$ functions are called continuously differentiable.

### Extrema

Just like with regular derivatives, the maxima and minima of a multivariable function correspond to zeroes of its partials.

##### _theorem:_ extrema correspond to partial zeroes

Let $A \subset \bb R^n$. If the maximum or minimum of $f : A \to \bb R$ occurs at a point $\bvec a$ in the interior of $A$, then $D_i f \Big |_{\bvec a} = 0$ for all $i$ for which it exists.

###### _proof:_

Let $g_i = f(a_1, \ldots, a_{i - 1}, x, a_{i + 1}, \ldots, a_n)$. If $f$ has a maximum at $\bvec a$, then $g_i$ must have a maximum at $a_i$, and thus, $g_i'(a_i) = D_i f \Big |_{\bvec a} = 0$.

Note that the converse is obviously not true. This could fail in a fairly dumb way with $g_i(x) = x^3$, and then none of them have a maximum or minimum at $0$ but $g_i'(0) = 0$ for all $i$. This could also fail in an even more spectacular way.

##### _example:_ saddle points

Consider the function $f : \bb R^2 \to \bb R$ given by $f(\bvec x) = x_1^2 - x_2^2$. We have partials
$$
D_1 f \Big |_{\bvec x} = 2x_1
$$
and
$$
D_2 f \Big |_{\bvec x} = -2x_2.
$$

Thus, $\bvec 0$ is a zero of both partials. However, if we look at the functions $g_i(x)$ as defined previously, we find that $0$ is a minimum of $g_1$ and a maximum of $g_2$. Obviously, this tells us that $\bvec 0$ is not a minimum or maximum of $f$, but also, this indicates that the graph of $f$ will have a unique "pringle" or "saddle" shape, leading to the terminology saddle point.

### The "total" derivative

The total derivative is just the [[The derivative#_definition _ derivative, differentiability|derivative]] that we already defined. We call it total to distinguish it from partial, and also, to indicate the following relationship between the partial and total derivatives.

##### _theorem:_ the partials of a differentiable function define its derivative

If $f : A \to \bb R^m$ ($A \subset \bb R^n$) is differentiable at $\bvec a$, then $D_i f_j \Big |_{\bvec a}$ exists for $i \in \bb N_n$ and $j \in \bb N_m$ with [[The derivative#_definition _ the Jacobian matrix|the Jacobian]] of $f$ at $\bvec a$ given by the matrix $\mathcal M$ with
$$
\mathcal M_{i, j} = D_j f_i \Big |_{\bvec a}.
$$
That is, we have
$$
D f_i \Big |_{\bvec a} = D_1 f_i \Big |_{\bvec a} \bvec e_1^\vee + \cdots + D_n f_i \Big |_{\bvec a} \bvec e_n^\vee.
$$

###### _proof:_

Note that we have already that the Jacobian of $f_i$ at $\bvec a$ is just the $i$th row of the Jacobian of $f_i$ at $\bvec a$ as [[Differentiability theorems#_theorem _ the projection principle holds for differentiability|a consequence of the projection principle]]. That is, we have $\mathcal M_{i, .} = D f_i \Big |_{\bvec a}$ and we only need to prove that for functions $g : A \to \bb R$ that the Jacobian is given by
$$
\begin{bmatrix}
D_1 g \Big |_{\bvec a}, \ldots, D_n g \Big |_{\bvec a}
\end{bmatrix}.
$$

Consider the function $h^i_{\bvec a} : \bb R \to \bb R^n$ given by $h^i_{\bvec a}(x) = (a_1, \ldots, a_{i - 1}, x, a_{i + 1}, \ldots, a_n)$. This is clearly differentiable with derivative such that
$$
D h^i_{\bvec a} \Big |_x (v) = v \bvec e_i
$$
(by the projection principle and single variable derivatives).

Note that $D_i g \Big |_{\bvec a}$ is just $D(g \circ h^i_\bvec a) |_{a_i}$. By the chain rule, we have
$$
\begin{split}
D(g \circ h^i_{\bvec a})\Big |_{a_i}(v) & = (Dg \Big |_{h^i_{\bvec a}(a_i)} \circ Dh_{\bvec a}^i \Big |_{a_i})(v) \\
& = Dg \Big |_{\bvec a}(D h^i_{\bvec a} \Big |_{a_i} (v)) \\
& = Dg \Big |_{\bvec a} (v\bvec e_i) \\
& = v D g \Big |_{\bvec a} (\bvec e_i) \\
& = v D_i g \Big |_{\bvec a} \\
& = D_i g \Big |_{\bvec a} (v)
\end{split}
$$
as desired.

It can be seen this is equivalent to the latter statement by just thinking about the matrices of $\bvec e_i^\vee$.

There are a few instances of the confusions of thinking of a partial as both a number and a linear functional in $\bb R^\vee$, but it isn't too bad and it is still correct, so we leave it without detailed explanation.

Essentially, this says that if $f$ is differentiable, you can build its "total derivative" from its partials. Note however that the existence of all partials is not enough to guarantee differentiability.

##### _example:_ the existence of partials doesn't give rise to differentiability

Consider $f : \bb R^2 \to \bb R$ defined by
$$
f(\bvec x) = \begin{cases} 
\dfrac{x_1^2 x_2}{\norm{\bvec x}^2} & \bvec x \neq \bvec 0\\
0 & \bvec x = \bvec 0.
\end{cases}
$$

Both partials clearly exist:
$$
D_1 f \Big |_{\bvec x} = D_2 f \Big |_{\bvec x} = 0.
$$

However, the linear map $\bvec 0 = 0 \bvec e_1^\vee + 0 \bvec e_2^\vee$ does not give a good approximation to $f(\bvec 0 + \bvec v) - f(\bvec 0)$ anywhere except for $\bvec v = \bvec 0$. If we graph the function, we can see this is because the function "creases" close to the origin — it looks kind of like the sharp point that we get from the $\abs{x}$ function.

##### _theorem:_ $\mathcal C_1$ functions are differentiable

For a function $f : A \to \bb R^m$ ($A \subset \bb R^n$) and some $\bvec a \in A$, if $f$ is $\mathcal C^1$ on some open $U \subset A$ with $\bvec a \in U$, $f$ is differentiable at $\bvec a$.

###### _proof:_

Again, note that by [[Differentiability theorems#_theorem _ the projection principle holds for differentiability|the projection principle]], we only need to show that this holds for $m = 1$. Other cases follow by the differentiability of component functions.

For $f : A \to \bb R$, we can rewrite a small perturbation to the function input as small perturbation to each variable:
$$
\begin{split}
f(\bvec a + \bvec v) - f(\bvec a) &= f(a_1 + v_1, \ldots, a_n + v_n) - f(a_1, \ldots, a_n) \\
& = f(a_1 + v_1, a_2, \ldots, a_n) - f(a_1, \ldots, a_n)\\
& + f(a_1 + v_1, a_2 + v_2 , a_3 \ldots, a_n) - f(a_1 + v_1, a_2, \ldots, a_n) \\
& \, \, \, \vdots \\
& + f(\bvec a + \bvec v) - f(a_1 + v_1, \ldots, a_{n - 1} + v_{n - 1}, a_n).
\end{split}
$$

Since each partial is continuous, we can write each $j$th difference as the product of $v_j$ and the $j$th partial of $f$ evaluated somewhere on the boundary of the closed box with $\bvec a$ and $\bvec a + \bvec v$ as its opposite corners. More specifically, for each $j \in \bb N_n$ we have
$$
\begin{split}
f(a_1 + v_1, \ldots, a_j + v_j, a_{j + 1}, \ldots, a_n) - f(a_1 + v_1, \ldots, a_{j - 1} + v_{j - 1}, a_j, \ldots, a_n) \\
= v_j \, D_jf \Big |_{(a_1 + v_1, \ldots, a_{j - 1} + v_{j - 1}, a_j + c_j, a_{j + 1}, \ldots, a_n)}
\end{split}
$$
with $c_j \in (0, v_j)$.

Let $\bvec b_j = (a_1 + v_1, \ldots, a_{j - 1} + v_{j - 1}, a_j + c_j, a_{j + 1}, \ldots, a_n)$.

Let $T$ be the linear map in $(\bb R^n)^\vee$ that sends $\bvec v$ to $\sum_{i = 1}^n v_i D_i f(\bvec a)$. Then it's easy to show that
$$
\begin{split}
\lim_{\bvec v \to \bvec 0} \frac{\abs{f(\bvec a + \bvec v) - f(\bvec a) - T \bvec v}}{\norm{\bvec v}} & = \lim_{\bvec v \to \bvec 0} \frac{\abs{\sum_{j = 1}^n v_j D_ jf \Big |_{\bvec b_j} - v_j D_j f \Big |_{\bvec a}}}{\norm{\bvec v}} \\
& \le \lim_{\bvec v \to \bvec 0} \sum_{j = 1}^n \abs{D_j f\Big |_{\bvec b_j} - D_j f \Big |_{\bvec a}} \frac{\abs{v_j}}{\norm{\bvec v}} \\
& \le \lim_{\bvec v \to \bvec 0} \sum_{j = 1}^n \abs{D_j f \Big |_{\bvec b_j} - D_j f \Big |_{\bvec a}} \\
& = 0.
\end{split}
$$
The last step follows since for $\bvec v$ approaching $\bvec 0$, $\bvec b_j$ gets closer and closer to $\bvec a$, and thus, by continuity $D_j f \Big |_{\bvec b_j}$ gets closer and closer to $D_j f \Big |_{\bvec a}$.

##### _theorem:_ the weak chain rule

Suppose have $m$ continuously differentiable functions $g_1, \ldots, g_m$ $g_j : A \to \bb R$ ($A \subset \bb R^n$) (we can think of these as the component functions of $g : A \to \bb R^m$, describing the input coordinates of another function), and $f : B \to \bb R$ ($B \subset \bb R^m$) is differentiable at $f(g(\bvec a))$ with $\bvec a$.

Then for $F = f \circ g$
$$
D_i F \Big |_{\bvec a} = \sum_{j = 1}^n D_j f \Big |_{g(\bvec a)} \cdot D_i g_j \Big |_{\bvec a}.
$$

###### _proof:_

This follows easily from [[Differentiability theorems#_theorem _ chain rule|the stronger chain rule]] and [[#_theorem _ the partials of a differentiable function define its derivative|the composition of the total derivative from partials]].

Since $g_1, \ldots, g_m$ are $\mathcal C_1$ at $\bvec a$, they are all differentiable (by [[#_theorem _ $ mathcal C_1$ functions are differentiable|the previous result]]), and so is $g$. In fact, we know that they have Jacobian matrices given by their partials, and thus, $g$ has the Jacobian
$$
\mathcal M(Dg \Big |_{\bvec a}) = 
\begin{bmatrix}
D_1 g_1  \Big |_{\bvec a} \cdots D_n g_1 \Big |_{\bvec a} \\
\vdots \quad \quad \quad \quad \quad \vdots \\
D_1 g_m \Big |_{\bvec a} \cdots D_n g_m \Big |_{\bvec a}.
\end{bmatrix}
$$

Since, $f$ is differentiable at $g(\bvec a)$ it too has a Jacobian given by its partials.
$$
\mathcal M(Df \Big |_{g(\bvec a)}) =
\begin{bmatrix}
D_1 f \Big |_{g(\bvec a)} \cdots D_m f \Big |_{g(\bvec a)}
\end{bmatrix}.
$$

By the chain rule we have that $f \circ g$ is differentiable and has Jacobian given by
$$
\mathcal M(D (f \circ g) \Big |_{\bvec a}) = \mathcal M(D f \Big |_{g(\bvec a)}) \, \mathcal M(Dg \Big |_{\bvec a}).
$$

Since $D_i F \Big |_{\bvec a}$ is the $i$th entry of $\mathcal M(D F \Big |_{\bvec a})$, it must also be the $i$th entry of $\mathcal M(D f \Big |_{g(\bvec a)}) \, \mathcal M(Dg \Big |_{\bvec a})$. By matrix multiplication, this gives us
$$
D_i F \Big |_{\bvec a} = \sum_{j = 1}^n D_j f \Big |_{g(\bvec a)} \cdot D_i g_j \Big |_{\bvec a}.
$$
Note again that there are some interesting technicalities to resolve if you want to think of a partial as a local linear approximation.