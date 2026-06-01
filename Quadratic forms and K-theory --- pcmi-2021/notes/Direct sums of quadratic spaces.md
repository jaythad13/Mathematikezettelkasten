---
tags:
- lin-alg
- alg
- pcmi-2021/1
---

We can do more than just combine vector spaces with direct sums — we can combine the quadratic forms on them too.

##### _definition:_ direct sum of quadratic spaces

The **direct sum of quadratic spaces** $V, q_{V}$ and $W, q_{W}$ is the quadratic space $(V, q_{V}) \oplus (W, q_{W}) = V \oplus W, q_{V} + q_{W}$ where $(q_{V} + q_{W})(v \oplus w) = q_{V}(v) + q_{W}(w)$. We may abbreviate the direct sum to $V_{1} \oplus V_{2}$ when there is no ambiguity about the forms.

Equivalently, $q_{V} + q_{W}$ restricts to $q_{V}$ on $V$ and $q_{W}$ on $W$, and $V \oplus W$ contains the two as orthogonal subspaces.

---

This construction really does deserve the name direct sum.

##### _proposition:_ the universal property of the quadratic direct sum

$V \oplus W, q_{V} + q_{W}$ with the obvious maps $i_{V} : V \to V \oplus W$ and $i_{W} : W \to V \oplus W$ is the [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ coproducts, direct sums|coproduct]] of  $V, q_{V}$ and $W, q_{W}$.

###### _proof sketch:_

Suppose $Z, q_{Z}$ has quadratic linear maps $i_{V}' : V \to Z$ and $i_{W}' : W \to Z$. Then consider $\amalg : V \oplus W \to Z$ by $v \oplus w \mapsto i_{V}'(v) + i'_{W}(w)$. It's easy to check that this is a quadratic linear map. This factors $i_{V}'$ as $i_{V}' = \amalg \circ i_{V}$ and similarly for $W$.

$\amalg$ is unique since it is the unique factorisation for the universal property of the direct sum in the category of vector spaces.

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

This is incredible! Typically **stable isomorphism classes** ($V \sim W$ if there exists some isomorphism $V \oplus Z \cong V \oplus Z$) identify many more objects than isomorphism classes. They are useful because we can localise/group-complete. This turns the stable isomorphism classes into an algebraic object. For example, the equivalence condition for [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_definition _ localisation of a ring, localisations at a prime, fraction field|localisation]]. Here, we still get the abstract goodness of group-completion and we also lose no information!