---
tags:
- rep-th
- math-174/8
- math-174/9
---

Suppose $G$ is a finite group and $\rho, V$ is an $\mathbb{F}$-linear representation of $G$.

We can think of characters as a special case of matrix coefficients.

##### _definition:_ character

The **character** of a representation $\rho, V$ is $\chi_{\rho} \in \mathbb{F}[G]$ given by $\sum_{g \in G} \operatorname{Tr} (\rho(g)) g$. 

We also think of the character as a function in the usual way with $\chi_{\rho}(g) = \operatorname{Tr}(\rho(g))$.

---

Since the trace is basis independent , isomorphic representations have the same trace. In fact, the character is a **class function** — it is constant on [[Abstract algebra --- math-171/notes/The class equation#_definition _ conjugacy classes|conjugacy classes]]. Finally, the trace is additive on direct sums of representations — $\chi_{\rho \oplus \sigma} = \chi_{\rho} + \chi_{\sigma}$.

##### _proposition:_ traces are just matrix coefficients

Suppose $\rho : G \to \mathrm{U}_{d}(\mathbb{C})$ is a unitary representation and $e_{1}, \dots, e_{d}$ is an orthonormal basis for the inner product. Then $\chi_{\rho} = u_{11} + \dots + u_{dd}$.

---

Since we have done the hard work to understand [[Representation theory --- math-174/notes/Orthogonality relations#_theorem _ all matrix coefficients of non-isomorphic irreps are orthogonal|orthogonality relations]] for [[Representation theory --- math-174/notes/Orthogonality relations#_definition _ matrix coefficients|matrix coefficients]] already, we get orthogonality of characters for free and many more useful corollaries for free.

##### _corollary:_ orthogonality for characters of irreducible representations

Suppose $\rho, \sigma$ are irreducible unitary representations (possibly of different dimension). Then with respect to the usual inner product on $\mathbb{C}[G]$,
$$
\left< \chi_{\rho}, \chi_{\sigma} \right> = \begin{cases}
\# G & \chi_{\rho} \cong \chi_{\sigma} \\
0.
\end{cases}
$$

---

##### _corollary:_ counting multiplicities of irreducible subrepresentations

Suppose $\rho, V$ is a representation of $G$ that decomposes into a direct sum of irreducible representations
$$
\rho = \rho_{1} \oplus \dots \oplus \rho_{k}.
$$

For $\sigma, W$ an irreducible representation of $G$, let $n_{\sigma} = \# \{ j \mid \rho_{j} \cong \sigma \}$ be the number of $\rho_{j}$ isomorphic to $\sigma$ so that $\rho = \bigoplus_{\sigma \in \widehat{G}} \sigma^{\oplus n_{\sigma}}$.

Then 
$$
n_{\sigma} = \frac{1}{\# G} \left< \chi_{\rho}, \chi_{\sigma} \right>.
$$

---

##### _corollary:_ finding irreducible representations

A representation of $G$, $\rho, V$ is irreducible if and only if $\lVert \chi_{\rho} \rVert^{2} = \# G$.

---

##### _corollary:_ representations are determined by their characters

Two representations of $G$, $\rho, V$ and $\sigma, W$ are isomorphic if and only if $\chi_{\rho} = \chi_{\sigma}$.

---

Finally, we get a decomposition theorem for $\mathbb{C}[G]$.

##### _theorem:_ irreducible decompositions of complex group algebras

Suppose $\lambda, \mathbb{C}[G]$ is the regular representation of $G$. Then
1) $\chi_{\lambda} = \# G 1_{G}$ or equivalently, $\chi_{\lambda}(g) = \begin{cases} \# G & g = 1 \\ 0. \end{cases}$
2) $\chi_{\lambda} = \sum_{\sigma \in \widehat{G}} d_{\sigma} \chi_{\sigma}$ where $d_{\sigma}$ is the dimension of the irreducible representation $\sigma$.
3) $\#G = \sum_{\sigma \in \widehat{G}} d_{\sigma}^{2}$
4) $\bigoplus_{\sigma \in \widehat{G}} \sigma^{\oplus d_{\sigma}} = \lambda$.

###### _proof:_

1) For the identity this is obvious. For other $g \in G$, notice that for $h \in G \subseteq \mathbb{C}[G]$, $g \cdot h = gh$ never has any component in the $h$ direction unless $g = 1$.
2) Since $\chi_{\lambda}$ only has component along $1$, we have $\left< \chi_{\lambda}, \chi_{\sigma} \right> = (\operatorname{Tr} \lambda(1)) (\operatorname{Tr} \sigma(1)) = \#G d_{\sigma}$. Thus, $n_{\sigma} = d_{\sigma}$.
3) Take the norm of $\chi_{\lambda}$.
4) Follows immediately from (2).

---

### Character tables

One useful tool is character tables.

##### _example:_ the character table of $\mathfrak{S}_{3}$

We already know what the irreducible representations are. Let $\rho_{1}$ be trivial, let $\rho_{2}$ be the sign representation, and let $\rho_{3}$ be the $2$-dimensional representation. Let $\chi_{1}, \chi_{2}, \chi_{3}$ be the corresponding characters. Then we have the following coefficients in the standard basis of $\mathbb{C}[\mathfrak{S}_{3}]$.

|            | $e$ | $(1 \, 2\, 3)$ | $(1\, 3 \, 2)$ | $(1 \, 2)$ | $(2 \, 3)$ | $(1 \, 3)$ |
| ---------- | --- | -------------- | -------------- | ---------- | ---------- | ---------- |
| $\chi_{1}$ | $1$ | $1$            | $1$            | $1$        | $1$        | $1$        |
| $\chi_{2}$ | $1$ | $1$            | $1$            | $-1$       | $-1$       | $-1$       |
| $\chi_{3}$ | $2$ | $-1$           | $-1$           | $0$        | $0$        | $0$        |

We can make this more compact by just writing just the conjugacy classes. One just has to be careful to weight each conjugacy class by its size when computing inner products.

|                | $e$ | $(1 \, 2\, 3)$ | $(1 \, 2)$ |
| -------------- | --- | -------------- | ---------- |
| $\chi_{1}$     | $1$ | $1$            | $1$        |
| $\chi_{2}$     | $1$ | $1$            | $-1$       |
| $\chi_{3}$<br> | $2$ | $-1$           | $0$        |
Notice, even without any weighting, the columns of this table are orthogonal with respect to the usual inner product, and that the table is square. Both of these are always true and we will prove this.

It's very useful to have this at hand. If we have the character table, we could quickly compute, that the permutation representation $\rho$ satisfies $\rho = \rho_{1} \oplus \rho_{3}$ by noticing that $\chi_{\rho} = \chi_{1} \oplus \chi_{2}$ (or just computing coefficients with respect to the orthonormal basis of $\chi_{i} / \# G$).

Similarly, for the regular representation $\lambda$ we can see that $\chi_{\lambda} = \chi_{1} + \chi_{2} + \chi_{3}$ and so $\lambda = \rho_{1} \oplus \rho_{2} \oplus \rho_{3}$.

---