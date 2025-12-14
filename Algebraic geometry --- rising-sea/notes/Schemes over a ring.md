---
tags:
- alg-geo
- comm-alg
- rising-sea/5/4
---

Let $A$ be a ring, $\mathbb{F}$ be a field.

We want to have a definition of a $\mathbb{F}$-scheme, or more generally an $A$-scheme — a scheme where points take values in $\mathbb{F}$ or $A$. We can do this both directly, using algebra, and also using morphisms of schemes. With morphisms of schemes we will see that $A$- and $\mathbb{F}$-schemes are special cases of the relative notion of $S$-schemes for an arbitrary base scheme $S$. This, in turn, is a special case of the notion of a slice category.

### ... algebraically

##### _definition:_ $A$-schemes

An **$A$-scheme** or **scheme over $A$** is a scheme $X$ where $\mathscr{O}_{X}$ is a sheaf of $A$-algebras.

---

The case we really want to consider are schemes that are roughly finite-dimensional in some sense — things like $\operatorname{Spec} \mathbb{F}[x_{1}, \dots, x_{n}] / \mathfrak{i}$ or $V(f) \subseteq \mathbb{P}^n_{A}$. Note that this isn't actually a notion of dimension.

##### _definition:_ locally of finite type, finite type

An $A$-scheme $X$ is **locally of finite type over $A$** if every affine open $\operatorname{Spec} B \subseteq X$ is a finitely generated $A$-algebra.

$X$ is **finite type** if it is locally of finite type and also [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#Quasicompactness|quasicompact]].

---

[[Algebraic geometry --- rising-sea/notes/Noetherian schemes#_definition _ locally Noetherian scheme, Noetherian scheme|Like Noetherianness]], this is another example of $P$ meaning locally $P$ plus quasicompact.

##### _example:_ quasiprojective schemes are finite type

Suppose $X = \operatorname{Proj} S_{\bullet}$ is a [[Algebraic geometry --- rising-sea/notes/Projective schemes#_definition _ projective $A$-schemes, quasiprojective $A$-schemes|projective]] $A$-scheme. Then $S_{\bullet}$ is finitely generated, and thus, so are all the $(S_{\bullet})_{f}$ and finally, all the $((S_{\bullet})_{f})_{0}$, giving a finite type affine cover of $X$.

Since all the affine opens covering $X$ are finite type, we can find a finite type affine open cover of any quasiprojective $U \subseteq X$ as well. In fact, this shows that any open subscheme of $X$ is locally of finite type. Of course, since we know [[Algebraic geometry --- rising-sea/notes/Examples of schemes#_example _ infinite-dimensional affine space is non-Noetherian|affine schemes that are not Noetherian]], we can find open subschemes that are locally of finite type but not actually of finite type.

---

As always with this type of thing, we don't actually want to check finite type-ness on every affine open. The affine communication lemma comes to the rescue once again.

##### _proposition:_ finite type-ness is affine local

Suppose $B$ is a ring and $(g_{1}, \dots, g_{n}) = B$. Let $B$ be an $A$-algebra.
1) If $B$ is finitely generated over $A$, then so is each $B_{g_{i}}$.
2) If each $B_{g_{i}}$ is finitely generated over $A$, then so is $B$.

###### _proof:_

Suppose $B$ is finitely generated over $A$. Since $B_{g} = B[g^{-1}] / (g g^{-1} - 1)$, if $B$ is finitely generated over $A$, then $B_{f}$ is finitely generated over $A$.

Suppose each $B_{g_{i}}$ is finitely generated over $A$. Specifically, let each $B_{g_{i}}$ be generated over $A$ by elements $x_{ij} / g_{i}^{\ell_{j}} \in B_{g_{i}}$. Writing $g \in B$ as an element of $B_{g_{i}}$ with these generators, and then converting that equality back into a cross-ratio in $B$ we get
$$
g_{i}^{m_{i}} g = g_{i}^{m_{i}} \sum a_{ij} (x_{ij} / g_{i}^{\ell_{j}})^{m_{ij}}.
$$
Since $D(g_{i}^{m_{i}}) = D(g_{i})$ (each principal ideals is [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_proposition _ containment of distinguished opens|contained in the radical of the other]]), the $D(g_{i}^{m_{i}})$ cover $\operatorname{Spec} B$, and [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_proposition _ distinguished covers generate the whole ring|thus]], $(g_{1}^{m_{1}}, \dots, g_{n}^{m_{n}}) = B$. Write $1 = \sum b_{i} g_{i}^{m_{i}}$. Thus, 
$$
g = \left( \sum_{i = 1}^n b_{i} g_{i}^{m_{i}} \right) g = \sum_{i = 1}^n \left( b_{i} g_{i}^{m_{i}} \sum_{ij} a_{ij} (x_{ij} / g_{i}^{\ell_{j}})^{m_{ij}} \right)
$$
which expresses $g$ in terms of the many, but finitely many $b_{i}$, $g_{i}$, and $x_{ij}$.

---

### Some variety

The notion of finite type schemes also allows us to define varieties (or a large class of them).

##### _definition:_ affine, projective, and quasiprojective varieties

An **affine $\mathbb{F}$-variety** is a [[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_definition _ reduced (schemes)|reduced]] [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition _ affine scheme|affine]] finite type $\mathbb{F}$.

A **(quasi)projective $\mathbb{F}$-variety** is a reduced (quasi)projective finite type $\mathbb{F}$-scheme

---

Some also require varieties to be irreducible (so disjoint unions of varieties are not varieties). This is of course equivalent to requiring [[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_definition _ integral scheme|integral]] instead of reduced.

Let $X$ be a locally finite type $\mathbb{F}$-scheme. One can study $X$ primarily at closed points (just like a variety), and in turn, one can study the closed points by their residue fields.

##### _proposition:_ closed points have finite residue field extensions

Suppose $p \in X$ is a closed point. Then $\kappa(p)$ is a finite field extension.

###### _proof:_

Identify $p$ with some maximal ideal $\mathfrak{m} \subseteq A$ where $A$ is a finitely generated $\mathbb{F}$-algebra. Then $\kappa(p) = A_{\mathfrak{m}} / \mathfrak{m}_{\mathfrak{m}} \cong (A / \mathfrak{m})_{\mathfrak{m}} \cong A / \mathfrak{m}$ is a finitely generated $\mathbb{F}$-algebra as well since there with surjection $\mathbb{F}[x_{1}, \dots, x_{n}] \to A \to A / \mathfrak{m}$. By [[Algebraic geometry --- rising-sea/notes/Hilbert's Nullstellensatz|Hilbert's Nullstellensatz]], a finitely-generated $\mathbb{F}$-algebra that is a field is also finitely generated as a field. 

---

##### _definition:_ degree of a closed point

The **degree of a closed point** $p \in X$ is the degree of the field extension $\kappa(p) / \mathbb{F}$.

---

For example, the point $(x^{2} + 1) \in \mathbb{A}_{\mathbb{R}}^1$ has degree $2$ since $\mathbb{C} / \mathbb{R}$ is a degree $2$ extension, while $(x^{3} + 2) \in \mathbb{A}_{\mathbb{Q}}^1$ has degree $3$ since $\mathbb{Q}(\sqrt[3]{ 2 }) / \mathbb{Q}$ is degree $3$.

### ... categorically