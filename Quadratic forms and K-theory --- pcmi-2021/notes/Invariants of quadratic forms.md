---
tags:
- lin-alg
- alg
- nt
- pcmi-2021/2
- pcmi-2021/3
---

Recall that the theory of hyperbolic quadratic forms reduces the work of classifying of all quadratic forms to classifying anisotropic forms.

Thus, in classification of quadratic forms, the following invariants are useful.

##### _definition:_ $u$-invariant

The **$u$-invariant** of a field $\mathbb{F}$ is $u(\mathbb{F})$, the largest dimension of an [[Quadratic forms and K-theory --- pcmi-2021/notes/Quadratic forms#_definition _ isotropic, isotropic vector, anisotropic, represents|anisotropic quadratic space]] over $\mathbb{F}$ if it exists, or $\infty$ otherwise

---

The $u$-invariant is then a measure of complexity of the theory of quadratic forms over the field — fields of small $u$-invariant require less work for the classification of quadratic forms. This is easiest to understand with some examples in which we already know the classification of quadratic forms.

##### _examples:_ $u$-invariants of $\mathbb{R}$ and $\mathbb{C}$

$u(\mathbb{R}) = \infty$ since $\left< 1, \dots, 1 \right>$ is always anisotropic. $u(\mathbb{C}) = 1$ and in fact $u(\overline{\mathbb{F}}) = 1$ for any algebraically closed field $\overline{\mathbb{F}}$ by [[Quadratic forms and K-theory --- pcmi-2021/notes/Diagonalisation of quadratic forms#_corollary _ diagonalising quadratic forms over $ overline{ mathbb{F}}$ and $ mathbb{R}$|diagonalisation]] and existence of $\sqrt{ n - 1 }$.

---

Another useful invariant is the discriminant.

##### _definition:_ determinant of a quadratic space

Suppose $V, q$ is a quadratic space. Choose a basis $e_{1}, \dots, e_{n}$ of $V$, let $a \mapsto \overline{a}$ denote the map $\mathbb{F}_{q} \to \mathbb{F}_{q}^\times / \mathbb{F}_{q}^{\times 2}$, and let $A$ be the matrix with $A_{ij} = \beta(e_{i}, e_{j})$. Then the **determinant** of $V, q$ is $\det (V, q) = \overline{\det A}$.

---

Note that $\det (\left< a_{1}, \dots, a_{n} \right>)$ is just $\overline{\prod a_{i}}$ then. It is invariant of the choice of basis — any change of basis changes the symmetric matrix as follows $A \mapsto B^\top A B$. Thus, $\det (B^\top A B) = \det A (\det B)^{2}$ and so $\overline{\det (B^\top A B)}$

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

We can classify the quadratic forms of dimensions $1$ and $2$ by their determinant (and dimension), and thus all quadratic forms. 

##### _theorem:_ classification of quadratic forms over a finite field

Suppose $V, q_{V}$ and $W, q_{W}$ are two quadratic spaces. $V, q_{V} \cong W, q_{W}$ if and only if $\dim V = \dim W$ and $\operatorname{det}(V, q_{V}) = \operatorname{det}(W, q_{W})$.

###### _proof:_

Clearly, if $V, q_{V} \cong W, q_{W}$, then the dimension and discriminant are equal.

Suppose $\dim V = \dim W = 1$ and $\det (V, q_{V}) = \det (W, q_{V})$. Then, for diagonalisations $\left< a \right>, \left < b \right>$ we have $\overline{a} = \overline{b}$ in $\mathbb{F}_{q}^\times / \mathbb{F}_{q}^{\times 2}$, and thus, $a = b u^{2}$. There is then an isomorphism given by $v \mapsto v / u$.

Suppose $\dim V = 2$ and $\operatorname{det}(V, q_{V}) = \overline{d}$. Since $u(\mathbb{F}_{q}) = 2$, the $3$-dimensional form $V \oplus \left< -1 \right>$ is isotropic. That is, there is some $(x, y, z) \in \mathbb{F}_{q}^3$ such that $q_{V}(x, y) - z^{2} = 0$. Since $V$ is anisotropic, $z$ must be non-zero. Scaling, we have $q(x / z, y / z) - 1 = 0$. That is, we have $v = (x / z, y / z) \in V$ with $q_{V}(v) = 1$. Choose $w \in \operatorname{span} (v)^\perp$ with $q(w) = a \in \mathbb{F}^\times$. (Such an anisotropic vector exists since $q$ is non-degenerate on $\operatorname{span} v$, and [[Quadratic forms and K-theory --- pcmi-2021/notes/Orthogonality for quadratic forms#_proposition _ direct sum decomposition of quadratic spaces|thus]] also on $\operatorname{span}(v)^\perp$). Then $v, w$ diagonalise $V, q_{V}$ as $\left< 1, a \right>$. This gives $\overline{1} \overline{a} = \det (V, q) = \overline{d}$. In other words, $a = d u^{2}$ and thus, $V, q_{V} \cong \left< 1, d \right>$.

If $\dim V = n > 2$ then $V, q_{V} \cong (U, q_{U}) \oplus H^m$ where $\dim U \leq 2$. We have $\det(V, q_{V}) = \overline{(-1)^m} \det (U, q_{U})$. The parity of the dimension determines $\dim U$ and $m$, dividing $\operatorname{disc}(V, q_{V})$ by $\overline{(-1)^m}$ then determines $U$.

---

To understand this result it is useful to know the form of $\mathbb{F}_{q}^\times / \mathbb{F}_{q}^{\times 2}$.

##### _lemma:_ the square class group of a finite field

$\mathbb{F}_{q}^\times / \mathbb{F}_{q}^{\times_{2}} \cong \mathbb{Z} / (2)$

###### _proof:_

By the proof above, $\# \mathbb{F}_{q}^{\times 2} \geq (q - 1) / 2$. Thus, $\# (\mathbb{F}_{q}^\times / \mathbb{F}_{q}^{\times 2}) \leq 2$. Not every element of $\mathbb{F}_{q}^\times$ is a square — in odd characteristic there are always  squares $a^{2}$ that have two distinct square roots $\pm a$ and there are only $q - 1$ possible square roots to go around.

---

This means that in every dimension, there are exactly two quadratic forms over $\mathbb{F}_{q}$.

### Witt's chain equivalence theorem

Since we can diagonalise any quadratic space, it helps us to understand

##### _theorem:_ Witt's chain equivalence theorem

The isomorphism classes of quadratic forms are the equivalence classes determined by the equivalence relation generated by the following isomorphisms (as well as $\left< a_{1}, \dots, a_{n} \right> \cong \left< a_{1} \right> \oplus \dots \oplus \left< a_{n} \right>$).
1) $\left< a \right> \cong \left< a u^{2} \right>$
2) $\left< a_{1}, a_{2} \right> \cong \left< a_{2}, a_{1} \right>$
3) $\left< a_{1}, a_{2} \right> \cong \left< a_{1} + a_{2}, \frac{a_{1} a_{2}}{a_{1} + a_{2}} \right>$.

###### _proof:_

We note that the three relations above are in fact isomorphisms of one and two-dimensional quadratic forms. The first two are clear. The isomorphism $\left< a_{1} + a_{2}, \frac{a_{1}a_{2}}{a_{1} + a_{2}} \right> \to \left< a_{1}, a_{2} \right>$ is given by the map with $e_{1} \mapsto e_{1} + e_{2}$ and $e_{2} \mapsto (a_{2} e_{1} - a_{1} e_{2}) / (a_{1} + a_{2})$.

Say $\left< a_{1}, \dots, a_{n} \right> \sim \left< b_{1}, \dots, b_{n} \right>$ if they are in the same equivalence class generated by the fundamental isomorphism (1) through (3).

We want to show that if $\left< a_{1}, \dots, a_{n} \right> \cong \left< b_{1}, \dots, b_{n} \right>$ then $\left< a_{1}, \dots, a_{n} \right> \sim \left< b_{1}, \dots, b_{n} \right>$. By the [[Quadratic forms and K-theory --- pcmi-2021/notes/Direct sums of quadratic spaces#_theorem _ Witt cancellation theorem or the cancellation theorem|Witt cancellation theorem]] and induction on the dimension of the form, it suffices to show that $\left< a_{1}, \dots, a_{n} \right> \sim \left< b_{1}, b_{2}', \dots, b_{n}' \right>$. 

 Suppose we have some isomorphism $\left < b_{1}, \dots, b_{n} \right> \to \left< a_{1}, \dots, a_{n} \right>$. Thus, we can solve the equation $b_{1} = \sum_{i = 1}^n a_{i} x_{i}^{2}$ (just let $(x_{1}, \dots, x_{n})$ be the image of $e_{1}$). We can use the equivalences $\left< a_{i}' \right> = \left< a_{i} x_{i}^{2} \right> \sim \left< a_{i} \right>$ when $x_{i} \neq 0$ and $\left< a_{i}' \right> = \left< a_{i} \right>$ otherwise, to give us a solution $b_{1} = \sum_{i = 1}^r a_{i}'$. Here we sort the $a_{i}'$ so that the first $r$ of the $x_{i}$ are non-zero and the rest are zero. We can recursively reduce the size of the sum to one as follows. If $a_{r - 1}' + a_{r}' = 0$, then $b_{1} = \sum_{i = 1}^{r - 2} a_{i}'$. Else, using equivalence $\left< a_{r - 1}'', a_{r}'' \right> \sim \left< a_{r - 1}' + a_{r}', \dots, a_{r - 1}' a_{r}'/ (a_{r - 1} + a_{r}') \right>$ we obtain $b_{1} = \sum_{i = 1}^r a_{i}''$. Thus, we obtain some equivalence $\left< a_{1}, \dots, a_{n} \right> \sim \left< a_{1}^{(m)}, \dots, a_{n}^{(m)} \right >$ with $a_{1}^{(m)} = b_{1}$ as desired.

---

This gives something like $O(n^{2})$ equivalences (not counting sorting) to get any isomorphism $\left< a_{1}, \dots, a_{n} \right> \cong \left< b_{1}, \dots, b_{n} \right>$.

This is very useful to define isomorphism invariants — just choose a function on $(\mathbb{F}^\times)^n$ that is invariant under the isomorphisms above.