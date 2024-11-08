---
tags:
- math-176/29
- math-176/30
- math-176/31
- alg-geo
---

Using the [[Algebraic Geometry --- math-176/notes/Non-singular projective varieties#_definition _ affine variety|ring-theoretic definition of affine varieties]], we can get a sensible set of functions on an affine variety. Grothendieck's philosophy tells us that the best way to understand an affine variety $X$ is to understand $\mathcal{O}$, the ring of functions on it. Then we can replace points $p \in X$ with ideals in the [[Algebraic Geometry --- math-176/notes/Spectra#_definition _ $ operatorname{mSpec} R$, the max spectrum|max spectrum]] and ultimately, just the [[Algebraic Geometry --- math-176/notes/Spectra#_definition _ $ operatorname{Spec} R$, spectrum|spectrum]] of $\mathcal{O}$.

##### _proposition, definition:_ functions on a variety

Suppose $I = (f_{1}, \dots, f_{n})$ is a prime ideal of $R$. Denote $\mathcal{O} = R / I$. Then each $\overline{f} \in \mathcal{O}$ defines a function
$$
\begin{split}
\overline{f} & : Z(I) \to \mathbb{A}(F) \\
 & : p \mapsto f(p)
\end{split} 
$$

###### _proof:_

We just need to show that $\overline{f}$ is a well-defined function. That is, if $\overline{f} = \overline{g}$ then $\overline{f}(p) = \overline{g}(p)$.

Note that if $\overline{f} = \overline{g}$, then $f - g \in I$. Thus, $f(p) = g(p) + i(p)$ where $i \in I$. But $p \in Z(I)$ so $f(p) = g(p)$, and thus, $\overline{f}(p) = \overline{g}(p)$.

