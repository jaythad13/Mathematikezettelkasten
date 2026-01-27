---
tags:
- math-195/3
- nt
---

##### _definition:_ algebraic, transcendental

A complex number $\alpha$ is **algebraic** if there exists a polynomial $p(x) \in \mathbb{Z}[x]$ such that $p(\alpha) = 0$. The set of all algebraic numbers is denoted $\overline{\mathbb{Q}}$.

If $\alpha \in \mathbb{C}$ is not algebraic, it is **transcendental**.

---

##### _example:_ algebraic numbers

Any $\alpha \in \mathbb{Q}$ is algebraic (choose $p(x) = nx - m$) and so are square roots and cube roots, and so on (choose $p(x) = x^n - d$). 

---

However, it is very difficult to find an example of a transcendental number. This is despite the transcendental numbers making up most of the complex numbers and also most of the real numbers.

##### _theorem:_ algebraic numbers are countable, or transcendental numbers exist

The algebraic numbers $\overline{\mathbb{Q}} \subseteq \mathbb{C}$ are a countable (infinite) subset.

Thus, the real algebraic numbers $\overline{\mathbb{Q}} \cap \mathbb{R} \subseteq \mathbb{R}$ are also a countable subset, the transcendental numbers are uncountable, and transcendental numbers exist.

###### _proof:_

We do this by using **heights**. Let $p(x) \in \mathbb{Z}[x]$ be a polynomial. The height of $p$ is the sum of the absolute values of all of its coefficients. It is a non-negative natural number.

For each height $H \in \mathbb{N}_{0}$ its easy to see that there are finitely many polynomials of height $H$ (there are finitely many choices of coefficients). Each of these polynomials has finitely many roots. Denote by $\overline{\mathbb{Q}}^H$, the set of roots of polynomials of height $H$. Then $\overline{\mathbb{Q}} \subseteq \bigcup_{H \in \mathbb{N}_{0}} \overline{\mathbb{Q}}^H$. The union is a countable union of finite sets, [[Analysis --- math-131/notes/Countability#_lemma _ countable unions of countable sets are countable|and so]] countable. Thus, there is an injection $\overline{\mathbb{Q}} \to \mathbb{N}$, or equivalently, $\overline{\mathbb{Q}}$ is at most countable. Since it is infinite, it is exactly countable.

---