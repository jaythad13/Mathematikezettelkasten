---
tags:
- math-199DR/17
- math-199DR/19
- cx-geo
- alg-geo
---

Let $X, Y$ be compact, connected Riemann surfaces.

Linear equivalence gives us a way to make our large space of all [[Introduction to Riemann Surfaces --- math-199DR/notes/Divisors#_definition _ divisor|divisors]] on a compact Riemann surface $X$ into a smaller one. This generalises the quotient equivalence relation that allows us to consider $\operatorname{Jac} X = \operatorname{Div}_{0}X / \operatorname{PDiv} X$.

##### _definition:_ linear equivalence

Two divisors on $X$ are linearly equivalent if their difference is [[Introduction to Riemann Surfaces --- math-199DR/notes/Divisors#_definition _ principal divisor|principal]].

The equivalence classes of canonical divisors under linear equivalence are called canonical classes.

The name linear equivalence comes from the idea of thinking of meromorphic functions $f$ as holomorphisms $\pi_{f}$ to the complex projective line $\mathbb{C} \mathbb{P}^1$ and then writing $\operatorname{div} f = Z - P$ where $Z = \pi_{f}^*0$ and $P = \pi_{f}^*\infty$ as the divisors of zeroes and poles respectively. Linear equivalence is then moving along the line from $Z$ to $P$ by considering $\pi^*(p)$ as $p \in \mathbb{C}\mathbb{P}^1$ varies from $0$ to $\infty$.

##### _example:_ linear equivalence on the Riemann sphere

[[Introduction to Riemann Surfaces --- math-199DR/notes/Divisors#_example _ all degree $0$ divisors on the Riemann sphere are principal|Recall]] that any degree zero divisor on the Riemann sphere is principal. It follows then that $D_{1}, D_{2} \in \operatorname{Div} \mathbb{C}_{\infty}$ are linearly equivalent exactly when $\operatorname{deg} D_{1} = \deg D_{2}$.

Linear equivalence is a very nicely behaved equivalence relation.

##### _proposition:_ linear equivalence under pullback

If $D_{1}, D_{2} \in \operatorname{Div} Y$ are linearly equivalent and $\pi : X \to Y$ is a [[Introduction to Riemann Surfaces --- math-199DR/notes/Holomorphisms of Riemann surfaces#_definition _ holomorphism|holomorphism]], then the [[Introduction to Riemann Surfaces --- math-199DR/notes/Divisors#_definition _ pullback of a divisor|pullbacks]] $\pi^* D_{1}$ and $\pi^* D_{2}$ are linearly equivalent on $X$.

###### _proof:_

Suppose $D_{1} - D_{2} = \operatorname{div} f$ for some meromorphic function $f$ on $Y$. Then since [[Introduction to Riemann Surfaces --- math-199DR/notes/Divisors#_proposition _ algebraic properties of pullback of divisors|the pullback is a homomorphism]], $\pi^* D_{1} - \pi^* D_{2} = \pi^* (\operatorname{div} f)$. Then since pullback commutes with $\operatorname{div}$, we have
$$
\pi^* D_{1} - \pi^* D_{2} = \operatorname{div} \pi^* f
$$
and thus, the pullbacks are linearly equivalent.

All of this means that we have a map of [[Abstract Algebra I --- math-171/notes/Exact sequences#_example _ short exact sequence|short exact sequences]]!

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

Suppose $D = \operatorname{div} f$ is principal on $X$. Let $\pi^* f$ be the pullback to a $\Lambda$-periodic meromorphic function on the complex plane. Certainly $D$ has degree $0$ [[Introduction to Riemann Surfaces --- math-199DR/notes/Topological properties of holomorphisms#_theorem _ the sum of orders of a meromorphic function|since]] $X$ is compact. We're left to show $\alpha(D) = 0$. We will do so by projecting to a parallelogram $\gamma_{p}$ in the plane with vertices $p, p + 1, p + \tau, p + 1 + \tau$ (with $\tau$ such that $\Lambda  = \mathbb{Z} + \tau \mathbb{Z}$) which bounds a region $\Sigma_{p}$

Notice that by the [[Complex Analysis --- math-135/notes/Meromorphic functions and singularities#_theorem _ the residue formula|residue formula]] (similar to the [[Complex Analysis --- math-135/notes/The argument principle and winding number#_theorem _ the argument principle|argument principle]])
$$
\alpha(D) = \sum_{z \in \Sigma_{p}} (\operatorname{ord}_{z} \pi^*f) z = \frac{1}{2 \pi i} \int_{\gamma_{p}} z \frac{(\pi^*f)'(z)}{(\pi^*f)(z)} \, dz.
$$
However, the integral on right is in $\Lambda$. We can see this by rewriting the integral using the $\Lambda$-periodicity of $\pi^* f$ to relate the integral on parallel sides of $\gamma_{p}$ —
$$
\frac{1}{2 \pi i} \int_{\gamma_{p}} z \frac{(\pi^*f)'(z)}{(\pi^*f)(z)} \, dz = \frac{1}{2 \pi i} \int_{\gamma_{p}} (1 + \tau) \frac{(\pi^*f)'(z)}{(\pi^*f)(z)} \, dz = (1 + \tau) \sum_{z \in \Sigma_{p}} \operatorname{ord}_{z} \pi^*f.
$$
The last equality follows from the argument principle. Note that $(1 + \tau) n \in \Lambda$ for any integer $\Lambda$. Thus
$$
\alpha(D) \equiv 0
$$
in $\mathbb{C} / \Lambda$.

Suppose $\operatorname{deg} D = 0$ and $\alpha(D) = 0$. Then we pair the points that cancel for degree $0$ as $p_{i} - q_{i}$, lift them to $z_{i} - w_{i}$ in $\mathbb{C} / \Lambda$ so that $\sum z_{i} - w_{i} = 0$ and finally, lift them again to $\mathbb{C}$ so that $\sum z_{i} - w_{i} = 0$ in $\mathbb{C}$. We can use the [[Introduction to Riemann Surfaces --- math-199DR/notes/Functions on Riemann surfaces#_example _ meromorphic functions on the torus|theta function construction]] to get a meromorphic function on $X$ with the prescribed zeroes and poles.

In fact, this generalises! In higher dimensions this is the Abel-Jacobi map that embeds a genus $g$ curve into $\mathbb{C}^g / \Lambda$.

This has some notable consequences — first, and obviously, $D_{1} \sim D_{2}$ if and only if $\operatorname{deg} D_{1} = \operatorname{deg} D_{2}$ and $\alpha(D_{1}) = \alpha(D_{2})$. However, it also gives us an isomorphism between any divisor of positive degree and a specific effective divisor. Moreover, it allows the freedom to exclude a specific point.

##### _corollary:_ a positive degree divisor is equivalent to a positive divisor

For any $D \in \operatorname{Div} \mathbb{C} / \Lambda$ of positive degree and $p \in X$ there is a positive divisor $E \geq 0$ such that $D \sim E$ and if $\deg D > 1$, $E$ can be chosen so that $E(p) = 0$.

###### _proof:_

Write $d = \deg D$.

If $d = 1$, then $D \sim \alpha(D)$ where $\alpha(D)$ is the single point divisor at $\alpha$.

Suppose $d > 1$. We can choose $q \neq p$ and consider the divisor $F = D - (d - 1) \cdot q$. This is a divisor of degree $1$. Thus, $F \sim \alpha(F)$. We can choose $q \neq p$ so that $\alpha(F) \neq p$. Thus, we have $D - (d - 1) \cdot q \sim \alpha(F)$ from which it follows that $D \sim (d - 1) \cdot q + \alpha(F)$. $E = (d - 1) \cdot q + \alpha(F)$ is the desired positive divisor.