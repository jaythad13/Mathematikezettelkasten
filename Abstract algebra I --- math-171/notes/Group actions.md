---
tags:
- alg
- math-171/7
- math-171/8
- math-171/15x
---

A lot of the time we think of groups as [[Dihedral groups and generators|representing the symmetries of an object]]. However, a symmetry of a thing is a finicky thing and sometimes its better to think of the group as acting on the object instead, keeping compositions of actions separate from states of the object.

##### _definition:_ (left) group action

A (left) group action of a group $G$ on a set $X$ is a map $G \times X \to X$ such that
- $g \cdot (h \cdot x) = (gh) \cdot x$ for all $g, h \in G$ and all $x \in X$
- $1 \cdot x$ for all $x \in X$.

We often write the action of $G$ on $X$ by $G \circlearrowright X$.

Note that there is also a sensible definition of a right group action where $g \cdot (h \cdot x) = (hg) \cdot x$ but we will rarely have need to use this.

##### _examples:_ group actions

1) A [[Vector spaces#_definition _ vector space|vector space]] is an [[Abstract Algebra I --- math-171/notes/Groups, and why you should care#_definition _ abelian group, commutative group|abelian group]] $V$ acted on by the multiplicative group of its base [[Abstract Algebra I --- math-171/notes/Fields#_definition _ fields|field]] $\mathbb{F}^\times$, with the additional requirement that the group action distributes over the operation on the abelian group and $0v = 0$.
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

Obviously, a group action induces structure on the set it acts on. One very important notion is that of an orbit —

##### _definition:_ orbit

The orbit of $x \in X$ under an action $G \circlearrowright X$ is $\mathcal{O}_{G}(x)$. the set of all $y \in X$ such that $y = g \cdot x$ for some $g \in G$. 

We verify in [[Abstract Algebra I --- math-171/attachments/homework/hw 7/hw 7.pdf#page=3|the homework]] that the equivalence relation $x \sim y$ if $y = g \cdot x$ for some $g \in G$ is an equivalence relation. We can understand the orbits as equivalence classes under this relation. Note that this means the orbits partition $X$!

Another important notion is that of fixed points.

##### _definition:_ fixed point

A fixed point of $g \in G$ under an action $G \circlearrowright X$ is $x$ such that $g \cdot x = x$.

We usually write the set of all fixed points of $g$ as $\operatorname{fix}_{X}(g)$.

It's also notable that a group action induces structure on the group itself. Again, in [[Abstract Algebra I --- math-171/attachments/homework/hw 7/hw 7.pdf#page=1|the homework]] we verify that the subsets below really are [[Abstract Algebra I --- math-171/notes/Subgroups#_definition _ subgroup, $ le$|subgroups]].

##### _definition:_ stabiliser

The stabiliser of $x \in X$ under a group action $G \circlearrowright X$ is $\operatorname{stab}_{G} x$, the subgroup of all $g \in G$ that fix $X$ — all $g \in G$ with $g \cdot x = x$.

Note that a stabiliser is sort of "dual" to the notion of the set of fixed points.

##### _definition:_ kernel

The kernel of a group action $G \circlearrowright X$ is $\ker (G \circlearrowright X)$, the set of all $g \in G$ that fix all $x \in X$ — all $g \in G$ such that $g \cdot x = x$ for any $x \in X$.

There is an incredibly useful theorem relating the structure on $G$ (stabilisers) and the structure on $X$ (orbits). This allows us to understand the structure of finite groups through [[Abstract Algebra I --- math-171/notes/The class equation#_theorem _ the class equation|the class equation]] and [[Abstract Algebra I --- math-171/notes/Sylow's theorem|the Sylow theorems]], and it gives us a powerful tool to solve combinatorial problems in [[Abstract Algebra I --- math-171/notes/Burnside's lemma]].

##### _theorem:_ the orbit-stabiliser theorem

Consider a group action of $G$ on a non-empty set $X$. For each $x \in X$ the size of the orbit containing $x$ is $\lvert G : \operatorname{stab}_{G}(x) \rvert = \lvert G \rvert / \lvert \operatorname{stab}_{G}(x) \rvert$ .

###### _proof:_

The notation referring to [[Abstract Algebra I --- math-171/notes/Lagrange's theorem#_definition _ index, $ lvert G H rvert$|the index]] of $\operatorname{stab}_{G}(x)$ is deliberate. Consider the map from the orbistat of $x$ to the set of cosets of $\operatorname{stab}_{G}(x)$ $g \cdot x \mapsto g \operatorname{stab}_{G}(x)$. This map is in fact well defined — if $g_{1} \cdot x = g_{2} \cdot x$ then $g_{1}$ differs from $g_{2}$ by an element $h \in \operatorname{stab}_{G}(x)$, so they have the same coset. We claim this is a bijection.

If $g_{1} \operatorname{stab}_{G}(x) = g_{2} \operatorname{stab}_{G}(x)$, then $g_{1}^{-1} g_{2} \in \operatorname{stab}_{G}(x)$. That is, $(g_{1}^{-1} g_{2}) \cdot x = x$, and thus,
$$
g_{1} \cdot x = g_{1} \cdot ((g_{1}^{-1} g_{2}) \cdot x) = g_{2} \cdot x.
$$
That is, the map is injective. The map is clearly surjective, since all the orbit of $x$, by definition contains all $g \cdot x$ and thus, map to all $g \operatorname{stab}_{G}(x)$.

Since this is a bijection, the sizes of the sets are the same. The last equality is just [[Abstract Algebra I --- math-171/notes/Lagrange's theorem#_theorem _ Lagrange's theorem|Lagrange's theorem]].

### Permutations from group actions

An important perspective to have is understanding group actions as homomorphisms to the [[Abstract Algebra I --- math-171/notes/Group combinatorics and symmetric groups#_definition _ the symmetric group on $ Omega$|symmetric group]] of the set they act on.

##### _definition:_ $\sigma_{g}$

Suppose $G$ acts on $X$. For some fixed $g \in G$ the function $\sigma_{g} : X \to X$ is defined by $x \mapsto g \cdot x$.

##### _theorem:_ group actions give rise to permutations

Suppose $G$ acts on $X$. For each $g \in G$, $\sigma_{g}$ is a permutation of $X$ and $\varphi : g \to \sigma_{g}$ is a [[Group homomorphisms#_definition _ group homomorphisms|group homomorphism]] $G \to S_{X}$ ([[Group combinatorics and symmetric groups#_definition _ the symmetric group on $ Omega$|the symmetric group]] on $X$).

###### _proof:_

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