---
tags:
- comm-alg
- hom-alg
- math-189AA/19
---

Let $A$ be a ring.

##### _definition:_ projective dimension, minimal projective resolution

An $A$-module $M$ has **finite projective dimension** if there exists a projective resolution of finite length.

Its **projective dimension** $\operatorname{proj dim} M = n$ is the least such length $n$ such that there exists $P_{\bullet}$ is a projective resolution with $P_{m} = 0$ for all $m > n$.

Such a projective resolution of minimal length is called a **minimal projective resolution**.

If there is no such finite length projective resolution, we say $\operatorname{proj dim} M = \infty$.

---

##### _example:_ projective dimension $0$

An $A$-module $M$ has projective dimension $0$ if and only if it is projective. (Exactness of the augmented sequence would require $\varepsilon : P_{0} \to M$)

---

We should probably show that this really is a well-defined invariant of a module.

##### _proposition:_ projective dimension is an isomorphism invariant

For any two isomorphic $A$-modules $M \cong N$, we have $\operatorname{proj dim} M = \operatorname{proj dim} N$.

###### _proof sketch:_

For any projective resolution $P_{\bullet}$ of $M$ we can construct a projective resolution of $N$ of the same length
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & P_{2} \ar[r] & P_{1} \ar[r] & P_{0} \ar[rd, "\varepsilon_{N}"] \ar[r, "\varepsilon_{M}"] & M \ar[d, "\sim"] \ar[r] & 0 \\
		& & & & N
	\end{tikzcd}
\end{document}
```
---

The horseshoe lemma tells us further that projective dimension behaves well in short exact sequences.

##### _proposition:_ projective dimension in short exact sequences

Suppose
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
				0 \ar[r] & M' \ar[r] & M \ar[r] & M'' \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is exact. Then $\operatorname{proj} \dim M \leq \max \{ \operatorname{proj} \dim M', \operatorname{proj} \dim M'' \}$.

---


How do we construct a minimal projective resolution? Homological algebraists have done this for us already.

##### _theorem:_ constructing minimal projective resolutions

The projective resolution obtained by choosing the minimal free module [[#_proposition _ constructing a projective module|in the construction above]] is minimal.

---

##### _example:_ constructing a minimal projective resolution

Consider $(x)$ as a $\mathbb{Q}[x, y, z]$-module. The first surjection is just $\mathbb{Q}[x, y, z] \to (x)$ by $p \mapsto px$. Since $\mathbb{Q}[x, y, z]$ is an [[Abstract algebra --- math-171/notes/Integral domains#_definition _ integral domain|integral domain]], this has kernel $0$.

In general, this follows because every [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ principal ideal domain|principal ideal]] of an integral domain is isomorphic to the ring (as a module over the ring).

---