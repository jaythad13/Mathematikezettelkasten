---
tags:
- lin-alg
- alg
- pcmi-2021/3
---

Let $\mathbb{F}$ be a field of characteristic not $2$.

We can tensor quadratic spaces! That is, for two quadratic spaces $V, q_{V}$ and $W, q_{W}$ there is a sensible choice of quadratic space $V \otimes W, q_{V} \otimes q_{W}$.

##### _definition:_ tensor product of quadratic spaces

Let $V, q_{V} \cong \left< a_{1}, \dots, a_{m} \right>$ and $W, q_{W} \cong \left< b_{1}, \dots, b_{n} \right>$ be two quadratic spaces with diagonalisations given by bases $v_{1}, \dots, v_{m}$ and $w_{1}, \dots, w_{n}$. Then their **tensor product $V \otimes W, q_{V} \otimes q_{W}$** is given by choosing the basis of $v_{i} \otimes w_{j}$ to be orthogonal and setting $(q_{V} \otimes q_{W})(v_{i} \otimes w_{j}) \cong a_{i} b_{j}$.

---

The universal property for the tensor product of quadratic spaces is less clear than for [[Quadratic forms and K-theory --- pcmi-2021/notes/Direct sums of quadratic spaces#_proposition _ the universal property of the quadratic direct sum|direct sums]], and we have to make an ad-hoc definition

##### _proposition:_ the universal property of the quadratic tensor product

Let $V, q_{V}$, $W, q_{W}$, and $Z, q_{Z}$ all be quadratic spaces over $\mathbb{F}$. We say $T : V \times W \to Z$ is **quadratic bilinear** if each $T_{w} : V, q_{W}(w) q_{V} \to Z, q_{Z}$ by $T_{w}(v) = T(v, w)$ and $T_{v} : W, q_{V}(v) q_{W} \to Z, q_{Z}$ by $T_{v}(w) = T(v, w)$ is a [[Quadratic forms and K-theory --- pcmi-2021/notes/Quadratic forms#_definition _ (non-degenerate, symmetric) bilinear forms, quadratic forms, quadratic spaces, homomorphisms of quadratic spaces, quadratic linear map|quadratic linear map]].

Every quadratic bilinear map $V \times W \to Z$ factors as the composition of the quadratic bilinear map $t : V \times W \to V \otimes W, q_{V} \otimes q_{W}$ by $(v, w) \mapsto v \otimes w$ and a unique quadratic linear map $V \otimes W \to Z$.

###### _proof sketch:_

Given a quadratic bilinear map $T : V \times W \to Z$ we can write $T = S \circ t$ where $S(v \otimes w) = T_{v}(w) = T_{w}(v)$. Note that this is quadratic linear since $q_{Z}(T_{v}(w)) = q_{V}(v) q_{W}(w)$ and $q(v \otimes w) = q_{V}(v) q_{W}(w)$. 

$S$ is unique since it is the unique factorisation for the universal property of the tensor product in the category of vector spaces.

---