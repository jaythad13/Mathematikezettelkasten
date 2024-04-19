---
tags:
- lin-alg
- self-study
---

### The Riesz representation theorem

One way to tell that orthogonal complements and projections are useful is that they give us a new way to prove [[Linear functionals on inner product spaces#_theorem _ Riesz representation theorem|an old theorem]].

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