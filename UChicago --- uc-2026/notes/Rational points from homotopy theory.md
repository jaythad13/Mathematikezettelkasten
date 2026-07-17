---
tags:
- tomer-schlank
- uc-2026
- alg-geo
- alg-top
---

The story of arithmetic geometry tells us that the Euclidean topology of the complex points of a scheme and the number theory of the integral points are closely related. Perhaps going from $X(\mathbb{C})$ to $X(\mathbb{Q})$ is a little too hard, but using the absolute Galois group $G_{\mathbb{Q}} = \operatorname{Gal}(\overline{\mathbb{Q}} / \mathbb{Q})$, we can understand the $\mathbb{Q}$-points. They are just the $G_{\mathbb{Q}}$-fixed points of $X(\overline{\mathbb{Q}})$. We can understand these using homotopy theory.

##### _definition:_ equivariant fundamental group

Suppose $X$ is a topological space with a continuous action of $G$.

Then the **equivariant fundamental group** with base point $x_{0}$ is $\pi(X, x_{0} \mid G)$ is the group of pairs $(g, [\alpha])$ where $g \in G$ and $[\alpha]$ is the homotopy class of a [[Algebraic topology --- concise/notes/The fundamental group#Paths and path homotopy|path]] $\alpha : [0, 1] \to X$ from $x_{0}$ to $g \cdot x_{0}$. The group multiplication is given by $(g_{1}, [\alpha_{1}]) (g_{2}, [\alpha_{2}]) = (g_{1} g_{2}, g_{1} \cdot [\alpha_{2}] [\alpha_{1}])$.

Note, $\pi_{1}(X, x_{0})$ may depend on $x_{0}$, even if $X$ is path-connected.

---

We have a map $\pi_{1}(X, x_{0} \mid G) \to G$ with kernel $\pi_{1}(X)$. It is surjective when $X$ is [[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ path-connected|path-connected]]. Then we have an exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \pi_{1}(X) \ar[r] & \pi_{1}(X \mid G) \ar[r] & G \ar[r] & 0
	\end{tikzcd}
\end{document}
```
Note, a $G$-fixed point gives a section $G \to \pi_{1}(X, x_{0} \mid G)$ up to conjugation by $\pi_{1}(X)$. 

Note that all of this is homotopy invariant in the pair of $X$ and the action $G \circlearrowright X$.

##### _proposition:_ $G$-fixed points give sections

Let $G \circlearrowright X$ be a continuous action on a path-connected topological space $X$ with base point $x_{0}$. Suppose $x \in X$ is a $G$-fixed point. Then for each path $\alpha$ from $x_{0}$ to $x$, there is a section $\sigma_{\alpha} : G \to \pi_{1}(X \mid G)$ of the canonical surjection $\varphi : \pi_{1}(X \mid G) \to G$.

###### _proof:_

Let $\alpha$ be such a path.

Consider $\sigma_{\alpha} : G \to \pi_{1}(X, x_{0} \mid G)$ by $g \mapsto (g, [g \cdot \alpha]^{-1} [\alpha])$. By definition
$$
\sigma_{\alpha}(g_{1} g_{2}) = (g_{1} g_{2}, [g_{1} g_{2} \cdot \alpha]^{-1}[\alpha]).
$$
Thus,
$$
\begin{align}
\sigma_{\alpha}(g_{1}) \sigma_{\alpha}(g_{2}) & = (g_{1}, [g_{1} \cdot \alpha]^{-1} [\alpha]) (g_{2}, [g_{2} \cdot \alpha]^{-1} [\alpha]) \\
 & = (g_{1} g_{2}, g_{1} \cdot([g_{2} \cdot \alpha]^{-1} [\alpha])[g_{1} \cdot \alpha]^{-1} [\alpha]) \\
 & = (g_{1} g_{2}, [g_{1}g_{2} \cdot \alpha]^{-1}[g_{1} \cdot \alpha] [g_{1} \cdot \alpha]^{-1} [\alpha]) \\
 & = (g_{1} g_{2}, [g_{1} g_{2} \cdot \alpha ]^{-1} [\alpha]) \\
 & = \sigma_{\alpha}(g_{1} g_{2}).
\end{align}
$$
Here, the action of $G$ commutes with taking homotopy classes of paths and with path composition because it is a continuous action.

---

Thus, we have a concrete obstruction to $G$ fixed points on a topological space. This gives us some clue of how something like Falting's theorem (that $X(\mathbb{Q})$ is finite for certain types of curves $X$) might be proved using homotopy-theoretic methods.

However, it's doesn't literally give us a way to do this. $X(\overline{\mathbb{Q}})$ is not at all $X(\mathbb{C})$ and it doesn't have a nice fundamental group to compute! This is why we use the **étale fundamental group**! It doesn't quite recover the fundamental group of $X(\mathbb{C})$ with the Euclidean topology, but it does recover its profinite completion. We won't say what this is, but we will just write $\pi_{1}^\text{ét}(X)$ for the étale fundamental group of a sufficiently nice [[Algebraic geometry --- rising-sea/notes/Schemes#_definition _ scheme, Zariski topology, isomorphism of schemes, functions|scheme]] $X$.

As a side note, Serre showed that recovering the profinite completion of $\pi_{1}(X(\mathbb{C}))$ is pretty much as good as we can do. He found a variety $X$ over a number field $\mathbb{F} / \mathbb{Q}$ with multiple embeddings $\mathbb{F} \subseteq \mathbb{C}$ such that the corresponding automorphism of $\mathbb{C}$ changes the fundamental group. That is, the two different versions of the complex topology are not homotopic.

The étale fundamental group of a (sufficiently nice) scheme $X \to \operatorname{Spec} \mathbb{Q}$ yields the following exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \pi_{1}^\mathrm{et}(X_{\overline{\mathbb{Q}}}) \ar[r] & \pi_{1}^\mathrm{et}(X) \ar[r, "\varphi"] & G_{\mathbb{Q}} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
and the same relation between $G_{\mathbb{Q}}$-fixed points of $X$ (which are exactly $X(\mathbb{Q})$) and sections of $\varphi$. In fact, this works for any field $\mathbb{F}$ and its separable closure $\mathbb{F}^\text{sep}$.

Grothendieck went further — he studied the functor
$$
X(\mathbb{F}) \to \{ \text{sections } \sigma : G_{\mathbb{F}} \to \pi_{1}^\text{ét}(X) \} / \pi_{1}^\text{et}(X_{\overline{\mathbb{F}}})\text{-conjugation}.
$$
In general, this is not a bijection (consider $\mathbb{C}$) but the Grothendieck section conjecture is that it is a bijection when $\mathbb{F}$ is a number field.

Artin–Mazur extended this $\pi_{1}^\text{ét}$ to get all étale $\pi^\text{ét}_{n}$s. These are recovered by the Morel–Voevodsky homotopy category. The informal idea is that $\mathbb{A}^1$-homotopy is equivalent to étale homotopy plus the Galois action.