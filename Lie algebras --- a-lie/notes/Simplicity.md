---
tags:
- a-lie/5
- lie
- alg
- diff-geo
---

Again, echoing the definition of simplicity for groups, we say Lie algebras are simple if they don't contain any meaningful inner substructure. To prevent pathologies, we don't allow trivial Lie algebras to be simple.

##### _definition:_ simple

A non-[[Lie algebras --- a-lie/notes/Lie algebras#_definition _ abelian Lie algebra|abelian]] Lie algebra $L$ is simple if it has no non-trivial ideals.

### The radical

The solubility of ideals of a Lie algebra gives us better insight into the structure of the Lie algebra than just the ideals in general. We can study them all together in the ideal that contains all of these ideals.

##### _proposition, definition:_ the radical of a Lie algebra

For a finite-dimensional Lie algebra $L$ there exists a unique [[Lie algebras --- a-lie/notes/Solubility#_definition _ soluble|soluble]] ideal that contains all soluble ideals of $L$. 

It is called the radical of $L$ and is denoted $\operatorname{rad} L$.

###### _proof:_

Consider the set of all soluble ideals of $L$, and choose $R$ to be an ideal of maximal dimension. For any other soluble ideal $I$, since $R + I$ is soluble, it must have dimension at most $\dim R$, but also, $R + I$ has dimension $\dim (R + I)\ge \dim R$. Thus, $\dim(R + I) = \dim R$. This only happens if $I \subset R$. Thus, $R$ contains all ideals.

Suppose there is another such soluble ideal. Then they must contain each other, and thus, be the same ideal. That is, $R$ is unique.

### Semisimplicity

With the notion of the radical, we can define semisimplicity of Lie algebras.

##### _definition:_ simple, semisimple

A non-abelian Lie algebra $L$ is semisimple if it has no non-trivial soluble ideals, or equivalently, $\operatorname{rad} L = 0$.

One example of a semisimple Lie algebra is just any Lie algebra mod its radical.

##### _proposition:_ $L / \operatorname{rad} L$ is semi-simple

###### _proof sketch:_

We never stated a fourth isomorphism theorem [[Lie algebras --- a-lie/notes/Lie algebra isomorphisms|for Lie algebras]], but there exists one that is the same as the fourth isomorphism theorem [[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the fourth isomorphism theorem|for rings]]. Here, we see that the ideals in $L / \operatorname{rad} L$ are exactly $J / \operatorname{rad} L$ for ideals $J \supset \operatorname{rad }L$.

If $J / \operatorname{rad} L$ were soluble, then since $\operatorname{rad} L$ is also soluble, we would have to have $J$ soluble. Thus, $J \subset \operatorname{rad} L$, giving us $J = \operatorname{rad} L$ by double inclusion. Thus, $J / \operatorname{rad} L = 0$ — any soluble ideal is trivial.