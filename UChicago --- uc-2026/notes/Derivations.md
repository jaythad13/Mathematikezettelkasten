---
tags:
- alg-geo
- uc-2026/de-rham/4
- michael-barz
---

Let $X = \operatorname{Spec} \mathbb{Z}[x_{1}, \dots, x_{d}] / (f_{1}, \dots, f_{r}) = \operatorname{Spec} A$. We want to understand the [[p-adic numbers --- math-177/notes/Hensel's lemma#_lemma _ multivariable Hensel's lemma|multivariable Hensel's lemma]] count of $p^{d - r}$ lifts $X(\mathbb{Z} / p) \to X(\mathbb{Z} / p^{2})$ as indicative of the dimension of the tangent space of $X$. 

More generally, given a square zero extension $\varphi : B \to B / \mathfrak{i}$, we want to understand the lifts $X(B / \mathfrak{i}) \to X(B)$. Is this injective? Is this surjective? If it is both, we can say $X$ is [[UChicago --- uc-2026/notes/Algebraic prespaces#_definition _ formally étale|formally étale]]. (Since there is a morphism $B \to B / \mathfrak{i}$, every point $X(B)$ gives another point $X(B / \mathfrak{i})$, so the other direction is not interesting).

It's hard to determine lifts straight away, but we can understand how they must behave when we have them. Suppose $\gamma \in X(B / \mathfrak{i})$ has a lift to some $\beta \in X(B)$. That is, $X\varphi(\gamma) = \beta$, and so $\varphi \circ \beta = \gamma$. This is exactly equivalent to the following diagrams commuting.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
	    \mathrm{Spec} \, B \ar[dr, dashed] \\
	    \mathrm{Spec} \, B / \mathfrak{i} \ar[r] \ar[u] & \mathrm{Spec} \, A
	\end{tikzcd}
\begin{tikzcd}
& B \ar[d, "\varphi"] \\
A \ar[ru, dashed, "\beta"] \ar[r, "\gamma"] & B/\mathfrak{i}
\end{tikzcd}
\end{document}
```
Thus, any two lifts $\beta_{1}, \beta_{2} \in X(B)$ of $\gamma \in X(B / \mathfrak{i})$ must satisfy $\varphi(\beta_{2} - \beta_{1}) = 0$ and thus, $\operatorname{img}(\beta_{2} - \beta_{1}) \in \mathfrak{i}$.

Let $d : A \to \mathfrak{i}$ be the abelian group homomorphism $\beta_{2} - \beta_{1}$. Not only is it additive, but also it satisfies
$$
\begin{align}
d(a_{1} a_{2}) & = \beta_{2}(a_{1} a_{2}) - \beta_{1}(a_{1} a_{2}) \\
 & = \beta_{2}(a_{1}) \beta_{2}(a_{2}) - \beta_{1}(a_{1}) \beta_{1}(a_{2}) \\
 & = \beta_{2}(a_{1}) \beta_{2}(a_{2}) - \beta_{1}(a_{1}) \beta_{1}(a_{2}) + \beta_{2}(a_{1}) \beta_{1}(a_{2}) - \beta_{2}(a_{1}) \beta_{1}(a_{2}) \\
 & = \beta_{2}(a_{1})(\beta_{2}(a_{2}) - \beta_{1}(a_{2})) + \beta_{1}(a_{2})(\beta_{2}(a_{1}) - \beta_{1}(a_{1})) \\
 & = \beta_{2}(a_{1}) d(a_{2}) + \beta_{1}(a_{2}) d(a_{1}) \\
 & = \beta_{2}(a_{1}) d(a_{2}) + (\beta_{2}(a_{2}) - d(a_{2})) d(a_{1}) \\
 & = \beta_{2}(a_{1}) d(a_{2}) + \beta_{2}(a_{2}) d(a_{1})
\end{align}
$$
Note that $d(a_{2}) d(a_{1}) \in \mathfrak{i}^{2}$ and therefore, is $0$. 

Viewing $\mathfrak{i}$ as an $A$-module through the structure map $\beta_{2} : A \to B$, we have
$$
d(a_{1} a_{2}) = a_{1} \cdot d(a_{2}) - a_{2} \cdot d(a_{1})
$$
That is, $d$ satisfies the Leibniz rule!

This will motivate the definition of a derivation. We will see that not only do derivations control the non-empty fibres of $X(B) \to X(B / \mathfrak{i})$, but also they control the surjectivity of the map, by cohomology!