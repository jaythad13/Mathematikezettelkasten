---
tags:
- math-199DR/17
- cx-geo
- alg-geo
---

Linear equivalence gives us a way to make our large space of all [[Introduction to Riemann Surfaces --- math-199DR/notes/Divisors#_definition _ divisor|divisors]] on a compact Riemann surface $X$ into a smaller one. This generalises the quotient equivalence relation that allows us to consider $\operatorname{Jac} X = \operatorname{Div}_{0}X / \operatorname{PDiv} X$.

##### _definition:_ linear equivalence

Two divisors on $X$ are linearly equivalent if their difference is [[Introduction to Riemann Surfaces --- math-199DR/notes/Divisors#_definition _ principal divisor|principal]].

The equivalence classes of canonical divisors under linear equivalence are called canonical classes.

##### _example:_ linear equivalence on the Riemann sphere

[[Introduction to Riemann Surfaces --- math-199DR/notes/Divisors#_example _ all degree $0$ divisors on the Riemann sphere are principal|Recall]] that any degree zero divisor on the Riemann sphere is principal. It follows then that $D_{1}, D_{2} \in \operatorname{Div} \mathbb{C}_{\infty}$ are linearly equivalent exactly when $\operatorname{deg} D_{1} = \deg D_{2}$.

Linear equivalence is a very nicely behaved equivalence relation — 

##### _proposition:_ linear equivalence under pullback



```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
	1 \ar[r, hook] & \mathcal{O}_{Y}^*(Y) \ar[r, hook] \ar[d, "\pi^*"] & \mathcal{M}^*_{Y}(Y) \ar[r, "f \mapsto \mathrm{div} f"] \ar[d, "\pi^*"] & \mathrm{Div}_{0} Y \ar[r, two heads] \ar[d, "\pi^*"] & \mathrm{Jac} Y \ar[r, two heads] \ar[d, "\pi^*"] & 0 \\
	1 \ar[r, hook] & \mathcal{O}_{X}^*(X) \ar[r, hook] & \mathcal{M}^*_{X}(X) \ar[r, "f \mapsto \mathrm{div} f"] & \mathrm{Div}_{0} X \ar[r, two heads] & \mathrm{Jac} X \ar[r, two heads] & 0.
	\end{tikzcd}
\end{document}
```

### Applications to elliptic curves

Linear equivalence can help us understand Riemann surfaces of genus $1$. In general, these are $X = \mathbb{C} / \Lambda$ for some lattice $\Lambda = \mathbb{Z} + \tau \mathbb{Z}$ where $\tau$ is in the upper half-plane. Consider the homomorphism $\alpha : \operatorname{Div} X \to X$ by $D \mapsto \sum_{z \in X} D(z) z$. We claim that this in fact gives an isomorphism $\operatorname{Jac} X \cong \mathbb{C} / \Lambda$ as groups.

##### _theorem:_ Abel's theorem for elliptic curves

The Jacobian of an elliptic curve is isomorphic to its group structure as $\mathbb{C} / \Lambda$.

###### _proof:_

We will show that $D$ is principal on $X$ if and only if $\operatorname{deg} D = 0$ and $\alpha(D) = 0$. Then the restriction of $\alpha$ to $\operatorname{Div}_{0} X$ is surjective onto $\mathbb{C} / \Lambda$ and has kernel $\operatorname{PDiv} X$. $\mathbb{C} / \Lambda \cong \operatorname{Jac}  X = \operatorname{Div}_{0} X / \operatorname{PDiv} X$.

Suppose $D = \operatorname{div} f$ is principal on $X$. Certainly $D$ has degree $0$ since $X$ is compact. We want to show that $\alpha(D) = 0$. Notice that by the residue theorem
$$
\alpha(D) = \sum_{i = 1}^n
$$

Suppose $\operatorname{deg} D = 0$ and $\alpha(D) = 0$. Then we pair the points that cancel for degree $0$ as $p_{i} - q_{i}$, lift them to $z_{i} - w_{i}$ in $\mathbb{C} / \Lambda$ so that $\sum z_{i} - w_{i} = 0$ and finally, lift them again to $\mathbb{C}$ so that $\sum z_{i} - w_{i} = 0$ in $\mathbb{C}$. We can use the [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_example _ meromorphic functions on the torus|theta function construction]] to get a meromorphic function on $X$ with the prescribed zeroes and poles. 

In fact, this generalises! In higher dimensions this is the Abel-Jacobi map that embeds a genus $g$ curve into $\mathbb{C}^g / \Lambda$.

