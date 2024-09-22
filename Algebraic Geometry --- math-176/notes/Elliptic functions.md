---
tags:
- alg-geo
- math-176/9
- math-176/10
---

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

Similarly, $\operatorname{sn}$ doesn't have a well defined inverse, but it's doubly periodic.

##### _theorem:_ angle addition on the quartic $y^{2} = (1 - x^{2})(1 - k x^{2})$

For any fixed modulus $k \neq 0, \pm 1$ and $k' = \sqrt{ 1 - k^{2} }$. Then for
$$
\begin{split}
\omega_{1} & =  2 \int_{-1 / k}^{1 / k} \frac{dx}{\sqrt{(1 - x^{2})(1 - k^{2} x^{2})}} = 4 K(k) - 4 i K(k') \\
\omega_{2} & =  2 \int_{-1}^{1} \frac{dx}{\sqrt{(1 - x^{2})(1 - k^{2} x^{2})}}  = 4 K(k)\\
\end{split}
$$
we have that the Jacobi elliptic function is doubly periodic with
$$
w(z + \omega) = w(z)
$$
for any period $\omega$ in the lattice
$$
\Lambda_{k} = \{ \omega = m \omega_{1} + n \omega_{2} \mid m, n \in \mathbb{Z} \}.
$$
Also, by the [[Abstract Algebra I --- math-171/notes/Group isomorphism theorems#_theorem _ the first isomorphism theorem|first group isomorphism theorem]] there is a [[Abstract Algebra I --- math-171/notes/Group isomorphisms#_definition _ group isomorphism, isomorphic|isomorphism]]
$\mathbb{C} / \Lambda_{k} \to E_{k}(\mathbb{C})$ induced by the map
$$
z \mapsto (\operatorname{sn} z, \operatorname{sn}' z)
$$where $E_{k}(\mathbb{C})$ is the set of all points $(x, y)$ in $\mathbb{C}^{2}$ on the curve $y^{2} = (1 - x^{2})(1 - k^{2} x^{2})$ with the obvious group operation
$$
(\operatorname{sn}(z_{1}), \operatorname{sn}'(z_{1})) \oplus (\operatorname{sn}(z_{2}), \operatorname{sn}'(z_{2})) = (\operatorname{sn}(z_{1} + z_{2}), \operatorname{sn'(z_{1} + z_{2})}).
$$

###### _proof sketch:_

The periodicity follows from some clever calculus substitutions to convert this into the form of a [[Algebraic Geometry --- math-176/notes/Elliptic integrals|complete elliptic integral]].

Note that the integral
$$
z = \int_{0}^w  \frac{dx}{\sqrt{ (1 - x^{2})(1 - k^{2} x^{2}) }} 
$$
gives us
$$
\frac{dz}{dw} = \frac{1}{\sqrt{ (1 - w^{2}) (1 - k^{2} w^{2}) }}
$$
and thus,
$$
\left( \frac{dw}{dz} \right)^{2} = (1 - w^{2})(1 - k^{2} w^{2}).
$$

That is, $(w, w')$ is a point on the quartic. Also notice that every point on the quartic corresponds to some distinct $w$ by the size of the period of $\operatorname{sn}$, thus, every point can be described by $(w, w')$.

Now if [[Algebraic Geometry --- math-176/notes/Elliptic integrals#_theorem _ reducing irrational quartic integrals|quartics can be reduced to cubics]], can this idea be used to say something about elliptic curves $y^{2} = x^{2} + ax + b$? Yes!

The same transformation that converts quartic to cubics, acts as a group homomorphism.