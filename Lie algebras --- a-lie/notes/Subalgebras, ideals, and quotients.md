---
tags:
- a-lie/2
- alg
- diff-geo
- self-study
---

Just like [[Abstract Algebra I --- math-171/notes/Rings#Substructures of rings|rings]] and [[Linear algebra done right --- ladr/notes/Vector spaces|vector spaces]] have substructures, so do Lie algebras.

### Subalgebras

The simplest substructure of a Lie algebra is a Lie subalgebra — it's just a smaller Lie algebra inside it.

##### _definition:_ Lie subalgebra

A Lie subalgebra $K$ of a Lie algebra $L$ is a vector subspace $K \subseteq L$ where $K$ is closed under the [[Lie algebras --- a-lie/notes/Lie algebras#_definition _ Lie algebra|Lie bracket]] — $[x, y] \in K$ for all $x, y \in K$.

##### _examples:_ Lie subalgebras of $\mathfrak{gl}_{n}(F)$

1) $\mathfrak{sl}_{n}(F)$ is the subalgebra of all traceless matrices in $\mathfrak{gl}_{n}(F)$ [[Lie algebras --- a-lie/notes/Lie algebras|as we've seen already]] in the case $n = 2$, $F = \mathbb{C}$.
2) $\mathfrak{b}_{n}(F)$ is the subalgebra of all [[Upper-triangular matrices|upper-triangular matrices]] in $\mathfrak{gl}_{n}(F)$.
3) $\mathfrak{n}_{n}(F)$ is the subalgebra of all strictly upper-triangular matrices in $\mathfrak{gl}_{n}(F)$.

### Ideals

Just as for [[Abstract Algebra I --- math-171/notes/Ideals and quotients|rings]], there is a sensible notion of an ideal of a Lie algebra.

##### _definition:_ (Lie) ideal 

A (Lie) ideal $I$ of a Lie algebra $L$ is a vector subspace $I \subseteq L$ that has the absorption property $[i, x] \in I$ for all $i \in I$ and $x \in L$.

##### _example:_ $\mathfrak{sl}_{n}(F)$ is an ideal

Since the trace is linear and satisfies $\operatorname{tr}(AB) = \operatorname{tr}(BA)$, for $A \in \mathfrak{sl}_{n}(F)$ and any $B \in \mathfrak{gl}_{n}(F)$, we have
$$
\begin{align}
\operatorname{tr} [A, B] & = \operatorname{tr}(AB) - \operatorname{tr}(BA) \\
 & = 0.
\end{align}
$$

While every ideal is a subalgebra, not every subalgebra is an ideal —

##### _example:_ $\mathfrak{b}_{n}(F)$ is not an ideal

Just notice that
$$
\begin{pmatrix}
1 & 0 \\
0 & 0
\end{pmatrix} \begin{pmatrix}
0 & 0 \\
1 & 1
\end{pmatrix} - \begin{pmatrix}
0 & 0 \\
1 & 1
\end{pmatrix} \begin{pmatrix}
1 & 0 \\
0 & 0
\end{pmatrix} = \begin{pmatrix}
0 & 0 \\
0 & 0
\end{pmatrix} - \begin{pmatrix}
0 & 0 \\
1 & 0
\end{pmatrix} = \begin{pmatrix}
0 & 0 \\
-1 & 0
\end{pmatrix}
$$
is not upper triangular. In general
$$
\left [ \begin{pmatrix}
1 & 0 &  \dotsm \\
0 & 0 & \\
\vdots & &  \ddots
\end{pmatrix}, \begin{pmatrix}
0 & \cdots & 0 \\
\vdots &  & \vdots \\
1 & \dotsm 1
\end{pmatrix} \right ]
$$
is not upper triangular.

One really important ideal of every Lie algebra is the centre. Again in analogy with [[Abstract Algebra I --- math-171/notes/Centralisers, centre, and normalisers#_definition _ centre, $Z(G)$|groups and rings]], the centre commutes with everything in the algebra. However, because Lie algebras are anti-commutative, we just require the bracket to vanish on the centre —

##### _definition:_ centre

The centre of a Lie algebra $L$ is
$$
Z(L) = \{ z \in L \mid [z, x] = 0 \text{ for all } x \in L \}.
$$

###### _proof:_

First we show that $Z(L)$ is a vector subspace of $L$. For $z_{1}, z_{2} \in Z(L)$ and $\alpha, \beta \in F$, we have
$$
\begin{align}
[\alpha z_{1} + \beta z_{2}, x] & = \alpha [z_{1}, x] + \beta [z_{2}, x]  \\
 & = 0.
\end{align}
$$
That is, $Z(L)$ is indeed a vector subspace.

Now we show that $[z, x] \in Z(L)$ for all $z \in Z(L)$ and $x \in L$. We just compute
$$
\begin{align}
[[z, x], y] & = [0, x] \\
 & = 0.
\end{align}
$$

### Quotient Lie algebras

Of course, the reason we care about ideals of Lie algebras is that, [[Abstract Algebra I --- math-171/notes/Ideals and quotients#_proposition, definition _ quotient rings are rings|just like with rings]], the corresponding quotients are Lie algebras if and only if the subalgebra we quotient by is an ideal.

##### _definition:_ quotient algebra

Given a Lie algebra $L$ and a subalgebra $I \subseteq L$, the quotient algebra is the [[Quotient spaces|quotient vector space]] $L / I$ with the bracket $[x + I, y + I] = [x, y] + I$.

##### _theorem:_ quotient Lie algebras are quotients by ideals

Suppose $L$ is a Lie algebra with subalgebra $I \subseteq L$. Then $L / I$ is a Lie algebra if and only if $I$ is an ideal.

###### _proof:_

First suppose $I$ is an ideal. Note that we have bilinearity by the fact that $L / I$ is a vector subspace. We also get antisymmetry and the Jacobi identity for free since $[x + I, y + I] = [x, y] + I$. Thus, we just need to show that the bracket is well defined.

For any $x + i_{1}$ and $y + i_{2}$, where $i_{1}, i_{2} \in I$,
$$
\begin{align}
[x + i_{1}, y + i_{2}] & = [x, y] + [x, i_{2}] + [y, i_{1}] + [i_{1}, i_{2}] \in [x, y] + I
\end{align}
$$
so the Lie bracket of different representatives $x + i_{1}, y + i_{2}$ differs from the Lie bracket of $x, y$ by an element of $I$.

Now suppose $L / I$ is a Lie algebra. Thus, the Lie bracket is well defined with
$$
[x + i_{1}, x] = i \in I
$$
so
$$
[x, x] + [i_{1}, x] = i \in I
$$
which by antisymmetry means
$$
[i_{1}, x] = i \in I
$$
for all $x \in L$. That is, $I$ is an ideal.