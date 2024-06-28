---
tags:
- ladr/6C
- lin-alg
- self-study
---

### The Riesz representation theorem

One way to tell that orthogonal complements and projections are useful is that they give us a new way to prove [[Linear algebra done right --- ladr/notes/The Riesz representation theorem#_theorem _ Riesz representation theorem|an old theorem]].

##### _theorem:_ Riesz representation theorem

Suppose $V$ is finite-dimensional. For each $v \in V$, define $\varphi_{v} \in V^\vee$ by
$$
\varphi_{v}(u) = \left< u, v \right>
$$
for all $u \in U$. Then the function by $v \mapsto \varphi_{v}$ is a bijection.

Note that the function is a linear map if $V$ is over $\mathbb{R}$ but not if $V$ is over $\mathbb{C}$.

###### _proof:_

First we will show that $v \mapsto \varphi_{v}$ is injective. Suppose $\varphi_{v} = \varphi_{w}$ for some $v, w \in V$. Then, for all $u \in V$, we must have $\varphi_{v}(u) - \varphi_{w}(u) = 0$. But
$$
\begin{split}
\varphi_{v}(u) - \varphi_{w}(u) & = \left< u, v \right> - \left< u, w \right> \\
 & = \left< u, v - w \right>.
\end{split}
$$
Since this gives us $\left< u, v - w \right> = 0$ for all $u \in V$, we must have that $v - w = 0$, and thus, $v = w$.

Now we will show that $v \mapsto \varphi_{v}$ is surjective. Suppose we have some $\varphi \in V^\vee$. If $\varphi = 0$, we obviously have $\varphi = \varphi_{0}$. If $\varphi \neq 0$, then $\dim \operatorname{null} \varphi = \dim V - 1$, and thus, $\dim (\operatorname{null} \varphi)^\perp = 1$.

Thus, we can choose some nonzero $w \in (\operatorname{null} \varphi)^\perp$. Consider
$$
v = \frac{\overline{\varphi(w)}}{\lVert w \rVert ^2}w.
$$
Note that $v \in (\operatorname{null} \varphi)^\perp$ and is nonzero since $\varphi(w) \neq 0$.

Note that
$$
\lVert v \rVert = \frac{\lvert \varphi(w) \rvert }{\lVert w \rVert }
$$
and thus,
$$
\begin{split}
\varphi(v) & = \frac{\overline{\varphi(w)} \varphi(w)}{\lVert w \rVert ^2} \\
 & = \frac{\lvert \varphi(w) \rvert ^2}{\lVert w \rVert ^2} \\
 & = \lVert v \rVert ^2.
\end{split}
$$

Thus, for any $u \in V$ we can write
$$
u = \left( u - \frac{\varphi(u)}{\varphi(v)} v \right) + \frac{\varphi(u)}{\lVert v \rVert ^2} v
$$
where we note that
$$
\begin{split}
\varphi\left( u - \frac{\varphi(u)}{\varphi(v)} v \right)  & = \varphi(u) - \frac{\varphi(u)}{\varphi(v)} \varphi(v) \\
 & = \varphi(u) - \varphi(u) \\
 & = 0.
\end{split}
$$

Thus the vector in parenthesis is in $\operatorname{null} \varphi$ and is orthogonal to $v$. Thus
$$
\begin{split}
\left< u, v \right> & = \left< u - \frac{\varphi(u)}{\varphi(v)} v, v \right> + \left< \frac{\varphi(u)}{\lVert v \rVert ^2} v, v \right> \\
 & = 0 + \frac{\lVert v \rVert^2 }{\lVert v \rVert ^2} \varphi(u) \\
 & = \varphi(u)
\end{split}
$$
as desired.

### Optimisation

Sometimes we want to approximate a certain vector by a vector that's nicer in some way — in particular, it's a member of a nice subspace of the whole vector space. It turns out that the closest vector in a subspace $U \subset V$ to $v \in V$ is just the orthogonal projection of $v$ onto $U$.

##### _proposition:_ the best subspace approximation

Suppose $U$ is a finite dimensional subspace of $V$. Let $v \in V$. Then, for any $u \in U$,
$$
\lVert v - P_{U}v \rVert \le \lVert v - u \rVert 
$$
with equality if and only if $u = P_{U}v$.

###### _proof:_

We know that $v - P_{U}v \in U^\perp$. Thus, $\left< v - P_{U}v, P_{U}v - u \right> = 0$. Then, by [[Orthogonality|Pythagoras' theorem]], we have
$$
\begin{split}
\lVert v - u \rVert^2 & = \lVert (v - P_{U}v) + (P_{U}v - u) \rVert^2 \\
 & = \lVert v - P_{U}v \rVert^2 + \lVert P_{U}v - u \rVert^2 \\
 & \ge \lVert v - P_{U}v \rVert^2
\end{split} 
$$
with equality if and only if $\lVert P_{U}v - u \rVert^2 = 0$.

Thus, we have
$$
\lVert v - P_{U}v \rVert \le \lVert v - u \rVert 
$$
with equality if and only if $u = P_{U}v$ as desired.

##### _example:_ approximating the sine function

An obviously important question in calculus is how best to approximate transcendental functions with easier to deal with polynomials. With inner product
$$
\left< f, g \right> = \int_{-\pi}^\pi f(x) g(x) \, dx 
$$
on $\mathcal{C}([-\pi, \pi])$ we can find the degree $n$ polynomial $p$ that minimises
$$
\lVert f - p \rVert^2 =  \int_{- \pi}^\pi \lvert f(x) - p(x) \rvert^2 \, dx
$$
and thus approximates $f$ really well.

In particular, replacing coefficients with a good decimal approximation, we get that
$$
p(x) = 0.987862 x - 0.155271 x^3 + 0.00564312 x^5
$$
is the best degree $5$ polynomial approximation of $\sin(x)$. Note that this is really close to the Taylor series expansion about the origin, but is not it (even with the real constants). In fact, this approximation is way better, particularly at $x$ values further from the origin.

### Pseudoinverse

The pseudoinverse applies this idea of the nearest approximation in a certain subspace to the the range of a linear map. For an injective linear map $T$ even if there doesn't exist $v \in V$ such that $w = Tv$, we can always map back to $v$ such that $\lVert Tv - w \rVert$ is minimised. In addition, we can always "ignore" the null space of the map to get an injective map. Note that we need finite-dimensionality for all of this to work.

##### _proposition:_ ignoring the null space of the map

Suppose $V$ is finite dimensional and $T \in \mathcal{L}(V, W)$. Then the restriction $T_{|(\operatorname{null} T)^\perp}$ is an isomorphism $(\operatorname{null} T)^\perp \to \operatorname{range} T$.

###### _proof:_

Suppose $T_{|(\operatorname{null} T)^\perp} u = 0$ for some $u \in (\operatorname{null} T)^\perp$. Then, $Tu = 0$ and thus $u \in \operatorname{null} T \cap (\operatorname{null} T)^\perp$ and thus, $u = 0$. Thus, $T$ is injective.

Suppose $w \in \operatorname{range} T$. Then we have $Tv = w$ for some $v \in V$. We know that we can write $v = u + u'$ with $u \in \operatorname{null} T$ and $u' \in (\operatorname{null} T)^\perp$. Thus,
$$
\begin{split}
Tu' & = Tv - Tu \\
 & = w - 0 \\
 & = w.
\end{split}
$$
The first equality holds by linearity and the second holds because $u \in \operatorname{null} T$. 

This gives us $\operatorname{range} T \subset \operatorname{range} T_{|(\operatorname{null} T)^\perp}$. Since the inclusion in the other direction is obviously true, we have $\operatorname{range} T = \operatorname{range} T_{|(\operatorname{null} T)^\perp}$, making $T_{|(\operatorname{null} T)^\perp}$ the desired isomorphism.

Note that this means that $T_{|(\operatorname{null} T)^\perp}^{-1}$ exists, allowing us to define the pseudoinverse.

##### _definition:_ pseudoinverse, $T^\dagger$

Suppose $V$ is finite dimensional and $T \in \mathcal{L}(V, W)$. The pseudoinverse of $T$ is the linear map $T^\dagger \in \mathcal{L}(W, V)$ defined by
$$
T^\dagger = T_{|(\operatorname{null} T)^\perp}^{-1} \circ P_{\operatorname{range} T}.
$$

The pseudoinverse is as nice as we could reasonably want. It acts like an inverse, except it only knows of vectors in $(\operatorname{null} T)^\perp \subset V$ and $\operatorname{range} T \subset W$. Specifically, we have the following result.

##### _proposition:_ $T^\dagger$ is as nice as can be

Suppose $V$ is finite dimensional and $T \in \mathcal{L}(V, W)$.
1) If $T$ is invertible, $T^\dagger = T^{-1}$.
2) $TT^\dagger = P_{\operatorname{range} T}$.
3) $T^\dagger T = P_{(\operatorname{null T})^\perp}$.

###### _proof:_

1) If $T$ is invertible $\operatorname{null} T = 0$ and thus, $(\operatorname{null} T)^\perp = V$. Also, $\operatorname{range T} = W$. Thus, $T_{|(\operatorname{null} T)^\perp} = T$ and $P_{\operatorname{range} T} = I_{W}$. Thus,
$$
\begin{split}
T^\dagger & = T^{-1} \circ I \\
 & = T^{-1}.
\end{split}
$$
2) We can just push through
$$
\begin{split}
T T^\dagger & = T T_{|(\operatorname{null} T)^\perp}^{-1} P_{\operatorname{range T}} \\
 & = T_{|(\operatorname{null} T)^\perp} T_{|(\operatorname{null} T)^\perp}^{-1} P_{\operatorname{range} T} \\
 & = P_{\operatorname{range} T}.
\end{split}
$$
   We can replace $T$ with $T_{|(\operatorname{null} T)^\perp}$ since $T_{|(\operatorname{null} T)^\perp} ^{-1}$ only spits out vectors in $(\operatorname{null} T)^\perp$.
3) Note that if $v \in \operatorname{null} T$, then $T^\dagger T v = 0$ and thus, $T^\dagger T v = P_{\operatorname{range} T} v$. If $v \in (\operatorname{null} T)^\perp$, then
$$
\begin{split}
T^\dagger T v & = T_{|(\operatorname{null} T)^\perp}^{-1} P_{\operatorname{range T}} T_{|(\operatorname{null} T)^\perp} v \\
 & = T_{|(\operatorname{null} T)^\perp}^{-1} T_{|(\operatorname{null} T)^\perp} v \\
 & = v \\
 & = P_{(\operatorname{null} T)^\perp} v.
\end{split}
$$
   Since $T^\dagger T = P_{(\operatorname{null} T)^\perp}$ on both $\operatorname{null} T$ and its orthogonal complement, the equality must hold on all of $V$.

And of course, it's a simple application of the definition to prove that the pseudoinverse has the property we really wanted — that it gives the closest thing to an inverse.

##### _proposition:_ the pseudoinverse gives the best approximate solution

Suppose $V$ is finite-dimensional. Let $T \in \mathcal{L}(V, W)$ and $w \in W$. Then
1) For any $v \in V$,
$$
\lVert TT^\dagger w - w \rVert \le \lVert Tv - w \rVert 
$$
   with equality if and only if $v \in T^\dagger w + \operatorname{null} T$.
2) If $v \in T^\dagger w + \operatorname{null} T$, then   
$$
\lVert T^\dagger w \rVert \le \lVert v \rVert 
$$
   with equality if and only if $v = T^\dagger w$.

###### _proof:_

1) This is just saying that $\lVert P_{\operatorname{range} T} w - w \rVert \le \lVert Tv - w \rVert$ with equality if and only if $Tv = P_{\operatorname{range} T} w$.
2) Write $v = T^\dagger w + u$ for $u \in \operatorname{null} T$. Then we have an orthogonal decomposition of $v$ since $T^\dagger w \in (\operatorname{null} T)^\perp$. Then, again by [[Orthogonality|Pythagoras' theorem]],
$$
\lVert v \rVert^2 = \lVert T^\dagger w \rVert^2 + \lVert u \rVert^2
$$
   giving us the desired inequality $\lVert T^\dagger w \rVert \le \lVert v \rVert$.