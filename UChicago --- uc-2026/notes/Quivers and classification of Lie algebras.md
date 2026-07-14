---
tags:
- uc-2026/quiver
- alg
- victor-ginzburg
---

This is a talk about a theorem that is really easy to state and really hard to prove.

Fix a field $\mathbb{F}$.

##### _definition:_ quivers, quiver representation, morphisms of representations

A **quiver** is a directed graph (with multiple and self edges allowed). Essentially, a quiver is a minimal Hasse diagram of a small category.

A **representation of a quiver** $Q$ (over $\mathbb{F}$) is a functor $\rho : Q \to \mathsf{finVec}_{\mathbb{F}}$ into the category of finite dimensional vector spaces (a diagram of finite vector spaces in the shape of $Q$). 

A **morphism of representations** is a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformation]] of the corresponding functors. An **isomorphism** is a natural isomorphism.

---

We are interested in the (simply laced) Dynkin diagrams. They classify simple Lie algebras, finite subgroups of $\mathrm{SL}_{2}(\mathbb{C})$, and of course, their own quiver representations.

##### _definition:_ (simply laced) Dynkin diagrams

The **(simply laced) Dynkin diagrams** are non-directed graphs comprising.
- $A_{n}$: the $n$-vertex tree with all but two vertices having degree $2$, for all $n \geq 1$
- $D_{n}$: the $n$-vertex tree with $n - 2$ vertices forming an $A_{n - 2}$ and two leaves adjoined to the $(n - 2)$th vertex.
- $E_{6}$, $E_{7}$, $E_{8}$: the $n$-vertex trees with $6$ vertices forming an $A_{n - 1}$ with one leaf adjoined to the third vertex

---

We sketch one direction of the following result of Gabriel.

##### _theorem:_ Dynkin diagrams are exactly finite type quivers

Suppose $\mathbb{F}$ is an algebraically closed field and $Q$ is a connected quiver. Then the underlying graph of $Q$ is a simply laced Dynkin diagram if and only if each assignment of objects $d: \operatorname{obj} Q \to \operatorname{obj} \mathsf{finVect}_{\mathbb{F}}$ corresponds to finitely many isomorphism classes of representations.

###### _proof sketch:_

We will consider dimension assignments $d : \operatorname{obj} Q \to \operatorname{obj} \mathsf{finVect}_{\mathbb{F}}$ giving $d_{i} \in \mathbb{Z}$ for each $i$. We can then construct for each $d$ a vector space $\operatorname{Rep}(Q, d) = \prod_{a : i \to j} \operatorname{Hom}(\mathbb{F}^{d_{i}}, \mathbb{F}^{d_{j}})$ and a group $G = \prod_{i \in \operatorname{obj} Q} \mathrm{GL}_{d_{i}}(\mathbb{F})$. Then $G$ acts on $\operatorname{Rep}(Q, d)$ by component-wise conjugation. In particular, for $a : i \to j$ we have $g \circlearrowright \rho(a)$ by $g_{j} \circ \rho(a) \circ g_{i}^{-1}$

Then classifying quiver representations of $Q$ is exactly the same as understanding this action of $G$. In particular, it suffices to enumerate the [[Abstract algebra --- math-171/notes/Group actions#_definition _ orbit|orbits]] in $\operatorname{Rep}(Q, d)$.

Suppose $Q$ is a connected graph with no edge-loops. Write $n = \# \operatorname{obj} Q$ and $n_{ij} = \# \operatorname{Mor}(i, j)$. Choose a standard basis of $\mathbb{R}^{\oplus n}$ where $e_{i}$ corresponds to object $i \in Q$. Define a symmetric bilinear form on $\mathbb{R}^{\oplus n}$
$$
\beta_{Q}(e_{i}, e_{j}) = \begin{cases}
2 & i = j \\
-n_{ij}.
\end{cases}
$$
Note, $\beta_{Q}(v, v) = 2 \sum_{i \in Q} v_{i}^{2} - \sum_{i \neq j} n_{ij} x_{i} x_{j}$.

The idea is to prove that finitely many isomorphism classes implies $\beta_{Q}$ is positive definite, which implies $Q$ is Dynkin. We don't have time to prove the latter implication.

Note $\dim \operatorname{Rep}(Q, d) = \sum_{a : i \to j} d_{i} d_{j} = \sum_{i, j} n_{ij} d_{i} d_{j}$.

We claim that if $G$ has finitely many orbits, then there exists an open orbit $U \subseteq \operatorname{Rep}(Q, d)$. In particular, $\dim U = \dim \operatorname{Rep}(Q, d)$.

We can also compute the dimension in a different way. Choose $p \in U$ and let $\operatorname{stab}_{G} p$ be its [[Abstract algebra --- math-171/notes/Group actions#_definition _ stabiliser, free|stabiliser]]. Then $\dim U = \dim G - \dim \operatorname{stab}_{G} p$ by some generalisation of the orbit stabiliser theorem. For any $\lambda \in \mathbb{F}^\times$, we have $\lambda \operatorname{id} \in \operatorname{stab}_{G} p$. Thus, $\operatorname{stab}_{G} p$ is at least $1$-dimensional. Also $\dim G = \sum_{i \in Q} d_{i}^{2}$. Thus,
$$
\sum_{i, j} n_{i, j} d_{i} d_{j} \leq \sum_{i \in Q} d_{i}^{2} - 1
$$
This gives positive definiteness for integers, which extends to rationals by dividing, and then to positive definiteness for all reals by some continuity argument.

---

##### _example:_ a non-finite type quiver 

Consider $Q$ the connected graph with one vertex of degree $4$ and the rest of degree $1$.

Assign dimension $1$ vector spaces to all the degree $1$ vertices. Assign a dimension $2$ vector space to the central vertex.

Assume all the. Let $\ell_{i}$ be the line defined be the image of the $i$th dimension $1$ vector sapce.

Any four lines $\ell_{1}, \dots, \ell_{4}$ in $\mathbb{F}^{\oplus 2}$ have a cross ratio defined as follows. Let $x_{i}$ be unique point at which $\ell_{i}$ intersects $y = 1$. Then the cross ratio is
$$
[\ell_{1}, \dots, \ell_{4}] =  \frac{(x_{1} - x_{2})(x_{3} - x_{4})}{(x_{1} - x_{4})(x_{3} - x_{2})}.
$$
This is $\mathrm{GL}$ invariant by classical projective geometry (fractional linear transformations preserve this formula). It can clearly take any of the infinitely many values in the algebraically closed base field $\mathbb{F}$, so we are done.


---