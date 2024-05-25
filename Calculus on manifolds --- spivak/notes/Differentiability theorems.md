---
tags:
- spivak
- anal
- calc
- self-study
---

Like with single variable calculus, there are lots of differentiability theorems that allow us to just take derivatives of functions on $\bb R^n$ without worrying too much.

### Chain rule

The chain rule allows us to take the derivative of compositions of functions that we already know are differentiable. Basically, if $f$ and $g$ are locally similar to linear maps $S$ and $T$ (respectively), then $g \circ f$ is locally similar to the linear map $T \circ S$.

##### _theorem:_ chain rule

If $f : A \to \bb R^m$ ($A \subset \bb R^n$) is differentiable at $\bvec a$ and $g : B \to \bb R^p$ ($B \subset \bb R^m$) is differentiable at $f(\bvec a)$, then the composition $g \circ f$ is differentiable at $\bvec a$ and has derivative
$$
D(g \circ f) \Big |_{\bvec a} = Dg \Big |_{f(\bvec a)} \circ Df \Big |_{\bvec a}.
$$

Note that the case where $n = m = p = 1$ is just the old chain rule $(g \circ f)'(a) = g'(f(a)) f'(a)$.

###### _proof:_

Let $f(\bvec a) = \bvec b$. Let $S = Df \Big |_{\bvec a}$ and $T = Dg \Big |_{f(\bvec b)}$. We will show that the map $T \circ S$  satisfies the limit condition to be the unique derivative of $g \circ f$.

We know that the following limits hold
$$
\begin{gathered}
	\lim_{\bvec v \to \bvec 0} \frac{\norm{f(\bvec a + \bvec v) - f(\bvec a) - S \bvec v}}{\norm{\bvec v}} = 0 \\\\
	\lim_{\bvec v \to \bvec 0} \frac{\norm{g(\bvec b + \bvec v) - g(\bvec b) - T \bvec v}}{\norm{\bvec v}} = 0.
\end{gathered}
$$

We know that 
$$
\begin{split}
	(g \circ f)(\bvec a + \bvec v) - (g \circ f)(\bvec a) - (T \circ S) \bvec v & = g(f(\bvec a + \bvec v)) - g(f(\bvec a)) - T(S\bvec v) \\
	& = g(f(\bvec a + \bvec v)) - g(\bvec b) - T(f(\bvec a + \bvec v) - f(\bvec a)) + T(f(\bvec a + \bvec v) - f(\bvec a) + S\bvec v).
\end{split}
$$

Thus,
$$
\begin{split}
\lim_{\bvec v \to \bvec 0} \frac{\norm{(g \circ f)(\bvec a + \bvec v) - (g \circ f)(\bvec a) - (T \circ S) \bvec v}}{\norm{\bvec v}} & = \lim_{\bvec v \to \bvec 0} \frac{\norm{g(f(\bvec a + \bvec v)) - g(\bvec b) - T(f(\bvec a + \bvec v) - f(\bvec a)) + T(f(\bvec a + \bvec v) - f(\bvec a) + S\bvec v)}}{\norm{\bvec v}} \\
& \le \lim_{\bvec v \to \bvec 0} \frac{\norm{g(f(\bvec a + \bvec v)) - g(\bvec b) - T(f(\bvec a + \bvec v) - \bvec b)}}{\norm{\bvec v}} - \frac{\norm{T(f(\bvec a + \bvec v) - f(\bvec a) + S\bvec v)}}{\norm{\bvec v}} \\
& = \lim_{\bvec v \to \bvec 0} \frac{\norm{g(f(\bvec a + \bvec v)) - g(\bvec b) - T(f(\bvec a + \bvec v) - \bvec b)}}{\norm{\bvec v}} - 0
\end{split}
$$

We can rewrite $f(\bvec a + \bvec v)$ by considering that $\lim_{\bvec v \to \bvec 0} f(\bvec a + \bvec v) - f(\bvec a) - S \bvec v = \bvec 0$. That is,
$$
\begin{split}
\lim_{\bvec v \to \bvec 0} \frac{\norm{g(f(\bvec a + \bvec v)) - g(\bvec b) - T(f(\bvec a + \bvec v) - \bvec b)}}{\norm{\bvec v}} & = \lim_{\bvec v \to \bvec 0} \frac{\norm{g(f(\bvec a + \bvec v) - f(\bvec a) - S \bvec v + \bvec b + S \bvec v) - g(\bvec b)}  - T(f(\bvec a + \bvec v) - f(\bvec a) - S\bvec v + S \bvec v)}{\norm{\bvec v}} \\ 
& = \lim_{\bvec v \to \bvec 0} \frac{\norm{g(\bvec 0 + \bvec b + S \bvec v) - g(\bvec 0 + \bvec b) - T(\bvec 0 + S \bvec v)}}{\norm{\bvec v}} \\
& = 0.
\end{split}
$$

We can apply limits inside $g$ since it is continuous at $\bvec a$.

### "Easy" derivatives

Some functions have obvious derivatives — constant functions don't change, and linear maps are their own best linear approximations.

##### _proposition:_ constant functions don't change

If $f : A \to \bb R^m$ ($A \subset \bb R^n$) is a constant function ($f(\bvec x) = \bvec y$ for some fixed $\bvec y \in \bb R^m$, for all $\bvec x \in \bvec a$), then
$$
Df \Big |_{\bvec a} = \bvec 0
$$
for all $\bvec a \in A$ at which $f$ is differentiable. 

Note that this is basically just all $\bvec a$ in the interior of $A$.

###### _proof:_

We will show that the $\bvec 0$ map satisfies the limit definition of the derivative of a constant function. That is,
$$
\begin{split}
\lim_{\bvec v \to 0} \frac{\norm{f(\bvec a + \bvec v) - f(\bvec a) - \bvec 0 (\bvec v)}}{\norm{\bvec v}} & = \lim_{\bvec v \to \bvec 0}\frac{\norm{\bvec y - \bvec y - \bvec 0}}{\norm{\bvec v}} \\
& = \lim_{\bvec v \to \bvec 0}\frac{\norm{\bvec 0}}{\norm{\bvec v}} \\
& = 0
\end{split}
$$
as desired.

##### _proposition:_ a linear map is its own best linear approximation

If $T : \bb R^n \to \bb R^m$ is a linear map, then
$$
DT \Big |_{\bvec a} = T.
$$
at all $\bvec a \in \bb R^n$.

###### _proof:_

Again, we show that $T$ satisfies the limit definition of its own derivative. Specifically,
$$
\begin{split}
\lim_{\bvec v \to \bvec 0} \frac{\norm{T(\bvec a + \bvec v) - T(\bvec a) - T(\bvec v)}}{\norm{\bvec v}} & = \lim_{\bvec v \to \bvec 0} \frac{\norm{T(\bvec a + \bvec v) - T(\bvec a + \bvec v)}}{\norm{\bvec v}} \\
& = \lim_{\bvec v \to \bvec 0} \frac{\norm{\bvec 0}}{\norm{\bvec v}} \\
& = 0
\end{split}
$$
as desired.

### Making all derivatives easy

Using the next three, results, we can make it almost trivial to take the derivative of almost any function. (We will get completely trivial derivatives later).

The [[Continuity#The projection principle|projection principle]] hinted that it sufficed to just look at the component functions of any function $f : A \to \bb R^m$, reducing our work to understanding functions $f : A \to \bb R$ where $A \subset \bb R^n$. We [[Chapter 1.pdf#page=6|showed that this holds for continuity]], and now we show that it holds for differentiability too.

##### _theorem:_ the projection principle holds for differentiability

For a function $f : A \to \bb R^m$ ($A \subset \bb R^n$), $f$ is differentiable at $\bvec a \in A$ if and only if each of its component functions $f_i$ is differentiable at $\bvec a$. Specifically,
$$
Df \Big |_{\bvec a} \bvec v = (Df_1 \Big |_{\bvec a} \bvec v, \ldots, Df_n \Big |_{\bvec a} \bvec v).
$$

###### _proof:_

Suppose $f$ is differentiable at $\bvec a$. Then any component function $f_i$ is given by $\pi_i \circ f$. Since $\pi_i$ is a linear map, it is its own derivative, making $f_i$ differentiable with derivative given by the [[#_theorem _ chain rule|chain rule]]:
$$
\begin{split}
Df_i \Big |_{\bvec a} &= D \pi_i \Big |_{f(\bvec a)} \circ Df \Big |_{\bvec a} \\
& = \pi_i \circ Df \Big |_{\bvec a}.
\end{split}
$$

Moreover, like with continuity, if one of the $f_i$ wasn't differentiable and the limit didn't work out, it would "stop" the limit from working out for $f$ as a whole.

If each $f_i$ is differentiable, then consider the function $g : \bb R^n \to \bb R^m$
$$
g(\bvec v) =  \frac{f(\bvec a + \bvec v) - f(\bvec a) - (Df_1 \Big |_a, \ldots, Df_n \Big |_{\bvec a} )}{\norm{\bvec v}}.
$$
Each component function $g_i$ is given by
$$
g_i(\bvec v) =  \frac{f_i(\bvec a + \bvec v) - f_i(\bvec a) - Df_i \Big |_a}{\norm{\bvec v}}.
$$
and gives
$$
\lim_{\bvec v \to \bvec 0} g_i(\bvec v) = \bvec 0.
$$

By the projection principle, this gives us
$$
\lim_{\bvec v \to \bvec 0} g(\bvec v) = \bvec 0
$$
and thus
$$
\lim_{\bvec v \to \bvec 0} \norm{g(\bvec v)} = 0
$$
as desired.

Note that we can also get this by bounding $\norm{g(\bvec v)}$ by the sum of all $\abs{g_i(\bvec v)}$ and avoid the sketchy thing about $0$ norm in the limit implying $\bvec 0$ in the limit. (Though it's pretty easy to see that it's true).

Now we show that differentiation holds for sums and for products using two easier results.

##### _proposition:_ sums are differentiable

$\Sigma : \bb R^2 \to \bb R$, defined by $\Sigma(\bvec x) = x_1 + x_2$ is differentiable with
$$
D \Sigma \Big |_{\bvec a} = \Sigma \bvec a
$$
for all $\bvec a \in \bb R^2$.

###### _proof:_

This follows from the fact that all linear transformations are their own derivative — note that $\Sigma$ is a functional in $(\bb R^2)^\vee$.

##### _corollary:_ the multivariable sum rule

If $f, g : A \to \bb R$ ($A \subset \bb R^n$) are differentiable at $\bvec a \in A$, then the function $f+ g : A \to \bb R$ given by $(f + g)(\bvec x) = f(\bvec x) + g(\bvec x)$ is differentiable with
$$
D(f + g) \Big |_{\bvec a} = Df \Big |_{\bvec a} + Dg \Big |_{\bvec a}.
$$

###### _proof:_

Consider that we have $f + g = \Sigma \circ (f, g)$ where $(f, g) : A \to \bb R^2$ with component functions $f$ and $g$ [[#_theorem _ the projection principle holds for differentiability|and is differentiable]]. Then by the chain rule we have
$$
\begin{split}
D(f + g) \Big |_{\bvec a} & = D \Sigma \Big |_{(f, g)(\bvec a)} \circ D(f, g) \Big |_{\bvec a} \\
& = \Sigma \circ (Df \Big|_{\bvec a}, Dg \Big |_{\bvec a}) \\
& = Df \Big |_{\bvec a} + Df \Big |_{\bvec a}.
\end{split}
$$

##### _proposition:_ products are differentiable

$\Pi : \bb R^2 \to \bb R$, defined by $\Pi(\bvec x) = x_1 x_2$ is differentiable with
$$
D \Pi \Big |_{\bvec a} \bvec v = a_2 v_1 + a_1 v_2 
$$
for all $\bvec a \in \bb R^2$.

###### _proof:_

We show that the limit definition works out. Let $\varphi \in (\bb R^2)^\vee$ be defined by $\varphi(\bvec v) = a_2 v_1 + a_1 v_2$. Then we have
$$
\begin{split}
	\lim_{\bvec v \to \bvec 0} \frac{\abs{(\Pi(\bvec a + \bvec v) - \Pi(\bvec a) - \varphi(\bvec v)}}{\norm{\bvec v}} & = \lim_{\bvec v \to \bvec 0} \frac{\abs{(a_1 + v_1)(a_2 + v_2) - a_1a_2 - a_2 v_1 - a_1 v_2}}{\norm{\bvec v}} \\
	& = \lim_{\bvec v \to \bvec 0} \frac{\abs{v_1 v_2}}{\norm{\bvec v}}
\end{split}
$$
Note that since $v_1 \le v_2$ or $v_2 \le v_1$, we must have $v_1 v_2 \le v_1 v_1$ or $v_1 v_2 \le v_2 v_2$. Thus,
$$
\begin{split}
 \lim_{\bvec v \to \bvec 0} \frac{\abs{v_1 v_2}}{\norm{\bvec v}} & \le \lim_{\bvec v \to \bvec 0} \frac{v_1^2 + v_2^2}{\norm{\bvec v}} \\
	& = \lim_{\bvec v \to \bvec 0} \norm{\bvec v} \\
	& = 0.
\end{split}
$$
Thus, $\varphi$ is the derivative of $\Pi$ at $\bvec a$ as desired.

##### _corollary:_ the multivariable product rule

If $f, g : A \to \bb R$ ($A \subset \bb R^n$) are differentiable at $\bvec a \in A$, then the function $f g : A \to \bb R$ given by $(fg)(\bvec x) = f(\bvec x) g(\bvec x)$ is differentiable with
$$
D(fg) \Big |_{\bvec a} = Df \Big |_{\bvec a} \times g(\bvec a) + f(\bvec a) \times Dg \Big |_{\bvec a}.
$$

###### _proof:_

Note that $(fg) = \Pi \circ (f, g)$. Then by the chain rule
$$
\begin{split}
	D(fg) \Big |_{\bvec a} & = D \Pi \Big |_{(f, g)(\bvec a)} \circ D(f, g) \Big |_{\bvec a} \\
	& = D \Pi \Big |_{(f, g)(\bvec a)} \circ (Df \Big |_{\bvec a}, Dg \Big |_{\bvec a}) \\
	& = g(\bvec a) \times Df \Big |_{\bvec a} + f(\bvec a) \times Dg \Big |_{\bvec a}.
\end{split}
$$
