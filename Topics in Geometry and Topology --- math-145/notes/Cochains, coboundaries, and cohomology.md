---
tags:
- math-145/6
- alg-top
---

### Cochains

Cochains are dual to chains. The following definition is then natural.

##### _definition:_ cochain

A $k$-cochain is an element of the dual space to the [[Topics in Geometry and Topology --- math-145/notes/Chains revisited#_definition _ $0$, $1$, and $2$-chains|space of chains]] — it is an element of $\mathrm{C}_{k}^\vee(U, \mathbb{F})$. Thus, a $k$-cochain is a linear map $\mathrm{C}_{k}(U, \mathbb{F}) \to \mathbb{F}$.

The space of $k$-cochains (over $U$, with coefficients in $\mathbb{F}$) is denoted $\mathrm{C}^k(U, \mathbb{F})$.

##### _example:_ cochains we've seen already

1) The "[[Topics in Geometry and Topology --- math-145/notes/Chains revisited#_definition _ the mass cocycle|mass cocycle]]" is also a $0$-cochain
2) The "[[Topics in Geometry and Topology --- math-145/notes/Discrete winding number#_definition _ angle cocycle|angle cocycle]]" $\theta$ is also a $1$-cochain.
3) The [[Topics in Geometry and Topology --- math-145/attachments/homework/hw 1/hw 1.pdf#page=11|area]] of a $2$-cycle, defined to be the area enclosed by its boundary is a $2$-cochain.

The [[Topics in Geometry and Topology --- math-145/notes/Discrete winding number#_theorem _ winding number|winding number]] (defined by [[Topics in Geometry and Topology --- math-145/notes/Discrete winding number#_proposition _ the ray escape formula|the ray escape formula]]) and $\theta / 2 \pi$ are $1$-cochains that agree on $1$-cycles — they are called cohomologous.

### Coboundaries and cocycles

To get a construction like that of homology from these arrows going in the "wrong" direction, we want arrows going from $\mathrm{C}^0 \to \mathrm{C}^1 \to \mathrm{C}^2$ also in the "wrong" direction (as compared to [[Topics in Geometry and Topology --- math-145/notes/Chains revisited#_definition _ boundary of a $1$-chain|boundary maps]]). These are just going to be the dual maps to the boundary maps.

##### _definition:_ $k$-coboundary map, coboundary of a $k$-cochain, derivative

Given $\varphi \in \mathrm{C}^k(U, \mathbb{F})$, the coboundary (or derivative) of $\varphi$ is $\delta_{k} \varphi \in \mathrm{C}^{k + 1}(U, \mathbb{F})$ by
$$
(\delta_{k} \varphi)[\mathbf{a}_{1}, \dots, \mathbf{a}_{k + 1}] = \varphi (\partial_{k} [\mathbf{a}_{1}, \dots, \mathbf{a}_{k + 1}]).
$$

The space of coboundaries is the image of a boundary map — a $(k + 1)$-coboundary is an element of $\operatorname{img} \delta_{k} = \mathrm{B}^{k + 1}$.

##### _example:_ $0$-coboundary

For example, any $0$-coboundary $\delta_{0} \varphi$ of a $0$-cochain $\varphi$ is given by $(\delta_{0} \varphi)[\mathbf{a}, \mathbf{b}] = \varphi([\mathbf{b}] = [\mathbf{a}])$.

Naturally, the cochains that have $0$ coboundary, are just cochains that are $0$ on boundaries. These are special enough to deserve a name — since they reverse the arrows of cycles, they are cocycles.

##### _definition:_ cocycle

A $k$-cocycle is a $k$-cochain that has $0$ coboundary — a cochain in $\ker \delta_{k}$.

The space of all $k$-cocycles is $\mathrm{Z}^k = \ker \delta_{k}$.

##### _definition:_ cohomology

The $k$th cohomology space (of $U$ over $\mathbb{F}$) is the quotient $\mathrm{H}^k(U, \mathbb{F}) = \mathrm{Z}^k(U, \mathbb{F}) / \mathrm{B}^k(U, \mathbb{F})$.

The dimension of the $k$th cohomology space is the $k$th dual Betti number $\mathrm{b}^k$.

### Duality!

Cohomology and homology at least appear to count the same things.

##### _example:_ zeroth cohomology counts [[Topics in Geometry and Topology --- math-145/notes/Homology in the plane#_definition _ polygonally path-connected, component|polygonally path-connected]] components

If $U$ has three polygonally path connected components, then any $0$-cocycle $\varphi$ must be constant on each connected component — given a path $\gamma$ between $\mathbf{a}, \mathbf{b}$, since $\varphi$ sends $\partial_{0}(\gamma) = [\mathbf{b}] - [\mathbf{a}]$ to zero, $\varphi[\mathbf{a}] = \varphi[\mathbf{b}]$. Thus, $\varphi$ is determined by choice on the three components. There are no coboundaries (or only the $0$ function is a coboundary).

##### _example:_ first cohomology (at least) counts holes

If $U$ has two holes, then the winding numbers about points in those holes are linearly independent cocycles (by [[Topology --- math-147/attachments/homework/hw 1/hw 1.pdf#page=2|the distant cycle lemma]])

The fact that homology gives [[Topics in Geometry and Topology --- math-145/notes/Homology in the plane#What does homology count?|the same answers]] suggests a duality theorem. 

##### _theorem:_ cohomology is dual to homology 

The cohomology (of a region $U$ over a field $\mathbb{F}$) is isomorphic to the dual space of the homology. That is,
$$
\mathrm{H}^k(U, \mathbb{F}) \cong \mathrm{H}_{k}^\vee(U, \mathbb{F}).
$$
###### _proof:_

Every cocycle $\varphi \in \mathrm{Z}^k$ defines a linear map $\tilde{\varphi} : \mathrm{H}_{k} \to \mathbb{F}$. Since $\varphi$ is a linear map on all of $\mathrm{C}_{k}$, it restricts to a map on $\mathrm{Z}_{k}$. Since cocycles are zero on boundaries $\mathrm{B}_{k}$, we can get a quotient map on $\mathrm{Z}_{k} / \mathrm{B}_{k} = \mathrm{H}_{k}$. This is the map $\tilde{\varphi}$. Write $\Psi$ for the map $\mathrm{Z}^k \to \mathrm{H}_{k}^\vee$ by $\varphi \mapsto \tilde{\varphi}$.

If $\varphi$ is a coboundary, then $\tilde{\varphi} = 0$ — if $\varphi$ is a coboundary, $\varphi$ is zero on all cycles in $\mathrm{Z}_{k}$ since it sends them to their non-existent boundary before acting on them. Thus $\mathrm{B}^k \subseteq \ker \Psi$. 

Suppose $\tilde{\varphi} = 0$. Extend it to a map $\overline{\tilde{\varphi}} : \mathrm{C}_{k} \to \mathbb{F}$ and then since it vanishes on $\mathrm{Z}_{k}$, it descends to $\tilde{\overline{\tilde{\varphi}}} : \mathrm{C}_{k} / \mathrm{Z}_{k} \to \mathbb{F}$ which we will just call $\phi$. By the first isomorphism theorem, 
$$
\mathrm{C}_{k} / \mathrm{Z}_{k} \cong_{\tilde{\partial}_{k - 1}} \mathrm{B}_{k - 1}
$$
Thus, $\tilde{\theta} = \phi \circ \tilde{\partial}_{k - 1}^{-1}$ is a map $\mathrm{B}_{k - 1} \to \mathbb{F}$ through this isomorphism. Thus, $\phi = \theta \circ \tilde{\partial}_{k - 1}$. Lifting back up (erasing the quotients by $\mathrm{Z}_{k}$) by setting everything $0$ on $\mathrm{Z}_{k}$, we get $\overline{\tilde{\varphi}} = \theta \circ \partial_{k - 1}$. Thus, we have reversed the inclusion and shown $\ker \Psi = \mathrm{B}^k$

Finally $\varphi \mapsto \tilde{\varphi}$ is surjective — given any $\psi \in \mathrm{H}_{k}^\vee$, we can lift to a map on $\psi \in \mathrm{Z}_{k}^\vee$ by setting $\psi = 0$ on $\mathrm{B}_{k}$. By the extension lemma, we can extend to $\overline{\psi}$ on $\mathrm{C}_{k}$, which is a cocycle since it vanishes on boundaries. (For example, extend winding number to angle cocycle in general).

By the first isomorphism theorem, $\mathrm{H}^k(U, \mathbb{F}) = \mathrm{Z}^k(U, \mathbb{F}) / \mathrm{B}^k(U, \mathbb{F}) \cong \mathrm{H}_{k}^\vee(U, \mathbb{F})$.

For finite dimensional homology, there is obviously an isomorphism $\mathrm{H}_{k}(U, \mathbb{F}) \cong \mathrm{H}^k(U, \mathbb{F})$ and thus, an isomorphism between homology and cohomology. Notice that for infinite dimensional spaces there doesn't have to be such an isomorphism (infinite sequences with finite support have countable basis, but their dual space, all infinite sequences is everything).

##### _lemma:_ the extension lemma

Let $V$ be a vector space, $U$ a subspace of $V$ and $W$ another vector space. Then any linear map $T : U \to W$ can be extended to a map $\overline{T} : V \to W$.

###### _proof sketch:_

By Zorn's lemma, a basis of $U$ exists and can be extended to a basis on $V$. Do the obvious thing to get a linear map (though it may require the axiom of choice to do it?).
