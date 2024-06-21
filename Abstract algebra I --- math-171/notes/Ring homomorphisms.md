---
tags:
- alg
- math-171
lecture:
- math-171-17
---

Ring homomorphisms of a ring $R$ are [[Abstract Algebra I --- math-171/notes/Group homomorphisms#_definition _ group homomorphisms|group homomorphisms]] of $(R, +)$ that respect the multiplication on $R$ too.

##### _definition:_ ring homomorphisms

Let $R$ and $S$ be rings. A map $\varphi : R \to S$ is a ring homomorphism if for all $a, b \in R$
$$
\varphi(ab) = \varphi(a) \varphi(b)
$$
and
$$
\varphi(a + b) = \varphi(a) + \varphi(b).
$$

##### _proposition:_ images and kernels

For any ring homomorphism $\varphi : R \to S$,
1) $\operatorname{im} \varphi$ is a subring of $S$
2) $\ker \varphi$ is a two-sided ideal of $R$ (and thus, also a subring)

###### _proof:_

1) Suppose $r, s \in \operatorname{im} \varphi$ with $\varphi(a) = r$ and $\varphi(b) = s$. Thus, $r + s = \varphi(a + b) \in \operatorname{im} \varphi$ and $rs = \varphi(ab) \in \operatorname{im} \varphi$ giving us that $\operatorname{im} \varphi$ is a subring.
2) Suppose $a, b \in \ker \varphi$ and $r \in R$. Then $\varphi(a + b) = \varphi(a) + \varphi(b) = 0_{S}$ and $\varphi(ab) = \varphi(a) \varphi(b) = 0_{S}$ and thus, $\ker \varphi$ is a subring. Also $\varphi(ra) = \varphi(r) \varphi(a) = \varphi(r) 0_{S} = 0_{S}$ and similarly for right multiplication by $R$, giving us that $\ker \varphi$ is a two-sided ideal.

##### _examples:_ ring homomorphisms

1) $\varphi : \mathbb{Z} \to \mathbb{Z} / n \mathbb{Z}$ by $x \mapsto \overline{x}$ is a surjective homomorphism with $\ker \varphi = n \mathbb{Z}$.
2) $\varphi : \mathbb{R}[x] \to \mathbb{R}$ by $p \mapsto p(0)$ is a very surjective homomorphism with $\ker \varphi = \{ p \in \mathbb{R}[x] \mid p \text{ has constant term } 0 \}$.
3) In fact, in general for a ring $A$, a nonempty set $X$, and $R$, the ring of functions $X \to A$, $$
\begin{split}
\alpha_{x} : & R \to A \\
& f \mapsto f(x)
\end{split}
$$
	for some fixed $x$ is a ring homomorphism.

### Isomorphism

With homomorphisms we can define isomorphisms in a natural way —

##### _definition:_ ring isomorphisms, isomorphic

We say a ring homomorphism $\varphi : R \to S$ is an isomorphism if it's bijective.

We say $R \cong S$ ($R$ is isomorphic to $S$) if there exists an isomorphism $\varphi : R \to S$.