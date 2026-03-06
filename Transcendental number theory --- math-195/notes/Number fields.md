---
tags:
- math-195/11
- math-195/12
- math-195/14
- nt
- alg-nt
---
 
Number fields are finite [[p-adic numbers --- math-177/notes/Algebraic field extensions#_definition _ algebraic, algebraic field extension, $ mathbb{F}[ alpha]$, $ mathbb{F}( alpha)$|algebraic field extensions]] of $\mathbb{Q}$. We restrict our attention to finite extensions, since they are always algebraic and are much nicer.

##### _definition:_ number field

A **number field** is a finite (and thus, algebraic) field extension $\mathbb{K} / \mathbb{Q}$.

---

##### _theorem, definition:_ the primitive element theorem, primitive element

Every number field $\mathbb{K} / \mathbb{Q}$ has some $\alpha \in \mathbb{K}$ such that $\mathbb{K} = \mathbb{Q}(\alpha)$.

Such an $\alpha$ is called a **primitive element**.

---

Our proof implies that to find a primitive element of $\mathbb{K}$ it suffices just to find an element of degree $\deg \mathbb{K} / \mathbb{Q}$. Most elements should be of this degree — anything of lower degree must satisfy additional conditions which is generically not true.

It's often useful to consider number fields as sitting in $\mathbb{C}$.

##### _definition:_ embedding of a number field

A **complex embedding** of a number field $\mathbb{K}$ is a field homomorphism ([[Abstract algebra --- math-171/notes/Ideals and quotients#_corollary _ fields map out injectively|necessarily injective]]) $\sigma : \mathbb{K} \to \mathbb{C}$.

---

Note that embeddings always preserve $\mathbb{Q}$. It suffices to show that they are maps of $\mathbb{Q}$-algebras which follows from the fact that maps of rings are always maps of $\mathbb{Z}$-algebras and that ring homomorphisms preserve multiplicative inverses.

##### _proposition:_ embeddings take numbers to conjugates

Suppose $\alpha \in \mathbb{K} / \mathbb{Q}$ a number field, and $\sigma$ is a complex embedding of $\mathbb{K}$. Then $\sigma(\alpha)$ is an algebraic conjugate of $\alpha$.

###### _proof:_

Write $\alpha$ as the root of $m_{\alpha}(x)$. Then $m_{\alpha}(\alpha) = 0$. But because $\sigma$ preserves $\mathbb{Q}$, $\sigma(m_{\alpha}(\alpha)) = m_{\alpha}(\sigma(\alpha))$. Thus, $m_{\alpha}(\sigma(\alpha)) = 0$, implying $\alpha$ and $\sigma(\alpha)$ are algebraic conjugates.

---

##### _corollary:_ degree $d$ fields have $d$ embeddings

Suppose $\deg \mathbb{K} / \mathbb{Q} = d$. Then there are exactly $d$ distinct embeddings $\mathbb{K} \to \mathbb{C}$.

###### _proof sketch:_

Choose $\alpha$ such that $\mathbb{K} = \mathbb{Q}(\alpha) = \mathbb{Q}[\alpha]$. Thus, each embedding is determined by the image of $\alpha$. Since $\mathbb{Q}$ is a perfect field, there are exactly $d$ conjugates of $\alpha$ that $\alpha$ can be sent to.

---

##### _example:_ a quartic number field

Consider $\mathbb{Q}(\sqrt{ 2 }, \sqrt{ 3 }) = \mathbb{Q}(\sqrt{ 2 } + \sqrt{ 3 })$. It has degree $4$. Then there are four embeddings defined by all combinations of $\sqrt{ 2 } \mapsto \pm \sqrt{ 2 }$ and $\sqrt{ 3 } \mapsto \pm \sqrt{ 3 }$.

---

This gives us a different way to think of primitive elements. $\alpha$ is a primitive element of some $\mathbb{K} / \mathbb{Q}$ of degree $d$, if and only if, for $p(x_{1}, \dots, x_{d}) = \prod_{i \neq j} (x_{i} - x_{j})$ we have $p(\sigma_{1}(\alpha), \dots, \sigma_{d}(\alpha)) \neq 0$.

### Rings of integers


##### _lemma:_ scale field extensions by rational integers to get algebraic integers

Suppose $\alpha \in \mathbb{K}$. Then there is some $n \in \mathbb{Z}$ such that $n \alpha \in \mathscr{O}_{\mathbb{K}}$. Specifically, choosing $n$ to be the largest denominator of the minimal polynomial $m_{\alpha} \in \mathbb{Q}[x]$ suffices.

###### _proof:_

Suppose $m_{\alpha}(x) = \sum_{i = 0}^d a_{i} x^i$. Choose $p(x) = n^{d} m_{\alpha}(x) = \sum_{i = 0}^d n^d a_{i} x^i$, and then choose $q(x) = \sum_{i = 0}^d n^{d - i} a_{i} x^i$ so that $q(n x) = p(x)$. Thus, 
$$
q(n \alpha) = p(\alpha) = n^{d}m_{\alpha}(\alpha) = 0.
$$
But $q$ is a monic polynomial in $\mathbb{Z}[x]$ — the $d$th coefficient is $n^{d - d} a_{d} = a_{d} = 1$, and the others are all $n^k a_{i} \in \mathbb{Z}$ since $k > 0$. Thus, $n \alpha$ is an algebraic integer in $\mathscr{O}_{\mathbb{K}}$.

---

##### _corollary:_ number fields are fraction fields of rings of integers

For $\mathbb{K}$ a number field, we have $\mathbb{K} = Q(\mathscr{O}_{\mathbb{K}})$.

---