---
tags:
- a-lie/6
- lie
- alg
- diff-geo
---

Weights are where you first see that Lie algebras have more structure than rings. They generalise the notion of an eigenvalue. Typically an eigenvalue is an eigenvalue of a one dimensional subspace of the linear maps on a space. Now we want to consider larger subspaces on which the eigenvalues vary linearly.

The weight space is corresponds to the notion of an eigenspace.

##### _definition, proposition:_ weight space

Let $H \subset L \subset \mathfrak{gl}(V)$ be a [[Lie algebras --- a-lie/notes/Subalgebras, ideals, and quotients#_definition _ Lie subalgebra|subalgebra]] of the Lie algebra $L$, and let $\lambda$ be a functional in $H^\vee$. Then
$$
V_{\lambda} = \{ v \in V \mid h(v) = \lambda(h) v \text{ for all } h \in H \}.
$$
$V_{\lambda}$ is a subspace of $V$. 

###### _proof:_

Suppose $v, w \in V_{\lambda}$  and $\alpha, \beta \in F$ (where $V$ is over $F$). Then we can compute $h(\alpha v + \beta w)$ for each $h \in H$ —
$$
\begin{align}
h(\alpha v + \beta w) & = \alpha h(v) + \beta h(w) \\
 & = \alpha \lambda(h)v + \beta \lambda(h) w \\
 & = \lambda(h)(\alpha v + \beta w).
\end{align}
$$
Thus, $av + \beta w \in V_{\lambda}$.

##### _definition:_ weight

For a subalgebra $H \subset L \subset \mathfrak{gl}(V)$ we say $\lambda \in H^{\vee}$ is a weight if $V_{\lambda}$ is not the zero subspace.

##### _example:_ the top left entry of upper-triangular matrices

All upper triangular matrices (say over $\mathbb{F}^3$) have eigenvector $e_{1} = (1, 0, 0)$ with eigenvalue equal to the top left entry of the matrices. We know that [[Lie algebras --- a-lie/notes/Subalgebras, ideals, and quotients#_examples _ Lie subalgebras of $ mathfrak{gl}_{n}(F)$|they form a subalgebra]] $\mathfrak{b}_{3}(\mathbb{F}) \subset \mathfrak{gl}_{3}(\mathbb{F})$, and the map $\lambda$ that sends a matrix to its top left entry is a functional (in fact it is the dual functional to the basis vector $E_{1, 1}$). Thus $\lambda$ is a weight for $\mathfrak{b}_{3}(\mathbb{F})$ with $V_{\lambda} = \operatorname{span} e_{1}$.

### The invariance lemma

The invariance lemma is an important result for using weights to understand Lie algebras.

##### the invariance _lemma_

Suppose $L \subset \mathfrak{gl}(V)$ is a Lie algebra, with $V$ finite dimensional and over a field $\mathbb{F}$ of characteristic $0$, $I \subset L$ is an ideal, and $\lambda \in I^\vee$ is a weight. Then $V_{\lambda}$ is an $L$-invariant subspace. That is, $L v \in V_{\lambda}$ for each $v \in V_{\lambda}$.

###### _proof:_

To show that $V_{\lambda}$ is $L$-invariant we will show that $h(x (v)) = \lambda(h) x(v)$ so $x(v)$ must be part of the weight space. Choose arbitrary $h \in I$, $x \in L$, and $v \in V_{\lambda}$. Then we can use the commutator to switch $x$ and $h$ around and get
$$
\begin{align}
h(x(v)) & = (hx)(v) \\
 & = (xh + [h, x])v \\
 & = x(h(v)) + x([h, x](v)) \\
 & = \lambda(h) x(v) + \lambda([h, x])(v)).
\end{align}
$$
If we can show that $\lambda([h, x]) = 0$, we will have the desired result.

Consider the maximal linearly independent list $\mathcal{B} = v, x(v), \dots, x^n(v)$ and let $W_{n}$ be its span. That is, $\mathcal{B}$ is a basis of $W_{n}$. $W_{n}$ is $x$-invariant by construction. We claim that $W_{n}$ is $I$-invariant and every $y \in I$ has an upper-triangular matrix with respect to $\mathcal{B}$, with all eigenvalues $\lambda(y)$. We can prove this by showing that each $W_{k} = \operatorname{span} (v, x(v), \dots, x^k(v))$ is $I$-invariant by [[Superdiscrete --- math-55A/notes/Induction and recurrence|induction]], in a manner similar to the proof that [[Upper-triangular matrices|every complex operator has an upper-triangular matrix]].

Now consider $\lambda([h, x])$. Since $h \in I$, $[h, x]$ is also in the ideal, and must have an upper-triangular matrix with respect to $\mathcal{B}$. Since the trace of a commutator vanishes, $\operatorname{tr} [h,x] = 0$ but by the upper-triangular form of the matrix, we have $\operatorname{tr} [h, x] = \lambda([h, x]) (n + 1)$. Thus, $\lambda([h, x]) = 0$.


