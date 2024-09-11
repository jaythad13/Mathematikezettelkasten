---
tags:
- math-176/6
- math-176/7
- alg-geo
---

### Pendulums

When exploring different types of Diophantine equations we saw two interesting propositions — that [[Algebraic Geometry --- math-176/notes/Diophantine equations#_proposition _ Heron triangles are rational points on a quartic|Heron triangles correspond to points on the quartic]] $y^{2} = (1 - x^{2})(1 - k^{2} x^{2})$, and that [[Algebraic Geometry --- math-176/notes/Diophantine equations#Congruent numbers|numbers are congruent if and only if the curve]] $y^{2} = x^{3} - A^{2} x$ has a rational point.

In fact, these curves have a mysterious relationship with pendulums! We've all seen that Galileo showed the period of a simple pendulum of length $l$ to be approximately $2\pi \sqrt{ l / g }$ for small angles.

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

### Elliptic integrals

This long derivation motivates defining

##### _definition:_ elliptic integral of the first kind

The elliptic integral of the first kind is
$$
K(k) = \int_{0}^{\pi / 2}  \frac{d\phi}{\sqrt{ 1 - k^{2} \sin ^{2}\phi }} = \int \frac{dx}{\sqrt{ (1 - x^{2})(1 - k^{2} x^{2}) }} 
$$

Note that its Taylor series expansion about $k = 0$ is $K(k) = \frac{\pi}{2} + \frac{\pi}{8} k^{2} + \cdots$. That is, Galileo's formula is a first order approximation. 

But why elliptic?

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