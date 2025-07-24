---
tags:
- ladr/5A
- ladr/5B
- lin-alg
---

Let $T$ be an operator on a vector space $V$ over $\mathbb{F}$.

Part of the reason that the theory of [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_definition _ operator|operators]] is richer than the theory of linear maps is, as we said that they form a ring (an algebra in fact). In particular, it is a result of previous

##### _proposition:_ the algebra of operators

The operators on $V$ form an algebra under (regular) addition and composition. 

This allows us the notation $T^m$ to refer to the operator obtained by composing $T$ with itself $m$ times, $T^{-m}$ for $(T^{-1})^m$ and so on. In particular, we have a notion of polynomials of an operator.

##### _definition:_ polynomials in an operator

Given a polynomial $p \in \mathbb{F}[z]$ with $p(z) = a_{0} + a_{1} z + \dots + a_{m} z^m$, the operator defined by that polynomial of $T$ is
$$
p(T) = a_{0} I + a_{1} T + \dots + a_{m} T^m.
$$

We denote the space of all polynomials in an operator $T$ (the set $\{ p(T) \mid p \in \mathbb{F}[z] \}$) by $\mathbb{F}[T]$. It is a subalgebra of $\mathcal{L}(V)$. 

Note that $\mathcal{L}(V)$ is not commutative, so we do still need to prove that $\mathbb{F}[T]$ is (for the same reasons that $\mathbb{F}[z]$ is).

Also note that despite its close relationship to $\mathbb{F}[z]$, $\mathbb{F}[T]$ is not necessarily isomorphic to $\mathbb{F}[z]$ since we could have, say $T^4 = I$ for $T$ the $\pi / 2$ [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_example _ eigenstuff is field-dependent|rotation]] on $\mathbb{R}^{2}$. We will see that for finite dimensional $V$, $\mathbb{F}[T] \cong \mathbb{F}[z] / (p)$ for some "minimal polynomial" $p$.

Understanding $\mathbb{F}[T]$ will be central to understanding the [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_definition _ eigenvalue, eigenvector|eigenstuff]] of $T$.

##### _proposition:_ $\mathbb{F}[T]$ is a quotient of $\mathbb{F}[z]$

We can express $\mathbb{F}[T]$ as a [[Abstract algebra --- math-171/notes/Ideals and quotients#_proposition, definition _ quotient rings are rings|quotient]]
$$
\mathbb{F}[T] = \mathbb{F}[z] / \mathfrak{i}
$$
for some [[Abstract algebra --- math-171/notes/Ideals and quotients#_definition _ ideal|ideal]] $\mathfrak{i} \subseteq \mathbb{F}[z]$.

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

Since $\mathbb{F}[T]$ is defined to be $\operatorname{img} \varphi$, it follows that $\mathbb{F}[T] = \mathbb{F}[z] / \ker \varphi$ and that the kernel must be an ideal from the [[Abstract algebra --- math-171/notes/Ring isomorphism theorems#_theorem _ the first isomorphism theorem|first isomorphism theorem]].

##### _corollary:_ $\mathbb{F}[T]$ is commutative

$\mathbb{F}[T]$ is a commutative algebra.

###### _proof sketch:_

... since $\mathbb{F}[z]$ is a commutative algebra.

The commutativity of $\mathbb{F}[T]$ gives us some more [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_definition _ invariant subspace|invariant subspaces]].

##### _corollary:_ the kernel and range of a polynomial of an operator are invariant

Given $p \in \mathbb{F}[z]$, its kernel $\ker p(T)$ and its image $\operatorname{img} p(T)$ are invariant under $T$.

###### _proof:_

Suppose $v \in \ker p(T)$. Then $p(T) Tv = T p(T) v = 0$ by the commutativity of $\mathbb{F}[T]$. That is, $Tv \in \ker p(T)$.

Suppose $v \in \operatorname{img} p(T)$ with $v = p(T) u$. Then $Tv = T p(T) u = p(T) (T u)$, again by commutativity. That is, $Tv \in \operatorname{img} p(T)$.

### The minimal polynomial

We remarked earlier that $\mathbb{F}[T]$ is not necessarily isomorphic to $\mathbb{F}[z]$. We will show that in fact, for $V$ finite-dimensional, $\mathbb{F}[T]$ is never isomorphic to $\mathbb{F}[z]$. In particular, there is always a non-zero polynomial that

##### _proposition:_ existence of an annihilating polynomial

Suppose $V$ is finite-dimensional. Then there is a (non-zero) monic polynomial $p \in \mathbb{F}[z]$ such that $p(T) = 0$ with $\deg p \le \dim V$.

###### _proof:_

We prove by induction on $\dim V$. If $\dim V = 0$ then it suffices to consider $p = 1$.

Now suppose that every operator on a vector space of dimension smaller than $\dim V$ has an annihilating polynomial. Consider some non-zero $u \in V$. Since the list $u, Tu, \dots, T^{\dim V} u$ has length $\dim V + 1$, it is linearly dependent. There is then a minimal $m \in \mathbb{N}$ such that $T^m u$ is a linear combination of $u, Tu, \dots, T^{m - 1} u$. In particular, we can write
$$
c_{0} u + c_{1} T u + \dots + c_{m - 1} T^{m - 1} u + T^m u = 0
$$
for some scalars $c_{0}, c_{1}, \dots, c_{m - 1} \in \mathbb{F}$ (which could be all zero if $T^m u$). In other words, there is a (non-zero) monic polynomial $q$ with coefficients $c_{0}, c_{1}, \dots, c_{m - 1}, 1$ such that $q(T) u = 0$. 

After applying $q(T)$, we're just left with its image. We only need to find a polynomial $s$ (of small enough degree) to kill its image. Then $sq(T) = 0$. Note that since $\mathbb{F}[T]$ is commutative, all $T^k u$ are in $\ker q(T)$ — 
$$
q(T) T^k u = T^k q(T) u = 0.
$$
Since $m$ is minimal, $u, Tu, \dots, T^{m - 1} u$ are linearly independent and the space of $T^k u$ has dimension at least $m$. By the [[rank-nullity theorem]], the dimension of the image is then at most $\dim V - m$.  Recall that $\operatorname{img} q(T)$ is invariant under $T$. Thus, by induction, there exists $s \in \mathbb{F}[z]$ of degree at most $\dim V - m$ with $s(T_{\mid \operatorname{img} q(T)}) = 0$. Now $sq$ has degree at most $\dim V$ and $sq(T) = 0$ since $\operatorname{img} q(T) \subseteq \ker s(T)$.


##### _definition:_ minimal polynomial

The minimal polynomial of $T$ is the unique monic polynomial $p \in \mathbb{F}[z]$ of smallest degree such that $p(T) = 0$.

##### _proposition:_ the kernel of $\mathbb{F}[z] \to \mathbb{F}[T]$ is a non-trivial principal ideal

The kernel of the homomorphism $\varphi : \mathbb{F}[z] \to \mathbb{F}[T]$ by $p \mapsto p(T)$ is $(q)$ for some non-zero polynomial $q$.

###### _proof:_

Since there exists an annihilating polynomial, the kernel of $\varphi$ is non-trivial. $\mathbb{F}[z]$ is a [[Abstract algebra --- math-171/notes/Factorisation in special rings#Euclidean domains|Euclidean domain]] with norm given by the degree of the polynomial. Since [[Abstract algebra --- math-171/notes/Factorisation in special rings#_proposition _ Euclidean domains are principal ideal domains|Euclidean domains are principal]], $\ker \varphi = (q)$ where $q$ is a non-zero element of $\ker \varphi$ of minimal degree. By multiplying by a unit in $\mathbb{F}$, this can be chosen to be monic.

##### _corollary:_ annihilating polynomials are multiples of the minimal polynomial

Let $p$ be the minimal polynomial of $T$. Then if $r \in \mathbb{F}[z]$ and $q(T) = 0$, $r = p q$ for some $q \in \mathbb{F}[z]$.

##### _example:_ the minimal polynomial of a restriction operator

If $U$ is invariant under $T$, then the minimal polynomial of $T$ is a multiple of the minimal polynomial of the restriction $T_{\mid U}$.

##### _proposition:_ eigenvalues are zeroes of the minimal polynomial

The zeroes of the minimal polynomial of $T$ are exactly the eigenvalues of $T$.

###### _proof:_

Let $p$ be the minimal polynomial of $T$.

First suppose $\lambda$ is an eigenvalue of $T$. Then there is some non-zero $v \in V$ with $Tv = \lambda v$. Further, since $T^n v = \lambda^n v$ linearity shows that $p(T) v = p(\lambda) v$. Since $p(T) = 0$ and $v \neq 0$, we must have $p(\lambda) = 0$.

Suppose $\lambda$ is a zero of $p$. Then $p(z) = (z - \lambda) q(z)$ for some $q$ of smaller degree. Write $s(z) = z - \lambda$. Since $q(T) \neq 0$ there is some $v \in V$ with $q(T) v \neq 0$ but $p(T) v = 0$, implying $s(T) v = 0$. Since $s(T) = T - \lambda I$ is non-injective, $\lambda$ is an eigenvalue of $T$.

##### _corollary:_ invertibility and the minimal polynomial

$T$ is invertible if and only if its minimal polynomial is not in $(z) \subseteq \mathbb{F}[z]$.

###### _proof sketch:_

$T$ having a minimal polynomial in $(z)$, is equivalent to $T$ having eigenvalue $0$, is equivalent to $T$ non-injective.