---
tags:
- a-lie/3
- alg
- lie
- diff-geo
- self-study
---

It's only natural to consider maps of Lie algebras. They're exactly what you'd expect — linear maps that preserve the bracket too. 

##### _definition:_ Lie algebra homomorphism

A Lie algebra homomorphism $\varphi : L_{1} \to L_{2}$ is a [[Linear maps|linear map]] of [[Linear algebra done right --- ladr/notes/Vector spaces|vector spaces]] such that
$$
\varphi([x, y]) = [\varphi(x), \varphi(y)].
$$

A homomorphism of Lie algebras naturally has a kernel —

##### _definition, proposition:_ kernel

The kernel of a Lie algebra homomorphism $\varphi : L_{1} \to L_{2}$ is an ideal
$$
\ker \varphi = \{ x \in L_{1} \mid \varphi(x) = 0 \} \subseteq L_{1}.
$$

###### _proof:_

It follows from linear algebra that the kernel of a linear map is a vector subspace. Thus, we only need to show that the kernel has [[Lie algebras --- a-lie/notes/Subalgebras, ideals, and quotients#_definition _ (Lie) ideal|the absorption property]]. For any $x \in \ker \varphi$. $y \in L_{1}$, we have
$$
\varphi([x, y]) = [\varphi(x), \varphi(y)] = [0, \varphi(y)] = 0
$$
so $[x, y] \in \ker \varphi$. Thus, the kernel is an ideal.

A Lie algebra homomorphism also has an image —

##### _definition, proposition:_ image

The image of a Lie algebra homomorphism $\varphi : L_{1} \to L_{2}$ is a subalgebra
$$
\varphi^\text{img}(L_{1}) = \{ y \in L_{2} \mid \varphi(x) = y, x \in L_{1} \} \subseteq L_{2}.
$$

###### _proof:_

Again, it follows from linear algebra that this is a vector space. Thus, we only need to show that it is [[Lie algebras --- a-lie/notes/Subalgebras, ideals, and quotients#_definition _ Lie subalgebra|closed under the bracket]]. For any $y_{1}, y_{2} \in \varphi^\text{img}(L_{1})$, we have
$$
[y_{1}, y_{2}] = [\varphi(x_{1}), \varphi(x_{2})] = \varphi([x_{1}, x_{2}])
$$
which is clearly an element of the image. Thus, the image is a subalgebra.