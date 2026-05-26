---
tags:
- lin-alg
- alg
- pcmi-2021/2
---

Let $\mathbb{F}$ be a field of characteristic not zero. All quadratic spaces are over $\mathbb{F}$.

In the study of isotropic quadratic spaces, most important one is the hyperbolic plane. They are the building blocks of isotropic forms.

##### _definition:_ the hyperbolic plane

The **hyperbolic plane** $H$ is the quadratic space $\left< 1, -1 \right>$.

Equivalently, $H$ is a quadratic space with a basis of two [[Quadratic forms and K-theory --- pcmi-2021/notes/Quadratic forms#_definition _ isotropic, isotropic vector, represents|isotropic vectors]] $e_{1}, e_{2}$ that have non-zero $b = \beta_{H}(e_{1}, e_{2})$. The diagonalisation is given by $f_{1} = e_{1} + e_{2} / 2b, f_{2} = e_{1} - e_{2} / 2b$.

---

##### _proposition:_ all isotropic spaces contain the hyperbolic plane

Suppose $V, q$ is an [[Quadratic forms and K-theory --- pcmi-2021/notes/Quadratic forms#_definition _ isotropic, represents|isotropic]] quadratic space. Then $V \cong U \oplus H$ for some unique $U$.

###### _proof:_

Since $V$ is isotropic, there is some $v \in V$ with $q(v) = 0$. Let $w \in V$ have $\beta(v, w) \neq 0$. Such a $w$ exists by [[Quadratic forms and K-theory --- pcmi-2021/notes/Quadratic forms#_definition _ (non-degenerate, symmetric) bilinear forms, quadratic forms, quadratic spaces, homomorphisms of quadratic spaces, quadratic linear map|definition]]. Consider $\beta(w - \lambda v, w - \lambda v) = q(w) - 2 \lambda \beta(v, w)$. There is some $\lambda \in \mathbb{F}$ such that $\beta(w - \lambda v) = 0$. Thus, $v, w$ span $H$.

By [[Quadratic forms and K-theory --- pcmi-2021/notes/Direct sums of quadratic spaces#_theorem _ Witt cancellation theorem or the cancellation theorem|the Witt cancellation theorem]], the smaller $U$ is determined up to isomorphism.

---

##### _corollary:_ it suffices to understand anisotropic forms

Any quadratic form $V, q$ decomposes uniquely into $H^{\oplus r} \oplus U$, where $U$ is an anisotropic quadratic form.

---

This reduces the work of classifying quadratic forms to classifying anisotropic quadratic forms. In fact, we can classify anisotropic quadratic forms using this too. To understand if two anisotropic quadratic spaces $V, W$ are isomorphic, we note that $V$ represents $a$ if and only if $W$ does too. Choose $a = q(v)$. Then $V \oplus \left< -a \right>$ is isotropic and $V \cong W$ only if $W \oplus \left< -a \right>$ is isotropic too. If $W \oplus \left< -a \right>$ is anisotropic, then $V \not \cong W$. Else, split off hyperbolic planes from $V \oplus \left< -a \right>$ and $W \oplus \left< -a \right>$ to get two smaller-dimensional dimensional quadratic spaces $V', W'$. $V \cong W$ if and only if $V \oplus \left< -a \right> \cong W \oplus \left< -a \right>$ if and only if $V' \cong W'$.