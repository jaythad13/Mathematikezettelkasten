---
tags:
- math-199DR/18
- cx-geo
- alg-geo
---

Let $X$ be a compact, connected Riemann surface.

Divisors naturally arise from functions — they keep track of their zeroes and poles. We can also define the spaces of functions and forms corresponding to the divisor $D$. These are the spaces of meromorphic functions and forms with poles that are "at worst" $D$. To define this, we need to define an ordering on $\operatorname{Div} X$.

##### _definition:_ ordering on divisors

There is a partial order on $\operatorname{Div} X$ where $D_{1} \ge D_{2}$ if $D_{1}(p) \geq D_{2}(p)$ at every $p \in X$.

$D_{1} > D_{2}$ if $D_{1} \geq D_{2}$ and $D_{1} \neq D_{2}$.

### The Riemann-Roch space of meromorphic functions

Then the Riemann-Roch function space of a divisor is the $\mathbb{C}$-vector space of meromorphic functions bounded by the divisor.

##### _definition:_ the Riemann-Roch function space of a divisor

Given $D \in \operatorname{Div} X$, the Riemann-Roch function space of $D$ is the vector space and $\mathcal{O}_{X}(X)$-module (not an $\mathcal{O}_{X}$-module)
$$
\mathcal{L}(D) = \{ f \in \mathcal{M}_{X}(X) \mid \operatorname{div} f \geq -D \}
$$

Given $f, g \in \mathcal{L}(D)$. It's easy to see $\lambda f \in \mathcal{L}(D)$ for $\lambda \in \mathbb{C}$, it follows that $f + g \in \mathcal{L}(D)$ since

##### _example:_ the function space of a divisor on the Riemann sphere

On the Riemann sphere, by allowing more poles at infinity, we allow more poles elsewhere. For example, the divisor $D = - 2 \cdot 4 + 3 \cdot i + 3 \cdot \infty$ has a space of functions that all vanish in degree $2$ at $4$ and have, at worst, poles of order $3$ at $i$ and infinity.
$$
\mathcal{L}(D) = \left\{  \frac{(z - 4)^2}{(z - i)^3} p(z) \mid \operatorname{deg} p \le 4  \right\}
$$
where $p$ is a polynomial. Notice then that $\mathcal{L}(D)$ is in some sense just the space of polynomials of degree at most $4$.

##### _lemma:_ negative degree divisors bound no functions

If $\operatorname{deg} D < 0$ the Riemann-Roch space $\mathcal{L}(D)$ is the trivial module $\{ 0 \}$.

###### _proof:_

$\operatorname{deg} D < 0$ means that functions in $\mathcal{L}(D)$ are required to have more zeroes than poles. Briefly, for non-zero $f \in \mathcal{L}(D)$
$$
\operatorname{div} f + D \ge 0
$$
forces
$$
\operatorname{deg} (\operatorname{div} f) + \operatorname{deg} D \geq 0 
$$
and thus, $\operatorname{deg} D \geq 0$ which is a contradiction.

##### _proposition:_ the space corresponding to the sum of divisors

There is a map $\mathcal{L}(D_{1}) \otimes \mathcal{L}(D_{2}) \to \mathcal{L}(D_{1} + D_{2})$.

###### _proof sketch:_

Consider $f \otimes g \mapsto fg$.

Ultimately, this allows us to think about $\mathcal{L}$ in some functorial way as an invertible sheaf and eventually, an $\mathcal{O}_{X}$-module.

##### _proposition:_ linear equivalence induces an isomorphism of function spaces

If $D_{1}, D_{2} \in \operatorname{Div} X$ are linearly equivalent then, $\mathcal{L}(D_{1}) \cong \mathcal{L}(D_{2})$.

###### _proof:_

Suppose $D_{1} = D_{2} + \operatorname{div} g$ and consider the map
$$
\begin{align}
\varphi & : \mathcal{L}(D_{1}) \to \mathcal{L}(D_{2}) \\
 & : f \mapsto fg.
\end{align}
$$

It really is a map to $\mathcal{L}(D_{2})$ because
$$
\operatorname{div}(fg) + D_{2} = \operatorname{div} f + \operatorname{div} g + D_{1} - \operatorname{div} g = \operatorname{div} f + D_{1} \geq 0.
$$
$\varphi$ is clearly $\mathbb{C}$-linear (by associativity of multiplication). It also has an inverse map $\varphi ^{-1} : f \to f / g$ which is linear and well-defined for the same reasons, so it is an isomorphism.

This gives us a nice way to compute the entire space of functions associated to a divisor on the Riemann sphere. 

##### _example:_ function spaces on the Riemann sphere

Using the notion of equivalence of divisors, we can formalise the intuition of our specific example. For any positive degree $D \in \operatorname{Div} \mathbb{C}_{\infty}$, we have $\mathcal{L}(D) \cong \mathcal{L}(\operatorname{deg} D \cdot \infty)$ — on $\mathbb{C}_{\infty}$, [[Introduction to Riemann Surfaces --- math-199DR/notes/Linear equivalence of divisors#_example _ linear equivalence on the Riemann sphere|divisors of same degree are linearly equivalent]]. But then we know from complex analysis that $\mathcal{L}(\operatorname{deg} D \cdot \infty)$ is just the space of polynomials of degree at most $\operatorname{deg} D$. Thus, we have $\operatorname{dim} \mathcal{L}(D) = \operatorname{deg} D + 1$.

Of course if $\operatorname{deg} D < 0$, then $\mathcal{L}(D)$ is trivial.

This, like most things to do with divisors, meromorphic functions, and forms on $\mathbb{C}_{\infty}$ is exceptional (which is why the Riemann-Roch theorem is non-trivial). In higher genera this fails.

##### _example:_ function spaces on the torus

On a complex torus $\mathbb{C} / \Lambda$, for any $D \in \operatorname{Div}(\mathbb{C} / \Lambda)$, we have
$$
\mathcal{L}(D) = \begin{cases}
0 & \operatorname{deg} D < 0 \\
1 & \operatorname{deg} D = 0, D \sim 0 \\
0 & \deg D = 0, D \not \sim 0 \\
1 & \deg D > 0.
\end{cases}
$$

### The Riemann-Roch form space of a divisor

We can do the same thing for meromorphic $1$-forms!

##### _definition:_ the Riemann-Roch form space of a divisor

Given $D \in \operatorname{Div} X$, the Riemann-Roch form space of $D$ is the vector space and $\mathcal{O}_{X}(X)$-module (not an $\mathcal{O}_{X}$-module)
$$
\mathcal{L}(D) = \{ f \in \mathcal{M}_{X}(X) \mid \operatorname{div} f \geq -D \}
$$

Given $f, g \in \mathcal{L}(D)$. It's easy to see $\lambda f \in \mathcal{L}(D)$ for $\lambda \in \mathbb{C}$. It follows that $f + g \in \mathcal{L}(D)$ from the fact that $\operatorname{ord}_{p}(f + g) \geq \min \{ \operatorname{ord}_{p}f, \operatorname{ord}_{p}g \}$.

In fact, divisors give us a way to identify $1$-forms with meromorphic functions.

##### _proposition:_ isomorphism between function and form spaces

For a [[Introduction to Riemann Surfaces --- math-199DR/notes/Divisors#_definition _ canonical divisor|canonical divisor]] $K$ there is an isomorphism $\mathcal{L}(D + K) \cong \mathcal{L}^{(1)}(D)$.

###### _proof sketch:_

For $K = \operatorname{div} \omega$, use the obvious map
$$
\begin{align}
\varphi  & : \mathcal{L}(D + K) \to \mathcal{L}^{(1)}(D) \\
 & : f \mapsto f \omega.
\end{align}
$$
$\mathbb{C}$-linearity and injectivity follow easily. However, we have to prove surjectivity separately. [[Introduction to Riemann Surfaces --- math-199DR/notes/Divisors#_proposition _ the difference of divisors of meromorphic $1$-forms|Recall]] that any $\eta \in \mathcal{L}^{(1)}(D)$ has $\eta = f \omega$ for some meromorphic $f$. Using the bounds on $\operatorname{div} \omega$ and $\operatorname{div} \eta$, we get the bounds on $\operatorname{div} f$ —
$$
	\operatorname{div} f +  D + K = \operatorname{div} \eta - \operatorname{div} \omega  + D + K = \operatorname{div} \eta + D \ge 0. 
$$