---
tags:
- math-176/15
- math-176/16
- alg-geo
---

Varieties are the great generalisation of lines. The simplest case is that of non-singular projective varieties.

##### _definition:_ non-singular projective variety

Let $F$ be a field. A subset
$$
V(F) = \{ p \in \mathbb{P}^n(F) \mid f_{1}(p) = \dots = f_m(p) = 0 \}
$$
is called a non-singular projective variety of dimension $d$ if the following axioms hold.
1) Homogeneity: each $f_{k}$ is a [[Algebraic Geometry --- math-176/notes/Diophantine equations#_definition _ homogenous polynomial|homogenous]] polynomial in ,of degree $e_{k}$ in $F[x_{1}, \dots, x_{n}, x_{0}]$.
2) Non-singularity: the $m$-by-$(n + 1)$ Jacobian of the function $f = (f_{1}, \dots, f_{m})$ has rank $m$ for all points $p \in \mathbb{P}^n(\overline{F})$, in the zero set of $f_{1}, \dots, f_{m}$, where $\overline{F}$ is the algebraic closure of $F$. That is, the Jacobian has rank $m$ for all points $p \in V(\overline{F})$.
3) Irreducibility: if $S(e)$ is the collection of homogenous polynomials of degree $e$ in $F[x_{1}, \dots, x_{n}, x_{0}]$. Then the ideal
$$
I(V) = \bigoplus_{e \ge 1} \{ f(x_{1}, \dots, x_{n}, x_{0}) \in S(e) \mid f(p) = 0 \text{ for all } p \in V(F) \}
$$
is a [[Abstract Algebra I --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|prime ideal]] in the graded polynomial ring $S = \bigoplus_{e \ge 1} S(e)$. (This condition says that we're using the minimal set of polynomials)
4) The dimension is $d = n - m$.

Often for $d = 1$ we say $V$ is a surface, for $d = 2$, we say $V$ is a surface, and for $d = 3$, we say $V$ is a $3$-fold.

What the fuck does this mean?

> Algebraic geometry is a revisionist history course

\- Edray Goins

Let's look at an example.

### Affine vs. projective curves

We can start with an irreducible
$$
f(x, y) = \sum_{i, j} a_{ij} x^i y^{j}
$$
in $F[x, y]$.

It makes complete sense to say that the zero set of $f$ is an affine curve. In fact, it makes sense to use this idea to define an affine curve in a plane —

##### _definition:_ affine plane curve

An affine plane curve in $\mathbb{A}^2(F)$ is the zero set of a polynomial $f \in F[x, y]$.

How can we relate this to a non-singular projective variety of dimension $d = 1$?

First, we turn $f$ into a homogenous polynomial in $F[x_{1}, x_{2}, x_{0}]$ by substituting $x = \frac{x_{1}}{x_{0}}$ and $y = \frac{x_{2}}{x_{0}}$. Then
$$
f(x, y) = \frac{\sum_{i, j} a_{ij} x_{1}^i x_{2}^j x_{0}^{e - i - j}}{x_{0}^e} 
$$
Thus,
$$
g(x_{1}, x_{2}, x_{0}) = \sum_{i, j} a_{ij} x_{1}^i x_{2}^j x_{0}^{e - i - j}
$$
is a homogenous polynomial of degree $e$.

Consider $V(F) = \{ (x_{1} : x_{2} : x_{0}) \in \mathbb{P}^2(F) \mid g(x_{1}, x_{2}, x_{0}) = 0 \}$. Notice that the embedding $\mathbb{A}^2(F) \xhookrightarrow{} \mathbb{P}^2(F)$ by $(x, y) \mapsto (x : y : 1)$ also embeds the affine curve defined by $f$ into the variety $V(F)$. 

Putting in $x_{0} = 1$ in $V(F)$ clearly recovers the affine curve, and thus, so do all points with $x_{0} \neq 0$. What about $x_{0} = 0$? Since this is the intersection of $V(F)$, a curve with the [[Algebraic Geometry --- math-176/notes/Projective space#_example _ projective line|line at infinity]] $x_{0} = 0$. This covers all the points in $V(F)$! Thus,
$$
V(F) = \{ (x : y : 1) \mid f(x, y) = 0 \} \cup X
$$
where $X$ is a set of finitely many points at infinity.

##### _example:_ the projective line is a non-singular projective curve

Consider the affine line $L = \{ (x, y) \in \mathbb{A}^2(F) \mid ax + by + c = 0 \}$. In order for this to be a sensible line, of course we have $a, b, c$ not all zero.

This corresponds to the homogenous polynomial $g \in F[x_{1}, x_{2}, x_{0}]$ with $g(x_{1} : x_{2} : x_{0}) = ax_{1} + bx_{2} + cx_{0}$. $g$ clearly has Jacobian $\begin{bmatrix} a  & b & c \end{bmatrix}$ at every point. This is rank $1$ everywhere, as long as $a, b, c$ are not all zero. We won't worry about irreducibility right now. Just note that it holds. Finally, the dimension is $2 - 1 = 1$. Thus, the line is a non-singular projective curve.

The points of infinity are points $(x_{1} : x_{2} : x_{0})$ that satisfy $g(x_{1} : x_{2} : x_{0}) = 0$ and $x_{0} = 0$. Thus, we must have $ax_{1} + bx_{2} = 0$ or and then $x_{1} : x_{2} = -b : a$ Thus, $(x_{1} : x_{2} : x_{0}) = (-b : a : 0)$. That is, if $L_{\mathbb{P}}$ is $L$ embedded in projective space, then
$$
V(F) = \{ p \in \mathbb{P}^2(F) \mid g(p) = 0 \}
$$
is $L_{\mathbb{P}}$ with finitely many points at infinity —
$$
V(F) = L_{\mathbb{P}} \cup \{ (-b : a : 0) \}
$$

##### _example:_ elliptic curves in projective space

Consider the affine cubic curve $E = \{ (x, y) \in \mathbb{A}^{2}(F) \mid y^{2} + a_{1} xy + a_{3} y = x^3 + a_{2} x^{2} + a_{4} x + a_{6} \}$. $E$ corresponds to the homogenous polynomial
$$
g(x_{1} : x_{2} : x_{0}) = (x_{1}^3 + a_{2} x_{1}^{2} x_{0} + a_{4} x_{1} x_{0}^{2} + a_{6} x_{0}^3) - (x_{2}^{2} x_{0} + a_{1} x_{1} x_{2} x_{0} + a_{3} x_{2} x_{0}^{2})
$$
Again, $V(F) = \{ p \in \mathbb{P}^2(F) \mid g(p) = 0 \}$ has only one point at infinity! Notice that $g(x_{1} : x_{2} : 0) = x_{1}^3$. Thus, $x_{1} = 0$ as well. Then we're left with only $O_{E} = (0 : 1 : 0)$ as a possible point at infinity.

Do we really want to do all the differentiation to show this is non-singular though?
