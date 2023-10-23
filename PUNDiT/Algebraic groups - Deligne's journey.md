---
tags:
- alg
---

### What's a group?

> A group is a formal codification of a symmetry type

\- Cris Negron

##### _example:_ cyclic symmetry type, representations

The group $C_n$ codifies rotational symmetry like
- rotating the plane $\bb{R}^2$ by multiples of $\frac{2 \pi}{n}$
- cyclically permuting $n$ numbers
- in $\bb{R}^3$, rotating the $xy$-plane by $\frac{2 \pi}{n}$ around the $z$-axis

These are representations of $C_n$ (not exactly, there's some subtleties with the second example)

##### _example:_ $\bb{Z}/2\bb{Z}$ symmetry

$\bb{Z}/2\bb{Z}$ codifies the symmetry of flipping about an axis. For example, if $f(-x) = -f(x)$, the function $f$ possesses this symmetry. This is useful because for such $f$
$$
\int_{-a}^a f(x) \, dx = 0.
$$

The lesson is that a group allows you to simplify things with symmetry.

The groups we've talked about so far are discrete (finite). But we can think about continuous symmetry too!

### Algebraic groups

##### _example:_ $\bb{GL}_2(\bb{R)}$

$\bb{GL}_2(\bb{R})$ is the set of two by two matrices with non-zero determinant. It's interesting because it's a space!

$M_2(\bb{R})$ is clearly a $4$-dimensional vector space. But note, that the vanishing of the determinant (where we think of the determinant as a polynomial on the entries of the matrix) is a closed set. Then it's complement is open! So we can do calculus on the complement! And the complement is just $\bb{GL}_2(\bb{R})$.

So what symmetries does $\bb{GL}_2(\bb{R})$ codify?

They codify linear transformations on $\bb{R}^2$! More importantly, they codify invertible linear transformations on $\bb{R}^2$, which we can just think of as a change of basis!

Where does the smoothness come in?

There's always some small bit I can move $A_{j, k}$ for $A \in \bb{GL}_2 (\bb{R})$, I stay inside $\bb{GL}_2 (\bb{R})$! That is, $\bb{GL}_2(\bb{R})$ is a group with smooooooooth structure, and linear transformations on $\bb{R}^2$ are a representation of it!

We have more examples of these 

##### _examples:_ algebraic groups

1) $SL_n{\bb{R}}$? Is the vanishing still closed? 
2) $\bb{R}$ - both the additive and multiplicative groups on it
3) $O_n{\bb{R}}$ - the group of orthogonal matrices

It turns out that these things are really fun! Despite them often being uncountably large and multiple dimensional, usually the continuity takes care of stuff and leaves behind just a "crystalline structure" of the group.

### Why do algebraic groups matter?

They appear a lot in physics! Specifically, when you're doing physics on some space $X$, where you can do calculus, the physics is usually defined by some function $f$ on $X$. We can find some continuous symmetry on $X$ that preserves $f$ and that helps us do physics better!



