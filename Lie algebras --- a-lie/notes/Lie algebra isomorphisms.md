---
tags:
- a-lie/3
- alg
- diff-geo
- lie
- self-study
---


It turns out that for the same reasons as for [[Abstract algebra --- math-171/notes/Group isomorphisms|groups]] and [[Abstract algebra --- math-171/notes/Ring homomorphisms#_definition _ ring isomorphisms, isomorphic|rings]], an invertible [[Lie algebras --- a-lie/notes/Morphisms of Lie algebras#_definition _ Lie algebra homomorphism|Lie algebra homomorphism]] has an inverse that is also a homomorphism. 

##### _definition:_ Lie algebra isomorphism

A Lie algebra isomorphism between Lie algebras $L_{1}$ and $L_{2}$ is an invertible Lie algebra homomorphism $\varphi : L_{1} \to L_{2}$.

Just as with [[Abstract algebra --- math-171/notes/Group homomorphisms|groups]] and [[Abstract algebra --- math-171/notes/Ring isomorphism theorems|rings]], there are isomorphism theorems for Lie algebras.

### First isomorphism theorem

##### _theorem:_ the first Lie algebra isomorphism theorem

If $\varphi : L_{1} \to L_{2}$ is a Lie algebra homomorphism, then $L_{1} / \ker \varphi \cong \varphi^\text{img}(L_{1})$ (uniquely).

###### _proof:_

We won't bother proving that the isomorphism is unique — it follows from a standard [[Basic category theory --- basic-cat/notes/An introduction to universal properties|universal property]] argument.

Consider the quotient map $\psi : L_{1} / \ker \varphi \to \varphi^\text{img}(L_{1})$ derived from $\varphi$ —
$$
\psi : x + \ker \varphi \mapsto \varphi(x).
$$

This is well defined since any two $x_{1}, x_{2} \in L_{1}$ with $x_{1} + \ker \varphi = x_{2} + \ker \varphi$ have $x_{1} - x_{2} \in \ker \varphi$, and thus $\varphi(x_{1}) = \varphi(x_{2})$.

This map is clearly a Lie algebra morphism since it inherits the properties of preserving sums, scaling, and brackets from $\varphi$. Since $\psi(x + \ker \varphi) = 0$ only if $x \in \ker \varphi$, $\psi(x + \ker \varphi) = 0$ only if $x + \ker \varphi = 0$. $\psi$ is also obviously surjective onto $\varphi^\text{img}(L_{1})$ — for $\varphi(x) \in \varphi^\text{img}(L_{1})$ we have $\psi(x + \ker \varphi) = \varphi(x)$. Thus, $\psi$ is the desired isomorphism giving $L_{1} / \ker \varphi \cong \varphi^\text{img}(L_{1})$.

##### _example:_ $\mathfrak{gl}_{2}(\mathbb{C}) = \mathfrak{sl}_{2}(\mathbb{C}) \oplus \mathbb{C}$

Consider the map
$$
\begin{align}
\varphi & : \mathfrak{gl}_{2}(\mathbb{C}) \to \mathfrak{sl}_{2}(\mathbb{C}) \\
 & : \begin{pmatrix}
a & b \\
c & d
\end{pmatrix} \mapsto \begin{pmatrix}
\frac{a - d}{2} & b \\
c & \frac{d - a}{2}
\end{pmatrix}.
\end{align}
$$
It turns out this isn't just a linear map — it preserves the bracket too!

Clearly, $\ker \varphi$ is just all scalar multiples of the identity matrix since we require $b = c = 0$ and $a - d = 0 \implies a = d$. That is, $\ker \varphi \cong \mathbb{C}$. It's also not difficult to show $\varphi$ is surjective. Thus, by the first isomorphism theorem, $\mathfrak{sl}_{2}(\mathbb{C}) \cong \mathfrak{gl}_{2}(\mathbb{C}) / \mathbb{C}$.

We can also consider the map
$$
\begin{align}
\pi & : \mathfrak{gl}_{2}(\mathbb{C}) \to \mathbb{C} \\
 & : A \mapsto \operatorname{tr} A.
\end{align}
$$
It's even more clear that the kernel of this map is the set of traceless of matrices $\mathfrak{sl}_{2}(\mathbb{C})$ and that it is surjective on $\mathbb{C}$. Thus, again, by the first isomorphism theorem, $\mathbb{C} \cong \mathfrak{gl}_{2}(\mathbb{C}) / \mathfrak{sl}_{2}(\mathbb{C})$.

This allows us to say that $\mathfrak{gl}_{2}(\mathbb{C})$ is the direct sum of these two ideals. Also this is a "proof" that $\mathfrak{sl}_{2}(\mathbb{C})$ and $\mathbb{C}$ are ideals.

### Second isomorphism theorem

##### _theorem:_ the second Lie algebra isomorphism theorem 

If $I, J$ are ideals of the Lie algebra $L$, then $(I + J) / J \cong I / I \cap J$.

###### _proof sketch:_

Apply the first isomorphism theorem to
$$
\begin{align}
\varphi & : I + J \to I / I \cap J \\
 & : i + j \mapsto i + I \cap J.
\end{align}
$$

### Third isomorphism theorem


##### _theorem:_ the third Lie algebra isomorphism theorem 

If $I \subseteq J$ are ideals of the Lie algebra $L$, then $(L / I) / (J / I) \cong L / J$.

###### _proof sketch:_

Apply the first isomorphism theorem to
$$
\begin{align}
\varphi & : L / I \to L / J \\
 & : x + I \to x + J.
\end{align}
$$