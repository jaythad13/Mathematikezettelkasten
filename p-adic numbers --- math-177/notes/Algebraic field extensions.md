---
tags:
- alg
- galois
- math-177/11
- math-177/12
---

(Algebraic) field extensions are concerned with finding where the roots of polynomials in $\mathbb{F}[x]$ live. It's most reasonable to focus on the irreducible factors — we can find the roots of any reducible polynomial by finding the roots of its irreducible factors.

It's not hard to show that if $\mathbb{F}$ is a [[Abstract algebra --- math-171/notes/Fields#_definition _ fields|field]], then $\mathbb{F}[x]$ is a [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ Euclidean domain|Euclidean domain]] (by polynomial long division). Thus, if $f \in \mathbb{F}[x]$ is irreducible (that is $f = g h$ implies $g$ or $h$ is a [[Abstract algebra --- math-171/notes/Rings#_definition _ unit|unit]]). Then $(f)$ is [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|prime]] and since [[Abstract algebra --- math-171/notes/Factorisation in special rings#_proposition _ Euclidean domains are principal ideal domains|a Euclidean domain is a]] [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ principal ideal domain|principal ideal domain]], it is in fact [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ maximal ideal|maximal]] (any $(g)$ containing $(f)$ would have $f = g h$, so ...).

Thus, $\mathbb{K} = \mathbb{F}[x] / (f)$ is a field. It's elements look like cosets $a_{0} + a_{1} x + \dots + a_{n - 1} x^{n - 1} + (f)$ with $a_{i} \in \mathbb{F}$. We can understand this as an $n$-dimensional [[Linear algebra done right --- ladr/notes/Vector spaces#_definition _ vector space|vector space]] (and actually, an [[Commutative algebra --- math-189AA/notes/Conventions for commutative algebra#_definition _ algebras|algebra]]) over $\mathbb{F}$. In this, we can reasonably look for roots of $f$. 

We have an injection $\mathbb{F} \to \mathbb{K}$ since we have $\mathbb{F} \to \mathbb{F}[x] \to \mathbb{K}$ and the kernel of $\mathbb{F}[x] \to \mathbb{K}$ has $0$ intersection with $\mathbb{F}$. Thus, we also have an injection $\mathbb{F}[y] \to \mathbb{K}[y]$. Note this is not the map $\mathbb{F}[y] \cong \mathbb{F}[x] \to \mathbb{K}$ (which is not an injection). Then the image of $f$ under $\mathbb{F}[y] \to \mathbb{F}[x][y] \to \mathbb{K}[y]$, evaluated at $x + (f)$ (evaluation at a specific value of $y$ as a morphism $\mathbb{F}[x][y] \to \mathbb{F}[x]$) is just $f(x) + (f) = (f) \in \mathbb{F}[x]$, and thus, $0$ in $\mathbb{K}$. That is, we have a root of $f$ in $\mathbb{K}$. 

Write $f(y) = (y - x) g(y)$ to indicate that $x$ is a root. Reduce $g$ to irreducibles in $\mathbb{K}[y]$, and then if they are not all linear, repeat to get all their roots.

This is enough yap, so let's think about an example.

##### _example:_ extending $\mathbb{Q}_{5}$ to get square roots of $2$

Since $x^{2} - 2$ is irreducible in $\mathbb{Q}_{5}[x]$, we can think of $\mathbb{Q}_{5}(\sqrt{ 2 }) = \{ a + b \sqrt{ 2 } \mid a, b \in \mathbb{Q}_{5} \}$ as the field $\mathbb{Q}_{5}[x] / (x^{2} - 2)$.

---

We can make this precise with the following definitions.

##### _definition:_ field extension, degree

A **field extension** of $\mathbb{F}$ is a field $\mathbb{K}$ with an (injective) homomorphism $\mathbb{F} \to \mathbb{K}$. The fact that $\mathbb{K}$ is a field extension of $\mathbb{F}$ is denoted $\mathbb{K} / \mathbb{F}$.

The **degree** $\mathbb{K} : \mathbb{F}$ of the field extension $\mathbb{K} / \mathbb{F}$ is the dimension of $\mathbb{K}$ as an $\mathbb{F}$-vector space.

---

##### _definition:_ algebraic, algebraic field extension

Let $\mathbb{K} / \mathbb{F}$ be a field extension.

$\alpha \in \mathbb K$ is **algebraic over $\mathbb{F}$** if there is some polynomial $p \in \mathbb{F}[x] \subseteq \mathbb{K}[x]$ with $p(\alpha) = 0$.

$\mathbb{K} / \mathbb{F}$ is **algebraic** if every $\alpha \in \mathbb{K}$ is algebraic over $\mathbb{F}$.

---

##### _proposition, definition:_ the minimal polynomial

Suppose $\mathbb{K} / \mathbb{F}$ is a field extension and $\alpha \in \mathbb{K}$ is algebraic over $\mathbb{F}$. Then there exists a unique monic irreducible polynomial $p_{\alpha} \in \mathbb{F}[x]$ such that $\mathbb{F}[\alpha] \cong \mathbb{F}[x] / (p_{\alpha})$.

This unique monic irreducible polynomial is called the **minimal polynomial** of $\alpha$ over $\mathbb{F}$.

###### _proof:_

Consider the evaluation homomorphism $\varphi : \mathbb{F}[x] \to \mathbb{F}[\alpha]$ that is identity on $\mathbb{F}$ and maps $x \mapsto \alpha$. It is surjective since every element of $\mathbb{F}[\alpha]$ is some "polynomial in $\alpha$". By the [[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the first isomorphism theorem|first isomorphism theorem]] $\mathbb{F}[x] / \ker \varphi \cong \mathbb{F}[\alpha]$. 

Since $\mathbb{F}[x]$ is a Euclidean domain, $\ker \varphi = (p_{\alpha})$ is principal. Choose $q$ to be monic by multiplying by a unit in $\mathbb{F}$. Also, since $\mathbb{F}[\alpha]$ is an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]], $\ker \varphi$ [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_proposition _ prime ideals have integral domains as quotients|must be prime]]. Thus, $p_{\alpha}$ must be irreducible.

If some other monic $q$ has $(q) = (p_{\alpha})$, then $q \mid p_{\alpha}$ and by irreducibility $p_{\alpha} = \beta q$ for some unit $\beta \in \mathbb{F}$. $q$ can only be monic if $\beta = 1$. That is, $q = p_{\alpha}$.

---

##### _corollary:_ minimal polynomials give minimal extensions

Suppose $\mathbb{K} / \mathbb{F}$ is a field extension and $\alpha \in \mathbb{K}$ is algebraic over $\mathbb{F}$. Then $\mathbb{F}[\alpha] \cong \mathbb{F}[x]  / (p_{\alpha})$ is the smallest subfield of $\mathbb{K}$ containing $\alpha$ and $\mathbb{F}$.

###### _proof:_

Any subfield of $\mathbb{K}$ containing $\alpha$ and $\mathbb{F}$ must contain all $a_{0} + a_{1} \alpha + \dots + a_{n} \alpha^n$. Thus, it must contain $\mathbb{F}[\alpha]$. We need only show $\mathbb{F}[\alpha]$ is a field. In a Euclidean domain, irreducible elements generate maximal ideals. Thus, $\mathbb{F}[\alpha] \cong \mathbb{F}[x] / (p_{\alpha})$ is a subfield of $\mathbb{K}$.

---

In general, this is not true — $\mathbb{Q}[\pi]$ is not a field. We give notation for the minimal field extension in general.

##### _definition:_ minimal field extension

If $\mathbb{K}$ is a field extension of $\mathbb{F}$ and $\alpha \in \mathbb{K}$, we write $\mathbb{F}(\alpha)$ for the minimal (by inclusion) field extension of $\mathbb{F}$ containing both $\mathbb{F}$ and $\alpha$.