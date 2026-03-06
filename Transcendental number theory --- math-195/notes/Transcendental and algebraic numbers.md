---
tags:
- math-195/3
- math-195/11
- nt
- alg-nt
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

### Transcendental extensions

We can extend the rational numbers by [[p-adic numbers --- math-177/notes/Algebraic field extensions#_definition _ adjoining, $ mathbb{F}[ alpha]$, $ mathbb{F}( alpha)$|adjoining]] algebraic or transcendental numbers from $\mathbb{C}$. Transcendental extensions behave very differently from [[p-adic numbers --- math-177/notes/Algebraic field extensions#_definition _ algebraic, algebraic field extension, $ mathbb{F}[ alpha]$, $ mathbb{F}( alpha)$|algebraic extensions]].

##### _proposition:_ transcendental extensions are infinite

Suppose $\alpha \in \mathbb{C}$ is transcendental. Then $\mathbb{Q}[\alpha]$ is infinite $\mathbb{Q}$-dimensional.

###### _proof sketch:_

For each $n$, the list $1, \dots, \alpha^n$ of length $n + 1$ is linearly independent.

---

##### _proposition:_ adjoining one algebraic number is finite

Suppose $\alpha \in \mathbb{C}$ is algebraic of degree $n$. Then $\dim_{\mathbb{Q}} \mathbb{Q}[\alpha] = n$ with basis $1, \alpha, \dots, \alpha^{n - 1}$.

---

##### _proposition:_ $\mathbb{Q}[\alpha]$ is a field if and only if $\alpha$ is algebraic

$\mathbb{Q}[\alpha]$ is a field if and only if $\alpha$ is algebraic. Further, $\mathbb{Q}[\alpha] = \mathbb{Q}(\alpha)$.

###### _proof:_

[[p-adic numbers --- math-177/notes/Algebraic field extensions#_corollary _ minimal polynomials give minimal extensions|We have seen]] that $\mathbb{Q}[\alpha] \cong \mathbb{Q}(\alpha)$ is a field if $\alpha$ is algebraic.

Suppose $\mathbb{Q}[\alpha]$ is a field. Then $f(\alpha) \alpha = 1$ for some polynomial $f$. Then $f(\alpha) \alpha - 1 = 0$, implying that $1, \dots, \alpha^{\deg f}$ is not $\mathbb{Q}$-linearly independent. Thus, $\alpha$ is not transcendental.

---

This allows us to prove that $\overline{\mathbb{Q}}$ is a field without appealing to the fact that it is the algebraic closure of $\mathbb{Q}$.

##### _proposition:_ the algebraic numbers form a field

$\overline{\mathbb{Q}}$ is a field.

###### _proof sketch:_

Let $\{ \alpha_{n} \}_{n \in \mathbb{N}}$ be [[Transcendental number theory --- math-195/notes/Transcendental and algebraic numbers#_theorem _ algebraic numbers are countable, or transcendental numbers exist|an enumeration]] of $\overline{\mathbb{Q}}$. Write $\mathbb{K}_{n} = \mathbb{Q}(\alpha_{1}, \dots, \alpha_{n})$. Each $\mathbb{K}_{n}$ is a finite extension, so each $\beta \in \mathbb{K}_{n}$ has $\mathbb{Q}(\beta) \subseteq \mathbb{K}_{n}$ an algebraic extension. Thus, $\mathbb{Q} \subseteq \mathbb{K}_{1} \subseteq \dots \subseteq \mathbb{K}_{n} \subseteq \dots \subseteq  \overline{\mathbb{Q}}$ and $\overline{\mathbb{Q}} = \bigcup_{n \in \mathbb{N}} \mathbb{K}_{n}$. It's easy to see that the union of a chain of field extensions of $\mathbb{Q}$ is a field extension of $\mathbb{Q}$ — for any $\alpha, \beta \in \overline{\mathbb{Q}}$ choose a sufficiently large $\mathbb{K}_{n}$ to contain their sum, product, and inverses.

---

Note that if we wanted to do this without results like this, we would have to find the minimal polynomial of $\alpha + \beta$ from the minimal polynomials of $\alpha, \beta$ which is hard.

This implies in the standard way that the transcendental numbers are not a field.

##### _proposition:_ the transcendental numbers are not a field

$\mathbb{C} \setminus \overline{\mathbb{Q}}$ and $\mathbb{R} \setminus \overline{\mathbb{Q}}$ are not fields.

###### _proof sketch:_

For $\alpha \in \overline{\mathbb{Q}}$ and $\beta$ transcendental, $\alpha + \beta$ is transcendental (else we would have $\beta = (\alpha + \beta) - \alpha \in \overline{\mathbb{Q}}$). But then the transcendentals $-\beta, \alpha + \beta$ have sum that is not transcendental. Similarly, if $\alpha \neq 0$, $\alpha \beta$ is transcendental.

---

This means that for each transcendental $\alpha$, we get two countable sets $\alpha + \overline{\mathbb{Q}}$ and $\alpha  \overline{\mathbb{Q}}^\times$ of transcendental numbers. However, getting "new" algebraic numbers in these sets isn't really so interesting — once we know $\pi$ is transcendental, it's useless to know that $16 \pi$ is also transcendental. This leads to the notions of algebraic independence and transcendence degree.

##### _definition:_ algebraic independence, transcendence degree

$\alpha_{1}, \dots, \alpha_{n} \in \mathbb{C}$ are **algebraically independent** over $\mathbb{Q}$ if, for each $i$, $\deg \mathbb{Q}(\alpha_{1}, \dots, \alpha_{i + 1}) / \mathbb{Q}(\alpha_{1}, \dots, \alpha_{i})$ is infinite.

The **transcendence degree** of $\alpha_{1}, \dots, \alpha_{n} \in \mathbb{C}$ is $\operatorname{tr \deg} \mathbb{Q}(\alpha_{1}, \dots, \alpha_{n}) / \mathbb{Q}$, the cardinality of a maximal algebraically independent set in $\mathbb{Q}(\alpha_{1}, \dots, \alpha_{n})$.

---

This gives us much more interesting questions. For example, it is known (and we will see) that $e$ and $\pi$ are each transcendental, but whether $\operatorname{tr \deg} \mathbb{Q}(e, \pi) / \mathbb{Q}$ is $1$ or $2$ is still an open question.

This notion also really is equivalent to the notion of algebraic independence we want.

##### _proposition:_ algebraic independence really is algebraic independece

$\alpha_{1}, \dots, \alpha_{n} \in \mathbb{C}$ are algebraically independent over $\mathbb{Q}$ if and only if there is no $p(x_{1}, \dots, x_{n}) \in \mathbb{Q}[x_{1}, \dots, x_{n}]$ such that $p(\alpha_{1}, \dots, \alpha_{k}) = 0$.

###### _proof:_

Suppose $\alpha_{1}, \dots, \alpha_{n} \in \mathbb{C}$ and $p(\alpha_{1}, \dots, \alpha_{k}) = 0$ for $p \in \mathbb{Q}[x_{1}, \dots, x_{n}]$. Then $f \in \mathbb{Q}(\alpha_{1}, \dots, \alpha_{n - 1})[x]$ defined by $f(x) = p(\alpha_{1}, \dots, \alpha_{n - 1}, x)$ has $f(\alpha_{k}) = 0$. But then $\mathbb{Q}(\alpha_{1}, \dots, \alpha_{n}) / \mathbb{Q}(\alpha_{1}, \dots, \alpha_{n - 1})$ is not an infinite extension. Thus, $\alpha_{1}, \dots, \alpha_{n}$ are not algebraically independent.

Conversely, suppose $\alpha_{1}, \dots, \alpha_{n}$ are not algebraically independent. Without loss of generality, suppose $f(\alpha_{n}) = 0$ for some $f \in \mathbb{Q}(\alpha_{1}, \dots, \alpha_{n - 1})[x]$. Write $f(x) = \sum_{i = 0}^d a_{i} x^i$. Then there exist $p_{i}, q_{i} \in \mathbb{Q}[x_{1}, \dots, x_{n - 1}]$ such that $a_{i} = p_{i}(\alpha_{1}, \dots, \alpha_{n - 1}) / q_{i}(\alpha_{1}, \dots, \alpha_{k - 1})$. But then, clearing denominators, we get
$$
\sum_{i = 0}^d p_{i}(\alpha_{1}, \dots, \alpha_{n}) \left( \prod_{j = 1, j \neq i}^{j = d} q_{j}(\alpha)  \right) \alpha_{n}^i = 0
$$
That is, we have a polynomial in $\mathbb{Q}[x_{1}, \dots, x_{n}]$ that evaluates to $0$ at $\alpha_{1}, \dots, \alpha_{n}$.

---

There is yet another way to understand this.

##### _proposition:_ algebraic independence and maps from function fields

Let $\alpha$ denote the $n$-tuple of $\alpha_{1}, \dots, \alpha_{n} \in \mathbb{C}$.

The following are equivalent
1) $\varphi_{\alpha} : \mathbb{Q}(x_{1}, \dots, x_{n}) \to \mathbb{Q}(\alpha_{1}, \dots, \alpha_{n})$ by $p / q \mapsto p(\alpha_{1}, \dots, \alpha_{n}) / q(\alpha_{1}, \dots, \alpha_{n})$ is a field isomorphism
2) $\alpha_{1}, \dots, \alpha_{n}$ are algebraically independent.

###### _proof:_

Suppose $\varphi_{\alpha}$ is a field isomorphism. For it to be well defined, we must never have $q(\alpha) = 0$ for any $q \in \mathbb{Q}[x_{1}, \dots, x_{n}]$. Thus, $\alpha_{1}, \dots, \alpha_{n}$ are algebraically independent.

Suppose $\alpha_{1}, \dots, \alpha_{n}$ are algebraically independent. Then $\varphi_{\alpha}$ is well-defined for each $p / q \in \mathbb{Q}(x_{1}, \dots, x_{n})$ since we never have $q(\alpha) = 0$. In particular, this is not the trivial rng homomorphism. $\varphi_{\alpha}$ is clearly surjective, and field homomorphisms [[Abstract algebra --- math-171/notes/Ideals and quotients#_corollary _ fields map out injectively|are always injective]], so $\varphi_{\alpha}$ is an isomorphism.

---

That is, $\alpha_{1}, \dots, \alpha_{n}$ are algebraically independent if and only if $\mathbb{Q}(\alpha_{1}, \dots, \alpha_{n})$ is isomorphic to the field of [[Transcendental number theory --- math-195/notes/Function fields and transcendence degree#_definition _ field of rational functions|field of rational functions]] $\mathbb{Q}(x_{1}, \dots, x_{n})$