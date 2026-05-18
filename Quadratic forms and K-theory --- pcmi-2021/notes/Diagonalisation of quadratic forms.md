---
tags:
- lin-alg
- alg
- pcmi-2021/1
---

Let $\mathbb{F}$ be a field of characteristic not $2$.

The nicest inner product spaces are one-dimensional and are given by just choosing a basis vector $e_{1}$ and the $a \in \mathbb{F}^\times$ such that $q(e_{1}) = a$. The next nicest we could imagine are [[Quadratic forms and K-theory --- pcmi-2021/notes/Direct sums of quadratic spaces#_definition _ direct sum of quadratic spaces|direct sums]] of these. It turns out that all quadratic forms are so nice!

##### _definition:_ diagonal quadratic forms

Let $a_{1}, \dots, a_{n} \in \mathbb{F}^\times$. A **diagonal quadratic form** on $\mathbb{F}^n$ is one given by $q(e_{i}) = a_{i}$ and $\beta_{q}(e_{i}, e_{j}) = 0$ for $i \neq j$. It is denoted $\left< a_{1}, \dots, a_{n} \right>$.

---

Note that $\left< a_{1}, \dots, a_{n} \right> \cong \left< a_{1} \right> \oplus \dots \oplus \left< a_{n} \right>$.

##### _theorem:_ diagonalisation of quadratic forms

Any quadratic space is isomorphic to a diagonal quadratic space.

Equivalently, any symmetric matrix is [[diagonalisable]].

###### _proof sketch:_

Choose some $v \in V$ such that $q(v) \neq 0$ (it's easy to see that there must be one by non-degeneracy). Write $U$ for $\operatorname{span} v$. $q$ restricts to an quadratic form on $U$ so $V \cong U \oplus U^\perp$. Clearly $U, q_{\mid U} \cong \left< a \right>$. The result follows by induction on the dimension of $V$.

---

Note that this diagonalisation is not unique. For example, for any $u_{1}, \dots, u_{n} \in \mathbb{F}^\times$, we have an isomorphism $\left< a_{1}, \dots, a_{n} \right> \to \left< a_{1} u_{1}^{2}, \dots, a_{n} u_{n}^{2} \right>$ by rescaling each $e_{i}$ by $1 / u_{i}$.

##### _corollary:_ diagonalising quadratic forms over $\overline{\mathbb{F}}$ and $\mathbb{R}$

If every element of $\mathbb{F}$ is a square (for example, if $\mathbb{F}$ is algebraically closed) then any quadratic space is isomorphic to $\left< 1, \dots, 1 \right>$.

If $\mathbb{F} = \mathbb{R}$, then any quadratic form is isomorphic to $\left< 1 \right>^{\oplus r} \oplus \left< -1 \right >^{\oplus s}$.

---

[[Quadratic forms and K-theory --- pcmi-2021/attachments/exercises/ex 1/ex 1.pdf#page=1|Sylvester's theorem]] shows that the choice of $r, s$ for a quadratic form over $\mathbb{R}$ is unique. It is called the **signature** of the quadratic form.