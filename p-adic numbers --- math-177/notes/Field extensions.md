---
tags:
- alg
- galois
- math-177/11
---

(Finite) field extensions are concerned with finding where the roots of polynomials in $\mathbb{F}[x]$ live. It's most reasonable to focus on the irreducible factors — we can find the roots of any reducible polynomial by finding the roots of its irreducible factors.

It's not hard to show that if $\mathbb{F}$ is a [[Abstract algebra --- math-171/notes/Fields#_definition _ fields|field]], then $\mathbb{F}[x]$ is a [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ Euclidean domain|Euclidean domain]] (by polynomial long division). Thus, if $f \in \mathbb{F}[x]$ is irreducible (that is $f = g h$ implies $g$ or $h$ is a [[Abstract algebra --- math-171/notes/Rings#_definition _ unit|unit]]). Then $(f)$ is [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ prime ideals|prime]] and since [[Abstract algebra --- math-171/notes/Factorisation in special rings#_proposition _ Euclidean domains are principal ideal domains|a Euclidean domain is a]] [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ principal ideal domain|principal ideal domain]], it is in fact [[Abstract algebra --- math-171/notes/Prime and maximal ideals#_definition _ maximal ideal|maximal]] (any $(g)$ containing $(f)$ would have $f = g h$, so ...).

Thus, $\mathbb{K} = \mathbb{F}[x] / (f)$ is a field. It's elements look like cosets $a_{0} + a_{1} x + \dots + a_{n - 1} x^{n - 1} + (f)$ with $a_{i} \in \mathbb{F}$. We can understand this as an $n$-dimensional vector space (and actually, an algebra) over $\mathbb{F}$. In this, we can reasonably look for roots of $f$. 

We have an injection $\mathbb{F} \to \mathbb{K}$ since we have $\mathbb{F} \to \mathbb{F}[x] \to \mathbb{K}$ and the kernel of $\mathbb{F}[x] \to \mathbb{K}$ has $0$ intersection with $\mathbb{F}$. Thus, we also have an injection $\mathbb{F}[y] \to \mathbb{K}[y]$. Note this is not the map $\mathbb{F}[y] \cong \mathbb{F}[x] \to \mathbb{K}$ (which is not an injection). Then the image of $f$ under $\mathbb{F}[y] \to \mathbb{F}[x][y] \to \mathbb{K}[y]$, evaluated at $x + (f)$ (evaluation at a specific value of $y$ as a morphism $\mathbb{F}[x][y] \to \mathbb{F}[x]$) is just $f(x) + (f) = (f) \in \mathbb{F}[x]$, and thus, $0$ in $\mathbb{K}$. That is, we have a root of $f$ in $\mathbb{K}$. 

Write $f(y) = (y - x) g(y)$ to indicate that $x$ is a root. Reduce $g$ to irreducibles in $\mathbb{K}[y]$, and then if they are not all linear, repeat to get their roots.

This is enough rubbish, so let's think about an example

##### _example:_ extending $\mathbb{Q}_{5}$ to get square roots of $2$

Since $x^{2} - 2$ is irreducible in $\mathbb{Q}_{5}[x]$, we can think of $\mathbb{Q}_{5}(\sqrt{ 2 }) = \{ a + b \sqrt{ 2 } \mid a, b \in \mathbb{Q}_{5} \}$ as the field $\mathbb{Q}_{5}[x] / (x^{2} - 2)$.

---