---
tags:
- math-189AA/16
- math-189AA/17
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

##### _proposition:_ $\operatorname{Ext}$ of injectives

For $E$ [[Commutative algebra --- math-189AA/notes/Injective modules#_definition _ injective modules|injective]], then $\operatorname{Ext}_{A}^i(M, E) = 0$ for all $i > 0$.

---

##### _proposition:_ $\operatorname{Ext}$ of projectives

If $\operatorname{proj dim} M \leq n$, then $\operatorname{Ext}_{A}^i(M, N) = 0$ for all $i > n$.

For $P$ [[Commutative algebra --- math-189AA/notes/Projective modules#_definition _ projective module|projective]], then $\operatorname{Ext}_{A}^i(P, N) = 0$ for all $i > 0$.

---