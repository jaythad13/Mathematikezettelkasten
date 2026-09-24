---
tags:
- alg
- rep-th
- math-174/4
- math-174/5
---

Unlike in the case of vector spaces, a submodule need not have a complement. Even if it does have a complement, not every choice of extension of the basis need give a complementary submodule.

##### _example:_ the permutation representation of $\mathfrak{S}_{2}$

Let $\mathbb{C}[\mathfrak{S}_{2}] \to \operatorname{End} \mathbb{C}^{\oplus 2}$ be given by the permutation representation on the standard basis of $\mathbb{C}^{\oplus 2}$. Then $(1, 1)$ spans a $\mathbb{C}[{\mathfrak{S}_{2}}]$-submodule. $(1, -1)$ spans a complementary submodule. $(1, 0)$ does not span a complementary submodule, but does also span a complementary subspace of $\mathbb{C}^{\oplus 2}$.

If direct sums correspond to block diagonal decompositions, then such a basis gives a block upper triangular decomposition of the matrices. In particular, if $N_{1} \subseteq M$, then extending a basis of $N_{1}$ to a basis of $M$ gives a decomposition
$$
\rho(g) = \begin{pmatrix}
\rho_{N_{1}}(g) & *(g) \\
0 & \widetilde{\rho}(g)
\end{pmatrix}.
$$
In fact, $g \mapsto \widetilde{\rho}(g)$  is also a representation. It has $\mathbb{C}$-dimension $\dim_{\mathbb{C}} N_{2} = \dim_{\mathbb{C}} M - \dim_{\mathbb{C}} N_{1}$. It's just the quotient representation $M / N_{1}$.

Of course, this discussion applies more generally than over a group algebra base over a field.

---

This leads us to some important definitions.

##### _definition:_ irreducible, simple modules

An $R$-module $M$ is **irreducible** or **simple** if it is non-zero and it's only submodules are $0$ and $M$ itself.

---

You should think of irreducible $R$-modules as analogous to prime integers.

In representation theory, our goal is to decompose $\mathbb{F}[G]$-modules $M$ into direct sums of irreducible submodules $N_{i}$. It is not always possible to do this for general $R$-modules. Even with $\mathbb{F}[G]$-modules we have to be careful ($\mathbb{F}$ should have characteristic not dividing $\#G$). This is [[Representation theory --- math-174/notes/Maschke's theorem|Maschke's theorem]]. However, there is a special class of modules for which it is possible.

##### _definition:_ semisimple modules

An $R$-module $M$ is **semisimple** if every submodule $N_{1} \subseteq M$ has a complement $N_{2}$ such that $N_{1} \oplus N_{2} \cong M$.

---

It follows essentially by induction that each semisimple module admits a (unique) decomposition into a direct sum of irreducible submodules.

##### _proposition:_ semisimple modules are direct sums of irreducibles

If $M$ is a semisimple $R$-module, then $M \cong N_{1} \oplus \dots \oplus N_{m}$ where each $N_{i}$ is an irreducible $R$-module.

###### _proof sketch:_

In the case that $R$ is an $\mathbb{F}$-algebra, use induction on the $\mathbb{F}$-dimension of $M$. Just keep breaking things into pieces until you can't.

---

### Facts about irreducible modules

##### _lemma:_ Schur's lemma

Suppose $M$ and $N$ are irreducible $R$-modules. Then any homomorphism $\varphi : M \to N$ is an isomorphism or $0$.

###### _proof:_

The kernel is a submodule, and thus, either $0$ or $M$. Similarly, the image is either $0$ or $N$.

---

This is a very useful tool!

> Schur's lemma is the whole toolbox

\- Michael Orrison

For example, we can prove

##### _corollary:_ endomorphisms of an irreducible representation

Suppose $\mathbb{F}$ is algebraically closed. Suppose $M$ is an irreducible $R$-module (for $R$ an $\mathbb{F}$-algebra). Then any $\varphi \in \operatorname{End}_{R} M$ is just $\lambda \operatorname{id}_{M}$ for some $\lambda \in \mathbb{F}$.

###### _proof:_

Since $\varphi$ is $R$-linear, it is also $\mathbb{F}$-linear. Since $\mathbb{F}$ is algebraically closed, $\varphi$ has an eigenvalue $\lambda \in \mathbb{F}$. Then $\varphi - \lambda \operatorname{id}_{M}$ is not invertible, and thus, is $0$. That is, $\varphi = \lambda \operatorname{id}_{M}$.

---

##### _corollary:_ irreducible representations of an abelian group are just characters

Suppose $\mathbb{F}$ is algebraically closed and $G$ is a finite abelian group. Every irreducible $\mathbb{F}[G]$-module is one-dimensional.

###### _proof:_

Suppose $M$ is an irreducible $\mathbb{F}[G]$-module. For each $g \in G$ define the maps $T_{g} : m \mapsto g \cdot m$. They all commute with each other. Thus, $T_{g} : M \to M$ is not just $\mathbb{F}$-linear but is $\mathbb{F}[G]$-linear. But then $T_{g}$ is just scaling by some $\lambda \in \mathbb{F}$. Thus, $G \to \mathrm{GL}(M)$ factors as $G \to \mathbb{F}^\times \to \mathrm{GL}(M)$. Since $M$ is irreducible, we have $\mathbb{F}^\times \cong \mathrm{GL}(M)$ and $\dim_{\mathbb{F}} M = 1$.

Equivalently, every $\mathbb{F}$-subspace of $M$ is an $\mathbb{F}[G]$-submodule, including the one-dimensional ones. Since $M$ is irreducible it has only two $\mathbb{F}[G]$-submodules, and thus, only two $\mathbb{F}$-subspaces, and thus, is one-dimensional (irreducibles cannot be $0$).

---