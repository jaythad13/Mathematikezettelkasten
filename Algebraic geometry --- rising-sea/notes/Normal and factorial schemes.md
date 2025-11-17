---
tags:
- rising-sea/5/4
- alg-geo
---

Let $A$ be a ring, and let $X$ be a scheme.

Smoothness is a tricky notion, but we can get something that sort of approximates it in normality (for reasons that we won't be able to explain until we know what smoothness is). Just as [[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_proposition _ integral schemes are one piece, no fuzz|integrality is a strengthening of reducedness]], we will see that factoriality strengthens normality.

### Normality

##### _definition:_ normal schemes

$X$ is a **normal scheme** if each stalk $\mathscr{O}_{X, p}$ is [[Algebraic geometry --- rising-sea/notes/Integrally closed domains#_definition _ integrally closed domain|integrally closed]].

---

Note again that since [[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_example _ integrality is not stalk-local|integrality is not stalk-local]], normal schemes are not necessarily [[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_definition _ integral scheme|integral]].

Since integral closure [[Algebraic geometry --- rising-sea/notes/Integrally closed domains#_proposition _ integral closure is (maximal) stalk-local|is stalk-local]], we can check the normality on any affine cover of a scheme.

##### _corollary:_ normality is affine-local

Suppose $X = \bigcup_{i \in \mathscr{I}} \operatorname{Spec} A_{i}$ and each $A_{i}$ is integrally closed. Then $X$ is a normal scheme.

---

##### _example:_ $\operatorname{Spec} \mathbb{Z}$ is normal

$\mathbb{Z}$ is [[Algebraic geometry --- rising-sea/notes/Integrally closed domains#_definition _ integrally closed domain|integrally closed]], so $\operatorname{Spec} \mathbb{Z}$ is normal.

---

### Factoriality

##### _definition:_ factorial schemes

$X$ is a **factorial scheme** if each stalk $\mathscr{O}_{X, p}$ is a [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ unique factorisation domains|unique factorisation domain]].

---

Since [[Algebraic geometry --- rising-sea/notes/Integrally closed domains#_proposition _ UFDs are integrally closed|unique factorisation domains are integrally closed]], factorial schemes are normal.

##### _proposition:_ factorial schemes are normal

If $X$ is a factorial, it is normal.

---


This yields lots of examples of normal schemes.

##### _examples:_ factorial and normal schemes

- $\operatorname{Spec} \mathbb{Z}$ is factorial since $\mathbb{Z}$ is a UFD
- $\mathbb{F}[x_{1}, \dots, x_{n}]$ is also a UFD, so $\mathbb{A}_{\mathbb{F}}^n$ is factorial
- Using the result below, this implies $\mathbb{P}_{\mathbb{F}}^n$ is factorial

---

It is difficult to tell whether a domain has unique factorisation. However, there are some tools. For example, unique factorisation does play nicely with localisation in one direction — non-zero localisations of UFDs are UFDs. Thus, it suffices to find a factorial cover of a scheme.

##### _proposition:_ factoriality on a cover suffices

Suppose $X = \bigcup_{i \in \mathscr{I}} \operatorname{Spec} A_{i}$ with each $A_{i}$ a UFD. Then $X$ is factorial.

###### _proof:_

Each non-zero localisation $A_{i, \mathfrak{p}}$ is a UFD. Thus, each stalk $\mathscr{O}_{X, p}$ is a UFD.

---

Note however, that the opposite does not hold — there are factorial schemes covered by non-UFD rings. The easiest example is of course affine.

##### _example:_ factorial affine schemes from non-UFD ring

Let $A$ be the degree zero portion of the graded ring $S_{\bullet} = \mathbb{Q}[x, y]_{x^{2} + y^{2}}$. That is, elements of $A$ are $f(x, y) / (x^{2} + y^{2})^n$ with $f$ having pure degree $2n$. $A$ is not a UFD since we have two distinct factorisations
$$
\left( \frac{xy}{x^{2} + y^{2}} \right)^{2} = \left( \frac{x^{2}}{x^{2} + y^{2}} \right)\left( \frac{y^{2}}{x^{2} + y^{2}} \right)
$$
Each of the factors is irreducible because its numerator is of minimal degree

The distinguished open sets $D(x^{2} / (x^{2} + y^{2}))$ and $D(y^{2} / (x^{2} + y^{2}))$ cover $A$ [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_proposition _ distinguished covers generate the whole ring|since]] the sum of the functions that don't vanish on them is $1$.

$B = A_{x^{2} / (x^{2} + y^{2})}$ then consists of 

A second example we will not explain in detail is that $\mathbb{Z}[\sqrt{ -5 }]$ is not a unique factorisation domain (factor $6$ two ways), but can be covered by $D(2)$ and $D(3)$ which are spectra of $\mathbb{Z}[\sqrt{ -5 }]_{2}$ and $\mathbb{Z}[\sqrt{ -5 }]_{3}$ , both UFDs.

---