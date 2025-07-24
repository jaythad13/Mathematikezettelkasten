---
tags:
- math-135/10
- anal
- complex
---

We can get something like a power series for functions even when they're only holomorphic on an annulus! This is another way to think about [[Complex analysis --- math-135/notes/Meromorphic functions and singularities|meromorphic functions]].

##### _theorem:_ Laurent expansion

If $f$ is holomorphic on the annulus $A = \{ z \mid r < \lvert z - z_{0} \rvert < R \}$ centred at $z_{0}$. Then for any $z \in A$,
$$
f(z) = \sum_{n = 0}^\infty a_{n} (z - z_{0})^n + \sum_{n = 1}^\infty \frac{a_{-n}}{(z - z_{0})^n}
$$
where
$$
a_{n} = \frac{1}{2 \pi i} \int_{C_{\rho}(z_{0})} \frac{f(\zeta)}{(\zeta - z_{0})^{n + 1}} \, d\zeta 
$$
where $\rho$ is any radius $r < \rho < R$.

###### _proof:_

Fix $z \in A$, and let $\rho = \lvert z - z_{0} \rvert$. Also choose $\rho_{1}, \rho_{2}$ such that $r < \rho_{2} < \rho < \rho_{1} < R$. Using a keyhole contour with circles $C_{\rho_{1}}$ and $C_{\rho_{2}}$ centred at $z_{0}$, with radii $\rho_{1}$ and $\rho_{2}$ respectively, we can use the Cauchy integral formula to see
$$
f(z) = \frac{1}{2 \pi i} \int_{C_{\rho_{1}}(z_{0})} \frac{f(\zeta)}{\zeta - z} \, d\zeta - \frac{1}{2 \pi i} \int_{C_{\rho_{2}}(z_{0})} \frac{f(\zeta)}{\zeta - z} \, dz  
$$
Using the same trick we used [[Complex analysis --- math-135/notes/Cauchy integral formula#_corollary _ the derivative form (holomorphic functions are smooth and analytic)|to get a power series from the Cauchy integral formula]], we can write the first integral as a power series —
$$
\frac{1}{2 \pi i} \int_{C_{\rho_{1}}} \frac{f(\zeta)}{\zeta - z} \, d\zeta = \sum_{n = 0}^\infty (z - z_{0})^n \frac{1}{2 \pi i} \int_{C_{\rho_{1}}} \frac{f(\zeta)}{(\zeta - z_{0})^{n + 1}} \, d\zeta 
$$

However, we can't do the same thing with the second integral —
$$
\begin{split}
\frac{1}{2 \pi i} \int_{C_{\rho_{2}}} \frac{f(\zeta)}{\zeta - z} \, dz & = \frac{1}{2 \pi i} \int_{C_{\rho_{2}}} \frac{f(z)}{\zeta - z_{0} - (z - z_{0})} \, d\zeta \\
 & = \frac{1}{2 \pi i} \int_{C_{\rho_{2}}} \frac{f(\zeta)}{\zeta - z_{0}}\frac{1}{1 - \frac{z - z_{0}}{\zeta - z_{0}}} \, d\zeta  \\
\end{split}
$$
From here we can't actually use the geometric series trick because we're integrating on $C_{\rho_{2}}$ where $\zeta - z_{0}$ is actually less than $z - z_{0}$, since $z$ is on a circle of radius $\rho > \rho_{2}$ centred at $z_{0}$. Instead, we use the following trick to flip the 
$$
\frac{1}{\zeta - z_{0}} \frac{1}{1 - \frac{z - z_{0}}{\zeta - z_{0}}} = - \frac{1}{z - z_{0}} \frac{1}{1 - \frac{\zeta - z_{0}}{z - z_{0}}}.
$$

Then using geometric series and uniform convergence to swap sums and integrals, we get
$$
\begin{split}
\frac{1}{2 \pi i} \int_{C_{\rho_{2}}} \frac{f(\zeta)}{\zeta - z_{0}}\frac{1}{1 - \frac{z - z_{0}}{\zeta - z_{0}}} \, d\zeta & = \frac{1}{2 \pi i} \int_{C_{\rho_{2}}} \frac{- f(\zeta)}{z - z_{0}} \frac{1}{1 - \frac{\zeta - z_{0}}{z - z_{0}}} \, d\zeta \\
 & = \frac{1}{2 \pi i} \int_{C_{2r_{2}}} \frac{-f(\zeta)}{z  - z_{0}} \sum_{n = 0}^\infty \left( \frac{\zeta - z_{0}}{z - z_{0}} \right)^n \, d\zeta \\
 & = - \sum_{n = 0}^\infty (z - z_{0})^{-(n + 1)} \frac{1}{2\pi i} \int_{C_{\rho_{2}}} \frac{f(\zeta)}{(\zeta - z_{0})^{- n}} \, d\zeta \\
 & = - \sum_{n = 1}^\infty (z - z_{0})^{-n} \frac{1}{2 \pi i} \int_{C_{\rho_{2}}} \frac{f(\zeta)}{(\zeta - z_{0})^{-n + 1}} \, d\zeta \\
 & = - \sum_{n = - \infty}^{-1} (z - z_{0})^n \frac{1}{2 \pi i} \int_{C_{\rho_{2}}} \frac{f(\zeta)}{(\zeta - z_{0})^{n + 1}} \, d\zeta.
\end{split}
$$

Thus,
$$
f(z) = \frac{1}{2 \pi i} \int_{C_{\rho_{1}}(z_{0})} \frac{f(\zeta)}{\zeta - z} \, d\zeta - \frac{1}{2 \pi i} \int_{C_{\rho_{2}}(z_{0})} \frac{f(\zeta)}{\zeta - z} \, dz = 
$$

Once we move the $z$ out of the integrals, we can just deform $C_{\rho_{1}}$ and $C_{\rho_{2}}$ to any circle in the annulus by [[Complex analysis --- math-135/notes/Homotopy and simply connected domains#_theorem _ deformation theorem|homotopy]].

Note that these coefficients are unique, since
$$
a_{n} = \frac{1}{2 \pi i} \int_{C} (z - z_{0})^{1 - n} \sum_{n = - \infty}^\infty a_{n} (z - z_{0})^n \, dz = \frac{1}{2 \pi i} \int_{C} (z - z_{0})^{1 - n}f(z) \, dz 
$$

##### _example:_ a very contrived application

If you want to evaluate the integral of $\frac{f(z)}{z^{-n + 1}}$ over a circle, it's just the $n$th term of the unique Laurent expansion of $f$. Often we get the Laurent expansion by some sort of chain rule shenanigan. For example,
$$
e^{1/z} = \sum_{n = 0}^\infty \frac{1}{n!} \frac{1}{z^n}
$$

In particular, if $f$ has an isolated singularity at one point in a disc, $f$ has a Laurent expansion at every point on the disc.

##### _theorem:_ classifying singularities

Suppose $f : D \to \mathbb{C}$ is holomorphic on some disc $D$ except at an isolated singularity at $z_{0} \in D$, and
$$
f(z) = \sum_{n = - \infty}^\infty a_{n} (z - z_{0})^n
$$
1) If $a_{n} = 0$ for all $n < 0$, then $z_{0}$ is a [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ removable singularity|removable singularity]]
2) If $a_{-N} \neq 0$ but $a_{n} = 0$ for all $n < -N$, $z_{0}$ is a [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ pole|pole]] of order $N$
3) If $a_{n} \neq 0$ for infinitely many negative integers, $z_{0}$ is an [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_definition _ essential singularity|essential singularity]].

###### _proof:_

The first follows since if there are no negative indexed coefficients, $f$ has a power series that converges on the disk, including at $z_{0}$.

The second case follows by the same thing as

We get a useful extension of [[Complex analysis --- math-135/notes/Cauchy-Goursat theorem#_corollary _ Cauchy's theorem|Cauchy's theorem]]:

##### _theorem:_

If $f$ is holomorphic on a disc $D \setminus \{ \zeta_{1}, \dots, \zeta_{k} \}$. If for all $j$, $\lim_{ z \to \zeta_{j} } (z - \zeta_{j})  f(z) = 0$ for any closed curve in $D$, then
$$
\int_{\gamma} f(z) \, dz = 0
$$
for any closed curve $\gamma$ in $D$.