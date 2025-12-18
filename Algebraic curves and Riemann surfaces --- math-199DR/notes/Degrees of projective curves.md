---
tags:
- math-199DR/24
- alg-geo
- cx-geo
---

The degree of a projective curve is an invariant that roughly describes it's intersection data with hyperplanes, and thus, if it is defined by the zero locus of a single polynomials, the degree of that polynomial.

We won't say what a projective curve is, but we will state some properties of it without proof.

##### _proposition:_

##### _proposition:_

To capture the hyperplane intersection data, we introduce the notion of a hyperplane divisor.

##### _definition:_ hyperplane divisor

Given a smooth projective curve $X$, and $H \subseteq \mathbb{C} \mathbb{P}^n$ a hyperplane (the vanishing set of a homogeneous linear polynomial $g$), the hyperplane divisor of $H$ with respect to $X$ is the [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Divisors#_definition _ divisor|divisor]] given by
$$
\operatorname{div} H(p) = \begin{cases}
\operatorname{ord}_{p} g / \ell & p \in H \cap X \\
0  & p \not\in X
\end{cases}
$$
where $\ell$ is a linear polynomial that does not vanish at $p$.

We claim that this is well defined, since for different $\ell_{1}, \ell_{2}$, we have $\operatorname{ord}_{p}(g / \ell_{1}) = \operatorname{ord}_{p}(g / \ell_{2}) + \operatorname{ord}_{p} (\ell_{2}/ \ell_{1})$ but since the $\ell_{i}$ are linear and non-vanishing at $p$, the order on the right vanishes.

Further, we claim that any, two hyperplane divisors on the same surface are [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Linear equivalence of divisors#_definition _ linear equivalence|linearly equivalent]], so we can unambiguously define the degree of a curve as the degree of a hyperplane divisor on it.

##### _proposition:_ hyperplane divisors on a curve are linearly equivalent

For any two hyperplanes $H_{1}, H_{2}$ in $\mathbb{C} \mathbb{P}^n$, their hyperplane divisors on the smooth projective curve $X$ are linearly equivalent.

###### _proof sketch:_

Given $p \in H_{1} \cap X$.

##### _definition:_ degree of a projective curve

The degree of a smooth projective curve $X$ embedded in $\mathbb{C} \mathbb{P}^n$ is $\deg (\operatorname{div} H)$ for $H$ a hyperplane in $\mathbb{C} \mathbb{P}^n$.

##### _example:_ the degree of the Segre embedding

Consider $X = \{ (x ^{2} : xy : y^{2}) \mid (x : y) \in \mathbb{C} \mathbb{P}^1 \}$ a smooth projective curve in $\mathbb{C} \mathbb{P} ^2$. Then the hyperplanes $H_{1} = \{ (x_{0} : x_{1} : x_{2}) \mid x_{0} = 0 \}$ and $H_{2} = \{ (x_{0} : x_{1} : x_{2}) \mid x_{1} = 0 \}$ have different divisors that are in fact linearly equivalent. We can see that the first has $H_{1}(0 : 0 : 1) = 2$ and is zero everywhere else, while the second has $H_{2}(1 : 0 : 0) = H_{2}(0 : 0 : 1) = 1$.

Thus, the Segre embedding has degree $2$.

