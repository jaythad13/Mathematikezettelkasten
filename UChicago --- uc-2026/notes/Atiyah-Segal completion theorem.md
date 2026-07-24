---
tags:
- alg-top
- uc-2026/alg-top/13
- peter-may
---

Let $G$ be a compact Lie group and let $\mathbb{F}$ be a field that is either $\mathbb{R}$ or $\mathbb{C}$. Let $K^\bullet$ be the corresponding topological $K$-theory.

The Atiyah–Segal completion theorem tells us that we can recover $K^0(BG)$ (and thus, [[UChicago --- uc-2026/notes/Characteristic classes#_definition _ characteristic class|characteristic classes]]) from the representation theory of $G$. To state it, we need some

##### _definition:_ representation group, representation ring

The **representation group** $\operatorname{Rep}_{\mathbb{F}} G$ of a compact Lie group is the [[Algebraic geometry --- rising-sea/notes/Adjoint functors#_example _ groupification as adjoint to forgetting|group completion]] of the commutative monoid of $\mathbb{F}$-representations of $G$ under direct sum.

The **representation ring** $\operatorname{Rep}_{\mathbb{F}} G$ is the ring with additive group given by the representation group and multiplication given by tensor product.

---

##### _definition:_ augmentation ideal

The **augmentation ideal** of a Lie group $G$ is the ideal $\mathfrak{i}_{G} \subseteq \operatorname{Rep}_{\mathbb{F}} G$. 

---

##### _theorem:_ the $0$th part of Atiyah–Segal completion

Let $R = \operatorname{Rep}_{\mathbb{F}} G$ and let $\mathfrak{i}$ be its augmentation ideal. Then $R_{\widehat{\mathfrak{i}}} \cong K^0(BG)$.

---

We actually will show that the representation ring is somehow obviously the $0$ part of $G$-equivariant $K$-theory $K_{G}^\bullet(EG)$ (which is itself $\mathfrak{i}$-adically complete). The real work of Atiyah–Segal is showing that $K_{G}^\bullet(EG)_{\hat{\mathfrak{i}}} \cong K^\bullet(BG)$ and more generally, that $K_{G}^\bullet(X)_{\hat{\mathfrak{i}}} \cong K^\bullet((X \times EG) / G)$.

### Equivariant $K$-theory

Where regular topological $K$-theory is a cohomology theory on spaces, $G$-equivariant $K$-theory is a cohomology theory on $G$-spaces.

##### _theorem:_ Borel equivalences give isomorphisms of completed $K$-theory

If $\pi : X \to Y$ is a Borel equivalence of $G$-spaces, then $\pi^* : K^\bullet_{G}(Y)_{\hat{\mathfrak{i}}} \to K^\bullet_{G}(X)_{\hat{\mathfrak{i}}}$ is an isomorphism.

###### _proof:_

It suffices to show that $\widetilde{K}^{\bullet}(X)_{\hat{\mathfrak{i}}} = 0$ for any contractible $X$ and that for any cofibre sequence $S^0 \to Y \to Y / S^0$ we have $Y$ contractible and thus, $\widetilde{K}_{G}(Y)_{\hat{\mathfrak{i}}} = 0$. Then using the fact that $G$-CW complexes are built up from pieces $G / H \wedge S^n$ we can get the following results for any sequence
$$
X \to X \wedge Y \to X \wedge Y / S^0.
$$
1) $\widetilde{K}_{G}(W \wedge Y)_{\hat{\mathfrak{i}}} = 0$ for any $W$
2) $\widetilde{K}_{G}(X \wedge Z)_{\hat{\mathfrak{i}}} = 0$ for any $Z$ with $Z^G$ contractible.



---