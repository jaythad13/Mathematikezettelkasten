---
tags:
- lin-alg
- alg
- nt
- pcmi-2021/1
---

The following classical results in number theory can all be understood through the theory of quadratic forms. They all show representability of certain numbers by quadratic forms over $\mathbb{Z}$.

##### _theorem:_ Lagrange's four squares theorem

Every positive integer is the sum of four integer squares.

---

##### _theorem:_ Legendre's three squares theorem

Let $n$ be a positive integer and let $n = 4^m d$ with $d$ not divisible by $4$. Then $n$ is the sum of three squares if and only if $n \not\equiv 7 \pmod 8$.

---

##### _theorem:_ Fermat's two squares theorem

A positive integer is a sum of two integer squares if and only if any prime factor $p \equiv 3 \pmod 4$ occurs with even multiplicity.

---

We will first study quadratic forms over an (almost arbitrary) field $\mathbb{F}$. In particular, for the rest of this note, let $\mathbb{F}$ be a field of [[p-adic numbers --- math-177/notes/Finite fields#_definition _ characteristic|characteristic]] not $2$. We want quadratic forms to be functions $q : \mathbb{F}^n \to \mathbb{F}$ such that $q(x) = \sum a_{ij} x_{i} x_{j}$ up to linear change of variables.

##### _definition:_ (non-degenerate, symmetric) bilinear forms, quadratic forms, quadratic spaces, homomorphisms of quadratic spaces, quadratic linear map

Let $V$ be a finite-dimensional $\mathbb{F}$-[[Linear algebra done right --- ladr/notes/Vector spaces#_definition _ vector space|vector space]].

A **bilinear form** on $V$ is a function $\beta : V \times V \to \mathbb{F}$ such that for each $u \in V$, the functions $V \to \mathbb{F}$ by $v \mapsto \beta(u, v)$ and $v \mapsto \beta(v, u)$ are linear. $\beta$ is **symmetric** if $\beta(v, w) = \beta(w, v)$ for each pair of $v, w \in V$. $\beta$ is **non-degenerate** if, for each $v \in V$, there exists some $w \in V$ such that $\beta(v, w) \neq 0$. Equivalently $\beta$ is non-degenerate if $v \mapsto \beta(v, -)$ is an injection $V \to V^\vee$ (and thus, an isomorphism).

We call a non-degenerate symmetric bilinear form a **quasi-inner product**.

Each non-degenerate, symmetric, bilinear form determines a function $q_{\beta} : V \to \mathbb{F}$ by $v \mapsto \beta(v, v)$. A function $q : V \to \mathbb{F}$ is a **quadratic form** if it is equal to some $q_{\beta}$. The pair $V, q$ of a vector space and a quadratic form on it is called a **quadratic space**.

A **homomorphism of quadratic spaces** or a **quadratic linear map** $T : V, q_{V} \to W, q_W$ is a linear map $T : V \to W$ such that $q_{V}(v) = q_{W}(T v)$.

---

Choose a basis $e_{1}, \dots, e_{n}$ of $V$. Note that the following pieces of information are equivalent — a non-degenerate symmetric bilinear form, the (symmetric) matrix $A$ with $A_{i,j} = \beta(e_{i}, e_{j})$, and the corresponding quadratic form $q_{\beta}$. It's easy to see that the first two are equivalent (by bilinearity) and they determine the third. The quadratic form determines the bilinear form by
$$
\beta(v, w) = \frac{q(v + w) - q(x) - q(y)}{2}.
$$
Here we use the fact that $2 \in \mathbb{F}^\times$. Thus, this allows us to denote the corresponding quasi-inner product for a quadratic space by $\beta_{q}$ or just $\beta$ when it's clear from context.

Finally, note that quasi-inner products over $\mathbb{R}$ are not the same as inner products over $\mathbb{R}$ (consider the quadratic form $v \mapsto - \lVert v \rVert$). We will see that this is the only possible difference (up to isomorphism).

We are interested in when two quadratic forms over the same vector space are isomorphic, and when there is a some non-zero $v \in V$ such that $q(v) = 0$. More generally, we are interested in which elements of $\mathbb{F}$ appear as $q(v)$ for some $v \in V$.

##### _definition:_ isotropic, represents

A quadratic space $V, q$ is **isotropic** if there is some non-zero $v \in V$ such that $q(v) = 0$.

More generally, $V, q$ represents $a \in \mathbb{F}$ if there is some non-zero $v \in V$ such that $q(v) = a$.

---

That is, we want to understand when quadratic spaces are isotropic and what $a \in \mathbb{F}$ they represent. We can answer all of these questions over $\mathbb{Q}$ by Hasse–Minkowski's [[PUNDiT --- pundit/notes/Introduction to the Hasse principle|local-to-global principle]]. These methods break down for higher degree forms because they don't have the symmetries that we get from the notion of orthogonality for quadratic forms.

### Orthogonality and diagonalisation

Just as for inner products over $\mathbb{R}$ and $\mathbb{C}$, we have a notion of orthogonality for quadratic spaces.

##### _definition:_ orthogonal, orthogonal complement

Two vectors in $V, q$ are **orthogonal** if $\beta(v, w) = 0$.

For a vector subspace $U \subseteq V$ its **orthogonal complement** is the set of all vectors orthogonal to $U$.
$$
U^\perp = \{ v \in V \mid \beta(u, v) \text{ for each } u \in U \}.
$$

---

Some of the results that are true for orthogonality over inner product spaces are true over quadratic spaces as well.

##### _proposition:_ dimension of the orthogonal complement

Suppose $U \subseteq V$ is a vector subspace. Then $\dim U + \dim U^\perp = \dim V$.

###### _proof sketch:_

Let $\varphi : V \to V^{\vee}$ be the isomorphism by $v \mapsto \beta(-, v)$. Then $U^\perp$ is the pre-image of $U^0$ the annihilator of $U$. Since $\varphi$ is an isomorphism, $\dim U^\perp = \dim U^0 = \dim V - \dim U$. 

---

Note that [[Linear algebra done right --- ladr/notes/Orthogonal complements and projections|unlike for inner products over]] $\mathbb{R}$ and $\mathbb{C}$, we do not have $V = U \oplus U^\perp$. It is true if and only if the quadratic form restricts to a quadratic form over $U$.

##### _proposition:_ direct sum decomposition of quadratic spaces

For any vector subspace $U \subseteq V$, the following are equivalent:
1) $V = U \oplus U^\perp$
2) $q$ restricts to a quadratic form on $U$.
3) $q$ restricts to a quadratic form on $U^\perp$

---

This generalises to the definition of the (external) direct sum of quadratic spaces.

##### _definition:_ direct sum of quadratic spaces

The **direct sum of quadratic spaces** $V_{1}, q_{1}$ and $V_{2}, q_{2}$ is the quadratic space $V_{1} \oplus V_{2}, q_{1} + q_{2}$ where $(q_{1} + q_{2})(v_{1} \oplus v_{2}) = q_{1}(v_{1}) + q_{2}(v_{2})$. 

Equivalently, $q_{1} + q_{2}$ restricts to $q_{i}$ on the corresponding $V_{i}$ and $V_{1} \oplus V_{2}$ contains the two as orthogonal subspaces.

---

The nicest inner product spaces are one-dimensional and are just given by choosing a basis vector $e_{1}$ and some $a \in \mathbb{F}^\times$ such that $q(e_{1}) = a$. The next nicest we could imagine are direct sums of these. It turns out that all quadratic forms are so nice!

##### _definition:_ diagonal quadratic forms

Let $a_{1}, \dots, a_{n} \in \mathbb{F}^\times$. A **diagonal quadratic form** on $\mathbb{F}^n$ is one given by $q(e_{i}) = a_{i}$ and $\beta_{q}(e_{i}, e_{j}) = 0$ for $i \neq j$. It is denoted $\left< a_{1}, \dots, a_{n} \right>$.

---

Note that $\left< a_{1}, \dots, a_{n} \right> \cong \left< a_{1} \right> \oplus \dots \oplus \left< a_{n} \right>$.

##### _theorem:_ diagonalisation of quadratic forms

Any quadratic space is isomorphic to a diagonal inner product space.

Equivalently, any symmetric matrix is [[diagonalisable]].

###### _proof sketch:_

 Choose some $v \in V$ such that $q(v) \neq 0$ (it's easy to see that there must be one by non-degeneracy). Write $U$ for $\operatorname{span} v$. $q$ restricts to an quadratic form on $U$ so $V \cong U \oplus U^\perp$. Clearly $U, q_{\mid U} \cong \left< a \right>$. The result follows by induction on the dimension of $V$.

---

Note that this diagonalisation is not unique. For example, for any $u_{1}, \dots, u_{n} \in \mathbb{F}^\times$, we have $\left< a_{1}, \dots, a_{n} \right> \cong \left< a_{1} u_{1}^{2}, \dots, a_{n} u_{n}^{2} \right>$.

##### _corollary:_ diagonalising quadratic forms over $\overline{\mathbb{F}}$ and $\mathbb{R}$

If every element of $\mathbb{F}$ is a square (for example, if $\mathbb{F}$ is algebraically closed) then any quadratic space is isomorphic to $\left< 1, \dots, 1 \right>$.

If $\mathbb{F} = \mathbb{R}$, then any quadratic form is isomorphic to $\left< 1 \right>^{\oplus r} \oplus \left< 1 \right >^{\oplus s}$.

---

A result of Sylvester shows that over $\mathbb{R}$, this choice of $r, s$ is unique. It is called the **signature** of the quadratic form.

### The orthogonal group

The orthogonal group is the group of symmetries of the quadratic space.

##### _definition:_ orthogonal group of a quadratic space

The orthogonal group of $V, q$, denoted $\mathrm{O}(V, q)$ is the group of quadratic linear isomorphisms of $V$.

---

There is a particular nice subgroup of the orthogonal group. In particular, for every $v \in V$, we can reflect across $\operatorname{span} v$.

##### _definition:_ reflections

For non-zero $u \in V$, the **reflection across $u$** is the quadratic linear isomorphism $R_{u} : V \to V$ given by
$$
R_{u}(v) = v - \frac{2 \beta(u, v)}{q(v)} v.
$$

---

##### _theorem:_ Cartan–Dieudonné

$\mathrm{O}(V, q)$ is generated by (at most $\dim V$) reflections.

---