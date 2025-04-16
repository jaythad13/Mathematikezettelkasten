---
tags:
- math-199DR/22
- cx-geo
- alg-geo
---

Let $X$ be an [[Introduction to Riemann Surfaces --- math-199DR/notes/Algebraic curves#_definition _ algebraic curve|algebraic curve]].

The Riemann–Roch theorem allows us to embed curves into projective space.

### Curves of low genus

We can show fairly easily that curves of low genus have projective embeddings. For genus $0$, there is exactly one (compact, connected) Riemann surface — the Riemann sphere.

##### _theorem:_ classification of genus $0$ curves

If $X$ has [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological invariants of a surface#_definition _ genus|genus]] $0$, then $X \cong \mathbb{C}_{\infty}$.

###### _proof:_

Choose one point $p$ and consider the divisor $D_{p}$ with $D_{p}(p) = 1$ and $D = 0$ for all other points. By [[Introduction to Riemann Surfaces --- math-199DR/notes/The Riemann-Roch theorem#_corollary _ Riemann–Roch for big divisors|the Riemann-Roch theorem for big divisors]], since $\deg D_{p} = 1 \geq 2g_{X} - 1$, we have $\dim \mathcal{L}(D_{p}) = 2$.

Thus, there is a non-constant meromorphic function $f$ with at worst a simple pole at $p$. But then the [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_proposition _ meromorphic functions are maps to the Riemann sphere|corresponding holomorphism to the Riemann sphere]] $\pi_{f}$ has [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_definition _ degree at a point|degree]] $1$ at $\infty$, [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_theorem _ degree is constant|and thus,]] degree $1$ everywhere. Then, $\pi_{f}$ [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_corollary _ isomorphism is determined by degree|is an isomorphism]] $X \to \mathbb{C}_{\infty}$.

Of course, since the Riemann sphere is $\mathbb{P} \mathbb{C}^1$, this is a projective embedding.

We can use a similar trick to classify curves of genus $1$, but we will need a lot more work. What we want to do is express every genus $1$ curve in Weierstrass form — as the compactification of the complex points of some curve $y^{2} = x^{3} + Ax + B$. 

##### _theorem:_ classification of genus $1$ curves

If $X$ has genus $1$, then $X \cong \{ (x, y) \in \mathbb{C}^{2} \mid y^{2} = x^3 + Ax + B \} \cup \{ \infty \}$.

###### _proof:_

Again, using Riemann–Roch for big divisors, we see that the divisor $D_{p}$ has $\dim \mathcal{L}(mD_{p}) = m$. From here we can use dimension counting arguments to get $7$ meromorphic functions in $\mathcal{L}(6 D_{p})$ expressed as polynomials of the basic non-constant meromorphic functions $x, y$. In particular, we claim
$$
\mathcal{L}(6 D_{p}) = \operatorname{span} (1, x, x^{2}, y, xy, y^{2}, x^3)
$$
where $y^{2}, x^3$ both have a pole of order $6$ at $p$ (and in fact, the functions are listed in increasing order of pole at $p$). Since $\mathcal{L}(6 D_{p})$ is only $6$ dimensional, and we already have that the lists without one of $y^{2}, x^3$ are linearly independent, we have an equation
$$
a_{1} y^2 + a_{2} y + a_{3} xy = a_{4} x^3 + a_{5} x^{2} + a_{6} x + a_{7}
$$
with $a_{1}$ and $a_{4}$ non-zero. By some magic algebra we can depress the cubic on the right and rewrite the quadratic on the left to get
$$
Y^{2} = X^{3} + AX + B
$$
for some meromorphic functions $X, Y$. From now on we relabel these $x, y$ to avoid confusion with the algebraic curve $X$ itself. 

We now have a map $\Phi : X \to \mathbb{P} \mathbb{C}^{2}$ by
$$
\Phi(q) = \begin{cases}
(x(q) : y(q) : 1) & q \neq p \\
(0 : 1 : 0) & q = p
\end{cases}
$$
We claim that this is [[Introduction to Riemann Surfaces --- math-199DR/notes/Divisors for projective embeddings#_definition _ holomorphic maps to projective space|holomorphic]] and can be written as $(x(q) : y(q) : z(q))$ (which is not so hard to prove but we will not do) and that it is an isomorphism onto the image $C$ in $\mathbb{P} \mathbb{C}^{2}$ since each component of the function is degree $1$.

Consider the projection map $\pi_{x} : C \to \mathbb{C}_{\infty}$ by $(x : y : z) \mapsto x / z$ for $z \neq 0$, and $(x : y : 0) \mapsto \infty$ . Since the diagram
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		X \ar[r, "\Phi"] \ar[rd, "x"] & C \ar[d, "\pi_{x}"] \\
		& \mathbb{C}_{\infty}
	\end{tikzcd}
\end{document}
```
commutes, and degree is multiplicative, we know that $(\deg \Phi) (\deg \pi_{x}) = \deg x = 2$. We claim $\deg \pi_{x} = 2$. This follows since given most $x / z$, there are typically two values of $y$ satisfying $y^{2} = x^3 / z + A x z + B z^{2}$ and thus, two points $(x : y_{1} : z)$ and $(x : y_{2} : z)$ mapping to $x / z$. Since degree of the composition $\pi_{x} \circ \Phi$ is just the product of degrees, it follows that $\deg \pi_{x} = 1$.

##### _example:_ a genus $1$ curve

The curve $\{ (a : b : c) \in \mathbb{P} \mathbb{C}^{2} \mid a^{3} + b^{3} = c^{3} \}$ is genus $1$ since $x = \frac{c}{a + b}$ has a pole of order $2$ at $p$ and $y = \frac{a - b}{a + b}$ has a pole of order $3$ at $p$. The functions $x, y$ satisfy the relation
$$
3 y^{2} = 3 \left( \frac{a - b}{a + b} \right)^2 = 4 \frac{a^{3} + b^{3}}{(a + b)^3} - 1 = 4 \left( \frac{c}{a + b} \right)^3 - 1 = 4 x^3 - 1
$$
By some simple substitutions scaling $x, y$ this can of course be put in the form
$$
y^{2} = x^3 + A x + B.
$$
Note that this form is not necessarily unique — we could have
$$
y^{2} = x^3 - 432
$$
or
$$
y^{2} = x^3 - \frac{1}{4}.
$$
