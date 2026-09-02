---
tags:
- math-171/17
- math-172
- alg
---

All of the [[Abstract algebra --- math-171/notes/Group isomorphism theorems|group isomorphism theorems]] hold true for [[Abstract algebra --- math-171/notes/Rings|rings]] if you replace "[[Abstract algebra --- math-171/notes/Normal subgroups#Normal subgroups|normal subgroup]]" with "[[Abstract algebra --- math-171/notes/Ideals and quotients#_definition _ ideal|ideal]]" (and [[Abstract algebra --- math-171/notes/Group isomorphisms|group isomorphisms]] with [[Abstract algebra --- math-171/notes/Ring homomorphisms#_definition _ ring isomorphism|ring isomorphisms]])

### First isomorphism theorem

This is exactly analogous to the [[Abstract algebra --- math-171/notes/Group isomorphism theorems#The first isomorphism theorem|the first isomorphism theorem for groups]].

##### _theorem:_ the first isomorphism theorem

Let $\varphi : R \to S$ be a ring homomorphism. Then
1) $\ker \varphi$ is an ideal
2) $R / \ker \varphi \cong \varphi(R)$.

---

##### _example:_ we are justified in calling it $\mathbb{Z} / n\mathbb{Z}$

$\varphi : \mathbb{Z} \to \mathbb{Z} / n \mathbb{Z}$ by $x \mapsto \overline{x}$ is a surjective homomorphism with $\ker \varphi = n \mathbb{Z}$. Then the first isomorphism theorem tells us that we really are justified in calling $\mathbb{Z} / n \mathbb{Z}$ since it is actually isomorphic to $\mathbb{Z}$ with the multiples of $n$ modded out.

---

##### _example:_ quotients of the Gaussian integers

Consider $A = \mathbb{Z}[i] / (1 + 3 i)$. Clearly $10 = (1 + 3i)(1 - 3i) \in (1 + 3i)$. Use [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_example _ initial and final objects in specific categories|the unique]] $\varphi : \mathbb{Z} \to A$. Since $a + b i = a + 3b \in A$, we have that $\mathbb{Z} \to A$ is surjective. If $n \in \ker \varphi$ then $(1 + 3 i ) \mid n$. In particular, $n = (1 + 3i)(a + bi)$ and so has real part $a - 3b$ and imaginary part $3a + b = 0$. But then $a - 3b = a - 3(-3a) = 10a$. Thus, $n \in (10)$. That is, $\ker \varphi \subseteq (10)$. We already know the converse, so $A \cong \mathbb{Z} / \ker \varphi \cong \mathbb{Z} / 10$. 

---

### Second isomorphism theorem

This is also analogous to [[Abstract algebra --- math-171/notes/Group isomorphism theorems#The second isomorphism theorem|the second isomorphism theorem for groups]]

##### _theorem:_ the second isomorphism theorem

Let $A \subset R$ be a subring and $B \subset R$ an ideal. Then
1) $A + B$ is a subring of $R$ with $A \cap B$ an ideal of $A$
2) $A + B / A \cong A / A \cap B$.

---

### Third isomorphism theorem

##### _theorem:_ the third isomorphism theorem

Let $I$ and $J$ be ideals with $I \subset J$. Then
1) $J / I$ is an ideal of $R/I$
2) $(R/I) /(J / I) \cong R / J$.

---

##### _example:_ more quotients of the Gaussian integers

We can think of the Gaussian integers $\mathbb{Z}[i]$ (the smallest $\mathbb{Z}$-subalgebra of $\mathbb{C}$ containing $i$) as $\mathbb{Z}[x] / (x^{2} + 1)$. Then $\mathbb{Z}[i] / (i - 2)$ is just $\mathbb{Z}[x] / (x^{2} + 1, x - 2) \cong \mathbb{Z}$.

---

### Fourth isomorphism theorem

##### _theorem:_ the fourth isomorphism theorem

Let $I \subset R$ be an ideal. There is an inclusion preserving bijection between the ideals $J$ of $R$ that contain $I$ and the set of subrings of $R/I$. Further, $J \subseteq R / I$ is an ideal if and only if $J / I$ is an ideal of $R / I$.

---