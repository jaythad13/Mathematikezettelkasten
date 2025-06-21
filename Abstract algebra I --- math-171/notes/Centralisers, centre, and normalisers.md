---
tags:
- alg
- math-171/8
- math-171/9
---

Recall [[Group automorphisms and automorphism groups#_proposition _ inner automorphisms are actually automorphisms|inner automorphisms]]. Note that if $G$ is [[Abstract Algebra I --- math-171/notes/Groups, and why you should care#_definition _ abelian group, commutative group|abelian]], then each inner automorphism is just the identity on $G$. The idea here is that group actions tell us something about a group, especially when it acts on itself. What if we look into non-abelian $G$ and its subgroups where inner automorphisms defined by elements are just identity?

### Studying $G$ acting on $G$

We want to look at how $G$ acts on itself. What is invariant? What is unchanged?

##### _definition:_ centraliser, $C_{G}(A)$

The centraliser of a set $A \subset G$ in $G$ is $C_{G}(A)$, set of all elements of $G$ that commute with every element in $A$. 

Note that this is equivalent to all elements such that there induced inner automorphism fixes all $a \in A$.

##### _definition:_ centre, $Z(G)$

The centre of a group $G$ is $Z(G)$, the centraliser of $G$ in $G$.

##### _definition:_ normaliser, $N_{G}(A)$

The normaliser of $A$ in $G$ is $N_{G}(A)$ is the set of all elements of $G$ that give $gag^{-1} \in A$ for all $a \in A$. 

That is, all $g \in G$ such that $A$ is invariant under the induced inner automorphism

##### _proposition:_ the hierarchy of centralisers, centres, normalisers

We have the chain of containment $Z(G)\subset Z_{G}(A) \subset N_{G}(A)$ for any $A \subset G$. We also have $Z(G) \le Z_{G}(A) \le N_{G}(A)$.

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

For any abelian group we have $Z(G) = Z_{G}(A) = N_{G}(A)$ for all $A \subset G$

##### _example:_ the kernel of conjugation

Let $N_{G}(A)$ act on $A \subset G$ by conjugation — $g \cdot a = g a g^{-1}$. What is the [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ kernel, effective action|kernel]]? 

It's just the centraliser of $A$ under $G$ (recall that $Z_{G}(A) \subset N_{G}(A)$).