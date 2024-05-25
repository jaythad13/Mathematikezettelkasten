---
tags:
- self-study
- lin-alg
---

> A vector is just an instruction for how to add it.

\- Peter Kagey

We have many notions of vectors - as lists of numbers, numbers arranged in column or row matrices, as "directed line segments", or as arrows from the origin. All of these are vectors, and none of them are all the vectors. What a vector really is is what they have in common. All of them encode ways to add things, and scale things. We add lists of numbers member-wise, column and row matrices coordinate-wise, and directed line segments and arrows by joining them to other vectors of their kind tip-to-tail. Similarly, we scale lists member-wise, column and row matrices coordinate-wise, and stretch directed line segments and arrows by a scaling factor.

##### _example:_ vectors as an instruction for how to add them

When we first see vectors in $\bb{R}^2$, the way we are taught to think of the correspondence between a vector, say $(1, 3)$ and the arrow that corresponds to it in the plane, is

> Move $1$ along the $x$-axis and $3$ along the $y$-axis.

If we think a little deeper about this "instruction", we can see that what it's telling us is also how to add the vector $(1, 3)$ to any other vector. When we carry out this "instruction" from the origin, we get $(0, 0) + (1, 3) = (1, 3)$, and then it is natural to think of this as just a way to get the vector. However, when we move accordingly, starting from some vector $(a, b)$, we can scarcely ignore that we get $(a, b) + (1, 3) = (a + 1, b + 3)$. What this tells us is that the reason this correspondence between the geometric and the purely algebraic exists is that we have notions of adding that correspond exactly. The essence of the vector is in how you add it.

Note that here we haven't mentioned scaling, but it wouldn't be too difficult to explain how it's really scaling together with addition that gives us the essence of a vector.

Because, it's only addition and scaling that make up the essence of a vector, for us to call something a vector, it need only add and scale in the ways that we typically associate with vectors. This is then what we use to define vectors. Since vectors typically come as a set of vectors, all with the same notion of addition and scaling, we define what this addition and scaling should look like for the set to be a vector space, and then define anything that is a member of a vector space as a vector:

##### _definition:_ vector space

A vector space $V$ is a set with a [[Fields|field]] $\bb{F}$ and the following functions:
- A binary operation, addition $a : V \times V \to V$ where $a(u, v)$ is usually written as $u + v$ for $u, v \in V$.
- Scaling, $s : \bb{F} \times V \to V$ where $s(\lambda, v)$ is usually written as $\lambda v$ for $\lambda \in \bb{F}$ and $v \in V$.
such that, for all $u, v, w \in V$ and $\alpha, \beta \in \bb{F}$
- Addition is commutative: $u + v = v + u$
- Addition and scaling are associative: $(u + v) + w = u + (v + w)$ and $\alpha(\beta v) = (\alpha \beta) v$
- The additive identity $0$ such that $v + 0 = 0$ exists
- The additive inverse $-v$ exists such that $v + (-v) = 0$
- For the multiplicative identity $1 \in \bb{F}$, we have $1 v = v$.
- Scaling distributes over addition as follows: $\alpha (u + v) = \alpha u + \alpha v$ and $(\alpha + \beta) v = \alpha v + \beta v$

