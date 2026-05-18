---
tags:
- lin-alg
- alg
- pcmi-2021/1
---

We can do more than just combine vector spaces with direct sums — we can combine the quadratic forms on them too.

##### _definition:_ direct sum of quadratic spaces

The **direct sum of quadratic spaces** $V_{1}, q_{1}$ and $V_{2}, q_{2}$ is the quadratic space $(V_{1}, q_{1}) \oplus (V_{2}, q_{2}) = V_{1} \oplus V_{2}, q_{1} + q_{2}$ where $(q_{1} + q_{2})(v_{1} \oplus v_{2}) = q_{1}(v_{1}) + q_{2}(v_{2})$. We may abbreviate the direct sum to $V_{1} \oplus V_{2}$ when there is no ambiguity about the forms.

Equivalently, $q_{1} + q_{2}$ restricts to $q_{i}$ on the corresponding $V_{i}$ and $V_{1} \oplus V_{2}$ contains the two as orthogonal subspaces.

---

### Witt cancellation theorem

Direct sums of quadratic forms are remarkable in that the stable isomorphism classes they induce are exactly the same as the regular isomorphism classes of quadratic forms.

##### _theorem:_ Witt cancellation theorem or the cancellation theorem

Let $(V, q_{V}), (W, q_{W}), (Z, q_{Z})$ be quadratic spaces. Suppose $V \oplus Z \cong W \oplus Z$. Then $V \cong W$.

###### _proof:_

We induct on the dimension of $Z$. Suppose $\dim Z = 1$. Let $T : V \oplus \left< c \right> \to W \oplus \left< c \right>$ be a quadratic linear isomorphism. Also, let $v_{0} \in V \oplus \left< c \right>$ span $\left< c \right>$ and choose $w_{0} \in W \oplus \left< c \right>$ similarly. Since [[Quadratic forms and K-theory --- pcmi-2021/notes/Orthogonality for quadratic forms#_lemma _ reflections act transitively on spheres|reflections act transitively on spheres]], there is some [[Quadratic forms and K-theory --- pcmi-2021/notes/Orthogonality for quadratic forms#_definition _ reflections|reflection]] $R$ with $R Tv_{0} = w_{0}$. Since $RT$ maps $\left< c \right>$ into $\left< c \right>$ isomorphically, it must also map orthogonal complements $V$ into $W$ isomorphically. That is, $R T_{\mid V}$ is an isomorphism $V \to W$.

Suppose $\dim Z = n$ and the theorem is true for all $Z$ of dimension at most $n - 1$. Diagonalise $Z, q_{Z}$ as $\left< c_{1}, \dots, c_{n} \right>$. Then
$$
V \oplus \left< c_{1}, \dots, c_{n - 1} \right> \oplus \left< c_{n} \right> \cong W \oplus \left< c_{1}, \dots, c_{n - 1} \right> \oplus \left< c_{n} \right>.
$$
Then $V \cong W$ follows from the cases of $1$ and $(n - 1)$-dimensional $Z$.

---

This is remarkable! Typically **stable isomorphism classes** ($V \sim W$ if there exists some isomorphism $V \oplus Z \cong V \oplus Z$) identify many more objects than isomorphism classes but are easier to deal with because we can localise/group-complete. This turns the stable isomorphism classes into an algebraic object. For example, the equivalence condition for [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_definition _ localisation of a ring, localisations at a prime, fraction field|localisation]]. Here, we still get the abstract goodness of group-completion and we also lose no information!