---
tags:
- math-135/12
- math-135/13
- anal
- complex
---

Recall that [[Complex analysis --- math-135/notes/What is complex analysis?#Polar representation|we defined]] $e^z = e^x e^{iy}$ for a complex number $z = x + iy$ where $e^{iy} = \cos{y} + i \sin{y}$. Thus, we noted that we could write any $w \in \mathbb{C}$ as $R e^{i \theta}$ for some $R, \theta \in \mathbb{R}$ (in fact there are infinitely many such $\theta \in \mathbb{R}$). We define

##### _definition:_ Argument

The Argument (note the capital A) of some $z \in \mathbb{C}$ is $\operatorname{Arg}(z) = \theta$ such that $z = R e^{i \theta}$ and $\theta \in [- \pi, \pi)$ for some $R \in \mathbb{R}$.

Note that we can recover any non-zero $w = a + i b$ as $w = e^z$ by choosing $z = x + iy$ such that $e^x = \lvert w \rvert$ (and thus, $x = \ln \lvert w \rvert$) and $y = \operatorname{Arg}(z)$. Thus $e^z$ maps $\mathbb{C}$ *onto* $\mathbb{C} \setminus \{ 0 \}$. Further, since $e^{iy}$ has period $2 \pi$, and $e^x$ is injective, $e^z$ is injective in any half-open horizontal strip of with $2 \pi$.

##### _notation:_ the half-open strip

For any $y_{0} \in \mathbb{R}$, let
$$
A_{y_{0}} = \{ x + i y \mid y_{0} \le y < y_{0} + 2 \pi \}.
$$

Note then that $e^z$ is a bijection $A_{y_{0}} \to \mathbb{C}$ (we've already shown it's injective; if $e^{z_{0}} = e^{z_{1}}$, they must differ by $2\pi i$, and thus cannot both be in the same half-open horizontal strip).

Now we can define the logarithm on this restricted set!

### The logarithm

##### _definition:_ logarithm, the logarithm

Given any $w \in \mathbb{C} \setminus \{ 0 \}$ we say $w$ is a logarithm of $z$ if $e^w = z$.

We call the function
$$
\begin{split}
\log & : \mathbb{C} \setminus \{ 0 \} \to A_{y_{0}} \\
 & : z \mapsto \ln \lvert z \rvert + i \theta \quad \text{where} \quad i \theta \in A_{y_{0}}
\end{split}
$$
the branch of the logarithm lying in $A_{y_{0}}$.

Note that the function $\operatorname{Log} : z \mapsto \ln \lvert z \rvert + i \operatorname{Arg} z$ is the branch of the logarithm lying in $A_{- \pi}$. This isn't actually continuous on $\mathbb{C}$ — points just above the negative real axis and just below it have completely different arguments!

##### _note:_ Riemann surfaces

This is why people think about Riemann surfaces — if you glue a whole bunch of complex planes into a manifold $X$ by joining them at the negative real axis, now $\log : X \to \mathbb{C}$ is a continuous (and locally holomorphic) function.

With all this intuition, we can consider the following equivalent definition of the logarithm —

##### _definition:_ logarithm

Let $\Omega$ be [[Complex analysis --- math-135/notes/Homotopy and simply connected domains#_definition _ simply connected|simply connected]] region containing $1$ but not $0$. We define
$$
\begin{split}
\log_{\Omega}(z) & : \Omega \to \mathbb{C} \\
 & :z \mapsto \int_{\gamma_{z}} \frac{1}{w} \, dw 
\end{split}
$$
Note that this is well defined by [[Complex analysis --- math-135/notes/Homotopy and simply connected domains#_theorem _ deformation theorem|the deformation theorem]]. Further, it agrees with the real logarithm on some small interval around $1$, and thus, is a holomorphic extension of it (just choose the straight line path along the real axis).

Now we can give an alternate definition of the principal branch of the logarithm —

##### _definition:_ $\operatorname{Log}$

$$
\operatorname{Log}(z) = \log_{\Omega}
$$
for
$$
\Omega = \mathbb{C} \setminus (- \infty, 0]
$$

##### _caution:_ the product rule does't work anymore

On a fixed branch $\log(z_{1} z_{2}) = \log(z_{1}) + \log(z_{2})$ is not always true. Consider, for example, $z_{1} = z_{2} = e^{2 \pi i/3}$. Then $\log(z_{1} z_{2}) = \log(e^{4 \pi i /3}) = -\frac{2 \pi i}{3}$.

However, note that if $w_{1} = \log_{\Omega}(z_{1})$ and $w_{2} = \log_{\Omega}(z)$, then $e^{w_{1} + w_{2}} = z_{1} z_{2}$ still holds.

### Complex powers!

Now we can define complex powers in a much more rigorous sense than we first did! Just like we can with real numbers, $a^b = e^{b \log a}$.

##### _definition:_ complex powers

For $z, a \in \mathbb{C}$. we define
$$
z^a = e^{a \log z}
$$
where $\log$ can be any logarithm of $z$.

Note that then $z^a$ is not necessarily unique unless $a \in \mathbb{Z}$.

##### _example:_ two square roots!

Using this definition, we get
$$
z^{1/2} = \pm \lvert z \rvert^{1/2} e^{i \operatorname{Arg}(z)/2}.
$$
for $n \in \mathbb{Z}$.

##### _theorem:_ logarithms of functions

Let $\Omega$ be a simply connected region. Then for any non-vanishing holomorphic function $f : \Omega \to \mathbb{C}$, there exists a holomorphic function $g : \Omega \to \mathbb{C}$ such that
$$
e^g = f.
$$

###### _proof:_

$g$ defined by
$$
g(z) = \int_{\gamma_{z}} \frac{f'(z)}{f(z)} \, dz + \log (f(z_{0}))
$$
where $\gamma_{z}$ is any path from $z_{0}$ to $z$, is that function.

Clearly we have $f = g$ at $z_{0}$. Now we have
$$
f(z_{0}) e^{- g(z_{0})} = 1.
$$
We can show that this holds everywhere by differentiating —
$$
\begin{split}
( f e^{-g} )' & = f' e^{-g} - f e^{-g} g' \\
 & = f' e^g - f \frac{f'}{f} e^{-g} \\
 & = 0.
\end{split}
$$

##### _corollary:_ functions with identical zeroes differ by an exponential

Given two holomorphic functions $f, g : \Omega \to \mathbb{C}$ with identical zeroes on simply connected region $\Omega$, 
$$
f = e^h g
$$
(except possibly at finitely many points) for some holomorphic $h$.

###### _proof sketch:_

$f/g$ only has [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#Removable singularities|removable singularities]] and so can be extended to a holomorphic function.