---
tags:
- math-177/12
- lin-alg
- galois
- alg
---

When we have a field extension $\mathbb{K} / \mathbb{F}$, we want to extend the absolute value on $\mathbb{F}$ to an absolute value on $\mathbb{K}$. Since a field norm on $\mathbb{K}$ that extends a norm on $\mathbb{F}$ is just a $\mathbb{F}$-vector space norm on $\mathbb{K}$, we can just study vector space norms over $\mathbb{F}$. Uniqueness of the extension then follows from some results on norms on vector spaces.

##### _lemma:_ characterising equivalent norms on a vector space

Suppose $V$ is a vector space over a field $\mathbb{F}$ with non-archimedean absolute value. Then two norms are equivalent if and only if there exists $c_{1}, c_{2} \in \mathbb{R}$ such that
$$
\begin{align}
\lVert v \rVert_{1}  &< c_{2} \lVert v \rVert _{2} \\
\lVert v \rVert _{2} & < c_{1} \lVert v \rVert _{1}.
\end{align}
$$
---

##### _theorem:_ all norms on a vector space are equivalent

All norms on a vector space $V$ over a field $\mathbb{F}$ with non-archimedean absolute value are equivalent.

---

These results still hold when $\mathbb{F}$ is archimedean if $V$ is finite-dimensional.

##### _theorem:_ characterising extensions of a norm

If $\mathbb{K}$ is a finite degree extension of $\mathbb{F}$ with non-archimedean absolute value, then there is at most one extension of the absolute value to $\mathbb{K}$.

###### _proof:_

Suppose there are two norms on $\mathbb{K}$ and suppose there is some $v \in \mathbb{K}$ for which $\lVert v \rVert_{1} > \lVert v \rVert_{2}$. Since they are equivalent, we have $c_{1}, c_{2} \in \mathbb{R}$ such that $\lVert v \rVert_{1} < c_{2} \lVert v \rVert_{2}$ and $\lVert v \rVert_{2} < c_{1} \lVert v \rVert_{1}$. Then $\lVert v^n \rVert_{1} < c_{2} \lVert v^n \rVert_{2}$ for all $n$. Choosing $n > \ln(c_{2}) / \ln (\lVert v \rVert_{1} / \lVert v \rVert_{2})$ gives a contradiction.

---

Note that here we have proved that the norms are *the same*, not just equivalent. Now we construct this unique norm.

##### _proposition:_ extension of norms

If $\mathbb{K} / \mathbb{F}$ is a field extension and $\alpha \in \mathbb{K}$ is algebraic over $\mathbb{F}$ (a field with non-archimedean norm) with minimal polynomial $p_{\alpha}(x) = a_{0} + a_{1} x + \dots + x^n$, then the unique extension of the norm to $\mathbb{K}$ has $\lvert \alpha \rvert = \lvert a_{0} \rvert^{1 / n}$.

---
