---
tags:
- math-171/11
- alg
---

Suppose $\varphi : G \to H$ is a group homomorphism. What about the other way? Even if $\varphi$ is not injective or surjective, what structures can we define that, in some sense go from $H$ to $G$?

We can look at the pre-image of any set in $H$ in the standard way, but particularly, we might be interested in all of the things that map to a single element. This is what a fibre is!

### Fibres

##### _definition:_ the fibre under a homomorphism

Suppose $\varphi : G \to H$ is a homomorphism. Then for any $h \in H$, we have
$$
\varphi^\text{fib}(h) = \varphi^\text{pre}(\{ h \}).
$$

Note that then $\varphi^\text{fib}$ is then a function $H \to \mathcal{P}(G)$ (if $h \not\in \operatorname{im} \varphi$ we have $\varphi^\text{fib}(h) = \emptyset$).

An interesting question is "when is $\varphi^\text{fib}(h)$ a group?"

##### _proposition:_ only $\varphi^\text{fib}(1_{H})$ is a group

Suppose $\varphi : G \to H$ is a homomorphism. Then $\varphi^\text{fib}(h)$ is a subgroup of $G$ if and only if $h = 1_H$.

###### _proof:_

If $h = 1_{H}$ then $\varphi^\text{fib}(h)$ is just $\ker \varphi$ which we already know is a subgroup of $G$.

If $\varphi^\text{fib}(h)$ is a subgroup (let us call it $F \le G$). Then we have $1_{G} \in F$ and thus, $h = \varphi(1_{G})$ giving us $h = 1_{H}$.

Notice that the only point at which $\varphi^\text{fib}$ is non-injective as a function, is for those $b \not\in \operatorname{im} \varphi$.

### Partitioning a group

##### _proposition:_ fibres partition the domain

For a homomorphism $\varphi : G \to H$. $\varphi^\text{fib} : H \to \mathcal{P}(G)$ partitions $G$.

Note that we can explicitly calculate the fibre that corresponds to any particular representative:

##### _proposition:_ the left and right cosets of the kernel are the fibre

Suppose $\varphi : G \to H$ is a homomorphism. Then $\varphi^\text{fib}(h) = x \ker \varphi = (\ker \varphi) x$ where $\varphi(x) = h$.

This leads us to define the general notion of a coset. These give us new ways to define equivalence classes on groups. We've actually used this idea before, but never really looked at how these partition the set.

##### _definition:_ cosets

Let $A \le B$. For $b \in A$, the left coset of $A$ in $B$ represented by $b$ is
$$
bA = \{ ba | a \in A \}
$$
and the right coset of $A$ in $B$ represented by $b$ is
$$
Ab = \{ ab | a \in A \}.
$$

Note that of course, we may have $b_{1} A = b_{2} A$ even if $b_{1} \neq b_{2}$.

##### _proposition:_ the cosets of a subgroup partition the set

Let $A \le B$. The set of all left cosets $\{ bA | b \in B \}$ is a partition of $B$, and similarly, the set of all right cosets $\{ Ab | b \in B \}$ is a partition of $B$.

### Quotients

Now we can start talking about quotients! The motivating example is

##### _definition, theorem:_ the quotient group is a group

Let $\varphi : G \to H$ be a group homomorphism. Then the quotient group
$$
G / \ker \varphi = \{ \varphi^\text{fib}(h) | h \in H \}
$$
is a group with the well defined operation $(x \ker \varphi)(y \ker \varphi) = (xy) \ker \varphi$.

###### _proof:_

For this, we will denote $x \ker \varphi$ by $\overline{x}$.

We really just need to show that the operation is well defined. The rest follows from the group structure of $G$.

Suppose $\overline{x_{1}} = \overline{x_{2}}$ and $\overline{y_{1}} = \overline{y_{2}}$. Then we want to show that $\overline{x_{1}} \, \overline{y_{1}} = \overline{x_{2}} \, \overline{y_{2}}$. This is equivalent to $\overline{x_{1} y_{1}}$ and $\overline{x_{2} y_{2}}$ being the same. Since they're in the same fibre, $x_{1} x_{2}^{-1}, y_{1} y_{2}^{-1} \in \ker \varphi$. Thus,
$$
\begin{split}
 \varphi(x_{1} y_{1} (x_{2} y_{2})^{-1}) & =  & \varphi(x_{1} y_{1} y_{2} ^{-1} x_{2}^{-1}) \\
 & = \varphi(x_{1}) \varphi(y_{1} y_{2}^{-1}) \varphi(x_{2}^{-1}) \\
 & = \varphi(x_{1}) \varphi (x_{2}^{-1})  \\
 & = \varphi(x_{1} x_{2} ^{-1}) \\
 & = 1_{H}
\end{split}
$$
which gives us $\overline{x_{1} y_{1}} = \overline{x_{2} y_{2}}$ as desired.

Associativity is by
$$
\begin{split}
(\overline{x} \, \overline{y}) \, \overline{z} & = \overline{xy} \, \overline{z} \\
 & = \overline{(xy) z} \\
 & = \overline{x(yz)} \\
 & = \overline{x} \, \overline{yz} \\
 & = \overline{x} (\overline{y} \, \overline{z}).
\end{split}
$$

The identity is just $\overline{1_{G}}$ since
$$
\begin{split}
\overline{1_{G}} \overline{x} & = \overline{1_{G}x} \\
 & = \overline{x} \\
 & = \overline{x 1_{G}} \\
 & = \overline{x} \overline{1_{G}}.
\end{split}
$$

We can see that inverses exist and are given by $\overline{x}^{-1} = \overline{x ^{-1}}$ just by
$$
\begin{split}
\overline{x} \overline{x ^{-1}} & = \overline{x x ^{-1}} \\
 & = \overline{1_{G}}. 
\end{split}
$$

### The first isomorphism theorem

It turns out that, just as we wanted, this quotient group is just a copy of the image of the homomorphism. More specifically, we have

![[Abstract algebra --- math-171/notes/Group isomorphism theorems#_theorem _ the first isomorphism theorem|Group isomorphism theorems]]