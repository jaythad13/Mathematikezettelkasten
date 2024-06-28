---
tags:
- ladr/6B
- self-study
- lin-alg
---

While we've seen some useful [[Orthonormal bases|properties of orthonormal bases]], they're only really useful if we have them. The Gram-Schmidt procedure uses the intuition of [[Orthogonal complements and projections|orthogonal projections]] from $\bb{R}^n$ to generate an orthonormal basis from any basis of a vector space. 

For any $v \in \bb{R}^n$, and any list of $n - 1$ (non-zero) orthogonal vectors in $\bb{R}^n$, the span of which doesn't contain $v$, we can can think of projecting $v$ onto the (hyper)plane formed by the orthogonal vectors. The difference between the orthogonal projection and $v$ is then just some vector normal to (hyper)plane, say $n$. Thus, by adding $n$ to our list, we can expand the span of our list to include $v$, while still keeping all of the vectors in our list orthogonal to each other.

##### _theorem:_ Gram-Schmidt procedure

Suppose $v_1, \ldots, v_m$ is a linearly independent list of vectors in $V$. Let $e_1 = \frac{v_1}{\norm{v_1}}$. For $j \in \set{2, \ldots, m}$, define $e_j$ recursively by
$$
u_j = v_j - (\langle v_j, e_1 \rangle  e_1 + \cdots + \langle v_j, e_{j - 1} \rangle e_{j - 1})
$$
and
$$
e_j = \frac{u_j}{\norm{u_j}}.
$$
Then $e_1, \ldots, e_m$ is an orthonormal list of vectors in $V$ such that
$$
\DeclareMathOperator{\span}{span}
\span{(v_1, \ldots, v_j)} = \span{(e_1, \ldots, e_j)}
$$
for all $j \in \bb{N}_m$.

###### _proof:_

We can show by induction on $j$ that this holds.

Note that for $j = 1$, $e_1$ is an orthonormal list with the same span as $v_1$ trivially - $e_1$ is just a non-zero scaled version of $v_1$ with $\norm{e_1} = 1$.

For any $j$ with $1 < j < m$, suppose we have
$$
\vspan{(v_1, \ldots, v_{j - 1})} = \span{(e_1, \ldots, e_{j - 1})}.
$$
Note that then $v_j \notin \span{(e_1, \ldots, e_j)}$ giving us non-zero $u_j$ and well-defined $e_j$. Also, obviously $\span{(v_1, \ldots, v_{j - 1})} = \span{(u_1, \ldots, u_{j - 1})}$ since each $u_k$ is just a scaled $e_k$. 

First we will show that $e_1, \ldots, e_j$ is orthonormal.

Since $e_j = \frac{u_j}{\norm{u_j}}$ where $u_j \neq 0$, we obviously have
$$
\langle e_j, e_j \rangle = \norm{e_j}^2 = \norm{\frac{u_j}{\norm{u_j}}}^2 = \frac{\norm{u_j}^2}{\norm{u_j}^2} = 1.
$$
For $k \neq j$, we have
$$
\langle e_j, e_k \rangle = c \langle u_j, u_k \rangle = \langle v_j, e_k \rangle - (\langle v_j, e_1 \rangle \langle e_1, e_k \rangle + \cdots + \langle v_j, e_k \rangle \langle e_{j - 1}, e_k \rangle) = \langle v_j, e_k \rangle - \langle v_j, e_k \rangle + 0 = 0.
$$
Thus, $e_1, \ldots, e_m$ is orthonormal.

Now we show that $e_1, \ldots, e_j$ has the same span as $v_1, \ldots, v_j$.

Since $\vspan{(v_1, \ldots, v_{j - 1}) = \vspan{(e_1, \ldots, e_{j - 1})}}$ and from the expression for $e_j$, $v_j \in \span{(e_1, \ldots, e_j)}$, we can have $\span{(v_1, \ldots, v_j)}$ as a subspace of $\span{(e_1, \ldots, e_j)}$. But since they both are $j$-dimensional, we must in fact have $\vspan{(v_1, \ldots, v_j)} = \vspan{(e_1, \ldots, e_j)}$, as desired.

##### _example:_ an orthonormal basis of $\mathcal{P}_2(\bb{R})$

We can compute an orthonormal basis of $\mathcal{P}_2(\bb{R})$ with respect to the inner product given by 
$$
\langle p, q \rangle = \int_{-1}^1 p(x) q(x) \, dx.
$$

We know that $1, x, x^2$ is a basis of $\mathcal{P}_2(\bb{R})$, and thus, we can use this to produce an orthonormal basis $e_0, e_1, e_2$. To start
$$
\norm{1}^2 = \int_{-1}^1 1^2 \, dx = 2
$$
and thus $\norm{1} = \sqrt{2}.$ This gives us
$$
e_0 = \frac{1}{\sqrt{2}}. 
$$

Then we have an expression for $e_1$ as well.
$$
u_1 = x - \frac{1}{\sqrt{2}} \int_{-1}^{1} x \frac{1}{\sqrt{2}} \, dx = x - 0 = x
$$
Since
$$
\norm{u_1}^2 = \int_{-1}^{1} x^2 \, dx = \frac{2}{3}
$$
we get 
$$
e_1 = \frac{u_1}{\norm{u_1}} = \sqrt{\frac{3}{2}} x.
$$

Finally, we get $e_2$.
$$
u_2 = x^2 - \sqrt{\frac{1}{2}}\int_{-1}^1 x^2 \frac{1}{\sqrt{2}} \, dx - \sqrt{\frac{3}{2}}x \int_{-1}^{1} x^2 \sqrt{\frac{3}{2}} x \, dx = x^2 - \frac{\sqrt{2}}{3\sqrt{2}} - 0 = x^2 - \frac{1}{3}.
$$
Since
$$
\norm{u_2}^2 = \int_{-1}^1 x^4 - \frac{2}{3}x^2 + \frac{1}{9} \, dx = \frac{8}{45}
$$
we have
$$
e_2 = \frac{u_2}{\norm{u_2}} = \sqrt{\frac{45}{8}} ( x^2 - \frac{1}{3}).
$$

Thus,
$$
\frac{1}{\sqrt{2}}, \sqrt{\frac{3}{2}}x, \sqrt{\frac{45}{8}}(x^2 - \frac{1}{3})
$$
is an orthonormal list of length $3$ in $\mathcal{P}_2(\bb{R})$, that is, a basis of $\mathcal{P}_2(\bb{R})$. 

##### _theorem:_ orthonormal bases always exist

Every finite-dimensional inner product space has an orthonormal basis.

###### _proof:_

Suppose $V$ is finite-dimensional with a basis $v_1, \ldots, v_m$. For $e_1, \ldots, e_m$, given by applying the Gram-Schmidt procedure to the basis, $e_1, \ldots, e_m$ is an orthonormal list of length $m = \dim V$. Since it is an [[Orthonormal bases#_proposition _ an orthonormal list of the right length is an orthonormal basis|orthonormal list of the right length]], it is an orthonormal basis.

##### _corollary:_ orthonormal lists extend to orthonormal bases

Suppose $V$ is finite-dimensional. Then every orthonormal list of vectors in $V$ can be extended to an orthonormal basis of $V$.

###### _proof:_

Suppose $e_1, \ldots, e_m$ is an orthonormal list in $V$. Then, as a linearly independent list, it can be extended to a basis of $V$, $e_1, \ldots, e_m, v_1, \ldots, v_n$. We can apply the Gram-Schmidt procedure to obtain an orthonormal basis from this basis. Notably, by the nature of the process, the first $m$ vectors are unchanged (subtracting inner products of the form $\langle e_j, e_k \rangle$ where $j \neq k$ is akin to doing nothing). Thus, we obtain an orthonormal basis $e_1, \ldots, e_m, f_1, \ldots, f_n$.

##### _theorem:_ upper-triangular matrices with respect to an orthonormal basis

Suppose $T \in \mathcal{L}(V)$. If $T$ has an upper-triangular matrix with respect to some basis of $V$, then $T$ has an upper-triangular matrix with respect to some orthonormal basis of $V$.

###### _proof:_

Suppose $T$ has an upper-triangular matrix with respect to some basis $v_1, \ldots, v_m$ which under the Gram-Schmidt procedure gives the orthonormal basis $e_1, \ldots, e_m$. Then, for each $j$, $\vspan{(v_1, \ldots, v_j)}$ [[Upper-triangular matrices|is invariant]] under $T$. But since $\vspan{(e_1, \ldots, e_j)}$ is the same subspace for each $j \in \bb{N}_m$, it too is invariant under $T$. Thus, $\mathcal{M}(T, (e_1, \ldots, e_m))$ must be upper-triangular.