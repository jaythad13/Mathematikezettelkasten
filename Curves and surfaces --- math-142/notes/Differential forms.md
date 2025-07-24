---
tags:
- diff-geo
- math-142/5
- math-142/6
---

Differential forms help us understanding things we've seen in vector calculus

### Motivating questions

We've already seen that given some smooth $f : \mathbb{R}^3 \to \mathbb{R}$, then $df$ is a $1$-form. This naturally [[Curves and surfaces --- math-142/notes/Differential 1-forms#_proposition _ $d$ is a linear map|led us to ask:]] if $\phi \in \Omega^1(\mathbb{R}^3)$, then must we have $\phi = df$ for some smooth function $f$?

This is really asking whether, if we have $\phi = P \, dx + Q \, dy + R \, dz$, is there some $f : \mathbb{R}^3 \to \mathbb{R}$ with partials $P, Q, R$. In multivariable calculus, we showed that this is true exactly when $\operatorname{curl}(P, Q, R) = 0$ (think of $(P, Q, R)$ as defining a vector field in the obvious way, or just do the computation as if it was). Note how the computation of the curl is alternating in some sense!

If we try to generalise this, we should get something like $\phi = df$ if $d \phi = 0$, which is kind of like the converse of [[Curves and surfaces --- math-142/notes/Differential 1-forms|what we hinted at earlier]] with $d^2 = 0$. More importantly $d \phi$ should be some alternating determinant type expression!

### Differential $k$-forms

> A differential $k$-form is just something you integrate over $k$-dimensional things

\- Someone, probably

The most obvious definition we can make is

##### _definition:_ $0$-forms

A $0$-form on $\mathbb{R}^3$ is a smooth function $f \in \mathcal{C}^\infty(\mathbb{R}^3)$.

The collection of all $0$-forms on $\mathbb{R}^3$ is $\Omega^0(\mathbb{R}^3)$

### Exterior algebra and differential $2$-forms

Recall the idea of a [[Linear algebra done right --- ladr/notes/Product spaces|product vector space]]. We can do this with modules too, and especially $\Omega^1(\mathbb{R}^3)$

While we want a sort of bilinearity over the product space with
$$
(f \phi, \psi) = f(\phi, \psi)
$$
and
$$
(\phi_{1} + \phi_{2}, \psi) = (\phi_{1}, \psi) + (\phi_{2}, \psi)
$$
and a sort of alternating structure with
$$
(\phi, \psi) = - (\psi, \phi).
$$

(Note that the alternating gives us linearity in the second slot as well)

While these aren't true in the normal product space, if we define a new product, $\wedge$ so that they are true, we get the wedge space $\wedge ^2(V)$. We get this by quotienting $V \times V$ by the set of the span of all of these relations. We won't define this explicitly, but we will use $\wedge^2(\Omega^1(\mathbb{R}^3))$.

##### _definition:_ wedge square

The wedge square $\wedge^2(V)$ of any vector space $V$ is 
$$
V \otimes V /\operatorname{span} \{ (\phi, \psi) + (\psi, \phi) \}.
$$

The wedge product $\phi \wedge \psi$ is the coset corresponding to $\phi \otimes \psi$ in this quotient. 

To understand this, we need to understand what $\otimes$ means.

$V \otimes V$ is the space of all bilinear maps $l : V \times V \to \mathbb{F}$ where $\mathbb{F}$ is the base field (or ring). By $v_{1} \otimes v_{2}$ for $v_{1}, v_{2} \in V$, we mean the bilinear map by
$$
(u_{1}, u_{2}) \mapsto \begin{cases}
1 & u_{i} = v_{i} \\
0
\end{cases}
$$
where the rest of the map is defined by $0$ wherever possible without breaking linearity (?)

%% ask about this!!! %%

##### _definition:_ tensor product

The tensor product $V \otimes V$ is a collection of all bilinear maps $l : V \times V \to \mathbb{F}$ where $\mathbb{F}$ is the base field (or ring, for modules).

Let's look at an explicit computation to stop our heads from hurting.

##### _example:_ the wedge product of two forms

Suppose $\phi  = f_{1} \, dx_{1} + f_{2} \, dx_{2} + f_{3} \, dx_{3}$ and $\psi = g_{1} \, dx_{1} + g_{2} \, dx_{2} + g_{3} \, dx_{3}$. What is $\phi \wedge \psi$?
$$
\begin{split}
\phi \wedge \psi & = \left( \sum_{i = 1}^3 (f_{i} \, dx_{i}) \right) \bigwedge \left( \sum_{i = 1}^3 (g_{i} \, dx_{i}) \right) \\
& = \left( \sum_{i = 1}^3 \sum_{j = 1}^3 f_{i} g_{j} \, dx_{i} \wedge dx_{j} \right)
\end{split}
$$
From here, we can use the alternating property to get
$$
\phi \wedge \psi = (f_{1} g_{2} - f_{2} g_{1}) \, dx_{1} \wedge dx_{2} + (f_{2} g_{3} - f_{3} g_{2}) \, dx_{2} \wedge dx_{3} + (f_{3} g_{1} - f_{1} g_{3}) \, dx_{3} \wedge dx_{1}
$$

Look!

$$
\phi \wedge \psi = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
f_{1} & f_{2} & f_{3} \\
g_{1} & g_{2} & g_{3}
\end{vmatrix}
$$
where $\mathbf{i}, \mathbf{j}, \mathbf{k}$ are that basis above.

Also, if it looks like there are $\binom{n}{k}$ basis vectors for the space of $k$-forms on $\mathbb{R}^n$ that's because it's true! For now we will just say it for $n = 3$ and $k = 2$

##### _proposition:_ the basis of the wedge space

$dx_{1} \wedge dx_{2}, dx_{2} \wedge dx_{3}, dx_{3} \wedge dx_{1}$ is a basis of $\wedge^2(\Omega^1(\mathbb{R}^3))$.

###### _proof:_

We will leave the proof for later when we properly understand what this wedge space is.

##### _definition:_ differential $2$-form

A $2$-form is an element of $\wedge^2(\Omega^1(\mathbb{R}^3))$. (Note that not everything is a pure wedge product).

We denote the collection of all of them by $\Omega^2(\mathbb{R}^3)$.

### Back to differential $k$-forms

Here we will say $V = \Omega^1(\mathbb{R}^3)$ and $R = \mathcal{C}^\infty$.

Let the $k$th tensor power $V^{\otimes k}$ be all $k$-linear maps from the $k$-fold cartesian product to $R$ and let 
$$
\theta_1 \otimes \dots \otimes \theta_{k} : (\phi_{1}, \dots, \phi_{k}) \mapsto \begin{cases}
1 & \phi_{i} = \theta_{i} \\
0.
\end{cases}
$$

Then the exterior algebra $\wedge^k(V) = V/U$ where $U$ is the subspace generated by the alternating property — the span of all $\phi_{1} \otimes \dots \phi_{i} \otimes \phi_{j} \dots \otimes \phi_{k} + \phi_{1} \otimes \dots \phi_{j} \otimes \phi_{i} \dots \otimes \phi_{k}$.

But why care?

First of all, note that in $\mathbb{R}^3$, we only care about $0, 1, 2, 3$-forms, since anything else goes to zero by alternating and the pigeonhole principle (at some point you have to have two of the same $dx_{i}$ wedged together).

$0$-forms are just smooth functions, $1$-forms are exactly what we already know, $2$-forms are what we just described, and $3$-forms are spanned by just one basis vector — $dx_{1} \wedge dx_{2} \wedge dx_{3}$.

But we can still think about differential $k$-forms on any $n$-space
$$
\Omega^k(\mathbb{R}^n) = \wedge^k(\Omega^1(\mathbb{R}^n))
$$
where $\Omega^1(\mathbb{R}^n)$ has the obvious definition.

Note that
$$
\dim \Omega^k(\mathbb{R}^n) = \binom{n}{k}.
$$

Also note that while we usually think of just the $k$-forms on $\mathbb{R}^n$ for some specific $k$, we can think of all the differential forms on $\mathbb{R}^n$ by thinking about the direct sum of all $\Omega^k(\mathbb{R}^n)$ for all $k \le n$ and the wedge product of things from two different spaces as just the wedge product of their basis representations (a multiple wedge product of $dx_{i}$ type $1$-forms). 