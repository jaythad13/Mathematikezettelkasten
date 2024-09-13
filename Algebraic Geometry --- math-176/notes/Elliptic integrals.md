---
tags:
- math-176/6
- math-176/7
- math-176/8
- alg-geo
---

When exploring different types of Diophantine equations we saw two interesting propositions — that [[Algebraic Geometry --- math-176/notes/Diophantine equations#_proposition _ Heron triangles are rational points on a quartic|Heron triangles correspond to points on the quartic]] $y^{2} = (1 - x^{2})(1 - k^{2} x^{2})$, and that $A$ is [[Algebraic Geometry --- math-176/notes/Diophantine equations#Congruent numbers|congruent if and only if the curve]] $y^{2} = x^{3} - A^{2} x$ has a rational point.

In fact, these curves have a mysterious relationship with pendulums and ellipses! We've all seen that Galileo showed the period of a simple pendulum of length $l$ to be approximately $2\pi \sqrt{ l / g }$ for small angles and that the perimeter of an ellipse is difficult to compute. Now, using some more of the mysterious substitutions we've seen in this course, we will see that Heron triangles and congruent triangles are related. In fact, they are our first example of birational equivalence!

### Pendulums

##### _proposition:_ the period of a simple pendulum

The period of a simple pendulum with mass $m$, length $l$ and initial angle $\theta_{0}$ is
$$
T = 4 \sqrt{ \frac{l}{g} } \int_{0}^{\pi / 2}  \frac{d\phi}{\sqrt{ 1 - k^{2} \sin ^{2}\phi }} 
$$
###### _proof sketch:_

Before we prove this, note that we can recover Galileo's formula by taking $\theta \approx 0$, and that the integral blows up for $\theta =\pi$ which is what we expected since at that point the pendulum doesn't move (infinite period).

To prove this formula, we use conservation of energy. Write
$$
E = \frac{m}{2} \left( l \frac{d\theta}{dt} \right)^{2} + mgl(1 - \cos \theta)
$$
for the total energy. Use $E = mgl(1 - \cos \theta_{0})$ initially to solve for
$$
dt = \sqrt{ \frac{l}{g} } \frac{d \theta}{\sqrt{ 2 (\cos\theta) - \cos \theta_{0} }}.
$$
Then $T$ is the integral of $dt$ over one oscillation. Using the substitution (this is literally just an algebraic substitution to make things nice)
$$
\phi = \arcsin \left( \frac{\sin (\theta / 2)}{\sin(\theta_{0} / 2)} \right) 
$$
we get
$$
T = 4 \sqrt{ \frac{l}{g} } \int_{0}^{\pi / 2}  \frac{d\phi}{\sqrt{ 1 - k^{2} \sin ^{2}\phi }}.
$$

This long derivation motivates defining

##### _definition:_ elliptic integral of the first kind

The elliptic integral of the first kind is
$$
K(k) = \int_{0}^{\pi / 2}  \frac{d\phi}{\sqrt{ 1 - k^{2} \sin ^{2}\phi }} = \int \frac{dx}{\sqrt{ (1 - x^{2})(1 - k^{2} x^{2}) }} 
$$

Note that its Taylor series expansion about $k = 0$ is $K(k) = \frac{\pi}{2} + \frac{\pi}{8} k^{2} + \cdots$. That is, Galileo's formula is a first order approximation. 

But why elliptic?

### Ellipses

##### _proposition:_ arc length of an ellipse

The arc length of the ellipse
$$
\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1
$$
is given by the integral
$$
4 a \int_{0}^{\pi/2} \sqrt{ 1 - k^{2} \sin ^{2}(\phi) } \, d\phi
$$

where $k = \sqrt{ \frac{a^{2} - b^{2}}{a^{2}} }$.

###### _proof sketch:_

Consider $r(\phi) = (a \sin \phi, b \cos \phi)$ (where sine is first for cosmetic reasons). Differentiate, then integrate the norm. Use symmetry to only integrate from $0$ to $\pi / 2$ four times instead of over all of $0$ to $2 \pi$.

This integral is obviously "elliptic" —

##### _definition:_ elliptic integral of the second kind

The complete elliptic integral of the second kind is
$$
E(k) = \int_{0}^{\pi / 2} \sqrt{ 1 - k^{2} \sin ^{2}\phi } \, d\phi = \int_{0}^1 \sqrt{ \frac{1 - k^{2} x^{2}}{1 - x^{2}} }  \, dx.
$$

It turns out that we only call the elliptic integrals of the first kind so because they look like elliptic integrals of the second kind.

It's easy enough to compute $K(0)$ and $E(0)$ since they reduce to quadratics polynomials under the root. How can we compute the integral in the general case?

##### _proposition:_ computing integrals of quadratics under the root

$$
\int \frac{dx}{\sqrt{ ax^{2} + bx + c }} = \frac{1}{\sqrt{ a }} \cosh ^{-1}\left( \frac{2ax + b}{b^{2} - 4 ac} \right).
$$

###### _proof sketch:_

Substitute $x(\phi) = -\frac{b}{2a} + \frac{\sqrt{ b^{2} - 4ac }}{2a} \cosh(\sqrt{ a } \phi)$.

### Computing irrational integrals of quartics and cubics


Consider the invertible substitution
$$
\begin{aligned}
x & = \frac{X - 3(5 - k^{2})}{X - 3(5k^{2} - 1)} & & & X & = \frac{3(5k^{2} - 1)x - 3(5 - k^{2})}{x - 1} \\
&&& \iff \\
y & = \frac{6(k^{2} - 1)Y}{(X - 3(5k^{2} - 1))^{2}} & && Y & = \frac{54(k^{2} - 1) y}{(x - 1)^{2}}
\end{aligned}
$$

Then $y^{2} = (1 - x^{2})(1 - k^{2} x^{2})$ is equivalent to $Y^{2} = X^{3} + AX + B$ for some integers $A, B$. Thus,
$$
\begin{split}
K(k) & = \int_{0}^1 \frac{dx}{\sqrt{ (1 - x^{2})(1 - k^{2} x^{2}) }} \\
 & = \int_{3(5 - k^{2})}^\infty  \frac{dX}{\sqrt{ X^{3} + AX + B }} 
\end{split}
$$
That is, we reduced the elliptic integral of the first kind to an irrational cubic integral. Can we do this for all quartics? What does that say about the curves these polynomials represent?

##### _theorem:_ reducing irrational quartic integrals

Every irrational quartic integral
$$
\int \frac{dx}{\sqrt{ a_{4} x^4 + a_{3} x^3 + a_{2} x^{2} + a_{1}x + a_{0} }} 
$$
can be written as an irrational cubic integral
$$
\int \frac{dX}{\sqrt{ X^{3} + AX + B }}.
$$
Both of these can be written as incomplete elliptic integrals.
###### _proof sketch:_

Let $p(x) = a_{4} x^4 + a_{3} x^3 + a_{2} x^{2} + a_{1}x + a_{0}$. Send the four roots $e_{1}, e_{2}, e_{3}, e_{4}$ of $p$ to the four roots of $(1 - x^{2})(1 - k^{2} x^{2})$. That is, send $e_{1}, e_{2}, e_{3}, e_{4}$ to $\pm \frac{1}{k}$ and $\pm 1$.

Specifically, [[Complex Analysis --- math-135/notes/Cauchy integral formula#_theorem _ the fundamental theorem of algebra|factor]] over $\mathbb{C}$ to get
$$
p(x) = a_{4}(x - e_{1})(x - e_{2})(x - e_{3})(x - e_{4}).
$$
Assuming we have no repeated roots (the other case is not too difficult to deal with), consider the invertible substitution
$$
\begin{aligned}
x & = f'(e_{4}) \frac{1}{X - f''(e_{4})/6} + e_{4} \\
y & = f'(e_{4}) \frac{Y}{(X - f''(e_{4}) / 6)^{2}}.
\end{aligned}
$$

It's easy to see that $y^{2} = p(x)$ is equivalent to $Y^{2} = X^{3} + AX + B$ for some $A, B \in \mathbb{C}$. Thus, the integrals are equal.

Use the Möbius transform $x(u) = \frac{au + b}{cu + d}$ that sends the roots of $p$ to the roots of $(1 - x^{2})(1 - k^{2} x^{2})$ for some $k$, determined by the roots $e_{1}, e_{2}, e_{3}, e_{4}$. Then check that
$$
\frac{dx}{\sqrt{ f(x) }} = C \frac{du}{\sqrt{ (1 - u^{2})(1 - k^{2} u^{2}) }}.
$$

##### _example:_ evaluating an irrational cubic integral

Using the right formulas, we can see that
$$
\int_{2}^\infty \frac{dx}{\sqrt{ x^{3} + 4x }} = K(i) = \int_{0}^1 \frac{dx}{\sqrt{ 1- x^4 }}  
$$

But how do we actually evaluate $K(k)$?

##### _definition:_ Jacobi elliptic function

For some fixed $k \in \mathbb{C}$, $k \neq \pm 1$, the Jacobi elliptic function $w(z) = \operatorname{sn}(z)$ is the inverse of
$$
z(w) = \int_{0}^w \frac{dx}{\sqrt{ (1 - x^{2})(1 - k^{2} x^{2}) }} = F(\arcsin w, k) 
$$

Notice that since $w(z) = \sin(z)$ for $k = 0$. Since $\sin$ is periodic, we know it doesn't have a well defined inverse on all domains and $z(w)$ is dependent on the path between $0$ and $w$ and accumulates residues as you loop around $0$. However, we can quotient out by this residue! That is, we have a well-defined function
$$
z : \mathbb{C} \to \mathbb{C} / 2 \pi \mathbb{Z}
$$
by
$$
w \mapsto \int_{0}^w \frac{dx}{\sqrt{ 1 - x^{2} }} \pmod {2 \pi n}
$$

Similarly, $\operatorname{sn}$ doesn't have a well defined inverse.