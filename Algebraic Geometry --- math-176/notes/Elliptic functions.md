---
tags:
- alg-geo
- math-176/9
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

##### _theorem:_ 

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
Also, by the [[Abstract Algebra I --- math-171/notes/Group isomorphism theorems#_theorem _ the first isomorphism theorem|first group isomorphism theorem]] there is a bijection $\mathbb{C} / \Lambda_{k} \to E_{k}(\mathbb{C})$ induced by the map
$$
z \mapsto (\operatorname{sn} z, \operatorname{sn}' z)
$$where $E_{k}(\mathbb{C})$ is the set of all points $(x, y)$ in $\mathbb{C}^{2}$ on the curve $y^{2} = (1 - x^{2})(1 - k^{2} x^{2})$ (with the group operation that we'll talk about later)