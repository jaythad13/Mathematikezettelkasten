---
tags:
- lin-alg
- ladr/5B
---

We can prove the existence of eigenvalues in the specific cases of odd-dimensional real vector spaces and arbitrary complex vector spaces. In effect we will prove the following existence result for invariant subspaces.

##### _theorem:_ existence of invariant subspaces

Let $V$ be a finite-dimensional vector space with a linear operator $T \in \mathcal{L}(V)$. 

If $V$ is complex and $\dim V > 1$, then $T$ has a non-trivial invariant subspace.

If $V$ is real and $\dim V > 2$, then $T$ has a non-trivial invariant subspace.

### Eigenvalues on complex vector spaces

The existence of eigenvalues of operators on vector spaces over $\mathbb{C}$ is essentially due to the algebraic completeness of $\mathbb{C}$ since it follows directly from [[Complex analysis --- math-135/notes/Cauchy integral formula#_theorem _ the fundamental theorem of algebra|the fundamental theorem of algebra]]. 

##### _theorem:_ existence of eigenvalues over $\mathbb{C}$

Every operator $T$ on a finite-dimensional complex vector space $V$ has an eigenvalue.

###### _proof:_

Let $n = \dim V$. Then choose a non-zero $v \in V$. Since $v, Tv, \dots, T^n v$ is a list of $n + 1$ vectors, it must be linearly dependent, with $a_{0}, a_{1}, \dots, a_{n} \in \mathbb{C}$ not all zero such that $a_{0} v + a_{1} Tv + \dots + a_{n} T^n v = 0$. That is, for the polynomial $p \in \mathbb{C}[z]$ given by $p(z) = a_{0} + a_{1} z + \dots + a_{n} z^n$, we have $p(T) v = 0$. In particular, $p(T)$ is not injective.

By the fundamental theorem of algebra $p$ is the product of $n$ linear polynomials $z - \lambda_{j}$. Since $\mathbb{C}[T]$ [[Linear algebra done right --- ladr/notes/Polynomials in an operator#_proposition _ $ mathbb{F}[T]$ is a quotient of $ mathbb{F}[z]$|is a homomorphic image]] of $\mathbb{C}[z]$, we get the factorisation
$$
p(T) = (T - \lambda_{1} I) \cdots (T - \lambda_{n} I).
$$
At least one of these multiplicands must be non-injective for their product to be. [[Linear algebra done right --- ladr/notes/Eigenstuff and invariant subspaces#_proposition _ equivalent conditions|Thus]], $T$ has at least one eigenvalue $\lambda_{j}$.

### Eigenvalues on real vector spaces

##### _lemma:_ operators with irreducible minimal polynomial have no eigenvectors

Suppose $T$ is an operator on a real vector space $V$. Let $b, c \in \mathbb{R}$ with $b^{2} < 4c$. Then if $T^{2} + bT + cI = 0$, $T$ has no eigenvectors.

###### _proof:_

Since $T^{2} + b T + c I = 0$, the polynomial $p$ given by $p(x) = x^{2} + b x + c$ [[Linear algebra done right --- ladr/notes/Polynomials in an operator#_corollary _ annihilating polynomials are multiples of the minimal polynomial|is a multiple of the minimal polynomial]]. Since $p$ is irreducible and monic, it must then be the minimal polynomial. [[Linear algebra done right --- ladr/notes/Polynomials in an operator#_proposition _ eigenvalues are zeroes of the minimal polynomial|Since it has no roots]], $T$ has no eigenvalues, and thus, no eigenvectors.

##### _lemma:_ irreducible quadratics have even-dimensional kernel

Suppose $T$ is an operator on a real vector space $V$. Let $b, c \in \mathbb{R}$ with $b^{2} < 4c$. Then $\dim \ker T^{2} + bT + cI$ is an even number.

###### _proof:_

Write $U = \ker T^{2} + bT + c I$ and $S = T_{\mid U} \in \mathcal{L}(U)$. Then $S^{2} + b S^{2} + c I = 0$ and we want to show that $U$ is even dimensional. Let $W \subseteq U$ be the maximal $S$-invariant subspace of even dimension. It is equivalent to show $W = U$.

Suppose by way of contradiction that $W \neq U$. We will show that $W$ cannot be maximal, a contradiction. Since $W \neq U$, there is some $v \in U \setminus W$. Consider $\operatorname{span}(v, Tv)$. Since $T(Tv) = - b Tv + c v$, it is invariant under $T$. Since $T$ has no eigenvalues, $v$ and $Tv$ are linearly independent, giving the span dimension $2$. Finally, $W \cap \operatorname{span}(v, Tv) = 0$ — $v \not\in W$ forces the intersection to be at most $1$-dimensional, and a $1$-dimensional invariant subspace of $T$ would just be the span of an eigenvector of $T$.

Thus, the sum $W + \operatorname{span}(v, Tv)$ is a direct sum $W \oplus \operatorname{span}(v, Tv)$ and has dimension $\dim W + 2$. This is a larger even-dimensional invariant subspace of $T$, and thus, a contradiction.

##### _theorem:_ existence of eigenvalues over $\mathbb{R}$

Every operator on an odd-dimensional vector space has an eigenvalue.

###### _proof:_

We've already proven the more general result about existence of eigenvalues for $V$ complex. Thus, assume $V$ real.

We prove the existence of eigenvalues by induction. By picking a basis it is clear that if $\dim V = 1$ then $T$ is multiplication by a scalar (possibly $0$), and thus, has an eigenvalue. Now assume that $\dim V \geq 3$ and all operators on vector spaces of odd-dimension less than $3$ have an eigenvalue. 

It's a consequence of the [[Complex analysis --- math-135/notes/Cauchy integral formula#_theorem _ the fundamental theorem of algebra|fundamental theorem of algebra]] and the fact that complex roots of a polynomial in $\mathbb{R}[x]$ come in conjugate pairs that $p \in \mathbb{R}[x]$, the [[Linear algebra done right --- ladr/notes/Polynomials in an operator#_definition _ minimal polynomial|minimal polynomial]] of $T$ can be factored as 
$$
p(x) = (x - \lambda_{1}) \dots (x - \lambda_{m}) (x^{2} + b_{1} x + c_{1}) \dots + (x^{2} + b_{n} x + c_{n})
$$
with $b_{j}^{2} < 4 c_{j}$ for each $j$. If there are any $(x - \lambda_{j})$ in the factorisation of $p$, $T$ has a real eigenvalue already — [[Linear algebra done right --- ladr/notes/Polynomials in an operator#_proposition _ eigenvalues are zeroes of the minimal polynomial|zeroes of the minimal polynomial are eigenvalues]]. Of course, we will prove that there always is such a $(x - \lambda_{j})$, but only indirectly.

Suppose $p(x) = q(x) (x^{2} + bx + c)$ with $b^{2} < 4c$. Then $q(T)(T^{2} + b T + c I) = 0$. This forces $q(T_{\mid \operatorname{img} T^{2} + bT + c I}) = 0$ and the minimality of $p$ forces $\operatorname{img} T^{2} + b T + cI \neq V$ so that $q(T) \neq 0$ in general. Since $\ker {T^{2} + b T + c I}$ is even-dimensional, rank-nullity gives that $\operatorname{img} T^{2} + b T + c I$ is a non-trivial odd-dimensional [[Linear algebra done right --- ladr/notes/Polynomials in an operator#_corollary _ the kernel and range of a polynomial of an operator are invariant|invariant subspace]] of $V$. On this subspace, the restriction of $T$ has an eigenvalue, and thus, $T$ has an eigenvalue.

Note that when $\dim V > 2$, even if $V$ is not odd-dimensional, the minimality of $p$ forces both $\operatorname{img} T^{2} + b T + c I$ and $\ker T^{2} + b T + c I$ to be non-trivial invariant subspaces.