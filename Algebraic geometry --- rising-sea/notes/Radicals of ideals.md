---
tags:
- rising-sea/3/4
- alg-geo
- comm-alg
---

Let $A$ be a ring.

The radical of an ideal describes elements that would be in the ideal if it were prime.

##### _definition:_ radical of an ideal, radical ideal

The **radical of an ideal** $\mathfrak{i} \subseteq A$ is $\sqrt{ \mathfrak{i} } = \{ x \mid x^n \in \mathfrak{i} \}$.

An ideal $\mathfrak{i} \subseteq A$ is **radical** if $\mathfrak{i} = \sqrt{ \mathfrak{i} }$.

---

##### _example:_ the nilradical is a radical

The nilradical $\mathfrak{N} \subseteq A$ is just $\sqrt{ (0) }$.

---

This definition really does have to do with primeness.

##### _proposition:_ the radical is the intersection of all primes containing the ideal

The radical of an ideal $\mathfrak{i} \subseteq A$ is the intersection of all primes $\mathfrak{p} \subseteq A$ containing $\mathfrak{i}$. That is,
$$
\sqrt{ \mathfrak{i} } = \bigcap_{\mathfrak{p} \supseteq \mathfrak{i}} \mathfrak{p}.
$$

###### _proof:_

Consider the nilradical $\mathfrak{N}_{A / \mathfrak{i}}$ in the quotient ring $A /\mathfrak{i}$. [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_definition _ nilpotents|By definition]] all $\overline{x} \in A / \mathfrak{i}$ such that $\overline{x}^n = 0$ corresponding to all $x \in A$ with $x^n \in \mathfrak{i}$. That is, $\mathfrak{N}_{A / \mathfrak{i}} = \sqrt{ \mathfrak{i} } / \mathfrak{i}$ [[Commutative algebra --- math-189AA/notes/Nilpotents and the nilradical#_proposition _ the nilradical is an ideal and the intersection of primes|It is also]] the intersection of all primes $\mathfrak{p} / \mathfrak{i} \subseteq A / \mathfrak{i}$. By the [[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the fourth isomorphism theorem|fourth isomorphism theorem]], this corresponds to all primes $\mathfrak{p} \subseteq A$ containing $\mathfrak{i}$. That is, $\mathfrak{N}_{A / \mathfrak{i}} = \bigcap_{\mathfrak{p} \supseteq \mathfrak{i}} \mathfrak{p} / \mathfrak{i}$. 

Since $\mathfrak{j} \mapsto \mathfrak{j} / \mathfrak{i}$ is injective, we have $\sqrt{ \mathfrak{i} } = \bigcap_{\mathfrak{p} \supseteq \mathfrak{i}} \mathfrak{p} / \mathfrak{i}$.

---

### Properties of the radical

Let $\mathfrak{i} \subseteq A$ be an ideal.

The radical has a bunch of useful properties that we collect here.

##### _proposition:_ the radical contains the ideal

$\sqrt{ \mathfrak{i} } \supseteq \mathfrak{i}$.

###### _proof sketch:_

For $x \in \mathfrak{i}$, choose $n = 1$.

---

##### _proposition:_ the radical of the radical

$\sqrt{ \mathfrak{i} } = \sqrt{ \sqrt{ \mathfrak{i} } }$.

###### _proof:_

We already have $\sqrt{ \mathfrak{i} } \subseteq \sqrt{ \sqrt{ \mathfrak{i} } }$.

Now suppose $x \in \sqrt{ \sqrt{ \mathfrak{i} } }$. Then $x^n \in \sqrt{ \mathfrak{i} }$, so $(x^n)^m \in \mathfrak{i}$. Thus, $x^{nm} \in \mathfrak{i}$, so $x \in \sqrt{ \mathfrak{i} }$.

---

##### _proposition:_ radicals commute with finite intersection

Let $\mathfrak{i}_{1}, \dots, \mathfrak{i}_{n} \subseteq A$ be ideals. Then
$$
\sqrt{ \bigcap_{j = 1}^n \mathfrak{i}_{j} } = \bigcap_{j = 1}^n \sqrt{ \mathfrak{i}_{j} }.
$$

###### _proof:_

Suppose $x \in \bigcap_{j = 1}^n \sqrt{ \mathfrak{i}_{j} }$. Then, for each $j$ there are $m_{j}$ such that $x^{m_{j}} \in \mathfrak{i}_{j}$. Choose the product $m = m_{1} \cdots m_{j}$. Then $x^{m} \in \bigcap_{j = 1}^n \mathfrak{i}_{j}$. Thus, $x$ is in the radical of the intersection.

Suppose $x \in \sqrt{ \bigcap_{j = 1}^n { \mathfrak{i}_{j} } }$. Thus, $x^m \in \bigcap_{j = 1}^n \mathfrak{i}_{j}$ for some $m$ and so $x^m \in \mathfrak{i}_{j}$ for each $j$.

---