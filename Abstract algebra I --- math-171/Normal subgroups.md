---
tags:
- math-171
- alg
lecture:
- math-171-12
- math-171-13
---

We've seen enough [[Fibres and quotients|examples]] of quotient groups. Now we want to see whether it makes sense to quotient out by any subgroup or there are some restrictions on what we can quotient out by.

### Normal subgroups

%% fill in from the lecture notes %%

### Quotient groups

Now we want to relate [[Fibres and quotients#_definition, theorem _ the quotient group is a group|quotients]] to normal subgroups in the obvious way that we've been hinting at this whole time — the subgroups you can quotient out are exactly the normal subgroups.

##### _theorem:_ quotients are only those of normal subgroups

If $N \le G$, then the binary operation on the [[Fibres and quotients#_definition _ cosets|cosets]] of $N$ by
$$
(gN)(hN) = (gh)N
$$
is well defined if and only if $N \trianglelefteq G$.

##### _proof:_

We have already shown that we need $N \trianglelefteq G$ for the binary operation to be well-defined in our motivation for defining the normal subgroup. Now we will show the converse.

Suppose we have $N \trianglelefteq G$. Suppose that we have $xN = x'N$ and $yN = y'N$. Notice then that we can write $x = n_{1}x'$ and $y = y'n_{2}$ for $n_{1}, n_{2} \in N$. Thus,
$$
\begin{split}
xy & = x' n_{1} y' n_{2} \\
 & = x' y' y'^{-1} n_{1} y'n_{2} \\
 & = x' y'(y'^{-1} n_{1} y')n_{2} \\
 & = x'y'n_{3} n_{2}
\end{split}
$$
and thus
$$
(xy)N = (x'y')N
$$
the binary operation is well defined.

##### _theorem:_ normal subgroups are the kernel of a homomorphism

$N \trianglelefteq G$ if and only if it is the kernel of some homomorphism from $G$.

##### _proof:_

We've already shown that kernels are normal subgroups. Now we just show that normal subgroups are kernels.

Note that since the binary operation by representative multiplication on cosets is well defined, we can talk about the natural projection
$$
\begin{split}
\pi : \, &G \to G /N \\
& g \mapsto gN.
\end{split}
$$
which has kernel $N$ since $nN = 1_{G}N$ (left action is a bijection).

### On being normal

##### _proposition:_ normality is not transitive

If $K \trianglelefteq H$ and $H \trianglelefteq G$, we don't necessarily have $K \trianglelefteq G$.