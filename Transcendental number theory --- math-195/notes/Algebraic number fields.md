---
tags:
- math-195/11
- nt
- alg-nt
---

Algebraic number fields are finite [[p-adic numbers --- math-177/notes/Algebraic field extensions|algebraic field extensions]] of $\mathbb{Q}$. We restrict our attention to finite extensions, since they are always algebraic and are much nicer.

### Transcendental versus algebraic extensions

We can first compare the dimensions.

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

###### _proof sketch:_

Suppose $\alpha$ is algebraic. $\mathbb{Q}[\alpha]$ is a finite $\mathbb{Q}$-algebra and an integral domain. [[Algebraic geometry --- rising-sea/notes/Hilbert's Nullstellensatz#_proposition _ characterising finite $ mathbb{F}$-algebras|Thus]], it is a field.

Suppose $f(\alpha) \alpha = 1$ for some polynomial $f$. Then $f(\alpha) \alpha - 1 = 0$, implying that $1, \dots, \alpha^{\deg f}$ is not $\mathbb{Q}$-linearly independent. Thus, $\alpha$ is not transcendental.

---

This allows us to prove that $\overline{\mathbb{Q}}$ is a field without appealing to the fact that it is the algebraic closure of $\mathbb{Q}$.

##### _proposition:_ the algebraic numbers form a field

$\overline{\mathbb{Q}}$ is a field.

###### _proof sketch:_

Let $\{ \alpha_{n} \}_{n \in \mathbb{N}}$ be [[Transcendental number theory --- math-195/notes/Transcendental and algebraic numbers#_theorem _ algebraic numbers are countable, or transcendental numbers exist|an enumeration]] of $\overline{\mathbb{Q}}$. Write $\mathbb{K}_{n} = \mathbb{Q}(\alpha_{1}, \dots, \alpha_{n})$. Each $\mathbb{K}_{n}$ is a finite extension, so each $\beta \in \mathbb{K}_{n}$ has $\mathbb{Q}(\beta) \subseteq \mathbb{K}_{n}$ an algebraic extension. Thus, $\mathbb{Q} \subseteq \mathbb{K}_{1} \subseteq \dots \subseteq \mathbb{K}_{n} \subseteq \dots \subseteq  \overline{\mathbb{Q}}$ and $\overline{\mathbb{Q}} = \bigcup_{n \in \mathbb{N}} \mathbb{K}_{n}$. It's easy to see that the union of a chain of field extensions of $\mathbb{Q}$ is a field extension of $\mathbb{Q}$ — for any $\alpha, \beta \in \overline{\mathbb{Q}}$ choose a sufficiently large $\mathbb{K}_{n}$ to contain their sum, product, and inverses.

---

Note that if we wanted to do this without results like this, we would have to find the minimal polynomial of $\alpha + \beta$ from the minimal polynomials of $\alpha, \beta$ which is not straightforward at all.

Also note that since $\overline{\mathbb{Q}}$ is a field containing all roots of polynomials in $\mathbb{Q}[x]$ it is the algebraic closure of $\mathbb{Q}$.

This implies in the standard way that the transcendental numbers are not a field.

##### _proposition:_ the transcendental numbers are not a field

$\mathbb{C} \setminus \overline{\mathbb{Q}}$ and $\mathbb{R} \setminus \overline{\mathbb{Q}}$ are not fields.

###### _proof sketch:_

For $\alpha \in \overline{\mathbb{Q}}$ and $\beta$ transcendental, $\alpha + \beta$ is transcendental (else we would have $\beta = (\alpha + \beta) - \alpha \in \overline{\mathbb{Q}}$). But then the transcendentals $-\beta, \alpha + \beta$ have sum that is not transcendental.

---

This also allows us to define the notion of algebraic independence.

##### _definition:_ algebraic independence

For $\alpha, \beta \in \mathbb{C}$, $\alpha$ and $\beta$ are **algebraically independent** over $\mathbb{Q}$ if $\deg \mathbb{Q}(\alpha, \beta) / \mathbb{Q}(\alpha) = \deg \mathbb{Q}(\alpha, \beta) / \mathbb{Q}(\beta) = \infty$. 

---

##### _definition:_ transcendence degree

The **transcendence degree** of $\alpha_{1}, \dots, \alpha_{n} \in \mathbb{C}$ is $\operatorname{tr \deg} \mathbb{Q}(\alpha_{1}, \dots, \alpha_{n}) / \mathbb{Q}$ is the cardinality of a maximal algebraically independent set in $\mathbb{Q}(\alpha_{1}, \dots, \alpha_{n})$.

---

We don't yet know $\operatorname{tr \deg} \mathbb{Q}(e, \pi) / \mathbb{Q}$, for example.