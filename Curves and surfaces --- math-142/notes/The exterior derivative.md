---
tags:
- diff-geo
- math-142/6
- math-142/7
---

[[Curves and surfaces --- math-142/notes/Differential 1-forms#_definition _ the differential/exterior derivative of a $1$-form|We know how to send]] $0$-forms to $1$-forms by
$$
d : f \mapsto Df.
$$

We also saw how a $1$-form is always a derivative of a $0$-form if it has zero curl.

### A special case: the curl

How do we generalise this to sending $1$-forms to $2$-forms?

##### _definition:_ the exterior derivative of $1$-forms

$$
d: \sum f_{i} dx_{i} \mapsto \sum df_{i} \wedge dx_{i}
$$
is the map that sends any $1$-form to the $2$-form that is its exterior derivative.

Note that this is exactly the generalisation we wanted — it looks like the curl! That is, for $\mathbf{F} = (f_{1}, f_{2}, f_{3})$ is a vector field in the traditional multivariable calculus sense, $\nabla \times \mathbf{F}$ has the same components as $d(f_{1} \, dx_{1} + \dots + f_{3} \, dx_{3})$ and you can just replace $\mathbf{i}$ with $dx_{2} \wedge dx_{3}$ and so on.

This is an instance of [[Hodge duality]]! We will see that slapping a [[Hodge duality|Hodge star]] on that will give the [[Hodge duality|Hodge dual]] which is just the dual (in the normal linear algebra sense) of the curl.

It is also a linear map and follows the Leibniz rule like anything that claims to be a derivative should be. We will prove these after we define them more generally.

Finally, it preserves the really important property $d^2 = 0$ [[Curves and surfaces --- math-142/notes/Differential forms#Motivating questions|that we've been hinting at]] — $\phi = df$ for some smooth function $f$, if and only if $d\phi = 0$ (here $\phi$ is a $1$-form).

### The exterior derivative, in general

More generally, for $k$-forms on $\mathbb{R}^n$ we have

##### _definition:_ the exterior derivative

The exterior derivative is the linear map
$$
d : \Omega^k(\mathbb{R}^n) \to \Omega^{k + 1}(\mathbb{R}^n)
$$
by
$$
d : \sum f_{I} dx_{I} \mapsto \sum df_{I} \wedge dx_{I}
$$
where $I$ is a multi-index of order $k$ on $\mathbb{N}_{n}$ and $dx_{I}$ is a wedge of $k$ $dx_{i_{j}}$s where the $k$ $i_{j}$s are the $k$ $i_{j}$s in the index of $f$. The sum is over all of these $\binom{n}{k}$ choices. I probably should have just written it out more obviously.

##### _example:_ curl and divergence

Note that in the special case of $2$-forms on $\mathbb{R}^3$ we get another really nice result. For $\phi = f_{1} \, dx_{2} \wedge dx_{3} + f_{2} \, dx_{3} \wedge dx_{1} + f_{3} \, dx_{1} \wedge dx_{3}$, we have
$$
d \phi = \left ( \frac{ \partial f_{1} }{ \partial x_{1} } + \frac{ \partial f_{2} }{ \partial x_{2} } + \frac{ \partial f_{3} }{ \partial x_{3} } \right ) \, dx_{1} \wedge dx_{2} \wedge dx_{3}  
$$
which looks exactly like the divergence.

Again, [[Hodge duality]]! We will see that slapping a [[Hodge duality|Hodge star]] on that will give the [[Hodge duality|Hodge dual]] which is just the dual (in the normal linear algebra sense) of the divergence (in this case, since $\mathbb{R}^\vee = \mathbb{R}$, it is just the divergence itself).

If we generalise the $\phi \in d^\text{img}(\Omega^{k - 1}(\mathbb{R}^n)) \iff \phi \in \ker d$ thing and apply it to this, we just get [[Gauss' divergence theorem]] from multivariable calculus!

### Properties of the exterior derivative

Here are all the properties (with proof) that we claimed the exterior derivative has but didn't quite prove that it has.

##### _proposition:_ the exterior derivative is linear over $\mathbb{R}$

For $\phi, \psi \in \Omega^k(\mathbb{R}^n)$, we have $\eta = a \, \phi + b \, \psi \in \Omega^k(\mathbb{R}^n)$ for scalars $a, b \in \mathbb{R}$ and
$$
d \eta = a \, d\phi + b \, d\psi \in \Omega^k(\mathbb{R}^n)
$$

###### _proof:_

Let $\phi = \sum f_{I} \, dx_{I}$ and $\psi = \sum g_{I} \, dx_{I}$. Then $a \, \phi + b \, \psi = \sum (a \, f_{I} + b \, g_{I}) \, dx_{I}$. Thus,
$$
\begin{split}
d(\phi + \psi) & = \sum d(a \, f_{I} + b \, g_{I}) \wedge dx_{I} \\
& = \sum (a \, df_{I} + b \, dg_{I}) \wedge dx_{I} \\
& = \sum a \, df_{I} \wedge dx_{I} + b \, dg_{I} \wedge dx_{I} \\
& = a \sum df_{I} \wedge dx_{I} + b \sum dg_{I} \wedge dx_{I} \\
& = a \, d\phi + b \, d\psi
\end{split}
$$
where the second step follows since we've already defined the linearity of the derivative of a $0$-form, and the third and second to last steps follow by the distributivity of the wedge product.

##### _proposition:_ the (graded) Leibniz rule

For $\phi \in \Omega^k(\mathbb{R}^n)$ and $\psi \in \Omega^l(\mathbb{R}^n)$ we have
$$
d(\phi \wedge \psi) = d \phi \wedge \psi + (-1)^k (\phi \wedge d\psi).
$$
###### _proof:_

Let $\phi = \sum_{I} f_{I} \, dx_{I}$ and $\psi = \sum_{J} g_{J} \, dx_{J}$ where $I$ is a multi-index of order $k$ and $J$ is a multi-index of order $l$, both on $\mathbb{N}_{n}$. Then $\phi \wedge \psi = \sum_{I, J} f_{I} \, g_{J} \, dx_{I} \wedge dx_{J}$, where by summing over $I, J$ we mean to sum over all possible choices of the pair $I, J$. From here we just bash —
$$
\begin{split}
d(\phi \wedge \psi) & = \sum_{I, J} d(f_{I} \, g_{J}) \, dx_{I} \wedge dx_{J} \\
& = \sum_{I, J} \sum_{r = 1}^n \frac{ \partial (f_{I} g_{J}) }{ \partial x_{r} } \, dx_{r} \wedge dx_{I} \wedge dx_{J} \\
& = ( \sum_{I, J} \sum_{r = 1}^n \frac{ \partial f_{I} }{ \partial x_{r} } \, g_{J} \, dx_{r} \wedge dx_{I} \wedge dx_{J} ) + (\sum_{I, J} \sum_{r = 1}^n f_{I} \, \frac{ \partial g_{J} }{ \partial x_{r} } \, dx_{r} \wedge dx_{I} \wedge dx_{J}).
\end{split}
$$
Note that since $dx_{I}$ is a $k$-form, $dx_{r} \wedge dx_{I} = (-1)^k dx_{I} \wedge dx_{r}$. Applying this allows us to continue from where we left off —
$$
\begin{split}
d(\phi \wedge \psi) & = \left(  \sum_{I, J} \sum_{r = 1}^n \frac{ \partial f_{I} }{ \partial x_{r} } \, g_{J} \, dx_{r} \wedge dx_{I} \wedge dx_{J}  \right) + (-1)^k \left( \sum_{I, J} \sum_{r = 1}^n f_{I} \, \frac{ \partial g_{J} }{ \partial x_{r} } \, dx_{I} \wedge dx_{r} \wedge dx_{J} \right) \\
& = \left(  \sum_{I} \sum_{r = 1}^n \frac{ \partial f_{I} }{ \partial x_{r} } \, dx_{r} \wedge dx_{I}  \right) \wedge \sum_{J} g_{J} \, dx_{J} + (-1)^k (\sum_{I} f_{I} \, dx_{I}) \left ( \sum_{J} \sum_{r = 1}^n \, \frac{ \partial g_{J} }{ \partial x_{r} } \, dx_{r} \wedge dx_{J} \right) \\
& = d \phi \wedge \psi + (-1)^k (\phi \wedge d\psi).
\end{split}
$$

##### _proposition:_ $d^2 = 0$

$d^2 : \Omega^k(\mathbb{R}^n) \to \Omega^{k + 2}(\mathbb{R}^n)$ by $\phi \mapsto d(d \phi)$ is the $0$ operator.

Equivalently, $d(d \phi) = 0$ for any $\phi \in \Omega^k(\mathbb{R}^n)$.

###### _proof:_

Let $\phi = \sum f_{I} \, dx_{I}$. Then $d\phi = \sum df_{I} \wedge dx_{I}$ which we can rewrite as
$$
d\phi = \sum_{I} \sum_{j = 1}^n \frac{ \partial f_{I} }{ \partial x_{j} }  dx_{j} \wedge dx_{I}
$$
Let $\omega_{I} = \sum_{j = 1}^n \frac{ \partial f_{I} }{ \partial x_{j} }  dx_{j} \wedge dx_{I}$ for any choice of multi-index $I$. We will show that it has derivative zero, and thus all sums of elements of its type are zero.
$$
\begin{split}
d \omega_{I} & = \sum_{r = 1}^n \sum_{j = 1, j \neq r}^n \frac{ \partial^2 f_{I} }{ \partial x_{r} \partial x_{j} } \, dx_{r} \wedge dx_{j} \wedge dx_{I} \\
& = \sum_{r = 1}^n \left( \sum_{j = 1}^{r - 1} \frac{ \partial^2 f_{I} }{ \partial x_{r} \partial x_{j} } \, dx_{r} \wedge dx_{j} \wedge dx_{I} + \sum_{j = r + 1}^n \frac{ \partial^2 f_{I} }{ \partial x_{r} \partial x_{j} } \, dx_{r} \wedge dx_{j} \wedge dx_{I}  \right).
\end{split}
$$

Notice that we can rearrange this! Since $1 \le k < j \le n$
$$
\begin{split}
\sum_{r = 1}^n \sum_{j = r + 1}^n \frac{ \partial^2 f_{I} }{ \partial x_{r} \partial x_{j} } \, dx_{r} \wedge dx_{j} \wedge dx_{I} & = \sum_{j = 1}^n \sum_{r = 1}^{j - 1} \frac{ \partial^2 f_{I} }{ \partial x_{r} \partial x_{j} } \, dx_{r} \wedge dx_{j} \wedge dx_{I} \\
& = \sum_{r = 1}^n \sum_{j = 1}^{r - 1} \frac{ \partial^2 f_{I} }{ \partial x_{j} \partial x_{r} } \, dx_{j} \wedge dx_{r} \wedge dx_{I} \\
& = - \sum_{r = 1}^n \sum_{j = 1}^{r - 1} \frac{ \partial^2 f_{I} }{ \partial x_{r} \partial x_{j} } \, dx_{r} \wedge dx_{j} \wedge dx_{I}
\end{split}
$$
where the first step follows by rearranging the sum, the second step follows by just reversing the indices, and the last step follows by [[Partials and the "total" derivative#_definition _ higher order partials|Clairaut's theorem]] and the [[Curves and surfaces --- math-142/notes/Differential forms#Exterior algebra and differential $2$-forms|anticommutativity of the wedge product]]. 

Substituting this back into the expression for $d\omega_{I}$ gives us
$$
d\omega_{I} = 0
$$
and since $d(d\phi) = \sum_{I} d\omega_{I}$, we have
$$
d(d\phi) = 0
$$
as desired.

Notice how we broke stuff up into $k$-forms and $n - k$-forms? [[Hodge duality]]!