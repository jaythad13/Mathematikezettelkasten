---
tags:
- comm-alg
- math-189AA/6
---

Let $A$ be a (commutative, unital) ring.

You may not have seen modules before, but you have seen modules. For example all abelian groups and rings have a $\mathbb{Z}$-module structure — you can make sense of scaling by elements of $\mathbb{Z}$ (either by $n \cdot g = g + \dots + g$ or $n \cdot a = \varphi(n) a$ for $\varphi : \mathbb{Z} \to A$). $A$-modules generalise these $\mathbb{Z}$-modules (and [[Linear algebra done right --- ladr/notes/Vector spaces#_definition _ vector space|vector spaces]] in general) by allowing scalars in an arbitrary ring $A$.

##### _definition:_ module

An $A$-module $M$ is an [[Abstract algebra --- math-171/notes/Groups, and why you should care#_definition _ abelian group, commutative group|abelian group]] (written additively) with a linear ring action of $A$ on $M$, or equivalently, a ring homomorphism $A \to Z(\operatorname{End} M)$ 

Here $\operatorname{End} M$ is given a (not)-necessarily commutative unital ring structure by composition, $Z(\operatorname{End} M)$ is its centre, and the morphism preserves identity by $1 \mapsto \operatorname{id}_{M}$.

---

##### _examples and non-examples:_ modules

1) $0$ is a module over every ring
2) $A$ is an $A$-module
3) The $\mathbb{Z}$-modules are exactly the abelian groups
4) The $\mathbb{F}$-modules are exactly the $\mathbb{F}$-vector spaces
5) Every ideal $\mathfrak{i} \subseteq A$ is an $A$-module, and so is every $A / \mathfrak{i}$
6) More generally, every ring homomorphism $\varphi : A \to B$ defines an $A$-module structure on $B$ by $ab = \varphi(a) b$.
7) $\mathbb{Q}$ is a $\mathbb{Z}$-module, but $\mathbb{Z}$ is not a $\mathbb{Q}$-ideal
8) In fact, $\mathbb{Z}$ is not a $\mathbb{Q}$-module under any scaling. Consider $n(1 / n) \cdot z = z$. Let $(1/n) \cdot z = y \in \mathbb{Z}$. Then $n \cdot y = z$. Writing $n = 1 + \dots + 1$, we get $ny = z$. Thus, all $n \in \mathbb{N}$ divide $z \in \mathbb{Z}$. There is no such $z \in \mathbb{Z}$.
9) In general, localisation $S^{-1} A$ is an $A$-module
10) $\mathbb{Q}$ is a $\mathbb{Q}$-module under addition, but not under multiplication
11) $\mathbb{C}[x]$ is $\mathbb{C}[x]$-module with scaling by $\lambda \in \mathbb{C}$ as usual, but scaling by $x$ corresponds to taking derivatives (with respect to $x$).

---

##### _homework:_ show that $\mathbb{C}[x]$ is a $\mathbb{C}[x]$-module under derivatives

##### _homework:_ is an $A$-module $M$ an $A / \operatorname{Ann}_{A} M$-module?

### New modules from old

##### _definition:_ localisation of a module

Given a multiplicative set $S \subseteq A$, and an $A$-module $M$, we can construct an $A$-module and $S^{-1} A$-module by localising away from $S$ —
$$
S^{-1} M = \{  m / s \mid m \in M, s \in S \} / \sim
$$
where $m_{1} / s_{1} \sim m_{2} / s_{2}$ exactly when $s(m_{1} s_{2} - m_{2} s_{1}) = 0$ for some $s \in S$.

Addition and scaling are defined in the obvious way.

---

##### _example:_

##### _definition:_