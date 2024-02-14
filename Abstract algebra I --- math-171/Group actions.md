---
tags:
- alg
- math-171
lecture:
- math-171-7
- math-171-8
---

A lot of the time we think of groups as [[Dihedral groups and generators|representing the symmetries of an object]]. However, a symmetry of a thing is a finicky thing and sometimes its better to think of the group as acting on the object instead, keeping compositions of actions separate from states of the object.

##### _definition:_ group action

A group action of a group $G$ on a set $X$ is a map $G \times X \to X$ such that
- $g \cdot (h \cdot x) = (gh) \cdot x$ for all $g, h \in G$ and all $x \in X$
- $1 \cdot x$ for all $x \in X$.

##### _examples:_ group actions

1) A [[Vector spaces#_definition _ vector space|vector space]] is an [[Motivating groups#_definition _ abelian group, commutative group|abelian group]] $V$ acted on by the multiplicative group of its base [[An introduction to rings and fields#_definition _ fields|field]] $\mathbb{F}^\times$, with the additional requirement that the group action distributes over the operation on the abelian group and $0v = 0$.
2) $(\mathbb{Z}, +)$ acts on itself by translation — $z \cdot a = z + a$.
3) Any group $G$ acts on itself by left multiplication. This is called the left regular action of $G$. Note that this is only true for right multiplication if $G$ is abelian since $(gh) \cdot x = g \cdot (h \cdot x)$ implies that $x g h = x h g$.
4) A group $G$ also acts on itself by conjugation — by $g \cdot x = g x g^{-1}$. The identity case is trivial and
$$
\begin{split}
g \cdot (h \cdot x) & = g (h \cdot x) g^{-1} \\
& = g h x h^{-1} g^{-1}
& = 
\end{split}
$$
5) If $G$ is graph, then $\operatorname{Aut} g$ [[Group automorphisms and automorphism groups#_example _ the automorphism group of a symmetric graph|acts on the set of vertices]] of $G$.
6) $S_{\Omega}$ acts on $\Omega$ by permuting.

### Automorphisms from group actions

We can build [[Group automorphisms and automorphism groups|group automorphisms]] from group actions.

##### _definition:_ $\sigma_{g}$

Suppose $G$ acts on $X$. For some fixed $g \in G$ the function $\sigma_{g} : X \to X$ is defined by $x \mapsto g \cdot x$.

##### _theorem:_ group actions give rise to permutations

Suppose $G$ acts on $X$. For each $g \in G$, $\sigma_{g}$ is a permutation of $X$ and $\varphi : g \to \sigma_{g}$ is a [[Group homomorphisms#_definition _ group homomorphisms|group homomorphism]] $G \to S_{X}$ ([[Group combinatorics and symmetric groups#_definition _ the symmetric group on $ Omega$|the symmetric group]] on $X$).

##### _proof:_

First we will show that $\sigma_{g}$ is a bijection. If $\sigma_{g}(x) = \sigma_{g}(y)$, then $g \cdot x = g \cdot y$. Acting on both of these elements by $g^{-1}$ we get $x = y$. Thus, $\sigma_{g}$ is injective. For any $x \in X$ notice that $y = g^{-1} \cdot x$ gives us $\sigma_{g}(y) = x$. Thus, $\sigma_{g}$ is surjective. Since $\sigma_{g}$ is a bijection $X \to X$ it is a permutation $X \to X$. Notice that we could also show this by noticing that $\sigma_{{g^{-1}}}$ is a two-sided inverse for $\sigma_{g}$.

We can show that $\varphi$ is a homomorphism by explicit computation.
$$
\begin{split}
\varphi(gh)(x) & = (gh) \cdot x \\
& = g \cdot (h \cdot x) \\
& = g \cdot (\sigma_{h}(x)) \\
& = \sigma_{g}(\sigma_{h}(x)) \\
& = \sigma_{g} \circ \sigma_{h}(x) \\
& = (\varphi(g) \circ \varphi(h)) (x).
\end{split}
$$

That is, $\varphi(gh) = \varphi(g) \circ \varphi(h)$. Thus, $\varphi$ is a homomorphism $G \to S_X$.