---
tags:
- alg-geo
- uc-2026/conics/1
- uc-2026/conics/2
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

This gives us naive and incorrect counts because $\mathbb{P}^5$ contains degenerate conics too. We can't just cut out the degenerate conics because the resulting space is not proper. Thus, we will have to do blow ups to get what we want.