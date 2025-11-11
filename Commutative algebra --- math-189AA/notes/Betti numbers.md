---
tags:
- math-189AA/21
- math-189AA/22
- comm-alg
- hom-alg
---

Let $A$ be a ring.

The Betti numbers of a module describe the number of generators required at each point down the line.

##### _definition:_ Betti numbers

Let $M$ be a finitely generated module over a local ring $A, \mathfrak{m}$. Then if $P_{\bullet}$ is a minimal free resolution of $M$, we define the **Betti numbers** $\beta_{i}(M)$ of $M$ to be the dimensions of the free modules $P_{i}$. 

That is, if
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & A^{\oplus \beta_{2}(M)} \ar[r] & A^{\oplus \beta_{1}(M)} \ar[r] & A^{\oplus \beta_{0}(M)} \ar[r] & M
	\end{tikzcd}
\end{document}
```
is a minimal free resolution, then the $\beta_{i}(M)$ are the Betti numbers.

---

##### _example:_ Betti numbers tell you about projective dimension

If $\beta_{i}(M) = 0$ for all $i > N$, then $\operatorname{proj} \dim M \leq N$ — a free resolution is certainly a projective resolution, so the minimal projective resolution also has length at most $N$.

---

We can also give an alternate definition using properties of tensoring and a small lemma.

##### _lemma:_ minimal surjections contain no units

Suppose $A$ is a Noetherian local ring and $M$ is a finitely generated module over it. If $\varepsilon : A^{\oplus n} \to M$ is a minimal surjection onto $M$ and $A^{\oplus m} \to \ker \varepsilon \to A^{\oplus n}$ is also minimal. Then the matrix representing $A^{\oplus m} \to A^{\oplus n}$ does not contain any units.

###### _proof sketch:_

Suppose $(a_{1}, \dots, a_{n - 1}, u) + \ker \varepsilon$ (with $u \in A$ a unit) is in the image of $\varepsilon$. Then show that we must have 
$$
(b_{1}, \dots, b_{n - 1}, b_{n}) + \ker \varepsilon = (b_{1} - u^{-1} a_{1} b_{n}, \dots, b_{n} - u^{-1} u b_{n}) + \ker \varepsilon = (b_{1}, \dots, b_{n - 1}, 0) + \ker \varepsilon.
$$
But then $A^{\oplus n - 1}$ surjects onto $M$, contradicting the minimality of $A^{\oplus n}$.

---

##### _proposition:_ computing Betti numbers from $\operatorname{Tor}$

Let $A, \mathfrak{m}$ be a local ring. For a projective resolution $P_{\bullet}$ of $M$, the $n$th Betti number of $M$ is
$$
\beta_{n}(M) = \dim_{A / \mathfrak{m}} H_{n}(P_{\bullet} \otimes A / \mathfrak{m}).
$$

---

We will see that this is an application of [[Commutative algebra --- math-189AA/notes/Tor-sion functor|the functor]] $\operatorname{Tor}$.