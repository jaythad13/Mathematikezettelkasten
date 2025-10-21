---
tags:
- math-177/12
- math-177/13
- lin-alg
- galois
- alg
---

When we have a field extension $\mathbb{K} / \mathbb{F}$, we want to extend the absolute value on $\mathbb{F}$ to an absolute value on $\mathbb{K}$. Since a field norm on $\mathbb{K}$ that extends a norm on $\mathbb{F}$ is just a $\mathbb{F}$-vector space norm on $\mathbb{K}$, we can just study vector space norms over $\mathbb{F}$. Uniqueness of the extension then follows from some results on norms on vector spaces.

##### _lemma:_ characterising equivalent norms on a vector space

Suppose $V$ is a vector space over a field $\mathbb{F}$ with absolute value. Then two norms are equivalent if and only if there exists $c_{1}, c_{2} \in \mathbb{R}$ such that
$$
\begin{align}
\lVert v \rVert_{1}  &< c_{2} \lVert v \rVert _{2} \\
\lVert v \rVert _{2} & < c_{1} \lVert v \rVert _{1}.
\end{align}
$$
---

##### _theorem:_ all norms on a vector space are equivalent

All norms on a finite-dimensional vector space $V$ over a (metrically) [[Analysis --- math-131/notes/Cauchy sequences and completeness#_definition _ completeness|complete]] field $\mathbb{F}$ are equivalent.

---

##### _theorem:_ characterising extensions of a norm

If $\mathbb{K}$ is a finite degree extension of $\mathbb{F}$ with non-archimedean absolute value, then there is at most one extension of the absolute value to $\mathbb{K}$.

###### _proof:_

Suppose there are two norms on $\mathbb{K}$ and suppose there is some $v \in \mathbb{K}$ for which (without loss of generality) $\lVert v \rVert_{1} > \lVert v \rVert_{2}$. Since they are equivalent, we have $c_{1}, c_{2} \in \mathbb{R}$ such that $\lVert v \rVert_{1} < c_{2} \lVert v \rVert_{2}$ and $\lVert v \rVert_{2} < c_{1} \lVert v \rVert_{1}$. Then $\lVert v^n \rVert_{1} < c_{2} \lVert v^n \rVert_{2}$ for all $n$. Choosing $n > \ln(c_{2}) / \ln (\lVert v \rVert_{1} / \lVert v \rVert_{2})$ gives a contradiction.

---

Note that here we have proved that the norms are *the same*, not just equivalent. Now we construct this unique norm. Note that the extension of the norm shouldn't depend on the precise root, but just its minimal polynomial — [[p-adic numbers --- math-177/notes/Algebraic field extensions#_corollary _ minimal polynomials give minimal extensions|we showed ]]that the corresponding field extensions are isomorphic.

##### _proposition:_ extension of norms

If $\mathbb{K} / \mathbb{F}$ is an algebraic field extension and $\alpha \in \mathbb{K}$ is algebraic over $\mathbb{F}$ (a field with non-archimedean norm) with minimal polynomial $p_{\alpha}(x) = a_{0} + a_{1} x + \dots + x^n$, then the unique extension of the norm to $\mathbb{K}$ has $\lvert \alpha \rvert = \lvert a_{0} \rvert^{1 / n}$.

###### _proof sketch:_

Work in the [[p-adic numbers --- math-177/notes/Algebraic field extensions#_definition _ splitting field|splitting field]] of $p_{\alpha}$. The extension of the norm to $\mathbb{K}$ should agree with the extension to the splitting field since they are both contained in the algebraic closure of $\mathbb{F}$.

Let all the roots be $\alpha_{i}$. They should all have the same norm, $\lvert \alpha \rvert$. But then since $a_{0} = (-1)^n \prod_{i = 1}^n \alpha_{i}$, we have $\lvert a_{0} \rvert^{1 / n} = \lvert \alpha \rvert$.

---

An alternate equivalent definition (showing equivalence is non-trivial) is the following. This definition makes showing mutliplicativity and non-archimedeanness easier.

##### _definition:_ extension of norms

Suppose $\mathbb{K}$ is an extension of $\mathbb{Q}_{p}$ of degree $n$. For some non-zero $\alpha \in \mathbb{K}$, let $L_{\alpha} : \mathbb{K} \to \mathbb{K}$ be the $\mathbb{Q}_{p}$-linear map by $a \mapsto \alpha a$. Then define
$$
\lvert \alpha \rvert _{p} = \lvert \det L_{\alpha} \rvert _{p}^{1 / n}.
$$

---

##### _corollary:_ classifying the values of the norm

Suppose $\deg \mathbb{K} / \mathbb{Q}_{p} = n$. Then $\{ \log_{p} (\lvert \alpha \rvert_{p}) \mid \alpha \in \mathbb{K}^\times \}$ is an additive subgroup of $\frac{1}{n} \mathbb{Z}$.

---

Note that this means that an algebraic number over $\mathbb{Q}_{p}$ sitting in a field of degree $n$ cannot have monic irreducible polynomial of degree $d \nmid n$.


##### _example:_ extension of norms by determinant

Consider the quadratic extension $\mathbb{Q}_{5}(\sqrt{ 2 }) / \mathbb{Q}_{p}$ and consider $\alpha = 1 - \sqrt{ 2 }$. Then multiplication by $\alpha$ has matrix $\begin{pmatrix} 1 & -2 \\ -1 & 1 \end{pmatrix}$ (with respect to basis $1, \sqrt{ 2 }$). This has determinant $3$, and so $\lvert \alpha \rvert_{p} = \lvert 3 \rvert_{p}^{1 / 2} = \sqrt{ 1 } = 1$.
