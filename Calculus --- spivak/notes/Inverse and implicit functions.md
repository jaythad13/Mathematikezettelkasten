---
tags:
- spivak
- anal
- calc
- self-study
---

Here, we generalise some theorems from single-variable calculus that allow us to "implicitly" define differentiable (and we will see, sometimes smooth) functions.

### Inverse functions

We're already familiar with the notion of defining a "local inverse function" for single-variable real functions. 

Specifically, for a function $f : A \to \bb R$ (with $A \subset \bb R$), differentiable at $a \in A$, if $f'(a) > 0$, then there is some open interval around $f(a)$, say $V$, which has $f$ differentiable and $f'(a) > 0$ on all of $U = f^\text{pre}(V)$. Since $f'(a) > 0$ everywhere, the restriction $f_{|U} : U \to V$ is a bijection with differentiable inverse $f^{-1}_{|U}$. The situation is similar for $f'(a) < 0$.

Moreover, by thinking about derivatives as linear maps, we can see $(f^{-1}_{|U})'(f(a)) = {1}/{f'(a)}$, or $f^{-1}_{|U}(y) = {1}/{f'(f^{-1}(y))}$. That is, if small perturbations to $a$, $h$, look like multiplying by $f'(a)$ when mapped under $f$, then when small perturbations to $f(a)$ are mapped under $f^{-1}_{|U}$, they should look like multiplying by $1/f'(a)$. 

The details are as follows. For any $y = f(a)$, $y + h' \in V$, we should be able to write $y + h' = f(a + h)$ with $h$ smaller as $h'$ gets smaller. Since $f(a + h) - f(a) \approx f'(a) h$, we have $f^{-1}_{|U}(y + h') - f^{-1}(y) \approx h'/f'(a)$.

Generalising this to functions on $\bb R^n$ requires some more involved set up, but amounts to essentially the same argument.

##### _lemma:_ partials give a Lipschitz condition for $\mathcal C^1$ functions

Let $A \subset \bb R^n$ be a rectangle and let $f : A \to \bb R^n$ be continuously differentiable. If there is some $M \in \bb R$ such that $\abs{D_j f_i \Big |_{\bvec x}} \le M$ for all $\bvec x \in A^{\circ}$, then
$$
\norm{f(\bvec x) - f(\bvec y)} \le n^2 M \norm{\bvec x - \bvec y}.
$$

###### _proof:_

We can do this by bounding the function by its component functions and then bounding them by the mean value theorem.

For any such $f$, we will have
$$
\norm{f(\bvec y) - f(\bvec x)} \le \sum_{i = 1}^n \abs{f_i(\bvec y) - f_i(\bvec x)}.
$$

Further, for each component function $f_i$, we can decompose $f_i(\bvec y) - f_i(\bvec x)$ [[Partials and the "total" derivative#_proof _|as we did to prove that functions with all continuous partials are differentiable]]. That is,
$$
\begin{split}
f_i(\bvec y) - f_i(\bvec x) & = f_i(y_1, x_2, \ldots, x_n) - f(x_1, \ldots, x_n) \\
& + f_i(y_1, y_2, x_3, \ldots, x_n) - f(y_1, x_2, \ldots, x_n) \\
& \, \, \, \vdots \\
& + f(y_1, \ldots, y_n) - f(y_1, \ldots, y_{n - 1}, x_n).
\end{split}
$$
which with the mean value theorem, allows, us to write the difference as the sum of $n$ partials of $f_i$ weighted by $y_j - x_j$. Specifically,
$$
\begin{split}
f_i(\bvec y) - f_i(\bvec x) & = \sum_{j = 1}^n (y_j - x_j) D_j f_i \Big |_{(y_1, \ldots, y_{j - 1}, c_j, x_j, \ldots, x_n)}.
\end{split}
$$

Thus,
$$
\begin{split}
\abs{f_i(\bvec y) - f_i(\bvec x)} & \le \sum_{j = 1}^n \abs{y_j - x_j} \abs{D_j f_i \Big |_{(y_1, \ldots, y_{j - 1}, c_j, x_j, \ldots, x_n)}} \\
& \le \sum_{j = 1}^n \abs{y_j - x_j} M \\
& \le \sum_{j = 1}^n \norm{\bvec y - \bvec x} M \\ 
& \le n M \norm{\bvec y - \bvec x}.
\end{split}
$$

Finally, combined with the first inequality, we get the bound we wanted.
$$
\begin{split}
\norm{f(\bvec y) - f(\bvec x)} & \le \sum_{i = 1}^n nM \norm{\bvec y - \bvec x} \\
& = n^2 M.
\end{split}
$$

Now we have the machinery to prove the inverse function theorem.

##### _theorem:_ the inverse function theorem

Suppose that $f : A \to \bb R^n$ (with $A \subset \bb R^n$) is [[Partials and the "total" derivative#_definition _ $ mathcal C n$|continuously differentiable]] in an open set containing $\bvec a$, and $Df \Big |_{\bvec a}$ is invertible. Then there is an open set $V$ containing $\bvec a$ and an open set $W$ containing $f(\bvec a)$ such that the restriction $f_{|V} : V \to W$ has a differentiable inverse $f_{|V}^{-1}$ satisfying
$$
D f_{|V}^{-1} \Big |_{\bvec y} = (D f_{|V} \Big |_{f_{|V}^{-1}(\bvec y)})^{-1}
$$

###### _proof:_

Note that we can assume without loss of generality that $Df \Big |_{\bvec a} = I$. Essentially, if $Df \Big |_{\bvec a} = T$, then $D(T^{-1} \circ f) \Big |_{\bvec a} = I$, and we have the theorem for $g_{|V} : V \to W$ given by $g = T^{-1} \circ f$ — we have a local differentiable inverse $g^{-1}|_{|V}$ (where $V$ and $W$) are open as desired.

But then $f : V \to T^\text{img}(W)$ given by $f = T \circ g$ certainly has a differentiable local inverse $f^{-1}_{|V} = g^{-1} \circ T^{-1}$ by the chain rule where $T^\text{img}(W)$ is open since it is the pre-image of the open set $W$ under the continuous mapping $T^{-1}$.

Thus, we can assume without loss of generality that $Df \Big |_{\bvec a} = I$

First we need to show that we can't have $f(\bvec a) = f(\bvec a + \bvec v)$ for arbitrarily small $\bvec v$ — we're moving towards finding a neighbourhood in which $f$ is at least injective.

Since wherever $f(\bvec a + \bvec v) = f(\bvec a)$ we have
$$
\begin{split}
\frac{\norm{f(\bvec a + \bvec v) - f(\bvec a) - Df \Big |_{\bvec a}(\bvec v)}}{\norm{\bvec v}} & = \frac{\norm{I \bvec v}}{\norm{\bvec v}} \\
& = 1.
\end{split}
$$
and
$$
\lim_{\bvec v \to \bvec 0} \frac{\norm{f(\bvec a + \bvec v) - f(\bvec a) - Df \Big |_{\bvec a}(\bvec v)}}{\norm{\bvec v}} = 0
$$
the open ball, around $\bvec 0$, of radius $\delta$, given by choosing $\varepsilon = 1/M$ in the $\varepsilon$-$\delta$ definition of this limit must contain no vectors $\bvec v$ such that $f(\bvec a + \bvec v) = f(\bvec a)$. Thus, there is an open ball around $\bvec a$ in which there is no $\bvec b$ with $f(\bvec b) = f(\bvec a)$.

Further, we can restrict the value of the first partials of the component functions, since they are continuous. Specifically, we can pick an open ball subset of this ball such that 
$$
\abs{D_j f_i \Big |_{\bvec x} - D_j f_i \Big |_{\bvec a}} < \frac{1}{2n^2}.
$$

Again, by continuity ($\det$ is a $\mathcal C^\infty$ function of the $n^2$ partials), we can choose to have $\det Df \Big |_{\bvec x} \neq 0$ everywhere in an open ball subset of the ball.

Finally, we can look at a closed rectangle, $U$, inside this final smallest ball, containing $\bvec a$ in its interior (just look at the closed ball of half the radius, and then look at the inscribed closed square).

If we consider $g(\bvec x) = f(\bvec x) - \bvec x$, we can bound its partials by our bounds on the partials of $f$ and then by [[#_lemma _ partials bound $ mathcal C 1$ functions|our lemma]], we can bound the difference between $g$ evaluated at any two points on $U$. Specifically,
$$
D_j g_i \Big |_{\bvec x} = \begin{cases}
D_j f_i \Big |_{\bvec x} - 1 & i = j \\
D_j f_i \Big |_{\bvec x} & i \neq j
\end{cases}
$$

Since $Df \Big |_{\bvec a} = I$ this gives us $D_j g_i \Big |_{\bvec a} = 0$ for all $i, j \in \bb N_n$.

This gives us
$$
\abs{D_j g_i \Big |_{\bvec x} - D_j g_i \Big |_{\bvec a}} = \abs{D_j f_i \Big |_{\bvec x} - D_j f_i \Big |_{\bvec a}}
$$
and thus,
$$
\begin{split}
\abs{\abs{D_j g_i \Big |_{\bvec x}} - \abs{D_j g_i \Big |_{\bvec a}}} & = \abs{D_j g_i \Big |_{\bvec x}} \\ & \le \abs{D_j f_i \Big |_{\bvec x} - D_j f_i \Big |_{\bvec a}} \\
& < \frac{1}{2n^2}.
\end{split}
$$

We can then get the bound
$$
\norm{g(\bvec x_1) - g(\bvec x_2)} \le \frac{1}{2} \norm{\bvec x_1 - \bvec x_2}.
$$

Expanding this using the triangle inequality gives us
$$
\begin{split}
\norm{\bvec x_1 - \bvec x_2} - \norm{f(\bvec x_1) - f(\bvec x_2)} & \le \norm{g(\bvec x_1) - g(\bvec x_2)} \\
& \le \frac{1}{2} \norm{\bvec x_1 - \bvec x_2}
\end{split}
$$

and thus,
$$
\norm{\bvec x_1 - \bvec x_2} \le 2 \norm{f(\bvec x_1) - f(\bvec x_2)}
$$
for $\bvec x_1, \bvec x_2 \in U$. That is, $f$ is injective on $U$.

Finally, since we can separate the compact $f^\text{img}(\partial U)$ (compact because its pre-image is) from its complement, we can draw an open ball around $f(\bvec a)$ that does not contain any points of $\partial U$ and is separated from it. Call this $W$. Note that we can choose the radius to be small enough that any point in $W$ is closer to $f(\bvec a)$ than any point in $\partial W$.

We will show that on $W$, $f$ is a bijection ($f$ takes every point on $W$, and at only one point in $U^\circ$). For each $\bvec y \in W$ consider the function $h_{\bvec y} : U \to \bb R$ with $h_{\bvec y} = \norm{\bvec y - f(\bvec x)}^2$.

$h_{\bvec y}$ is continuous, and thus, has a minimum on the compact set $U$. If $\bvec x \in \partial U$, then $\bvec y$ is closer to $f(\bvec a)$, so $\bvec x$ does not give the minimum of $h_{\bvec y}$. Thus, the minimum occurs at the interior, where there must therefore be some point $\bvec x$ with $D h_{\bvec y} \Big |_{\bvec x} = \bvec 0$. Using the chain rule, we can rewrite this as
$$
2 \sum_{i = 1}^n (y_i - f_i(\bvec x)) D_j f_i \Big |_{\bvec x} = 0
$$
for all $j \in \bb N_n$.

Since this is a linear system of equations $Df \Big |_{\bvec x} (\bvec y - f(\bvec x)) = \bvec 0$, and $Df \Big |_{\bvec x}$ is invertible on $U$, we must have $\bvec y - f(\bvec x) = \bvec 0$. Thus, $f$ takes every point on $W$ by some point in $U^\circ$. We already have uniqueness since $f$ is injective on $U$.

Let $V = U^\circ \cap f^\text{pre}(W)$. Then we have defined a bijection $f|_{|V} : V \to W$. If we rewrite the bound we have for $f$ on $U$ in terms of its inverse $f^{-1}_{|V}$ we get
$$
\norm{f^{-1}_{|V}(\bvec y_1) - f^{-1}_{|V}(\bvec y_2)} \le 2 \norm{\bvec y_1 - \bvec y_2}
$$
which proves that $f^{-1}_{|V}$ is continuous (just choose $\delta = \varepsilon/2$).

For differentiability, we can then just rehash the arguments from the single variable case. Let $\bvec x \in V$ have $D f_{|V} \Big |_{\bvec x} = T$ and $f_{|V}(\bvec x) = \bvec y$. We need to show that $f^{-1}_{|V}$ has derivative $T^{-1}$ at $\bvec y$.

Let $\psi(\bvec v) = f(\bvec x + \bvec v) - f(\bvec x) - T(\bvec v)$. Note that we already have $\lim_{\bvec v \to \bvec 0} \norm{\psi(\bvec v)}/\norm{\bvec v} = 0$. Consider some $\bvec u$ such that $\bvec y + \bvec u \in W$. Then we have $f^{-1}_{|V}(\bvec y + \bvec u) = \bvec x + \bvec v \in W$. Thus,
$$
\begin{split}
\mu(\bvec u) & = f^{-1}_{|V}(\bvec y + \bvec u) - f^{-1}_{|V}(\bvec y) - T^{-1}(\bvec u) \\
& = \bvec v - T^{-1}(\psi(\bvec v) + T(\bvec v)) \\
& = T^{-1}(\psi(\bvec v)).
\end{split}
$$

We already know $\lim_{\bvec v \to \bvec 0} \norm{T^{-1} \psi(\bvec v)}/{\norm{\bvec v}} = 0$ but now we just have to show that the limit holds even as $\bvec u \to \bvec 0$ with $\bvec v$ defined, as above, as the difference $f^{-1}_{|V}(\bvec y + \bvec u) - f^{-1}_{|V}(\bvec y)$. But this holds because of continuity, so we're done.

Note that an inverse function can still exist even if $\det D f \Big |_{\bvec a} = 0$, it just can't be differentiable (if it is differentiable then the chain rule implies that the derivative will have to be an invertible linear map).

##### _corollary:_ $f^{-1}$ doesn't lose any derivatives

Suppose that $f : A \to \bb R^n$ (with $A \subset \bb R^n$) is $\mathcal C^n$ (for some $n \in \bb N \cup \set{\infty}$) containing $\bvec a$, and $Df \Big |_{\bvec a}$ is invertible. Then the inverse given by the inverse function theorem, $f_{|V}^{-1}$ is also $\mathcal C^n$.

###### _proof sketch:_

The "adjoint" formula for the entries of an inverse of an invertible matrix is a $\mathcal C^\infty$ function of the entries of the original matrix. Thus, each partial of $f_{|V}^{-1}$ is given by a $\mathcal C^\infty$ function of the $\mathcal C^{n - 1}$ partials of $f_{|V}$, which makes them, by the chain rule, $\mathcal C^{n - 1}$. Thus, $f_{|V}^{-1}$ is $\mathcal C^n$.

### Implicit functions

The implicit function theorem generalises the following idea from single variable calculus.

##### _example:_ the circle $x^2 + y^2 - 1 = 0$

Consider the zeroes of the function $f : \bb R^2 \to \bb R$ given by $f(x, y) = x^2 + y^2 - 1$. These define the unit circle in $\bb R^2$. While to each $x$ there are two corresponding $y$ such that $f(x, y) = 0$, if we choose $(a, b)$ such that $f(a, b) = 0$, then there is only one sensible way to choose $x$ values near $a$ such that $y$ is a differentiable function of $a$ (unless of course $a = \pm 1$).

That is, if $b > 0$, we choose $y = \sqrt{1 - x^2}$, and lose the bottom half of the circle, and if $b < 0$. we choose $y = - \sqrt{1 - x^2}$ and lose the top half of the circle. Both functions are clearly differentiable around $a$, and give us $f(x, y) = 0$.

In general, we want to be able to answer when, for a function $f : \bb R^{n + m} \to \bb R^m$ and a zero $(\bvec a, \bvec b)$ ($\bvec a \in \bb R^n$ and $\bvec b \in \bb R^m$) there exists a differentiable function $g : \bb R^n \to \bb R^m$ such that  $f(\bvec x, g(\bvec x)) = \bvec 0$ for all $\bvec x \in \bb R^n$. Of course, this simplifies to a question about a system of $m$ equations. Note that we restrict the variables to $m$ as well by choosing $g : \bb R^n \to \bb R^m$ and not any arbitrary $\bb R^p$ to prevent trivial over/underspecification. 

The simplest case in which this is true is if $f$ is linear, and we will prove this as a lemma. First however we need to define a natural notion that arises when trying to look at implicit functions — splitting a linear map.

##### _definition:_ splitting a linear map

Every linear map $T  \in \mathcal L(\bb R^{n + m}, \bb R^m)$ can be split into $T_{|\bb R^n} \in \mathcal L(\bb R^n, \bb R^m)$ and $T_{|\bb R^m} \in \mathcal L(\bb R^m, \bb R^m)$ such that $T_{|\bb R^n}(\bvec x) = T(\bvec x, \bvec 0)$ and $T_{|\bb R^m}(\bvec y) = T(\bvec 0, \bvec y)$.

Note that $T(\bvec x, \bvec y) = T_{|\bb R^n}(\bvec x) + T_{|\bb R^m}(\bvec y)$.

##### _lemma:_ the implicit linear function theorem

If $T \in \mathcal L(\bb R^{n + m}, \bb R^m)$ and $T_{|\bb R^m}$ is invertible, to each $\bvec x \in \bb R^n$ corresponds a $\bvec y \in \bb R^m$ such that $T(\bvec x, \bvec y) = \bvec 0$.

###### _proof:_

For $\bvec x \in \bb R^n$, we obviously have $T_{|\bb R^n} (\bvec x) \in \bb R^m$. Thus, we can take $\bvec y = T^{-1}_{|\bb R^m}(- T_{\bb R^n} (\bvec x))$. Then
$$
\begin{split}
T(\bvec x, \bvec y) & = T_{|\bb R^n}(\bvec x) + T_{|\bb R^m}(\bvec y) \\
& = T_{|\bb R^n}(\bvec x) + T_{|\bb R^n}(T^{-1}_{|\bb R^m}(- T_{\bb R^n} (\bvec x))) \\
& = T_{|\bb R^n}(\bvec x) + (- T_{\bb R^n} (\bvec x)) \\
& = \bvec 0.
\end{split}
$$

The implicit function theorem in general is of course a little more difficult to prove.

##### _abuse of notation:_ $f_{|\bb R^m}$

Note that properly, we can't really talk about $f_{|\bb R^m}$ (or $T_{|\bb R^m}$) for $f : \bb R^{n + m} \to \bb R^m$, only $f_{|\set{\bvec a} \times \bb R^m}$. However since this is unwieldy we don't care about it (it is also isomorphic to what is nicer). Note that there is no confusion with the notation since $\bb R^m$ is not actually a subset of $\bb R^{n + m}$, just imbedded in it.

##### _theorem:_ the implicit function theorem

Suppose $f : \bb R^{n + m} \to \bb R^m$ is continuously differentiable in an open set containing $(\bvec a, \bvec b)$ ($\bvec a \in \bb R^n$ and $\bvec b \in \bb R^m$) and let $f(\bvec a, \bvec b) = 0$. 

Let $T$ be the linear operator in $\mathcal L(\bb R^m)$ defined by
$$
T \bvec v = (\sum_{j = 1}^n D_{n + j} f_1 \Big |_{(\bvec a, \bvec b)} v_j, \ldots, \sum_{j = 1}^n D_{n + j} f_n \Big |_{(\bvec a, \bvec b)} v_j).
$$
If $T$ is invertible, there is an open set $A \subset \bb R^n$ and an open set $B \subset \bb R^m$ with $(\bvec a, \bvec b) \in A \times B$ such that for each $\bvec x \in A$, there is a unique $g(\bvec x) \in B$ such that $f(\bvec x, g(\bvec x)) = \bvec 0$ and $g$ is differentiable.

###### _proof:_

Consider the function $F : \bb R^{n + m} \to \bb R^{n + m}$ with $F(\bvec x, \bvec y) = (\bvec x, f(\bvec x, \bvec y))$.
$$
DF \Big |_{(\bvec a, \bvec b)} = \begin{bmatrix}
I & \bvec 0 \\
\bvec 0 & T
\end{bmatrix}
$$
and thus, $\det DF \Big |_{(\bvec a, \bvec b)} = \det T \neq 0$. That is, $DF \Big |_{(\bvec a, \bvec b)}$ is invertible.

By [[#_theorem _ the inverse function theorem|the inverse function theorem]], we have $F^{-1}_{|A \times B}$, the inverse function of the restriction of $F$ to some open set $A \times B$ containing $(\bvec a, \bvec b)$, defined on the open set $W$. Since $F_{|\bb R^n}$ is just the identity function on $\bb R^n$, so is $F^{-1}_{|\bb R^n|A \times B}$. That is,
$$
F^{-1}_{|A \times B}(\bvec x, \bvec y) = (\bvec x, k(\bvec x, \bvec y))
$$
We can choose $g(\bvec x) = k(\bvec x, \bvec 0)$. Then
$$
\begin{split}
f(\bvec x, g(\bvec x)) & = f(\bvec x, k(\bvec x, \bvec 0)) \\
& = f(F^{-1}_{|A \times B}(\bvec x, \bvec 0)) \\
& = \pi_{\bb R^m} (F(F^{-1}_{|A \times B}(\bvec x, \bvec 0))) \\
& = \bvec 0.
\end{split}
$$


We can generalise this theorem to the case where the variables aren't so neatly arranged — even if the last $m$ variables aren't specified by the first $n$, we can "rearrange" the variables so that they are.

##### _theorem:_ the rank theorem

Suppose $f : X \to \bb R^p$ (where $X \subset \bb R^n$ and $p \le n$) is $\mathcal C^1$ in an open set containing $\bvec a$. If $f(\bvec a) = \bvec 0$ and $\operatorname{rank} Df \Big |_{\bvec a} = p$, then there is an open set $A$ in $\bb R^n$ containing $\bvec a$, and a differentiable function $h : A \to X$ with differentiable inverse such that
$$
(f \circ h) (x_1, \ldots, x_n) = (x_{n - p + 1}, \ldots, x_n).
$$

###### _proof sketch:_

Since $\operatorname{rank} Df \Big |_{\bvec a} = p$, there must be some $p$ columns of the $Df \Big |_{a}$ we can choose such that they form an invertible matrix. Permute the columns by some function $g$ so that they are the last $p$ columns of $D(f \circ g) \Big |_{\bvec a}$. The [[#_theorem _ the implicit function theorem|proof of the implicit function theorem]] tells us that the theorem holds for $f \circ g$ and so we have a function $k$ that gives us 
$$
((f \circ g) \circ k) (x_1, \ldots, x_n) = (x_{n - p + 1}, \ldots, x_n)
$$
and thus,
$$
(f \circ (g \circ k)) (x_1, \ldots, x_n) = (x_{n - p + 1}, \ldots, x_n).
$$

That is, choose $h = g \circ k$.
%%
##### _theorem:_ the implicit function theorem

Suppose $f : \bb R^{n + m} \to \bb R^m$ is continuously differentiable in an open set containing $(\bvec a, \bvec b)$ ($\bvec a \in \bb R^n$ and $\bvec b \in \bb R^m$) and let $f(\bvec a, \bvec b) = 0$. 

Let $T$ be the derivative of $f_{|\bb R^m} : \bb R^m \to \bb R^m$, defined by $f_{|\bb R^m} (\bvec y) = f(\bvec a, \bvec y)$ at $\bvec b$. Then
$$
T \bvec v = (\sum_{j = 1}^n D_{n + j} f_1 \Big |_{(\bvec a, \bvec b)} v_j, \ldots, \sum_{j = 1}^n D_{n + j} f_n \Big |_{(\bvec a, \bvec b)} v_j)
$$
and if $T$ is invertible, there is an open set $A \subset \bb R^n$ and an open set $B \subset \bb R^m$ with $(\bvec a, \bvec b) \in A \times B$ such that for each $\bvec x \in A$, there is a unique $g(\bvec x) \in B$ such that $f(\bvec x, g(\bvec x)) = \bvec 0$ and $g$ is differentiable.

###### _proof:_

First we have to show that the derivative of $f_{|\bb R^m}$ really does take the given form. The $j$th partial of the $i$th component function of $f_{|\bb R^m}$ is
$$
\begin{split}
D_j f_{i|\bb R^m} \Big |_{\bvec b} & = \lim_{h \to 0} \frac{f_{i|\bb R^m}(b_1, \ldots, b_j + h, \ldots, b_n) - f_{i|\bb R^m}(\bvec b)}{h} \\
& = \lim_{h \to 0} \frac{f_i(\bvec a, b_1, \ldots, b_j + h, \ldots, b_n) - f_i(\bvec a, \bvec b)}{h} \\
& = D_{n + j} f_i \Big |_{(\bvec a, \bvec b)}.
\end{split}
$$

Since these are all continuous partials of $f_i$, $f_{i|\bb R^n}$ is continuously differentiable, and then we have the desired derivative $T$ composed from the partials. Also note that this tells us that $Df_{|\bb R^m} \Big |_{\bvec b}$ is the same as $(Df \Big |_{(\bvec a, \bvec b)})_{|\bb R^m}$.

Consider also $f_{|\bb R^n} : \bb R^n \to \bb R^m$ defined by $f_{|\bb R^n}(\bvec x) = f(\bvec x, \bvec b)$. Clearly, $f_{|\bb R^n}(\bvec a) = f_{|\bb R^m}(\bvec b) = \bvec 0$. Also, $f_{|\bb R^n}$ is $\mathcal C^1$ too, with its Jacobian composed of the remaining partials of $f$ in the obvious way.

For any $\varepsilon > 0$, there is some $\delta > 0$ such that if $\bvec v \in \bb R^n$ with $\norm{\bvec v} < \delta$ then consider $f_{|\bb R^n}(\bvec a + \bvec v)$. We must have $\norm{f_{|\bb R^n}(\bvec a + \bvec v)} < \varepsilon$. Thus, we can get this $\varepsilon$-neighbourhood small enough that it is in the open set $W$ on which the function $f_{|\bb R^m|V} : V \to W$ has an inverse by the [[#_theorem _ the inverse function theorem|inverse function theorem]]. Since this is a $\varepsilon$-neighbourhood of $\bvec 0$, we also have $-f_{|\bb R^n}(\bvec a + \bvec v)$ in it. 

Since $f_{|\bb R^m|V} : V \to W$ has a differentiable inverse we can have
$$
D f^{-1}_{|\bb R^n|V} \Big |_{\bvec b}(-f_{|\bb R^n}(\bvec a + \bvec v)) = T^{-1}(-f(\bvec a + \bvec v)) = \bvec u.
$$
Thus, $f_{|\bb R^m}(\bvec b + \bvec u) - f_{|\bb R^m}(\bvec b)$ is well approximated by $-f(\bvec a + \bvec v)$

%%
