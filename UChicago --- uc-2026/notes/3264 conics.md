---
tags:
- alg-geo
- uc-2026/conics/1
- uc-2026/conics/2
- uc-2026/conics/3
- altan-erdnigor
---

Enumerative geometry is concerned with questions like the following. In the plane we can ask how many lines pass through two general points (there is one), how many circles pass through three general points (there is one), how many conics pass through five general points (there is one), or how many. In $3$-space we can ask how many lines pass through four general lines (there are two).

The question we are concerned with was asked by Steiner (1848) — how many conics are tangent to five general conics? Schubert gave an (unrigorous) answer to this and many other questions through Schubert calculus. In particular Chasles (1864) — there are $3264$ conics tangent to five general conics.

We will use 19th century methods. In particular, we will use no schemes.

### Quadrics and conics

We work over $\mathbb{C}$ always.

##### _definition:_ quadrics

A **quadric** $Q = V(f) \subseteq \mathbb{P}^n$ is the vanishing subvariety defined by a homogeneous quadratic polynomial $f$.

---

##### _definition:_ conics

A **conic** $C \subseteq \mathbb{P}^{2}$ is a curve that is isomorphic to $\mathbb{P}^1$.

---

Note, by the diagonalisation of [[Quadratic forms and K-theory --- pcmi-2021/notes/Diagonalisation of quadratic forms#_corollary _ diagonalising quadratic forms over $ overline{ mathbb{F}}$ and $ mathbb{R}$|quadratic forms over ]]$\mathbb{C}$, quadrics are classified by their rank — the maximal subspace of $\mathbb{C}^n$ where they are non-degenerate.

##### _proposition:_ quadrics in the projective plane

Let $f$ be a homogeneous quadratic polynomial in $\mathbb{C}[x_{1}, x_{2}, x_{3}]$ cutting out a quadric curve $C \subseteq \mathbb{P}^{2}$
- if $\operatorname{rank} f = 3$, then $C \cong \mathbb{P}^1$.

###### _proof:_

Suppose $\operatorname{rank} f = 3$. Then there is a linear change of coordinates that allows us to write $f(x) = x_{0} x_{2} - x_{1}^{2}$. Then there is an isomorphism $C \to \mathbb{P}^1$ given by
$$
(x_{0} : x_{1} : x_{2}) \mapsto \begin{cases}
(x_{0} : x_{1}) & x_{0} \neq 0 \\
(x_{1} : x_{2}) & x_{2} \neq 0.
\end{cases}
$$
It has inverse $(y_{0} : y_{1}) \mapsto (y_{0}^{2} : y_{0} y_{1} : y_{1}^{2})$. This is a special case of the [[Algebraic geometry --- rising-sea/notes/Morphisms of graded rings and projective schemes#Veronese subrings|Veronese embedding]]. Note also, this gives

Suppose $\operatorname{rank} f = 2$. Then there is a linear change of coordinates such that $f(x) = x_{1} x_{2}$ and thus $C$ is an irreducible union of $2$ conics. (It's clear that $V(x_{1}) \cong \mathbb{P}^1$).

If $\operatorname{rank} f = 1$, then we can write $f(x) = x_{0}^{2}$. Thus, $C$ is a [[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_definition _ reduced (schemes)|non-reduced]] thickening of a conic.

---

We call the latter two degenerate conics. We will see that the moduli space of all conics in $\mathbb{P}^{2}$ is just $\mathbb{P}^5$ and that there are loci $\Delta_{2} \supseteq \Delta_{1}$ of non-degenerate and reduced conics respectively.

### Some naive counts

##### _proposition:_ the tangent curves

Let $L \subseteq \mathbb{P}^{2}$ be a (projective) line. Consider $\mathbb{P}^5$ as the moduli space of all conics $C \subseteq \mathbb{P}^{2}$ and let $T_{L} \subseteq \mathbb{P}^5$ be the subset of those $C$ such that $L$ is tangent to $C$ in $\mathbb{P}^{2}$. 

Then $T_{L}$ is a quadric. 

###### _proof sketch:_

Assume general equations $L = V(x_{2})$ and $C = V(f)$ such that $f(x_{0}, x_{1}, 0)$ is general. Then tangency of $L$ to $C$ is a quadric condition on the coefficients of $f(x_{0}, x_{1}, 0)$.

---

Dual projective space parameterises hyperplanes. Thus, the dual projective plane parameterises projective lines in $\mathbb{P}^{2}$ which is exactly what we want to understand tangency.

##### _definition:_ dual projective space

**Dual projective space** $\check{\mathbb{P}}^n$ is the moduli space of hyperplanes in $\mathbb{P}^n$.

---

Note $\check{\mathbb{P}}^n \cong \mathbb{P}^n$.

Thus, for each conic, we can define a dual conic. It will turn out to actually be a conic in $\check{\mathbb{P}}^{2}$.

##### _definition:_ dual conic

The **dual conic** to a conic $C \subseteq \mathbb{P}^{2}$ is $\check{C} = \{ L \mid L \text{ tangent to } C \}$.

---

##### _proposition:_ the dual conic is a conic

Given a conic $C \subseteq \mathbb{P}^{2}$, the dual conic $\check{C} \subseteq \check{\mathbb{P}}^{2}$ is a (smooth) conic.

###### _proof:_

Suppose $C = V(x_{0} x_{2} - x_{1}^{2})$. Then for a line $L = V(a_{0} x_{0} + a_{1} x_{1} + a_{2} x_{2})$ corresponding to $(a_{0} : a_{1} : a_{2}) \in \check{\mathbb{P}}^{2}$, the tangency of $L$ and $C$ is the condition that $a_{1}^{2} - a_{0} a_{2} = 0$. This is just a smooth conic!

---

##### _proposition:_ the sextic of tangent conics

Let $C_{0} \subseteq \mathbb{P}^{2}$ be a conic 

---

This gives us naive and incorrect counts because $\mathbb{P}^5$ contains degenerate conics too. In particular, non-reduced conics have intersection multiplicity $2$ at every intersection with every conic and every line. For example, we should think that the number of conics tangent to five given conics is $\# T_{C_{1}} \cap \dots \cap T_{C_{5}}$, but this is $6^5 = 7776$ which the title of this talk tells us incorrect

We can't just cut out the degenerate conics because the resulting space is not proper. In particular, Bezout's theorem does not apply. Thus, we will have to do blow ups to get what we want.

### The moduli space of complete conics

Here we will always think of $\mathbb{P}^5$ as the moduli space of conics, and equivalently, as the moduli space of symmetric $3 \times 3$ matrices up to scaling.

##### _proposition:_ locus of non-reduced conics is a local complete intersection

$\Delta_{1} \subseteq \mathbb{P}^5$ is a local complete intersection.

###### _proof sketch:_

It suffices to show that $\Delta_{1}$ is cut out by equations in a local neighbourhood of $A = \begin{pmatrix} 1 & & \\ & 0 & \\ & & 0 \end{pmatrix}$. It suffices to show that all $2 \times 2$ minors vanish

---

##### _definition:_ moduli space of complete conics

The **moduli space of complete conics** is $M = \operatorname{Bl}_{\Delta_{1}} \mathbb{P}^5$ (the moduli space of all conics, [[UChicago --- uc-2026/notes/Blowups of local complete intersections#_definition _ blowups of local complete intersections|blown up]] at the locus of non-reduced conics).

---

The way this helps is that now the [[UChicago --- uc-2026/notes/Blowups of local complete intersections#_definition _ blowups of local complete intersections, exceptional divisor, proper transform|proper transform]] of two different $T_{C}, T_{C'}$ do not necessarily intersect on the exceptional divisor. In fact, we will show that the intersection of five different $T_{C}$s with the exceptional divisor is empty.

We can give a global description of $M$.

##### _proposition:_ global descriptions of the moduli of space of complete conics

Consider the [[Algebraic geometry --- rising-sea/notes/Rational maps|rational map]] $\mathbb{P}^5 \dashrightarrow \mathbb{P}^5$ by $A \mapsto \operatorname{adj} A$ (on the $5$-dimensional locus where $A$ is invertible, this is $A \mapsto A^{-1} \det A$). Then $M = \overline{\Gamma_{\varphi}} \subseteq \mathbb{P}^5 \times \mathbb{P}^5$ where $\Gamma_{\varphi}$ is the graph of $\varphi$.

Equivalently $M = \{ (A, B) \in \mathbb{P}^5 \times \mathbb{P}^5 \mid A B = \lambda \operatorname{id}_{\mathbb{C}^3} \}$.

###### _proof sketch:_

This is only a vague idea of the proof.

Call the three different descriptions (blowup, graph of rational map, matrices) $M_{1}, M_{2}, M_{3}$ resepctively.

Use the local complete intersection description of $\Delta_{1}$ to get a closed embedding $M_{1} \subseteq \mathbb{P}^5 \times \mathbb{P}^5$. Then using three different projections $\mathbb{P}^5 \times \mathbb{P}^5 \to \mathbb{P}^5$ onto the first factor, you get three different maps $M_{i} \to \mathbb{P}^5$. Then check that they all satisfy the universal property.

---

It turns out that $M$ is actually symmetric in these two projections — the last description tells us that $M$ is symmetric in the two matrices. In particular, we actually have two different exceptional divisors $E_{1}, E_{2}$ on $M$ and we can cut them out in different combinations.

##### _theorem:_ $3264$ conics

There are $3264$ conics tangent to $5$ generally given conics.

###### _Chasles' proof:_

Let $\Sigma \subseteq M$ be a $1$-parameter family of conics. Let $p \in \mathbb{P}^{2}$ and let $L \subseteq \mathbb{P}^{2}$ be a line. Let $\mu$ be the locus of conics in $\Sigma$ containing $p$ and let $\nu$ be the locus of conics in $\Sigma$ tangent to $L$. Note that for general $p, L$ these shouldn't depend on $p, L$.

Then for any degree $d$ curve, we claim that the number of conics in $\Sigma$ tangent to $Z$ is $d(d - 1) \mu + d \nu$. For $Z$ a conic this is $2(\mu + \nu)$. This is where Schubert calculus comes in. The idea is that we want to evaluate "$(2 (\mu + \nu))^5$" and we can do so by assigning enumerative meaning to each monomial in the expansion. Of course we are not really evaluating the numbers $\mu^5$ or $\mu^3 \nu^{2}$ — we are just taking intersections in cohomology in some sense. Note that in the interpretations of $\mu^5$ et c. we drop the assumption that $C \in \Sigma$. Then this is just counting.
$$
\mu^5 = \# \{ C \in M \mid C \ni p_{1}, \dots, p_{5} \} = 1
$$
since there is a unique conic containing $5$ points.
$$
\mu^4 \nu = \# \{ C \in M \mid C \ni p_{1}, \dots, p_{4}, C \text{ tangent to } L \} = 2
$$
since there are two possible points where a conic can be tangent to. Finally
$$
\mu^3 \nu^{2} = 4
$$
since this is essentially the intersection $T_{L_{1}} \cap T_{l_{2}} \cap \mathbb{P}^{2}$ which is just intersecting two conics in $4$ points in $\mathbb{P}^{2}$. The rest are the same by point-line duality in projective space.

Then
$$
(2(\mu + \nu))^5 = 32 (1 + 5 x 2 + 10 \times 4 + 10 \times 4 + 5 \times 2 + 1) = 3264.
$$

###### _proof by cohomology:_

Let $E_{1}, E_{2}$ be the two exceptional divisors corresponding to the two projections $\pi_{1}, \pi_{2} : M \to \mathbb{P}^{5}$. Then we claim $2 \pi_{1}^*[H_{1}] = \pi_{2}^* [H_{2}] + [E]$ where $H_{1}, H_{2}$ are the hyperplane divisors. This essentially follows by considering the $\varphi : \mathbb{P}^5 \dashrightarrow \mathbb{P}^5$ that makes the diagram commute. Note $\varphi^*$ turns the hyperplane section $H_{2}$ into a quadric.

Then we claim that the class of the proper transform of $T_{L}$ is $[\widetilde{T_{L}}] = 2 \pi^*_{1} [H] - [E] = \pi_{2}^*[H]$. Thus, we get rid of the $2$ that we had in $[T_{L}]^5$ and get $[\widetilde{T_{L}}]^5 = 1$. Similarly, $[\widetilde{T_{C}}] = 6 \pi^*[H] - 2[E] = 2(\pi_{1}^*[H_{1}] + 2 \pi_{2}^*[H_{2}])$. But then this is exactly what we want to talk about. The computation of the monomials is exactly the same as what we wanted. To see that they are in fact the same, think of the second copy of $\mathbb{P}^5$ as dual projective space. Then $[H_{1}] = [I_{p}]$ where $I_{p}$ is the locus of conics passing through a point (since this is a linear condition on the coefficients of the conic). Also, $[H_{2}] = [I_{\ell}]$ where $\ell$ is the point corresponding to tangency through some line $\ell$ in non-dual projective space.

---