---
tags:
- robert-cass
- alg-geo
- cx-geo
---

### Riemann–Hilbert over $\mathbb{C}$

The Riemann–Hilbert correspondence over $\mathbb{C}$ concerns solutions to differential equations over complex manifolds.

##### _example:_ the complex logarithm

Consider the differential equation $f' = a f / z$ on the punctured plane $\mathbb{C}^*$. This has the "solution" $f = c z^a$ but if $a \not\in \mathbb{Z}$, this is not defined everywhere on $\mathbb{C}^*$. Rather, this is only well-defined on simply-connected open subsets $U \subseteq \mathbb{C}^*$

In fact, the assignment $\mathscr{L}(U) = \{ f : U \to \mathbb{C} \mid f' = a f / z \}$ is a [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf, separated presheaf|sheaf]] of vector spaces.

---

In fact, this is nicer than a sheaf — it is a local system. This will be the first thing we need to define.

##### _definition:_ local system

A **local system** is a sheaf on $X$ such that for small enough simply connected $U \subseteq X$, we have $\mathscr{F}(K) = \mathscr{F}(U)$ for all connected open subsets $K \subseteq U$.

---

##### _theorem:_ Riemann–Hilbert correspondence (Deligne)

Let $X$ be a smooth complex algebraic variety, there is an equivalence of categories between algebraic differential equations on $X$ with regular singularities and the category of local systems on $X$.

---

To do this, we need a generalisation of local systems.

##### _definition:_ constructible sheaves

A **constructible sheaf** is a sheaf that restricts to a local system on some stratification of $X$.

---

The important example to think of here is extending the sheaf $\mathscr{L}$ (defined earlier) to $\mathbb{C}$.

##### _example:_ extension by zero

Consider the inclusion $i : \mathbb{C}^* \to \mathbb{C}$. Then 
$$
i_{!}(\mathscr{L})(U) = \begin{cases}
\mathscr{L}(U) & U \subseteq \mathbb{C}^* \\
0
\end{cases}
$$
is a constructible sheaf on $\mathbb{C}$.

---

We also want to be able to think of our solutions algebraically instead of as solutions of differential equations.

##### _example:_ differential equations are just $\operatorname{Hom}_{\mathscr{D}_{X}}(\mathscr{F}, \mathscr{O}_{X}^\text{an})$

---


Finally, we need to pass to the derived category.

##### _example:_ use $\operatorname{Ext}^1$ not $\operatorname{Hom}$

---

Now we can get the full version of Riemann–Hilbert as proved by Kashiwara.

##### _theorem:_ Riemann–Hilbert correspondence (Kashiwara)

There is an equivalence of categories between the derived category of regular holonomic $\mathscr{D}$-modules on $X$ and the derived category of constructible (sheaves of) vector spaces on $X$.

The functor from left to right is $\mathscr{F} \mapsto \operatorname{Hom}_{\mathscr{D}_{X}}(\mathscr{F}, \mathscr{O}_{X}^\text{an})$.

---

### Riemann–Hilbert in characteristic $p$

In characteristic $p$ we don't have an obvious choice of differential operator. Instead we work with the Frobenius $p$-power operator in $\mathscr{O}_{X}[F]$.

##### _definition:_ the Frobenius operator, $\mathscr{O}_{X}[F]$

The **Frobenius operator** is an element $F$ of the ring $\mathscr{O}_{X}[F]$ with $F \cdot a = a^p F$.

---

Note that this is a ring since $(a + b)^p = a^p + b^p$.

Then it is a theorem that the same thing works!

##### _theorem:_ (Emerton–Kisin and also Bhatt–Lurie)

There is an equivalence categories between holonomic $\mathscr{O}_{X}[F]$-modules and perverse sheaves.

Suppose $X$ is a smooth variety and $Y \subseteq X$ is a (possibly non-smooth) subvariety. Then there is an irreducible perverse sheaf $\mathscr{IC}_{Y}$ supported on $Y$ such that the restriction to the smooth locus $\mathscr{IC}_{Y \mid Y^\text{sm}}$ is just $\underline{\mathbb{F}_{p}}$.

---

What are perverse sheaves? Complexes of sheaves.

The main theorem of this talk characterises when the $\mathscr{IC}$ perverse sheaf is indeed constant.

##### _theorem:_ (Cass and Lourenço)

Let $X$ be a (possibly non-smooth) connected $\mathbb{F}_{p}$-variety. Then $\mathscr{I C}_{X}$ is the constant sheaf $\underline{\mathbb{F}_{p}}$ if and only if the [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ stalks, germs|stalks]] $\mathscr{O}_{X, p}$ of the structure sheaf are $F$-nilpotent rings

---

What then is $F$-nilpotence?

Let $A$ be a (commutative, unital) Noetherian local ring with unique maximal ideal $\mathfrak{m}$. 

Then for any $A$-module $N$ define
$$
\Gamma_{\mathfrak{m}} (N) = \{ x \in N \mid \mathfrak{m}^a \cdot x = a, a \gg 0 \}.
$$

Then the **local cohomology groups** $H^i_{\mathfrak{m}}(N)$ are the derived functors of $\Gamma_{\mathfrak{m}}$ (whatever that means.)

$A$ is then $F$-nilpotent if there is some $n > 0$ such that $F^n(H^i_{\mathfrak{m}}(A)) = 0$ for all $i < \dim A$ and $H^{\dim A}_{\mathfrak{m}}(A) / \ker F^n$ is an irreducible $A[F]$ module for all sufficiently large $n$.

##### _example:_ an $F$-nilpotent ring (Blickle)

$\mathbb{F}[[x, y, z]] / (x^4 + y^4 - z^4)$ is $F$-nilpotent if and only if $\mathbb{F}$ has characteristic $p = 3 \pmod{4}$.