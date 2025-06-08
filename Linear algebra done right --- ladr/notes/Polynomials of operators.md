---
tags:
- ladr/5A
- lin-alg
---

Let $T$ be an operator on a vector space $V$ over $\mathbb{F}$.

Part of the reason that the theory of [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_definition _ operator|operators]] is richer than the theory of linear maps is, as we said that they form a ring (an algebra in fact). In particular, it is a result of previous

##### _proposition:_ the algebra of operators

The operators on $V$ form an algebra under (regular) addition and composition. 

This allows us the notation $T^m$ to refer to the operator obtained by composing $T$ with itself $m$ times, $T^{-m}$ for $(T^{-1})^m$ and so on. In particular, we have a notion of polynomials of an operator.

##### _definition:_ polynomials of an operator

Given a polynomial $p \in \mathbb{F}[z]$ with $p(z) = a_{0} + a_{1} z + \dots + a_{m} z^m$, the operator defined by that polynomial of $T$ is
$$
p(T) = a_{0} I + a_{1} T + \dots + a_{m} T^m.
$$

We denote the space of all polynomials of an operator (the set $\{ p(T) \mid p \in \mathbb{F}[z] \}$) in $T$ by $\mathbb{F}[T]$. It is subalgebra of $\mathcal{L}(V)$. 

Note that $\mathcal{L}(V)$ is not commutative, so we do still need to prove that $\mathbb{F}[T]$ is (for the same reasons that $\mathbb{F}[z]$ is).

Also note that despite its close relationship to $\mathbb{F}[z]$, $\mathbb{F}[T]$ is not necessarily isomorphic to $\mathbb{F}[z]$ since we could have, say $T^4 = I$ for $T$ the $\pi / 2$ [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_example _ eigenstuff is field-dependent|rotation]] on $\mathbb{R}^{2}$. We will see that for finite dimensional $V$, $\mathbb{F}[T] \cong \mathbb{F}[z] / (p)$ for some "minimal polynomial" $p$.

Understanding $\mathbb{F}[T]$ will be central to understanding the [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_definition _ eigenvalue, eigenvector|eigenstuff]] of $T$.

##### _proposition:_ $\mathbb{F}[T]$ is a quotient of $\mathbb{F}[z]$

We can express $\mathbb{F}[T]$ as a [[Abstract Algebra I --- math-171/notes/Ideals and quotients#_proposition, definition _ quotient rings are rings|quotient]]
$$
\mathbb{F}[T] = \mathbb{F}[z] / \mathfrak{i}
$$
for some [[Abstract Algebra I --- math-171/notes/Ideals and quotients#_definition _ ideal|ideal]] $\mathfrak{i} \subseteq \mathbb{F}[z]$.

###### _proof sketch:_

We show that the map $\varphi : \mathbb{F}[z] \to \mathcal{L}(V)$ by $p \mapsto p(T)$ is a homomorphism. This amounts to showing that for  $p, q \in \mathbb{F}[z]$ we have $(pq)(T) = p(T) q(T)$. 

We previously showed that $\mathcal{L}(V)$ and thus $\mathbb{F}[T]$, is an (associative) algebra under addition and composition with additive identity $0$ and multiplicative identity $I$. Thus we can do all the same algebraic steps to show
$$
\begin{align}
p(T) q(T)  & = \left( \sum_{j = 0}^m a_{j} T^j \right) \left( \sum_{k = 0}^n b_{k} T^k \right) \\
 & = \sum_{j = 0}^m \sum_{k = 0}^n a_{j} b_{k} T^{j + k}  \\
 & = (pq)(T)
\end{align}
$$
for $p$ with coefficients $a_{j}$ and $q$ with coefficients $b_{k}$.

Since $\mathbb{F}[T]$ is defined to be $\operatorname{img} \varphi$, it follows that $\mathbb{F}[T] = \mathbb{F}[z] / \ker \varphi$ and that the kernel must be an ideal from the [[Abstract Algebra I --- math-171/notes/Ring isomorphism theorems#_theorem _ the first isomorphism theorem|first isomorphism theorem]].

##### _corollary:_ $\mathbb{F}[T]$ is commutative

$\mathbb{F}[T]$ is a commutative algebra.

###### _proof sketch:_

... since $\mathbb{F}[z]$ is a commutative algebra.

The commutativity of $\mathbb{F}[T]$ gives us some more [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_definition _ invariant subspace|invariant subspaces]].

##### _corollary:_ the kernel and range of a polynomial of an operator are invariant

Given $p \in \mathbb{F}[z]$, its kernel $\ker p(T)$ and its image $\operatorname{img} p(T)$ are invariant under $T$.

###### _proof:_

Suppose $v \in \ker p(T)$. Then $p(T) Tv = T p(T) v = 0$ by the commutativity of $\mathbb{F}[T]$. That is, $Tv \in \ker p(T)$.

Suppose $v \in \operatorname{img} p(T)$ with $v = p(T) u$. Then $Tv = T p(T) u = p(T) (T u)$, again by commutativity. That is, $Tv \in \operatorname{img} p(T)$