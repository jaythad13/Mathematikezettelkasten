---
tags:
- alg
- math-171
lecture: math-171-1
---

Given $2 + 5x = 16$ how do you find the value of $x$?

You can add $-2$ to both sides (which we usually think of as subtracting $2$), and then get $2 + (-2) + 5x = 16 + (-2)$. That gives us $0 + 5x = 14$. 

Note that in order to do this, we assumed that we had an additive inverse for $2$, and also that adding that to any other "number" would give us another "number". Obviously, to have an additive inverse, we must have an additive identity, $0$, and thus, we get $5x = 14$. 

From here, we multiply by $\frac{1}{5}$, giving us $\frac{1}{5} 5x = \frac{1}{5} 14$. Similarly, here we need multiplicative identity and multiplicative inverses to then get $1x = \frac{14}{5}$ and finally, $x = \frac{14}{5}$

##### _(very rough) definition:_ algebra

An algebra is a setting in which operations like addition, multiplication, scalar multiplication, et c. occur. 

### Structure

Algebra is about studying things that have structure. For contrast, we can look at examples of things that have no structure.

##### _example:_ sets have no structure

For us, it's usually good enough to think of a set as an unordered collection of different elements. Even though $\mathbb{R}$, $\mathbb{C}$, the set of rational points on an elliptic curve, et c. may usually be thought of as having some structure, when we think of them as just sets, they have no structure.

Even though sets themselves have no structure, we can think about structures that we can impose on "all" sets 

##### _example:_ structure on sets

For all the subsets of a set $X$ ($\mathcal{P}(X)$) we can think of the structure induced by taking unions and intersections of sets.

It turns out that this is an example of a binary operation.

##### _definition:_ binary operation, $h * g$

A binary operation $*$ on a set $G$ is a function $* : G \times G \to G$.

We often write $(h, g) \mapsto h * g$, and we often use other symbols.

##### _examples:_ binary operations

1) Exponentiation on $\mathbb{R}$ is a binary operation. Note that the same isn't true for $\mathbb{Q}$ because of roots and $\mathbb{Z}$ because of negative exponents, but is true for $\mathbb{N}$.
2) Addition on all $3 \times 3$ matrices, $\mathcal{M}_{3}(\mathbb{R})$, is a binary operation.
3) Function composition on polynomials (when we think of them as functions on $\mathbb{R}$)
4) Addition on $\mathbb{R}$.

##### _non-example:_ binary operation

A binary operation $\mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}$ by $(a, b) \mapsto \frac{a}{b}$ fails to be a binary operation on multiple counts — it isn't always in $\mathbb{Z}$ when it's defined, and it isn't always defined (if $b = 0$).

Some binary operations are nicer.

##### _definition:_ associativity

A binary operation $*$ on $G$ is associative if for all $a, b, c \in G$ we have $(a * b) * c = a * (b * c)$.

##### _definition:_ commutativity

A binary operation $*$ on $G$ is associative if for all $a, b \in G$ we have $a * b = b * a$.

This makes defining groups at least somewhat natural, if you've seen enough natural examples.

### Groups

Groups are just a nice sub-type of sets with binary relations.

##### _definition:_ group

A group is a set with a binary operation $(G, *)$ such that
1) $*$ is associative
2) there exists some $e \in G$ such that $a * e = a = e * a$ for all $a \in G$.
3) for all $a \in G$ there exists some $a^{-1} \in G$ such that $a * a^{-1} = e = a^{-1} * a$.

We call $e$ the identity of the group, and sometimes indicated that is the identity of $G$ by writing $e_{G}$. Sometimes we use $1$ and $1_{G}$ instead.

We call $a^{-1}$ the inverse of $a$.

##### _definition:_ abelian group, commutative group

A group $(G, *)$ is called abelian or commutative if $*$ is commutative.

##### _examples:_ groups

1) $\mathbb{Z}$ with addition is a group
2) $\mathbb{R}^\times$ with multiplication is a group
3) $\mathrm{GL}_{3}(\mathbb{R})$, the set of all $3 \times 3$ matrices with non-zero determinant is a group

##### _non-examples:_ groups

1) $\mathbb{R}^3$ with the cross product isn't a group — there isn't even an identity.
2) $\mathbb{N}$ with addition isn't a group — there isn't an identity.
3) Even if you add the identity to $\mathbb{N}$ by considering $\mathbb{Z}_{\ge 0}$, you still don't have a group since there are no inverses.





