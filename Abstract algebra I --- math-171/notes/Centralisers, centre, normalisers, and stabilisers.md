---
tags:
- alg
- math-171
lecture:
- math-171-8
- math-171-9
---

Recall [[Group automorphisms and automorphism groups#_proposition _ inner automorphisms are actually automorphisms|inner automorphisms]]. Note that if $G$ is [[Motivating groups#_definition _ abelian group, commutative group|abelian]], then each inner automorphism is just the identity on $G$. The idea here is that group actions tell us something about a group, especially when it acts on itself. What if we look into non-abelian $G$ and its subgroups where inner automorphisms defined by elements are just identity?

### Studying $G$ acting on $G$

We want to look at how $G$ acts on itself. What is invariant? What is unchanged?

##### _definition:_ centraliser, $C_{G}(A)$

The centraliser of a set $A \subset G$ in $G$ is $C_{G}(A)$, set of all elements of $G$ that commute with every element in $A$. 

Note that this is equivalent to all elements such that there induced inner automorphism fixes all $a \in A$.

##### _definition:_ centre, $C_{G}$

The centre of a group $G$ is $C_{G}$, the centraliser of $G$ in $G$.

##### _definition:_ normaliser, $N_{G}(A)$

The normaliser of $A$ in $G$ is $N_{G}(A)$ is the set of all elements of $G$ that give $gag^{-1} \in A$ for all $a \in A$. 

That is, all $g \in G$ such that $A$ is invariant under the induced inner automorphism

##### _proposition:_ the hierarchy of centralisers, centres, normalisers

We have the chain of containment $C_{G} \subset C_{G}(A) \subset N_{G}(A)$ for any $A \subset G$. We also have $C_{G} \le C_{G}(A) \le N_{G}(A)$.

###### _proof:_ %% finish later %%

Note that $N_{G}(A)$ is nonempty since it contains $1_{G}$. Suppose $x, y \in N_{G}(A)$. Then we have
$$
\begin{split}
(xy) A (xy)^{-1} & = x y A y^{-1} x^{-1} \\
& = xAx^{-1} \\
& = A.
\end{split}
$$
Also, we have $x A x^{-1} = A$ which on multiplying on the right by $x$ and on the left by $x^{-1}$ gives us $x^{-1} A x = A$.

Again, $C_{G}(A)$ is nonempty since it contains $1_{G}$. Suppose $x, y \in C_{G}(A)$.

##### _example:_ things on $S_{3}$

For $G = S_{3}$ and $A$ is the set of all transpositions, we have $C_{G}(A) = C_{G} = \{ 1_{G} \}$ and $N_{G}(A) = G$.

##### _example:_ abelian groups

For any abelian group we have $C_{G} = C_{G}(A) = N_{G}(A)$ for all $A \subset G$

### $G$ acting on $A$

We can generalise these ideas to a group acting on any set. Stabilisers sort of correspond to centralisers and kernels to the centre, but only sort of for both.

##### _definition:_ stabiliser

For $G$ acting on $A$, stabiliser of $a \in A$ is $\operatorname{stab}_{G}(a)$, the set of all $g \in G$ such that $g \cdot a = a$.

###### _proof:_

See [[Homework 7.pdf#page=1|Homework 7]].

##### _definition:_ kernel

For $G$ acting on $A$, the stabiliser of $a \in A$ is $\ker_{G}(A)$, the set of all $g \in G$ such that $g \cdot a = a$ for all $a \in A$.

###### _proof:_

Again, see [[Homework 7.pdf#page=1|Homework 7]].

##### _example:_ going back to groups acting on themselves

Let $N_{G}(A)$ act on $A \subset G$ by conjugation — $g \cdot a = g a g^{-1}$. What is the kernel? 

It's just the centraliser of $A$ under $G$ (recall that $C_{G}(A) \subset N_{G}(A)$).