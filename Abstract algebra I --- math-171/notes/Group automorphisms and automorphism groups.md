---
tags:
- alg
- cat-th
- math-171/6
- math-171/7
---

### Group automorphisms

##### _definition:_ automorphism

An group automorphism is an [[Group isomorphisms#_definition _ group isomorphism, isomorphic|isomorphism]] from a group to itself.

The set of automorphisms on a group $G$ is $\operatorname{Aut} G$.

##### _examples:_ automorphisms

1) The trivial automorphism is the identity $\operatorname{id} : g \mapsto g$.
2) The inner automorphism for some particular $g \in G$ is $\varphi_{g} : x \mapsto g x g^{-1}$.

##### _proposition:_ inner automorphisms are actually automorphisms

For some fixed $g \in G$ let $\varphi_{g} : x \mapsto g x g^{-1}$. Every element of $G$ has the form $g x g^{-1}$ for some $x \in G$.

Note that this is equivalent to surjectivity for $\varphi_{g}$, and for finite $G$, this is equivalent to $\varphi_{g}$ being an automorphism. Also note that showing that $\varphi_{g}$ is an automorphism is sufficient.

###### _proof:_

We can show $\varphi_{g}$ is a homomorphism by standard tricks.
$$
\begin{split}
\varphi_{g}(xy) & = g x y g^{-1} \\
& = g x 1 y g^{-1} \\
& = g x g^{-1} g y g^{-1} \\
& = \varphi_{g}(x) \varphi_{g}(y)
\end{split}
$$
Suppose $\varphi_{g}(x) = 1$. Then $g x g^{-1} = 1$ and multiplying by $g$ on the right and $g^{-1}$ on the left, we get $x = g^{-1} g = 1$. Thus $\ker \varphi_{g} = \{ 1 \}$.

For any $x \in G$ note that for $y = g^{-1} x g$ gives us
$$
\begin{split}
\varphi_{g}(y) & = g g^{-1} x g g^{-1} \\
& = 1 x 1 \\
& = x.
\end{split}
$$
That is, every $x \in G$ is also in $\operatorname{im} \varphi_{g}$.

Thus, we've shown that $\varphi_{g}$ is an injective, surjective homomorphism $G \to G$. That is $\varphi_{g}$ is an automorphism on $G$.

### Automorphism groups

The automorphisms on a group naturally form a group under composition. Usually when we say $\operatorname{Aut} G$ this is what we mean. 

Automorphism groups also exist for other objects.

##### _example:_ the automorphism group of a symmetric graph

What's the automorphism group of this graph?

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		1 \ar[rd, dash] & & & 2 \ar[ld, dash] \\
		& \circ \ar[r, dash] & \circ & \\
		3 \ar[ru, dash] & & & 4 \ar[lu, dash]
	\end{tikzcd}
\end{document}
```

These are all the rigid symmetries of the graph —

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		1 \ar[rd, dash] & & & 2 \ar[ld, dash] \\
		& \circ \ar[r, dash] & \circ & \\
		3 \ar[ru, dash] & & & 4 \ar[lu, dash]
	\end{tikzcd}
	\begin{tikzcd}
		2 \ar[rd, dash] & & & 1 \ar[ld, dash] \\
		& \circ \ar[r, dash] & \circ & \\
		4 \ar[ru, dash] & & & 3 \ar[lu, dash]
	\end{tikzcd}
\end{document}
```

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		3 \ar[rd, dash] & & & 4 \ar[ld, dash] \\
		& \circ \ar[r, dash] & \circ & \\
		1 \ar[ru, dash] & & & 2 \ar[lu, dash]
	\end{tikzcd}
	\begin{tikzcd}
		4 \ar[rd, dash] & & & 3 \ar[ld, dash] \\
		& \circ \ar[r, dash] & \circ & \\
		2 \ar[ru, dash] & & & 1 \ar[lu, dash]
	\end{tikzcd}
\end{document}
```

Label the four symmetries $1, a, b, c$ in $\begin{bmatrix} 1 & a \\ b & c \end{bmatrix}$.

| -   | $1$ | $a$ | $b$ | $c$ |
| --- | --- | --- | --- | --- |
| $1$ | $1$ | $a$ | $b$ | $c$ |
| $a$ | $a$ | $1$ | $c$ | $b$ |
| $b$ | $b$ | $c$ | $1$ | $a$ |
| $c$ | $c$ | $b$ | $a$ | $1$ |

Note that this is commutative and has $ab = ba = c$. This is a group of order $4$, that is not $\mathbb{Z} / 4 \mathbb{Z}$ (the cyclic group of order $4$). It is called the Klein four-group.