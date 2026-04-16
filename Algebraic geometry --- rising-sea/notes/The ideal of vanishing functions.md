---
tags:
- rising-sea/3/7
- alg-geo
- comm-alg
---

Let $A$ be a ring.

The [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition, proposition _ the Zariski topology (is a topology)|Zariski topology]] on an affine scheme $\operatorname{Spec} A$ gives a closed set of vanishing points for each ideal $\mathfrak{i} \subseteq A$, and in fact, [[Algebraic geometry --- rising-sea/notes/Affine schemes#_proposition _ vanishing sets uniquely identify only radical ideals|uniquely identifies these ideals up to radicals]]. It turns out that each Zariski closed subset determines an ideal of functions vanishing on it, and thus, we have a bijection between closed sets and radical ideals. We can further extend this to give a bijection between the [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#_definition _ irreducibility, reducible|irreducible]] closed subsets and minimal prime ideals.

##### _example:_ the ideal function on the affine plane

Let $A = \mathbb{F}[x, y]$ and $S = \{ (y), (x, y - 1) \}$ (corresponding to the $x$-axis and the point $(0, 1)$ in $\mathbb{F}^{2}$). Then the polynomials vanishing at (all points of) $S$ are just the polynomials contained in both ideals (by definition) and thus, form the ideal $(x, y - 1) \cap (y) = (xy, y(y - 1))$.

---

##### _definition:_ the ideal of vanishing functions

Given a subset $S \subseteq \operatorname{Spec} A$, the **ideal of vanishing functions** on $S$ is the set of all functions vanishing at each point of $S$. It is denoted $I(S)$ and is given by
$$
I(S) = \bigcap_{\mathfrak{p} \in S} \mathfrak{p} \subseteq A.
$$

---

Note that when $S$ is empty, the intersection is empty, and thus all of $A$. This is reasonable — for every function $f \in A$ there is no point $\mathfrak{p} \in S$ with $f \not\in \mathfrak{p}$.

##### _example:_ the ideal of functions vanishing on the $x$, $y$, and $z$-axes

Let $S = \{ (x, y), (y, z), (z, x) \} \subseteq \mathbb{A}_{\mathbb{C}}^{3}$. Then we claim $I(S) = (xy, yz, zx)$. Clearly $(xy, yz, zx) \subseteq (x, y) \cap (y, z) \cap (z, x)$.

---

We make some observations.

##### _proposition:_ the ideal of vanishing functions is an ideal

$I(S)$ is an ideal of $A$.

###### _proof sketch:_

The intersection of ideals is an ideal.

---

##### _proposition:_ the ideal function is inclusion reversing

If $S_1 \subseteq S_{2}$, then $I(S_{2}) \subseteq I(S_{1})$.

###### _proof sketch:_

$I(S_{2})$ is the intersection of more prime ideals.

---

##### _proposition:_ the ideal function doesn't care about closures

Let $\overline{S}$ be the Zariski [[Topology --- math-147/notes/Limit points and closed sets#_definition _ closure, closed|closure]] of $S$. Then $I(\overline{S}) = I(S)$.

###### _proof:_

Since $S \subseteq \overline{S}$, we have $I(\overline{S}) \subseteq I(S)$. We show the other direction.

Suppose $f \in I(S)$. The set of all points where $f$ vanishes is the closed set $V(f)$. Thus, we must have $S \subseteq V(f)$. But then since the [[Topology --- math-147/notes/Limit points and closed sets#_proposition _ the closure is the smallest closed set|closure is the smallest closed set]] containing $S$, we have $\overline{S} \subseteq V(f)$, and thus, $f \in I(\overline{S})$ as well.

---

In combination with the fact that $V$ doesn't care about radical signs, the fact that $I$ doesn't care about closures gives a correspondence between closed sets and radical ideals. (Note that we need to show that $I(S)$ is always radical).

##### _proposition:_ Zariski closed sets are in bijection with radical ideals

$V : \sqrt{ \mathfrak{i} } \to V(\sqrt{ \mathfrak{i} })$ and $I : V(\mathfrak{i}) \mapsto I(V({ \mathfrak{i} })) = \sqrt{ \mathfrak{i} }$ (note, we need to show the last equality) are inverse functions giving an inclusion-reversing bijection between closed sets of $\operatorname{Spec} A$ and radical ideals of $A$.

###### _proof:_

$V$ is [[Algebraic geometry --- rising-sea/notes/Affine schemes#_proposition _ vanishing sets uniquely identify only radical ideals|injective on radical ideals]] ($V(\sqrt{ \mathfrak{i} }) = V(\sqrt{ \mathfrak{j} }) \iff \sqrt{ \mathfrak{i} } = \sqrt{ \mathfrak{j} }$), and [[Algebraic geometry --- rising-sea/notes/Affine schemes#_proposition _ vanishing sets uniquely identify only radical ideals|radical ideals surject onto all closed sets]] ($V(\mathfrak{i}) = V(\sqrt{ \mathfrak{i} })$). It only remains to show that $I(V({\mathfrak{i}})) = \sqrt{ \mathfrak{i} }$. But $I(V(\mathfrak{i}))$ is the intersection of all primes in $V(\mathfrak{i})$, which is the intersection of all primes containing $\mathfrak{i}$, [[Algebraic geometry --- rising-sea/notes/Radicals of ideals#_proposition _ the radical is the intersection of all primes containing the ideal|which is the radical]] $\sqrt{ \mathfrak{i} }$.

---

The result above is sometimes called Hilbert's Nullstellensatz, but we reserve that for [[Algebraic geometry --- rising-sea/notes/Hilbert's Nullstellensatz#_theorem _ Hilbert's (strong) Nullstellensatz or Zariski's lemma|a more specific result]] about maximal ideals of $\mathbb{F}[x_{1}, \dots, x_{n}]$.

##### _example:_ $I \circ V$ is not the identity on general ideals

Let $\mathfrak{j} = (x^{2} + y^{2} - 1, y - 1) \subseteq \mathbb{C}[x, y]$. Notice that $x^{2} = x^{2} + y^{2} - 1 - (y + 1)(y  - 1) \in \mathfrak{j}$.

Consider $I(V(\mathfrak{j})) = \sqrt{ \mathfrak{j} }$. Since $x^{2} \in \mathfrak{j}$, we have $x \in \sqrt{ \mathfrak{j} }$.

We claim $x \not\in \mathfrak{j}$. Note that $\mathfrak{j} = (x^{2}, y - 1)$. If $x = p(x, y) x^{2} + q(x, y) (y - 1) \in \mathfrak{j}$, we must have $q(x, y) = -x$ in order to have any pure $x$ term of degree $1$. But then we can't have $p(x, y) x^{2} - xy = 0$ since $p$ only adds to the $x$-degree.

---

##### _proposition:_ irreducible Zariski closed sets are in bijection with prime ideals

$V : \mathfrak{p} \to V(\mathfrak{p})$ and $I : V(\mathfrak{p}) \mapsto I(V(\mathfrak{p}))$ are inverse functions giving an inclusion-reversing bijection between irreducible closed sets of $\operatorname{Spec} A$ and prime ideals of $A$.

###### _proof:_

$V$ is injective on primes (since primes are radical). Primes also surject onto irreducible closed subsets. This is because $V(\mathfrak{i}) \cong \operatorname{Spec} A / \mathfrak{i}$ is irreducible [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#_proposition _ an algebraic characterisation of irreducible affine schemes|if and only if]] $\mathfrak{N}_{A / \mathfrak{i}} = \sqrt{ \mathfrak{i} } / \mathfrak{i}$ is prime. Then $\sqrt{ \mathfrak{i} }$ is prime, so $V(\mathfrak{i}) \cong V(\mathfrak{p})$. $I(V(\mathfrak{p})) = \mathfrak{p}$ since primes are radical.

---

##### _corollary:_ irreducible components are in bijection with minimal prime ideals

###### _proof sketch:_

The bijection is inclusion-reversing so maximal and minimal elements are interchanged

---
##### _corollary:_ irreducible closed sets have unique generic points

###### _proof sketch:_

For $Z \subseteq \operatorname{Spec} A$, choose $\mathfrak{p} = I(Z)$. Then $V(\mathfrak{p}) = Z$. The generic point $\mathfrak{p}$ is unique — $V$ is injective on primes.

---

##### _corollary:_ a [[Algebraic geometry --- rising-sea/notes/Noetherian rings and modules#_definition _ Noetherian rings|Noetherian ring]] has a finite number of minimal prime ideals

###### _proof:_

Let $A$ be Noetherian. Then $\operatorname{Spec} A$ is a [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#_definition _ Noetherian topological spaces|Noetherian space]] and [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#_proposition _ Noetherian spaces break up into finitely many irreducible components|has finitely many irreducible closed subsets]]. Thus, $A$ has finitely many minimal prime ideals.

---

We should check that this is reasonable in reasonable circumstances (say over a polynomial ring).

##### _example:_ minimal prime ideals of finite $\mathbb{F}$-algebras or irreducible components of affine varieties

Let $A = \mathbb{F}[x_{1}, \dots, x_{n}]$ and $f \in A$. The subset $\operatorname{Spec} A / (f) \cong V(f) \subseteq \operatorname{Spec} A$ has irreducible components corresponding to the irreducible factors of $f$. This is essentially because $A$ is a [[Abstract algebra --- math-171/notes/Unique factorisation#_definition _ unique factorisation domains|unique factorisation domain]]. In such a ring irreducibles are [[Abstract algebra --- math-171/notes/Unique factorisation#_examples _ irreducible and prime elements|prime elements]]. 

Suppose $f = g_{1} \cdots g_{n}$. Write $f = g_{i} h_{i}$. Then $(f) \subseteq (g_{i})$ for each $i$. If we had $(f) \subseteq \mathfrak{g} \subseteq (g_{i})$, we would have $f = g h$ and $g = g_{i} h'_{i}$, a factorisation $f = g_{i} h_{i}' h$ as opposed to $f = g_{i} h_{i}$. Thus, $h_{i}' h$ differs from $h_{i}$ by a unit. A little work shows that either $(f) = (g)$ or $(g) = (g_{i})$. Either way, $(g_{i})$ is a minimal prime containing 

>[! warning]
> assumes $A$ is principal which may be generally false (maybe sandwiching between principals helps)

For example, the minimal prime ideals of $\mathbb{F}[x, y] / (xy)$ are $(x)$ and $(y)$.

---