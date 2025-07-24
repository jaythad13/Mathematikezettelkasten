---
tags:
- math-171/17
- alg
---

All of the [[Abstract algebra --- math-171/notes/Group isomorphism theorems|group isomorphism theorems]] hold true for [[Abstract algebra --- math-171/notes/Rings|rings]] if you replace "[[Abstract algebra --- math-171/notes/Normal subgroups#Normal subgroups|normal subgroup]]" with "[[Abstract algebra --- math-171/notes/Ideals and quotients#_definition _ ideal|ideal]]" (and [[Abstract algebra --- math-171/notes/Group isomorphisms|group isomorphisms]] with [[Abstract algebra --- math-171/notes/Ring homomorphisms#_definition _ ring isomorphism|ring isomorphisms]])

### First isomorphism theorem

This is exactly analogous to the [[Abstract algebra --- math-171/notes/Group isomorphism theorems#The first isomorphism theorem|the first isomorphism theorem for groups]].

##### _theorem:_ the first isomorphism theorem

Let $\varphi : R \to S$ be a ring homomorphism. Then
1) $\ker \varphi$ is an ideal
2) $R / \ker \varphi \cong \varphi(R)$.

##### _example:_ we are justified in calling it $\mathbb{Z} / n\mathbb{Z}$

$\varphi : \mathbb{Z} \to \mathbb{Z} / n \mathbb{Z}$ by $x \mapsto \overline{x}$ is a surjective homomorphism with $\ker \varphi = n \mathbb{Z}$. Then the first isomorphism theorem tells us that we really are justified in calling $\mathbb{Z} / n \mathbb{Z}$ since it is actually isomorphic to $\mathbb{Z}$ with the multiples of $n$ modded out.

### Second isomorphism theorem

This is also analogous to [[Abstract algebra --- math-171/notes/Group isomorphism theorems#The second isomorphism theorem|the second isomorphism theorem for groups]]

##### _theorem:_ the second isomorphism theorem

Let $A \subset R$ be a subring and $B \subset R$ an ideal. Then
1) $A + B$ is a subring of $R$ with $A \cap B$ an ideal of $A$
2) $A + B / A \cong A / A \cap B$.

### Third isomorphism theorem

##### _theorem:_ the third isomorphism theorem

Let $I$ and $J$ be ideals with $I \subset J$. Then
1) $J / I$ is an ideal of $R/I$
2) $(R/I) /(J / I) \cong R / J$.

### Fourth isomorphism theorem

##### _theorem:_ the fourth isomorphism theorem

Let $I \subset R$ be an ideal. There is an inclusion preserving bijection between the subrings $A$ of $R$ that contain $I$ and the set of subrings of $R/I$. Further, $A$ is an ideal if and only if $A / I$ is an ideal of $R / I$.