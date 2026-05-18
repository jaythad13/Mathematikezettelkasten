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
\beta(v, w) = \frac{q(v + w) - q(v) - q(w)}{2}.
$$
Here we use the fact that $2 \in \mathbb{F}^\times$. Thus, this allows us to denote the corresponding quasi-inner product for a quadratic space by $\beta_{q}$ or just $\beta$ when it's clear from context.

Finally, note that quasi-inner products over $\mathbb{R}$ are not the same as inner products over $\mathbb{R}$ (consider the quadratic form $v \mapsto - \lVert v \rVert$). We will see that this is the only possible difference (up to isomorphism) — for inner products over $\mathbb{R}$ we require $\left< v, v \right> > 0$ rather than just $\left< v, v \right> \neq 0$ for some $v \in V$. They are not the same as inner products over $\mathbb{C}$ which are sesquilinear rather than bilinear.

We are interested in when two quadratic forms over the same vector space are isomorphic, and when there is a some non-zero $v \in V$ such that $q(v) = 0$. More generally, we are interested in which elements of $\mathbb{F}$ appear as $q(v)$ for some $v \in V$.

##### _definition:_ isotropic, isotropic vector,ll represents

A quadratic space $V, q$ is **isotropic** if there is some non-zero $v \in V$ such that $q(v) = 0$. Such a $v$ is called an **isotropic vector**.

Generally, $V, q$ **represents $a \in \mathbb{F}$** if there is some non-zero $v \in V$ such that $q(v) = a$.

---

That is, we want to understand when quadratic spaces are isotropic and which $a \in \mathbb{F}$ they represent. We can answer all of these questions over $\mathbb{Q}$ by Hasse–Minkowski's [[PUNDiT --- pundit/notes/Introduction to the Hasse principle|local-to-global principle]]. These methods break down for higher degree forms because they don't have the symmetries that we get from the notion of [[Quadratic forms and K-theory --- pcmi-2021/notes/Orthogonality for quadratic forms#_definition _ orthogonal, orthogonal complement|orthogonality for quadratic forms]].