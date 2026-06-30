---
tags:
- alg-geo
- uc-2026/de-rham/4
- uc-2026/de-rham/5
- michael-barz
---

### Derivations

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
 & = \beta_{2}(a_{1}) \beta_{2}(a_{2}) - \beta_{1}(a_{1}) \beta_{1}(a_{2}) + 0 \\
 & = \beta_{2}(a_{1}) \beta_{2}(a_{2}) - \beta_{1}(a_{1}) \beta_{1}(a_{2}) + \beta_{2}(a_{1}) \beta_{1}(a_{2}) - \beta_{2}(a_{1}) \beta_{1}(a_{2}) \\
 & = \beta_{2}(a_{1})(\beta_{2}(a_{2}) - \beta_{1}(a_{2})) + \beta_{1}(a_{2})(\beta_{2}(a_{1}) - \beta_{1}(a_{1})) \\
 & = \beta_{2}(a_{1}) \, da_{2} + \beta_{1}(a_{2}) \, da_{1} \\
 & = \beta_{2}(a_{1}) \, da_{2} + (\beta_{2}(a_{2}) - da_{2}) \, da_{1} \\
 & = \beta_{2}(a_{1}) \, da_{2} + \beta_{2}(a_{2}) \, da_{1}
\end{align}
$$
Note that $d a_{2} \, da_{1} \in \mathfrak{i}^{2}$ and therefore, is $0$. Also note that we could see that the last line is the same as $\beta_{1}(a_{1}) da_{1} + \beta_{1}(a_{2}) \, da_{1}$ since their difference lies in $A$.

Viewing $\mathfrak{i}$ as an $A$-module through the structure map $\beta_{2} : A \to B$ (or equivalently, $\beta_{1} : A \to B$) we have
$$
d(a_{1} a_{2}) = a_{1} \, da_{2} - a_{2} \, d a_{1}
$$
That is, $d$ satisfies the Leibniz rule!

This will motivate the definition of a derivation. We will see that not only do derivations control the non-empty fibres of $X(B) \to X(B / \mathfrak{i})$, but also they control the surjectivity of the map, by cohomology and a connection to smoothness.

##### _definition:_ derivations

Let $M$ be an $A$-module. An **$M$-valued derivation** is a morphism of abelian groups
 $d : a \to M$ such that $d(a_{1} a_{2}) = a_{1} \, d a_{2} + a_{2} \, d a_{1}$.

We write $\operatorname{Der}(A, M)$ for the set of all derivations $A \to M$.

---

Our discussion above really proves half of the following proposition.

##### _proposition:_ lifts of square-zero extensions are controlled by derivations

Let $X = \operatorname{Spec} A$, $\varphi : B \to B / \mathfrak{i}$ a square-zero extension, and let $\gamma \in X(B / \mathfrak{i})$. Then either the set of lifts $\beta \in X(B / \mathfrak{i})$ such that $X\varphi(\beta) = \gamma$ is empty, or it contains some $\beta$ giving a bijection with $\operatorname{Der}(A, \mathfrak{i})$ by $\beta' \mapsto \beta - \beta'$ (or in the other direction, $d \mapsto \beta + d$).

---

Note, that in some sense, this tells us that the set of lifts of a square zero extension is a **torsor** — once we choose a single lift, we get all lifts as the abelian group of derivations.

### Kähler differentials

While derivations are useful, we don't actually need to study this weird new algebraic structure derivations themselves. Or at least, there is an [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_example _ initial and final objects in specific categories|initial]] derivation, and we only really need to understand that one.

##### _proposition, definition:_ Kähler differentials

Suppose $A$ is a ring. There is an $A$-module $\Omega_{A}^1$ the **Kähler differentials** of $A$, with a derivation $d_{\Omega^1} : A \to \Omega^1_{A}$ such that each derivation $d_{M} : A \to M$ factors through a unique module homomorphism $\varphi : \Omega^1_{A} \to M$ as follows.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		A \ar[r, "\Omega^1"] \ar[rr, "d_{M}"', bend right] & \Omega^1_{A} \ar[r, "\varphi"] & M
	\end{tikzcd}
\end{document}
```

---

##### _example:_ some Kähler differentials

If $A = \mathbb{Z}[x]$, then $\Omega^1_{A} = \mathbb{Z}[x] \, dx$ — the free $\mathbb{Z}[x]$ module generated by $dx$. The universal derivation $d : \mathbb{Z}[x] \to \Omega^1_{A}$ is given by $f(x) \mapsto f'(x) \, dx$.

---