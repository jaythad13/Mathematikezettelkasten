---
tags:
- alg
- math-171/12
- math-171/13
---

We've seen enough [[Fibres and quotients|examples]] of quotient groups. Now we want to see whether it makes sense to quotient out by any subgroup or there are some restrictions on what we can quotient out by.

### Normal subgroups

[[Abstract Algebra I --- math-171/notes/Fibres and quotients#_definition, theorem _ the quotient group is a group|We've seen]] that there's a natural group structure on the cosets of a homomorphism kernel. Do we need a subgroup to be a kernel to quotient out by it in that way? Can all subgroups be kernels? Yes and no.

For the quotient of a group $G$ by a subgroup $H$ to have a reasonable structure, we would want the canonical projection $\pi : G \to G/H$ by $g \mapsto gH$ to be a homomorphism. That is, we want $(x H)(y H) = (x y) H$.

Obviously, this needs to be well defined — if $x_{1} H = x_{2} H$ and $y_{1} H = y_{2} H$ we want $(x_{1} y_{1}) H = (x_{2} y_{2}) H$. Particularly, since $hH = 1_{G}H$, we need $(gH)(hH)(g^{-1}H) = 1_{G} H$ for all $g \in G$ and all $h \in H$. This will only happen if $ghg^{-1} \in H$ for all $g$. Note that this is the condition as the [[Abstract Algebra I --- math-171/notes/Centralisers, centre, and normalisers#_definition _ normaliser, $N_{G}(A)$|normaliser]] being the whole group. That's why we call these groups normal!

##### _definition:_ normal subgroups

A subgroup $N \le G$ is normal in $G$ if $ghg^{-1} \in N$ for all $g \in G$ and all $h \in N$.

We denote that $N$ is normal in $G$ by $N \trianglelefteq G$.

Basically, if the group was abelian, we could easily avoid all of this struggle just as easily as we did with [[Linear algebra done right --- ladr/notes/Quotients spaces|quotient spaces]], but because it's not, we have to settle for normality — the next best thing.

### Quotient groups

Now we want to relate [[Fibres and quotients#_definition, theorem _ the quotient group is a group|quotients]] to normal subgroups in the obvious way that we've been hinting at this whole time — the subgroups you can quotient out are exactly the normal subgroups.

##### _theorem:_ quotients are exactly those of normal subgroups

If $N \le G$, then the binary operation on the [[Fibres and quotients#_definition _ cosets|cosets]] of $N$ by
$$
(gN)(hN) = (gh)N
$$
is well defined if and only if $N \trianglelefteq G$.

###### _proof:_

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

###### _proof:_

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

###### _proof:_

In $D_{8}$, $\left< s \right> \trianglelefteq \left< s, r^2 \right> \trianglelefteq D_{8}$ (because each subgroup has [[Abstract Algebra I --- math-171/notes/Lagrange's theorem#_proposition _ index $2$ subgroups are normal|index 2]] in the next with orders 2, 4, and 8 respectively). However $\left< s \right>$ is not normal in $D_{8}$ since $rsr^{-1} = sr^{2} \not\in \left< s \right>$. Note that $sr^{2}$ is still in $\left< s, r^{2} \right>$ since [[Abstract Algebra I --- math-171/notes/Group automorphisms and automorphism groups#_proposition _ inner automorphisms are actually automorphisms|inner automorphisms]] of $D_{8}$ fix $\left< s, r^{2} \right>$. The problem is that even if a subset is invariant under a function, its elements may still get moved around within it.