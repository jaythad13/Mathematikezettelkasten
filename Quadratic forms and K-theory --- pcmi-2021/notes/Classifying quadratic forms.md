---
tags:
- lin-alg
- alg
- nt
- pcmi-2021/2
---

Recall that the theory of hyperbolic quadratic forms reduces the work of classifying of all quadratic forms to classifying anisotropic forms.

Thus, in classification of quadratic forms, the following idea is useful.

##### _definition:_ $u$-invariant

The **$u$-invariant** of a field $\mathbb{F}$ is $u(\mathbb{F})$, the largest dimension of an [[Quadratic forms and K-theory --- pcmi-2021/notes/Quadratic forms#_definition _ isotropic, isotropic vector, anisotropic, represents|anisotropic quadratic space]] over $\mathbb{F}$ if it exists, or $\infty$ otherwise

---

The $u$-invariant is then a measure of complexity of the theory of quadratic forms over the field — fields of small $u$-invariant require less work for the classification of quadratic forms. This is easiest to understand with some examples in which we already know the classification of quadratic forms.

##### _examples:_ $u$-invariants of $\mathbb{R}$ and $\mathbb{C}$

$u(\mathbb{R}) = \infty$ since $\left< 1, \dots, 1 \right>$ is always anisotropic. $u(\mathbb{C}) = 1$ and in fact $u(\overline{\mathbb{F}}) = 1$ for any algebraically closed field $\overline{\mathbb{F}}$ by [[Quadratic forms and K-theory --- pcmi-2021/notes/Diagonalisation of quadratic forms#_corollary _ diagonalising quadratic forms over $ overline{ mathbb{F}}$ and $ mathbb{R}$|diagonalisation]] and existence of $\sqrt{ n - 1 }$.

---

Another useful invariant is the discriminant.

##### _definition:_ discriminant of a quadratic space

Suppose $V, q$ is a quadratic space. Choose a basis $e_{1}, \dots, e_{n}$ of $V$, let $a \mapsto \overline{a}$ denote the map $\mathbb{F}_{q} \to \mathbb{F}_{q}^\times / \mathbb{F}_{q}^{\times 2}$, and let $A$ be the matrix with $A_{ij} = \beta(e_{i}, e_{j})$. Then the **discriminant** of $V, q$ is $\operatorname{disc}(V, q) = \overline{\det A}$.

---

Note that $\operatorname{disc}(\left< a_{1}, \dots, a_{n} \right>)$ is just $\overline{\prod a_{i}}$ then. It is invariant of the choice of basis — any change of basis changes the symmetric matrix as follows $A \mapsto B^\top A B$. Thus, $\det (B^\top A B) = \det A (\det B)^{2}$ and so $\overline{\det (B^\top A B)}$

### Quadratic forms over a finite field.

Fix a finite field $\mathbb{F}_{q}$, where $q = p^n$ for some prime $p$.

A much more involved example is the complete classification of quadratic spaces over finite fields. We will see how the $u$-invariant and discriminant are useful.

##### _theorem:_ $u$-invariant of a finite field

$u(\mathbb{F}_{q}) = 2$.

###### _proof:_

It suffices to show that every quadratic form of dimension $3$ is isotropic and that there exist anisotropic forms of dimensions $1$ and $2$.

For the former, we want to show that for any $a, b, c \in \mathbb{F}_{q}^\times$, there exist $x, y, z \in \mathbb{F}_{q}$, not all zero, such that $ax^{2} + by^{2} + cz^{2} = 0$. Suppose, without loss of generality, that $z = 1$. Then we want $ax^{2} = -c + by^{2}$. There are at least $1 + (q - 1) / 2 = (q + 1) / 2$ squares. The only element squaring to $0$ is $0$. The other $q - 1$ elements of $\mathbb{F}_{q}$ give rise to at least $q$.

Since $x^{2} \mapsto ax^{2}$ and $y^{2} \mapsto -c + by^{2}$ are both invertible, $\{ ax^{2} \mid x \in \mathbb{F}_{q} \}$ and $\{ -c + by^{2} \mid y \in \mathbb{F}_{q} \}$ both have cardinality $(q + 1) / 2 > \# \mathbb{F}_{q} / 2$ and thus, have non-empty intersection.

In dimension $1$, any $\left< a \right>$ is anisotropic. Suppose $a \in \mathbb{F}_{q}^\times \setminus \mathbb{F}_{q}^{\times 2}$. Then $\left< 1, -a \right>$ is anisotropic — if $x^{2} - ay^{2} = 0$, then $a = (x / y)^{2}$.

---

We can classify the quadratic forms of dimensions $1$ and $2$ by their discriminant (and dimension), and thus all quadratic forms. 

##### _theorem:_ classification of quadratic forms over a finite field

Suppose $V, q_{V}$ and $W, q_{W}$ are two quadratic spaces. $V, q_{V} \cong W, q_{W}$ if and only if $\dim V = \dim W$ and $\operatorname{disc}(V, q_{V}) = \operatorname{disc}(W, q_{W})$.

###### _proof:_

Clearly, if $V, q_{V} \cong W, q_{W}$, then the dimension and discriminant are equal.

Suppose $\dim V = \dim W = 1$. Then giving an isomorphism $V, q_{V} \cong W, q_{W}$ is equivalent to giving an isomorphism $\left< a \right> \cong \left< b \right>$. Since $\mathrm{GL}(\mathbb{F}_{q}^1) = \mathbb{F}_{q}^\times$, the isomorphism must be given by $v \mapsto uv$. Then $a = q_{V}(v) = q_{W}(uv) = u^{2} q_W(v) = u^{2} b$. That is, $\overline{a} = \overline{b}$ (as elements of $\mathbb{F}_{q}^\times / \mathbb{F}_{q}^{\times 2}$).

Suppose $\dim V = 2$ and $\operatorname{disc}(V, q_{V}) = \overline{d}$. Since $u(\mathbb{F}_{q}) = 2$, $V \oplus \left< -1 \right>$ is isotropic. That is, there is some $(x, y, z) \in \mathbb{F}_{q}^3$ such that $q_{V}(x, y) - z^{2} = 0$. Since $V$ is anisotropic, $z$ must be non-zero. Thus, without loss of generality we can choose $z = 1$. That is, we have $v = (x, y) \in V$ with $q_{V}(x, y) = 1$. Choose $w \in \operatorname{span} (x, y)^\perp$. Then $v, w$ diagonalise $V, q_{V}$ as $\left< 1, a \right>$. This gives $\overline{1} \overline{a} = \operatorname{disc}(V, q) = \overline{d}$, and thus, $V, q_{V} \cong \left< 1, d \right>$.

If $\dim V = n > 2$ then $V, q_{V} \cong (U, q_{U}) \oplus H^m$ where $\dim U \leq 2$. We have $\operatorname{disc}(V, q_{V}) = \overline{(-1)^m} \operatorname{disc}(U, q_{U})$. The parity of the dimension determines $\dim U$ and $m$, dividing $\operatorname{disc}(V, q_{V})$ by $\overline{(-1)^m}$ then determines $U$.

---

To understand this result it is useful to know the form of $\mathbb{F}_{q}^\times / \mathbb{F}_{q}^{\times 2}$.

##### _lemma:_ the square class group of a finite field

$\mathbb{F}_{q}^\times / \mathbb{F}_{q}^{\times_{2}} \cong \mathbb{Z} / (2)$

###### _proof:_

By the proof above, $\# \mathbb{F}_{q}^{\times 2} \geq (q - 1) / 2$. Thus, $\# (\mathbb{F}_{q}^\times / \mathbb{F}_{q}^{\times 2}) \leq 2$. Not every element of $\mathbb{F}_{q}^\times$ is a square — in odd characteristic there are always  squares $a^{2}$ that have two square roots $\pm a$ and there are only $q - 1$ possible square roots to go around.

---

This means that in every dimension, there are exactly two quadratic forms over $\mathbb{F}_{q}$.