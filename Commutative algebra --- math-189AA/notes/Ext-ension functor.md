---
tags:
- math-189AA/16
- math-189AA/17
- math-189AA/18
- hom-alg
- comm-alg
---

Let $A$ be a ring.

The Ext-ension functor $\operatorname{Ext}$ is the second $A$-module invariant we have after [[Commutative algebra --- math-189AA/notes/Projective resolutions#Projective dimension|projective dimension]].

##### _definition:_ Ext-ension functor, $\operatorname{Ext}$

Let $M, N$ be $A$-modules. Let $P_{\bullet}$ be a projective resolution of $M$. Then $\operatorname{Ext}_{A}^i(M, N)$ is the $i$th cohomology of the complex $\operatorname{Hom}_{A}(P_{\bullet}, N)$ given by $\operatorname{Hom}(P_{i}, N) \to \operatorname{Hom}(P_{i + 1}, N)$.

That is, $\operatorname{Ext}^i_{A}(M, N) = H^i(\operatorname{Hom}_{A}(P_{\bullet}, N))$.

---

Note that the definition depends on a choice of projective resolution, but we claim this is an $A$-module invariant, and thus, should not depend on that choice.

##### _example:_ $\operatorname{Ext}$ of a familiar example

Consider $A = \mathbb{F}[x, y] / (xy)$ and $M = A / (x)$. Consider the projective resolution $P_{\bullet}$ of $M$ by
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & A \ar[r, "\times y"] & A \ar[r, "\times x"] & A \ar[r] & 0.
	\end{tikzcd}
\end{document}
```
This gives $\operatorname{Hom}(P_{\bullet}, M)$ going the other direction with
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathrm{Hom}_{A}(A, M) \ar[r] \ar[d, equal] & \mathrm{Hom}_{A}(A, M) \ar[r] \ar[d, equal] & \mathrm{Hom}_{A}(A, M) \ar[d, equal] \ar[r] & \cdots \\
		0 \ar[r] & M \ar[r, "\times x"] & M \ar[r, "\times y"] & M \ar[r, "\times x"] & \cdots
	\end{tikzcd}
\end{document}
```

Multiplying by $x$ in $M = A / (x)$ sends everything to zero. Since all the $x$ in $M$ are already killed, multiplying by $y$ has kernel $(\overline{x}) = 0$. Of course, it has image $(y) \subseteq M$. Thus, we have $\operatorname{Ext}^0_{A}(M, M) = M$, $\operatorname{Ext}_{A}^1(M, M) = 0$ and $\operatorname{Ext}_{A}^i(M, M)$

---

##### _example:_ $\operatorname{Ext}$ with an injective module

Consider $A = \mathbb{Z}$, $M = \mathbb{Z} / (3)$ and $N = \mathbb{Q}$. What are the $\operatorname{Ext}^i_{\mathbb{Z}}(\mathbb{Z} / (3), \mathbb{Q})$?

Consider the projective resolution
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathbb{Z} \ar[r, "\times 3"] & \mathbb{Z} \ar[r] & 0.
	\end{tikzcd}
\end{document}
```
This is actually minimal since $\mathbb{Z} / (3)$ is not $\mathbb{Z}$-projective.

This gives rise to the complex
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathrm{Hom}_{\mathbb{Z}}(\mathbb{Z}, \mathbb{Q}) \ar[r, "\times 3"] & \mathrm{Hom}_{\mathbb{Z}}(\mathbb{Z}, \mathbb{Q}) \ar[r] & 0
	\end{tikzcd}
\end{document}
```
The homology in the first spot is $\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}, \mathbb{Q}) / \operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}, \mathbb{Q}) = 0$ since any map $\varphi : \mathbb{Z} \to \mathbb{Q}$ is mapped to by $\varphi / 3$. The homology in the second spot is $0$ since the "$\times 3$" map is injective. Thus, $\operatorname{Ext}_{\mathbb{Z}}^i(\mathbb{Z} / (3), \mathbb{Q})$ is always $0$.

Notice that $\mathbb{Q}$ is an injective $\mathbb{Z}$-module and the $\operatorname{Ext}$s all vanish. This is because we can equivalently define $\operatorname{Ext}_{A}^i(M, N)$ as the cohomology of the homset complex of an injective resolution of $M$.

---

### Properties of $\operatorname{Ext}$

##### _proposition:_ the zeroth $\operatorname{Ext}$

$\operatorname{Ext}^0_{A}(M, N) = \operatorname{Hom}(M, N)$.

###### _proof:_

Choose a projective resolution and apply $M \mapsto \operatorname{Hom}(M, N)$ recalling that this is left-exact. We get the following complex where the diagonals are exact (notice that the last map is not surjective since $\operatorname{Hom}$ is only left-exact)
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& & 0 \ar[rd] \\
		& & & \mathrm{Hom}(\Omega M, N) \ar[rd] \\
		0 \ar[rr, "f_{0}"] \ar[rd] & & \mathrm{Hom}(P_{0}, N) \ar[rr, "f_{1}"] \ar[ru] & & \mathrm{Hom}(P_{1}, N) \ar[rr] & & \mathrm{Hom}(P_{2}, N) \\
		& \mathrm{Hom}(M, N) \ar[ru] \\
		0 \ar[ru]
	\end{tikzcd}
\end{document}
```
$\operatorname{Ext}^0_{A}(M, N) = H^1(\operatorname{Hom}(P_{\bullet}, N)) = \ker f_{1} / \operatorname{img} f_{0}$. $\operatorname{img} f_{0} = 0$ so we don't have to worry about it. Since $f_{1}$ factors as $\operatorname{Hom}(P_{0}, N) \to \operatorname{Hom}(\Omega M, N) \to \operatorname{Hom}(P_{1}, N)$ and the latter map is an injection, we have that $\ker f_{1}$ is just the kernel of the map $\operatorname{Hom}(P_{0}, N) \to \operatorname{Hom}(\Omega M, N)$. This is just $\operatorname{Hom}(M, N)$ (by the exactness of the first diagonal).

---

##### _proposition:_ $\operatorname{Ext}$ of injectives

For $E$ [[Commutative algebra --- math-189AA/notes/Injective modules#_definition _ injective modules|injective]], then $\operatorname{Ext}_{A}^i(M, E) = 0$ for all $i > 0$.

---

##### _proposition:_ $\operatorname{Ext}$ of projectives

If $\operatorname{proj dim} M \leq n$, then $\operatorname{Ext}_{A}^i(M, N) = 0$ for all $i > n$.

For $P$ [[Commutative algebra --- math-189AA/notes/Projective modules#_definition _ projective module|projective]], then $\operatorname{Ext}_{A}^i(P, N) = 0$ for all $i > 0$.

---

##### _corollary:_ $\operatorname{Ext}^{\operatorname{proj} \dim M}(M, N)$ is right exact

###### _proof:_

Apply the long-exact sequence in cohomology to get.

---