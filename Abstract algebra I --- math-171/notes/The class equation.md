---
tags:
- alg
- comb
- alg-comb
- math-171/15x
---

### $G$ acting on itself by conjugation

We showed previously that an [[Abstract Algebra I --- math-171/notes/Group automorphisms and automorphism groups#_proposition _ inner automorphisms are actually automorphisms|inner automorphism]] $\varphi_{g} : x \mapsto gxg^{-1}$ is a homomorphism in $x$. It turns out that it is also a homomorphism in $g$ — it is a [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ (left) group action|group action]]! We call this the action of $G$ on itself by conjugation.

##### _proposition:_ inner automorphisms are group actions by conjugation

The group action $G \circlearrowright G$ by $g \cdot x = g x g^{-1}$ is a group action.

###### _proof:_

Clearly $1 x 1^{-1} = x$, so we just need to show $g \cdot (h \cdot x) = (gh) \cdot x$. We compute
$$
\begin{align}
g \cdot (h \cdot x) & = g \cdot (h x h^{-1}) \\
 & = g h x h^{-1} g^{-1} \\
 & = g h x (g h)^{-1} \\
 & = (gh) \cdot x.
\end{align}
$$

This action is very important!

##### _definition:_ conjugacy classes

The conjugacy classes of $G$ are the orbits of $G$ under its action on itself by conjugation — $a$ and $b$ are in the same class if there is some $g$ such that $g a g^{-1} = b$.

##### _example:_ conjugacy classes of some groups

1) The conjugacy classes of $\mathbb{Z}$ and any [[Abstract Algebra I --- math-171/notes/Groups, and why you should care#_definition _ abelian group, commutative group|abelian group]] are just the elements.
2) The conjugacy classes of [[Abstract Algebra I --- math-171/notes/Matrix groups and the quaternions|the quaternions]] $Q_{8}$ are all $\{ \pm q \}$ for $1 \neq q \in Q_{8}$ with $1$ and $-1$ forming their own conjugacy classes since they are in the [[Abstract Algebra I --- math-171/notes/Centralisers, centre, and normalisers#_definition _ centre, $C_{G}$|centre]] of the group — the conjugacy class of any $g \in Z(G)$ is just $\{ g \}$.
3) The conjugacy classes of $S_{3}$ are more complicated. They are $\{ \operatorname{id} \}, \{ (1 \, 2 \, 3), (1 \, 3 \, 2) \}$, $\{ (1 \, 2), (2\, 3), (3\, 1) \}$.

### The class equation

The class equation allows us to figure out the order of a group in terms of representatives of non-trivial conjugacy classes.

##### _theorem:_ the class equation

Let $G$ be a finite group and $g_{1}, \dots, g_{r}$ be representatives of the conjugacy classes that are not in the centre $Z(G)$. Then
$$
\lvert G \rvert = \lvert Z(G) \rvert  + \sum_{i = 1}^r \lvert G : Z_{G}(g_{i}) \rvert 
$$

###### _proof sketch:_

Since the conjugacy classes are equivalence classes, they partition the group. The elements in the centre of the group each have one-element conjugacy classes. We can compute the size of the rest of the conjugacy classes to be $\lvert G : Z_{G}(g_{i}) \rvert$ by [[Abstract Algebra I --- math-171/notes/Group actions#_theorem _ the orbit-stabiliser theorem|orbit-stabiliser theorem]] — the stabiliser of $g_{i}$ under conjugation is just all elements that commute with it.

##### _corollary:_ groups of prime power order have commuting elements

If $G$ is a (non-trivial) group of prime power order $p^a$, then it has non-trivial centre.

###### _proof:_

Note that each $\lvert G : Z_{G}(g_{i}) \rvert$ must be divisible by $p$ since they are all of the form $p^k$ (with $k \le a$) by [[Abstract Algebra I --- math-171/notes/Lagrange's theorem#_theorem _ Lagrange's theorem|Lagrange's theorem]] and $k \neq 0$ since that would imply $Z_{G}(g_{i})$ is the whole group, which we know is not true since the $g_{i}$ are not in the centre of $G$.

Thus, $p$ must divide $\lvert Z(G) \rvert = \lvert G \rvert - \sum_{i = 1}^r \lvert G : Z_{G}(g_{i}) \rvert$ as well.