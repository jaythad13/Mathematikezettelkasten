---
tags:
- vsrp-2025
- complex
- comb
- graph
---

The parafermionic observable twists the [[Holomorphicity in loop models --- vsrp-2025/notes/The connective constant of the honeycomb lattice#_definition _ the partition function|partition function]] of self-avoiding walks by winding in order to make it "holomorphic".

### Topological preliminaries

In order to define the parafermionic observable, we need to define the domain it is defined on and the winding that we twist by. The definition of a domain is easy.

##### _definition:_ (finite) domain of the honeycomb lattice, boundary

A (finite) domain of the honeycomb lattice is the intersection of a (compact) domain $\Omega \subseteq \mathbb{C}$ with $\mathbb{H} \cup \mathbb{H}'$ as well as the closure of the intersection so that each hexagon is completely included, and the mid-edges from each hexagon are included as well.

By abuse of notation, we denote the domain on the honeycomb lattice obtained from $\Omega \subseteq \mathbb{C}$ by $\Omega$ as well. We denote the set of all mid-edges in the domain by $\Omega'$.

The boundary of the honeycomb lattice domain is the set of mid-edges emanating from the complete hexagons, denoted by $\partial \Omega$.

The winding of a walk can be defined more generally for any graph embedded in $\mathbb{R}^{2}$ in the same manner as the [[Simplicial homology and random walks --- math-145/notes/Discrete winding number#_definition _ angle cocycle (of a $1$-chain)|winding number of a chain]] by considering the chain of edges in between vertices in sequence in the walk. Here, for simplicity, we define winding just for walks on the [[Holomorphicity in loop models --- vsrp-2025/notes/The connective constant of the honeycomb lattice#Walks on mid-edges|mid-edges of the honeycomb lattice]] $\mathbb{H}'$.

In contrast with topological uses of the winding number, we are interested in the residue modulo $2 \pi$ (how much of an "incomplete loop" is left over) rather than the number of times a walk winds about a particular point. Also, we are considering self-avoiding walks, so all our walks will have some non-zero residue. For that reason, we don't divide out by $2 \pi$ in our definition. Finally, we define winding of a walk from its source to any point in it, rather than the winding of the whole walk around any point not in it.

##### _definition:_ winding of a walk on $\mathbb{H}'$

For a walk $\gamma : a \to z \in \mathbb{H}'$ on the mid-edges of the honeycomb lattice, its winding from $a$ to $z$ is the total rotation in radians when $\gamma$ is traversed from $a$ to $b$
$$
W(\gamma) = \frac{\pi}{3} (\# \text{left turns} - \# \text{right turns}).
$$

Since this is the same as the topological invariant winding, and our walks will typically be self avoiding, we can deform most walks (in a simply connected domain) into a walk around part of a single hexagon, and then a straight line of no winding. This means that winding is defined by what part of the hexagon you end up on, up to an integer multiple of $2 \pi$ (which we will see we don't care about).

### Parafermionic observables

The parafermionic observable will be a function of mid-edges on a graph, but it will also depend on the domain $\Omega$, a starting mid-edge $a$, and choices of generating function variable $x$ and winding weight $\sigma$.

##### _definition:_ parafermionic observables

Given a domain $\Omega$ on the honeycomb lattice, a choice of starting mid-edge $a \in \Omega$, some positive real $x$ and a real $\sigma$, the parafermionic observable is $F : \Omega' \to \mathbb{C}$ by
$$
F(z) = \sum_{\gamma : a \to z} e^{-i \sigma W(\gamma)} x^{\ell(\gamma)}.
$$

While this parafermionic observable doesn't necessarily satisfy all the requirements to be discrete holomorphic in the conventional sense for probabilists, the [[Complex analysis --- math-135/notes/Cauchy-Goursat theorem|Cauchy-Goursat theorem]] holds — its integral around any closed contour in the domain is $0$. On taking limits of the parafermionic observable on the dilation $\delta \Omega$ as $\delta \to \Omega$, we get that if a continuous limit exists, it must have zero integral everywhere. Thus, by [[Complex analysis --- math-135/notes/Cauchy integral formula#_theorem _ Morera's theorem|Morera's theorem]], it is holomorphic. However, what we know is not strong enough to guarantee the existence of a continuous limit. In the limit we are only guaranteed to obtain a "divergence-free" complex function.

Of course to make sense of what it means for the parafermionic observable to satisfy Cauchy's theorem, we should have a notion of what an integral is.

##### _definition:_ discrete integral on the honeycomb lattice

Given a domain $\Omega \subseteq \mathbb{C}$ and a simple closed curve $\Gamma \subseteq \Omega$ (a walk $v_{0} \dots v_{n}$ with degree $2$ everywhere) on the dual triangular lattice $\mathbb{T}$ to the honeycomb lattice, the integral of a function on mid-edges, say $f : \mathbb{H}' \to \mathbb{C}$, over $\Gamma$ is
$$
\int_{\Gamma} f(z) \, dz = \sum_{i = 0}^n (v_{i + 1} - v_{i}) f(z) 
$$
where $z$ is the  mid edge of $v_{i} v_{i + 1} \in \Gamma$. Note of course that the mid-edges of edges in the dual lattice are just mid-edges of corresponding edges in the original lattice.

##### _theorem:_ Goursat's theorem for parafermionic observables

Given a choice of domain $\Omega$ on $\mathbb{H}$ and starting vertex $a \in \Omega$ for each basic triangle $\Delta$ on the dual lattice of $\Omega$ (with faces contained in $\Omega$),
$$
\int_{\Delta} F(z) \, dz =  0.
$$
for $x = x_{c} = 1 / \sqrt{ 2 + \sqrt{ 2 } }$ and $\sigma = 5 / 8$, and any choice

###### _proof:_

What we need to show is exactly that for each $v \in \Omega$ and $p, q, r$ the three mid-edges surrounding it (counterclockwise),
$$
 F(p) + \tau F(q) + \tau F(r) = 0.
$$
where $\tau = e^{2 \pi i / 3}$. This is because the edges of $\Delta$ in $\mathbb{T}$ are all $\tau$ rotations of each other. We have $(v_{3} - v_{2}) = \tau (v_{2} - v_{1})$ and $(v_{1} - v_{3}) = \tau^{2} (v_{2} - v_{1})$ for $\Delta = v_{1} v_{2} v_{3}$ counterclockwise. Since $(v_{2} - v_{1})$ and $(p - v)$ are non-zero,
$$
\int_{\Delta} F(z) \, dz = 0 \iff F(p) + \tau F(q) + \tau^{2} F(r) = 0.
$$

Now, we write the expression as a sum over the contribution of paths ending at one of $p, q, r$ —
$$
F(p) + \tau F(q) + \tau F(r)= \sum_{\gamma : a \to \{ p, q, r \}, \gamma \subseteq \Omega} c(\gamma)
$$
where
$$
c(\gamma) = \tau^j e^{-i \sigma W({\gamma})} x^{\ell(\gamma)}
$$
with $j = 0$ for $\gamma$ ending at $p$, and so on. We will group $\gamma$ with other paths so that their contributions cancel. 

Suppose without loss of generality that $\gamma$ visits $p$ first. If $\gamma$ visits both $q$ and $r$ (in that order), then we can decompose $\gamma$ into a path $\gamma_{\mid a, p}$ from $a$ to $p$, the path from $p$ to $q$ visiting just $v$, and a path $\gamma_{\mid q, r}$ from $q$ to $r$. That is,
$$
\gamma = \gamma_{\mid a, p} \cdot v_{\mid p, q} \cdot \gamma_{\mid q, r}.
$$
Consider also the alternate choice to visit $v$, go to $r$ instead and then run $\gamma_{\mid q, r}$ in reverse instead. We write this path
$$
\gamma' = \gamma_{\mid a, p} \cdot v_{\mid p, r} \cdot \gamma_{\mid q, r}^{-1}.
$$
Since it is reversed, $\gamma_{\mid q, r} ^{-1}$ starts at $r$ rather than $q$. For ease of notation we write $\gamma = \gamma_{\mid a, p} \cdot \alpha$ and $\gamma' = \gamma_{\mid a, p} \cdot \alpha'$. We claim that the contributions of these paths cancel — that $c(\gamma) + c(\gamma') = 0$. This (and similar consideration of paths that visit $q$ or $r$ first) takes care of the contributions of paths that visit all of the mid-edges $p, q, r$.

The other case is if $\gamma$ visits at most two of the mid-edges. If it visits only two of them, they must be visited in succession since the only vertex $\gamma$ can visit after the first mid-edge (still, without loss of generality, $p$) is $v$, and the only unvisited mid-edges on edges of $v$ are $q$ and $r$. $\gamma$ only visits $p$. For $\gamma$ to only visit $p$ out of $p, q, r$, it must stop at $p$. Thus, the other two paths that we can group $\gamma$ with are obviously the one-vertex extensions to $q$ and $r$
$$
\gamma_{q} = \gamma \cdot v_{\mid p, q} \quad \text{and} \quad \gamma_{r} = \gamma \cdot v_{\mid p, r}.
$$
We claim that the sum of the contributions of these paths vanish too — that $c(\gamma) + c(\gamma_{q}) + c(\gamma_{r}) = 0$. This (and similar consideration of paths that visit $q$ or $r$ first) takes care of all paths that visit at most $2$ of the mid-edges $p, q, r$. Since 

We will see that in order to get these expressions to cancel with arbitrary $x, \sigma$ we have to choose $x = x_{c}$ and $\sigma = 5 / 8$. First, we show that $c(\gamma) + c(\gamma') = 0$. This will force $\sigma = 5 / 8$. 

Notice that $\ell(\gamma) = \ell(\gamma')$. Thus, the power of $x$ part of their contributions is the same. Their windings only differ in the last part after $\gamma_{\mid a, p}$. As reasoned previously, this can be determined by the endpoints of $\alpha$ up to an integer multiple of $2 \pi$ (and, in this case, even over $\mathbb{R}$ itself). Specifically, $W(\alpha) = - 4 \pi / 3 + m 2 \pi$ and $W({\alpha ^{-1}}) = 4 \pi / 3 + m 2 \pi$ ($\alpha$ is reduced to the path around a small hexagon going clockwise from $p$ to $r$ to $q$). Thus,
$$
\begin{align}
c(\gamma) + c(\gamma') & = \tau e^{-i \sigma W(\gamma)} x^{\ell(\gamma)} + \tau^2 e^{-i \sigma W({\gamma'})} x^{\ell(\gamma')} \\
 & = e^{- i \sigma W(\gamma_{\mid a, p})} x^{\ell(\gamma)} (\tau e^{-i \sigma W(\alpha)} + \tau^{2} e^{-i \sigma W(\alpha ^{-1})}) \\
 & = e^{- i \sigma W(\gamma_{\mid a, p})} x^{\ell(\gamma)} (\tau e^{-i \sigma W(\alpha)} + \overline{\tau e^{-i \sigma W(\alpha)}} ) \\
 & = e^{- \sigma W(\gamma_{\mid a, p})} x^{\ell(\gamma)} (e^{i 2 \pi / 3 + i \sigma 4 \pi / 3} + \overline{e^{i 2 \pi / 3 + i \sigma 4 \pi / 3}}).
\end{align}
$$
For this contribution to be zero, we need to obtain a complex number that is the additive inverse of its conjugate — it must be $\pm i$. This forces $\sigma = 5 / 8$ so that $2 / 3 + \sigma 4 / 3 = 3 / 2$.

Now we show that to get $c(\gamma) + c(\gamma_{q}) + c(\gamma_{r}) = 0$ will force $x = x_{c} = 1 / 2 \cos (\pi / 8)$ (given $\sigma = 5 / 8$). Notice that $\gamma_{q}$ and $\gamma_{r}$ have length $\ell(\gamma_{p}) + 1$. We also have that their windings differ from $W(\gamma_{p})$ by $- \pi / 3$ and $+ \pi / 3$ respectively. Thus,
$$
\begin{align}
c(\gamma_{p}) + c(\gamma_{q}) + c(\gamma_{r}) & = e^{- i \sigma W(\gamma_{p})} x^{\ell(\gamma_{p})} + \tau e^{-i \sigma W(\gamma_{q})} x^{\ell(\gamma_{q})} + \tau^{2} e^{-i \sigma W(\gamma_{r})} x^{\ell(\gamma_{r})} \\
 & = e^{- i \sigma W(\gamma_{p})} x^{\ell(\gamma_{p})} (1 + \tau e^{-i \sigma \pi / 3} x + \overline{\tau e^{-i \sigma \pi / 3}} x) \\
 & = e^{-i \sigma W(\gamma_{p})} x^{\ell(\gamma_{p})} (1 + x (e^{i 7 \pi / 8} + e^{- i 7 \pi / 8})).
\end{align}
$$
The only value of $x$ that makes the expression in the parentheses on the right $0$ is $x = -1 /  2 \cos(7 \pi / 8) = 1 / 2 \cos(\pi / 8)$.


##### _corollary:_ Cauchy's theorem for parafermionic observables

For any simply connected domain $\Omega \subseteq \mathbb{C}$, the integral of the parafermionic observable around a closed self-avoiding walk is $0$.